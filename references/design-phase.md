# Accessibility in the design phase

Read this when you design screens, components or a design system, or review wireframes and mockups before code exists. Many WCAG barriers are decided here: structure, focus order, states, focus indicators, target size, color, dragging, help placement, layout at small widths and motion. The end of the file has a review checklist for wireframes and mockups.

Each item says whether it is a **requirement** (a WCAG 2.2 success criterion, with ID, level and the version it entered), a **technique** (a W3C technique: one way to meet a criterion) or **guidance** (useful practice that no criterion requires). Nothing fails WCAG for missing guidance, and AAA criteria are named as AAA, not as AA requirements. The default target is WCAG 2.2 AA ([legal-framework.md](legal-framework.md) for when 2.1 AA applies instead). A design file cannot pass or fail WCAG by itself: conformance is judged on the built page. The design decides whether the build can conform without redesign.

## Contents

- [Structure: headings, regions and reading order](#structure-headings-regions-and-reading-order)
- [Focus order](#focus-order)
- [Interactive states](#interactive-states)
- [Focus indicator](#focus-indicator)
- [Target size](#target-size)
- [Color and contrast](#color-and-contrast)
- [Alternatives to dragging](#alternatives-to-dragging)
- [Consistent help](#consistent-help)
- [Forms and authentication](#forms-and-authentication)
- [Responsive layout, reflow and zoom](#responsive-layout-reflow-and-zoom)
- [Motion and flashing](#motion-and-flashing)
- [What to deliver in the handoff](#what-to-deliver-in-the-handoff)
- [Design review checklist (wireframe or mockup)](#design-review-checklist-wireframe-or-mockup)
- [Sources](#sources)

## Structure: headings, regions and reading order

- **Requirement (1.3.1 Info and Relationships, A, 2.0).** Structure that the design conveys visually (headings, lists, groups, tables, regions) must be programmatically determinable once built. The designer's job is to make that structure explicit so it can be built: mark which text is a heading and its level, which areas are regions (header, navigation, main, complementary, footer), and which items are lists or tables.
- **Requirement (1.3.2 Meaningful Sequence, A, 2.0).** When the order of content affects its meaning, a correct reading sequence must be programmatically determinable. Understanding 1.3.2 notes that the visual layout does not have to match the code order everywhere: "Providing a particular linear order is only required where it affects meaning." Annotate the intended reading order where a multi-column layout, a card or an overlay could be read in the wrong order.
- **Requirement (2.4.6 Headings and Labels, AA, 2.0).** Headings and labels that exist describe topic or purpose. It does not require headings to exist; the content's structure does (1.3.1).
- **Requirement (2.4.1 Bypass Blocks, A, 2.0).** A way to skip blocks repeated on many pages (a skip link, headings, regions). Show where the skip link appears when it receives focus.
- **Guidance.** One `h1` per page and no skipped levels are common conventions, not WCAG requirements. Writing headings, link text and alternative text is covered in the content guidance.

## Focus order

- **Requirement (2.4.3 Focus Order, A, 2.0).** When sequential navigation affects meaning or operation, focusable components receive focus in an order that preserves meaning and operability.
- **Guidance.** Number the focus order on the mockup (arrows or numbers through every interactive element), including what happens when a dialog, menu or drawer opens and closes: where focus goes first and where it returns. Initial and return focus options for dialogs: [authentication-and-modal-focus.md](authentication-and-modal-focus.md#2-initial-focus-and-focus-return-in-modal-dialogs).
- Specify the keyboard behavior of every custom component (which keys do what). Before designing one, check whether a native control does the job: [components.md](components.md#before-you-build-a-custom-component).

## Interactive states

Design every state of every interactive component: **default, hover, focus, active (pressed), selected or checked, disabled, error**, and where relevant expanded, current page and loading.

- **Requirement (1.4.1 Use of Color, A, 2.0).** Color is not the only visual means of conveying information, indicating an action, prompting a response or distinguishing an element. A selected tab, an error field or a link in a paragraph needs a cue besides hue (underline, icon, border, weight, text).
- **Requirement (1.4.11 Non-text Contrast, AA, 2.1).** Visual information needed to identify a component and its state has at least 3:1 against adjacent colors. Understanding 1.4.11 applies this to "whether a component is selected or focused". Author-added hover effects are "supplemental" and need not meet 3:1, but must not reduce the contrast of the component or of other states. Inactive (disabled) components are exempt.
- **Requirement (1.4.13 Content on Hover or Focus, AA, 2.1).** Content that appears on hover or focus (tooltips, previews) is dismissible, hoverable and persistent. Prefer a design that does not hide needed information behind hover: [components.md](components.md#tooltip-and-toggletip-last-resort).
- **Guidance.** A disabled button gives no reason why it is disabled. Consider keeping it enabled and explaining what is missing when it is used, or show the reason next to it.

## Focus indicator

- **Requirement (2.4.7 Focus Visible, AA, 2.0).** Every keyboard-operable interface has a mode in which the focus indicator is visible. Understanding 2.4.7 says it sets no size or contrast: it "does not specify what that form is".
- **Requirement (1.4.11, AA, 2.1).** A focus indicator styled by the author is visual information needed to identify the focused state, so it needs 3:1 against adjacent colors.
- **Requirement (2.4.11 Focus Not Obscured (Minimum), AA, new in 2.2).** When a component receives keyboard focus, it is not **entirely** hidden by author-created content. Understanding 2.4.11 names "sticky footers, sticky headers, and non-modal dialogs" as typical causes, and says a sticky cookie banner fails if it entirely obscures the focused component. Technique C43 (CSS `scroll-padding`); failure F110.
- **AAA, not part of an AA target.** 2.4.12 Focus Not Obscured (Enhanced) (no part hidden) and 2.4.13 Focus Appearance (minimum area and 3:1 change of contrast for the indicator), both new in 2.2. They are useful design goals; do not report them as AA failures.
- **Technique.** Design one focus style for the whole system (techniques G195 author-supplied indicator, C45 `:focus-visible`, C40 a two-color indicator that contrasts on light and dark backgrounds). Do not remove the browser's indicator without a replacement (failure F78).

## Target size

- **Requirement (2.5.8 Target Size (Minimum), AA, new in 2.2).** Pointer targets are at least 24 × 24 CSS px, except when:
  - **Spacing:** an undersized target has a 24 CSS px diameter circle centered on its bounding box that does not intersect another target or another undersized target's circle;
  - **Equivalent:** the same function is available through another control on the page that meets the criterion;
  - **Inline:** the target is in a sentence or its size is constrained by the line height of non-target text;
  - **User agent control:** the size is set by the browser and not modified by the author;
  - **Essential:** a particular presentation is essential or legally required.
- **AAA.** 2.5.5 Target Size (Enhanced), AAA, 2.1, uses 44 × 44 CSS px. Understanding 2.5.8 advises: "For important links/controls, consider aiming for the stricter 2.5.5 Target Size (Enhanced)."
- **Guidance.** Platform guidelines for touch (44 pt on iOS, 48 dp on Android) are platform design guidance, not WCAG: [mobile.md](mobile.md). Technique C42 (`min-height` and `min-width` on the target container).

## Color and contrast

- **Requirements.** 1.4.3 Contrast (Minimum), AA, 2.0, for text and images of text; 1.4.11 Non-text Contrast, AA, 2.1, for component boundaries, states, focus indicators and graphics needed to understand content; 1.4.1 Use of Color, A, 2.0.
- The ratios, large-text thresholds, exceptions and the palette workflow are in [typography-color-and-preferences.md](typography-color-and-preferences.md#contrast-matrix-wcag-21--22) and [the palette design workflow](typography-color-and-preferences.md#palette-design-workflow); rules in `data/color-palette-rules.csv`. Check every pair in every state and theme (light, dark, high contrast), including text over images and gradients.
- Forced colors and other user preferences: [user preference media queries](typography-color-and-preferences.md#user-preference-media-queries).

## Alternatives to dragging

- **Requirement (2.5.7 Dragging Movements, AA, new in 2.2).** All functionality that uses dragging can be achieved with a single pointer without dragging, unless dragging is essential or the behavior is set by the user agent and not modified by the author.
- Understanding 2.5.7 examples: arrow buttons next to a draggable map, forward and back buttons for a carousel, clicking the slider track to move the thumb, up and down controls next to a sortable item.
- A keyboard alternative alone does not meet it: "achieving keyboard equivalence for a dragging operation does not automatically meet this success criterion" (2.1.1 Keyboard is a separate requirement). Technique G219. Build pattern: [components.md](components.md#accessible-drag--drop-wcag-257).

## Consistent help

- **Requirement (3.2.6 Consistent Help, A, new in 2.2).** If a set of pages repeats a help mechanism (human contact details, a human contact mechanism, a self-help option, or a fully automated contact mechanism such as a chatbot), it appears in the same order relative to other page content, unless the user changes it.
- Understanding 3.2.6: "it is not the intent of this success criterion to require authors to provide help". The order is the order in the content, not the exact visual position; layout changes caused by the user, such as zoom, are exempt.
- **Guidance.** Put the help link or chat launcher in the same place in the template for every page.

## Forms and authentication

Design decides labels, instructions, required-field marks, error messages, multi-step progress and whether users must re-enter information (3.3.7 Redundant Entry, A, new in 2.2). Read [forms.md](forms.md) for the criteria and patterns, and [authentication-and-modal-focus.md](authentication-and-modal-focus.md#1-accessible-authentication) for login steps (3.3.8, AA, new in 2.2).

## Responsive layout, reflow and zoom

Design the narrow layout as part of the design, not as an afterthought: content must reflow at 320 CSS px width without scrolling in two directions (1.4.10 Reflow, AA, 2.1), text must resize to 200% (1.4.4 Resize Text, AA, 2.0), and content must not be locked to one orientation unless essential (1.3.4 Orientation, AA, 2.1). Sticky headers and footers that are acceptable at 100% can cover most of the screen when zoomed, and the focused element with them (2.4.11).

## Motion and flashing

- **Requirement (2.2.2 Pause, Stop, Hide, A, 2.0).** Moving, blinking or scrolling information that starts automatically, lasts more than five seconds and is shown in parallel with other content has a mechanism to pause, stop or hide it; the same for auto-updating information. Design the pause control with the carousel or animation.
- **Requirement (2.3.1 Three Flashes or Below Threshold, A, 2.0).** Nothing flashes more than three times in any one second, unless the flash is below the general and red flash thresholds.
- **AAA.** 2.3.3 Animation from Interactions, AAA, 2.1: motion animation triggered by interaction can be disabled unless essential.
- **Guidance.** Specify a reduced-motion alternative for every animation: [prefers-reduced-motion](typography-color-and-preferences.md#prefers-reduced-motion).

## What to deliver in the handoff

Annotate structure, focus order, keyboard behavior, accessible names, states, contrast-audited tokens, motion alternatives, target sizes, and errors and status messages. The list of artifacts is in [inclusive-practice.md](inclusive-practice.md#designer--developer-handoff), the phase-by-phase checklist in `data/handoff-checklist.csv` (`python scripts/search.py handoff --phase Design`), and review prompts in `prompts/review-figma-handoff.md` and `prompts/design-tokens-audit.md`.

## Design review checklist (wireframe or mockup)

"Basis" says whether the item maps to a WCAG 2.2 requirement (to be confirmed on the built page) or is guidance.

| Check | How to check on the design | Basis |
|-------|----------------------------|-------|
| Headings and their levels are marked | Every heading has a level in the annotations; the levels follow the content's structure | 1.3.1 A; 2.4.6 AA for wording |
| Regions are marked | Header, navigation, main, complementary and footer areas are labelled | 1.3.1 A; 2.4.1 A (bypass) |
| Reading order is annotated where layout could mislead | Multi-column areas, cards and overlays have a numbered reading order | 1.3.2 A |
| Focus order is numbered | Every interactive element has a position; dialogs and menus show initial and return focus | 2.4.3 A |
| Keyboard behavior of custom components is specified | Keys and results are written for each custom widget | 2.1.1 A |
| All states are designed | Default, hover, focus, active, selected, disabled and error exist for each component | 1.4.1 A; 1.4.11 AA |
| State is not shown by color alone | Selected, current, error and required have a non-color cue | 1.4.1 A |
| Focus indicator is visible and contrasts | One focus style; 3:1 against adjacent colors in every theme | 2.4.7 AA; 1.4.11 AA |
| Sticky or floating elements cannot cover the focused element | Check sticky header, footer, cookie banner and chat launcher at 100% and zoomed | 2.4.11 AA (2.2) |
| Pointer targets are at least 24 × 24 CSS px or meet an exception | Measure icon buttons, close buttons, pagination, inline controls; check spacing circles | 2.5.8 AA (2.2) |
| Important targets are larger | 44 × 44 CSS px for primary controls | Guidance; 2.5.5 is AAA |
| Text contrast | Every text pair in every state and theme, including text over images | 1.4.3 AA |
| Non-text contrast | Component boundaries needed to identify them, icons that convey meaning, chart elements | 1.4.11 AA |
| Every drag has a single-pointer alternative | Sliders, sortable lists, maps, carousels, file drop zones | 2.5.7 AA (2.2) |
| Repeated help is in the same relative order | Help link, contact details and chat launcher across templates | 3.2.6 A (2.2) |
| Form fields have visible labels, instructions before the field and designed error messages | See [forms.md](forms.md) | 3.3.2 A; 3.3.1 A; 3.3.3 AA |
| Information is not asked twice in one process | Shipping/billing, multi-step flows | 3.3.7 A (2.2) |
| Narrow layout exists | A 320 CSS px wide layout without two-dimensional scrolling (data tables, maps and similar excepted) | 1.4.10 AA |
| Hover-only content is avoided or dismissible, hoverable and persistent | Tooltips, previews, mega-menus | 1.4.13 AA |
| Auto-moving content has a pause control | Carousels, tickers, animated backgrounds over five seconds | 2.2.2 A |
| Nothing flashes more than three times per second | Video, animation, loaders | 2.3.1 A |
| Reduced-motion alternative is specified | Each animation has a reduced or static version | Guidance; 2.3.3 is AAA |
| Accessible names are planned for icon-only controls | Each icon button has its name in the annotations | 4.1.2 A |

## Sources

Consulted on 2026-11-15:

- WCAG 2.2 (W3C Recommendation, 12 December 2024): https://www.w3.org/TR/WCAG22/
- What's New in WCAG 2.2: https://www.w3.org/WAI/standards-guidelines/wcag/new-in-22/
- What's New in WCAG 2.1: https://www.w3.org/WAI/standards-guidelines/wcag/new-in-21/
- Understanding 1.3.2 Meaningful Sequence: https://www.w3.org/WAI/WCAG22/Understanding/meaningful-sequence.html
- Understanding 1.4.11 Non-text Contrast: https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html
- Understanding 2.4.7 Focus Visible: https://www.w3.org/WAI/WCAG22/Understanding/focus-visible.html
- Understanding 2.4.11 Focus Not Obscured (Minimum): https://www.w3.org/WAI/WCAG22/Understanding/focus-not-obscured-minimum.html
- Understanding 2.5.7 Dragging Movements: https://www.w3.org/WAI/WCAG22/Understanding/dragging-movements.html
- Understanding 2.5.8 Target Size (Minimum): https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html
- Understanding 3.2.6 Consistent Help: https://www.w3.org/WAI/WCAG22/Understanding/consistent-help.html
