# Accessible Component Examples

Reference and learning HTML components demonstrating WCAG 2.1/2.2 AA accessibility patterns.
Each file is self-contained, except the demo poster and video of `media-player.html`, which load from external hosts. No keyboard or screen-reader verification is recorded for these examples; test and review them before using any of them in production.

---

## Components

### 🗓️ [date-picker.html](./date-picker.html)
**Pattern:** Dialog — WAI-ARIA Date Picker Dialog Pattern  
**WCAG SCs:** 1.3.1, 2.1.1, 2.1.2, 2.4.3, 2.4.7, 2.4.11, 4.1.2

| Feature | Implementation |
|---------|---------------|
| Keyboard | Arrow keys navigate days; Page Up/Down change months; Home/End jump to week start/end |
| Screen reader | `role="dialog"` + `aria-modal` + `aria-labelledby`; day buttons announce full date |
| Focus trap | Tab cycles within dialog; Escape closes and returns focus to trigger |
| Text input | Typed dates (`MM/DD/YYYY`) parsed with live error region |
| Roving tabindex | Only focused day has `tabindex="0"` |

---

### 🔔 [toast-notifications.html](./toast-notifications.html)
**Pattern:** Live Region / Status Message  
**WCAG SCs:** 1.3.3, 2.2.1, 4.1.3

| Feature | Implementation |
|---------|---------------|
| Polite region | `role="status"` + `aria-live="polite"` for success, info, warning |
| Assertive region | `role="alert"` + `aria-live="assertive"` for errors only; `aria-atomic="false"` so each new toast is announced alone. Error toasts are plain groups: no `alertdialog`, focus never moves (APG alert) |
| Dismiss | Every toast has a dismiss button with accessible name |
| Time limit | Success and info toasts are timed (5 s) and pause (timer and progress bar) on hover and focus as a courtesy. Errors and anything that asks for action (the "Session expiring" toast) have no timer and stay until dismissed: the APG alert pattern advises avoiding alerts that disappear on their own, and the 2.2.1 Understanding page treats a 5-second toast as exempt only when the user can learn the information another way. Relevant criterion: 2.2.1 Timing Adjustable (not 2.2.2, which covers moving or auto-updating content) |
| Reduced motion | Slide animation disabled when `prefers-reduced-motion: reduce` |

---

### 🎠 [carousel.html](./carousel.html)
**Pattern:** Carousel — WAI-ARIA Carousel Pattern  
**WCAG SCs:** 2.2.2, 1.3.1, 2.1.1, 2.4.7, 4.1.2

| Feature | Implementation |
|---------|---------------|
| Play/Pause | Required by WCAG 2.2.2 — button always visible; the carousel starts paused and only the user starts it |
| ARIA | `role="region"` + `aria-roledescription="carousel"` on container; `role="group"` + `aria-roledescription="slide"` on slides |
| Auto-pause | Rotation stops when keyboard focus enters the carousel and does not restart unless the user asks (APG). It also stops while the pointer is over it; this example does not resume it on pointer leave either (a stricter choice than the APG requires) |
| Dot navigation | Native `<button>`s in a labelled `role="group"` with `aria-current="true"` on the active one (the APG grouped style marks the current picker with `aria-disabled` instead; this example's choice). One tab stop per dot |
| Keyboard | Left/Right arrows change slide from anywhere in the carousel (single handler); Play/Pause, dots and arrows are native buttons (Enter/Space) |
| Announcements | `aria-live="polite"` on slide area (only when paused to avoid verbosity) |

---

### 🌳 [tree-view.html](./tree-view.html)
**Pattern:** Tree View — WAI-ARIA Tree Pattern  
**WCAG SCs:** 2.1.1, 2.4.3, 2.4.7, 4.1.2

| Feature | Implementation |
|---------|---------------|
| ARIA structure | `role="tree"` → `role="treeitem"` → `role="group"` (nested) |
| Expand/collapse | `aria-expanded` on parent nodes; the `hidden` attribute on collapsed nested groups |
| Selection | Enter/Space (or click) select a node and toggle it if it has children; `aria-selected="true"` on the selected `treeitem` (single-select) |
| Focus | The `treeitem` carries `tabindex` 0/-1, but each node also holds a `<button>` that Tab can reach, so this is not a clean roving tabindex yet |
| Keyboard | ↑↓ navigate; → expand or enter child; ← collapse or exit to parent; Home/End jump; `*` expands all visible nodes at the same level, even under other parents (the APG says siblings) |
| Position | `aria-level`, `aria-setsize`, `aria-posinset` on every node |

---

### 🗂️ [tabs.html](./tabs.html)
**Pattern:** Tabs — WAI-ARIA Tabs Pattern  
**WCAG SCs:** 1.3.1, 2.1.1, 2.4.3, 4.1.2

| Feature | Implementation |
|---------|---------------|
| ARIA structure | `role="tablist"` → `role="tab"` → `role="tabpanel"` |
| State | `aria-selected` reflects active tab |
| Relationship | `aria-controls` links tab to panel; `aria-labelledby` links panel to tab |
| Roving tabindex | Only the active tab has `tabindex="0"` |
| Keyboard | ←/→ Arrow keys switch tabs with automatic activation; Home/End jump |

---

### 🎥 [media-player.html](./media-player.html)
**Pattern:** Custom Media Player  
**WCAG SCs:** 1.2.2, 1.2.3, 1.2.5, 2.1.1, 2.4.7, 2.5.3, 4.1.2

| Feature | Implementation |
|---------|---------------|
| Captions | Embedded `<track kind="captions">` with toggle button |
| Audio Description | Embedded `<track kind="descriptions">` with toggle button |
| Keyboard | Native behavior only, no custom shortcuts: Tab between controls, Space/Enter activate the focused button, arrow keys move the focused slider (seek or volume) |
| ARIA states | Fixed label + `aria-pressed` for CC and AD (names `CC (closed captions)` / `AD (audio descriptions)` contain the visible text, 2.5.3); Play/Pause and Mute/Unmute change their label and do not use `aria-pressed` (never both) |
| Play/Pause label | Follows the video's `play`, `pause` and `ended` events, not only clicks |
| ARIA values | `aria-valuetext` on sliders for screen readers to read percentages |

---

### 📊 [data-grid.html](./data-grid.html)
**Pattern:** Sortable, filterable data table (native `<table>`, not an ARIA grid)

**WCAG SCs:** 1.3.1, 2.1.1, 2.5.3, 4.1.2, 4.1.3

| Feature | Implementation |
|---------|---------------|
| Name | Named by its `<caption>` (no `aria-label` on the table) |
| Sorting | `<th scope="col" aria-sort>` containing a native `<button>`; Enter/Space sort and `aria-sort` toggles ascending/descending; a status region announces the result |
| Search | Visible `<label>` "Search:" is the field's name (name matches label, 2.5.3); result count in a live region |
| Row controls | Native checkboxes and buttons with row context in their names; select-all with `indeterminate` state |
| Keyboard | Native behavior only: Tab through the controls, Enter/Space on buttons, Space on checkboxes. No cell-by-cell grid navigation |
| Not verified | The `overflow-x:auto` wrapper has no `tabindex`, role or name; see `PROGRESS.md` |

---

## Testing these components

### Keyboard test
Open any file in a browser and test with keyboard only:
- `Tab` to reach the component
- Use the documented keyboard shortcuts for each component
- Verify focus is always visible (never lost)
- Verify `Escape` closes dialogs and menus

### Screen reader test (recommended pairs)
- **NVDA 2023.x + Firefox** (Windows) — most common AT pair
- **VoiceOver + Safari** (macOS/iOS)
- **TalkBack + Chrome** (Android)

### Automated check
```bash
# Run axe-core on any component via CLI
npx axe examples/components/date-picker.html
npx axe examples/components/carousel.html
```

---

## Adding a new component

See [`CONTRIBUTING.md`](../../CONTRIBUTING.md#adding-a-component-example) for the full
checklist and required header comment template.
