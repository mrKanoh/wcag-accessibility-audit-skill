"""Structure checks for the JSON files in evals/.

They validate shape only. They do not judge whether an expectation is
correct; that needs a human or a model reading the standard.
"""

import json
from pathlib import Path

import pytest

EVALS_DIR = Path(__file__).resolve().parent.parent / "evals"
EVALS_JSON = EVALS_DIR / "evals.json"
TRIGGER_JSON = EVALS_DIR / "trigger-evals.json"


def _load(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def _json_files():
    return sorted(EVALS_DIR.glob("*.json"))


@pytest.mark.parametrize("path", _json_files(), ids=lambda p: p.name)
def test_eval_json_files_load(path):
    # Catches a syntax error or bad encoding in any evals/*.json.
    assert _load(path) is not None


def test_evals_json_has_evals():
    data = _load(EVALS_JSON)
    assert isinstance(data.get("evals"), list) and data["evals"]


def test_evals_ids_are_unique():
    # Catches a copied eval whose id was not changed.
    ids = [e.get("id") for e in _load(EVALS_JSON)["evals"]]
    assert len(ids) == len(set(ids)), f"duplicate ids: {ids}"


def test_each_eval_has_required_fields():
    # Catches an eval with an empty prompt, empty expected_output, or no expectations.
    for e in _load(EVALS_JSON)["evals"]:
        for field in ("prompt", "expected_output"):
            value = e.get(field)
            assert isinstance(value, str) and value.strip(), f"eval {e.get('id')}: empty {field}"
        exp = e.get("expectations")
        assert isinstance(exp, list) and exp, f"eval {e.get('id')}: expectations missing or empty"
        for item in exp:
            assert isinstance(item, str) and item.strip(), f"eval {e.get('id')}: blank expectation"


def test_no_keyword_assertions_left():
    # Catches the old keyword format (contains / contains_any) coming back.
    for e in _load(EVALS_JSON)["evals"]:
        assert "assertions" not in e, f"eval {e.get('id')} still has assertions"


def test_evals_json_description_says_meaning_not_keywords():
    # Catches removal of the note that evals are judged by meaning.
    assert "meaning" in _load(EVALS_JSON)["description"].lower()


def test_trigger_evals_shape():
    # Catches a missing query, a non-boolean should_trigger (e.g. "true"),
    # or a set that has only positives or only negatives.
    data = _load(TRIGGER_JSON)
    assert isinstance(data, list) and data
    for i, item in enumerate(data):
        assert isinstance(item.get("query"), str) and item["query"].strip(), f"item {i}: bad query"
        assert isinstance(item.get("should_trigger"), bool), f"item {i}: should_trigger not bool"
    values = {item["should_trigger"] for item in data}
    assert values == {True, False}, "need both should_trigger true and false"
