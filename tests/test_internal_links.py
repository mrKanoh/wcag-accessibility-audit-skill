"""
Internal link checks for the skill's Markdown entry points.

- Every relative Markdown link in SKILL.md, README.md, README-es.md and
  references/*.md points to an existing file or directory, and every
  #anchor points to a heading of the target Markdown file (GitHub slug rules).
- Every repository path that SKILL.md quotes in backticks (references/,
  templates/, prompts/, data/, examples/, scripts/) exists, so the task map
  never sends the agent to a missing file.

Run from the skill root:
  pytest tests/test_internal_links.py -v
"""

import re
from pathlib import Path

import pytest

ROOT = Path(__file__).parent.parent

DOCS = sorted(
    [ROOT / "SKILL.md", ROOT / "README.md", ROOT / "README-es.md"]
    + list((ROOT / "references").glob("*.md"))
)

LINK_RE = re.compile(r"(?<!!)\[(?:[^\]]*)\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
FENCE_RE = re.compile(r"^\s*(```|~~~)")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.*?)\s*#*\s*$")
PATH_PREFIXES = ("references/", "templates/", "prompts/", "data/", "examples/", "scripts/")
BACKTICK_PATH_RE = re.compile(r"`((?:%s)[^`\s]*)`" % "|".join(re.escape(p) for p in PATH_PREFIXES))


def prose_lines(path: Path):
    """Yield (line_number, line) outside fenced code blocks."""
    in_fence = False
    for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if FENCE_RE.match(line):
            in_fence = not in_fence
            continue
        if not in_fence:
            yield number, line


def github_slug(heading: str) -> str:
    """Approximate GitHub's heading anchor: rendered text, lowercased,
    punctuation and symbols dropped, spaces turned into hyphens."""
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", heading)  # links -> text
    text = text.replace("`", "").replace("*", "")
    text = text.strip().lower()
    text = re.sub(r"[^\w\- ]", "", text)
    return text.replace(" ", "-")


def anchors(path: Path) -> set:
    seen: dict = {}
    result = set()
    for _, line in prose_lines(path):
        match = HEADING_RE.match(line)
        if not match:
            continue
        slug = github_slug(match.group(2))
        count = seen.get(slug, 0)
        seen[slug] = count + 1
        result.add(slug if count == 0 else f"{slug}-{count}")
    return result


def relative_links(path: Path):
    for number, line in prose_lines(path):
        for target in LINK_RE.findall(line):
            if re.match(r"^[a-z][a-z0-9+.-]*:", target, re.I):  # http:, https:, mailto:
                continue
            yield number, target


@pytest.mark.parametrize("doc", DOCS, ids=lambda p: str(p.relative_to(ROOT)))
def test_relative_links_resolve(doc: Path):
    broken = []
    for number, target in relative_links(doc):
        file_part, _, anchor = target.partition("#")
        dest = (doc.parent / file_part).resolve() if file_part else doc
        if not dest.exists():
            broken.append(f"{doc.name}:{number} -> {target} (missing file)")
            continue
        if anchor and dest.suffix == ".md" and anchor not in anchors(dest):
            broken.append(f"{doc.name}:{number} -> {target} (missing anchor)")
    assert not broken, "\n".join(broken)


def test_skill_backtick_paths_exist():
    skill = ROOT / "SKILL.md"
    missing = []
    for number, line in prose_lines(skill):
        for raw in BACKTICK_PATH_RE.findall(line):
            if "*" in raw or "<" in raw:  # globs and placeholders such as data/*.csv
                continue
            if not (ROOT / raw.rstrip("/")).exists():
                missing.append(f"SKILL.md:{number} -> {raw}")
    assert not missing, "\n".join(missing)


def test_slug_rules():
    assert github_slug("Accessible Drag & Drop (WCAG 2.5.7)") == "accessible-drag--drop-wcag-257"
    assert github_slug("Svelte 5 — Modal dialog with native `<dialog>`") == "svelte-5--modal-dialog-with-native-dialog"
    assert github_slug("What it does") == "what-it-does"
