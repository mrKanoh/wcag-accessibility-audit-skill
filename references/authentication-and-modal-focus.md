# Accessible authentication (3.3.8, 3.3.9) and focus in modal dialogs

Read this when a review covers a login or verification flow, or the focus behavior of a modal dialog.
It keeps three things apart: what the criterion requires (normative), a technique that can meet it,
and what still has to be checked in the real process or page.

## 1. Accessible authentication

**Requirement (WCAG 2.2, normative).** A cognitive function test (such as remembering a password or
solving a puzzle) is not required for any step in an authentication process unless that step provides
at least one of the following:

| Exception | 3.3.8 (AA) | 3.3.9 (AAA) |
|-----------|------------|-------------|
| Alternative: another authentication method that does not rely on a cognitive function test | yes | yes |
| Mechanism: a mechanism is available to assist the user in completing the test | yes | yes |
| Object recognition: the test is to recognize objects | yes | **no** |
| Personal content: the test is to identify non-text content the user provided | yes | **no** |

Understanding defines a cognitive function test as a task that requires the user to remember,
manipulate or transcribe information. Name, email address and phone number are not treated as such tests.

**What the Understanding documents add (informative).**
- Scope is every step of authenticating an existing user, including multi-factor steps and recovery. Account creation is not covered.
- Usernames and passwords are not prohibited. Remembering a password is a cognitive function test, so the step passes through the *mechanism* exception (password managers and paste work) or an *alternative*.
- Blocking paste or autofill of a password or code is the documented failure F109.
- Requiring users to retype a verification code by hand does not meet the criterion unless an applicable alternative or assisting mechanism is available; allowing paste or autofill can satisfy the mechanism exception for that step, but does not by itself establish conformance of the whole process.
- An audio CAPTCHA that still requires transcribing is not an alternative. Object-recognition CAPTCHAs are excepted at AA only.
- Techniques cited: G218 (email link authentication), H100 (properly marked-up email and password inputs).

**How to report.**
- Do not call a whole authentication process conformant or non-conformant from one field, or from the presence of a password field, CAPTCHA, paste or autofill. The criterion is assessed per step and for the process.
- A cognitive function test with no alternative and no assisting mechanism is a *possible* failure of 3.3.8 and 3.3.9. State what evidence would confirm it (the other methods offered, whether paste and password managers work, what the CAPTCHA asks).
- An object-recognition-only challenge is excepted by 3.3.8 but not by 3.3.9 unless an alternative or mechanism is also provided. 3.3.9 is AAA: report it only when the target includes AAA.
- A password with a working password manager and paste is not a failure for requiring a password. Verify that the mechanism actually works in the browser, and check the other steps (codes, recovery).
- Blocking paste (for example `onpaste`) does not show that autofill or a password manager is blocked: check them separately. Report F109 only on evidence that re-entry in the same format is prevented.
- An alternative that does not rely on a cognitive function test can satisfy the matching 3.3.9 condition for that step if it works and the other applicable conditions are met. That is not proof that the whole process conforms at AAA.
- A CAPTCHA also falls under 1.1.1: it needs text alternatives that identify and describe its purpose, and alternative forms of CAPTCHA for different sensory modalities. If a description does not say whether the image has a text alternative, do not report it missing; ask or mark it unverified. A description that states there is no other-modality option supports a finding about alternative forms, on that basis.
- Mark the following as not verifiable from markup: whether a password manager fills the field, which methods the server offers, and how recovery works.

## 2. Initial focus and focus return in modal dialogs

**Source types.** The WAI-ARIA Authoring Practices Guide (APG) dialog (modal) pattern is guidance,
not a WCAG requirement. WCAG constrains the outcome through criteria such as 2.1.1 Keyboard,
2.1.2 No Keyboard Trap, 2.4.3 Focus Order and 2.4.7 Focus Visible. It does not say which element
receives initial focus. Say which statement is APG guidance.

**Choosing initial focus (APG).** "Generally" the first focusable element, but choose by content and task:

| Situation | Reasonable initial focus |
|-----------|--------------------------|
| Simple dialog (a short form or message) | The first control, or the control the task needs |
| Long or structured content (lists, tables, several paragraphs) that is better read from the start | A static element at the start, such as the title or the content wrapper, with `tabindex="-1"` set and focused by script; it is not a Tab stop. APG suggests not adding `aria-describedby` for such content |
| An action that is hard to reverse (delete, complete a transaction) | The least destructive action (APG alert dialog guidance). Not a universal rule: choose by task |
| Information or "continue" dialogs | The most frequently used control, such as OK or Continue |

**Returning focus (APG).** Normally to the element that opened the dialog. If that element no longer
exists (for example it was removed by the action), or the flow moves on, to a logical element of the
workflow.

**Keep.** Tab and Shift+Tab stay inside the dialog (wrap from last to first); Escape closes it; the
dialog has an accessible name (`aria-labelledby` or `aria-label`); a visible close or cancel control.

**Roles do not implement behavior.** `role="dialog"` and `aria-modal="true"` describe the dialog to
assistive technology. They do not move focus, contain Tab, close on Escape or make the page behind
inert. APG says to set `aria-modal` only when the code blocks interaction with outside content.
Native `<dialog>` opened with `showModal()`: per the HTML Standard the rest of the document is blocked
(inert), the dialog focusing steps pick an `autofocus` element, else the dialog's focus delegate, else
the dialog itself, and on close focus is restored to the previously focused element if there is one.
The standard does not define Tab cycling, and an inert background is not the same as a Tab loop
implemented in JavaScript: verify Tab, Escape and initial focus in the target browsers. Native
dialogs do not choose the best initial focus for your content; use `autofocus` or script for that, and
handle a trigger that no longer exists yourself.

**Report.** An initial-focus choice that differs from the first control is not a defect by itself.
Flag it when the result is a barrier (focus lands where it hides the start of the content, or the
focus order is illogical), and say it needs checking with keyboard and screen reader if not run.

Behavior known only from a comment or description (what a script does, where focus goes) is reported
as described, attributed to that source, and not as observed. Do not state where focus ends or from
where Tab continues unless it was run; say what the description implies and that it is unverified.
Cite a criterion only for the reason it applies (for example 2.4.3 for an illogical focus order),
not to add numbers.

## Sources

| Type | Source |
|------|--------|
| Normative | WCAG 2.2: https://www.w3.org/TR/WCAG22/#accessible-authentication-minimum and #accessible-authentication-enhanced |
| Understanding (informative) | https://www.w3.org/WAI/WCAG22/Understanding/accessible-authentication-minimum.html, accessible-authentication-enhanced.html |
| Guidance, not WCAG | APG dialog (modal): https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/ |
| Native behavior | HTML Standard, the dialog element: https://html.spec.whatwg.org/multipage/interactive-elements.html#the-dialog-element |
| CAPTCHA and 1.1.1 | WCAG 2.2: https://www.w3.org/TR/WCAG22/#non-text-content |
