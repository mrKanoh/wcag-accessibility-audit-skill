# Changelog

All notable changes to this project will be documented in this file.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
This project uses [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [Unreleased]

### Added
- `python scripts/search.py wcag --wcag-version 2.1|2.2`: filters by exact membership in the
  existing `versions` column (2.1: 50 records, 2.2: 58). Combines with `--id`, `--keyword`,
  `--level` and `--principle`; not available in `all` or the MCP server; without it results
  are unchanged. With `--level AAA` it prints a note to stderr because the catalog has no
  2.1 AAA criteria. Covered by new tests.

### Fixed
- Reviews of form fragments over-claimed: a missing `<label>` was reported as a certain 4.1.2/1.3.1/3.3.2/2.4.6
  failure, `type="text"` was tied to 1.3.5, server behavior was inferred, and severity was automatic.
  Added `references/form-labels-and-names.md` (evidence categories, accessible-name sources, what each
  criterion requires), a pointer in `SKILL.md` and the component audit prompt, and corrected the
  techniques/failures and descriptions for 1.3.1, 1.3.5, 2.4.6, 3.3.2 and 4.1.2 in
  `data/wcag-criteria.csv` plus two notes in `data/semantic-html.csv` (sources: WCAG 2.2, Understanding
  pages, HTML-AAM Working Draft).
- Quote comma-containing fields in the typography and semantic HTML databases so
  recommendations, WCAG references, and notes stay in their intended columns.
- Check every database row for extra or missing fields in the CSV integrity tests.
- Separate WCAG requirements from design guidance in typography: 16 px / 1rem, body
  weight 400 and a named typeface are no longer presented as WCAG obligations; text
  spacing (1.4.12) is described as tolerance to user overrides; line length and
  alignment are tied to the AAA mechanism of 1.4.8. Synced `data/typography-rules.csv`
  and SKILL.md section 6 (sources: WCAG 2.2 and Understanding 1.4.3, 1.4.4, 1.4.8, 1.4.12).
- Replace unsupported install commands in both READMEs with a `git clone` of the
  public repository into `wcag-accessibility`, and document that the full package
  (`scripts/` and `data/`) is required, unlike copying only `SKILL.md`.

### Changed
- State in `SKILL.md` that `scripts/search.py` needs Python 3.10 or newer (standard library only).
- Use "WCAG Accessibility Audit Skill" as the display title in the skill and both
  READMEs, with an introduction describing audit guidance, remediation, and
  manual validation. Keep the technical skill identifier and repository URLs.
- Make instructions provider-neutral: "Notes for the agent", assistant-neutral prompts, and a
  usage-modes note in `SKILL.md` (native skill, Python search, manual context; never invent
  results when a query cannot run). Both READMEs now document the three modes, a
  compatibility matrix for Claude Code, Codex, Cursor and GitHub Copilot that separates
  support documented by each vendor from support tested here, and the MCP server as
  optional resources only. Tested so far: Claude Code only, in the environment the READMEs
  describe (project install from a local copy, Windows, new non-interactive sessions);
  Codex, Cursor and Copilot remain NOT VERIFIED. This neutral-wording and documentation
  change did not itself touch code, data, tests or metadata; other entries here cover those.

## [2.2.0] - 2026-04-21
### Added
- MCP Server (`scripts/mcp-server.py`) to expose 15 databases to Claude directly.
- WCAG 3.0 Draft database (`data/wcag3-draft.csv`).
- Accessible Media Player component (`examples/components/media-player.html`).
- Pull Request Template (`.github/PULL_REQUEST_TEMPLATE.md`).
- Synced `RESOURCES.md` using `generate-resources-md.py`.

## [2.1.0] - 2026-04-21
### Added
- Optimized Skill description with 14 trigger categories.
- Evaluation prompts (`evals/evals.json`) for skill testing.
- GitHub Actions CI workflow (`.github/workflows/test.yml`).
- Accessible Combobox component (`examples/components/combobox.html`).
- Accessible Data Grid component (`examples/components/data-grid.html`).
- Pytest configuration (`pytest.ini`).
- Security policy (`SECURITY.md`).
- MIT License file (`LICENSE`).
- Component README with feature tables.

### Added
- **VPAT 2.5 template** (`templates/vpat-2.5-template.md`) — full official ITI VPAT 2.5
  Rev WCAG format covering WCAG 2.x (A/AA/AAA), Section 508, and EN 301 549
- **Cognitive accessibility database** (`data/cognitive-accessibility.csv`) — 20 patterns
  based on W3C COGA (Cognitive Accessibility) supplemental guidance, covering ADHD,
  dyslexia, memory impairments, anxiety, and autism
- **6 new prompts** for advanced accessibility workflows:
  - `prompts/remediate-legacy-code.md` — audit + fix legacy HTML/jQuery/Bootstrap code
  - `prompts/generate-vpat-entry.md` — translate audit findings into VPAT ACR language
  - `prompts/test-with-screen-reader.md` — generate step-by-step SR test scripts (NVDA/VO/TalkBack)
  - `prompts/mobile-a11y-checklist.md` — React Native, SwiftUI, Jetpack Compose checklists
  - `prompts/inclusive-ux-writing.md` — plain language + inclusive terminology review
  - `prompts/design-tokens-audit.md` — audit Figma/Style Dictionary tokens against WCAG
- **Accessible component examples** (`examples/components/`):
  - `date-picker.html` — fully accessible date picker (dialog pattern, WCAG 2.2 AA,
    arrow key navigation, roving tabindex, typed input, live region errors)
  - `toast-notifications.html` — accessible toast system with `role="status"` (polite) and
    `role="alert"` (assertive) live regions, dismiss button, reduced motion support
- `CHANGELOG.md` — this file

### Changed
- `SKILL.md` — extended with:
  - **Section 19**: Vue 3 Composition API accessible examples (reactive form, modal, toggle)
  - **Section 20**: React Native accessibility (accessibilityLabel, accessibilityRole,
    Dynamic Type, reduceMotion, focus management)
  - **Section 21**: Cognitive Accessibility (COGA) — design patterns and WCAG mapping
  - **Section 22**: WCAG 3.0 / APCA preview — what's coming, how to prepare
- `scripts/search.py` — added:
  - `--output {table,json,csv}` flag on all subcommands
  - `--export <file>` flag to save results to disk
  - `all` subcommand: cross-database keyword search across all 14 CSVs
  - ANSI color support (auto-detected, `NO_COLOR` env var respected)
  - `cognitive` subcommand to search the new cognitive-accessibility.csv
- `data/` — added `cognitive-accessibility.csv` (14th database, 20 patterns)
- `.gitignore` — added reports/, *.json output, node_modules/, .venv/, env/
- `README.md` — updated to reflect new files, added CI status badge section

---

## [1.0.0] — 2026-04-10

### Added
- Initial release with full WCAG 2.1/2.2 skill (`SKILL.md`)
- 13 searchable CSV databases:
  - `wcag-criteria.csv` — 70+ WCAG 2.0/2.1/2.2 criteria
  - `aria-patterns.csv` — 25+ WAI-ARIA component patterns
  - `testing-tools.csv` — 30+ tools by type/platform/cost
  - `screen-reader-keys.csv` — NVDA, JAWS, VoiceOver, TalkBack, Narrator shortcuts
  - `semantic-html.csv` — element → role → when to use/avoid
  - `typography-rules.csv` — 20 accessible typography rules
  - `color-palette-rules.csv` — contrast, HCM, color-blindness rules
  - `kpis.csv` — 15 accessibility KPIs with formulas and targets
  - `handoff-checklist.csv` — Research → Design → Dev → QA → Release checklist
  - `disability-models.csv` — Medical, Social, Biopsychosocial, CRPD, Identity models
  - `glossary-es.csv` — 70+ Spanish ↔ English accessibility terms
  - `legal-framework.csv` — 25+ jurisdictions: ADA, EAA, Section 508, AODA, LGPD
  - `resources.csv` — 50+ authoritative books, blogs, research papers, tools
- `scripts/search.py` — unified CLI to query all databases
- `templates/audit-report.md` — complete fill-in audit report template
- `templates/a11y-ci.yml` — GitHub Actions pipeline (axe + pa11y + Playwright + Lighthouse)
- 6 Claude prompts: `audit-component`, `sc-to-acceptance-criteria`, `generate-alt-text`,
  `review-figma-handoff`, `summarize-audit-findings`, `generate-aria-pattern`
- `RESOURCES.md` — curated human-readable bibliography
- Stack examples: Next.js App Router, Angular, Svelte 5, Astro, SolidJS

---

[Unreleased]: https://github.com/mrKanoh/claude-wcag-accessibility-skill/compare/v1.0.0...HEAD
[1.0.0]: https://github.com/mrKanoh/claude-wcag-accessibility-skill/releases/tag/v1.0.0
