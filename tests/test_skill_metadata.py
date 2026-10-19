"""
Tests for SKILL.md frontmatter (Agent Skills specification limits).

Run from the skill root:
  pytest tests/test_skill_metadata.py -v
"""

import re
from pathlib import Path

ROOT = Path(__file__).parent.parent
SKILL = ROOT / "SKILL.md"

NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")


def parse_frontmatter() -> dict:
    """Parse the flat `key: value` / folded `key: >` frontmatter of SKILL.md."""
    text = SKILL.read_text(encoding="utf-8")
    match = re.match(r"^---\r?\n(.*?)\r?\n---\r?\n", text, re.S)
    assert match, "SKILL.md must start with a YAML frontmatter block"
    fields: dict = {}
    key = None
    for line in match.group(1).splitlines():
        top = re.match(r"^([A-Za-z][\w-]*):\s*(.*)$", line)
        if top:
            key, value = top.group(1), top.group(2).strip()
            fields[key] = "" if value in (">", "|") else value
        elif key and line.strip():
            fields[key] = (fields[key] + " " + line.strip()).strip()
    return fields


class TestSkillFrontmatter:
    def test_required_fields_present(self):
        fm = parse_frontmatter()
        assert fm.get("name")
        assert fm.get("description")

    def test_name_follows_spec(self):
        name = parse_frontmatter()["name"]
        assert len(name) <= 64
        assert NAME_RE.match(name), f"invalid name: {name!r}"

    def test_description_within_1024_chars(self):
        # Agent Skills spec limit. Issue #4 reports the Claude app rejecting the
        # upload over this limit; Claude Code (CLI) loaded the long description.
        description = parse_frontmatter()["description"]
        assert 1 <= len(description) <= 1024, f"description is {len(description)} chars"
