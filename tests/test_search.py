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
    """Verify database headers and that every row has the same field count."""

    EXPECTED_COLS = {
        "wcag-criteria.csv":          {"id", "level", "principle", "criterion", "versions"},
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
        for row_number, row in enumerate(rows, start=2):
            assert None not in row, (
                f"{filename}: row {row_number} has extra fields: {row.get(None)!r}"
            )
            missing_values = [column for column, value in row.items() if value is None]
            assert not missing_values, (
                f"{filename}: row {row_number} is missing fields: {missing_values}"
            )


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


# ── Metadatos de versión del catálogo WCAG (D2-1) ─────────────────────────

# Criterios añadidos en WCAG 2.2 (W3C: https://www.w3.org/TR/WCAG22/). 4.1.1 Parsing existe en
# WCAG 2.1 y está marcado «Obsolete and removed» en 2.2.
ADDED_IN_22 = {"2.4.11", "2.4.12", "2.4.13", "2.5.7", "2.5.8", "3.2.6", "3.3.7", "3.3.8", "3.3.9"}
REMOVED_IN_22 = {"4.1.1"}


def wcag_rows() -> list[dict]:
    with open(DATA / "wcag-criteria.csv", newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


class TestWcagVersionMetadata:
    """La columna `versions` clasifica cada fila; no es un catálogo completo de WCAG (faltan los 28 AAA de 2.1)."""

    def test_catalogo_conserva_59_ids_sin_duplicados(self):
        ids = [r["id"] for r in wcag_rows()]
        assert len(ids) == 59
        assert len(set(ids)) == 59

    def test_clasificacion_de_cada_fila(self):
        for row in wcag_rows():
            if row["id"] in REMOVED_IN_22:
                expected = "2.1"
            elif row["id"] in ADDED_IN_22:
                expected = "2.2"
            else:
                expected = "2.1;2.2"
            assert row["versions"] == expected, row["id"]

    def test_conteos_por_clasificacion(self):
        counts: dict[str, int] = {}
        for row in wcag_rows():
            counts[row["versions"]] = counts.get(row["versions"], 0) + 1
        assert counts == {"2.1;2.2": 49, "2.1": 1, "2.2": 9}

    def test_columna_versions_es_la_ultima(self):
        with open(DATA / "wcag-criteria.csv", newline="", encoding="utf-8") as f:
            assert (csv.reader(f).__next__())[-1] == "versions"

    @pytest.mark.parametrize("criterion_id,versions", [("4.1.1", "2.1"), ("2.5.8", "2.2"), ("1.4.3", "2.1;2.2")])
    def test_json_expone_versions(self, criterion_id, versions):
        r = run("wcag", "--id", criterion_id, "--output", "json")
        assert r.returncode == 0
        data = json.loads(r.stdout)
        assert [(d["id"], d["versions"]) for d in data] == [(criterion_id, versions)]

    def test_csv_conserva_sus_cinco_columnas(self):
        r = run("wcag", "--level", "A", "--output", "csv")
        assert r.returncode == 0
        header = r.stdout.splitlines()[0]
        assert header == "id,level,principle,criterion,description"
        assert "versions" not in r.stdout

    def test_tabla_no_muestra_versions(self):
        r = run("wcag", "--id", "4.1.1")
        assert r.returncode == 0
        assert "versions" not in r.stdout

    def test_level_sin_version_no_cambia(self):
        data = json.loads(run("wcag", "--level", "A", "--output", "json").stdout)
        assert len(data) == 32
        assert "4.1.1" in {d["id"] for d in data}  # sin --wcag-version no se filtra por versión

    def test_exportacion_json_incluye_versions(self, tmp_path):
        out = tmp_path / "wcag.json"
        r = run("wcag", "--id", "4.1.1", "--output", "json", "--export", str(out))
        assert r.returncode == 0
        assert json.loads(out.read_text(encoding="utf-8"))[0]["versions"] == "2.1"


class TestKeywordIgnoresVersions:
    """`versions` no participa en --keyword (línea base anterior al cambio de columna)."""

    def test_keyword_2_1_en_wcag(self):
        ids = [d["id"] for d in json.loads(run("wcag", "--keyword", "2.1", "--output", "json").stdout)]
        assert ids == ["1.2.1", "2.1.1", "2.1.2", "2.1.4", "2.2.1", "3.2.1", "4.1.1"]

    def test_keyword_2_2_en_wcag(self):
        ids = [d["id"] for d in json.loads(run("wcag", "--keyword", "2.2", "--output", "json").stdout)]
        assert ids == ["1.2.2", "2.2.1", "2.2.2", "3.2.2", "4.1.1"]

    @pytest.mark.parametrize(
        "keyword,expected",
        [
            ("2.1", {"wcag": 7, "aria": 4, "tools": 1, "glossary": 1, "legal": 17, "resources": 3, "cognitive": 3}),
            ("2.2", {"wcag": 5, "aria": 1, "handoff": 1, "glossary": 1, "legal": 1, "resources": 7, "cognitive": 7}),
        ],
    )
    def test_all_conserva_los_resultados_por_base(self, keyword, expected):
        data = json.loads(run("all", "--keyword", keyword, "--output", "json").stdout)
        by_db: dict[str, int] = {}
        for row in data:
            by_db[row["_database"]] = by_db.get(row["_database"], 0) + 1
        assert by_db == expected

    def test_all_wcag_coincide_solo_por_campos_de_contenido(self):
        for row in json.loads(run("all", "--keyword", "2.2", "--output", "json").stdout):
            if row["_database"] == "wcag":
                content = [str(v) for k, v in row.items() if k not in ("versions", "_database")]
                assert any("2.2" in v for v in content), row["id"]


class TestWcagVersionFilter:
    """`--wcag-version` filtra por pertenencia exacta a la columna `versions`."""

    @staticmethod
    def ids(*args: str) -> list[str]:
        r = run("wcag", *args, "--output", "json")
        assert r.returncode == 0, r.stderr
        return [d["id"] for d in json.loads(r.stdout)]

    @staticmethod
    def rows(*args: str) -> list[dict]:
        r = run("wcag", *args, "--output", "json")
        assert r.returncode == 0, r.stderr
        return json.loads(r.stdout)

    @pytest.mark.parametrize("version,total,level_a", [("2.1", 50, 30), ("2.2", 58, 31)])
    def test_conteos_por_version(self, version, total, level_a):
        data = self.rows("--wcag-version", version)
        assert len(data) == total
        assert sum(d["level"] == "A" for d in data) == level_a
        assert all(version in d["versions"].split(";") for d in data)

    def test_sin_filtro_conserva_59_y_32_de_nivel_a(self):
        data = self.rows()
        assert len(data) == 59
        assert sum(d["level"] == "A" for d in data) == 32

    def test_4_1_1_solo_en_2_1_y_2_5_8_solo_en_2_2(self):
        v21, v22 = self.ids("--wcag-version", "2.1"), self.ids("--wcag-version", "2.2")
        assert "4.1.1" in v21 and "2.5.8" not in v21
        assert "4.1.1" not in v22 and "2.5.8" in v22

    def test_pertenencia_exacta_no_por_identificador(self):
        # 2.5.8 empieza por "2." pero solo está etiquetado 2.2; 4.1.1 solo 2.1.
        assert self.ids("--wcag-version", "2.1", "--id", "2.5.8") == []
        assert self.ids("--wcag-version", "2.2", "--id", "4.1.1") == []
        assert self.ids("--wcag-version", "2.2", "--id", "2.5.8") == ["2.5.8"]
        assert self.ids("--wcag-version", "2.1", "--id", "4.1.1") == ["4.1.1"]

    def test_combina_con_level_exacto(self):
        aa22 = self.ids("--wcag-version", "2.2", "--level", "AA")
        assert "2.5.8" in aa22 and "1.1.1" not in aa22  # AA exacto, no A+AA
        assert set(aa22) == set(self.ids("--level", "AA")) - {
            d["id"] for d in self.rows("--level", "AA") if "2.2" not in d["versions"].split(";")
        }

    def test_combina_con_principle_y_keyword(self):
        assert self.ids("--wcag-version", "2.2", "--principle", "Operable", "--keyword", "target") == ["2.5.8"]
        assert self.ids("--wcag-version", "2.1", "--keyword", "target") == []

    def test_keyword_2_1_sigue_sin_coincidir_por_versions(self):
        ids = self.ids("--wcag-version", "2.1", "--keyword", "2.2")
        assert ids == ["1.2.2", "2.2.1", "2.2.2", "3.2.2", "4.1.1"]

    def test_version_invalida_la_rechaza_argparse(self):
        for bad in ("2.0", "3.0", "2", ""):
            r = run("wcag", "--wcag-version", bad)
            assert r.returncode == 2
            assert "invalid choice" in r.stderr and r.stdout == ""

    @pytest.mark.parametrize("version", ["2.1", "2.2"])
    def test_exportacion_json_con_version(self, version, tmp_path):
        out = tmp_path / "wcag.json"
        r = run("wcag", "--wcag-version", version, "--output", "json", "--export", str(out))
        assert r.returncode == 0
        data = json.loads(out.read_text(encoding="utf-8"))
        assert data == json.loads(r.stdout)
        assert len(data) == (50 if version == "2.1" else 58)
        assert all("versions" in d for d in data)

    def test_csv_con_version_conserva_cinco_columnas(self):
        r = run("wcag", "--wcag-version", "2.2", "--output", "csv")
        assert r.returncode == 0
        rows = [x for x in csv.reader(r.stdout.splitlines()) if x]  # ignora líneas en blanco de fin de línea
        assert rows[0] == ["id", "level", "principle", "criterion", "description"]
        assert len(rows) == 59 and {len(x) for x in rows} == {5}

    def test_tabla_con_version_no_muestra_versions(self):
        r = run("wcag", "--wcag-version", "2.2", "--id", "2.5.8")
        assert r.returncode == 0 and "2.5.8" in r.stdout and "versions" not in r.stdout

    def test_aviso_aaa_solo_en_stderr(self):
        r = run("wcag", "--wcag-version", "2.2", "--level", "AAA", "--output", "json")
        assert r.returncode == 0
        assert "AAA" in r.stderr and "not include" in r.stderr
        assert [d["id"] for d in json.loads(r.stdout)] == ["2.4.12", "2.4.13", "3.3.9"]

    def test_sin_aviso_fuera_de_aaa(self):
        assert run("wcag", "--wcag-version", "2.2", "--level", "AA").stderr == ""
        assert run("wcag", "--level", "AAA").stderr == ""

    def test_level_aaa_sin_version_no_cambia(self):
        assert self.ids("--level", "AAA") == ["2.4.12", "2.4.13", "3.3.9"]

    def test_all_no_acepta_el_filtro(self):
        assert run("all", "--keyword", "contrast", "--wcag-version", "2.2").returncode == 2


class TestFormCriteriaTechniqueIds:
    """IDs de técnicas/fallos de formularios verificados contra las páginas Understanding de W3C."""

    @staticmethod
    def row(criterion_id: str) -> dict:
        return json.loads(run("wcag", "--id", criterion_id, "--output", "json").stdout)[0]

    def test_4_1_2_lista_f68_para_control_sin_nombre(self):
        failures = self.row("4.1.2")
        assert "F68" in failures["failures"] and "F68" not in failures["techniques"]

    def test_3_3_2_no_atribuye_f86_ni_f82_a_campos_obligatorios(self):
        failures = self.row("3.3.2")["failures"]
        assert "F86" not in failures  # F86 pertenece a 4.1.2 (campos multiparte)
        assert "required" not in failures

    def test_1_3_5_lista_f107_y_h98(self):
        r = self.row("1.3.5")
        assert "H98" in r["techniques"] and "F107" in r["failures"]


class TestAuthenticationAndModalData:
    """Datos de 3.3.8/3.3.9 y del patrón de diálogo modal, contrastados con WCAG 2.2 y APG."""

    @staticmethod
    def wcag(criterion_id: str) -> dict:
        return json.loads(run("wcag", "--id", criterion_id, "--output", "json").stdout)[0]

    def test_3_3_8_y_3_3_9_lista_f109_y_no_cita_captcha_sin_audio_como_fallo(self):
        for cid in ("3.3.8", "3.3.9"):
            row = self.wcag(cid)
            assert "F109" in row["failures"]
            assert "audio" not in row["failures"].lower()

    def test_3_3_9_no_conserva_las_excepciones_de_reconocimiento_ni_contenido_personal(self):
        text = self.wcag("3.3.9")["description"].lower()
        assert "alternative" in text and "mechanism" in text
        assert "are not exceptions" in text

    def test_3_3_8_conserva_las_cuatro_excepciones(self):
        text = self.wcag("3.3.8")["description"].lower()
        for word in ("alternative", "mechanism", "object recognition", "provided"):
            assert word in text

    def test_modal_no_impone_siempre_el_primer_elemento(self):
        rows = json.loads(run("aria", "--component", "modal", "--output", "json").stdout)
        focus = rows[0]["focus_management"].lower()
        assert "tabindex=-1" in focus and "least destructive" in focus
        assert "logical element" in focus
