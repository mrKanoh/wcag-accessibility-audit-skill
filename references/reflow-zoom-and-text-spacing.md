# Reflow, zoom, text resize and text spacing

Read this when you design or build a responsive layout, review how a page behaves when zoomed, or test text resize and text spacing. It covers 1.4.4 Resize Text, 1.4.10 Reflow, 1.4.12 Text Spacing and 1.3.4 Orientation, sticky content at high zoom, CSS patterns and a manual test procedure.

Each item says whether it is a **requirement** (a WCAG 2.2 success criterion, with ID, level and the version it entered), a **technique** (a W3C technique: one way to meet a criterion) or **guidance**. Nothing fails WCAG for missing guidance. The default target is WCAG 2.2 AA ([legal-framework.md](legal-framework.md)). Typography guidance (body size, line height as an initial design choice, line length) stays in [typography-color-and-preferences.md](typography-color-and-preferences.md#accessible-typography); this file does not repeat it.

## Contents

- [What the criteria require](#what-the-criteria-require)
- [Browser zoom and viewport width](#browser-zoom-and-viewport-width)
- [Content allowed to scroll in two dimensions](#content-allowed-to-scroll-in-two-dimensions)
- [Sticky and fixed content when zoomed](#sticky-and-fixed-content-when-zoomed)
- [CSS patterns](#css-patterns)
- [Manual test procedure](#manual-test-procedure)
- [Native apps and text size settings](#native-apps-and-text-size-settings)
- [Sources](#sources)

## What the criteria require

| ID | Name | Level | Entered | Requirement (summary of the normative text) |
|----|------|-------|---------|----------------------------------------------|
| 1.4.4 | Resize Text | AA | 2.0 | Except for captions and images of text, text can be resized without assistive technology up to 200 percent without loss of content or functionality |
| 1.4.10 | Reflow | AA | 2.1 | Content can be presented without loss of information or functionality, and without scrolling in two dimensions, for vertical scrolling content at a width equivalent to **320 CSS px** and horizontal scrolling content at a height equivalent to **256 CSS px**; except for parts of the content that require two-dimensional layout for usage or meaning |
| 1.4.12 | Text Spacing | AA | 2.1 | No loss of content or functionality when the user sets all of these, changing no other style property: line height at least **1.5** × font size; spacing after paragraphs at least **2** × font size; letter spacing at least **0.12** × font size; word spacing at least **0.16** × font size. Languages and scripts that do not use one of these properties can conform using only the properties that exist for them |
| 1.3.4 | Orientation | AA | 2.1 | Content does not restrict its view and operation to a single display orientation (portrait or landscape) unless a specific orientation is essential |

Notes from the Understanding documents:

- **1.4.4.** Content meets it if text scales to 200% with at least one mechanism that user agents support, such as full-page zoom; the author's job is not to block user agent scaling, or to provide scaling directly. Failures: F69 (text, images or controls clipped, truncated or obscured at 200%), F80 (text-based form controls that do not resize with the text), F94 (text sized only with viewport units).
- **1.4.10.** The 320 CSS px width applies to content that scrolls vertically; the 256 CSS px height applies to content that scrolls horizontally (for example vertical text). Failure F102: content that disappears and is not available after reflow.
- **1.4.12.** Authors do not have to use these values by default and need not provide a spacing control: the requirement is that "when a user overrides the authored text spacing, content or functionality is not lost". An ellipsis can still conform if the full text stays available through a mechanism (revealed on focus or activation, or on a linked page); "if there is no mechanism to show the truncated text, it fails". Failure F104 (clipped or overlapping content).
- **1.3.4.** Understanding 1.3.4 gives as essential examples a banking app that needs landscape to capture a check, a piano app, and virtual reality. Failures: F97 (locking orientation), F100 (showing a message asking the user to reorient the device). Technique G214 (a control to reach content otherwise restricted to one orientation).

## Browser zoom and viewport width

Understanding 1.4.10: "320 CSS pixels is equivalent to a starting viewport width of 1280 CSS pixels wide at 400% zoom." So the same layout can be checked by zooming a 1280 px wide window to 400% or by setting the viewport to 320 CSS px wide. Text resize (1.4.4) is checked at 200%, which is a different test: a page can pass one and fail the other.

## Content allowed to scroll in two dimensions

The 1.4.10 exception covers parts of the content that need two-dimensional layout for usage or meaning. Understanding 1.4.10 lists images required for understanding (maps, diagrams), video, games, presentations, data tables (the table may scroll, but the cell content should still wrap), and interfaces that need toolbars to stay in view.

- **Only that part** may scroll in two directions; the rest of the page must still reflow.
- **Code and preformatted text.** Understanding 1.4.10 notes that "maintaining indentations and non-breaking lines can be important to help understand code patterns". Long code lines may scroll inside their block; reducing indentation width at small widths helps.
- **Long strings** (URLs, email addresses, IDs) in normal text should wrap (technique C33) or be truncated with a way to see the full text.
- A container that scrolls on its own must be operable by keyboard (2.1.1 Keyboard, A, 2.0): make sure the user can scroll it with the keyboard, for example by making it focusable and giving it a name. An example of a named, focusable scroll region is `examples/components/data-grid.html`.

## Sticky and fixed content when zoomed

- Sticky headers, footers, cookie banners and chat launchers take a fixed share of the screen. At 400% they can cover most of the viewport. Understanding 1.4.10 says "it is strongly suggested that at smaller viewport sizes that such components are modified to have static positioning", or that their display can be toggled. Advisory technique C34 (media queries to un-fix sticky headers and footers).
- **Requirement (2.4.11 Focus Not Obscured (Minimum), AA, new in 2.2).** A focused component must not be entirely hidden by author-created content, also when zoomed. Check keyboard focus at 400% with every sticky element present. Technique C43 (`scroll-padding`); a one-line fix is in [common issues and fixes](audit-process-and-kpis.md#common-issues--fixes). The design side is in [design-phase.md](design-phase.md#focus-indicator).

## CSS patterns

Techniques from Understanding 1.4.4, 1.4.10 and 1.4.12. They are ways to meet the criteria, not the only ways.

| Pattern | Technique | Why |
|---------|-----------|-----|
| Grid or flexbox that changes columns with media or container queries | C32, C31 | Columns stack instead of forcing horizontal scroll |
| Text containers sized in `em`/`rem`, liquid layout | C28, G146 | Containers grow with the text at 200% |
| Font sizes in relative units (`%`, `em`, `rem`, named sizes) | C12, C13, C14 | Respects user and browser text size; F94 is viewport units alone |
| Size and position computed by script in a way that scales with text | SCR34 | Script-driven layouts still follow text size |
| Labels and inputs with `width`/`max-width` and flexbox | C38 | Form rows fit 320 CSS px |
| Long URLs and strings allowed to wrap | C33 | No horizontal scroll from one long word |
| No fixed `height` on boxes that contain text; let them grow, or allow overflow to scroll | C36, C35 | Text spacing overrides do not clip or overlap (F104) |
| Images with `max-width: 100%` and `height: auto` | C37 (advisory) | Images shrink with the viewport |
| Sticky header/footer become static at small widths | C34 (advisory) | Frees the viewport at high zoom |
| Do not block zoom (for example `user-scalable=no` or `maximum-scale=1` in the viewport meta) | Guidance; G142 relies on user agent zoom | Understanding 1.4.4 asks authors not to block user agent scaling |

```css
/* Not tested: illustrative patterns; check them in your own layout at 320 CSS px and 400% zoom. */
.cards {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 18rem), 1fr)); /* stacks below ~18rem */
  gap: 1rem;
}
.card { padding: 1em; }                 /* no fixed height: grows with text and spacing */
.prose { overflow-wrap: break-word; }   /* long URLs and strings wrap */
img { max-width: 100%; height: auto; }
@media (max-width: 40em) {
  .site-header { position: static; }    /* un-stick at narrow widths / high zoom */
}
```

## Manual test procedure

The audit matrix, evidence fields and the other manual protocols are in [site-audit-procedure.md](site-audit-procedure.md#3-execute-manual-protocols); this is the step-by-step for these four criteria.

1. **Record the setup.** Browser and version, OS, window size, zoom level, and the page and state tested (menus open, dialogs, error states).
2. **Resize text (1.4.4).** At a normal window size, zoom to 200% (and, if the browser offers it, also try text-only zoom). Check that no text, control or image of a control is clipped, truncated, overlapped or hidden, that form fields grow with their text, and that every function still works.
3. **Reflow (1.4.10).** Set a 1280 CSS px wide window and zoom to 400%, or set the viewport to 320 CSS px wide. Scroll the page vertically from top to bottom. Note any horizontal scrolling of the whole page, content or functions that disappeared (F102), and overlaps. For each part that scrolls in two dimensions, decide whether it falls under the exception (map, data table, code, toolbar…) and record why.
4. **Sticky content and focus (1.4.10, 2.4.11).** At 400%, Tab through the page. Check that each focused element is not entirely hidden behind sticky headers, footers, banners or chat widgets, and how much of the viewport they take.
5. **Text spacing (1.4.12).** Apply all four values together and change nothing else (the test CSS is in [Accessible Typography](typography-color-and-preferences.md#accessible-typography)). Look for clipped, overlapping, truncated or hidden text and lost functionality. If text is truncated, check whether the full text is available through a mechanism.
6. **Orientation (1.3.4).** On a phone or tablet, or with device emulation, rotate between portrait and landscape. The content must not be locked to one orientation or ask the user to rotate, unless the orientation is essential.
7. **Record each result** with its evidence (screenshot with zoom level visible) and the exception you applied, if any. A pass at one zoom level or width is not a pass at another.

## Native apps and text size settings

This file is about web content. For native apps and the platform text size settings (Dynamic Type on iOS, font scale on Android), see [Dynamic Type / text resize](typography-color-and-preferences.md#dynamic-type--text-resize) and [mobile.md](mobile.md).

## Sources

Consulted on 2026-11-15:

- WCAG 2.2 (W3C Recommendation, 12 December 2024): https://www.w3.org/TR/WCAG22/
- What's New in WCAG 2.1: https://www.w3.org/WAI/standards-guidelines/wcag/new-in-21/
- Understanding 1.4.4 Resize Text: https://www.w3.org/WAI/WCAG22/Understanding/resize-text.html
- Understanding 1.4.10 Reflow: https://www.w3.org/WAI/WCAG22/Understanding/reflow.html
- Understanding 1.4.12 Text Spacing: https://www.w3.org/WAI/WCAG22/Understanding/text-spacing.html
- Understanding 1.3.4 Orientation: https://www.w3.org/WAI/WCAG22/Understanding/orientation.html
- Understanding 2.4.11 Focus Not Obscured (Minimum): https://www.w3.org/WAI/WCAG22/Understanding/focus-not-obscured-minimum.html
