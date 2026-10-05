<div align="center">

# ♿ wcag-accessibility-skill

**A Claude Code skill for web and mobile accessibility — grounded in WCAG 2.1/2.2 Level AA and Paul J. Adam's expertise.**

[![WCAG 2.2 AA](https://img.shields.io/badge/WCAG-2.2_AA-blueviolet?style=for-the-badge)](https://www.w3.org/WAI/standards-guidelines/wcag/)
[![Claude Code](https://img.shields.io/badge/Claude_Code-Skill-D97757?style=for-the-badge&logo=anthropic&logoColor=white)](https://claude.ai)
[![License: MIT](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](https://opensource.org/licenses/MIT)
[![Tests](https://img.shields.io/github/actions/workflow/status/mrKanoh/claude-wcag-accessibility-skill/test.yml?branch=main&label=tests&style=for-the-badge)](https://github.com/mrKanoh/claude-wcag-accessibility-skill/actions)

[🇪🇸 Leer en Español](./README-es.md)

<br>

[What it does](#-what-this-skill-does) • [Installation](#-installation) • [Searchable Databases](#searchable-databases) • [Skill Coverage](#skill-coverage) • [File Structure](#file-structure)

</div>

---

## ✨ What This Skill Does

This skill gives Claude comprehensive, actionable knowledge to help you:

* **🔍 Audit** websites and apps against WCAG 2.0 / 2.1 / 2.2 and Section 508.
* **🏗️ Build** accessible components: forms, modals, tabs, accordions, data tables, date pickers, autocompletes.
* **🎹 Implement** WAI-ARIA roles, states, and properties correctly.
* **🎧 Test** with real assistive technologies: NVDA, JAWS, VoiceOver, TalkBack.
* **⚙️ Set up** automated accessibility testing in CI/CD (axe-core, Playwright, Jest).
* **🎨 Evaluate** color contrast, keyboard navigation, focus management, and mobile touch targets.

> Comes with **searchable CSV databases** and a **Python search utility** — inspired by the `ui-ux-pro-max` skill architecture.

---

## 📦 Installation

### Claude Code (CLI / Desktop)

**The fastest way** — one command:

```bash
npx claude-code-templates@latest --skill accessibility/wcag-accessibility
```

**Or clone the full repository:**

```bash
# macOS / Linux
git clone https://github.com/mrKanoh/wcag-accessibility-skill.git ~/.claude/skills/wcag-accessibility

# Windows (PowerShell)
git clone https://github.com/mrKanoh/wcag-accessibility-skill.git "$env:USERPROFILE\.claude\skills\wcag-accessibility"
```

**Or copy just the skill file:**

```bash
# macOS / Linux
mkdir -p ~/.claude/skills/wcag-accessibility
curl -o ~/.claude/skills/wcag-accessibility/SKILL.md \
  https://raw.githubusercontent.com/mrKanoh/wcag-accessibility-skill/main/SKILL.md
```

Claude Code automatically discovers skills in `~/.claude/skills/`. No restart required.

---

## Searchable Databases

Run searches from the skill root:

```bash
# All WCAG AA criteria
python scripts/search.py wcag --level AA

# Criteria about contrast — output as JSON
python scripts/search.py wcag --keyword contrast --output json

# Export results to a file
python scripts/search.py wcag --level AA --output json --export aa-criteria.json

# Full ARIA spec for a modal dialog
python scripts/search.py aria --component modal --detail

# ARIA patterns involving keyboard focus
python scripts/search.py aria --keyword focus

# Free screen reader tools for Windows
python scripts/search.py tools --type screen-reader --platform Windows --free --url

# NVDA shortcuts for heading navigation
python scripts/search.py keys --reader NVDA --action heading

# Cognitive accessibility patterns (COGA)
python scripts/search.py cognitive --keyword memory
python scripts/search.py cognitive --user-group ADHD

# Cross-database search across all 14 databases at once
python scripts/search.py all --keyword contrast
python scripts/search.py all --keyword "focus" --output json

# Semantic HTML reference
python scripts/search.py semantic --element nav

# Accessible typography rules by category
python scripts/search.py typography --category Spacing

# Color palette rules
python scripts/search.py color --scope Non-text

# Accessibility KPIs
python scripts/search.py kpis --category Remediation

# Handoff checklist by phase / owner
python scripts/search.py handoff --phase Design --owner Designer

# Models of disability
python scripts/search.py models --keyword social

# Legal framework by jurisdiction
python scripts/search.py legal --jurisdiction EU
python scripts/search.py legal --jurisdiction Spain

# Curated resources
python scripts/search.py resources --category "Official Standards"
python scripts/search.py resources --type Blog --url
python scripts/search.py resources --authority W3C

# Spanish ↔ English glossary
python scripts/search.py glossary --keyword contrast
```

| File | Contents |
|------|----------|
| `data/wcag-criteria.csv` | 59 WCAG criteria: all Level A and AA of 2.1 plus the 9 added in **2.2** (2.4.11–2.4.13, 2.5.7–2.5.8, 3.2.6, 3.3.7–3.3.9). **Not complete:** the 28 Level AAA criteria of 2.1 are missing. `versions` column: `2.1`, `2.2` or `2.1;2.2`; 4.1.1 Parsing is a historical 2.1 entry, removed in 2.2 |
| `data/aria-patterns.csv` | 25+ component patterns · ARIA · keyboard · focus mgmt |
| `data/testing-tools.csv` | 30+ tools by type · platform · browser · cost |
| `data/screen-reader-keys.csv` | Shortcuts for NVDA · JAWS · VoiceOver (macOS/iOS) · TalkBack · Narrator |
| `data/semantic-html.csv` | Semantic HTML element → role → when to use / avoid |
| `data/typography-rules.csv` | 20 accessible typography rules mapped to WCAG |
| `data/color-palette-rules.csv` | Palette design rules (contrast, color-blindness, HCM, states) |
| `data/kpis.csv` | 15 accessibility KPIs with formulas, targets, cadence |
| `data/handoff-checklist.csv` | Research → Design → Dev → QA → Release handoff |
| `data/disability-models.csv` | Medical / Social / Biopsychosocial / CRPD / Identity |
| `data/glossary-es.csv` | Spanish ↔ English a11y glossary (70+ terms with definitions) |
| `data/legal-framework.csv` | 25+ jurisdictions: ADA, EAA, Section 508, AODA, LGPD, and more |
| `data/resources.csv` | 50+ curated books, blogs, research papers, tools, and standards |
| `data/cognitive-accessibility.csv` | 20 COGA patterns: ADHD, dyslexia, memory, anxiety, autism |
| `scripts/search.py` | CLI search across all **14 databases** · `wcag3` shows WCAG 3 draft status and W3C links only · `--output json/csv` · `--export` · `all` subcommand |
| `scripts/mcp-server.py` | Model Context Protocol server exposing all databases to Claude directly |
| `RESOURCES.md` | Human-readable bibliography — browse by category, W3C standards, academic research, etc. |
| `templates/audit-report.md` | Fill-in audit report template |
| `templates/a11y-ci.yml` | GitHub Actions pipeline (axe + pa11y + Playwright + Lighthouse) |
| `templates/vpat-2.5-template.md` | Official VPAT 2.5 Rev WCAG (A/AA/AAA · Section 508 · EN 301 549) |
| `templates/.pa11yci.json` | pa11y-ci config referenced by the CI pipeline |
| `templates/.lighthouserc.json` | Lighthouse CI config with accessibility assertions |
| `prompts/audit-component.md` | Prompt: audit a UI component |
| `prompts/sc-to-acceptance-criteria.md` | Prompt: WCAG SC → Gherkin ACs |
| `prompts/generate-alt-text.md` | Prompt: generate alt text |
| `prompts/review-figma-handoff.md` | Prompt: review design handoff |
| `prompts/summarize-audit-findings.md` | Prompt: exec summary from findings |
| `prompts/generate-aria-pattern.md` | Prompt: generate any accessible widget |
| `prompts/remediate-legacy-code.md` | Prompt: audit + fix legacy HTML/jQuery/Bootstrap |
| `prompts/generate-vpat-entry.md` | Prompt: translate audit findings into VPAT ACR language |
| `prompts/test-with-screen-reader.md` | Prompt: step-by-step NVDA/VoiceOver/TalkBack test scripts |
| `prompts/mobile-a11y-checklist.md` | Prompt: React Native / SwiftUI / Jetpack Compose checklist |
| `prompts/inclusive-ux-writing.md` | Prompt: plain language + inclusive terminology review |
| `prompts/design-tokens-audit.md` | Prompt: audit Figma/Style Dictionary tokens against WCAG |
| `examples/components/date-picker.html` | Date picker: dialog pattern, roving tabindex, Arrow keys, typed input |
| `examples/components/toast-notifications.html` | Toast system: `role="status"` + `role="alert"`, reduced motion |
| `examples/components/carousel.html` | Carousel: play/pause (WCAG 2.2.2), ARIA, auto-rotation, reduced motion |
| `examples/components/tree-view.html` | Tree View: expand/collapse, roving tabindex, full keyboard nav |
| `examples/components/combobox.html` | Combobox/Autocomplete: ARIA 1.2, real-time filtering, live region |
| `examples/components/data-grid.html` | Data Grid: aria-sort, select-all, pagination, search filter |
| `examples/components/media-player.html` | Media Player: Custom CC/AD toggles, accessible sliders |

---

## Trigger Examples

Claude loads this skill automatically when you ask things like:

- *"Is this button accessible?"*
- *"What's the correct ARIA pattern for a modal dialog?"*
- *"How do I test my site with NVDA?"*
- *"Does this color combination pass WCAG AA contrast?"*
- *"How do I make this form validation accessible?"*
- *"What keyboard shortcuts does VoiceOver use?"*
- *"Set up axe-core in my Playwright tests"*
- *"My React tab component isn't announcing correctly in JAWS"*
- *"What WCAG criterion covers focus visibility?"*

---

## Skill Coverage

This skill spans 7 interconnected domains to support accessibility work from research through release:

### 🎯 **Standards & Compliance**
Meet global accessibility requirements across WCAG, Section 508, and jurisdictional laws.

| Domain | What You Can Do |
|--------|-----------------|
| **WCAG & Standards** | Audit against WCAG 2.0 / 2.1 / 2.2, Section 508, EN 301 549, EAA, WAI-ARIA 1.2 |
| **Legal Framework** | Check 25+ jurisdictions (ADA, EAA, Section 508, AODA, LGPD, etc.) with scope & effective dates |
| **Accessibility KPIs** | Track 15 key metrics: violation density, MTTR, conformance rate, AC coverage |

**Example:** Query `python scripts/search.py legal --jurisdiction "EU"` → get EAA requirements for your product.

---

### 🎨 **Design & Content**

Build accessible designs and content from the start—avoid remediation costs later.

| Domain | What You Can Do |
|--------|-----------------|
| **Semantic HTML** | Reference all HTML elements with roles, ARIA equivalents, when to use/avoid |
| **Typography** | Apply 20 accessible typography rules (size, spacing, reflow, zoom, dyslexia-friendly) |
| **Color Palettes** | Design contrast-safe palettes: AA/AAA ratios, dark mode, forced-colors, color blindness |
| **Handoff Checklist** | Phase-by-phase checklist: Research → Design → Dev → QA → Release with owner responsibilities |

**Example:** Need to ensure your form design is accessible? Use the handoff checklist (Design phase section) to verify label placement, field grouping, and error messaging before handing to dev.

---

### 🛠️ **Implementation & Testing**

Choose the right tools and patterns for your tech stack.

| Domain | What You Can Do |
|--------|-----------------|
| **ARIA Patterns** | 25+ component patterns with keyboard behavior, focus management (modals, tabs, accordions, etc.) |
| **Components** | Build accessible UI: modals, tabs, accordions, forms, tables, date pickers, autocomplete, carousels |
| **Keyboard Navigation** | Tab order, focus management, arrow key patterns, detect and fix keyboard traps |
| **Screen Readers** | Test with NVDA, JAWS, VoiceOver (macOS + iOS), TalkBack (Android), Narrator—get platform-specific shortcuts |
| **Mobile Accessibility** | Touch targets, gesture alternatives, platform-specific testing checklists |

**Example:** Building a modal in React? Query `python scripts/search.py aria --component modal --detail` → get exact ARIA roles, focus trap code, and VoiceOver-tested patterns.

---

### 📊 **Testing & CI/CD**

Automate accessibility testing from pull request to production.

| Domain | What You Can Do |
|--------|-----------------|
| **Testing Tools** | 30+ tools by type (browser extensions, CLI, frameworks): axe DevTools, WAVE, Accessibility Insights, ARC Toolkit |
| **CI/CD** | GitHub Actions pipeline with axe-core, Playwright, Jest, and Lighthouse |
| **Stack Support** | Next.js App Router, Angular, Svelte, Astro, SolidJS, React (Radix UI), Vue 3, HTML+Vanilla JS, SwiftUI, Jetpack Compose |

**Example:** New Next.js app? Copy `templates/a11y-ci.yml` → add to your GitHub Actions → get automated a11y checks on every PR.

---

### 🧠 **Inclusive Design & Research**

Understand disability, research users, and document your process.

| Domain | What You Can Do |
|--------|-----------------|
| **Disability Models** | Learn medical, social, ICF, CRPD, and identity-based frameworks for accessibility |
| **Inclusive Research** | Plan user research: recruitment strategies, consent, modality, disability categories |
| **User Preferences** | Detect and respect browser/OS settings: prefers-reduced-motion, prefers-contrast, forced-colors |
| **Alternative Input** | Support diverse input methods: switch access, voice control, eye tracking, head pointer, cognitive a11y (COGA) |

**Example:** Designing a video feature? Respect `prefers-reduced-motion` to avoid motion sickness for vestibular users.

---

### 📚 **Reference & Localization**

Keep 13 searchable databases at your fingertips—in English and Spanish.

| Domain | What You Can Do |
|--------|-----------------|
| **Spanish Glossary** | 70+ a11y terms translated: English ↔ Spanish with context and definitions |
| **Ready-to-Use Prompts** | 6 Claude prompts for audit reports, alt text, ARIA patterns, design handoff review, findings summaries |

**Example:** Working with a Spanish-speaking team? Query `python scripts/search.py glossary-es --keyword contrast` → get the right terminology.

---

## File Structure

```
wcag-accessibility/
  ├─ SKILL.md                          ← Claude skill (28 sections, loaded by Claude Code)
  ├─ README.md                         ← This file
  ├─ CHANGELOG.md                      ← Version history
  ├─ CONTRIBUTING.md                   ← Contribution guide
  │
  ├─ data/                             ← 14 searchable databases
  │  ├─ wcag-criteria.csv              59 WCAG criteria (2.1 A/AA + 9 added in 2.2; no 2.1 AAA)
  │  ├─ aria-patterns.csv              25+ component patterns: keyboard, focus, roles
  │  ├─ testing-tools.csv              30+ tools: axe, WAVE, Accessibility Insights, etc.
  │  ├─ screen-reader-keys.csv         Shortcuts for NVDA, JAWS, VoiceOver, TalkBack, Narrator
  │  ├─ semantic-html.csv              HTML element → role → when to use/avoid
  │  ├─ typography-rules.csv           20 accessible typography rules mapped to WCAG
  │  ├─ color-palette-rules.csv        Palette design: AA/AAA contrast, HCM, CVD
  │  ├─ kpis.csv                       15 accessibility KPIs with formulas & targets
  │  ├─ handoff-checklist.csv          Research → Design → Dev → QA → Release checklist
  │  ├─ disability-models.csv          Medical, Social, ICF, CRPD, Identity frameworks
  │  ├─ glossary-es.csv                Spanish ↔ English a11y glossary (70+ terms)
  │  ├─ legal-framework.csv            25+ jurisdictions: ADA, EAA, Section 508, AODA, LGPD
  │  ├─ resources.csv                  50+ curated books, blogs, research, tools
  │  └─ cognitive-accessibility.csv    20 COGA patterns: ADHD, dyslexia, memory, anxiety
  │
  ├─ RESOURCES.md                      ← Human-readable bibliography by category
  │
  ├─ scripts/
  │  ├─ search.py                      ← CLI to query all 14 databases
  │  │                                    --output json/csv, --export, 'all' subcommand
  │  ├─ generate-resources-md.py       ← Auto-generate RESOURCES.md from CSV
  │  └─ mcp-server.py                  ← Model Context Protocol server
  │
  ├─ tests/
  │  └─ test_search.py                 ← pytest suite (39 tests, all pass)
  │
  ├─ templates/                        ← Ready-to-use files
  │  ├─ audit-report.md                Fill-in audit report template
  │  ├─ a11y-ci.yml                    GitHub Actions CI pipeline
  │  ├─ vpat-2.5-template.md           VPAT 2.5 Rev WCAG (A/AA/AAA + S508 + EN 301 549)
  │  ├─ .pa11yci.json                  pa11y-ci config
  │  └─ .lighthouserc.json             Lighthouse CI config with a11y assertions
  │
  ├─ examples/
  │  └─ components/                    ← 7 working accessible HTML components
  │     ├─ date-picker.html            Dialog pattern, roving tabindex, Arrow keys
  │     ├─ toast-notifications.html    Live regions: polite + assertive, reduced motion
  │     ├─ carousel.html               Play/pause (WCAG 2.2.2), ARIA, auto-rotation
  │     ├─ tree-view.html              Expand/collapse, roving tabindex, full keyboard
  │     ├─ combobox.html               ARIA 1.2, real-time filtering, live region
  │     ├─ data-grid.html              aria-sort, select-all, pagination, search filter
  │     └─ media-player.html           Custom CC/AD toggles, accessible sliders
  │
  ├─ prompts/                          ← 12 Claude prompts ready to copy-paste
  │  ├─ audit-component.md
  │  ├─ sc-to-acceptance-criteria.md
  │  ├─ generate-alt-text.md
  │  ├─ review-figma-handoff.md
  │  ├─ summarize-audit-findings.md
  │  ├─ generate-aria-pattern.md
  │  ├─ remediate-legacy-code.md
  │  ├─ generate-vpat-entry.md
  │  ├─ test-with-screen-reader.md
  │  ├─ mobile-a11y-checklist.md
  │  ├─ inclusive-ux-writing.md
  │  └─ design-tokens-audit.md
  │
  └─ .github/
     └─ ISSUE_TEMPLATE/
        ├─ bug_report.md
        └─ feature_request.md
```

### How to Use Each Database

```bash
# Query WCAG AA criteria
python scripts/search.py wcag --level AA

# Find ARIA patterns for modals with focus management details
python scripts/search.py aria --component modal --detail

# Get all screen reader shortcuts for heading navigation
python scripts/search.py keys --reader NVDA --action heading

# Find tools that work on Windows and are free
python scripts/search.py tools --platform Windows --free

# Look up Spanish terminology
python scripts/search.py glossary-es --keyword "contrast"

# Check legal requirements for EU
python scripts/search.py legal --jurisdiction "EU"
```

---

## Attribution & Credits

This skill is based on the work and expertise of **Paul J. Adam**, Web & Mobile Accessibility Specialist/Consultant based in Austin, TX.

Paul provides enterprise-level accessibility consulting across government, financial, healthcare, and technology sectors, and has been a leading voice in the web accessibility community for over a decade.

- **Website**: [pauljadam.com](https://pauljadam.com/)
- **Specialty**: WCAG compliance, WAI-ARIA, iOS/Android accessibility, screen reader testing

Additional standards and references:
- [W3C Web Content Accessibility Guidelines (WCAG 2.1)](https://www.w3.org/TR/WCAG21/)
- [WAI-ARIA Authoring Practices Guide](https://www.w3.org/WAI/ARIA/apg/)
- [WebAIM](https://webaim.org/)
- [Deque axe-core](https://github.com/dequelabs/axe-core)
- [The A11Y Project](https://www.a11yproject.com/)

---

## Contributing

Improvements, corrections, and new component patterns are welcome.
See [`CONTRIBUTING.md`](./CONTRIBUTING.md) for full guidelines, commit conventions,
component checklist, and how to run the tests.

```bash
# Run the test suite
pip install pytest
pytest tests/ -v

# Regenerate RESOURCES.md from the CSV
python scripts/generate-resources-md.py
```

Quick areas that could grow:
- More accessible component examples (data grid, rich text editor, combobox multi-select)
- Additional ARIA patterns
- More localization of Spanish-language a11y terminology
- Remediation cost/effort estimation heuristics

---

## License

MIT — free to use, share, and adapt with attribution.
