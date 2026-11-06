# Accessible Component Examples

Reference and learning HTML components demonstrating WCAG 2.1/2.2 AA accessibility patterns.
Each file is self-contained (no external dependencies). No keyboard or screen-reader verification is recorded for these examples; test and review them before using any of them in production.

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
**WCAG SCs:** 1.3.3, 2.2.2, 4.1.3

| Feature | Implementation |
|---------|---------------|
| Polite region | `role="status"` + `aria-live="polite"` for success, info, warning |
| Assertive region | `role="alert"` + `aria-live="assertive"` for errors only |
| Dismiss | Every toast has a dismiss button with accessible name |
| Pause on hover/focus | Timers pause on hover and focus (WCAG 2.2.2) |
| Reduced motion | Slide animation disabled when `prefers-reduced-motion: reduce` |

---

### 🎠 [carousel.html](./carousel.html)
**Pattern:** Carousel — WAI-ARIA Carousel Pattern  
**WCAG SCs:** 2.2.2, 1.3.1, 2.1.1, 2.4.7, 4.1.2

| Feature | Implementation |
|---------|---------------|
| Play/Pause | Required by WCAG 2.2.2 — button always visible; pauses auto-rotation |
| ARIA | `role="region"` + `aria-roledescription="carousel"` on container; `role="group"` + `aria-roledescription="slide"` on slides |
| Auto-pause | Rotation pauses on hover, focus-in, and when `prefers-reduced-motion` is set |
| Dot navigation | `role="tablist"` + `role="tab"` dots with `aria-current` and roving tabindex |
| Announcements | `aria-live="polite"` on slide area (only when paused to avoid verbosity) |

---

### 🌳 [tree-view.html](./tree-view.html)
**Pattern:** Tree View — WAI-ARIA Tree Pattern  
**WCAG SCs:** 2.1.1, 2.4.3, 2.4.7, 4.1.2

| Feature | Implementation |
|---------|---------------|
| ARIA structure | `role="tree"` → `role="treeitem"` → `role="group"` (nested) |
| Expand/collapse | `aria-expanded` on parent nodes; `aria-hidden` on nested groups |
| Roving tabindex | Only focused node has `tabindex="0"` |
| Keyboard | ↑↓ navigate; → expand or enter child; ← collapse or exit to parent; Home/End jump; `*` expands all siblings |
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
**WCAG SCs:** 1.2.2, 1.2.3, 1.2.5, 2.1.1, 2.4.7, 4.1.2

| Feature | Implementation |
|---------|---------------|
| Captions | Embedded `<track kind="captions">` with toggle button |
| Audio Description | Embedded `<track kind="descriptions">` with toggle button |
| Keyboard | Space/Enter plays/pauses; Arrow keys scrub video and adjust volume |
| ARIA states | Fixed label + `aria-pressed` for CC and AD; Play/Pause and Mute/Unmute change their label and do not use `aria-pressed` (never both) |
| ARIA values | `aria-valuetext` on sliders for screen readers to read percentages |

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
