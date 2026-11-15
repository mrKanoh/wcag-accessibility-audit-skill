# AI assistants and chat interfaces

Read this when you build or review a chat or assistant interface: a conversation history, a message box, streamed responses, generated content, a floating chat widget. It is about making the **interface** accessible. Using AI tools to help write accessible code is a different topic: [inclusive-practice.md](inclusive-practice.md#ai-assisted-accessible-development).

**WCAG has no chat-specific success criteria, and the ARIA Authoring Practices Guide has no chat pattern** (its patterns index lists none; the closest are Feed and the `log` role). The requirements are the general WCAG 2.2 criteria listed below, applied to a chat. Everything else here is a technique (W3C) or guidance, labelled as such. Nothing fails WCAG for missing guidance. The default target is WCAG 2.2 AA ([legal-framework.md](legal-framework.md)).

## Contents

- [Criteria that apply](#criteria-that-apply)
- [Conversation history](#conversation-history)
- [Message input and sending](#message-input-and-sending)
- [Focus after sending](#focus-after-sending)
- [Streamed responses](#streamed-responses)
- [Structure of generated content](#structure-of-generated-content)
- [Errors, retries and time limits](#errors-retries-and-time-limits)
- [Attachments and voice input](#attachments-and-voice-input)
- [Panel layout: contrast, reflow and target size](#panel-layout-contrast-reflow-and-target-size)
- [Floating chat widgets](#floating-chat-widgets)
- [Risks of generated content](#risks-of-generated-content)
- [Minimal example](#minimal-example)
- [Review checklist](#review-checklist)
- [Sources](#sources)

## Criteria that apply

| ID | Name | Level | Entered | Where it applies in a chat |
|----|------|-------|---------|----------------------------|
| 1.1.1 | Non-text Content | A | 2.0 | Images in replies, icon buttons, avatars that convey who is speaking |
| 1.3.1 | Info and Relationships | A | 2.0 | Who wrote each message; headings, lists, tables and code in replies |
| 1.4.3 / 1.4.11 | Contrast (Minimum) / Non-text Contrast | AA | 2.0 / 2.1 | Message text and bubbles, input border, icon buttons, focus indicator |
| 1.4.10 | Reflow | AA | 2.1 | The panel at 320 CSS px width / 400% zoom |
| 2.1.1 | Keyboard | A | 2.0 | Sending, stopping, copying, opening and closing the widget |
| 2.1.4 | Character Key Shortcuts | A | 2.1 | Single printable-key shortcuts (if any) can be turned off, remapped, or work only on focus |
| 2.2.1 | Timing Adjustable | A | 2.0 | Session timeouts, auto-closing chats |
| 2.4.3 | Focus Order | A | 2.0 | Where focus goes after sending, opening, closing |
| 2.4.4 | Link Purpose (In Context) | A | 2.0 | Links in generated replies |
| 2.4.11 | Focus Not Obscured (Minimum) | AA | 2.2 | A floating widget or launcher covering the focused element |
| 2.5.8 | Target Size (Minimum) | AA | 2.2 | Send, stop, copy, close and launcher buttons |
| 3.2.6 | Consistent Help | A | 2.2 | A chatbot repeated across pages is a help mechanism: same relative order |
| 3.3.1 / 3.3.2 | Error Identification / Labels or Instructions | A | 2.0 | Input errors (empty, too long, bad attachment); the message box label |
| 4.1.2 | Name, Role, Value | A | 2.0 | Icon-only buttons (send, stop, copy, attach, microphone) |
| 4.1.3 | Status Messages | AA | 2.1 | "Responding…", "Copied", "Response complete", errors |

## Conversation history

- **Requirement (1.3.1).** Who wrote each message must be programmatically determinable, not only shown by bubble color, side or avatar (1.4.1 Use of Color also applies if color alone separates the authors). A heading or visually hidden text per message ("You", "Assistant") does this and lets screen reader users jump between messages with heading navigation. An ordered list of messages adds a count and position.
- **Technique (ARIA23, `role="log"`).** ARIA23 uses `role="log"` for a chat history so that new messages are announced without moving focus; `log` is a polite live region in which only the added content is announced. Its limits in a chat with streamed replies:
  - every text node added to the log is a change; text streamed into a message inside the log can be announced piece by piece, which is the behavior to avoid ([Streamed responses](#streamed-responses));
  - the user's own message can be announced back to them as it is added;
  - very long replies are read in full with no structure.
  So either add each message to a `log` only once it is complete, or keep the history as a non-live list and announce through a separate status region, as in the [minimal example](#minimal-example). Test the choice with the screen readers you support.
- **Guidance.** Keep earlier messages in the page (do not replace the history); give the history a label ("Conversation"); timestamps as text if they matter.

## Message input and sending

- **Requirement (3.3.2, 4.1.2, 2.5.3).** The message box has a label (a visible label is the guidance; a placeholder alone is weak, see [form-labels-and-names.md](form-labels-and-names.md#2-label-versus-accessible-name)). Icon-only buttons (send, attach, microphone) have accessible names.
- **Requirement (2.1.1).** Sending must work with the keyboard. Enter to send and Shift+Enter for a new line is a common convention. **Guidance:** state the convention near the box (and connect it with `aria-describedby`), keep a visible Send button, and do not send while an input method editor is composing text (`event.isComposing`).
- **Requirement (2.1.4 Character Key Shortcuts, A, 2.1).** If the chat adds shortcuts made only of printable characters (letters, numbers, punctuation, symbols), they can be turned off, remapped to include a non-printable key, or are active only when their component has focus. Enter is not a printable character, so Enter-to-send is outside 2.1.4.
- **Guidance.** Use a `<textarea>` that grows, not a single-line input, when messages can be long. Do not clear the user's text if sending fails.

## Focus after sending

- **Guidance.** Keep focus in the message box after sending, so the user can type the next message. Do not move focus to the new reply automatically: the user may still be typing, and the reply is announced through a status message instead.
- **Requirement (2.4.3).** When a control that has focus disappears (a Stop button hidden when the reply ends, a widget that closes), move focus somewhere logical (the message box, the launcher) instead of letting it fall to the page body.

## Streamed responses

Replies that appear token by token are the main chat-specific barrier.

- **Guidance.** Do not put the streaming text inside an active live region: it can be read in fragments or over and over. Instead:
  1. When the request starts, set a status message: "Assistant is responding…" (`role="status"`, 4.1.3).
  2. Stream the text visually into an element that is not a live region.
  3. When the reply is complete, announce it once: either "Assistant replied" (the user reads it with heading navigation) or the full text of a short reply. Announcing paragraph by paragraph is a middle option for long replies. Which works best depends on reply length and users: test with them.
  4. Offer a **Stop** button while generating, with an accessible name, reachable by keyboard; announce "Response stopped".
- `aria-busy="true"` on the streaming message is not a reliable way to silence it: ARIA 1.2 only says assistive technologies *may* ignore changes while it is set ([dynamic-content.md](dynamic-content.md#loading-states-and-skeletons)).
- **2.2.2 Pause, Stop, Hide.** A reply that streams after the user presses Send is the "direct result of a user's intentional activation", which Understanding 2.2.2 does not count as starting automatically, so 2.2.2 is generally not what requires the Stop button. Content that updates on its own (for example a live agent typing indicator that loops, or auto-scrolling) can fall under 2.2.2. The Stop button is guidance that helps everyone.
- **Guidance.** Do not auto-scroll the history while the user is reading earlier messages; offer a "Jump to latest" button instead.

## Structure of generated content

- **Requirement (1.3.1).** Render Markdown or rich output to semantic HTML: real headings, lists, tables with header cells, `<code>`/`<pre>` for code, `<a>` for links. Do not show raw Markdown symbols or fake structure with bold text only. Heading levels inside a reply should fit under the message's own heading. Tables follow [content.md](content.md#lists-and-data-tables).
- **Requirement (4.1.2, 2.5.3).** A "Copy" button per code block has an accessible name that starts with its visible text and says what it copies when there are several ("Copy code", "Copy code: Python example"). Confirm the copy with a status message ("Copied").
- **Requirement (1.4.10).** Long code lines may scroll inside their block (two-dimensional exception); prose in the reply must wrap ([reflow-zoom-and-text-spacing.md](reflow-zoom-and-text-spacing.md#content-allowed-to-scroll-in-two-dimensions)).
- **Requirement (3.1.2, AA).** A reply in another language than the page should carry `lang` when the language is known ([content.md](content.md#language-of-the-page-and-of-parts)).

## Errors, retries and time limits

- **Requirement (3.3.1).** An input error (empty message, text too long, unsupported attachment) is identified in text and connected to the input ([forms.md](forms.md#identifying-errors-and-suggesting-fixes)).
- **Requirement (4.1.3).** A failed reply or a lost connection is a status message: show it in text in the conversation and announce it (`role="status"`, or `role="alert"` when the user must act now). Provide a Retry button with an accessible name; keep the user's message.
- **Requirement (2.2.1).** If the chat session expires or the widget closes after inactivity, the user can turn the limit off, adjust it, or is warned and can extend it with at least 20 seconds to respond ([dynamic-content.md](dynamic-content.md#time-limits)).

## Attachments and voice input

- **Requirement (3.3.2, 4.1.2).** The attach control has an accessible name; accepted types and size limits are stated before the user chooses a file (3.3.2); attached files are listed in text with a named remove button.
- **Requirement (2.5.7, AA, 2.2).** If files can be dropped onto the chat, a button to pick files is also available (dragging alternative).
- **Guidance.** Voice input is an option, not the only way to send: keep the text box. The microphone button has a name and shows and announces its state (listening, stopped).

## Panel layout: contrast, reflow and target size

- **Requirements.** Message text 4.5:1 (1.4.3); bubble borders when they are the only way to identify a message, the input border, and icon buttons 3:1 (1.4.11); the panel reflows at 320 CSS px and works at 200% text (1.4.10, 1.4.4); send, stop, copy and close targets at least 24 × 24 CSS px or meeting an exception (2.5.8). Detail: [design-phase.md](design-phase.md#target-size) and [reflow-zoom-and-text-spacing.md](reflow-zoom-and-text-spacing.md).

## Floating chat widgets

- **Requirement (2.4.11 Focus Not Obscured (Minimum), AA, new in 2.2).** A floating launcher or open chat panel must not entirely hide the element that has keyboard focus on the page. Understanding 2.4.11 names non-modal dialogs and sticky content as typical causes. At high zoom a fixed panel can cover most of the screen ([reflow-zoom-and-text-spacing.md](reflow-zoom-and-text-spacing.md#sticky-and-fixed-content-when-zoomed)).
- **Guidance.** Decide whether the open panel is modal or not. If it is modal, trap focus and return it to the launcher on close ([authentication-and-modal-focus.md](authentication-and-modal-focus.md#2-initial-focus-and-focus-return-in-modal-dialogs)). If it is non-modal, put it in the reading order next to the launcher, move focus into it on open, and let users close it with a button and Escape.
- **Requirement (3.2.6 Consistent Help, A, new in 2.2).** Understanding 3.2.6 lists "a fully automated contact mechanism such as a chatbot" as a help mechanism; if it repeats across pages, keep it in the same order relative to other content. Understanding 3.2.6 also gives chatbot guidance for people with cognitive disabilities: recognize misspellings, offer human contact details if it cannot resolve the question after three attempts, be dismissible in one interaction and recallable through a link or button (guidance, not part of the normative text).
- **Guidance.** Do not open the widget automatically or play a sound on page load.

## Risks of generated content

Generated text is content published on the page, and the same criteria apply to it:

- **Alternative text (1.1.1).** Images or alt text generated by a model must be reviewed by a person before they are presented as reliable descriptions; mark generated descriptions as such when they are not reviewed. [Content: text alternatives](content.md#text-alternatives-for-images).
- **Links (2.4.4).** Generated replies often produce "click here" or bare URLs. Instruct the model and post-process output so link text describes the destination.
- **Structure (1.3.1).** Bold lines used as headings, or tables rendered as text, lose their structure; render real elements.
- **Language (3.1.2) and plain language (guidance).** Ask for the user's language and a plain register; 3.1.5 Reading Level is AAA.

## Minimal example

A history as a non-live list with an author heading per message, a polite status region for "responding / replied / stopped / failed", Enter to send, Shift+Enter for a new line, focus kept in the box, and a Stop button. `streamReply` is a stand-in for a real streaming API. To stay short, the example omits the Retry button and does not restore the user's text when a reply fails; a real chat should do both ([Errors, retries and time limits](#errors-retries-and-time-limits)).

```html
<!-- Tested with keyboard in a Chromium browser (2026-11-15): Enter sends, Shift+Enter adds a line,
     focus stays in the textarea, Stop aborts and returns focus to the textarea; status text and
     names checked by script and in the accessibility tree. Not tested with a screen reader,
     Firefox or Safari. -->
<section aria-labelledby="chat-title">
  <h2 id="chat-title">Help assistant</h2>
  <ol id="messages" aria-label="Conversation"></ol>
  <div id="chat-status" role="status" class="visually-hidden"></div>

  <form id="chat-form">
    <label for="chat-input">Message</label>
    <textarea id="chat-input" rows="2" aria-describedby="chat-help"></textarea>
    <p id="chat-help">Enter sends. Shift+Enter adds a new line.</p>
    <button type="submit">Send</button>
    <button type="button" id="stop" hidden>Stop generating</button>
  </form>
</section>

<script>
  const form = document.getElementById('chat-form');
  const input = document.getElementById('chat-input');
  const list = document.getElementById('messages');
  const status = document.getElementById('chat-status');
  const stop = document.getElementById('stop');
  let controller = null;

  function addMessage(author, text) {
    const item = document.createElement('li');
    const heading = document.createElement('h3');
    heading.textContent = author;
    const body = document.createElement('div');
    body.textContent = text;
    item.append(heading, body);
    list.append(item);
    return body;
  }

  input.addEventListener('keydown', (event) => {
    if (event.key === 'Enter' && !event.shiftKey && !event.isComposing) {
      event.preventDefault();
      form.requestSubmit();
    }
  });

  form.addEventListener('submit', async (event) => {
    event.preventDefault();
    const text = input.value.trim();
    if (!text || controller) return;
    addMessage('You', text);
    input.value = '';                          // focus stays in the textarea
    const reply = addMessage('Assistant', '');
    status.textContent = 'Assistant is responding…';
    stop.hidden = false;
    controller = new AbortController();
    try {
      for await (const chunk of streamReply(text, controller.signal)) {
        reply.textContent += chunk;            // visual only: not a live region
      }
      status.textContent = 'Assistant replied.';
    } catch (error) {
      if (error.name === 'AbortError') {
        if (!reply.textContent) reply.textContent = '(Response stopped.)';
        status.textContent = 'Response stopped.';
      } else {
        reply.textContent = 'The reply failed. Send your message again to retry.';
        status.textContent = 'Error: the reply failed.';
      }
    } finally {
      controller = null;
      if (document.activeElement === stop) input.focus(); // do not lose focus when Stop hides
      stop.hidden = true;
    }
  });

  stop.addEventListener('click', () => controller?.abort());

  // Stand-in for a real streaming API: yields words with a delay and honors abort.
  async function* streamReply(prompt, signal) {
    const words = `You asked: "${prompt}". This is a simulated reply.`.split(' ');
    for (const word of words) {
      await new Promise((resolve, reject) => {
        const timer = setTimeout(resolve, 150);
        signal.addEventListener('abort', () => {
          clearTimeout(timer);
          reject(new DOMException('Aborted', 'AbortError'));
        }, { once: true });
      });
      yield `${word} `;
    }
  }
</script>
```

## Review checklist

| Check | Basis |
|-------|-------|
| Each message's author is in text or markup, not only color or position | 1.3.1 A; 1.4.1 A |
| The message box has a label; icon buttons have names | 3.3.2 A; 4.1.2 A |
| Sending, stopping, copying, opening and closing work with the keyboard | 2.1.1 A |
| Single printable-key shortcuts can be turned off, remapped or are focus-only | 2.1.4 A |
| Focus stays in the box after sending and is not lost when controls disappear | Guidance; 2.4.3 A |
| "Responding", "replied", "stopped", "copied" and errors are status messages | 4.1.3 AA |
| Streaming text is not read token by token | Guidance (test with AT) |
| Replies render real headings, lists, tables, code and links | 1.3.1 A; 2.4.4 A |
| Copy buttons have names that include their visible text | 4.1.2 A; 2.5.3 A |
| Panel reflows at 320 CSS px; text and controls contrast | 1.4.10 AA; 1.4.3 AA; 1.4.11 AA |
| Targets at least 24 × 24 CSS px or meet an exception | 2.5.8 AA (2.2) |
| A floating widget never entirely covers the focused element | 2.4.11 AA (2.2) |
| A chatbot on many pages stays in the same relative order | 3.2.6 A (2.2) |
| Time limits can be turned off, adjusted or extended | 2.2.1 A |
| Drag-and-drop attachments have a file-picker button | 2.5.7 AA (2.2) |
| Generated alt text is reviewed before it is presented as reliable | 1.1.1 A; guidance |

## Sources

Consulted on 2026-11-15:

- WCAG 2.2 (W3C Recommendation, 12 December 2024): https://www.w3.org/TR/WCAG22/
- What's New in WCAG 2.1: https://www.w3.org/WAI/standards-guidelines/wcag/new-in-21/
- What's New in WCAG 2.2: https://www.w3.org/WAI/standards-guidelines/wcag/new-in-22/
- Technique ARIA23 (`role="log"`, chat example): https://www.w3.org/WAI/WCAG22/Techniques/aria/ARIA23
- Understanding 4.1.3 Status Messages: https://www.w3.org/WAI/WCAG22/Understanding/status-messages.html
- Understanding 2.2.2 Pause, Stop, Hide: https://www.w3.org/WAI/WCAG22/Understanding/pause-stop-hide.html
- Understanding 2.1.4 Character Key Shortcuts: https://www.w3.org/WAI/WCAG22/Understanding/character-key-shortcuts.html
- Understanding 2.4.11 Focus Not Obscured (Minimum): https://www.w3.org/WAI/WCAG22/Understanding/focus-not-obscured-minimum.html
- Understanding 3.2.6 Consistent Help: https://www.w3.org/WAI/WCAG22/Understanding/consistent-help.html
- WAI-ARIA 1.2 (`log`, `status`, `aria-busy`): https://www.w3.org/TR/wai-aria-1.2/
- ARIA APG, patterns index (no chat pattern): https://www.w3.org/WAI/ARIA/apg/patterns/
