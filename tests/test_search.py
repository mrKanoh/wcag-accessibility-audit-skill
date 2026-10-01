"""
Tests for scripts/search.py

Run from the skill root:
  pytest tests/ -v
"""

import subprocess
import json
import sys
import csv
from pathlib import Path
import pytest

ROOT = Path(__file__).parent.parent
SCRIPT = ROOT / "scripts" / "search.py"
DATA = ROOT / "data"
PYTHON = sys.executable


def run(*args: str) -> subprocess.CompletedProcess:
    """Run search.py with the given arguments and return the result."""
    return subprocess.run(
        [PYTHON, str(SCRIPT), *args],
        capture_output=True,
        text=True,
        encoding='utf-8',
        cwd=ROOT,
    )


# ── CSV integrity ─────────────────────────────────────────────────────────────

class TestCSVIntegrity:
    """Verify every database CSV can be loaded and has expected columns."""

    EXPECTED_COLS = {
        "wcag-criteria.csv":          {"id", "level", "principle", "criterion"},
        "aria-patterns.csv":           {"component", "role", "keyboard"},
        "testing-tools.csv":           {"tool", "type", "platform", "free"},
        "screen-reader-keys.csv":      {"reader", "platform", "action", "key"},
        "kpis.csv":                    {"kpi", "category", "target"},
        "disability-models.csv":       {"model", "view_of_disability"},
        "typography-rules.csv":        {"rule", "category", "recommendation"},
        "color-palette-rules.csv":     {"rule", "scope"},
        "handoff-checklist.csv":       {"phase", "owner", "item"},
        "semantic-html.csv":           {"element", "role"},
        "glossary-es.csv":             {"en", "es"},
        "legal-framework.csv":         {"jurisdiction", "law"},
        "resources.csv":               {"Title", "URL", "Category"},
        "cognitive-accessibility.csv": {"pattern_id", "pattern_name", "user_group", "wcag_ref"},
    }

    @pytest.mark.parametrize("filename,required_cols", EXPECTED_COLS.items())
    def test_csv_loads_and_has_columns(self, filename: str, required_cols: set):
        path = DATA / filename
        assert path.exists(), f"Missing database: {filename}"
        with open(path, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            cols = set(reader.fieldnames or [])
            rows = list(reader)
        assert len(rows) > 0, f"{filename} is empty"
        missing = required_cols - cols
        assert not missing, f"{filename} missing columns: {missing}"


# ── Table output ──────────────────────────────────────────────────────────────

class TestTableOutput:
    def test_wcag_level_aa(self):
        r = run("wcag", "--level", "AA")
        assert r.returncode == 0
        assert "result(s)" in r.stdout
        # Should contain AA criteria
        assert "AA" in r.stdout

    def test_wcag_keyword_contrast(self):
        r = run("wcag", "--keyword", "contrast")
        assert r.returncode == 0
        assert "contrast" in r.stdout.lower()

    def test_wcag_id_filter(self):
        r = run("wcag", "--id", "1.4.3")
        assert r.returncode == 0
        assert "1.4.3" in r.stdout

    def test_aria_component_modal(self):
        r = run("aria", "--component", "modal")
        assert r.returncode == 0
        assert "modal" in r.stdout.lower()

    def test_tools_free_windows(self):
        r = run("tools", "--platform", "Windows", "--free")
        assert r.returncode == 0
        assert "result(s)" in r.stdout

    def test_keys_nvda_heading(self):
        r = run("keys", "--reader", "NVDA", "--action", "heading")
        assert r.returncode == 0
        assert "NVDA" in r.stdout

    def test_glossary_keyword(self):
        r = run("glossary", "--keyword", "contrast")
        assert r.returncode == 0

    def test_legal_eu(self):
        r = run("legal", "--jurisdiction", "EU")
        assert r.returncode == 0
        assert "European Union" in r.stdout

    def test_cognitive_keyword(self):
        r = run("cognitive", "--keyword", "memory")
        assert r.returncode == 0
        assert "result(s)" in r.stdout

    def test_no_results(self):
        r = run("wcag", "--keyword", "xyznonexistentterm12345")
        assert r.returncode == 0
        assert "No results" in r.stdout


# ── JSON output ───────────────────────────────────────────────────────────────

class TestJSONOutput:
    def test_wcag_json(self):
        r = run("wcag", "--level", "AA", "--output", "json")
        assert r.returncode == 0
        data = json.loads(r.stdout)
        assert isinstance(data, list)
        assert len(data) > 0
        assert "id" in data[0]
        assert "level" in data[0]

    def test_aria_json(self):
        r = run("aria", "--component", "modal", "--output", "json")
        assert r.returncode == 0
        data = json.loads(r.stdout)
        assert isinstance(data, list)

    def test_cognitive_json(self):
        r = run("cognitive", "--keyword", "memory", "--output", "json")
        assert r.returncode == 0
        data = json.loads(r.stdout)
        assert isinstance(data, list)
        assert all("pattern_id" in r for r in data)

    def test_tools_json_free(self):
        r = run("tools", "--free", "--output", "json")
        assert r.returncode == 0
        data = json.loads(r.stdout)
        assert all(d["free"].lower().startswith("true") for d in data)


# ── CSV output ────────────────────────────────────────────────────────────────

class TestCSVOutput:
    def test_wcag_csv_output(self):
        r = run("wcag", "--level", "A", "--output", "csv")
        assert r.returncode == 0
        lines = r.stdout.strip().splitlines()
        assert len(lines) >= 2  # header + at least 1 data row
        assert "id" in lines[0]
        assert "level" in lines[0]


# ── Export flag ───────────────────────────────────────────────────────────────

class TestExportFlag:
    def test_export_json(self, tmp_path):
        out = tmp_path / "output.json"
        r = run("wcag", "--level", "AA", "--output", "json", "--export", str(out))
        assert r.returncode == 0
        assert out.exists()
        data = json.loads(out.read_text(encoding="utf-8"))
        assert isinstance(data, list)
        assert len(data) > 0

    def test_export_table(self, tmp_path):
        out = tmp_path / "output.json"
        r = run("keys", "--reader", "NVDA", "--export", str(out))
        assert r.returncode == 0
        assert out.exists()
        data = json.loads(out.read_text(encoding="utf-8"))
        assert isinstance(data, list)


# ── Cross-database 'all' subcommand ──────────────────────────────────────────

class TestAllSubcommand:
    def test_all_finds_results(self):
        r = run("all", "--keyword", "contrast")
        assert r.returncode == 0
        # Should find results in multiple databases
        assert "result(s)" in r.stdout

    def test_all_json(self):
        r = run("all", "--keyword", "focus", "--output", "json")
        assert r.returncode == 0
        data = json.loads(r.stdout)
        assert isinstance(data, list)
        assert len(data) > 0
        # Each result has a _database field
        assert all("_database" in row for row in data)
        # Should span multiple databases
        dbs = {row["_database"] for row in data}
        assert len(dbs) > 1

    def test_all_no_results(self):
        r = run("all", "--keyword", "xyznonexistentterm99999")
        assert r.returncode == 0
        assert "No results" in r.stdout


# ── Edge cases ────────────────────────────────────────────────────────────────

class TestEdgeCases:
    def test_missing_subcommand_exits_nonzero(self):
        r = run()
        assert r.returncode != 0

    def test_wcag_principle_filter(self):
        r = run("wcag", "--principle", "Perceivable", "--output", "json")
        assert r.returncode == 0
        data = json.loads(r.stdout)
        assert all("Perceivable" in d["principle"] for d in data)

    def test_tools_type_filter(self):
        r = run("tools", "--type", "screen-reader", "--output", "json")
        assert r.returncode == 0
        data = json.loads(r.stdout)
        assert all("screen-reader" in d["type"].lower() for d in data)

    def test_kpis_category(self):
        r = run("kpis", "--category", "Technical", "--output", "json")
        assert r.returncode == 0
        data = json.loads(r.stdout)
        assert all("Technical" in d["category"] for d in data)

    def test_models_keyword(self):
        r = run("models", "--keyword", "social")
        assert r.returncode == 0
        assert "social" in r.stdout.lower()


# ── WCAG 3 draft status notice (draft records retired) ───────────────────────

W3C_DRAFT = "https://www.w3.org/TR/wcag-3.0/"
W3C_INTRO = "https://www.w3.org/WAI/standards-guidelines/wcag/wcag3-intro/"


class TestWcag3Notice:
    """`wcag3` returns only a draft-status notice; no invented criteria."""

    def test_csv_removed(self):
        assert not (DATA / "wcag3-draft.csv").exists()

    def test_table_output_is_notice(self):
        r = run("wcag3")
        assert r.returncode == 0
        assert W3C_DRAFT in r.stdout and W3C_INTRO in r.stdout
        assert "not a standard" in r.stdout
        assert "result(s)" not in r.stdout

    def test_json_output_is_object_without_records(self):
        r = run("wcag3", "--output", "json")
        assert r.returncode == 0
        data = json.loads(r.stdout)
        assert isinstance(data, dict)
        assert data["status"] == "draft-records-retired"
        assert data["records"] == []
        assert data["draft_url"] == W3C_DRAFT
        assert data["intro_url"] == W3C_INTRO
        assert data["ignored_arguments"] == []

    def test_legacy_level_bronze_ignored_table(self):
        r = run("wcag3", "--level", "Bronze")
        assert r.returncode == 0
        assert "Ignored arguments: --level" in r.stdout
        assert "Lc " not in r.stdout and "3.1.1" not in r.stdout

    def test_legacy_arguments_ignored_json(self):
        r = run("wcag3", "--level", "Bronze", "--category", "Focus",
                "--keyword", "APCA", "--output", "json")
        assert r.returncode == 0
        data = json.loads(r.stdout)
        assert data["records"] == []
        assert data["ignored_arguments"] == ["--level", "--category", "--keyword"]

    def test_csv_output_is_single_notice_row(self):
        r = run("wcag3", "--output", "csv")
        assert r.returncode == 0
        rows = list(csv.DictReader(r.stdout.splitlines()))
        assert len(rows) == 1
        assert rows[0]["status"] == "draft-records-retired"

    def test_all_search_returns_no_wcag3_records(self):
        # "Bronze" appears in no remaining database: `all` prints its no-results message.
        r = run("all", "--keyword", "Bronze", "--output", "json")
        assert r.returncode == 0
        assert r.stdout.strip() == "No results for 'Bronze' in any database."

        # A common term still hits other databases: non-empty JSON, none from wcag3.
        r = run("all", "--keyword", "contrast", "--output", "json")
        assert r.returncode == 0
        rows = json.loads(r.stdout)
        assert rows, "expected 'contrast' hits from the remaining databases"
        assert all(row["_database"] != "wcag3" for row in rows)

    def test_mcp_resource_matches_cli_notice(self, monkeypatch):
        """Load mcp-server.py with a stubbed `mcp` package (dependency not required)."""
        import importlib.util
        import types

        class FakeFastMCP:
            def __init__(self, *_a, **_k):
                pass

            def resource(self, _uri):
                return lambda fn: fn

        pkg = types.ModuleType("mcp")
        server = types.ModuleType("mcp.server")
        fast = types.ModuleType("mcp.server.fastmcp")
        fast.FastMCP = FakeFastMCP
        for name, mod in (("mcp", pkg), ("mcp.server", server), ("mcp.server.fastmcp", fast)):
            monkeypatch.setitem(sys.modules, name, mod)

        spec = importlib.util.spec_from_file_location("mcp_server_under_test", ROOT / "scripts" / "mcp-server.py")
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        resource = json.loads(module.get_wcag3_draft())
        cli = json.loads(run("wcag3", "--output", "json").stdout)
        cli.pop("ignored_arguments")
        assert resource == cli
        assert resource["records"] == []
