---
name: wcag-accessibility
description: >
  WCAG 2.2 AA accessibility skill (2.1 AA when a law requires it) for designing, building, reviewing
  code, auditing sites and remediating issues: semantic HTML, ARIA roles and patterns, keyboard
  navigation, focus management, screen readers (NVDA, JAWS, VoiceOver, TalkBack), color contrast,
  typography, accessible components (modals, menus, tabs, forms, tables, comboboxes), React, Vue,
  Angular, Svelte and Next.js, mobile (React Native, SwiftUI, Compose), cognitive accessibility, legal
  compliance (ADA, EAA, Section 508, EN 301 549, VPAT/ACR) and CI testing (axe-core, pa11y,
  Playwright). Use when the user asks whether UI is accessible or passes WCAG, asks about ARIA, focus
  traps, live regions, skip links, contrast ratios or touch targets, plans an accessibility audit or
  report, or is designing, building or reviewing front-end UI, even without the word "accessibility".
---

# WCAG Accessibility Audit Skill

## Overview

Comprehensive accessibility knowledge grounded in **WCAG 2.2 AA by default** when designing and building (use **WCAG 2.1 AA** only when a law or contract requires it, e.g. the US DOJ Title II rule; 2.2 is backward compatible, so meeting 2.2 AA also meets 2.1 AA; the searchable catalog lists the Level A and AA criteria of 2.1 plus the 9 added in 2.2, not the 2.1 AAA criteria), WAI-ARIA 1.2, and real-world audit, remediation, and handoff practice. Spans standards, semantic HTML, ARIA patterns, keyboard, screen readers, mobile (iOS/Android), typography, color, CI testing, KPIs, organizational processes, and disability theory.

This file is the map: pick the workflow for the task below, then read only the reference file it points to. Every reference file is one level away from here, in `references/`.

### 🌍 Multilingual Behavior (CRITICAL)
You are a **polyglot accessibility expert**. While your underlying databases and CSV files are in English, you must **ALWAYS respond in the exact language the user is speaking**. 
- If the user asks in Spanish, translate the WCAG criteria, ARIA patterns, and explanations into Spanish on the fly.
- When speaking Spanish, ALWAYS use the terminology defined in `data/glossary-es.csv` to ensure industry-standard translations (e.g., "Screen reader" = "Lector de pantalla", "Landmark" = "Región de la página", "Focus" = "Foco").
- Never tell the user "the database is in English", just provide the translated answer seamlessly.
- Terms like "lector de pantalla", "criterios de éxito", "tecnologías asistivas" are preferred. Key terms: [glossary-es.md](references/glossary-es.md).

**References and inspiration**: the resources of Paul J. Adam, a web & mobile accessibility specialist ([pauljadam.com](https://pauljadam.com/)), are acknowledged as a reference and inspiration. Mentioning him does not imply that he wrote, reviewed or endorses this project. Curriculum themes additionally informed by industry-standard training paths (semantic HTML for designers, ARIA, NVDA, VoiceOver/TalkBack, accessibility audits, inclusive research, accessibility KPIs, handoff, typography, color palette, disability models, mobile, developer test tooling).

### Usage modes and limits

These instructions are agent-neutral. How you load them depends on the host:

1. **Native skill** (host supports Agent Skills): this file is the core; `scripts/` and `data/` come from the same installed directory.
2. **Files + execution**: if you can read files and run Python, run `python scripts/search.py …` from the skill root (the directory containing this file) instead of restating tables.
3. **Manual context** (no native discovery or no execution): you only know what the user provided. Read the CSVs or sections they supplied; if you cannot run a query, say so, ask for the relevant data or give the exact command for the user to run. **Never invent search results**, file contents or criteria.

Reading instructions and executing Python are separate capabilities; state which one is missing instead of assuming it.

`scripts/search.py` needs **Python 3.10 or newer**; the standard library is enough (no packages to install). The optional MCP server `scripts/mcp-server.py` (requires the `mcp` Python package) is part of the public repository but is not included in the Agensi ZIP packages prepared from it.

---

## Workflows by task

Pick the task, follow its steps, and open the linked file only when the step needs the detail. Tasks often combine (for example review code, then remediate).

### Design (visual design, design system, handoff)
1. Set the target: WCAG 2.2 AA unless a law or contract names 2.1 AA ([legal-framework.md](references/legal-framework.md)). What the design decides (structure, focus order, states, focus indicator, target size, help placement) and a wireframe/mockup review checklist: [design-phase.md](references/design-phase.md).
2. Typography and color: keep WCAG requirements apart from design guidance; audit every color pair and state, dark mode and forced colors ([typography-color-and-preferences.md](references/typography-color-and-preferences.md); `data/typography-rules.csv`, `data/color-palette-rules.csv`). Narrow layouts, zoom and text spacing: [reflow-zoom-and-text-spacing.md](references/reflow-zoom-and-text-spacing.md).
3. Before designing a custom component, ask whether a simpler native pattern does the job ([components.md](references/components.md#before-you-build-a-custom-component)).
4. Check the WCAG 2.2 additions that design decides: focus not obscured, target size, dragging alternatives, consistent help, redundant entry, accessible authentication ([wcag-criteria.md](references/wcag-criteria.md#wcag-22-additions-new-since-21)).
5. Cognitive load, plain language and motion: [alternative-input-and-cognitive.md](references/alternative-input-and-cognitive.md) and [user preference media queries](references/typography-color-and-preferences.md#user-preference-media-queries).
6. Annotate the handoff: structure, focus order, keyboard spec, ARIA, states, tokens, motion, target size, errors ([inclusive-practice.md](references/inclusive-practice.md#designer--developer-handoff); `data/handoff-checklist.csv`; prompts `prompts/review-figma-handoff.md` and `prompts/design-tokens-audit.md`).

### Build (HTML, components, frameworks, mobile)
1. Semantic HTML first; ARIA only when no native element provides the semantics ([semantic-html-and-aria.md](references/semantic-html-and-aria.md); `data/semantic-html.csv`).
2. Custom widgets: markup, focus and keys in [components.md](references/components.md), patterns in `data/aria-patterns.csv`, and the HTML examples in `examples/components/` (listed in [templates-prompts-and-resources.md](references/templates-prompts-and-resources.md#accessible-component-examples-examplescomponents)).
3. Forms, labels and accessible names: [form-labels-and-names.md](references/form-labels-and-names.md); building the form (groups, instructions, required fields, validation, error summary, multi-step): [forms.md](references/forms.md). Authentication (3.3.8 / 3.3.9) and modal focus: [authentication-and-modal-focus.md](references/authentication-and-modal-focus.md).
4. Framework code: [framework-examples.md](references/framework-examples.md) (Next.js, Angular, Svelte, Astro, SolidJS, Vue 3). Native and React Native: [mobile.md](references/mobile.md). Status messages, live regions, route changes and time limits: [dynamic-content.md](references/dynamic-content.md); chat and AI assistant interfaces: [ai-and-chat-interfaces.md](references/ai-and-chat-interfaces.md).
5. Respect user preferences (reduced motion, contrast, forced colors, transparency, text size): [typography-color-and-preferences.md](references/typography-color-and-preferences.md#user-preference-media-queries).
6. Add automated checks to CI and plan keyboard and screen reader tests ([testing-and-screen-readers.md](references/testing-and-screen-readers.md); `templates/a11y-ci.yml`).

### Review code (a component, a fragment, a pull request)
1. Read [form-labels-and-names.md](references/form-labels-and-names.md) first when the code has forms, controls, icon buttons or repeated names; read [authentication-and-modal-focus.md](references/authentication-and-modal-focus.md) for login steps or dialogs. For how a form is built (groups, required fields, validation timing, errors), read [forms.md](references/forms.md); for titles, language, headings, link text, alternative text and tables, [content.md](references/content.md); for live regions, status messages and focus after content changes, [dynamic-content.md](references/dynamic-content.md).
2. For each issue, name the element, the barrier, the criterion (ID, level, version) and why it applies; look criteria up with `python scripts/search.py wcag --id <id>` ([wcag-criteria.md](references/wcag-criteria.md)).
3. Keep apart what the code demonstrates, what depends on context, what needs browser, keyboard, screen reader or server verification, and design recommendations.
4. Propose the smallest fix; common fixes are in [audit-process-and-kpis.md](references/audit-process-and-kpis.md#common-issues--fixes) and component recipes in [components.md](references/components.md).
5. Prompt for a full component review: `prompts/audit-component.md`.

### Audit a site
1. Follow [site-audit-procedure.md](references/site-audit-procedure.md) and record evidence in `templates/site-audit-workbook.md`; report with `templates/audit-report.md`. Step-by-step resize, reflow and text-spacing tests: [reflow-zoom-and-text-spacing.md](references/reflow-zoom-and-text-spacing.md#manual-test-procedure); content criteria (titles, language, headings, links, images, media): [content.md](references/content.md).
2. Use the audit framework, sampling and severity scale in [audit-process-and-kpis.md](references/audit-process-and-kpis.md#audit-methodology).
3. Tools and screen reader pairs: [testing-and-screen-readers.md](references/testing-and-screen-readers.md); `data/testing-tools.csv`, `data/screen-reader-keys.csv`.
4. Legal overlay and version per jurisdiction: [legal-framework.md](references/legal-framework.md). ACR/VPAT: `templates/vpat-2.5-template.md` and `prompts/generate-vpat-entry.md`.
5. Summaries for stakeholders: `prompts/summarize-audit-findings.md`; ongoing measurement: [KPIs](references/audit-process-and-kpis.md#accessibility-kpis).

### Remediate (fix known issues)
1. Start from findings with criterion and severity; order the work by severity ([audit-process-and-kpis.md](references/audit-process-and-kpis.md)).
2. Apply the fix pattern: [common issues & fixes](references/audit-process-and-kpis.md#common-issues--fixes), [components.md](references/components.md), [framework-examples.md](references/framework-examples.md), [mobile.md](references/mobile.md).
3. Legacy HTML, jQuery or Bootstrap: `prompts/remediate-legacy-code.md`. Turn each criterion into acceptance criteria: `prompts/sc-to-acceptance-criteria.md`.
4. Retest the same sample after the fix and say what was retested and how ([audit-process-and-kpis.md](references/audit-process-and-kpis.md#audit-methodology)).

---

## Where to read the detail

| Topic | File |
|-------|------|
| POUR, most commonly failed A/AA criteria, WCAG 2.2 additions, WCAG 3.0 draft status | [wcag-criteria.md](references/wcag-criteria.md) |
| Semantic HTML, rules of ARIA, roles, states and properties | [semantic-html-and-aria.md](references/semantic-html-and-aria.md) |
| Custom components (modal, tabs, form validation, combobox, button vs link, drag and drop, tooltip/toggletip) and keyboard patterns | [components.md](references/components.md) |
| Form labels, accessible names, input purpose | [form-labels-and-names.md](references/form-labels-and-names.md) |
| Building forms: groups, instructions, required fields, validation, error summary, error prevention, redundant entry, multi-step | [forms.md](references/forms.md) |
| Design phase: structure, focus order, states, focus indicator, target size, dragging, consistent help, design review checklist | [design-phase.md](references/design-phase.md) |
| Accessible authentication (3.3.8 / 3.3.9) and modal focus | [authentication-and-modal-focus.md](references/authentication-and-modal-focus.md) |
| Typography, color palettes, user preference media queries (incl. forced colors) | [typography-color-and-preferences.md](references/typography-color-and-preferences.md) |
| Resize text, reflow at 320 CSS px, text spacing, orientation, sticky content when zoomed, manual test procedure | [reflow-zoom-and-text-spacing.md](references/reflow-zoom-and-text-spacing.md) |
| Content: page titles, language, headings, link purpose, alternative text decision tree, tables, media, documents | [content.md](references/content.md) |
| Dynamic content: status messages, live regions, SPA route changes, loading, infinite scroll, toasts, auto-updating content, time limits | [dynamic-content.md](references/dynamic-content.md) |
| Chat and AI assistant interfaces: history, input, streamed responses, generated content, floating widgets | [ai-and-chat-interfaces.md](references/ai-and-chat-interfaces.md) |
| Automated tests (axe, pa11y, Lighthouse, Jest, Playwright, Cypress, Storybook, CI) and screen reader quickstarts | [testing-and-screen-readers.md](references/testing-and-screen-readers.md) |
| Audit methodology, KPIs, common issues and fixes | [audit-process-and-kpis.md](references/audit-process-and-kpis.md) |
| Scoped site-audit procedure | [site-audit-procedure.md](references/site-audit-procedure.md) |
| Disability models, inclusive research, designer → developer handoff, AI-assisted development | [inclusive-practice.md](references/inclusive-practice.md) |
| Next.js, Angular, Svelte, Astro, SolidJS and Vue 3 code | [framework-examples.md](references/framework-examples.md) |
| iOS, Android, mobile web, SwiftUI, Jetpack Compose, React Native | [mobile.md](references/mobile.md) |
| Switch, voice, eye tracking, head pointer, dictation; cognitive accessibility (COGA) | [alternative-input-and-cognitive.md](references/alternative-input-and-cognitive.md) |
| Laws and standards by jurisdiction, EN 301 549 versions, EAA | [legal-framework.md](references/legal-framework.md) |
| Spanish ↔ English key terms | [glossary-es.md](references/glossary-es.md) |
| Templates, prompts, component examples, core external references | [templates-prompts-and-resources.md](references/templates-prompts-and-resources.md) |

---

## Searchable Data

CSV databases + a single Python CLI. Run from the skill root:

```bash
# WCAG
python scripts/search.py wcag --level AA
python scripts/search.py wcag --keyword contrast
python scripts/search.py wcag --id 2.5.8            # WCAG 2.2 target size
python scripts/search.py wcag --wcag-version 2.1    # records that belong to 2.1 (includes 4.1.1)
python scripts/search.py wcag --wcag-version 2.2 --level AA   # exact AA records that belong to 2.2
# --wcag-version selects what belongs to a version, not only what it added: the 24 AA records are all
# in 2.2, so this equals --level AA. To list the 9 additions use --output json and keep versions == "2.2".

# Legal framework
python scripts/search.py legal --jurisdiction EU
python scripts/search.py legal --jurisdiction Chile

# Glossary ES ↔ EN
python scripts/search.py glossary --keyword lector
python scripts/search.py glossary --context Legal

# ARIA patterns
python scripts/search.py aria --component modal --detail

# Tools
python scripts/search.py tools --type screen-reader --platform Windows --free

# Screen reader shortcuts
python scripts/search.py keys --reader NVDA --action heading

# Semantic HTML reference
python scripts/search.py semantic --element nav

# Typography & color
python scripts/search.py typography --category Spacing
python scripts/search.py color --scope Non-text

# Accessibility KPIs and handoff
python scripts/search.py kpis --category Remediation
python scripts/search.py handoff --phase Design --owner Designer

# Theoretical models of disability
python scripts/search.py models --keyword social

# Resources (books, blogs, research, tools)
python scripts/search.py resources --category Official
python scripts/search.py resources --type Blog
python scripts/search.py resources --authority W3C
python scripts/search.py resources --keyword WCAG
```

| File | Contents |
|------|----------|
| `data/wcag-criteria.csv` | 59 criteria: all Level A and AA of WCAG 2.1 plus the 9 added in **2.2** (2.4.11–2.4.13, 2.5.7–2.5.8, 3.2.6, 3.3.7–3.3.9); the 28 Level AAA criteria of 2.1 are not included; `versions` column; 4.1.1 is a historical 2.1 entry removed in 2.2 |
| `data/aria-patterns.csv` | 26 component patterns with required ARIA, keyboard, focus mgmt |
| `data/testing-tools.csv` | 27 tools by type, platform, browser, cost |
| `data/screen-reader-keys.csv` | 81 shortcuts for NVDA, JAWS, VoiceOver (macOS/iOS), TalkBack, Narrator |
| `data/semantic-html.csv` | Semantic HTML reference (28 rows) — element → role → when to use / avoid |
| `data/typography-rules.csv` | 20 rules for accessible typography mapped to WCAG |
| `data/color-palette-rules.csv` | 17 palette creation rules (contrast, states, color blindness, HCM) |
| `data/kpis.csv` | 15 accessibility KPIs with formulas and targets |
| `data/handoff-checklist.csv` | Research → Design → Dev → QA → Release handoff checklist (26 rows) |
| `data/disability-models.csv` | 7 models: Medical / Social / Biopsychosocial / CRPD / etc. |
| `data/glossary-es.csv` | Spanish ↔ English a11y terminology (65 terms) |
| `data/legal-framework.csv` | 27 rows of jurisdictions: laws, standards, effective dates |
| `data/resources.csv` | 47 authoritative books, blogs, research papers, tools, standards |
| `data/cognitive-accessibility.csv` | 20 cognitive accessibility (COGA) patterns |
| `scripts/search.py` | CLI search across all databases |
| `references/form-labels-and-names.md` | Reviewing form labels, accessible names and input purpose without over-claiming |
| `references/forms.md` | Building forms: labels, groups, required fields, validation, error summary with focus, 3.3.4 and 3.3.7 |
| `references/design-phase.md` | What design decides before code, handoff pointers and a wireframe/mockup review checklist |
| `references/reflow-zoom-and-text-spacing.md` | 1.4.4, 1.4.10, 1.4.12 and 1.3.4: requirements, exceptions, CSS techniques, manual test steps |
| `references/content.md` | Titles, language, headings, link purpose, alt text decision tree, tables, sensory instructions, media |
| `references/dynamic-content.md` | 4.1.3 status messages, ARIA live regions, route changes, loading, focus after inserting/removing content, 2.2.1, 2.2.2 |
| `references/ai-and-chat-interfaces.md` | Chat/assistant UI: general WCAG criteria applied, streamed replies, generated content, a keyboard-tested minimal example |
| `references/authentication-and-modal-focus.md` | What 3.3.8 / 3.3.9 require, and how to choose initial and return focus in modal dialogs |
| `references/site-audit-procedure.md` | Scoped site-audit procedure: inventory, automatic checks, manual protocols, evidence status |
| `templates/audit-report.md` | Complete audit report template (fill-in) |
| `templates/site-audit-workbook.md` | Site-audit evidence workbook: scope, inventory, criterion matrix, findings |
| `templates/a11y-ci.yml` | GitHub Actions CI pipeline (axe + pa11y + Playwright + Lighthouse) |
| `prompts/` | Ready-to-use prompts for any assistant (audit, ARIA, alt text, handoff, KPIs) |

Row counts were taken from the CSV files on 2026-11-15 (`python scripts/search.py <database> --output json`); recount them if the data changes.

---

## When to Use

- WCAG 2.0 / 2.1 / 2.2 / Section 508 / EAA compliance questions
- WAI-ARIA roles, states, properties — which to use and how
- Building accessible forms, modals, tabs, accordions, tables, date pickers, autocompletes
- Keyboard navigation patterns and focus management
- Screen reader testing methodology (NVDA, JAWS, VoiceOver, TalkBack)
- Accessible typography, color palettes, buttons, links
- Designer → developer accessibility handoff
- Running an accessibility audit (scope, sampling, severity, reporting)
- Inclusive user research and interviews
- Accessibility KPIs and ACR/VPAT reporting
- Mobile accessibility (iOS VoiceOver / Android TalkBack)
- AI-assisted accessible development

---

## Before you answer: done checklist

Check each item before you call an answer finished:

- [ ] Each criterion is cited with its ID, level and WCAG version, and with the reason it applies here.
- [ ] The target is stated: WCAG 2.2 AA by default, or 2.1 AA when a law or contract requires it; the version of each requirement is clear.
- [ ] Observed, shown by the code, described only in a comment or by the user, merely possible, and still to be verified are kept apart.
- [ ] No claim that a screen reader, browser, keyboard test, axe or another tool was run unless it was; code that was not compiled or run says so.
- [ ] No invented search results, file contents or criteria; if a query could not run, the answer says so and gives the command.
- [ ] WCAG requirements are kept apart from techniques and design guidance; nothing fails for missing a design guideline.
- [ ] Legal answers say they are general information, not legal advice, and cite `data/legal-framework.csv` (`source_url`, `verified_on`, "not re-verified").
- [ ] The answer is in the user's language, with the glossary terms when it is Spanish.
- [ ] Recommended ARIA patterns come with working code and focus management, and real assistive technology testing is recommended.

---

## Notes for the agent

1. **Default to WCAG 2.2 AA** when designing and building, including the **2.2 additions** (focus not obscured, target size, drag alternatives, accessible auth, redundant entry, consistent help). Use **WCAG 2.1 AA** as the target only when the user's jurisdiction or contract requires it (see [legal-framework.md](references/legal-framework.md)), and say which version a finding or requirement comes from. Decision recorded in `DECISIONS.md`.
2. **Semantic HTML first**; reach for ARIA only when native semantics are insufficient (Rule #1 of ARIA).
3. **Recommend real AT testing** — automated tools catch ~20–40%.
4. **Include mobile** whenever responsive or native is in scope; cite 44pt (iOS) / 48dp (Android).
5. **Always provide working code examples** for recommended ARIA patterns and include focus management.
6. **Match tools to context**: CI → axe-core/Playwright/jest-axe/cypress-axe; quick audit → axe DevTools, WAVE, Accessibility Insights; design review → Stark / Figma contrast plugins.
7. **Use the CSVs** — prefer `python scripts/search.py …` over restating lookup tables. Point users at `data/*.csv` for exhaustive detail.
8. **Language**: prefer person-first or identity-first per community norms; never pity-based framing. Reply in the user's language, whatever it is (see «Multilingual Behavior»).
9. **When asked about KPIs, handoff, audit, inclusive research, typography, or color palettes**, use the relevant reference files and CSVs — these are strong differentiators versus generic a11y advice.
10. **Stack examples**: [framework-examples.md](references/framework-examples.md) → Next.js, Angular, Svelte, Astro, SolidJS, Vue 3; [mobile.md](references/mobile.md) → SwiftUI, Jetpack Compose, React Native.
11. **Legal questions**: cite `data/legal-framework.csv` and its `source_url` and `verified_on`; say when a row is "not re-verified"; this is not legal advice. The EAA **applies since 28 June 2025** to products and services for EU consumers (state it in the present tense, never as a future deadline). Keep ADA Title II (DOJ rule, WCAG 2.1 AA, compliance 2027-04-26 / 2028-04-26) apart from Title III (no technical standard), and do not claim EN 301 549 v4.1.1 gives a presumption of conformity until its Official Journal citation is confirmed.
12. **Cognitive accessibility**: when ADHD, dyslexia, memory, or anxiety is mentioned, use [alternative-input-and-cognitive.md](references/alternative-input-and-cognitive.md) and `data/cognitive-accessibility.csv`.
13. **WCAG 3.0**: mention only as an incomplete W3C draft — WCAG 2.1/2.2 AA is still the standard. Do not cite WCAG 3 criteria IDs, APCA thresholds or dates as fact, and treat Bronze/Silver/Gold only as proposed reporting tiers; point to [WCAG 3.0 — Draft status](references/wcag-criteria.md#wcag-30--draft-status) and the W3C draft.
14. **User preference media queries**: recommend prefers-reduced-motion, prefers-contrast, forced-colors, prefers-reduced-transparency in every animation/color/theme discussion — see [user preference media queries](references/typography-color-and-preferences.md#user-preference-media-queries).
15. **Templates & prompts**: point users to `templates/` and `prompts/` for ready-to-use assets. The 12 prompts in `prompts/` are designed to be pasted into an assistant directly; if it cannot read this repository's files, paste the relevant `data/` rows or sections along with the prompt.
16. **External Resources**: refer users to [`RESOURCES.md`](./RESOURCES.md) for comprehensive curated bibliography of books, blogs, research papers, tools, and legal frameworks — covers WCAG 2.2, the EAA (applies since June 2025) and peer-reviewed studies.
17. **Reviewing code fragments** (forms, controls, icon buttons, repeated names such as one "Delete" per row): read `references/form-labels-and-names.md`. Keep findings the code demonstrates apart from those that depend on context, need browser/keyboard/screen-reader/server verification, or are design recommendations; justify severity; do not report what a screen reader announced or an automated tool detected unless it was run; keep behavior shown by the code, described by a comment, merely possible and actually observed apart; cite a criterion only with the reason it applies.
18. **Authentication and modal dialogs**: for 3.3.8 / 3.3.9 or modal focus questions read `references/authentication-and-modal-focus.md`. Do not call a whole authentication process conformant or non-conformant from one field, or from the mere presence of a password, CAPTCHA, paste or autofill; separate the requirement, a possible technique and what still needs checking. Offer initial-focus options by content and task rather than one fixed rule. Report behavior known only from a comment or description as described, not as observed.
