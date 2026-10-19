# Reviewing form labels, accessible names and input purpose

Read this when a review covers a form control, an icon-only button or a code fragment. It keeps
what the supplied code demonstrates apart from what depends on context. Sources are listed at the
end; they have different authority (see "Source types").

## 1. Report findings in four categories

| Category | Use when |
|----------|----------|
| **Demonstrated by the code** | The markup supplied is enough (for example a `<button>` whose only content is an `aria-hidden` SVG, with no `aria-label`, `aria-labelledby` or `title`). Say it applies to the supplied markup: CSS-generated content or scripts elsewhere could change the result. |
| **Depends on context** | The criterion applies only in some situations (for example 1.3.5, only for fields collecting information about the user). State the condition. |
| **Needs verification** | Browser, keyboard, assistive-technology or server behavior decides it. Say it was not run. |
| **Design recommendation** | Useful, but no success criterion requires it (persistent visible labels, `type="email"` for the keyboard and native validation). |

- Do not state what a screen reader announced, or that axe or another tool would or would not report a case, unless it was actually run.
- Do not infer that a field is required, how errors are handled, what the server returns, or that a status message exists from a fragment that does not show it. Say it cannot be assessed.
- Give severity (Critical / Serious / Moderate / Minor) with a one-line reason: who is blocked, whether a workaround exists, how widespread it is. Not every finding is Critical.

## 2. Label versus accessible name

- A missing `<label>` does not by itself prove a missing accessible name. Check every name source for the element: `aria-labelledby`, `aria-label`, `<label>`, `title`, and for text inputs the `placeholder` fallback in the HTML-AAM mapping (a W3C Working Draft: not WCAG, and not proof of how every browser and assistive technology behaves). For `<button>`: `aria-labelledby`, `aria-label`, its content, then `title`.
- A control with none of these has no accessible name in the supplied markup: 4.1.2 (failure F68).
- `placeholder` as the only identifying text: a name usually exists through the fallback, so 4.1.2 is not shown to fail by that alone. Do not declare such a field a pass or a fail. The real concerns are that the text disappears on input, often has low contrast and leaves no persistent label: whether 3.3.2 is met is a judgement about the page, and a persistent visible `<label>` is the recommendation. Verify the name in the browser accessibility tree.
- `aria-label` with no `<label>` gives a name. It is not a 4.1.2 failure. Whether a label or instructions are presented to all users (3.3.2) is a visual check. If visible label text exists, its text should be in the name (2.5.3).

## 3. Which criterion says what

| Criterion | What it requires | What it does not |
|-----------|------------------|------------------|
| 4.1.2 Name, Role, Value | Every UI component has a name and role that software can determine | Does not say the name must come from a `<label>` |
| 1.3.1 Info and Relationships | Information and relationships conveyed visually are programmatically determinable or in text | Does not decide whether label text is useful |
| 3.3.2 Labels or Instructions | Labels or instructions are provided where content accepts input; the name may be hidden, the label is shown to all users | Does not check markup association (1.3.1) or label quality (2.4.6) |
| 2.4.6 Headings and Labels | Headings and labels that exist describe topic or purpose | Does **not** require labels to exist; never cite it as the reason to add a `<label>` |
| 1.3.5 Identify Input Purpose | For fields collecting information about the user whose purpose is in the WCAG input-purposes list, the purpose is programmatically determinable | Not for every field (an order number or a search box is out of scope) |

Cite a criterion only with the reason it applies to that element. Do not stack numbers.

## 4. Input purpose (1.3.5)

- `type="email"` and `autocomplete="email"` are different things. `type` is a broad category of input; Understanding 1.3.5 says it does not show, for example, whether an address is the user's own. The sufficient technique is `autocomplete` (H98).
- `type="text"` is not a 1.3.5 failure by itself. A field that collects the user's own email and has no valid `autocomplete` token is the situation to flag, and only if the field is plausibly about the user (say what you assumed). A wrong token is failure F107.
- `autocomplete` is the technique for HTML, not the only conceivable way to meet the criterion.
- `type="email"` is a reasonable design choice (keyboard, native validation), reported as a recommendation.

## Source types

| Type | Sources |
|------|---------|
| Normative | WCAG 2.2: https://www.w3.org/TR/WCAG22/ |
| Understanding (informative) | https://www.w3.org/WAI/WCAG22/Understanding/name-role-value.html, labels-or-instructions.html, headings-and-labels.html, identify-input-purpose.html, info-and-relationships.html |
| Techniques and failures | F68, F111, H44, H65, H91, H98, F107, F82 (cited from the Understanding pages above) |
| Accessibility API mapping | HTML-AAM (Working Draft): https://www.w3.org/TR/html-aam/, accessible name computation for `input`, `textarea` and `button` |
