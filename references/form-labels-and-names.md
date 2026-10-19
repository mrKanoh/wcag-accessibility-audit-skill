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

### Behavior: shown, described, possible, observed

Label each claim about behavior with the level of evidence it has:

| Level | Meaning | Wording that fits |
|-------|---------|-------------------|
| **Shown** | The supplied code demonstrates it | "the markup has no accessible name" |
| **Described** | A comment or description says it; the code is not provided | "the comment says the script removes the item and then calls `focus()` on it" (attribute it to its source) |
| **Possible** | A consequence or risk that follows from the code or the description under a condition | "if the trigger is gone when `focus()` runs, the call cannot focus it and focus may end up somewhere unhelpful" |
| **Observed** | Seen in a test that was actually run | "in NVDA with Firefox the control was announced as…" (say what was run) |

- A "not run" disclaimer at the start does not make concrete consequences safe later. Without a real test, do not state as fact where focus ends, where Tab continues, which position is lost, or what a screen reader does or does not announce. Say it as a risk with its condition, say who could be affected, and name the check.
- What a fragment does not contain is not proof that the page lacks it. A missing status region in a snippet does not show that none exists, nor a 4.1.3 failure: it cannot be assessed.
- Recommended destinations (for example where focus goes after the control that opened a dialog disappears) are guidance, such as the APG (see `authentication-and-modal-focus.md`), not a WCAG requirement for a specific element. Propose the destination with its reason and the check still pending: focus destination, Tab continuation and announcements in the real environment.
- Choosing the least destructive control as initial focus fits when the action is known to be hard to reverse; otherwise it depends on the task.

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

## 5. Repeated names (lists, tables, repeated actions)

Several controls sharing a name, such as a "Delete" button on every row, are not by themselves a
WCAG failure. No success criterion requires unique accessible names. Keep three questions apart:

| Question | Criterion | What it asks |
|----------|-----------|--------------|
| Does the name exist? | 4.1.2 | The name is programmatically determinable. Repeated names do not fail it |
| Does the label describe the purpose? | 2.4.6 | A label that exists must describe topic or purpose. A short word can be enough ("a word, or even a single character, may suffice"). Report a failure only with the reason this label does not describe the purpose here, not from repetition alone |
| Can the target of the action be identified? | 2.4.4 (links only) | A link's purpose is determined from its text alone or with its programmatically determined context. It is about links; do not move it to buttons automatically |

- 2.5.3 Label in Name asks that the accessible name contain the visible label text. It does not require unique names and does not require adding an object name. A name that starts with the visible text and adds the object (for example "Delete Report.pdf") still meets it.
- A possible problem when controls are listed on their own (a controls list, voice commands) is a barrier to explain, not a failure by itself: say who is affected, what context (row text, heading, `aria-labelledby`/`aria-describedby` association) already identifies the target, and what still has to be checked in the browser and with assistive technology.
- Classify the case: **justified failure** (the label is inaccurate or unclear in its context, or the purpose of a link cannot be determined from text and context); **context pending** (it depends on markup, CSS or behavior not shown); **recommendation** (more specific names).
- A more specific name such as "Delete Report.pdf" can be an improvement. Keep "Delete" in it. Do not impose `aria-label` when the context or a suitable association (`aria-labelledby` to the button and the item name, `aria-describedby`, row context) already solves the need.
- This is not "repeated names are always fine": evaluate the case. Identical text for controls that do different things in an ambiguous context is the situation to flag.

## Source types

| Type | Sources |
|------|---------|
| Normative | WCAG 2.2: https://www.w3.org/TR/WCAG22/ |
| Understanding (informative) | https://www.w3.org/WAI/WCAG22/Understanding/name-role-value.html, labels-or-instructions.html, headings-and-labels.html, label-in-name.html, link-purpose-in-context.html, identify-input-purpose.html, info-and-relationships.html |
| Techniques and failures | F68, F111, H44, H65, H91, H98, F107, F82 (cited from the Understanding pages above) |
| Accessibility API mapping | HTML-AAM (Working Draft): https://www.w3.org/TR/html-aam/, accessible name computation for `input`, `textarea` and `button` |
