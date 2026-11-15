# Building accessible forms

Read this when you build or redesign a form: labels, groups, instructions, required fields, validation, error messages, multi-step flows. It is about construction. For reviewing accessible names, `placeholder`, repeated names and input purpose in a code fragment, read [form-labels-and-names.md](form-labels-and-names.md); this file links there instead of repeating it.

Each item says whether it is a **requirement** (a WCAG 2.2 success criterion, with ID, level and the version it entered), a **technique** (a W3C sufficient or advisory technique: one way to meet a criterion, not the only one) or **guidance** (useful practice that no criterion requires). Nothing fails WCAG for missing guidance. The default target is WCAG 2.2 AA ([legal-framework.md](legal-framework.md) for when 2.1 AA applies instead).

## Contents

- [Criteria that apply to forms](#criteria-that-apply-to-forms)
- [Visible, associated labels](#visible-associated-labels)
- [Grouping with fieldset and legend](#grouping-with-fieldset-and-legend)
- [Instructions and format before the field](#instructions-and-format-before-the-field)
- [Required fields](#required-fields)
- [Input purpose and autocomplete](#input-purpose-and-autocomplete)
- [When to validate](#when-to-validate)
- [Identifying errors and suggesting fixes](#identifying-errors-and-suggesting-fixes)
- [Error summary and focus](#error-summary-and-focus)
- [Preventing errors in legal, financial and data submissions](#preventing-errors-in-legal-financial-and-data-submissions)
- [Redundant entry](#redundant-entry)
- [Multi-step forms](#multi-step-forms)
- [Changing a control must not change the context](#changing-a-control-must-not-change-the-context)
- [Authentication steps](#authentication-steps)
- [Sources](#sources)

## Criteria that apply to forms

| ID | Name | Level | Entered | What it asks of a form |
|----|------|-------|---------|------------------------|
| 1.3.1 | Info and Relationships | A | 2.0 | Labels, groups and the field ↔ instruction ↔ error relationships are programmatically determinable |
| 1.3.5 | Identify Input Purpose | AA | 2.1 | Fields that collect information about the user have a programmatically determinable purpose |
| 2.2.1 | Timing Adjustable | A | 2.0 | Time limits can be turned off, adjusted or extended (with exceptions) |
| 2.5.3 | Label in Name | A | 2.1 | The accessible name contains the visible label text |
| 3.2.2 | On Input | A | 2.0 | Changing a control's setting does not change the context unless the user was told before |
| 3.3.1 | Error Identification | A | 2.0 | A detected input error is identified and described to the user in text |
| 3.3.2 | Labels or Instructions | A | 2.0 | Labels or instructions are provided when content requires user input |
| 3.3.3 | Error Suggestion | AA | 2.0 | Known suggestions for correction are provided, unless that would jeopardize security or purpose |
| 3.3.4 | Error Prevention (Legal, Financial, Data) | AA | 2.0 | Such submissions are reversible, checked, or confirmed |
| 3.3.7 | Redundant Entry | A | 2.2 | Information already entered in the same process is auto-populated or selectable |
| 3.3.8 | Accessible Authentication (Minimum) | AA | 2.2 | No cognitive function test in an authentication step without an alternative or assistance |
| 4.1.2 | Name, Role, Value | A | 2.0 | Every control exposes name, role, state and value |
| 4.1.3 | Status Messages | AA | 2.1 | Status messages (for example "Saved", "3 results") can be presented by assistive technology without receiving focus |

Look any of them up with `python scripts/search.py wcag --id <id>`.

## Visible, associated labels

- **Requirement.** Every field needs a label or instructions (3.3.2). The association between label and field must be programmatically determinable (1.3.1); 3.3.2 itself does not check the markup. If the label is visible text, the accessible name contains it (2.5.3).
- **Technique.** A `<label for>` pointing to the field's `id` (H44), or wrapping the field in the `<label>`. For a field whose purpose is given by an adjacent button, such as a search field with a "Search" button, G167 is a last resort, not the default.
- **Guidance.** Keep the label visible and persistent above or beside the field. Understanding 3.3.2 says labels and instructions "need to be persistently available to users". Do not use `placeholder` as the only label; why it is weak, and why it is not automatically a failure, is in [form-labels-and-names.md](form-labels-and-names.md#2-label-versus-accessible-name).
- How to tell a missing label from a missing accessible name, which criterion says what, and repeated names: [form-labels-and-names.md](form-labels-and-names.md#3-which-criterion-says-what).

## Grouping with fieldset and legend

- **Requirement.** When a group of controls only makes sense together (the options of one question, the parts of a date), the group and its label are part of 1.3.1, and the group's question is a label or instruction under 3.3.2.
- **Technique (H71).** Wrap radio buttons or checkboxes that answer one question in `<fieldset>`, with `<legend>` as its first child. H71 also suggests it for looser groups that need their own heading, such as an address. It is not needed when each control's own label already gives clear instructions and distinct choices (H44 is then enough), and nesting fieldsets unnecessarily "can lead to confusion".
- **Caution on announcements.** H71 says that "often" user agents present the legend before each control's label. That is not a guarantee: test with the screen readers you support.
- An ARIA alternative for custom widgets is `role="group"` or `role="radiogroup"` with `aria-labelledby` (technique ARIA17). Prefer the native elements.

```html
<fieldset>
  <legend>Delivery method</legend>
  <input type="radio" id="ship-standard" name="ship" value="standard">
  <label for="ship-standard">Standard (3–5 days)</label>
  <input type="radio" id="ship-express" name="ship" value="express">
  <label for="ship-express">Express (next day)</label>
</fieldset>
```

## Instructions and format before the field

- **Requirement (3.3.2).** When the input has an expected format or allowed values, say so. Understanding 3.3.2 gives the example of a date format such as dd/mm/yyyy. It also warns that "too much information or instruction can be just as harmful as too little".
- **Technique.** Put the format and an example in text (G89). Instructions that apply to the whole form or a group go before it (G184). Connect an instruction to its field with `aria-describedby` (ARIA1) so it is read with the field.
- **Guidance.** Place the instruction before the field in reading order (between label and field, or in the label), not only after it or in a tooltip. Instructions must not rely only on shape, position or color, for example "the field on the right" or "the fields in red" (1.3.3 Sensory Characteristics, A, 2.0; see also 1.4.1).

```html
<label for="dob">Date of birth</label>
<p id="dob-hint">Use the format DD/MM/YYYY, for example 07/03/1990.</p>
<input id="dob" name="dob" type="text" inputmode="numeric" autocomplete="bday"
       aria-describedby="dob-hint">
```

## Required fields

- **Requirement.** Understanding 3.3.2 says the criterion "applies to all form fields, whether they're required or optional", and lists marking required controls in the label or legend (H90) among its techniques. If "required" is shown visually, it is also programmatically determinable (1.3.1).
- **Technique.** Put the word in the label ("Email (required)") or explain the symbol once before the form ("Fields marked * are required") (H90). For the programmatic state, use the HTML `required` attribute; ARIA in HTML says authors **should not** add `aria-required="true"` to an element that already has `required`. `aria-required="true"` is for custom widgets that are not native form controls (technique ARIA2, advisory).
- **Guidance.** An asterisk alone is a symbol many people misread; give it a text explanation or use the word. If most fields are required, marking the optional ones instead is a common design choice, as long as the convention is stated.
- `required` triggers the browser's native validation messages. If you replace them with your own (with `novalidate` on the form), your messages must meet 3.3.1 and 3.3.3 instead.

## Input purpose and autocomplete

Fields that collect information about the user (name, email, address, phone, birthday, payment details in the WCAG list of input purposes) need a programmatically determinable purpose: 1.3.5 Identify Input Purpose, AA, entered in 2.1. In HTML the sufficient technique is the `autocomplete` attribute with a valid token (H98). What is and is not in scope, and why `type="email"` is not the same thing: [form-labels-and-names.md](form-labels-and-names.md#4-input-purpose-135).

## When to validate

No success criterion says when to validate; these are **guidance** from the WAI Forms tutorial ("User Notifications"):

- **On submit** is the baseline: check everything, show the errors, keep what the user entered.
- **When the user leaves a field** suits fields with a required format, such as dates. The tutorial explains that checking while typing "would display error messages most of the time".
- **While typing** can help (password rules, character counts), but "not all situations may be appropriate". If you do it, do not announce a new error on every keystroke: let the message update quietly and avoid `role="alert"` or `aria-live="assertive"` for it.
- Do not disable the submit button until the form is valid: users then get no explanation of what is wrong. Let them submit and identify the errors. (This is guidance; a disabled button is not itself a WCAG failure.)
- Validate on the server too. Client-side checks are a convenience, not the only check.

## Identifying errors and suggesting fixes

- **Requirement (3.3.1, A).** When an input error is detected automatically, the item in error is identified and the error is described in text. Understanding 3.3.1 says "it is not sufficient to only re-display the form without providing any hint that the submission failed". A required field left empty is an input error.
- **Requirement (3.3.3, AA).** If the error is detected and a correction is known, suggest it ("Enter a date in the past", "Did you mean name@gmail.com?"), unless that would jeopardize security or the purpose of the content (for example a test answer or a password).
- **Requirement (1.4.1, 1.3.1, 4.1.2).** Do not show the error only with a red border: add text and, if useful, an icon. The message must be connected to its field, and the field's invalid state exposed.
- **Technique.** Text for an empty required field (G83), for a value outside the allowed list (G84) or format (G85), error text added to the page by script (SCR32). Set `aria-invalid="true"` on the field after validation and connect the message with `aria-describedby` (ARIA21). ARIA21 adds: do not set `aria-invalid="true"` before validation has run, and `aria-invalid="false"` is the same as leaving the attribute out.
- **Guidance.** Write each message so it says what is wrong and how to fix it, starting with the field name ("Email: enter an address like name@example.com"). Prefixing the message with "Error:" helps when the visual cue is not perceived.
- **When to use `role="alert"`.** Use it (or a live region) for an error that appears **without** a focus change, such as a message added when the user leaves a field. Do not put `role="alert"` on error text that is already in the page when it loads, and do not combine it with moving focus to the same message: the move already announces it, and both together may announce it twice (test with the screen readers you support). The existing fragment in [components.md](components.md#accessible-form-validation) shows the field markup (`aria-invalid`, `aria-describedby`).

## Error summary and focus

- **Technique (G139, advisory for 3.3.1 and 3.3.3).** After a failed submission, show a summary at the top of the form that says errors occurred, describes each one and links to each field, "so that the user does not have to search for it". The WAI Forms tutorial recommends listing errors "at the top of the page, before the form", and for a submission that reloads the page, putting the error count in the `<title>` (for example "3 errors – Billing address") and in the main heading.
- **Where focus goes (guidance).** G139 example 3 moves focus to the error message; the WAI tutorial instead sets focus on the first field with an error. Both are reasonable; choose one, apply it consistently and test it. Moving focus to the summary lets users hear how many errors there are before fixing them; it is the approach in the fragment below.
- **Requirement (2.4.3, A).** Whatever you choose, the focus order after the move must preserve meaning and operability.

The fragment below validates on submit, fills the summary with links, gives the summary focus and keeps each inline message tied to its field. It is a minimal example, not a validation library: server-side validation is still needed.

```html
<!-- Tested with keyboard in a Chromium browser (2026-11-15): empty, partly valid and valid
     submissions; focus moves to the summary and each link focuses its field; aria-invalid and
     aria-describedby checked by script, names in the accessibility tree. Not tested with a
     screen reader, Firefox or Safari. -->
<form id="signup" novalidate>
  <div id="error-summary" tabindex="-1" hidden aria-labelledby="error-summary-title">
    <h2 id="error-summary-title">There is a problem</h2>
    <ul id="error-list"></ul>
  </div>

  <p>All fields are required.</p>

  <label for="full-name">Full name</label>
  <input id="full-name" name="full-name" type="text" autocomplete="name" required>
  <p id="full-name-error" class="error" hidden></p>

  <label for="email">Email</label>
  <p id="email-hint">For example, name@example.com</p>
  <input id="email" name="email" type="email" autocomplete="email" required
         aria-describedby="email-hint">
  <p id="email-error" class="error" hidden></p>

  <button type="submit">Create account</button>
</form>

<script>
  const form = document.getElementById('signup');
  const summary = document.getElementById('error-summary');
  const list = document.getElementById('error-list');
  const rules = [
    { id: 'full-name', message: 'Enter your full name.',
      valid: (el) => el.value.trim() !== '' },
    { id: 'email', message: 'Enter an email address like name@example.com.',
      valid: (el) => el.value.trim() !== '' && el.validity.valid },
  ];

  form.addEventListener('submit', (event) => {
    list.replaceChildren();
    for (const rule of rules) {
      const field = document.getElementById(rule.id);
      const error = document.getElementById(`${rule.id}-error`);
      // Remember the field's own description (hint) once, before adding the error id.
      field.dataset.hint ??= field.getAttribute('aria-describedby') ?? '';
      const describedBy = [field.dataset.hint];

      if (rule.valid(field)) {
        error.hidden = true;
        error.textContent = '';
        field.removeAttribute('aria-invalid');
      } else {
        error.textContent = `Error: ${rule.message}`;
        error.hidden = false;
        field.setAttribute('aria-invalid', 'true');
        describedBy.push(error.id);

        const link = document.createElement('a');
        link.href = `#${rule.id}`;
        link.textContent = rule.message;
        link.addEventListener('click', (e) => {
          e.preventDefault();
          field.focus(); // move focus to the field, not only scroll to it
        });
        const item = document.createElement('li');
        item.append(link);
        list.append(item);
      }

      const ids = describedBy.join(' ').trim();
      if (ids) field.setAttribute('aria-describedby', ids);
      else field.removeAttribute('aria-describedby');
    }

    if (list.children.length > 0) {
      event.preventDefault();
      summary.hidden = false;
      summary.focus();
    } else {
      summary.hidden = true;
    }
  });
</script>
```

Notes on the fragment:
- The summary is a plain container that receives focus (`tabindex="-1"`), so it does not need `role="alert"` (see [When to use `role="alert"`](#identifying-errors-and-suggesting-fixes)).
- Error elements are referenced by `aria-describedby` only while they are shown: under Accessible Name and Description Computation 1.2 (step 2A), an element referenced directly by `aria-describedby` is used for the description even when it is hidden, so leaving the reference in place could describe a field with a stale error.
- The summary heading level (`h2`) depends on the page's outline.

## Preventing errors in legal, financial and data submissions

**Requirement (3.3.4 Error Prevention (Legal, Financial, Data), AA, 2.0).** For pages that cause legal commitments or financial transactions for the user, that modify or delete user-controllable data in data storage systems, or that submit test responses, at least one is true:

- **Reversible:** the submission can be undone (technique G164: a period in which the request can be amended or cancelled; G99: deleted information can be recovered).
- **Checked:** the input is checked for errors and the user can correct them.
- **Confirmed:** the user can review, confirm and correct the information before finalizing (G98: a review step; G155: a confirmation checkbox next to the submit button; G168: ask for confirmation before continuing).

Understanding 3.3.4 says it is "not the intent to require a confirmation for each save command".

## Redundant entry

**Requirement (3.3.7 Redundant Entry, A, new in 2.2).** Information previously entered by or provided to the user that is required again **in the same process** is either auto-populated or available to select. Exceptions: re-entering is essential, the information is required for security, or it is no longer valid.

- A "billing address same as delivery" checkbox, or a summary step that shows what was entered, are common ways to meet it.
- Understanding 3.3.7 says it "does not add a requirement to store information between sessions", and that a process can span domains (a third-party payment step in a checkout is in scope).
- Re-typing a password to confirm it is a security case. For password managers and paste in authentication, see 3.3.8 below.

## Multi-step forms

- **Guidance.** Show where the user is ("Step 2 of 4: Delivery") in text, not only as a colored progress bar (if the bar conveys information, 1.4.1 and 1.4.11 apply to it). Give each step a unique page title or main heading. Let users go back without losing what they entered.
- **Requirement.** Data already entered in the process must not have to be typed again (3.3.7, above). A final review step is one way to meet 3.3.4 when it applies.
- **Requirement (2.2.1 Timing Adjustable, A, 2.0).** If the session or the step has a time limit set by the content, the user can turn it off, adjust it to at least ten times the default, or is warned and given at least 20 seconds to extend it with a simple action, unless the limit is real-time, essential, or longer than 20 hours. Session techniques: G133 (offer a longer or no session limit on the first page of a multi-part form), G198 (turn the limit off); script techniques: SCR16 (warn before it expires) with SCR1 (allow extending it). For the cognitive side of time limits, see [alternative-input-and-cognitive.md](alternative-input-and-cognitive.md#cognitive-accessibility-coga-1).

## Changing a control must not change the context

**Requirement (3.2.2 On Input, A, 2.0).** Changing the setting of a control (choosing an option, ticking a box, typing in a field) does not automatically cause a change of context, unless the user was told about the behavior before using the control. A change of context is a major change such as opening a new window, moving focus, or navigating to another page; showing or hiding related fields in place is usually a change of content, not of context.

- Failures: F36 (submitting the form automatically when a field receives a value), F37 (opening a new window when a radio button, checkbox or select changes).
- Techniques: a submit button for the action (G80, H32, H84), or describing what will happen before the change (G13).
- **Guidance.** A `<select>` that navigates as soon as an option is chosen is the classic example to avoid; add a "Go" button.

## Authentication steps

Login, verification codes and password fields follow 3.3.8 Accessible Authentication (Minimum), AA, new in 2.2: allow paste and password managers, offer an alternative to cognitive function tests, and judge the whole process, not one field. Read [authentication-and-modal-focus.md](authentication-and-modal-focus.md#1-accessible-authentication).

## Sources

Consulted on 2026-11-15:

- WCAG 2.2 (W3C Recommendation, 12 December 2024): https://www.w3.org/TR/WCAG22/
- What's New in WCAG 2.1 (criteria added in 2.1): https://www.w3.org/WAI/standards-guidelines/wcag/new-in-21/
- Understanding 3.3.2 Labels or Instructions: https://www.w3.org/WAI/WCAG22/Understanding/labels-or-instructions.html
- Understanding 3.3.1 Error Identification: https://www.w3.org/WAI/WCAG22/Understanding/error-identification.html
- Understanding 3.3.4 Error Prevention (Legal, Financial, Data): https://www.w3.org/WAI/WCAG22/Understanding/error-prevention-legal-financial-data.html
- Understanding 3.3.7 Redundant Entry: https://www.w3.org/WAI/WCAG22/Understanding/redundant-entry.html
- Understanding 3.2.2 On Input: https://www.w3.org/WAI/WCAG22/Understanding/on-input.html
- Understanding 2.2.1 Timing Adjustable: https://www.w3.org/WAI/WCAG22/Understanding/timing-adjustable.html
- Technique G139 (jump to errors): https://www.w3.org/WAI/WCAG22/Techniques/general/G139
- Technique ARIA21 (`aria-invalid`): https://www.w3.org/WAI/WCAG22/Techniques/aria/ARIA21
- Technique H71 (`fieldset` and `legend`): https://www.w3.org/WAI/WCAG22/Techniques/html/H71
- WAI Forms tutorial, User Notifications: https://www.w3.org/WAI/tutorials/forms/notifications/
- ARIA in HTML (`aria-required` with `required`): https://www.w3.org/TR/html-aria/
- Accessible Name and Description Computation 1.2 (hidden nodes referenced by `aria-describedby`): https://www.w3.org/TR/accname-1.2/
