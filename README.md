<div align="center">

# ♿ WCAG Accessibility Audit Skill

**An open-source accessibility skill for AI agents and people working with WCAG 2.1/2.2 AA.**

Review web UI code, plan keyboard and screen reader tests, and prepare accessibility
findings in English or Spanish. Includes WAI-ARIA patterns, mobile guidance,
searchable reference data, and report templates. AI reviews and automated checks
require manual validation.

[![Scope: WCAG 2.1/2.2 AA](https://img.shields.io/badge/Scope-WCAG_2.1%2F2.2_AA-blueviolet)](https://www.w3.org/WAI/standards-guidelines/wcag/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green)](./LICENSE)
[![Tests](https://img.shields.io/github/actions/workflow/status/mrKanoh/wcag-accessibility-audit-skill/test.yml?branch=main&label=tests)](https://github.com/mrKanoh/wcag-accessibility-audit-skill/actions/workflows/test.yml)

[Leer en español](./README-es.md)

[What it does](#what-it-does) · [Installation](#installation) · [Compatibility](#compatibility-matrix-from-official-documentation) · [First use](#first-use) · [Scope and limitations](#scope-and-limitations) · [Searchable databases](#searchable-databases)

</div>

## What it does

For developers, designers, and people reviewing accessibility, this skill provides reusable instructions and references for AI-assisted work:

- Review UI code and suggest corrections for semantics, forms, keyboard behavior, focus, contrast, and WAI-ARIA (roles, states, and properties for assistive technologies).
- Plan manual keyboard and screen reader tests, including NVDA, JAWS, VoiceOver, and TalkBack.
- Prepare findings, acceptance criteria, design handoffs, and audit reports.
- Consult reference data and adapt examples of automated accessibility checks to a project.

The skill instructs the agent to answer in the user's language. Its reference data is primarily in English; the included [English–Spanish glossary](./data/glossary-es.csv) supports Spanish terminology.

## Installation

This project is intended for people using different AI agents, not just Claude Code. Its data, prompts, and templates can also be consulted directly without AI. The repository follows the open [Agent Skills format](https://agentskills.io/specification): a directory with a `SKILL.md` plus `scripts/` and `data/`. A single `SKILL.md` is the core for every product; there are no per-vendor copies.

### Three ways to use it

1. **Native skill** — in an agent that supports Agent Skills, install the **full directory** under the name `wcag-accessibility` (the specification requires `name` to match the directory name).
2. **Search with Python** — if the agent can read the files and run commands, it can query the databases with `python scripts/search.py …` from the skill root. This needs **Python 3.10 or newer** (`requires-python = ">=3.10"` in `pyproject.toml`); loading the instructions does not.
3. **Manual context** — give the assistant `SKILL.md` and the relevant `data/*.csv` files or [`prompts/`](./prompts) as context, where the product allows it. This mode has no automatic discovery and no execution. If the assistant cannot run a query, it should say so, ask you for the data, or give you the command to run yourself. It must not invent results.

Reading instructions and executing Python are different capabilities: an agent can have the first without the second.

### Compatibility matrix (from official documentation)

Evidence states: **documented** = the vendor documents the format and paths; **NOT VERIFIED** = not tested by this project. Only Claude Code has been tested, and only in the single environment described under the table; installation, discovery, and execution remain **NOT VERIFIED** for Codex, Cursor, and Copilot. Do not read this table as a guarantee of compatibility.

| Agent | Documented skill locations | Documented limits | Source |
|-------|---------------------------|-------------------|--------|
| Claude Code | Personal `~/.claude/skills/<name>/SKILL.md`; project `.claude/skills/<name>/SKILL.md`; supporting files allowed | `/reload-skills` if the top-level `skills` folder is new | [docs](https://code.claude.com/docs/en/skills) |
| Codex (OpenAI) | Repo `.agents/skills` (from the working directory up to the repo root); user `$HOME/.agents/skills`; admin `/etc/codex/skills` | Same-named skills are not merged. Repository skills are available in cloud tasks; local personal skills are not synced there. Script execution needs the target environment and permissions | [Skills](https://learn.chatgpt.com/docs/build-skills), [cloud environments](https://learn.chatgpt.com/docs/environments/cloud-environments) |
| Cursor | Project `.agents/skills/`, `.cursor/skills/`; user `~/.agents/skills/`, `~/.cursor/skills/`; also reads `.claude/skills/`, `.codex/skills/`, `~/.claude/skills/`, `~/.codex/skills/` | The agent runs referenced scripts when the skill is invoked. Cloud Agents: only `~/.cursor/skills/` syncs, and only if enabled; project skills and `~/.agents/skills/` are not copied | [docs](https://cursor.com/docs/skills) |
| GitHub Copilot | Project `.github/skills`, `.claude/skills`, `.agents/skills`; personal `~/.copilot/skills`, `~/.agents/skills` | Documented for Copilot cloud agent, code review, CLI, the Copilot app, and agent mode in VS Code and JetBrains. The page does not cover frontmatter or script execution | [docs](https://docs.github.com/en/copilot/concepts/agents/about-agent-skills) |

| Status | Claude Code | Codex | Cursor | Copilot |
|--------|-------------|-------|--------|---------|
| Format support documented | Yes | Yes | Yes | Yes |
| Installation tested | Yes (project copy, see below) | NOT VERIFIED | NOT VERIFIED | NOT VERIFIED |
| Discovery tested | Yes (project copy, see below) | NOT VERIFIED | NOT VERIFIED | NOT VERIFIED |
| Execution tested | Yes (`search.py`, see below) | NOT VERIFIED | NOT VERIFIED | NOT VERIFIED |

**Claude Code test scope (2026-10-19):** Claude Code 2.1.292 on Windows 11, non-interactive mode (`claude -p`, `--setting-sources project`), model `claude-sonnet-5-5`. The skill files were copied by hand into an isolated project at `.claude/skills/wcag-accessibility/`; Claude Code listed the skill at startup and loaded it. In one run the agent executed the bundled `scripts/search.py` (`--wcag-version`, `--id`, `aria --component`) and its WCAG 2.1/2.2 record counts (50/58) matched a direct run of the script. In a second run it reviewed a small `form.html` statically without modifying files. This is two runs in one environment, not a guarantee for other versions, operating systems, models, or interactive sessions. A later check ran six small form-review cases and a new-session install and first-use walk-through from a local copy of the candidate files (not from GitHub); this is a technical walk-through, not a usability test with an external person, and it did not include a screen reader. In that check one case first produced an invented finding and passed on a repeat, and one answer misread `--wcag-version` as "only criteria added in that version" (the catalog notes now explain that it selects what belongs to a version). The test records are stored in the local `reports/` folder of the development checkout, which Git ignores: they are not part of the published repository. Installing through any marketplace or third-party distribution channel (including Agensi) was not tested.

### Get a local copy without choosing an agent

From a parent directory of your choice:

```bash
git clone https://github.com/mrKanoh/wcag-accessibility-audit-skill.git wcag-accessibility
cd wcag-accessibility
```

If the destination already exists, inspect it first or choose another location. You can browse this copy or run the Python CLI without an agent. For native skill discovery, use the appropriate host-specific location below instead; a generic clone is not automatically installed in every agent.

### Install the full package

Requirements: Git to clone and update; Python 3.10+ only for `scripts/search.py`. Choose **one location per product** and avoid keeping duplicate copies: no single folder is documented for all four products. Claude Code reads `~/.claude/skills/`; Codex and Copilot (personal) read `~/.agents/skills/`; Cursor reads both, so it needs only one of them.

```bash
# Claude Code (Cursor also reads this folder)
git clone https://github.com/mrKanoh/wcag-accessibility-audit-skill.git ~/.claude/skills/wcag-accessibility

# Codex, GitHub Copilot, Cursor (user level)
git clone https://github.com/mrKanoh/wcag-accessibility-audit-skill.git ~/.agents/skills/wcag-accessibility
```

```powershell
# Windows (PowerShell), Claude Code; how Codex/Copilot resolve $HOME on Windows is NOT VERIFIED
git clone https://github.com/mrKanoh/wcag-accessibility-audit-skill.git "$env:USERPROFILE\.claude\skills\wcag-accessibility"
```

For a single repository, clone into that repository's project folder instead (for example `.claude/skills/wcag-accessibility` or `.agents/skills/wcag-accessibility`, as listed above). Cloud agents (Copilot cloud agent, Cursor Cloud Agents, Codex cloud) work from what the cloud environment can see, so a local user-level install may not apply there; check each vendor's page.

If the target directory already exists, `git clone` fails and nothing is overwritten. Do not delete it:

- If it is a clone of this repository, run `git status` inside it first. Commit or stash local changes you want to keep, then update with `git pull`.
- If it is another installation, keep it: rename or move it outside the skills folders, so two copies are not loaded side by side, or clone into another directory outside them to compare both before deciding which to install.

Copying only `SKILL.md` is **not** equivalent: the instructions would load, but the searchable databases and `scripts/search.py` would be missing.

### MCP server (optional, separate from the skill format)

`scripts/mcp-server.py` exposes the CSV databases as 15 MCP **resources** (`wcag://…`). It defines no tools or prompts, and it is not an audit engine. Resource support depends on the client; no client validation record is provided here (**NOT VERIFIED**). It imports the `mcp` Python package, which is not declared in `pyproject.toml`. This repository does not configure it for you.

For Claude Code, if the top-level `skills` directory did not exist when the session started, run `/reload-skills`. Reading instructions does not grant file access or permission to execute scripts in any agent.

## First use

Load the skill using your agent's supported mechanism, or provide the relevant instructions and supporting files manually. For the Claude Code installation above, invoke it directly:

```text
/wcag-accessibility
```

In either case, paste or identify the component you want reviewed and describe the intended behavior:

```text
Review this modal against WCAG 2.2 AA. Identify the code you inspected,
explain each potential barrier, cite the relevant criterion, and suggest
small corrections. Separate confirmed findings from issues that need
browser, keyboard, or screen reader testing. Do not modify files yet.
```

A useful finding should identify the element, the barrier, the related criterion, a proposed correction, and the verification still needed. For example:

> **Illustrative finding:** an icon-only button has no accessible name in the supplied HTML (4.1.2). Add an appropriate accessible name, then check its announcement in a browser with a screen reader. Code reviewed; screen reader test not performed.

You can also ask naturally, such as “How do I test this form with NVDA?” In Claude Code, automatic activation depends on Claude matching your request to the skill description. If it does not activate, use `/wcag-accessibility`. See the [official skill documentation](https://code.claude.com/docs/en/skills).

## Scope and limitations

- **WCAG target:** the skill instructions use WCAG 2.1 AA by default and discuss additions in 2.2. State the version and level you need in your request. The scope badge above describes the subject matter, not a certification.
- **Catalog coverage:** [wcag-criteria.csv](./data/wcag-criteria.csv) contains 59 records: all 50 A/AA criteria of 2.1 plus the nine additions in 2.2, including three AAA additions. The 28 AAA criteria inherited from 2.1 are absent. Criterion 4.1.1 is retained for historical 2.1 use; it was removed in 2.2.
- **Version metadata:** each catalog record has a `versions` field (`2.1`, `2.2`, or `2.1;2.2`), visible in JSON. Use `--wcag-version 2.1` or `--wcag-version 2.2` on the `wcag` subcommand to keep only records tagged with that version (exact match on the field; 2.1 gives 50 records including 4.1.1, 2.2 gives 58 including 2.5.8). Without it nothing is filtered. The filter selects the criteria that belong to a version, not only those it added: every AA record belongs to 2.2, so `--wcag-version 2.2 --level AA` returns the same 24 records as `--level AA`. To list only the nine 2.2 additions, use `--output json` and keep the records whose `versions` is exactly `2.2`; the table and CSV outputs do not show `versions`. The catalog has no 2.1 AAA criteria, so a version filter combined with `--level AAA` is not a complete list.
- **Review evidence:** AI suggestions and automated scans do not establish conformance. Test relevant pages, states, complete user flows, keyboard behavior, and assistive technologies in the target environment. Record what was actually tested.
- **Other platforms and legal references:** mobile guidance and jurisdictional summaries are starting points. Select applicable platform requirements and verify current official legal sources; a database lookup cannot determine your product's legal obligations.

Use the [W3C WCAG 2.2 recommendation](https://www.w3.org/TR/WCAG22/) as the normative source. The `wcag3` CLI command returns a draft-status notice and W3C links, not a criteria catalog.

## Searchable databases

The Python command-line interface (CLI) can be used without any AI agent. It uses the Python standard library; no additional Python packages are needed for these searches.

Run searches from the root of your local copy (`wcag-accessibility` in the generic clone above). If you used the Claude Code personal installation, change to its directory:

```bash
# macOS / Linux
cd ~/.claude/skills/wcag-accessibility
```

```powershell
# Windows (PowerShell)
Set-Location "$env:USERPROFILE\.claude\skills\wcag-accessibility"
```

For a Claude Code project installation, use `.claude/skills/wcag-accessibility` instead; for other agents, use the actual repository location. The following commands work from that directory:

```bash
# Criteria about contrast, including version metadata
python scripts/search.py wcag --keyword contrast --output json

# Modal pattern: roles, keyboard behavior, and focus guidance
python scripts/search.py aria --component modal --detail

# English–Spanish glossary
python scripts/search.py glossary --keyword contrast
```

These glossary and contrast searches should return matching records; the modal search should describe dialog behavior. If `python` is unavailable, try `python3` on macOS/Linux or `py` on Windows, and check that it is Python 3.10 or newer. A “can't open file” error usually means you are outside the skill root.

<details>
<summary>More searches and output options</summary>

```bash
# Only records labeled AA (not A + AA)
python scripts/search.py wcag --level AA

# Only records tagged with a WCAG version (combines with --level, --id, --keyword, --principle)
python scripts/search.py wcag --wcag-version 2.2 --level AA

# All available WCAG records; inspect level and versions for your target
python scripts/search.py wcag --output json

# NVDA heading-navigation shortcuts
python scripts/search.py keys --reader NVDA --action heading

# Free screen reader tools for Windows
python scripts/search.py tools --type screen-reader --platform Windows --free --url

# Cross-database search
python scripts/search.py all --keyword contrast --output json

# All subcommands and WCAG-specific options
python scripts/search.py --help
python scripts/search.py wcag --help
```

Conformance at level AA requires meeting both level A and level AA criteria. `--level AA` is an exact level filter, not a complete AA checklist. Search terms generally need to match the language of the data; use English terms for most databases.

Use `--output json` or `--output csv` for structured output and `--export results.json` to save the selected output format to a file. JSON WCAG records include `versions`; the table and CSV outputs show a smaller set of fields.

</details>

<details>
<summary>Browse all 14 databases</summary>

| Command after `python scripts/search.py` | Reference data |
|---|---|
| `wcag` | WCAG criteria, levels, techniques, failures, sources, and versions |
| `aria` | Component roles, properties, keyboard behavior, and focus management |
| `tools` | Testing tools by platform, type, and cost |
| `keys` | Screen reader shortcuts |
| `semantic` | HTML semantics and usage guidance |
| `typography` | Typography, spacing, reflow, and zoom guidance |
| `color` | Contrast, states, forced colors, and color perception |
| `kpis` | Accessibility metrics and suggested targets |
| `handoff` | Research, design, development, QA, and release checklists |
| `models` | Models of disability |
| `glossary` | English–Spanish terminology and definitions |
| `legal` | Jurisdictional reference summaries |
| `resources` | Standards, guides, research, tools, and community references |
| `cognitive` | Cognitive accessibility patterns |

Use `all --keyword contrast` to search across these databases. `wcag3` is a separate status command.

</details>

## Examples and project resources

The repository includes eight HTML component examples: [date picker](./examples/components/date-picker.html), [toast notifications](./examples/components/toast-notifications.html), [carousel](./examples/components/carousel.html), [tree view](./examples/components/tree-view.html), [combobox](./examples/components/combobox.html), [data grid](./examples/components/data-grid.html), [media player](./examples/components/media-player.html), and [tabs](./examples/components/tabs.html).

Treat these as learning and adaptation examples. Before using them in a product, review their behavior and test them with the browsers and assistive technologies your users need. Inclusion here is not evidence of production readiness or a completed compatibility test.

| Resource | Purpose |
|---|---|
| [SKILL.md](./SKILL.md) | Agent instructions and entry point for hosts with skill support |
| [Prompts](./prompts/) | Twelve task prompts for reviews, remediation, content, design handoffs, and test planning |
| [Audit report](./templates/audit-report.md) | Starting point for documenting scope, findings, and evidence |
| [CI template](./templates/a11y-ci.yml) | Example automated checks; adapt dependencies, commands, URLs, configuration paths, and failure handling to your project |
| [VPAT reporting template](./templates/vpat-2.5-template.md) | Reporting aid; consult [ITI's official VPAT resources](https://www.itic.org/policy/accessibility/vpat) before preparing an Accessibility Conformance Report (ACR) |
| [Bibliography](./RESOURCES.md) | Standards and additional reading |
| [MCP server source](./scripts/mcp-server.py) | Optional Model Context Protocol server for exposing reference data; requires the `mcp` Python package and separate client configuration |
| [Changelog](./CHANGELOG.md) | Recorded project changes |

## References and credits

Standards and reference materials include [WCAG 2.1](https://www.w3.org/TR/WCAG21/), [WCAG 2.2](https://www.w3.org/TR/WCAG22/), the [WAI-ARIA Authoring Practices Guide](https://www.w3.org/WAI/ARIA/apg/), [WebAIM](https://webaim.org/), [Deque axe-core](https://github.com/dequelabs/axe-core), and [The A11Y Project](https://www.a11yproject.com/).

[Paul J. Adam's accessibility resources](https://pauljadam.com/) and the `ui-ux-pro-max` skill architecture are acknowledged as references and inspiration. These acknowledgments do not imply authorship, review, or endorsement of this project by the referenced people or organizations. See the [bibliography](./RESOURCES.md) for individual resource links.

## Contributing

Corrections to documentation, criteria, examples, and translations are welcome. See [CONTRIBUTING.md](./CONTRIBUTING.md) for the contribution process. Include a source for technical corrections and distinguish code review from tests you actually performed.

To run the existing Python tests from a development checkout with pytest installed:

```bash
python -m pytest tests/ -v
```

These tests exercise the search utility and data checks; they do not establish accessibility conformance or screen reader compatibility.

## License

[MIT](./LICENSE). You may use, share, and adapt the project under the license terms, including preservation of its copyright and permission notice.
