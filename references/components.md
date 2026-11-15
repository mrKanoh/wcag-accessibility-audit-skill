# Accessible components and keyboard patterns

Markup, focus and keyboard behaviour for common custom components, and the expected keys for each widget type.

## Contents

- [Accessible Components](#accessible-components)
  - [Before you build a custom component](#before-you-build-a-custom-component)
  - [Modal Dialog](#modal-dialog)
  - [Tab Panel](#tab-panel)
  - [Accessible Form Validation](#accessible-form-validation)
  - [Combobox (Autocomplete)](#combobox-autocomplete)
  - [Accessible Button vs. Link (WCAG 2.2 friendly)](#accessible-button-vs-link-wcag-22-friendly)
  - [Accessible Drag & Drop (WCAG 2.5.7)](#accessible-drag--drop-wcag-257)
  - [Tooltip and toggletip (last resort)](#tooltip-and-toggletip-last-resort)
- [Keyboard Interaction Patterns](#keyboard-interaction-patterns)

---

## Accessible Components

### Before you build a custom component
Design guidance, not WCAG requirements (source: Heydon Pickering, *Inclusive Components*, 2018–2019; the chapter is cited per item). Ask first whether a simpler, native pattern does the job:
- **Tooltip** (book chapter «Tooltips & Toggletips»): last resort. Show the information as visible text instead. If you need one, use the recipe in «Tooltip and toggletip (last resort)» below.
- **Tabs** («Tabbed Interfaces»): avoid when there are more than about four, or when nothing needs them; use an accordion (disclosure buttons) or plain headed sections. The APG tabs pattern gives the `tabpanel` `tabindex="0"` when its first content is not focusable; the book documents a variant of panel focus, and this skill follows the APG.
- **Modal dialog** («Modal Dialogs»): only for something urgent or critical. Consider `confirm()` (the book) or native `<dialog>` (this skill, see below) first, or inline content.
- **Carousel** («Content Slider»): prefer a scrollable or stepped slider that never moves by itself. A scrolling slider must be keyboard-reachable (a named region with `tabindex="0"` if it overflows). WCAG 2.2.2 applies to content that starts automatically, moves for more than 5 seconds and appears alongside other content: it needs pause, stop or hide.
- **Menu** («Menus & Menu Buttons»): `role="menu"` is for application actions, not site navigation; use `nav` with a list of links (see [WAI-ARIA Quick Reference](semantic-html-and-aria.md#wai-aria-quick-reference)).

### Modal Dialog
```html
<div role="dialog" aria-modal="true" aria-labelledby="title" aria-describedby="desc">
  <h2 id="title">Confirm Delete</h2>
  <p id="desc">This action cannot be undone.</p>
  <button>Delete</button>
  <button aria-label="Close dialog">×</button>
</div>
```
- Initial focus depends on the content and the task (APG guidance; WCAG does not name the element): the first focusable element for a simple dialog; a static title or the start of long or structured content (`tabindex="-1"`, focused by script, not a Tab stop) so reading starts at the top; the least destructive action when the action is hard to reverse
- On close, focus normally returns to the trigger; if it no longer exists or the flow moves on, to a logical element of the workflow
- Keyboard (APG): Tab and Shift+Tab stay inside the dialog and Escape closes it. WCAG asks that keyboard users are not trapped (2.1.2) and can operate the dialog (2.1.1)
- Background: `inert` (or `aria-hidden="true"` with care)
- `role="dialog"` and `aria-modal="true"` only describe the dialog; an inert background, Tab containment, Escape and focus management must be implemented. Native `<dialog>.showModal()` makes the rest of the document inert, applies the HTML dialog focusing steps and restores focus to the previously focused element on close; an inert background is not the same as a Tab cycle written in JavaScript, so verify Tab, Escape and initial focus in your target browsers. Details: [authentication-and-modal-focus.md](authentication-and-modal-focus.md)

### Tab Panel
```html
<div role="tablist" aria-label="Account settings">
  <button role="tab" id="t1" aria-selected="true"  aria-controls="p1">Profile</button>
  <button role="tab" id="t2" aria-selected="false" aria-controls="p2" tabindex="-1">Security</button>
</div>
<div role="tabpanel" id="p1" aria-labelledby="t1" tabindex="0">…</div>
<div role="tabpanel" id="p2" aria-labelledby="t2" tabindex="0" hidden>…</div>
```
- Arrow keys switch tabs; Home/End jump to first/last
- `tabindex="0"` on each `tabpanel` puts the panel in the page's Tab sequence ([APG Tabs](https://www.w3.org/WAI/ARIA/apg/patterns/tabs/), checked 2026-11-09: set it when the panel has no focusable content or its first content is not focusable). If the first element inside the panel is focusable (a button, link or field), omit it
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
When to validate, when to use `role="alert"`, and an error summary with focus management: [forms.md](forms.md).

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
<!-- Action → button. Toggle: fixed label + aria-pressed -->
<button type="button" aria-pressed="false">Like</button>

<!-- Navigation → link -->
<a href="/dashboard">Dashboard</a>

<!-- Icon button (always needs accessible name) -->
<button aria-label="Delete item">
  <svg aria-hidden="true" focusable="false">…</svg>
</button>
```
- Toggle buttons use ONE form: a fixed label with `aria-pressed`, or a label that changes with no `aria-pressed`. Don't change the label and the state at the same time ([APG button pattern](https://www.w3.org/WAI/ARIA/apg/patterns/button/)).
- Targets ≥ **24×24 CSS px** (WCAG 2.5.8). 44×44 recommended for touch.
- Visible focus ring (WCAG 2.4.7); if you style it, ≥ 3:1 vs adjacent colors (WCAG 1.4.11). 2.4.13 (AAA) adds size and focused-vs-unfocused contrast.
- Never rely on color alone for state (e.g., disabled, selected).

### Accessible Drag & Drop (WCAG 2.5.7)
SC 2.5.7 (AA, WCAG 2.2) requires that any function done by dragging can also be done with a single pointer without dragging, unless dragging is essential. Reordering with plain buttons is enough. Keep a normal list (not a `listbox`, whose children must be `option`s and cannot contain buttons) and announce the result in a status region:
```html
<ul aria-label="Reorder items">
  <li>
    <span>Item A</span>
    <button type="button" data-move="up" aria-label="Move up: Item A">↑</button>
    <button type="button" data-move="down" aria-label="Move down: Item A">↓</button>
  </li>
  <li>
    <span>Item B</span>
    <button type="button" data-move="up" aria-label="Move up: Item B">↑</button>
    <button type="button" data-move="down" aria-label="Move down: Item B">↓</button>
  </li>
</ul>
<p role="status" class="visually-hidden"></p> <!-- after a move, write e.g. "Item A moved to position 2 of 3" -->
```
Moving the `<li>` with `insertBefore()` removes it from the DOM and re-inserts it, which drops focus to the document (in practice `<body>`): the HTML Standard's removing steps set the focused area to the viewport when the focused node is removed, and the focus fixup rule does the same when the focused element stops being a focusable area (html.spec.whatwg.org, checked 2026-11). After the move, call `.focus()` again on the button the user pressed; if it is now disabled or hidden at a list edge (first item's "Move up"), focus the other button of the pair instead of losing focus. `Node.moveBefore()` moves a node without resetting its state (including focus); it is newer, so feature-detect it (`if (list.moveBefore)`) and keep the explicit `.focus()` as the fallback. Not compiled or run; `moveBefore` support was not checked here.

### Tooltip and toggletip (last resort)
Prefer visible text (see «Before you build a custom component»). The `title` attribute is not a substitute: it is not keyboard- or touch-accessible, and browser-controlled tooltips fall under the 1.4.13 exception, so they are not covered by its protections.

**Tooltip** = supplementary description of a focusable control. The control keeps its own accessible name; the tip is its description (`aria-describedby`). Use `aria-labelledby` only when the tip is the control's name (icon-only control without other text). Requirements ([WCAG 1.4.13](https://www.w3.org/WAI/WCAG22/Understanding/content-on-hover-or-focus.html), checked 2026-11-06): dismissible without moving pointer or focus (Esc), hoverable (the pointer can move onto the tip), persistent (stays until hover/focus leaves or the user dismisses). Appear on focus **and** hover; no interactive content inside. The [APG tooltip pattern](https://www.w3.org/WAI/ARIA/apg/patterns/tooltip/) is marked work in progress (no task-force consensus yet), so treat it as provisional.
```html
<span class="tip-wrap">
  <button type="button" aria-describedby="tip-save">Save</button>
  <span role="tooltip" id="tip-save" hidden>Saves a draft. Nothing is published.</span>
</span>
<script>
document.querySelectorAll('.tip-wrap').forEach((wrap) => {
  const tip = wrap.querySelector('[role="tooltip"]');
  let hovered = false, focused = false;
  const update = () => { tip.hidden = !(hovered || focused); };
  wrap.addEventListener('mouseenter', () => { hovered = true; update(); });
  wrap.addEventListener('mouseleave', () => { hovered = false; update(); });
  wrap.addEventListener('focusin',    () => { focused = true; update(); });
  wrap.addEventListener('focusout',   () => { focused = false; update(); });
  document.addEventListener('keydown', (e) => {   // Esc hides it; focus does not move
    if (e.key === 'Escape' && !tip.hidden) { hovered = focused = false; tip.hidden = true; }
  });
});
</script>
```
Position the tip touching or overlapping the trigger (no gap), so the pointer can reach it without leaving `.tip-wrap`. If the control sits inside a dialog, Esc can close both the tip and the dialog; closing only the tip requires listening in the capture phase (`addEventListener('keydown', fn, true)`) and calling `stopPropagation()` only while the tip is visible.

**Toggletip** = a button that reveals information that is not the control's label, announced through a live region. The `role="status"` container exists in the DOM before the content is inserted. Closes with Esc, when focus leaves, or on a click outside (some browsers, e.g. Safari on macOS, do not focus a button on click, so no blur fires).
```html
<span class="toggletip">
  <button type="button" aria-label="More about password rules">i</button>
  <span role="status"></span>
</span>
<script>
document.querySelectorAll('.toggletip').forEach((box) => {
  const btn = box.querySelector('button');
  const live = box.querySelector('[role="status"]');
  btn.addEventListener('click', () => {
    live.textContent = '';  // re-insert so a repeat click is announced again
    setTimeout(() => { live.textContent = 'Use at least 12 characters.'; }, 100);
  });
  const close = () => { live.textContent = ''; };
  btn.addEventListener('blur', close);
  box.addEventListener('keydown', (e) => { if (e.key === 'Escape') close(); });
  document.addEventListener('click', (e) => { if (!box.contains(e.target)) close(); });
});
</script>
```
Pointer persistence also applies to a toggletip if it opens on hover; opening on click avoids that. Screen reader announcement of live regions varies; test with your target pairs.

---

## Keyboard Interaction Patterns

| Widget | Keys |
|--------|------|
| Link | Tab, Enter |
| Button | Tab, Enter, Space |
| Checkbox / Switch | Tab, Space |
| Radio group | Tab onto group; Arrow keys between |
| Select / Listbox | Tab, Arrows, Home/End, type-ahead |
| Combobox | Tab, Arrows, Enter, Esc |
| Tabs | Tab to list; Arrow keys switch; Enter/Space activate |
| Menu / Menu bar (application menus only; not site navigation, see [WAI-ARIA Quick Reference](semantic-html-and-aria.md#wai-aria-quick-reference)) | Arrow keys, Enter, Esc, Tab exits |
| Dialog | Tab cycles inside; Esc closes |
| Tree | Arrows (→ expand, ← collapse), Enter activates |
| Grid / Data table | Arrow keys between cells; Enter activates cell editor |
| Slider | Arrow keys, Home/End, PgUp/PgDn |
| Date picker | Arrow keys calendar, PgUp/PgDn months |
