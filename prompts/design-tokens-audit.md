# Prompt: Audit design tokens against WCAG

Use when you want the assistant to audit a set of design tokens (from Figma Tokens,
Style Dictionary, or a CSS custom properties file) against WCAG color contrast
and semantic accessibility requirements.

---

## Prompt (copy & paste)

```
Audit the following design tokens for WCAG 2.1/2.2 AA compliance.

For each token pair that is used as text-on-background or UI-on-background,
calculate the contrast ratio and report:
1. Token names (e.g., --color-text-primary on --color-bg-surface)
2. Hex values
3. Contrast ratio (to 2 decimal places)
4. WCAG result: Pass AA / Fail AA / Pass AAA / Fail AAA
5. Context: text (4.5:1 required) / large text (3:1) / UI component (3:1) / decorative (exempt)
6. Fix suggestion if failing: provide an adjusted hex value that passes with minimal
   visual change (adjust lightness in HSL, not arbitrary change)

**Contrast thresholds:**
- Normal text AA: 4.5:1 (SC 1.4.3)
- Large text AA (18pt / 14pt bold): 3:1 (SC 1.4.3)
- UI components, icons, borders: 3:1 (SC 1.4.11)
- Focus indicators vs adjacent: 3:1 (SC 2.4.11 / 2.4.13)
- Text AAA: 7:1 | Large text AAA: 4.5:1

**Also check:**
- Are all states defined? (default, hover, active, focus, disabled, error, selected)
  — Disabled elements are exempt from contrast, but non-text disabled indicators are not
- Is meaning conveyed through color alone anywhere?
  (e.g., "red = error" without icon or text label — fails SC 1.4.1)
- Do the tokens include a forced-colors / high contrast mode variant?
  (check for `forced-colors: active` media query support)
- Are focus ring tokens defined and do they meet 3:1 against adjacent colors?

**Design tokens to audit:**
[PASTE TOKENS — CSS custom properties, JSON, or Figma Tokens format]

**Usage context (optional — helps determine which threshold applies):**
[e.g., "color-text-muted is used for helper text below inputs"]
```

---

## Tips

- Paste CSS variables (`--color-*: #hex;`) or a JSON token object.
- Figma Tokens plugin exports a JSON that you can paste directly.
- For a full palette audit, list the pairs you actually use in the UI (not all combinations).
- If the assistant can read this repository's files, point it to `data/color-palette-rules.csv`
  for additional palette design rules; otherwise paste the relevant rows.
- Use the [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/)
  to verify the assistant's calculations if needed.
