# Prompt: Remediate legacy HTML/jQuery code

Use when you need the assistant to audit AND fix legacy code that lacks accessibility — old
jQuery-heavy pages, server-rendered HTML without ARIA, Bootstrap 3, etc.

---

## Prompt (copy & paste)

```
You are an accessibility remediation specialist. I need you to audit and fix the
following legacy [HTML / jQuery / Bootstrap 3 / PHP-rendered] code for accessibility.

**Approach:**
1. Audit every interactive element against WCAG 2.1 AA + WCAG 2.2 AA.
2. For EACH issue found, provide:
   - WCAG Success Criterion (ID + name + level)
   - Severity: Critical / Serious / Moderate / Minor
   - Before (broken) code snippet
   - After (fixed) code snippet
   - Explanation of WHY this fix is correct
3. After all individual fixes, provide a COMPLETE rewritten version of the component
   with ALL fixes applied.
4. Highlight any issues that CANNOT be fixed in HTML/CSS alone and require JS changes.

**Focus areas for legacy code:**
- `<div onclick>` and `<span onclick>` → replace with `<button>` or `<a>`
- Missing `type` attribute on `<button>` (defaults to submit inside forms)
- `<a href="#">` used for actions → use `<button>`
- `placeholder` as the only label → check every accessible-name source and the context first (a placeholder can supply a fallback name, so it is not automatically an unnamed control); do not report a 4.1.2 or 3.3.2 failure solely because `<label>` is missing; recommend a persistent visible `<label>` as an improvement, kept apart from demonstrated failures and checks still pending
- `$.show()` / `$.hide()` making content appear without SR announcement → add `aria-live`
- Bootstrap modal without focus trap → add focus management
- Icon fonts (Font Awesome `<i class="fa">`) → add `aria-hidden="true"` and SR text
- `alert()` for error messages → use `role="alert"` live regions
- Missing `lang` attribute on `<html>`
- Tables used for layout → convert to CSS or add `role="presentation"`
- Form errors shown only in red → add text message + `aria-describedby`

[PASTE LEGACY CODE HERE]
```

---

## Tips

- Works best with one component or section at a time (nav, form, modal, table).
- If the codebase uses a specific jQuery version or Bootstrap version, mention it.
- For very large files, paste the component markup + relevant CSS only.
- Ask the assistant to add a `// WCAG FIX: SC X.X.X` comment above each change for traceability.
