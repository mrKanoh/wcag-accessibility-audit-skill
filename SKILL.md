---
name: wcag-accessibility
description: >
  WCAG 2.1/2.2 AA accessibility skill: audits, remediation, ARIA roles and patterns, keyboard
  navigation, focus management, screen reader behavior (NVDA, JAWS, VoiceOver, TalkBack), color
  contrast, accessible components (modals, menus, tabs, forms, tables, comboboxes), React, Vue,
  Angular, Svelte and Next.js, mobile a11y (React Native, SwiftUI, Compose), cognitive accessibility,
  legal compliance (ADA, EAA, Section 508, EN 301 549, VPAT/ACR) and CI testing (axe-core, pa11y,
  Playwright). Use when the user asks whether UI is accessible or passes WCAG, asks about ARIA,
  focus traps, live regions, skip links, contrast ratios or touch targets, or is building or
  reviewing front-end UI, even without the word "accessibility".
---

# Paul J. Adam Web & Mobile Accessibility Skill

## Overview

Comprehensive accessibility knowledge grounded in **WCAG 2.1 AA by default** (with full **WCAG 2.2** coverage), WAI-ARIA 1.2, and real-world audit, remediation, and handoff practice. Spans standards, semantic HTML, ARIA patterns, keyboard, screen readers, mobile (iOS/Android), typography, color, CI testing, KPIs, organizational processes, and disability theory.

### 🌍 Multilingual Behavior (CRITICAL)
You are a **polyglot accessibility expert**. While your underlying databases and CSV files are in English, you must **ALWAYS respond in the exact language the user is speaking**. 
- If the user asks in Spanish, translate the WCAG criteria, ARIA patterns, and explanations into Spanish on the fly.
- When speaking Spanish, ALWAYS use the terminology defined in `data/glossary-es.csv` to ensure industry-standard translations (e.g., "Screen reader" = "Lector de pantalla", "Landmark" = "Región de la página", "Focus" = "Foco").
- Never tell the user "the database is in English", just provide the translated answer seamlessly.

**Authority**: Paul J. Adam — Web & Mobile Accessibility Specialist/Consultant ([pauljadam.com](https://pauljadam.com/)). Curriculum themes additionally informed by industry-standard training paths (semantic HTML for designers, ARIA, NVDA, VoiceOver/TalkBack, accessibility audits, inclusive research, accessibility KPIs, handoff, typography, color palette, disability models, mobile, developer test tooling).

---

## Searchable Data

CSV databases + a single Python CLI. Run from the skill root:

```bash
# WCAG
python scripts/search.py wcag --level AA
python scripts/search.py wcag --keyword contrast
python scripts/search.py wcag --id 2.5.8            # WCAG 2.2 target size

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
| `data/wcag-criteria.csv` | WCAG 2.1 A/AA + **WCAG 2.2** additions (2.4.11–2.4.13, 2.5.7–2.5.8, 3.2.6, 3.3.7–3.3.9) |
| `data/aria-patterns.csv` | 25+ component patterns with required ARIA, keyboard, focus mgmt |
| `data/testing-tools.csv` | 30+ tools by type, platform, browser, cost |
| `data/screen-reader-keys.csv` | Shortcuts for NVDA, JAWS, VoiceOver (macOS/iOS), TalkBack, Narrator |
| `data/semantic-html.csv` | Semantic HTML reference — element → role → when to use / avoid |
| `data/typography-rules.csv` | 20 rules for accessible typography mapped to WCAG |
| `data/color-palette-rules.csv` | Palette creation rules (contrast, states, color blindness, HCM) |
| `data/kpis.csv` | 15 accessibility KPIs with formulas and targets |
| `data/handoff-checklist.csv` | Research → Design → Dev → QA → Release handoff checklist |
| `data/disability-models.csv` | Medical / Social / Biopsychosocial / CRPD / etc. |
| `data/glossary-es.csv` | Spanish ↔ English a11y terminology (70+ terms) |
| `data/legal-framework.csv` | 25+ jurisdictions: laws, standards, effective dates |
| `data/resources.csv` | 50+ authoritative books, blogs, research papers, tools, standards |
| `scripts/search.py` | CLI search across all databases |
| `templates/audit-report.md` | Complete audit report template (fill-in) |
| `templates/a11y-ci.yml` | GitHub Actions CI pipeline (axe + pa11y + Playwright + Lighthouse) |
| `prompts/` | Ready-to-use Claude prompts (audit, ARIA, alt text, handoff, KPIs) |

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

## 1. Disability Models & Inclusive Mindset

Design decisions depend on which model of disability you implicitly assume. Prefer **Social** and **Human Rights (CRPD)** models; use **Biopsychosocial (WHO ICF)** when discussing context and interaction.

| Model | View | Design implication |
|-------|------|--------------------|
| **Medical** | Impairment to fix | Assistive devices; risk of pathologizing users |
| **Social** | Barriers disable people, not impairments | Remove barriers; universal design |
| **Biopsychosocial (ICF)** | Interaction of body, activity, participation, environment | Consider context & situational limitations |
| **Human Rights (CRPD)** | Access is a right | Accessibility is mandatory, not charity |
| **Charity** (avoid) | Pity-driven | Paternalistic design |
| **Identity / Affirmative** | Disability as valued identity | Co-design with disabled users |

> Full table: `data/disability-models.csv`

**Language**: use person-first ("person with a disability") or identity-first ("Deaf person", "autistic person") as the community prefers; avoid "suffers from", "wheelchair-bound", "handicapped", "special needs", "normal".

**Global statistics (WHO 2023)**: ~1.3 billion people — 16% of the world's population — live with a significant disability. Plan for permanent, temporary, and situational impairments.

---

## 2. WCAG Principles (POUR)

| Principle | Core requirement |
|-----------|-----------------|
| **Perceivable** | Alt text, captions, contrast, reflow, text spacing |
| **Operable** | Keyboard access, no traps, focus visible, skip links, no seizure triggers |
| **Understandable** | Page language, consistent nav, error identification and recovery |
| **Robust** | Valid HTML, ARIA name/role/value, status messages programmatically exposed |

### High-impact AA criteria (most commonly failed)

| ID | Criterion | Requirement |
|----|-----------|-------------|
| 1.1.1 | Non-text Content | `alt` for informative; `alt=""` for decorative |
| 1.3.1 | Info and Relationships | Semantic structure preserved programmatically |
| 1.4.3 | Contrast (Minimum) | 4.5:1 text / 3:1 large (18pt or 14pt bold) |
| 1.4.10 | Reflow | Usable at 320 CSS px with no horizontal scroll |
| 1.4.11 | Non-text Contrast | 3:1 vs adjacent colors for visual info needed to identify UI components and states (e.g. an author-styled focus indicator) and graphics needed to understand content; exceptions: inactive components, user-agent default appearance not modified by the author, essential graphics |
| 1.4.12 | Text Spacing | Supports line-height 1.5, paragraph 2×, letter 0.12×, word 0.16× |
| 2.1.1 | Keyboard | All functionality operable by keyboard |
| 2.1.2 | No Keyboard Trap | Focus must never get stuck |
| 2.4.3 | Focus Order | Logical focus sequence |
| 2.4.7 | Focus Visible | A keyboard focus indicator must be visible (sets no contrast ratio; see 1.4.11 / 2.4.13) |
| 3.3.1 | Error Identification | Errors described in text |
| 4.1.2 | Name, Role, Value | Interactive elements expose name/role/state |
| 4.1.3 | Status Messages | Dynamic updates announced without focus move |

### WCAG 2.2 additions (new since 2.1)

| ID | Level | Criterion | What changed |
|----|-------|-----------|--------------|
| 2.4.11 | AA | **Focus Not Obscured (Minimum)** | Focused element can't be entirely hidden by author-created content such as sticky UI (no contrast requirement) |
| 2.4.12 | AAA | Focus Not Obscured (Enhanced) | …or *partially* hidden |
| 2.4.13 | AAA | Focus Appearance | Indicator area ≥ a 2 CSS px perimeter of the unfocused component, and 3:1 between the same pixels focused vs unfocused; exceptions: user-agent indicator, or indicator and its background not modified by the author |
| 2.5.7 | AA | **Dragging Movements** | Drag operations need a single-pointer alternative |
| 2.5.8 | AA | **Target Size (Minimum)** | Pointer targets ≥ 24×24 CSS px (exceptions apply) |
| 3.2.6 | A | **Consistent Help** | Help mechanisms in consistent relative order |
| 3.3.7 | A | **Redundant Entry** | Don't force re-entry of already-provided info |
| 3.3.8 | AA | **Accessible Authentication (Minimum)** | No cognitive-function tests (allow paste, password manager, WebAuthn) |
| 3.3.9 | AAA | Accessible Authentication (Enhanced) | No cognitive-function tests at all |

> Full criteria database: `data/wcag-criteria.csv`

---

## 3. Semantic HTML First

**Rule of thumb**: semantic HTML > ARIA. Only reach for ARIA when no native element provides the semantics.

```html
<header>       <!-- role=banner at top-level -->
<nav aria-label="Primary">
<main>         <!-- exactly one per page -->
<aside>        <!-- role=complementary -->
<footer>       <!-- role=contentinfo at top-level -->
<section aria-labelledby="h">  <!-- region if labeled -->
<article>
<h1>…<h6>      <!-- never skip levels; one h1 per page -->
<button type="button">   <!-- actions -->
<a href="/x">            <!-- navigation -->
<ul><li>        <dl><dt><dd>
<table><caption><thead><th scope="col">
<label for="id">  <fieldset><legend>
<details><summary>        <!-- native disclosure -->
<dialog>                  <!-- with showModal() for focus trap -->
```

**Common mistake**: using `<div onclick>` for a button — breaks keyboard, SR, and focus. Always prefer `<button>`.

> Full element reference: `data/semantic-html.csv`

---

## 4. WAI-ARIA Quick Reference

### Three rules of ARIA
1. Don't use ARIA if a native element exists.
2. Don't change native semantics unless you really must.
3. All interactive ARIA controls must be keyboard-operable and have an accessible name.

### Essential roles
```html
role="dialog"      aria-modal="true"
role="alertdialog"
role="alert"                             <!-- assertive live region -->
role="status"                            <!-- polite live region -->
role="tablist" role="tab" role="tabpanel"
role="combobox" role="listbox" role="option"
role="grid" role="row" role="gridcell"
role="progressbar" role="slider" role="switch"
role="tree" role="treeitem"
role="menu" role="menuitem"
```

### Essential properties & states
```html
aria-label="Close"
aria-labelledby="heading-id"
aria-describedby="hint-id"
aria-expanded="true|false"
aria-selected="true|false"
aria-checked="true|false|mixed"
aria-hidden="true"                 <!-- never on focusable elements -->
aria-live="polite|assertive"
aria-invalid="true"
aria-required="true"
aria-modal="true"
aria-disabled="true"
aria-sort="ascending|descending"
aria-current="page|step|date|true"
aria-haspopup="menu|listbox|dialog|grid|tree"
aria-activedescendant="id"
aria-controls="id"
aria-owns="id"
```

> Full component patterns: `data/aria-patterns.csv`

---

## 5. Accessible Components

### Modal Dialog
```html
<div role="dialog" aria-modal="true" aria-labelledby="title" aria-describedby="desc">
  <h2 id="title">Confirm Delete</h2>
  <p id="desc">This action cannot be undone.</p>
  <button>Delete</button>
  <button aria-label="Close dialog">×</button>
</div>
```
- Move focus to first focusable element inside on open
- Return focus to trigger on close
- Tab cycles within dialog; Escape closes
- Background: `inert` (or `aria-hidden="true"` with care)

### Tab Panel
```html
<div role="tablist" aria-label="Account settings">
  <button role="tab" id="t1" aria-selected="true"  aria-controls="p1">Profile</button>
  <button role="tab" id="t2" aria-selected="false" aria-controls="p2" tabindex="-1">Security</button>
</div>
<div role="tabpanel" id="p1" aria-labelledby="t1">…</div>
<div role="tabpanel" id="p2" aria-labelledby="t2" hidden>…</div>
```
- Arrow keys switch tabs; Home/End jump to first/last
- Active tab `tabindex="0"`; inactive `tabindex="-1"` (roving tabindex)

### Accessible Form Validation
```html
<label for="email">Email <span aria-hidden="true">*</span></label>
<input id="email" type="email"
       autocomplete="email"
       aria-required="true"
       aria-invalid="true"
       aria-describedby="email-help email-error">
<span id="email-help">We'll never share it.</span>
<span id="email-error" role="alert">Enter a valid email address.</span>
```

### Combobox (Autocomplete)
```html
<label for="search">Search</label>
<input id="search" type="text" role="combobox"
       aria-expanded="true" aria-haspopup="listbox"
       aria-controls="results" aria-autocomplete="list"
       aria-activedescendant="opt-2">
<ul id="results" role="listbox">
  <li id="opt-1" role="option">Apple</li>
  <li id="opt-2" role="option" aria-selected="true">Avocado</li>
</ul>
```

### Accessible Button vs. Link (WCAG 2.2 friendly)
```html
<!-- Action → button -->
<button type="button" aria-pressed="false">Like</button>

<!-- Navigation → link -->
<a href="/dashboard">Dashboard</a>

<!-- Icon button (always needs accessible name) -->
<button aria-label="Delete item">
  <svg aria-hidden="true" focusable="false">…</svg>
</button>
```
- Targets ≥ **24×24 CSS px** (WCAG 2.5.8). 44×44 recommended for touch.
- Visible focus ring (WCAG 2.4.7); if you style it, ≥ 3:1 vs adjacent colors (WCAG 1.4.11). 2.4.13 (AAA) adds size and focused-vs-unfocused contrast.
- Never rely on color alone for state (e.g., disabled, selected).

### Accessible Drag & Drop (WCAG 2.5.7)
Always provide a non-drag alternative:
```html
<ul role="listbox" aria-label="Reorder items">
  <li>Item A
    <button aria-label="Move up">↑</button>
    <button aria-label="Move down">↓</button>
  </li>
</ul>
```

---

## 6. Accessible Typography

| Rule | Recommendation | WCAG |
|------|----------------|------|
| Body size | ≥ 16 px / 1rem | 1.4.4 |
| Line height | ≥ 1.5× font size | 1.4.12 |
| Paragraph spacing | ≥ 2× font size | 1.4.12 |
| Letter / word spacing | 0.12× / 0.16× supported | 1.4.12 |
| Line length | 45–75 characters | 1.4.8 AAA |
| Alignment | Left-align LTR; avoid justified | 1.4.8 AAA |
| Reflow | Usable at 320 CSS px width | 1.4.10 |
| Zoom | Works at 200% (AA) / 400% reflow | 1.4.4 / 1.4.10 |
| Contrast | 4.5:1 body / 3:1 large | 1.4.3 |
| Avoid all-caps for long copy | Reduces legibility & SR may spell | — |
| Body weight ≥ 400 | Avoid 100–300 for paragraphs | 1.4.3 |
| Dyslexia-friendly faces | Atkinson Hyperlegible, Lexend, Inter | — |
| No text-in-images | Use real text (logos exempt) | 1.4.5 |

```css
/* Text-spacing user override test — content must not be clipped */
* {
  line-height: 1.5 !important;
  letter-spacing: 0.12em !important;
  word-spacing: 0.16em !important;
}
p { margin-bottom: 2em !important; }
```

> Full ruleset: `data/typography-rules.csv`

---

## 7. Accessible Color Palettes

### Contrast matrix (WCAG 2.1 / 2.2)

| Context | Ratio |
|---------|-------|
| Body text (AA) | 4.5:1 |
| Large text (AA) — 18pt / 14pt bold | 3:1 |
| Body text (AAA) | 7:1 |
| UI components / icons / borders | 3:1 (1.4.11) |
| Author-styled focus indicator vs adjacent colors | 3:1 (1.4.11; 2.4.7 requires it to be visible) |
| Focus indicator, same pixels focused vs unfocused (AAA) | 3:1 plus size rule (2.4.13) |

### Palette design workflow
1. Define semantic tokens: `text`, `text-muted`, `bg`, `surface`, `border`, `primary`, `success`, `warning`, `error`, `focus`.
2. For each token, define **default / hover / active / focus / disabled** variants.
3. Audit every *pair* used in UI against the matrix.
4. Test in **dark mode**, **high contrast mode** (`forced-colors: active`), and color-blindness simulators (deuteranopia, protanopia, tritanopia).
5. Never encode meaning in color alone — pair with icon, text, or pattern.

```css
/* Windows High Contrast Mode support */
@media (forced-colors: active) {
  button { border: 1px solid ButtonText; }
  :focus-visible { outline: 2px solid CanvasText; }
}
```

> Full rules: `data/color-palette-rules.csv`

---

## 8. Keyboard Interaction Patterns

| Widget | Keys |
|--------|------|
| Link | Tab, Enter |
| Button | Tab, Enter, Space |
| Checkbox / Switch | Tab, Space |
| Radio group | Tab onto group; Arrow keys between |
| Select / Listbox | Tab, Arrows, Home/End, type-ahead |
| Combobox | Tab, Arrows, Enter, Esc |
| Tabs | Tab to list; Arrow keys switch; Enter/Space activate |
| Menu / Menu bar | Arrow keys, Enter, Esc, Tab exits |
| Dialog | Tab cycles inside; Esc closes |
| Tree | Arrows (→ expand, ← collapse), Enter activates |
| Grid / Data table | Arrow keys between cells; Enter activates cell editor |
| Slider | Arrow keys, Home/End, PgUp/PgDn |
| Date picker | Arrow keys calendar, PgUp/PgDn months |

---

## 9. Audit Methodology

Structured audit framework (matches professional curriculum):

```
1. Scope       Sample pages (home, template types, auth, checkout, top 10 by traffic)
2. Standard    WCAG 2.1/2.2 level (usually AA); jurisdictional overlays (Section 508, EN 301 549, EAA)
3. Automated   axe DevTools + Lighthouse + WAVE → baseline violations
4. Keyboard    Tab through every flow; verify reachability + visible focus
5. Screen AT   NVDA+Firefox, VoiceOver+Safari, TalkBack+Chrome
6. Visual      Zoom 200% & 400%; reflow 320 px; text-spacing override
7. Manual SC   Check non-automatable criteria (1.3.1 structure, 2.4.3 order, 3.3.x errors, 2.5.x target size, 2.4.11 focus obscured)
8. Findings    One row per issue: URL · element · criterion · severity · steps · recommendation
9. Severity    Critical / Serious / Moderate / Minor (align to Deque or internal scale)
10. Report     Executive summary, remediation plan, VPAT/ACR update, retest plan
```

**Sampling guidance**: choose representative templates rather than every page. Re-audit the same sample after remediation to measure regression.

**ACR/VPAT**: maintain a current Accessibility Conformance Report mapping every WCAG SC → Supports / Partially Supports / Does Not Support / Not Applicable with rationale.

---

## 10. Inclusive Research & Interviews

- Recruit across disability categories: vision (blind, low-vision, color-blind), hearing (Deaf, HoH), motor (switch, voice, limited dexterity), cognitive (dyslexia, ADHD, memory), speech, seizure sensitivity.
- Ask about **assistive tech** (AT), customization (zoom level, magnifier, reduced motion) and environment (lighting, bandwidth, noise).
- Provide accessible recruitment materials (captioned videos, plain language, screen-reader-friendly forms).
- Offer **choice of modality** (video with captions, audio only, async written, in-person).
- Compensate equitably; avoid extractive research.
- Reflect findings back to participants; credit collaboration.

**Consent**: explicit recorded consent; right to pause/withdraw without penalty.

---

## 11. Designer → Developer Handoff

Handoff artifacts a designer must include:
- **Semantic structure**: headings, landmarks, lists marked in the design
- **Focus order**: numbered arrows through interactive elements
- **Keyboard spec**: which keys do what for each custom component
- **ARIA annotations**: role, accessible name, states
- **Component states**: default / hover / active / focus / selected / disabled / error
- **Contrast-audited tokens**: every pair with ratio documented
- **Motion**: `prefers-reduced-motion` alternative
- **Target size**: ≥ 24×24 CSS px (ideally 44×44 for touch)
- **Errors & status**: inline + live region pattern

> Full phase-by-phase checklist: `data/handoff-checklist.csv` (Research → Design → Dev → QA → Release).

---

## 12. Accessibility KPIs

Measure what you ship, not only what you scan.

| KPI | Target | Cadence |
|-----|--------|---------|
| Axe violations per 1k DOM nodes | < 1.0 | Per build |
| WCAG AA conformance rate (pages) | 100% | Quarterly |
| Critical issues open | 0 | Weekly |
| MTTR (mean time to remediate) | < 14 days | Monthly |
| Keyboard task completion rate | ≥ 95% | Per release |
| Screen reader task success rate | ≥ 90% | Per release |
| Focus-visible coverage | 100% | Per build |
| Alt text presence on informative images | 100% | Per build |
| VPAT/ACR freshness | ≤ 180 days | Quarterly |
| Accessibility AC coverage in user stories | ≥ 90% | Sprint |

> Full KPI catalog: `data/kpis.csv`

---

## 13. Testing: Automation + Manual

### Automated — recipes

```bash
# axe-core CLI
npx @axe-core/cli https://example.com --tags wcag2a,wcag2aa,wcag22aa

# pa11y (wraps axe + HTML_CodeSniffer)
npx pa11y https://example.com --standard WCAG2AA

# Lighthouse
npx lighthouse https://example.com --only-categories=accessibility
```

### Jest + Testing Library + jest-axe
```ts
import { render } from '@testing-library/react';
import { axe, toHaveNoViolations } from 'jest-axe';
expect.extend(toHaveNoViolations);

test('modal has no a11y violations', async () => {
  const { container } = render(<MyModal open />);
  expect(await axe(container)).toHaveNoViolations();
});
```

### Playwright + axe
```ts
import { test } from '@playwright/test';
import AxeBuilder from '@axe-core/playwright';

test('homepage passes WCAG 2.2 AA', async ({ page }) => {
  await page.goto('/');
  const results = await new AxeBuilder({ page })
    .withTags(['wcag2a', 'wcag2aa', 'wcag22aa'])
    .analyze();
  expect(results.violations).toEqual([]);
});
```

### Cypress + cypress-axe
```js
cy.visit('/');
cy.injectAxe();
cy.checkA11y(null, { runOnly: { type: 'tag', values: ['wcag2a', 'wcag2aa', 'wcag22aa'] } });
```

### Storybook a11y addon
```js
// .storybook/main.js
export default { addons: ['@storybook/addon-a11y'] };
```

### GitHub Actions
```yaml
- name: a11y tests
  run: |
    npm ci
    npm test -- --testPathPattern=a11y
    npx playwright test --grep @a11y
```

> Reminder: automated scans catch ~20–40% of issues. Always pair with keyboard and real AT.

---

## 14. Screen Reader Testing

| Reader | OS | Pair with | Cost |
|--------|-----|-----------|------|
| **NVDA** | Windows | Firefox or Chrome | Free |
| **JAWS** | Windows | Chrome or Edge | Paid |
| **Narrator** | Windows | Edge | Built-in |
| **VoiceOver** | macOS / iOS | Safari | Built-in |
| **TalkBack** | Android | Chrome | Built-in |

### NVDA quickstart (Windows)
- **Insert** is the NVDA modifier key (or CapsLock in laptop layout).
- **Ctrl** silences speech.
- **H / Shift+H** next/previous heading.
- **F / B / L / T / K** next form field / button / list / table / link.
- **Insert+F7** elements list (headings, links, form fields).
- **Insert+Space** toggle browse / focus mode.

### VoiceOver (macOS) — VO = Control+Option
- **VO+Right/Left** next/prev element
- **VO+U** rotor (headings, links, form controls…)
- **VO+Space** activate
- **VO+Command+H** next heading
- **VO+Shift+M** context menu

### VoiceOver (iOS)
- Swipe right/left → navigate; double-tap → activate
- Three-finger swipe → scroll
- Two-finger rotation → rotor
- Three-finger triple-tap → screen curtain

### TalkBack (Android)
- Swipe right/left → navigate
- Double-tap → activate
- Two-finger swipe → scroll
- Swipe up then right → global context menu

> Full shortcut catalog: `data/screen-reader-keys.csv`

---

## 15. Mobile Accessibility

### iOS (VoiceOver)
- Touch targets ≥ **44×44 pt**
- `accessibilityLabel`, `accessibilityHint`, `accessibilityTraits` set correctly
- Custom gestures must have single-tap alternatives
- Dynamic Type: respect user font size (`UIFontMetrics`)
- Reduce Motion: honor `UIAccessibility.isReduceMotionEnabled`
- Test in **Accessibility Inspector** (Xcode)

### Android (TalkBack)
- Touch targets ≥ **48×48 dp**
- `contentDescription` on non-text elements
- `android:labelFor` to link labels to inputs
- `importantForAccessibility="no"` on decorative views
- Support large font scale and high-contrast text
- Test with **Accessibility Scanner** app

### Web on mobile
- Respect `prefers-reduced-motion`, `prefers-contrast`, `prefers-color-scheme`
- Use `<input type="email|tel|number|url|search">` for correct keyboards
- `autocomplete` tokens (`email`, `name`, `street-address`, `postal-code`, `cc-number`…)
- Avoid hover-only affordances (no hover on touch)

---

## 16. AI-Assisted Accessible Development

- **Generate alt text drafts** with vision models; review & edit — never ship unreviewed.
- **Explain ARIA patterns** but verify against the [APG](https://www.w3.org/WAI/ARIA/apg/) — LLMs can hallucinate roles/states.
- **Translate WCAG to user stories**: convert each failing SC to acceptance criteria.
- **Summarize audit findings** into exec-friendly language while preserving SC IDs.
- **Accessibility code review**: use LLMs to flag likely issues (missing labels, `div`-as-button, color-only meaning) as a *supplement*, not a replacement, for real testing.
- **Caution**: LLMs often suggest ARIA where semantic HTML would be correct. Apply Rule #1 of ARIA.

---

## 17. Common Issues & Fixes

| Issue | Fix |
|-------|-----|
| Missing alt text | Descriptive `alt` for informative; `alt=""` for decorative |
| Poor color contrast | ≥ 4.5:1 body, 3:1 large (1.4.3) |
| No keyboard support | `<button>`; or `tabindex="0"` + Enter/Space handlers |
| Invisible focus | `:focus-visible { outline: 2px solid; }`; never `outline: none` |
| Missing form labels | `<label for="id">` or `aria-label` / `aria-labelledby` |
| Bad heading hierarchy | h1→h2→h3 in order |
| ARIA misuse | Semantic HTML first |
| Focus trapped in modal | Tab wraps inside; Escape closes; focus returns to trigger |
| Unlabeled icon button | `aria-label` on `<button>` + `aria-hidden="true"` on SVG |
| Auto-playing media | Pause/stop control within 3s |
| AJAX content not announced | `aria-live="polite"` region; inject content into it |
| Color as sole conveyor | Add text, icon, or pattern |
| Sticky header hides focus (2.4.11) | `scroll-padding-top: <header-height>` |
| Small tap targets (2.5.8) | ≥ 24×24 CSS px; spacing can satisfy |
| Drag-only reorder (2.5.7) | Provide ↑/↓ buttons or menu |
| Password paste blocked (3.3.8) | Allow paste; allow password managers |

---

## 18. Stack-Specific Code Examples

### Next.js App Router — Focus management on navigation
```tsx
// app/layout.tsx — announce route changes to screen readers
'use client';
import { usePathname } from 'next/navigation';
import { useEffect, useRef } from 'react';

export default function RootLayout({ children }: { children: React.ReactNode }) {
  const pathname = usePathname();
  const announceRef = useRef<HTMLParagraphElement>(null);

  useEffect(() => {
    if (announceRef.current) {
      announceRef.current.textContent = `Navigated to ${document.title}`;
    }
  }, [pathname]);

  return (
    <html lang="en">
      <body>
        {/* Visually hidden live region for route announcements */}
        <p
          ref={announceRef}
          aria-live="polite"
          aria-atomic="true"
          className="sr-only"
        />
        <a href="#main-content" className="skip-link">Skip to main content</a>
        {children}
      </body>
    </html>
  );
}
```

### Angular — Accessible reactive form
```typescript
// login.component.ts
import { Component } from '@angular/core';
import { ReactiveFormsModule, FormBuilder, Validators } from '@angular/forms';

@Component({
  selector: 'app-login',
  standalone: true,
  imports: [ReactiveFormsModule],
  template: `
    <form [formGroup]="form" (ngSubmit)="submit()" novalidate>
      <div>
        <label for="email">Email <span aria-hidden="true">*</span></label>
        <input
          id="email"
          type="email"
          formControlName="email"
          autocomplete="email"
          [attr.aria-invalid]="email.invalid && email.touched"
          [attr.aria-describedby]="email.invalid && email.touched ? 'email-error' : null"
          aria-required="true"
        />
        <span
          id="email-error"
          role="alert"
          *ngIf="email.invalid && email.touched"
        >
          {{ email.hasError('required') ? 'Email is required' : 'Enter a valid email' }}
        </span>
      </div>
      <button type="submit" [disabled]="form.invalid">Log in</button>
    </form>
  `
})
export class LoginComponent {
  form = this.fb.group({ email: ['', [Validators.required, Validators.email]] });
  get email() { return this.form.controls.email; }
  constructor(private fb: FormBuilder) {}
  submit() { /* … */ }
}
```

### Svelte 5 — Accessible modal with focus trap
```svelte
<script>
  import { onMount } from 'svelte';
  let { open = false, onClose } = $props();
  let dialogEl;

  $effect(() => {
    if (open) dialogEl?.showModal();
    else dialogEl?.close();
  });
</script>

<dialog
  bind:this={dialogEl}
  aria-labelledby="dialog-title"
  aria-describedby="dialog-desc"
  on:close={onClose}
  on:click|self={onClose}
>
  <h2 id="dialog-title">Confirm action</h2>
  <p id="dialog-desc">This cannot be undone.</p>
  <menu>
    <li><button on:click={onClose}>Cancel</button></li>
    <li><button class="primary">Confirm</button></li>
  </menu>
</dialog>

<!-- Native <dialog> provides focus trap, Escape key, and aria-modal automatically -->
```

### Astro — Accessible island with ARIA
```astro
---
// Card.astro
export interface Props { title: string; href: string; description: string; }
const { title, href, description } = Astro.props;
---
<article aria-labelledby={`card-title-${title.replace(/\s/g,'-')}`}>
  <h3 id={`card-title-${title.replace(/\s/g,'-')}`}>
    <a href={href}>{title}</a>
  </h3>
  <p>{description}</p>
</article>
```

### SolidJS — Accessible toggle button
```tsx
import { createSignal } from 'solid-js';

export function ThemeToggle() {
  const [isDark, setIsDark] = createSignal(false);

  const toggle = () => {
    setIsDark(d => !d);
    document.documentElement.dataset.theme = isDark() ? 'light' : 'dark';
  };

  return (
    <button
      type="button"
      aria-pressed={isDark()}
      aria-label={isDark() ? 'Switch to light mode' : 'Switch to dark mode'}
      onClick={toggle}
    >
      {isDark() ? '☀️' : '🌙'}
    </button>
  );
}
```

---

## 19. Native Mobile — Code Examples

### SwiftUI (iOS / iPadOS / macOS)

```swift
// Accessible custom card
struct CourseCard: View {
    let title: String
    let instructor: String
    let duration: String
    let isCompleted: Bool

    var body: some View {
        VStack(alignment: .leading) {
            Text(title).font(.headline)
            Text(instructor).font(.subheadline)
            Text(duration).font(.caption)
        }
        .accessibilityElement(children: .combine)
        .accessibilityLabel("\(title), by \(instructor), \(duration)")
        .accessibilityHint(isCompleted ? "Completed" : "Double tap to open course")
        .accessibilityAddTraits(isCompleted ? .isSelected : [])
    }
}

// Accessible form field
struct EmailField: View {
    @Binding var email: String
    @State private var isInvalid = false

    var body: some View {
        VStack(alignment: .leading) {
            TextField("Email", text: $email)
                .textContentType(.emailAddress)
                .keyboardType(.emailAddress)
                .autocapitalization(.none)
                .accessibilityLabel("Email address")
                .accessibilityHint("Enter your email address")
                .accessibilityValue(isInvalid ? "Invalid email format" : "")
            if isInvalid {
                Text("Enter a valid email address")
                    .foregroundColor(.red)
                    .accessibilityLiveRegion(.assertive)
            }
        }
    }
}

// Respect system accessibility settings
@main
struct MyApp: App {
    @Environment(\.accessibilityReduceMotion) var reduceMotion
    @Environment(\.accessibilityInvertColors) var invertColors
    @Environment(\.sizeCategory) var sizeCategory  // Dynamic Type

    var body: some Scene {
        WindowGroup { ContentView() }
    }
}
```

### Jetpack Compose (Android)

```kotlin
// Accessible card
@Composable
fun CourseCard(
    title: String,
    instructor: String,
    duration: String,
    isCompleted: Boolean,
    onClick: () -> Unit
) {
    Card(
        modifier = Modifier
            .clickable(onClick = onClick)
            .semantics {
                contentDescription = "$title, by $instructor, $duration" +
                    if (isCompleted) ", completed" else ""
                role = Role.Button
            }
    ) {
        Column(modifier = Modifier.padding(16.dp)) {
            Text(title, style = MaterialTheme.typography.titleMedium)
            Text(instructor, style = MaterialTheme.typography.bodyMedium)
            Text(duration, style = MaterialTheme.typography.bodySmall)
        }
    }
}

// Accessible text field with error
@Composable
fun EmailField(email: String, onValueChange: (String) -> Unit, isError: Boolean) {
    OutlinedTextField(
        value = email,
        onValueChange = onValueChange,
        label = { Text("Email") },
        isError = isError,
        keyboardOptions = KeyboardOptions(keyboardType = KeyboardType.Email),
        supportingText = {
            if (isError) {
                Text(
                    "Enter a valid email address",
                    modifier = Modifier.semantics { liveRegion = LiveRegionMode.Assertive }
                )
            }
        },
        modifier = Modifier
            .fillMaxWidth()
            .semantics {
                if (isError) error("Enter a valid email address")
            }
    )
}

// Reduce motion
@Composable
fun AnimatedContent() {
    val reduceMotion = LocalAccessibilityManager.current?.isReduceMotionEnabled ?: false
    val animationSpec = if (reduceMotion) snap() else tween(300)
    // use animationSpec in animations
}
```

---

## 20. User Preference Media Queries

Always respect OS/browser-level accessibility preferences. Never override them.

### prefers-reduced-motion
```css
/* Default: animate freely */
.card { transition: transform 0.3s ease; }

/* User opted out of motion */
@media (prefers-reduced-motion: reduce) {
  .card { transition: none; }
  /* Or provide an instant/fade alternative */
  .card { transition: opacity 0.1s linear; }
}
```

```js
// JS: check before triggering animations
const prefersReduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
if (!prefersReduced) { element.animate(keyframes, options); }
```

### prefers-color-scheme (dark mode)
```css
:root {
  --text: #1a1a1a;
  --bg: #ffffff;
}
@media (prefers-color-scheme: dark) {
  :root {
    --text: #f0f0f0;
    --bg: #121212;
  }
}
/* Re-check all contrast pairs in both modes */
```

### prefers-contrast
```css
/* High contrast mode request (not forced-colors) */
@media (prefers-contrast: more) {
  :root {
    --text: #000000;
    --bg: #ffffff;
    --border: #000000;
  }
  button { border: 2px solid #000; }
}

/* Reduced contrast (e.g. users with migraine) */
@media (prefers-contrast: less) {
  :root { --text: #444; }
}
```

### forced-colors (Windows High Contrast Mode)
```css
/* System replaces your colors — don't fight it */
@media (forced-colors: active) {
  /* Use system color keywords */
  button {
    border: 1px solid ButtonText;
    background: ButtonFace;
    color: ButtonText;
  }
  :focus-visible {
    outline: 2px solid Highlight;
  }
  /* Restore SVG icons hidden by forced-colors */
  svg { forced-color-adjust: none; fill: CanvasText; }
}
```

### prefers-reduced-transparency
```css
@media (prefers-reduced-transparency: reduce) {
  .overlay { background: rgba(0,0,0,0.9); /* instead of 0.5 */ }
  .frosted { backdrop-filter: none; background: var(--bg-solid); }
}
```

### prefers-reduced-data (emerging)
```css
@media (prefers-reduced-data: reduce) {
  /* Don't load decorative images or heavy fonts */
  .hero-bg { background-image: none; }
}
```

### Dynamic Type / text resize
```css
/* Use relative units everywhere — never px for type */
html { font-size: 100%; }   /* respect browser base */
body { font-size: 1rem; }
h1   { font-size: clamp(1.5rem, 5vw, 3rem); }
```

---

## 21. Alternative Input Methods

Users with motor disabilities may use input methods beyond keyboard and mouse. Design and test for all of them.

### Switch Access (1–2 buttons)

- iOS: Settings → Accessibility → Switch Control
- Android: Settings → Accessibility → Switch Access
- Behavior: single-switch or two-switch scanning through focusable elements
- **Requirements**: logical focus order; no time-limited actions; adequate target size

**Test yourself**: enable Switch Control (iOS) or Switch Access (Android) with a Bluetooth keyboard spacebar as the switch.

### Voice Control / Dragon NaturallySpeaking

- iOS: Settings → Accessibility → Voice Control
- Android: Voice Access app (Google)
- Windows: Dragon NaturallySpeaking, Windows Voice Access
- Users say element names or grid coordinates to activate elements

**Requirements**:
- Visible label text must match (or be contained in) the accessible name — WCAG 2.5.3 Label in Name
- Unique visible labels for all interactive elements (no duplicate "Learn more" links)
- `aria-label` must contain the visible text, not replace it

```html
<!-- ❌ Label in Name failure: aria-label replaces visible text -->
<button aria-label="Course details">Learn more</button>

<!-- ✅ aria-label extends visible text -->
<button aria-label="Learn more about HTML Semántico">Learn more</button>
```

### Eye Tracking (Tobii, Eyegaze)

- Users dwell on elements to activate them; no keyboard or pointer precision
- **Requirements**: large targets (44×44pt minimum), no hover-only UI, no time-limited interactions, minimal cognitive load

### Head Pointer / Mouth Stick

- Like mouse but reduced precision
- **Requirements**: adequate spacing between targets (WCAG 2.5.8), no drag-only interactions (WCAG 2.5.7)

### Dictation (macOS built-in, Google Docs Voice Typing)

- Passive dictation into text fields
- **Requirements**: `autocomplete` attributes, no auto-correcting input values, visible editable boundaries

### Cognitive accessibility (COGA)

- Plain language: reading level ≤ grade 8 for general content
- Consistent navigation and labeling (WCAG 3.2.3 / 3.2.4)
- Error recovery: suggest corrections (3.3.3), allow undo (3.3.4)
- No time limits or extend them (2.2.1)
- Accessible authentication — no cognitive puzzles (WCAG 3.3.8)
- Break complex processes into steps; show progress
- Use icons alongside text for reinforcement

---

## 22. Legal Framework

Compliance is often mandatory. Key jurisdictions:

| Region | Law | Standard | Applies to | Effective |
|--------|-----|----------|------------|-----------|
| 🇺🇸 USA (federal) | Section 508 | WCAG 2.0 AA | Federal ICT | 2017 |
| 🇺🇸 USA (private) | ADA Titles II & III | WCAG 2.1 AA (DOJ 2024 rule) | State/local govt + public accommodations | 2024+ |
| 🇪🇺 EU | EAA (Directive 2019/882) | EN 301 549 / WCAG 2.1 AA | B2C products & services | **28 Jun 2025** |
| 🇪🇺 EU | Web Accessibility Directive | EN 301 549 | Public sector websites & apps | In force |
| 🇬🇧 UK | Equality Act + PSBAR 2018 | WCAG 2.1 AA | Public sector | In force |
| 🇨🇦 Canada | ACA | WCAG 2.1 AA | Federal entities | In force |
| 🇨🇦 Ontario | AODA | WCAG 2.0 AA | Public + large private | Full since 2021 |
| 🇦🇺 Australia | DDA + Digital Service Standard | WCAG 2.1 AA | Government | Active |
| 🇧🇷 Brazil | LBI (Lei 13.146) + eMAG | WCAG 2.1 AA | Public + private collective use | Active |
| 🇨🇱 Chile | Ley 20.422 + Decreto 1 | WCAG 2.0 AA | Government | Active |
| 🇲🇽 Mexico | NOM-034 / Ley GID | WCAG 2.1 AA | Public sector | Evolving |
| 🇪🇸 Spain | RD 1112/2018 (WAD transposition) | EN 301 549 | Public sector | Active |
| 🇫🇷 France | RGAA 4 + Loi 2005-102 | WCAG 2.1 AA via RGAA | Public + large companies | Active |

> Full table with enforcement and notes: `data/legal-framework.csv`
> Search: `python scripts/search.py legal --jurisdiction "Chile"`

**EAA 2025 alert**: Private sector digital products and services (e-commerce, banking, transport, e-books, streaming) serving EU consumers must comply by **28 June 2025**.

---

## 23. Spanish ↔ English Glossary

Key terms for Spanish-speaking teams:

| English | Spanish |
|---------|---------|
| accessibility | accesibilidad |
| accessible name | nombre accesible |
| accessibility tree | árbol de accesibilidad |
| alt text | texto alternativo |
| assistive technology | tecnología asistiva / tecnología de apoyo |
| color contrast | contraste de color |
| focus indicator | indicador de foco |
| focus management | gestión del foco |
| heading | encabezado / título |
| keyboard trap | trampa de teclado |
| landmark | punto de referencia |
| live region | región en vivo |
| screen reader | lector de pantalla |
| semantic HTML | HTML semántico |
| skip link | enlace de salto |
| status message | mensaje de estado |
| success criterion | criterio de éxito |
| target size | tamaño de objetivo |
| WCAG | Pautas de Accesibilidad para el Contenido Web |

> Full glossary (70+ terms, with definitions and context): `data/glossary-es.csv`
> Search: `python scripts/search.py glossary --keyword lector`

---

## 24. Templates & Prompts

### Templates (ready to fill)

| File | Purpose |
|------|---------|
| `templates/audit-report.md` | Complete audit report with finding blocks, severity scale, conformance table, retest plan |
| `templates/a11y-ci.yml` | GitHub Actions pipeline: jest-axe + axe CLI + pa11y-ci + Playwright + Lighthouse |
| `templates/vpat-2.5-template.md` | Official VPAT 2.5 Rev WCAG — covers WCAG 2.x (A/AA/AAA), Section 508, EN 301 549 |

### Prompts for Claude (copy & paste)

| File | When to use |
|------|-------------|
| `prompts/audit-component.md` | Get a full a11y audit of a component with WCAG SC + code fixes |
| `prompts/sc-to-acceptance-criteria.md` | Convert WCAG success criteria to Gherkin ACs for a user story |
| `prompts/generate-alt-text.md` | Draft alt text for informative or complex images |
| `prompts/review-figma-handoff.md` | Review a design handoff for a11y gaps before dev |
| `prompts/summarize-audit-findings.md` | Exec-friendly summary of raw findings with 90-day plan |
| `prompts/generate-aria-pattern.md` | Generate production-ready accessible widget in any framework |
| `prompts/remediate-legacy-code.md` | Audit + fix legacy HTML/jQuery/Bootstrap code for accessibility |
| `prompts/generate-vpat-entry.md` | Translate audit findings into VPAT ACR language |
| `prompts/test-with-screen-reader.md` | Generate step-by-step NVDA/VoiceOver/TalkBack test scripts |
| `prompts/mobile-a11y-checklist.md` | React Native, SwiftUI, Jetpack Compose accessibility checklist |
| `prompts/inclusive-ux-writing.md` | Review UI copy for plain language and inclusive terminology |
| `prompts/design-tokens-audit.md` | Audit Figma/Style Dictionary tokens against WCAG contrast requirements |

### Accessible component examples (`examples/components/`)

| File | What it demonstrates |
|------|---------------------|
| `examples/components/date-picker.html` | Full date picker: dialog pattern, roving tabindex, Arrow/Page/Home/End keys, typed input, live region errors |
| `examples/components/toast-notifications.html` | Toast system: `role="status"` (polite) + `role="alert"` (assertive), dismiss, reduced-motion support |

---

## 25. Comprehensive Resource Repository

📚 **See [`RESOURCES.md`](./RESOURCES.md) for a complete, curated repository of:**
- Official W3C/WAI standards & guidelines
- Practical implementation guides (2024–2025)
- Academic research & systematic reviews
- Blogs, communities & education
- Testing tools & frameworks (axe, WAVE, Lighthouse, etc.)
- Recommended books & courses
- Legal frameworks by jurisdiction
- Case studies & accessible websites

---

## 26. Core References

### Official Standards & Specifications

- [WCAG 2.2 Recommendation](https://www.w3.org/TR/WCAG22/) — Official W3C standard
- [WCAG 2.2 Quick Reference](https://www.w3.org/WAI/WCAG22/quickref/) — Filterable by level, principle
- [Understanding WCAG 2.2](https://www.w3.org/WAI/WCAG22/Understanding/) — Detailed explanations & techniques
- [WAI-ARIA Authoring Practices Guide (APG)](https://www.w3.org/WAI/ARIA/apg/) — 25+ component patterns with code
- [WCAG Evaluation Methodology (WCAG-EM)](https://w3c.github.io/wai-wcag-em/) — Structured audit framework
- [WCAG2Mobile](https://www.w3.org/WAI/mobile/) — Applying WCAG to mobile apps
- [WCAG2ICT](https://w3c.github.io/wcag2ict/) — Applying WCAG to non-web ICT

### Practical Guides (2024–2025)

- [AllAccessible: WCAG 2.2 Complete Compliance Guide](https://www.allaccessible.org/blog/wcag-22-complete-guide-2025) — 9 new criteria patterns
- [Deque: Beginner's Guide to Web Accessibility](https://www.deque.com/web-accessibility-beginners-guide/) — Entry-level foundations
- [Usercentrics: Mastering WCAG 2.2 & Inclusive Design](https://usercentrics.com/knowledge-hub/mastering-web-app-accessibility-wcag2-2-and-inclusive-design/)

### Academic Research

- [Accessibility Engineering: Systematic Literature Review (152 papers)](https://pmc.ncbi.nlm.nih.gov/articles/PMC9881526/) — 2010–2021 methodologies
- [WCAG 2.2 & ADA 2024: Policy Impact (PRISMA 2020)](https://www.researchgate.net/publication/396366120_Policy_in_Practice_A_Systematic_Review_of_WCAG_22_and_ADA_2024_Effects_on_Web_and_Mobile_Accessibility) — Regulatory compliance effects
- [Cognitive Disabilities: Rapid Evidence Assessment](https://pmc.ncbi.nlm.nih.gov/articles/PMC8869505/) — Specific needs & WCAG gaps
- [Web Accessibility in Universities (UK Study)](https://journals.sagepub.com/doi/full/10.1177/21582440211056614) — 349 institutions; 80% below AA
- [How WCAG Compliance Shapes User Experience](https://www.sciencedirect.com/science/article/pii/S1071581922001756) — Evidence on real-world impact

### Blogs & Communities

- [WebAIM](https://webaim.org/) — 25 years of free resources, 1 monthly newsletter
- [WebAIM Blog](https://webaim.org/blog/feed/) — Weekly updates on standards & tools
- [The A11Y Project](https://www.a11yproject.com/) — Community, events, curriculum
- [Inclusive Components (Heydon Pickering)](https://inclusive-components.design/) — Component patterns with inclusivity focus
- [Paul J. Adam](https://pauljadam.com/) — Specialist in web & mobile accessibility
- [Deque: Accessible Design Hub](https://www.deque.com/accessible-design/)

### Component Libraries & Pattern Libraries

- [WAI-ARIA Authoring Practices Guide (APG)](https://www.w3.org/WAI/ARIA/apg/) — 25+ patterns with live examples
- [React Aria (Adobe)](https://react-spectrum.adobe.com/react-aria/) — Accessible React components & hooks
- [Radix UI](https://www.radix-ui.com/) — Unstyled, accessible component library
- [USWDS (US Web Design System)](https://designsystem.digital.gov/) — Government standards
- [Inclusive Components](https://inclusive-components.design/) — Design-first patterns

### Testing & Automation

- [axe-core (Deque)](https://github.com/dequelabs/axe-core) — De facto standard automated testing engine
- [WAVE (WebAIM)](https://wave.webaim.org/) — Visual accessibility feedback
- [Lighthouse (Google)](https://developers.google.com/web/tools/lighthouse) — Built into Chrome
- [pa11y](https://pa11y.org/) — CLI & CI integration
- [jest-axe](https://github.com/nickcolley/jest-axe) — Jest + Testing Library integration
- [@axe-core/playwright](https://github.com/dequelabs/axe-core-npm/tree/develop/packages/playwright) — Playwright integration
- [cypress-axe](https://github.com/component-driven/cypress-axe) — Cypress integration

### Human Rights & Disability Models

- [UN Convention on the Rights of Persons with Disabilities (CRPD)](https://www.un.org/development/desa/disabilities/convention-on-the-rights-of-persons-with-disabilities.html) — Legal framework
- [WHO International Classification of Functioning (ICF)](https://www.who.int/standards/classifications/international-classification-of-functioning-disability-and-health) — Biopsychosocial model
- [Disability Models in Design (Social, Medical, Identity-First)](https://www.a11yproject.com/) — Frameworks for inclusive thinking

---

## 25. Vue 3 Accessibility Examples

### Accessible reactive form (Composition API)
```vue
<script setup lang="ts">
import { ref, computed } from 'vue';

const email = ref('');
const touched = ref(false);
const isInvalid = computed(() => touched.value && !/^[^@]+@[^@]+\.[^@]+$/.test(email.value));
const errorId = 'email-error';
const hintId  = 'email-hint';
</script>

<template>
  <form @submit.prevent="handleSubmit" novalidate>
    <div>
      <label for="email">
        Email address <span aria-hidden="true">*</span>
      </label>
      <input
        id="email"
        v-model="email"
        type="email"
        autocomplete="email"
        aria-required="true"
        :aria-invalid="isInvalid || undefined"
        :aria-describedby="[hintId, isInvalid ? errorId : ''].filter(Boolean).join(' ')"
        @blur="touched = true"
      />
      <span :id="hintId">We will never share your email.</span>
      <span
        v-if="isInvalid"
        :id="errorId"
        role="alert"
      >
        Enter a valid email address.
      </span>
    </div>
    <button type="submit" :disabled="isInvalid">Subscribe</button>
  </form>
</template>
```

### Accessible modal (Vue 3 + Teleport)
```vue
<script setup lang="ts">
import { ref, watch, nextTick } from 'vue';
const props = defineProps<{ open: boolean }>();
const emit  = defineEmits<{ (e: 'close'): void }>();
const closeBtn = ref<HTMLButtonElement | null>(null);

watch(() => props.open, async (val) => {
  if (val) {
    await nextTick();
    closeBtn.value?.focus(); // Move focus into dialog
  }
});

function handleKeydown(e: KeyboardEvent) {
  if (e.key === 'Escape') emit('close');
}
</script>

<template>
  <!-- Teleport out of current DOM tree so aria-modal works correctly -->
  <Teleport to="body">
    <div
      v-if="open"
      role="dialog"
      aria-modal="true"
      aria-labelledby="modal-title"
      aria-describedby="modal-desc"
      @keydown="handleKeydown"
    >
      <h2 id="modal-title">Confirm action</h2>
      <p id="modal-desc">This cannot be undone.</p>
      <button ref="closeBtn" @click="emit('close')">Cancel</button>
      <button class="primary">Confirm</button>
    </div>
    <!-- Backdrop -->
    <div v-if="open" aria-hidden="true" @click="emit('close')" />
  </Teleport>
</template>
```

### Accessible toggle button (Vue 3)
```vue
<script setup lang="ts">
import { ref } from 'vue';
const isDark = ref(false);
function toggle() {
  isDark.value = !isDark.value;
  document.documentElement.dataset.theme = isDark.value ? 'dark' : 'light';
}
</script>

<template>
  <button
    type="button"
    :aria-pressed="isDark"
    :aria-label="isDark ? 'Switch to light mode' : 'Switch to dark mode'"
    @click="toggle"
  >
    {{ isDark ? '☀️' : '🌙' }}
  </button>
</template>
```

### Live region (Vue 3)
```vue
<script setup lang="ts">
import { ref } from 'vue';
const announcement = ref('');
function save() {
  // ... save logic ...
  announcement.value = 'Document saved successfully.';
  setTimeout(() => { announcement.value = ''; }, 3000);
}
</script>

<template>
  <!-- Visually hidden live region -->
  <div aria-live="polite" aria-atomic="true" class="sr-only">
    {{ announcement }}
  </div>
  <button type="button" @click="save">Save</button>
</template>
```

---

## 26. React Native Accessibility

React Native accessibility maps to the same WCAG principles but uses platform-specific APIs.

### Core props
```tsx
import {
  View, Text, TouchableOpacity, TextInput,
  AccessibilityInfo, findNodeHandle
} from 'react-native';

// ── Accessible card (combines children into one focus target)
function CourseCard({ title, instructor, isCompleted }: Props) {
  return (
    <View
      accessible={true}                          // combine into single focus
      accessibilityLabel={`${title}, by ${instructor}`}
      accessibilityHint={isCompleted ? undefined : 'Double-tap to open course'}
      accessibilityRole="button"
      accessibilityState={{ selected: isCompleted }}
    >
      <Text>{title}</Text>
      <Text>{instructor}</Text>
    </View>
  );
}

// ── Accessible text input with error
function EmailInput({ value, onChange, error }: InputProps) {
  return (
    <View>
      <Text nativeID="email-label">Email address</Text>
      <TextInput
        value={value}
        onChangeText={onChange}
        accessibilityLabelledBy="email-label"
        accessibilityInvalidated={!!error}        // maps to aria-invalid
        accessibilityErrorMessage={error}          // RN 0.74+
        keyboardType="email-address"
        autoComplete="email"
        textContentType="emailAddress"            // iOS autofill
      />
      {error && (
        <Text
          accessibilityLiveRegion="assertive"     // announce immediately
          accessibilityRole="alert"
        >
          {error}
        </Text>
      )}
    </View>
  );
}
```

### Touch targets (WCAG 2.5.8 equivalent)
```tsx
import { StyleSheet } from 'react-native';

const styles = StyleSheet.create({
  // iOS: minimum 44x44 pt; Android: minimum 48x48 dp
  touchable: {
    minWidth: 44,
    minHeight: 44,
    justifyContent: 'center',
    alignItems: 'center',
  },
  // hitSlop expands tap area without changing visual size
  // Use when the visual element must be smaller
});

// Use hitSlop for small icons
<TouchableOpacity
  hitSlop={{ top: 12, bottom: 12, left: 12, right: 12 }}
  accessibilityRole="button"
  accessibilityLabel="Delete item"
/>
```

### Dynamic Type (font scaling)
```tsx
import { Text } from 'react-native';

// ❌ Never: fixed font sizes block Dynamic Type
<Text style={{ fontSize: 16 }}>Static text</Text>

// ✅ Allow: system font that scales with user preference
<Text>Default text</Text>  // inherits system font size

// ✅ If you must set size, allow scaling
<Text allowFontScaling={true} style={{ fontSize: 16 }}>Scalable text</Text>

// ✅ maxFontSizeMultiplier: prevent runaway scaling in tight UIs
<Text maxFontSizeMultiplier={1.5} style={{ fontSize: 14 }}>Compact text</Text>
```

### Reduce Motion
```tsx
import { useEffect, useState } from 'react';
import { AccessibilityInfo } from 'react-native';
import Animated, { useSharedValue, withTiming, withSpring } from 'react-native-reanimated';

function AnimatedCard() {
  const [reduceMotion, setReduceMotion] = useState(false);
  const opacity = useSharedValue(0);

  useEffect(() => {
    AccessibilityInfo.isReduceMotionEnabled().then(setReduceMotion);
    const sub = AccessibilityInfo.addEventListener('reduceMotionChanged', setReduceMotion);
    return () => sub.remove();
  }, []);

  useEffect(() => {
    opacity.value = reduceMotion
      ? withTiming(1, { duration: 0 })   // instant
      : withSpring(1);                    // animated
  }, [reduceMotion]);

  return <Animated.View style={{ opacity }} />;
}
```

### Focus management (screen transition)
```tsx
import { useRef, useEffect } from 'react';
import { View, AccessibilityInfo, findNodeHandle } from 'react-native';

function NewScreen() {
  const headingRef = useRef<View>(null);

  useEffect(() => {
    // Move VoiceOver/TalkBack focus to screen heading on mount
    const node = findNodeHandle(headingRef.current);
    if (node) AccessibilityInfo.setAccessibilityFocus(node);
  }, []);

  return (
    <View>
      <View
        ref={headingRef}
        accessible={true}
        accessibilityRole="header"
      >
        <Text>Settings</Text>
      </View>
    </View>
  );
}
```

> Quick search: `python scripts/search.py keys --reader TalkBack` for TalkBack gestures,
> `python scripts/search.py keys --reader VoiceOver --platform iOS` for VoiceOver iOS.

---

## 27. Cognitive Accessibility (COGA)

Cognitive, language, and learning disabilities affect ~15% of people. WCAG addresses them partially — COGA supplemental guidance fills the gaps.

### Top 10 COGA design patterns

| Pattern | What to do | WCAG mapping |
|---------|-----------|---------------|
| Plain language | Reading level ≤ grade 8; short sentences; active voice | 3.1.5 (AAA) |
| Familiar patterns | Standard nav location; known icons; no novel interactions | 3.2.3 / 3.2.4 |
| No time limits | Extend or remove timers; show countdown with `aria-live` | 2.2.1 / 2.2.3 |
| Reduce cognitive load | ≤7 nav items; progressive disclosure; no autoplay | 3.2.2 |
| Support memory | Pre-fill known data; breadcrumbs; undo; don't re-ask (3.3.7) | 3.3.7 (WCAG 2.2) |
| Clear error recovery | Say what happened + exactly what to do; inline validation | 3.3.1 / 3.3.3 |
| Visible labels | `<label>` always visible; placeholder ≠ label | 3.3.2 |
| No distractions | `prefers-reduced-motion`; no autoplay audio | 2.2.2 / 2.3.1 |
| Consistent vocabulary | Same word for same thing; glossary available | 3.1.3 (AAA) |
| Multiple input modes | Text + autocomplete; voice input; no drag-only (2.5.7) | 2.1.1 / 2.5.7 |

### Accessible authentication (WCAG 3.3.8 — WCAG 2.2)
```html
<!-- ❌ Cognitive function test — fails 3.3.8 -->
<p>Type the characters you see in the image:</p>
<img src="captcha.png" alt="">
<input type="text" name="captcha">

<!-- ✅ Alternatives that pass 3.3.8 -->
<!-- 1. Allow paste into password fields -->
<input type="password" autocomplete="current-password">
<!-- 2. Use WebAuthn (passkeys) -->
<!-- 3. Use OTP sent to email/phone -->
<!-- 4. If CAPTCHA is unavoidable: provide accessible alternative (audio CAPTCHA) -->
```

> Full pattern database: `data/cognitive-accessibility.csv` (20 patterns)
> Search: `python scripts/search.py cognitive --keyword memory`

---

## 28. WCAG 3.0 — Draft status

WCAG 3.0 is an **incomplete W3C Working Draft** and **not a standard**. WCAG 2.1/2.2 AA remains the compliance target. The draft says it still has several years of work and that details will change; it also states that WCAG 3 does not replace WCAG 2, which will still be required in many places for a long time.

Sources (check them for the current status; reviewed 2026-10-01 against the 10 September 2026 Working Draft):
- Draft: https://www.w3.org/TR/wcag-3.0/
- Introduction: https://www.w3.org/WAI/standards-guidelines/wcag/wcag3-intro/

### What not to state as fact
- No WCAG 3 success criteria with fixed numbers (such as "3.1.1"): requirements in the draft are named (for example "Text contrast sufficient (minimum)") and may change.
- Bronze, Silver and Gold **do** appear in section 4.1.4 of the draft, as the 4th–6th *reporting tiers* above conformance (the 3rd tier is conformance), but the number of supplemental requirements and assertions for each is still **TBD**. Section 4 is informative and exploratory, and the draft's editor's notes say the model is still under discussion (an alternative proposal uses scoring, with Bronze/Silver/Gold awarded after conformance). Present them as proposed reporting tiers in development, not as a finalized conformance target, and do not say what is required to reach them.
- The draft does not use A/AA/AAA levels in the way WCAG 2 does; do not map WCAG 2 levels onto WCAG 3 tiers.
- No contrast algorithm or thresholds: the draft says the contrast algorithm is yet to be determined. APCA is **not** confirmed as the WCAG 3 algorithm, so do not quote APCA Lc values as WCAG 3 requirements.
- No finalization date.

### How to prepare now
1. **Keep targeting WCAG 2.1/2.2 AA.** Contrast compliance is measured with the WCAG 2.x ratios (1.4.3, 1.4.6, 1.4.11).
2. **Follow the draft** at the links above before answering any WCAG 3 question, and label anything from it as draft.
3. If a user asks about APCA, explain that it is a separate contrast model that is not part of WCAG 2.x conformance and not confirmed for WCAG 3.

> The CLI command `python scripts/search.py wcag3` and the MCP resource `wcag://draft-wcag3` return only a draft-status notice with these links; they contain no criteria.

---

## Notes for Claude

1. **Default to WCAG 2.1 AA** and surface **WCAG 2.2 additions** when relevant (focus obscured, target size, drag alternatives, accessible auth, redundant entry, consistent help).
2. **Semantic HTML first**; reach for ARIA only when native semantics are insufficient (Rule #1 of ARIA).
3. **Recommend real AT testing** — automated tools catch ~20–40%.
4. **Include mobile** whenever responsive or native is in scope; cite 44pt (iOS) / 48dp (Android).
5. **Always provide working code examples** for recommended ARIA patterns and include focus management.
6. **Match tools to context**: CI → axe-core/Playwright/jest-axe/cypress-axe; quick audit → axe DevTools, WAVE, Accessibility Insights; design review → Stark / Figma contrast plugins.
7. **Use the CSVs** — prefer `python scripts/search.py …` over restating lookup tables. Point users at `data/*.csv` for exhaustive detail.
8. **Language**: prefer person-first or identity-first per community norms; never pity-based framing.
9. **When asked about KPIs, handoff, audit, inclusive research, typography, or color palettes**, use the relevant sections and CSVs — these are strong differentiators versus generic a11y advice.
10. **Reply in the user's language** (English or Spanish) when they ask in Spanish; use `data/glossary-es.csv` for terminology. Terms like "lector de pantalla", "criterios de éxito", "tecnologías asistivas" are preferred.
11. **Stack examples**: section 18 → Next.js, Angular, Svelte, Astro, SolidJS; section 19 → SwiftUI, Jetpack Compose; section 25 → Vue 3; section 26 → React Native.
12. **Legal questions**: cite `data/legal-framework.csv`; always highlight the **EAA 28 June 2025** deadline for EU-facing products.
13. **Cognitive accessibility**: when ADHD, dyslexia, memory, or anxiety is mentioned, use section 27 and `data/cognitive-accessibility.csv`.
14. **WCAG 3.0**: mention only as an incomplete W3C draft — WCAG 2.1/2.2 AA is still the standard. Do not cite WCAG 3 criteria IDs, APCA thresholds or dates as fact, and treat Bronze/Silver/Gold only as proposed reporting tiers; point to section 28 and the W3C draft.
15. **User preference media queries**: recommend prefers-reduced-motion, prefers-contrast, forced-colors, prefers-reduced-transparency in every animation/color/theme discussion — see section 20.
16. **Templates & prompts**: point users to `templates/` and `prompts/` for ready-to-use assets. The 12 prompts in `prompts/` are designed to be pasted into Claude directly.
17. **External Resources**: refer users to [`RESOURCES.md`](./RESOURCES.md) for comprehensive curated bibliography of books, blogs, research papers, tools, and legal frameworks — updated 2025 with WCAG 2.2, EAA deadline, and peer-reviewed studies.
