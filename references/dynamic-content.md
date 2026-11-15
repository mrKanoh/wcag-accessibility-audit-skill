# Dynamic content: status messages, live regions, route changes and timing

Read this when content changes without a page load: status and error messages, notifications, search results that update, single-page app navigation, loading states, infinite scroll and "load more", content that is inserted or removed, content that updates itself, and time limits.

Each item says whether it is a **requirement** (a WCAG 2.2 success criterion, with ID, level and the version it entered), a **technique** (a W3C technique, a WAI-ARIA definition or an APG pattern) or **guidance**. Nothing fails WCAG for missing guidance. The default target is WCAG 2.2 AA ([legal-framework.md](legal-framework.md)).

**Live region behavior varies between screen readers, browsers and versions.** The ARIA specification says what assistive technologies *should* or *may* do, not what each one does. Test every announcement with the screen reader and browser pairs you support ([testing-and-screen-readers.md](testing-and-screen-readers.md#screen-reader-testing)); do not state that something "is announced" without having tested it.

## Contents

- [Criteria that apply](#criteria-that-apply)
- [Status messages (4.1.3)](#status-messages-413)
- [Live region roles and attributes](#live-region-roles-and-attributes)
- [The region must exist before its content changes](#the-region-must-exist-before-its-content-changes)
- [Route changes in single-page apps](#route-changes-in-single-page-apps)
- [Loading states and skeletons](#loading-states-and-skeletons)
- [Infinite scroll, pagination and "load more"](#infinite-scroll-pagination-and-load-more)
- [Inserting and removing content: where focus goes](#inserting-and-removing-content-where-focus-goes)
- [Notifications and toasts](#notifications-and-toasts)
- [Content that updates itself](#content-that-updates-itself)
- [Time limits](#time-limits)
- [Changes of context](#changes-of-context)
- [Sources](#sources)

## Criteria that apply

| ID | Name | Level | Entered | What it asks |
|----|------|-------|---------|--------------|
| 2.1.1 | Keyboard | A | 2.0 | All functionality operable by keyboard, including content loaded later |
| 2.2.1 | Timing Adjustable | A | 2.0 | Time limits set by the content can be turned off, adjusted or extended (with exceptions) |
| 2.2.2 | Pause, Stop, Hide | A | 2.0 | Moving, blinking, scrolling or auto-updating information can be paused, stopped or hidden (with conditions) |
| 2.4.2 | Page Titled | A | 2.0 | The title describes the current page or view |
| 2.4.3 | Focus Order | A | 2.0 | Focus order preserves meaning and operability |
| 3.2.1 | On Focus | A | 2.0 | Receiving focus does not initiate a change of context |
| 3.2.2 | On Input | A | 2.0 | Changing a setting does not automatically change the context unless the user was told |
| 4.1.3 | Status Messages | AA | 2.1 | Status messages can be programmatically determined through role or properties, so they can be presented without receiving focus |

## Status messages (4.1.3)

- **Requirement (4.1.3 Status Messages, AA, 2.1).** In content implemented with markup languages, status messages can be programmatically determined through role or properties such that they can be presented to the user by assistive technologies without receiving focus.
- **Definition.** A status message is a "change in content that is not a change of context" that gives information on the success or results of an action, the waiting state of an application, the progress of a process, or the existence of errors.
- **Examples from Understanding 4.1.3:** "18 results returned" after a search, "5 items" in a cart after adding a product, "Your form was successfully submitted", "5 errors on page", intermittent progress updates.
- **Not status messages.** Content that takes focus, such as a dialog, is a change of context, not a status message ("the dialog takes focus"). The list of search results itself is not the status message; the short text about the results is.
- **Techniques.** `role="status"` (ARIA22), with success feedback (G199); `role="alert"` or a live region for errors (ARIA19); `role="log"` for sequential updates (ARIA23); a live region for a progress bar (ARIA25).
- **Failures.** F103: status messages that cannot be programmatically determined through role or properties. Understanding 4.1.3 also lists as a failure using `role="alert"` or `aria-live="assertive"` on content that is not important and time-sensitive.
- What a code fragment does not contain is not proof that the page lacks a status message: [form-labels-and-names.md](form-labels-and-names.md#behavior-shown-described-possible-observed).

## Live region roles and attributes

Definitions from WAI-ARIA 1.2:

| Role or attribute | Definition (WAI-ARIA 1.2) | Implicit values | Use for |
|-------------------|---------------------------|-----------------|---------|
| `role="status"` | "advisory information for the user but is not important enough to justify an alert" | `aria-live="polite"`, `aria-atomic="true"` | Results counts, "Saved", "Copied", progress text |
| `role="alert"` | "important, and usually time-sensitive, information" | `aria-live="assertive"`, `aria-atomic="true"` | Errors and warnings that need attention now |
| `role="log"` | "new information is added in meaningful order and old information may disappear" | `aria-live="polite"` | Chat history, activity logs (ARIA23 says only the added content is announced) |
| `aria-live="polite"` | updates presented "at the next graceful opportunity" | — | A custom region when no role fits |
| `aria-live="assertive"` | updates "have the highest priority"; assistive technologies "could potentially clear the speech queue of previous updates" | — | Rarely: "Authors SHOULD NOT use the assertive value unless the interruption is imperative" |
| `aria-live="off"` (default) | updates not presented "unless the user is currently focused on that region" | — | Regions that should stay quiet |
| `aria-atomic` | whether assistive technologies "present all, or only parts of, the changed region"; default `false` (only the changed nodes) | — | `true` when the whole message must be read together |
| `aria-busy` | when `true`, assistive technologies "MAY ignore changes to content owned by that element"; default `false` | — | Batching several DOM changes into one update |

- **`alert` does not need focus.** ARIA 1.2: neither authors nor user agents are required to manage focus to an alert, and "authors SHOULD NOT require users to close an alert". The APG Alert pattern adds that alerts "do not affect keyboard focus", that designers should avoid alerts "that disappear automatically", and should limit their frequency.
- **Do not overuse `assertive` or `alert`.** It interrupts whatever the user is doing. Reserve it for errors and time-critical warnings; use `status` for everything else.
- **Prefer the roles** over bare `aria-live` when one fits: the role says what the content is.
- ARIA22 advises an explicit `aria-atomic="true"` on a status container "if the entire contents of the container should be announced", even though it is the implicit value.

## The region must exist before its content changes

- **Technique (ARIA22 test procedure).** "Check that the container destined to hold the status message has a `role` attribute with a value of `status`" and that "when the status message is triggered, it is inside the container". In practice: render the empty region with the page, then change its text.
- **Caution (APG Alert).** "screen readers do not inform users of alerts that are present on the page before page load completes". A message already in the markup when the page loads, or a region inserted in the same moment as its text, may not be announced. Neither ARIA22 nor Understanding 4.1.3 states a rule for inserting a region together with its content, so treat it as unreliable and test it.
- **Guidance.** Keep one polite and, if needed, one assertive region per page, shared by components, rather than many regions. Clearing the region before writing the same message again lets a repeated message be noticed as a change; whether it is announced again depends on the screen reader.

```html
<!-- Not tested with a screen reader: announcement timing varies between screen readers and browsers. -->
<div id="status" role="status" class="visually-hidden"></div>  <!-- present at page load, empty -->

<script>
  function announce(message) {
    const region = document.getElementById('status');
    region.textContent = '';                        // clear first, so a repeated message is a change
    setTimeout(() => { region.textContent = message; }, 100);
  }
  // announce('18 results returned');
</script>
```

The `visually-hidden` class is the usual clip pattern (content readable by assistive technology, not shown). Show the message visually too when sighted users also need it.

## Route changes in single-page apps

When a client-side route change replaces the view without a page load:

- **Requirement (2.4.2, A).** Understanding 2.4.2: "the title of the page should also be changed dynamically to reflect the content or topic of the current view."
- **Requirement (2.4.3, A).** Focus must not be left on a control that no longer exists or at the top of a stale view in a way that breaks meaning or operation.
- **Guidance.** Either announce the new view (title or main heading) in a live region, or move focus to the main heading (`tabindex="-1"`), or both, and test that the result is not too verbose. Some frameworks already ship an announcer: do not add a second one for the same announcement. Next.js example, and the focus-on-route-change component: [framework-examples.md](framework-examples.md#nextjs-app-router--focus-management-on-navigation); a Vue live region: [framework-examples.md](framework-examples.md#live-region-vue-3).

## Loading states and skeletons

- **Guidance.** Announce the start of a long load and its end in a status region ("Loading results…", "18 results returned"), not every intermediate step. Give skeleton placeholders no text content for assistive technology (for example `aria-hidden="true"` on the skeleton), so users do not hear empty shapes.
- **`aria-busy`.** ARIA 1.2 says assistive technologies *may* ignore changes while it is `true`; it is not a promise that anything is announced or withheld. The APG Feed pattern uses `aria-busy="true"` while articles are added in several DOM operations and stresses that "it is extremely important that `aria-busy` is set to `false` when the operation is complete", or the changes may not become visible to some assistive technology users. Support may differ between screen readers: do not rely on `aria-busy` alone to announce loading, and test it.
- A loading indicator that animates for more than five seconds alongside other content is moving content under 2.2.2 (see [below](#content-that-updates-itself)).

## Infinite scroll, pagination and "load more"

No success criterion prefers one pattern; these are **guidance**, with the requirements they touch:

- **Pagination** gives stable positions, a way back and a reachable footer. It is the simplest option to make accessible.
- **"Load more" button.** After loading, move focus to the first new item (or keep it on the button and announce how many items were added in a status region). Do not leave focus on a button that disappears (2.4.3).
- **Infinite scroll.** Content that keeps loading as the user scrolls can make the footer and the links after the list unreachable by keyboard (2.1.1 if functionality there cannot be reached). Offer a way to stop loading or a "load more" alternative, and announce new content politely. The APG [Feed pattern](https://www.w3.org/WAI/ARIA/apg/patterns/feed/) defines `role="feed"` with `role="article"` items, `aria-setsize`/`aria-posinset`, and suggested keys (Page Down/Page Up between articles, Ctrl+End to leave the feed); the APG says these keys are not an established convention, so document them.

## Inserting and removing content: where focus goes

- **Requirement (2.4.3 Focus Order, A).** After content is inserted or removed, focus order must still preserve meaning and operability.
- **Guidance.**
  - Removing the focused item (delete a row, dismiss a card): move focus to a logical neighbor (the next item, the previous one, or the list's heading) and confirm the action in a status region ("Report.pdf deleted").
  - Expanding content in place (disclosure, "show more"): keep focus on the control; the new content follows it in reading order.
  - Inserting a message the user must act on now: if it is a dialog, it takes focus (a change of context, see [authentication-and-modal-focus.md](authentication-and-modal-focus.md#2-initial-focus-and-focus-return-in-modal-dialogs)); otherwise use a live region and do not move focus.
- How to report focus behavior known only from code or a comment: [form-labels-and-names.md](form-labels-and-names.md#behavior-shown-described-possible-observed).

## Notifications and toasts

- A toast is a status message (4.1.3): use a polite region for confirmations and `role="alert"` only for errors.
- **Requirement (2.2.1, A).** A toast that disappears on a timer is a time limit set by the content. Errors and messages that ask for action should stay until dismissed; the APG Alert pattern advises avoiding alerts that disappear automatically.
- Every toast that stays needs a dismiss control with an accessible name; a toast must not take focus.
- Worked example with polite and assertive regions, dismiss buttons, pause on hover and focus, and reduced motion: `examples/components/toast-notifications.html` (described in [templates-prompts-and-resources.md](templates-prompts-and-resources.md#accessible-component-examples-examplescomponents)).

## Content that updates itself

- **Requirement (2.2.2 Pause, Stop, Hide, A, 2.0).** For moving, blinking or scrolling information that starts automatically, lasts more than five seconds and is shown in parallel with other content, there is a mechanism to pause, stop or hide it. For auto-updating information (content that "updates or disappears based on a preset time interval", such as news, weather or stock prices) there is a mechanism to pause, stop, hide or control the frequency, and Understanding 2.2.2 says "there is no five second exception for auto-updating". Exception: the movement or updating is essential.
- Understanding 2.2.2: "starts automatically" means updates that are "not the direct result of a user's intentional activation" such as selecting a link or button; content started by focusing, hovering or scrolling it into view does start automatically.
- Techniques: G186 (a control to stop moving, blinking or auto-updating content), G4 (pause and restart from the same point), SCR33 (scripted scrolling with a pause mechanism).
- **Guidance.** A live region that announces every automatic update (a ticker, a live score) can make a page unusable with a screen reader; announce on request or summarize, and let the user pause.

## Time limits

**Requirement (2.2.1 Timing Adjustable, A, 2.0).** For each time limit set by the content, at least one is true: the user can turn it off before encountering it; adjust it over a range at least ten times the default; or is warned before it expires and given at least 20 seconds to extend it with a simple action (at least ten times). Exceptions: real-time events where the limit is required, limits that are essential, and limits longer than 20 hours.

- Session timeouts, timed toasts, auto-advancing steps and quizzes are all time limits.
- Techniques: G133 and G198 for sessions, G180, SCR16 with SCR1 for scripted limits ([forms.md](forms.md#multi-step-forms) for multi-step forms).
- The warning itself is a message that needs attention: an `alertdialog` that takes focus, or a `role="alert"` message with a button to extend.
- Cognitive side of time limits: [alternative-input-and-cognitive.md](alternative-input-and-cognitive.md#cognitive-accessibility-coga-1).

## Changes of context

- **Requirement (3.2.1 On Focus, A, 2.0).** When a component receives focus, it does not initiate a change of context (submitting a form, opening a window, moving focus elsewhere). F55: using script to remove focus when it is received.
- **Requirement (3.2.2 On Input, A, 2.0).** Changing a control's setting does not automatically cause a change of context unless the user was told before: [forms.md](forms.md#changing-a-control-must-not-change-the-context).
- Dynamic updates that only change content (filtering a list, expanding a section) are changes of content, not of context; they may need a status message (4.1.3) instead.

## Sources

Consulted on 2026-11-15:

- WCAG 2.2 (W3C Recommendation, 12 December 2024): https://www.w3.org/TR/WCAG22/
- What's New in WCAG 2.1: https://www.w3.org/WAI/standards-guidelines/wcag/new-in-21/
- Understanding 4.1.3 Status Messages: https://www.w3.org/WAI/WCAG22/Understanding/status-messages.html
- Understanding 2.2.2 Pause, Stop, Hide: https://www.w3.org/WAI/WCAG22/Understanding/pause-stop-hide.html
- Understanding 2.2.1 Timing Adjustable: https://www.w3.org/WAI/WCAG22/Understanding/timing-adjustable.html
- Understanding 3.2.1 On Focus: https://www.w3.org/WAI/WCAG22/Understanding/on-focus.html
- Understanding 2.4.2 Page Titled: https://www.w3.org/WAI/WCAG22/Understanding/page-titled.html
- Technique ARIA22 (`role="status"`): https://www.w3.org/WAI/WCAG22/Techniques/aria/ARIA22
- Technique ARIA23 (`role="log"`): https://www.w3.org/WAI/WCAG22/Techniques/aria/ARIA23
- WAI-ARIA 1.2 (roles `alert`, `log`, `status`; `aria-live`, `aria-atomic`, `aria-busy`): https://www.w3.org/TR/wai-aria-1.2/
- ARIA APG, Alert pattern: https://www.w3.org/WAI/ARIA/apg/patterns/alert/
- ARIA APG, Feed pattern: https://www.w3.org/WAI/ARIA/apg/patterns/feed/
- ARIA APG, patterns index: https://www.w3.org/WAI/ARIA/apg/patterns/
