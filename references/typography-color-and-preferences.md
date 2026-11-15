# Typography, color and user preferences

Typography requirements versus design guidance, contrast and palette design, and the CSS media queries that respect user preferences (motion, color scheme, contrast, forced colors, transparency, data, text size).

## Contents

- [Accessible Typography](#accessible-typography)
- [Accessible Color Palettes](#accessible-color-palettes)
  - [Contrast matrix (WCAG 2.1 / 2.2)](#contrast-matrix-wcag-21--22)
  - [Palette design workflow](#palette-design-workflow)
- [User Preference Media Queries](#user-preference-media-queries)
  - [prefers-reduced-motion](#prefers-reduced-motion)
  - [prefers-color-scheme (dark mode)](#prefers-color-scheme-dark-mode)
  - [prefers-contrast](#prefers-contrast)
  - [forced-colors (Windows High Contrast Mode)](#forced-colors-windows-high-contrast-mode)
  - [prefers-reduced-transparency](#prefers-reduced-transparency)
  - [prefers-reduced-data (emerging)](#prefers-reduced-data-emerging)
  - [Dynamic Type / text resize](#dynamic-type--text-resize)

---

## Accessible Typography

Keep three things apart when reporting: **WCAG requirement** (normative text), **conformance technique** (how to meet it), and **design guidance** (useful, but not a pass/fail test). Do not fail content for missing a design guideline.

| Topic | Type | Guidance | Source |
|-------|------|----------|--------|
| Resize text | Requirement (AA) | Text resizes up to 200% without assistive technology and without loss of content or functionality; exceptions: captions, images of text. Browser zoom or text-only resize may satisfy it; do not block it | [1.4.4](https://www.w3.org/TR/WCAG22/#resize-text); detail in [reflow-zoom-and-text-spacing.md](reflow-zoom-and-text-spacing.md) |
| Body size (16 px / 1rem) | Design guidance | A common starting size, **not** a WCAG minimum. Smaller text is not a 1.4.4 failure by itself; rem does not guarantee accessibility | [Understanding 1.4.4](https://www.w3.org/WAI/WCAG22/Understanding/resize-text.html) |
| Text spacing | Requirement (AA) | No loss of content or functionality when the **user** sets all four together: line height 1.5, spacing after paragraphs 2, letter 0.12, word 0.16 (× font size). Content need not start with these values and need not offer a spacing control. Languages and scripts that lack a property may conform with the properties they use | [1.4.12](https://www.w3.org/TR/WCAG22/#text-spacing) |
| Line height / paragraph spacing as initial design | Design guidance | About 1.5 line height is a common start. A smaller initial value is not a 1.4.12 failure; content or functionality lost under the overrides is. Truncation with an ellipsis can still conform if the full content stays available through an accessible mechanism (e.g. revealed on focus or activation, or shown on a linked page); truncation with no such mechanism fails. Hover, `title` or `aria-label` alone are not a universal solution or sufficient proof | [Understanding 1.4.12](https://www.w3.org/WAI/WCAG22/Understanding/text-spacing.html) |
| Line length | Design guidance; AAA | 45–75 characters is a common readability target, not WCAG. AAA 1.4.8 requires a *mechanism* (page or user agent) for width ≤ 80 characters (40 CJK) | [1.4.8](https://www.w3.org/TR/WCAG22/#visual-presentation) |
| Alignment | Design guidance; AAA | Avoid fully justified blocks; align to the start edge of the writing direction (left in LTR, right in RTL). AAA 1.4.8 requires a mechanism so text is not justified, not a particular default look | [1.4.8](https://www.w3.org/TR/WCAG22/#visual-presentation) |
| Reflow | Requirement (AA) | Usable at 320 CSS px width | 1.4.10; detail in [reflow-zoom-and-text-spacing.md](reflow-zoom-and-text-spacing.md) |
| Contrast | Requirement (AA) | 4.5:1 body / 3:1 large (18pt, or 14pt bold) | [1.4.3](https://www.w3.org/TR/WCAG22/#contrast-minimum) |
| Font weight | Design guidance | Prefer regular or heavier weights for body text. 1.4.3 sets no minimum weight. Size and bold together classify text as large (≥ 18 pt, or ≥ 14 pt bold; equivalent sizes for other fonts), so AA requires 4.5:1 for normal text and 3:1 for large text, subject to the criterion's exceptions. Very thin strokes may benefit from heavier strokes or more contrast: a legibility recommendation, not a mandatory weight or an automatic failure | [Understanding 1.4.3](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html) |
| Typeface | Design guidance | No WCAG criterion requires a specific face, and no font guarantees benefits for readers with dyslexia. Choose clearly distinguishable letterforms and test with your audience | — |
| Avoid all-caps for long copy | Design guidance | Can reduce legibility; screen readers may spell some words | — |
| No text-in-images | Requirement (AA) | Use real text (logos exempt) | 1.4.5 |

```css
/* Manual test aid for 1.4.12, NOT production styles and NOT a complete check.
   Apply all four together (and change nothing else), then look for clipped,
   overlapping, truncated or hidden text and lost functionality. Truncated text is a
   signal to review (is the full content still available?), not an automatic verdict. */
* {
  line-height: 1.5 !important;
  letter-spacing: 0.12em !important;
  word-spacing: 0.16em !important;
}
p { margin-bottom: 2em !important; }
```

Audit cases: text under 16 px, a weight under 400, or an initial line height under 1.5 are not failures by themselves — report a barrier only with evidence (e.g. content lost at 200% or under the 1.4.12 overrides). Under an AA target, do not apply the AAA conditions of 1.4.8 automatically.

> Full ruleset: `data/typography-rules.csv`

---

## Accessible Color Palettes

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
4. Test in **dark mode**, **high contrast mode** (`forced-colors: active`; CSS in [forced-colors](#forced-colors-windows-high-contrast-mode)), and color-blindness simulators (deuteranopia, protanopia, tritanopia).
5. Never encode meaning in color alone — pair with icon, text, or pattern.

> Full rules: `data/color-palette-rules.csv`

---

## User Preference Media Queries

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
    /* CanvasText also works for the outline: outline: 2px solid CanvasText; */
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
