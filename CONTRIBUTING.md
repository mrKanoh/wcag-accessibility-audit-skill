# Contributing to wcag-accessibility-audit-skill

Thank you for helping improve this skill! Every contribution — fixes, new patterns,
better prompts, corrected CSV data — makes a real difference for developers building
accessible products.

The project is intended for use across AI agents and for direct human consultation.
Keep reusable guidance independent of a particular host; label host-specific installation
steps and report compatibility only for environments actually tested. See the usage routes
in [README.md](./README.md) and [README-es.md](./README-es.md).

---

## Table of Contents

- [Types of contributions](#types-of-contributions)
- [Getting started](#getting-started)
- [Project structure](#project-structure)
- [CSV database conventions](#csv-database-conventions)
- [Adding a component example](#adding-a-component-example)
- [Adding or improving a prompt](#adding-or-improving-a-prompt)
- [Improving SKILL.md](#improving-skillmd)
- [Commit conventions](#commit-conventions)
- [Pull request checklist](#pull-request-checklist)
- [Code of conduct](#code-of-conduct)

---

## Types of contributions

Use WCAG Success Criterion (SC) identifiers when explaining a standards-related change.
ARIA refers to roles, states, and properties exposed to assistive technologies; SR means screen reader.

| Type | Where | Notes |
|------|-------|-------|
| Bug fix in a CSV (wrong WCAG SC, typo) | `data/*.csv` | Reference the correct SC or spec |
| New ARIA pattern | `data/aria-patterns.csv` + `examples/components/` | Must include keyboard + focus behavior |
| New accessible component | `examples/components/` | Plain HTML first; document keyboard and SR test evidence |
| New/improved agent prompt | `prompts/` | Follow the prompt template format |
| New jurisdiction in legal framework | `data/legal-framework.csv` | Include law name, standard, effective date, scope |
| New glossary term (ES↔EN) | `data/glossary-es.csv` | Include context field |
| SKILL.md improvement | `SKILL.md` | Keep core instructions concise; link supporting references instead of duplicating them |
| New template | `templates/` | Include usage instructions inside the file |
| search.py improvement | `scripts/search.py` | Include tests in `tests/test_search.py` |
| Documentation | `README.md`, `README-es.md`, `RESOURCES.md` | Keep both README languages aligned with actual behavior |

---

## Getting started

Use Python 3.10 or newer for the search utility and tests, plus Git for a development checkout. The search utility uses the Python standard library; the tests additionally need pytest.

Fork the repository on GitHub, then clone your fork:

```bash
git clone https://github.com/YOUR-USERNAME/wcag-accessibility-audit-skill.git
cd wcag-accessibility-audit-skill
python -m venv .venv
```

Activate the environment using the instructions for your shell:

```powershell
# Windows (PowerShell)
.\.venv\Scripts\Activate.ps1
```

```bash
# macOS / Linux (bash or zsh)
source .venv/bin/activate
```

Install the test dependency, run the existing checks, and create a branch:

```bash
python -m pip install pytest
python -m pytest tests/ -v
python scripts/search.py all --keyword contrast --output json
git switch -c docs/your-improvement-description
```

Use a branch name that describes your contribution. After making and reviewing your changes, commit and push to your fork when ready, then open a pull request against `main`. Report actual results, including any failures or checks you could not run. Python tests do not validate the HTML examples with keyboards or screen readers.

---

## Project structure

```
wcag-accessibility/
├── SKILL.md                    ← Skill instructions (loaded when invoked)
├── README.md                   ← English project documentation
├── README-es.md                ← Spanish project documentation
├── CHANGELOG.md                ← Document your changes here
├── CONTRIBUTING.md             ← This file
│
├── data/                       ← 14 searchable CSV databases
│   ├── wcag-criteria.csv
│   ├── aria-patterns.csv
│   ├── cognitive-accessibility.csv   ← COGA patterns
│   └── ...
│
├── examples/
│   └── components/             ← HTML examples; record test evidence per component
│       ├── date-picker.html
│       ├── toast-notifications.html
│       ├── carousel.html
│       └── tree-view.html
│
├── prompts/                    ← 12 task prompts
├── templates/                  ← Audit report, CI pipeline, VPAT
├── scripts/
│   ├── search.py               ← CLI search tool
│   └── generate-resources-md.py
└── tests/
    └── test_search.py          ← pytest suite for search.py
```

---

## CSV database conventions

Each CSV has a consistent header row. When adding or renaming columns, review
`scripts/search.py`, `scripts/mcp-server.py`, tests, and documentation for affected consumers.
Update them as needed and document the change in `CHANGELOG.md`. Preserve existing output
contracts unless the change explicitly calls for a different contract.

### wcag-criteria.csv columns

`id,level,principle,criterion,description,techniques,failures,url,versions`

`versions` uses `2.1`, `2.2`, or `2.1;2.2`. Retain 4.1.1 only for 2.1; it was removed
in 2.2. The current catalog contains 2.1 A/AA criteria plus the nine additions in 2.2;
it does not contain the 28 AAA criteria inherited from 2.1. JSON exposes `versions`;
the WCAG table and CSV outputs intentionally use a smaller field set. Do not assume
that adding a source column changes every output format.

### aria-patterns.csv columns

`component,role,required_aria,optional_aria,keyboard,focus_management,notes,wcag_ref`

### cognitive-accessibility.csv columns

`pattern_id, pattern_name, user_group, wcag_ref, coga_objective, description, design_guidance, implementation_notes, testing_notes`

### General rules

- Use UTF-8 encoding
- Quote fields containing commas, newlines, or double quotes; escape internal double quotes by doubling them
- Keep descriptions concise (one sentence per field where possible)
- Reference the applicable WCAG SC (`1.4.3`, `2.1.1`, etc.) and an authoritative source; distinguish requirements from recommendations

---

## Adding a component example

Component examples live in `examples/components/` as self-contained HTML files.

### Requirements checklist

Before submitting, verify your component and document the results. For manual tests,
record the date, operating system, browser and screen reader versions, steps, expected
behavior, and observed result. Use `PASS`, `FAIL`, `NOT RUN`, or a justified `NOT APPLICABLE`;
leave unperformed checks unchecked and disclose the gaps in the pull request.
A checklist or a code comment alone is not evidence that testing occurred.

- [ ] Works with **keyboard only** (Tab, Enter, Space, Arrow keys, Escape where applicable)
- [ ] Has been tested with **NVDA + Firefox** (Windows)
- [ ] Has been tested with **VoiceOver + Safari** (macOS) OR TalkBack
- [ ] Uses correct **ARIA roles, states, and properties** per the WAI-ARIA APG
- [ ] Keyboard focus is visible ([2.4.7](https://www.w3.org/WAI/WCAG22/Understanding/focus-visible.html)); do not remove the default indicator without an adequate replacement
- [ ] Author-styled focus indicators meet [1.4.11](https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html) where applicable: 3:1 against adjacent colors, with the criterion's exceptions. 2.4.7 itself sets no contrast ratio
- [ ] For WCAG 2.2 AA, the focused component is not entirely hidden by author-created content ([2.4.11](https://www.w3.org/WAI/WCAG22/Understanding/focus-not-obscured-minimum.html))
- [ ] Pointer targets meet [2.5.8](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html): at least **24×24 CSS px**, or a documented exception (spacing, equivalent, inline, user-agent control, or essential). **44×44 CSS px** belongs to [2.5.5, level AAA](https://www.w3.org/WAI/WCAG22/Understanding/target-size-enhanced.html), with its own exceptions
- [ ] Respects **`prefers-reduced-motion`**
- [ ] Sets the `<html lang>` value to the language of the example (for example, `en` or `es`)
- [ ] Has an inline `<style>` block (self-contained, no external dependencies)
- [ ] Keeps any required JavaScript inline (no frameworks or external CDN)
- [ ] Includes a **`<h1>`** describing what the component demonstrates
- [ ] Lists relevant WCAG SCs and verification status in a comment block at the top; does not claim complete conformance from an example alone

### File header comment template

```html
<!--
  Component: Accessible [Name]
  Pattern: [WAI-ARIA APG pattern name if applicable]
  Target: [WCAG version and level]
  Test evidence (replace NOT RUN only after performing the check):
    Keyboard: NOT RUN
    NVDA + Firefox: NOT RUN
    VoiceOver + Safari or TalkBack + Chrome: NOT RUN
  For each performed test, record:
    Status: [PASS / FAIL / NOT RUN / NOT APPLICABLE with reason]
    Date and environment: [OS, browser, screen reader versions]
    Steps: [actions and keys used]
    Expected / observed: [behavior and any limitations]
  Relevant SCs (verify each; this list is not a conformance claim):
    - 1.3.1 Info and Relationships
    - 2.1.1 Keyboard
    - 2.4.3 Focus Order
    - 2.4.7 Focus Visible
    - 4.1.2 Name, Role, Value
    [add others]
-->
```

---

## Adding or improving a prompt

Prompts live in `prompts/` as Markdown files.

### Template structure

````markdown
# Prompt: [Descriptive title]

[One sentence: when to use this prompt]

---

## Prompt (copy & paste)

```
[The actual prompt text — what the user provides to the agent]
```

---

## Tips

- [Tip 1]
- [Tip 2]
````

### Rules

- State the required inputs (code, URL, design, or findings) and ask for missing evidence rather than inventing it
- Reference relevant CSV databases at the bottom if useful
- Keep prompts focused — one primary use case per file

---

## Improving SKILL.md

`SKILL.md` contains the reusable instructions an agent reads when the skill is activated. Keep it:

- **Concise** — keep core instructions focused and move detailed material into linked references when appropriate; avoid adding arbitrary line limits
- **Easy to navigate** — use clear headings and preserve references when reorganizing sections
- **Evidence-based** — distinguish normative requirements, recommendations, illustrative code, and tests actually performed
- **Cross-referenced** — point to CSV databases instead of duplicating data
- **Portable** — keep reusable instructions agent-neutral, isolate host-specific setup, and document the host/version and evidence for any compatibility claim
- **Scoped to the task** — choose guidance for the target platform and WCAG version; do not treat a web-only check as proof about a native app or document

When adding a new framework section:

1. Add it as `## N. Framework Name` (next available number)
2. Update the "Notes for the agent" bullet that lists stack examples
3. Update both `README.md` and `README-es.md` if the documented scope changes

---

## Commit conventions

Use [Conventional Commits](https://www.conventionalcommits.org/):

```
feat: add Vue 3 accessible modal example
fix: correct aria-expanded usage in accordion pattern
docs: update README file structure table
data: add 5 cognitive accessibility patterns to CSV
test: add pytest cases for --output json flag
chore: update .gitignore
```

Reference a WCAG SC in the commit body when fixing a specific criterion:

```
fix: correct focus trap in date picker dialog

Keyboard focus could not leave the dialog and Escape did not close it.
Restore a keyboard exit path and verify focus returns to the trigger (WCAG 2.1.2).
```

---

## Pull request checklist

Before opening a PR, confirm:

- [ ] Run `python -m pytest tests/ -v` for search or data changes; report results. For documentation-only changes, verify links and examples and state if the suite was not run
- [ ] Run affected documented commands; for search or data changes, also check a relevant query such as `python scripts/search.py all --keyword contrast --output json`
- [ ] Host-specific instructions are labeled, and compatibility claims identify the environments actually tested
- [ ] Both README languages reflect changes to behavior, scope, or project resources
- [ ] CHANGELOG.md updated under `[Unreleased]`
- [ ] Commit message follows Conventional Commits format
- [ ] PR description cites the relevant WCAG SC or WAI-ARIA pattern where applicable and separates automated results, manual results, and tests not run

---

## Code of conduct

This project follows the [Contributor Covenant v2.1](https://www.contributor-covenant.org/version/2/1/code_of_conduct/).

In short: be kind, be specific, and assume good intent. Accessibility is for everyone —
so is contributing to this project.

For questions or corrections, open a [GitHub issue](https://github.com/mrKanoh/wcag-accessibility-audit-skill/issues) with reproduction steps and supporting sources.
