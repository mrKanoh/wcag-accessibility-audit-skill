# Prompt: Audit this component

Use when you want the assistant to evaluate a UI component for accessibility issues.

---

## Prompt (copy & paste)

```
Audit the following [HTML / React / Vue / Svelte] component for accessibility issues.

For each issue found:
1. Identify the WCAG Success Criterion (ID + name + level) and why it applies to this element
2. Rate severity: Critical / Serious / Moderate / Minor, with a one-line reason (who is affected, any workaround, how widespread)
3. Explain the real-world impact on users with disabilities
4. Provide a corrected code snippet

Apply these checks as a minimum:
- Accessible name on every interactive element (4.1.2)
- Keyboard operability (2.1.1) and no traps (2.1.2)
- Visible focus indicator (2.4.7 / 2.4.11)
- Correct ARIA roles, states, and properties
- Color not used as sole conveyor (1.4.1)
- Heading hierarchy (1.3.1)
- Alt text on images (1.1.1)
- Form labels or instructions (3.3.2), and error messages (3.3.1 / 3.3.3) only where the code shows error handling
- Target size ≥ 24×24 CSS px (2.5.8 WCAG 2.2)

Label every finding as one of: demonstrated by the code / needs verification (browser, keyboard,
screen reader, server) / design recommendation. Do not infer behavior the code does not show (required
fields, server errors, CSS, scripts). Do not state what a screen reader announced or what an automated
tool would report unless it was run. Check every accessible-name source before reporting a missing name.

[PASTE COMPONENT CODE HERE]
```

---

## Tips

- Paste the full component including markup, not just a description.
- For React/Vue/Svelte, include any props that affect rendering.
- If you have context about how the component is used (inside a modal, inside a form), include it.
