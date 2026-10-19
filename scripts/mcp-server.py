#!/usr/bin/env python3
"""
MCP Server for the WCAG Accessibility Skill.
Exposes the accessibility databases to any MCP client.
"""
import sys
import json
import csv
from pathlib import Path
from mcp.server.fastmcp import FastMCP

ROOT_DIR = Path(__file__).parent.parent
DATA_DIR = ROOT_DIR / "data"

# Keep in sync with WCAG3_NOTICE in search.py (tests/test_search.py compares them).
WCAG3_NOTICE = {
    "status": "draft-records-retired",
    "message": (
        "WCAG 3 is an incomplete W3C Working Draft and not a standard; WCAG 2.x remains "
        "the compliance target. The retired data file assigned fixed criterion IDs and APCA "
        "thresholds that the W3C draft does not support (Bronze appears there only as a "
        "proposed reporting tier), so no criteria are returned."
    ),
    "draft_url": "https://www.w3.org/TR/wcag-3.0/",
    "intro_url": "https://www.w3.org/WAI/standards-guidelines/wcag/wcag3-intro/",
    "records": [],
}

# Initialize FastMCP server
mcp = FastMCP("WCAG Accessibility Skill Data")

def read_csv(filename: str) -> list[dict]:
    """Helper to read a CSV file into a list of dicts."""
    filepath = DATA_DIR / filename
    if not filepath.exists():
        return []
    
    with open(filepath, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return list(reader)

@mcp.resource("wcag://criteria")
def get_wcag_criteria() -> str:
    """Get WCAG 2.1 and 2.2 criteria."""
    data = read_csv("wcag-criteria.csv")
    return json.dumps(data, indent=2)

@mcp.resource("wcag://draft-wcag3")
def get_wcag3_draft() -> str:
    """WCAG 3.0 draft status notice with W3C links (no criteria)."""
    return json.dumps(WCAG3_NOTICE, indent=2)

@mcp.resource("wcag://aria-patterns")
def get_aria_patterns() -> str:
    """Get ARIA component patterns."""
    data = read_csv("aria-patterns.csv")
    return json.dumps(data, indent=2)

@mcp.resource("wcag://semantic-html")
def get_semantic_html() -> str:
    """Get accessible HTML semantics."""
    data = read_csv("semantic-html.csv")
    return json.dumps(data, indent=2)

@mcp.resource("wcag://screen-reader-keys")
def get_screen_reader_keys() -> str:
    """Get screen reader shortcut keys."""
    data = read_csv("screen-reader-keys.csv")
    return json.dumps(data, indent=2)

@mcp.resource("wcag://testing-tools")
def get_testing_tools() -> str:
    """Get accessibility testing tools."""
    data = read_csv("testing-tools.csv")
    return json.dumps(data, indent=2)

@mcp.resource("wcag://cognitive")
def get_cognitive() -> str:
    """Get cognitive accessibility (COGA) patterns."""
    data = read_csv("cognitive-accessibility.csv")
    return json.dumps(data, indent=2)

@mcp.resource("wcag://color-palette")
def get_color_palette() -> str:
    """Get color contrast rules."""
    data = read_csv("color-palette-rules.csv")
    return json.dumps(data, indent=2)

@mcp.resource("wcag://typography")
def get_typography() -> str:
    """Get accessible typography rules."""
    data = read_csv("typography-rules.csv")
    return json.dumps(data, indent=2)

@mcp.resource("wcag://disability-models")
def get_disability_models() -> str:
    """Get disability models."""
    data = read_csv("disability-models.csv")
    return json.dumps(data, indent=2)

@mcp.resource("wcag://glossary-es")
def get_glossary_es() -> str:
    """Get English/Spanish accessibility glossary."""
    data = read_csv("glossary-es.csv")
    return json.dumps(data, indent=2)

@mcp.resource("wcag://handoff-checklist")
def get_handoff_checklist() -> str:
    """Get design to dev handoff checklist."""
    data = read_csv("handoff-checklist.csv")
    return json.dumps(data, indent=2)

@mcp.resource("wcag://kpis")
def get_kpis() -> str:
    """Get accessibility KPIs."""
    data = read_csv("kpis.csv")
    return json.dumps(data, indent=2)

@mcp.resource("wcag://legal-framework")
def get_legal_framework() -> str:
    """Get accessibility legal frameworks."""
    data = read_csv("legal-framework.csv")
    return json.dumps(data, indent=2)

@mcp.resource("wcag://resources")
def get_resources() -> str:
    """Get curated accessibility resources."""
    data = read_csv("resources.csv")
    return json.dumps(data, indent=2)


if __name__ == "__main__":
    mcp.run()
