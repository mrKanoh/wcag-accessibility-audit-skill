# Prompt: Generate an accessible ARIA pattern

Use when you need complete reference code for a complex accessible widget. Review and test the output (keyboard, screen reader) before shipping it.

---

## Prompt (copy & paste)

```
Write reference code for an accessible [COMPONENT] in [HTML+JS / React / Vue 3 / Svelte / Angular].

Requirements:
1. Follow the WAI-ARIA Authoring Practices Guide (APG) pattern for [COMPONENT]
2. Include all required ARIA roles, states, and properties
3. Full keyboard support (specify which keys and what they do)
4. Correct focus management (where focus moves on open/close/selection)
5. Visible focus indicator (:focus-visible)
6. Works with NVDA+Firefox and VoiceOver+Safari
7. No violations when run through axe-core
8. Reduced motion: respect prefers-reduced-motion for any transitions
9. Forced colors: work in Windows High Contrast Mode

Component: [e.g. "Modal dialog with confirm/cancel", "Multi-select combobox", "Sortable data table", "Accordion", "Date picker"]
Framework: [HTML+Vanilla JS / React 18 / Vue 3 / Svelte 5 / Angular 17]
Additional context: [Any specific requirements — dark mode, Tailwind, headless, etc.]
```

---

## Tips

- The more specific you are about the component behavior, the better the output.
- Always test generated patterns with a real screen reader before shipping.
- For complex components (data grids, carousels, trees), request the keyboard interaction table separately.
