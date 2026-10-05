#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
wcag-accessibility skill search utility.

Search the CSV databases by keyword, WCAG level, component, or tool type.

Usage:
  python search.py wcag --level AA
  python search.py wcag --keyword contrast --output json
  python search.py wcag --principle Perceivable --export results.json
  python search.py aria --component modal --detail
  python search.py tools --type screen-reader --platform Windows --free
  python search.py keys --reader NVDA --action heading
  python search.py cognitive --keyword memory
  python search.py all --keyword contrast            # cross-database search
  python search.py resources --category "Official Standards" --url
  python search.py legal --jurisdiction EU
"""

import csv
import sys
import json
import argparse
import os
import io
from pathlib import Path

# Force UTF-8 output on Windows (cp1252 can't encode many a11y symbols)
if sys.stdout.encoding and sys.stdout.encoding.lower() not in ('utf-8', 'utf-8-sig'):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

DATA_DIR = Path(__file__).parent.parent / "data"

WCAG_CSV       = DATA_DIR / "wcag-criteria.csv"
ARIA_CSV       = DATA_DIR / "aria-patterns.csv"
TOOLS_CSV      = DATA_DIR / "testing-tools.csv"
KEYS_CSV       = DATA_DIR / "screen-reader-keys.csv"
KPIS_CSV       = DATA_DIR / "kpis.csv"
MODELS_CSV     = DATA_DIR / "disability-models.csv"
TYPOGRAPHY_CSV = DATA_DIR / "typography-rules.csv"
COLOR_CSV      = DATA_DIR / "color-palette-rules.csv"
HANDOFF_CSV    = DATA_DIR / "handoff-checklist.csv"
SEMANTIC_CSV   = DATA_DIR / "semantic-html.csv"
GLOSSARY_CSV   = DATA_DIR / "glossary-es.csv"
LEGAL_CSV      = DATA_DIR / "legal-framework.csv"
RESOURCES_CSV  = DATA_DIR / "resources.csv"
COGNITIVE_CSV  = DATA_DIR / "cognitive-accessibility.csv"

# All databases for cross-search
ALL_DATABASES = {
    "wcag":        WCAG_CSV,
    "aria":        ARIA_CSV,
    "tools":       TOOLS_CSV,
    "keys":        KEYS_CSV,
    "kpis":        KPIS_CSV,
    "models":      MODELS_CSV,
    "typography":  TYPOGRAPHY_CSV,
    "color":       COLOR_CSV,
    "handoff":     HANDOFF_CSV,
    "semantic":    SEMANTIC_CSV,
    "glossary":    GLOSSARY_CSV,
    "legal":       LEGAL_CSV,
    "resources":   RESOURCES_CSV,
    "cognitive":   COGNITIVE_CSV,
}

# ── ANSI colors (disabled by NO_COLOR env var or non-TTY) ────────────────────
_USE_COLOR = sys.stdout.isatty() and not os.environ.get("NO_COLOR")

def _c(code: str, text: str) -> str:
    return f"\033[{code}m{text}\033[0m" if _USE_COLOR else text

def green(t):  return _c("32", t)
def cyan(t):   return _c("36", t)
def bold(t):   return _c("1",  t)
def yellow(t): return _c("33", t)
def dim(t):    return _c("2",  t)


def load_csv(path: Path) -> list[dict]:
    if not path.exists():
        print(f"Warning: database not found: {path}", file=sys.stderr)
        return []
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


# Metadato de versión del catálogo WCAG (`wcag-criteria.csv`): se expone en JSON, pero no
# participa en `--keyword` (de lo contrario "2.1" o "2.2" coincidirían con casi todas las filas).
WCAG_METADATA_FIELDS = ("versions",)


def matches(row: dict, keyword: str, ignore: tuple[str, ...] = ()) -> bool:
    keyword = keyword.lower()
    return any(keyword in str(v).lower() for k, v in row.items() if k not in ignore)


# ── Output helpers ────────────────────────────────────────────────────────────

def print_table(rows: list[dict], columns: list[str], export: str | None = None) -> None:
    if not rows:
        print("No results found.")
        return

    widths = {col: len(col) for col in columns}
    for row in rows:
        for col in columns:
            widths[col] = max(widths[col], len(str(row.get(col, ""))))

    header = "  ".join(bold(col.ljust(widths[col])) for col in columns)
    separator = dim("  ".join("-" * widths[col] for col in columns))
    print(header)
    print(separator)
    for row in rows:
        print("  ".join(str(row.get(col, "")).ljust(widths[col]) for col in columns))
    print(f"\n{cyan(str(len(rows)))} result(s)")

    if export:
        _export_rows(rows, export)


def print_json(rows: "list[dict] | dict", export: str | None = None) -> None:
    output = json.dumps(rows, ensure_ascii=False, indent=2)
    print(output)
    if export:
        _export_text(output, export)


def print_csv_out(rows: list[dict], columns: list[str], export: str | None = None) -> None:
    import io
    buf = io.StringIO()
    writer = csv.DictWriter(buf, fieldnames=columns, extrasaction="ignore")
    writer.writeheader()
    writer.writerows(rows)
    text = buf.getvalue()
    print(text)
    if export:
        _export_text(text, export)


def _export_rows(rows: list[dict], path: str) -> None:
    _export_text(json.dumps(rows, ensure_ascii=False, indent=2), path)


def _export_text(text: str, path: str) -> None:
    Path(path).write_text(text, encoding="utf-8")
    print(dim(f"  → Exported to {path}"), file=sys.stderr)


def render(rows: list[dict], columns: list[str], fmt: str, export: str | None) -> None:
    if fmt == "json":
        print_json(rows, export)
    elif fmt == "csv":
        print_csv_out(rows, columns, export)
    else:
        print_table(rows, columns, export)


# ── WCAG ──────────────────────────────────────────────────────────────────────

def cmd_wcag(args: argparse.Namespace) -> None:
    rows = load_csv(WCAG_CSV)
    if args.level:
        rows = [r for r in rows if r["level"].upper() == args.level.upper()]
    if args.principle:
        rows = [r for r in rows if args.principle.lower() in r["principle"].lower()]
    if args.keyword:
        rows = [r for r in rows if matches(r, args.keyword, ignore=WCAG_METADATA_FIELDS)]
    if args.id:
        rows = [r for r in rows if r["id"].startswith(args.id)]

    cols = ["id", "level", "principle", "criterion", "description"]
    render(rows, cols, args.output, args.export)

    if args.url and rows and args.output == "table":
        print()
        for r in rows:
            print(f"  {r['id']} → {green(r['url'])}")


# ── WCAG 3.0 Draft (status notice only) ──────────────────────────────────────

WCAG3_DRAFT_URL = "https://www.w3.org/TR/wcag-3.0/"
WCAG3_INTRO_URL = "https://www.w3.org/WAI/standards-guidelines/wcag/wcag3-intro/"
WCAG3_NOTICE = {
    "status": "draft-records-retired",
    "message": (
        "WCAG 3 is an incomplete W3C Working Draft and not a standard; WCAG 2.x remains "
        "the compliance target. The retired data file assigned fixed criterion IDs and APCA "
        "thresholds that the W3C draft does not support (Bronze appears there only as a "
        "proposed reporting tier), so no criteria are returned."
    ),
    "draft_url": WCAG3_DRAFT_URL,
    "intro_url": WCAG3_INTRO_URL,
    "records": [],
}


def cmd_wcag3(args: argparse.Namespace) -> None:
    ignored = [f"--{n}" for n in ("level", "category", "keyword") if getattr(args, n)]
    if args.output == "json":
        print_json({**WCAG3_NOTICE, "ignored_arguments": ignored}, args.export)
        return
    if args.output == "csv":
        cols = ["status", "message", "draft_url", "intro_url"]
        print_csv_out([WCAG3_NOTICE], cols, args.export)
        return
    print(bold("WCAG 3: draft status (no criteria available)"))
    print(WCAG3_NOTICE["message"])
    if ignored:
        print(f"Ignored arguments: {' '.join(ignored)}")
    print(f"Draft:        {green(WCAG3_DRAFT_URL)}")
    print(f"Introduction: {green(WCAG3_INTRO_URL)}")
    if args.export:
        _export_text(json.dumps(WCAG3_NOTICE, ensure_ascii=False, indent=2), args.export)


# ── ARIA ──────────────────────────────────────────────────────────────────────

def cmd_aria(args: argparse.Namespace) -> None:
    rows = load_csv(ARIA_CSV)
    if args.component:
        rows = [r for r in rows if args.component.lower() in r["component"].lower()]
    if args.keyword:
        rows = [r for r in rows if matches(r, args.keyword)]

    cols = ["component", "role", "required_aria", "keyboard", "focus_management"]
    render(rows, cols, args.output, args.export)

    if args.detail and rows and args.output == "table":
        print()
        for r in rows:
            print(f"\n{bold('── ' + r['component'] + ' ──')}")
            for k, v in r.items():
                if v:
                    print(f"  {cyan(k)}: {v}")


# ── TOOLS ─────────────────────────────────────────────────────────────────────

def cmd_tools(args: argparse.Namespace) -> None:
    rows = load_csv(TOOLS_CSV)
    if args.type:
        rows = [r for r in rows if args.type.lower() in r["type"].lower()]
    if args.platform:
        rows = [r for r in rows if args.platform.lower() in r["platform"].lower()]
    if args.browser:
        rows = [r for r in rows if args.browser.lower() in r["browser"].lower()]
    if args.free:
        rows = [r for r in rows if r["free"].lower().startswith("true")]
    if args.keyword:
        rows = [r for r in rows if matches(r, args.keyword)]

    cols = ["tool", "type", "platform", "browser", "free", "best_for"]
    render(rows, cols, args.output, args.export)

    if args.url and rows and args.output == "table":
        print()
        for r in rows:
            print(f"  {r['tool']} → {green(r['url'])}")


# ── SCREEN READER KEYS ────────────────────────────────────────────────────────

def cmd_keys(args: argparse.Namespace) -> None:
    rows = load_csv(KEYS_CSV)
    if args.reader:
        rows = [r for r in rows if args.reader.lower() in r["reader"].lower()]
    if args.platform:
        rows = [r for r in rows if args.platform.lower() in r["platform"].lower()]
    if args.mode:
        rows = [r for r in rows if args.mode.lower() in r["mode"].lower()]
    if args.action:
        rows = [r for r in rows if args.action.lower() in r["action"].lower()]

    cols = ["reader", "platform", "mode", "action", "key"]
    render(rows, cols, args.output, args.export)


# ── KPIs ──────────────────────────────────────────────────────────────────────

def cmd_kpis(args: argparse.Namespace) -> None:
    rows = load_csv(KPIS_CSV)
    if args.category:
        rows = [r for r in rows if args.category.lower() in r["category"].lower()]
    if args.keyword:
        rows = [r for r in rows if matches(r, args.keyword)]
    cols = ["kpi", "category", "target", "cadence", "formula"]
    render(rows, cols, args.output, args.export)


# ── DISABILITY MODELS ─────────────────────────────────────────────────────────

def cmd_models(args: argparse.Namespace) -> None:
    rows = load_csv(MODELS_CSV)
    if args.keyword:
        rows = [r for r in rows if matches(r, args.keyword)]
    cols = ["model", "focus", "view_of_disability", "design_implication"]
    render(rows, cols, args.output, args.export)


# ── TYPOGRAPHY ────────────────────────────────────────────────────────────────

def cmd_typography(args: argparse.Namespace) -> None:
    rows = load_csv(TYPOGRAPHY_CSV)
    if args.category:
        rows = [r for r in rows if args.category.lower() in r["category"].lower()]
    if args.keyword:
        rows = [r for r in rows if matches(r, args.keyword)]
    cols = ["rule", "category", "recommendation", "wcag_ref"]
    render(rows, cols, args.output, args.export)


# ── COLOR PALETTE ─────────────────────────────────────────────────────────────

def cmd_color(args: argparse.Namespace) -> None:
    rows = load_csv(COLOR_CSV)
    if args.scope:
        rows = [r for r in rows if args.scope.lower() in r["scope"].lower()]
    if args.keyword:
        rows = [r for r in rows if matches(r, args.keyword)]
    cols = ["rule", "scope", "recommendation", "wcag_ref", "tool"]
    render(rows, cols, args.output, args.export)


# ── HANDOFF ───────────────────────────────────────────────────────────────────

def cmd_handoff(args: argparse.Namespace) -> None:
    rows = load_csv(HANDOFF_CSV)
    if args.phase:
        rows = [r for r in rows if args.phase.lower() in r["phase"].lower()]
    if args.owner:
        rows = [r for r in rows if args.owner.lower() in r["owner"].lower()]
    if args.keyword:
        rows = [r for r in rows if matches(r, args.keyword)]
    cols = ["phase", "owner", "item", "artifact"]
    render(rows, cols, args.output, args.export)


# ── SEMANTIC HTML ─────────────────────────────────────────────────────────────

def cmd_semantic(args: argparse.Namespace) -> None:
    rows = load_csv(SEMANTIC_CSV)
    if args.element:
        rows = [r for r in rows if args.element.lower() in r["element"].lower()]
    if args.keyword:
        rows = [r for r in rows if matches(r, args.keyword)]
    cols = ["element", "role", "use_for", "avoid_when"]
    render(rows, cols, args.output, args.export)


# ── GLOSSARY (ES↔EN) ─────────────────────────────────────────────────────────

def cmd_glossary(args: argparse.Namespace) -> None:
    rows = load_csv(GLOSSARY_CSV)
    if args.keyword:
        rows = [r for r in rows if matches(r, args.keyword)]
    if args.context:
        rows = [r for r in rows if args.context.lower() in r["contexto"].lower()]
    cols = ["en", "es", "definicion", "contexto"]
    render(rows, cols, args.output, args.export)


# ── LEGAL FRAMEWORK ────────────────────────────────────────────────────────────

def cmd_legal(args: argparse.Namespace) -> None:
    rows = load_csv(LEGAL_CSV)
    if args.jurisdiction:
        rows = [r for r in rows if args.jurisdiction.lower() in r["jurisdiction"].lower()]
    if args.keyword:
        rows = [r for r in rows if matches(r, args.keyword)]
    cols = ["jurisdiction", "law", "standard_referenced", "effective", "scope"]
    render(rows, cols, args.output, args.export)


# ── RESOURCES ─────────────────────────────────────────────────────────────────

def cmd_resources(args: argparse.Namespace) -> None:
    rows = load_csv(RESOURCES_CSV)
    if args.category:
        rows = [r for r in rows if args.category.lower() in r["Category"].lower()]
    if args.type:
        rows = [r for r in rows if args.type.lower() in r["Type"].lower()]
    if args.authority:
        rows = [r for r in rows if args.authority.lower() in r["Authority"].lower()]
    if args.language:
        rows = [r for r in rows if args.language.lower() in r["Language"].lower()]
    if args.year:
        rows = [r for r in rows if args.year in r["Year"]]
    if args.keyword:
        rows = [r for r in rows if matches(r, args.keyword)]

    cols = ["Category", "Title", "Type", "Authority", "Year"]
    render(rows, cols, args.output, args.export)

    if args.url and rows and args.output == "table":
        print()
        for r in rows:
            print(f"  {r['Title']} -> {green(r['URL'])}")


# ── COGNITIVE ACCESSIBILITY ───────────────────────────────────────────────────

def cmd_cognitive(args: argparse.Namespace) -> None:
    rows = load_csv(COGNITIVE_CSV)
    if args.user_group:
        rows = [r for r in rows if args.user_group.lower() in r["user_group"].lower()]
    if args.wcag_ref:
        rows = [r for r in rows if args.wcag_ref.lower() in r["wcag_ref"].lower()]
    if args.keyword:
        rows = [r for r in rows if matches(r, args.keyword)]
    cols = ["pattern_id", "pattern_name", "user_group", "wcag_ref", "coga_objective", "design_guidance"]
    render(rows, cols, args.output, args.export)


# ── ALL (cross-database search) ───────────────────────────────────────────────

def cmd_all(args: argparse.Namespace) -> None:
    keyword = args.keyword
    combined: list[dict] = []
    for db_name, csv_path in ALL_DATABASES.items():
        rows = load_csv(csv_path)
        ignore = WCAG_METADATA_FIELDS if db_name == "wcag" else ()
        hits = [r for r in rows if matches(r, keyword, ignore=ignore)]
        for r in hits:
            r["_database"] = db_name
        combined.extend(hits)

    if not combined:
        print(f"No results for '{keyword}' in any database.")
        return

    if args.output == "json":
        print_json(combined, args.export)
    else:
        # Group by database for readability
        by_db: dict[str, list] = {}
        for r in combined:
            by_db.setdefault(r["_database"], []).append(r)

        for db_name, rows in by_db.items():
            print(f"\n{bold(yellow(f'── {db_name.upper()} ({len(rows)} hit(s)) ──'))}")
            cols = [k for k in rows[0].keys() if k != "_database"][:5]
            print_table(rows, cols)

        if args.export:
            _export_rows(combined, args.export)


# ── CLI ───────────────────────────────────────────────────────────────────────

def add_common_args(p: argparse.ArgumentParser) -> None:
    """Add --output and --export flags to a subcommand parser."""
    p.add_argument(
        "--output", choices=["table", "json", "csv"], default="table",
        help="Output format (default: table)"
    )
    p.add_argument(
        "--export", metavar="FILE",
        help="Save results to file (JSON for table/json, CSV for csv)"
    )


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Search the WCAG Accessibility skill databases.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    sub = parser.add_subparsers(dest="command", required=True)

    # wcag
    p_wcag = sub.add_parser("wcag", help="Search WCAG criteria")
    p_wcag.add_argument("--level", help="A, AA, or AAA")
    p_wcag.add_argument("--principle", help="Perceivable / Operable / Understandable / Robust")
    p_wcag.add_argument("--keyword", help="Search across all fields")
    p_wcag.add_argument("--id", help="Criterion ID prefix (e.g. 1.4 or 2.1.1)")
    p_wcag.add_argument("--url", action="store_true", help="Show understanding URLs")
    add_common_args(p_wcag)

    # wcag3
    p_wcag3 = sub.add_parser("wcag3", help="WCAG 3.0 draft status and W3C links (no criteria)")
    p_wcag3.add_argument("--level", help="Deprecated, ignored (draft records were retired)")
    p_wcag3.add_argument("--category", help="Deprecated, ignored")
    p_wcag3.add_argument("--keyword", help="Deprecated, ignored")
    add_common_args(p_wcag3)

    # aria
    p_aria = sub.add_parser("aria", help="Search ARIA component patterns")
    p_aria.add_argument("--component", help="Component name (e.g. modal, button, tabs)")
    p_aria.add_argument("--keyword", help="Search across all fields")
    p_aria.add_argument("--detail", action="store_true", help="Show full detail for each result")
    add_common_args(p_aria)

    # tools
    p_tools = sub.add_parser("tools", help="Search testing tools")
    p_tools.add_argument("--type", help="browser-extension / cli / screen-reader / mobile / color")
    p_tools.add_argument("--platform", help="Windows / macOS / Android / iOS / Any")
    p_tools.add_argument("--browser", help="Chrome / Firefox / Edge / Safari / Any")
    p_tools.add_argument("--free", action="store_true", help="Free tools only")
    p_tools.add_argument("--keyword", help="Search across all fields")
    p_tools.add_argument("--url", action="store_true", help="Show tool URLs")
    add_common_args(p_tools)

    # keys
    p_keys = sub.add_parser("keys", help="Search screen reader keyboard shortcuts")
    p_keys.add_argument("--reader", help="NVDA / JAWS / VoiceOver / TalkBack / Narrator")
    p_keys.add_argument("--platform", help="Windows / macOS / iOS / Android")
    p_keys.add_argument("--mode", help="Browse / Forms / Table / General / Web")
    p_keys.add_argument("--action", help="Keyword in action name (e.g. heading, link, table)")
    add_common_args(p_keys)

    # kpis
    p_kpis = sub.add_parser("kpis", help="Search accessibility KPIs")
    p_kpis.add_argument("--category", help="Technical / Conformance / Remediation / User Outcome")
    p_kpis.add_argument("--keyword", help="Search across all fields")
    add_common_args(p_kpis)

    # models
    p_models = sub.add_parser("models", help="Search theoretical models of disability")
    p_models.add_argument("--keyword", help="Search across all fields")
    add_common_args(p_models)

    # typography
    p_type = sub.add_parser("typography", help="Search accessible typography rules")
    p_type.add_argument("--category", help="Size / Spacing / Layout / Responsive / Contrast")
    p_type.add_argument("--keyword", help="Search across all fields")
    add_common_args(p_type)

    # color
    p_color = sub.add_parser("color", help="Search color palette rules")
    p_color.add_argument("--scope", help="Text / Non-text / Meaning / System / Theme")
    p_color.add_argument("--keyword", help="Search across all fields")
    add_common_args(p_color)

    # handoff
    p_hand = sub.add_parser("handoff", help="Search design-to-dev a11y handoff checklist")
    p_hand.add_argument("--phase", help="Research / Design / Development / QA / Release")
    p_hand.add_argument("--owner", help="UX / Designer / Dev / QA / PM")
    p_hand.add_argument("--keyword", help="Search across all fields")
    add_common_args(p_hand)

    # semantic
    p_sem = sub.add_parser("semantic", help="Search semantic HTML element reference")
    p_sem.add_argument("--element", help="Element name (e.g. nav, button, table)")
    p_sem.add_argument("--keyword", help="Search across all fields")
    add_common_args(p_sem)

    # glossary
    p_gloss = sub.add_parser("glossary", help="Spanish <-> English accessibility glossary")
    p_gloss.add_argument("--keyword", help="Search term in English or Spanish")
    p_gloss.add_argument("--context", help="Context category (e.g. ARIA / Legal / AT)")
    add_common_args(p_gloss)

    # legal
    p_legal = sub.add_parser("legal", help="Legal frameworks by jurisdiction")
    p_legal.add_argument("--jurisdiction", help="Country or region (e.g. Spain, Brazil, EU, US)")
    p_legal.add_argument("--keyword", help="Search across all fields")
    add_common_args(p_legal)

    # resources
    p_res = sub.add_parser("resources", help="Search curated resources (books, blogs, research, tools)")
    p_res.add_argument("--category", help="Category (e.g. Official Standards, Blogs, Research)")
    p_res.add_argument("--type", help="Type (e.g. Blog, Tool, Specification, Research)")
    p_res.add_argument("--authority", help="Authority (e.g. W3C, WebAIM, Deque, IAAP)")
    p_res.add_argument("--language", help="Language code (EN, ES, FR, etc.)")
    p_res.add_argument("--year", help="Year filter (e.g. 2024, 2025)")
    p_res.add_argument("--keyword", help="Search across all fields")
    p_res.add_argument("--url", action="store_true", help="Show resource URLs")
    add_common_args(p_res)

    # cognitive  ← NEW
    p_cog = sub.add_parser("cognitive", help="Search cognitive accessibility patterns (COGA)")
    p_cog.add_argument("--user-group", dest="user_group", help="e.g. ADHD / Dyslexia / Anxiety")
    p_cog.add_argument("--wcag-ref", dest="wcag_ref", help="WCAG SC reference (e.g. 3.3.7)")
    p_cog.add_argument("--keyword", help="Search across all fields")
    add_common_args(p_cog)

    # all  ← NEW: cross-database search
    p_all = sub.add_parser("all", help="Search across ALL 14 databases simultaneously")
    p_all.add_argument("--keyword", required=True, help="Search term")
    add_common_args(p_all)

    args = parser.parse_args()

    dispatch = {
        "wcag":       cmd_wcag,
        "wcag3":      cmd_wcag3,
        "aria":       cmd_aria,
        "tools":      cmd_tools,
        "keys":       cmd_keys,
        "kpis":       cmd_kpis,
        "models":     cmd_models,
        "typography": cmd_typography,
        "color":      cmd_color,
        "handoff":    cmd_handoff,
        "semantic":   cmd_semantic,
        "glossary":   cmd_glossary,
        "legal":      cmd_legal,
        "resources":  cmd_resources,
        "cognitive":  cmd_cognitive,
        "all":        cmd_all,
    }
    dispatch[args.command](args)


if __name__ == "__main__":
    main()
