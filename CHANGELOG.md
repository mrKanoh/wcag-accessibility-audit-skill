# Changelog

All notable changes to this project will be documented in this file.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
This project uses [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [Unreleased]

### Added
- `SKILL.md` §5: «Before you build a custom component» (design guidance from *Inclusive Components*,
  labelled as such, not WCAG requirements: tooltip, tabs, modal, carousel, menu), and a «Tooltip and
  toggletip (last resort)» recipe that meets WCAG 1.4.13 (Esc dismiss, hoverable, persistent); notes
  that the APG tooltip pattern is still work in progress. Code written for this skill and run in the
  built-in browser; no screen readers tested.
- `SKILL.md` §4/§8: `role="menu"` is for application menus, not site navigation (`nav` + links with
  `aria-expanded` disclosure buttons, per APG Disclosure Navigation), and a `<select>` that navigates
  on change is a change of context on input (3.2.2).
- A scoped site-audit procedure and evidence workbook covering page/state inventory,
  cumulative WCAG A/AA scan configuration, manual protocols, support-control comparisons
  and optional institutional inclusion review. Linked from `SKILL.md` and both READMEs; the audit report
  now records evidence gaps and limits conclusions to evaluated coverage. These are
  instructions and templates, not a crawler, INFLESZ calculator or executed audit.
- `python scripts/search.py wcag --wcag-version 2.1|2.2`: filters by exact membership in the
  existing `versions` column (2.1: 50 records, 2.2: 58). Combines with `--id`, `--keyword`,
  `--level` and `--principle`; not available in `all` or the MCP server; without it results
  are unchanged. With `--level AAA` it prints a note to stderr because the catalog has no
  2.1 AAA criteria. Covered by new tests.

### Fixed
- `SKILL.md` Next.js example: no longer titled «focus management» while only adding a live region;
  now notes Next.js's built-in route announcer (avoid duplicating it) and shows an optional
  focus-to-`<h1>` component, with `app/layout.tsx` kept a Server Component.
- «production-ready» claims removed from `prompts/generate-aria-pattern.md` and the `SKILL.md`
  prompt index (the output is reference code to review and test); the Playwright+axe test is
  renamed to «no axe violations for the selected rules» since axe cannot prove WCAG conformance.
- `data/cognitive-accessibility.csv` COG008: no longer recommends the `title` attribute for tooltips
  (not keyboard/touch accessible; 1.4.13 user-agent tooltip exception); prefers visible labels.
- «Dark mode» toggle icon (SolidJS, Vue) now shows the current state instead of the opposite.
- `examples/components/carousel.html`: starts paused (Play visible), no longer resumes on
  `focusout`/`mouseleave` (only the user restarts it, per APG and WCAG 2.2.2), arrow keys on a dot
  advance one slide instead of two (single `keydown` handler), dots are plain buttons with
  `aria-current="true"` instead of `role="tab"` + `aria-selected`, and the header no longer
  claims a Space handler (Space/Enter work natively on the buttons); the arrow handler ignores
  Alt/Ctrl/Meta/Shift so browser shortcuts such as Alt+Left keep working.
- `examples/components/toast-notifications.html`: error toasts no longer use
  `role="alertdialog"` + `aria-modal="false"` without moving focus (plain group inside the live
  region); assertive region uses `aria-atomic="false"`; error toasts and the "Session expiring"
  toast persist until dismissed (APG alert: avoid alerts that disappear on their own), while
  success/info toasts stay timed and their progress bar and timer really pause on hover/focus (a
  courtesy, not a 2.2.1 option); the README cites 2.2.1 (Understanding Timing Adjustable) instead of 2.2.2.
- `examples/components/data-grid.html`: sortable headers are now `<th aria-sort><button>` (native
  Enter/Space) instead of `<th tabindex="0">` with custom key handling; removed the table
  `aria-label` that overrode the `<caption>` and the search `aria-label` that did not contain the
  visible "Search:" label (2.5.3); header and comments no longer describe an `aria-label` on sort
  buttons or cell navigation with Tab that the code does not have; the sort announcement uses the
  visible header text; `examples/components/README.md` now lists the data grid, and its tree-view
  and carousel rows were corrected to match the code and the APG.
- `examples/components/media-player.html`: CC and AD names now contain their visible text
  (2.5.3); the Play/Pause label follows the video's `play`, `pause` and `ended` events; header,
  comments and README no longer claim Space/Enter/arrow shortcuts that are only native control behavior.
- `examples/components/tree-view.html`: removed `aria-pressed` from node buttons and `aria-selected`
  from `<button>` (not allowed there); selection stays on the `treeitem` and the selected style now applies.
- Toggle buttons no longer change label and `aria-pressed` together: the SolidJS and Vue theme
  toggles in `SKILL.md` use a fixed "Dark mode" label with `aria-pressed`, and Play/Pause and
  Mute/Unmute in `examples/components/media-player.html` change only their label. Added a short
  rule to the button guidance in `SKILL.md` (source: WAI-ARIA APG button pattern).
- SolidJS theme toggle in `SKILL.md` computed the theme from the already-updated signal and inverted it; it now uses a local `next` value.
- `examples/components/README.md` no longer claims the examples are production-ready or
  keyboard and screen-reader tested; no such testing is recorded.
- `data/aria-patterns.csv` Tooltip row: Escape dismisses without moving focus, adds WCAG 1.4.13,
  and distinguishes name (`aria-labelledby`) from description (`aria-describedby`); notes that the
  APG tooltip pattern is work in progress.
- axe-core tag sets in `SKILL.md` and `templates/a11y-ci.yml` now include `wcag21a,wcag21aa`
  next to `wcag2a,wcag2aa,wcag22aa`, matching `references/site-audit-procedure.md`
  (source: axe-core `doc/API.md`).
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
