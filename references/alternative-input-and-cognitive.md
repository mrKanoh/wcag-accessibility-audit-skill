# Alternative input and cognitive accessibility

Input methods beyond keyboard and mouse (switch, voice, eye tracking, head pointer, dictation) and cognitive accessibility (COGA) patterns, including accessible authentication.

## Contents

- [Alternative Input Methods](#alternative-input-methods)
  - [Switch Access (1–2 buttons)](#switch-access-12-buttons)
  - [Voice Control / Dragon NaturallySpeaking](#voice-control--dragon-naturallyspeaking)
  - [Eye Tracking (Tobii, Eyegaze)](#eye-tracking-tobii-eyegaze)
  - [Head Pointer / Mouth Stick](#head-pointer--mouth-stick)
  - [Dictation (macOS built-in, Google Docs Voice Typing)](#dictation-macos-built-in-google-docs-voice-typing)
  - [Cognitive accessibility (COGA)](#cognitive-accessibility-coga)
- [Cognitive Accessibility (COGA)](#cognitive-accessibility-coga-1)
  - [Top 10 COGA design patterns](#top-10-coga-design-patterns)
  - [Accessible authentication (WCAG 3.3.8 — WCAG 2.2)](#accessible-authentication-wcag-338--wcag-22)

---

## Alternative Input Methods

Users with motor disabilities may use input methods beyond keyboard and mouse. Design and test for all of them.

### Switch Access (1–2 buttons)

- iOS: Settings → Accessibility → Switch Control
- Android: Settings → Accessibility → Switch Access
- Behavior: single-switch or two-switch scanning through focusable elements
- **Requirements**: logical focus order; no time-limited actions; adequate target size

**Test yourself**: enable Switch Control (iOS) or Switch Access (Android) with a Bluetooth keyboard spacebar as the switch.

### Voice Control / Dragon NaturallySpeaking

- iOS: Settings → Accessibility → Voice Control
- Android: Voice Access app (Google)
- Windows: Dragon NaturallySpeaking, Windows Voice Access
- Users say element names or grid coordinates to activate elements

**Requirements**:
- Visible label text must match (or be contained in) the accessible name — WCAG 2.5.3 Label in Name
- Prefer labels that tell repeated controls apart when their context does not (for example several "Learn more" links); this is a usability recommendation for voice control, not a WCAG uniqueness requirement (see `references/form-labels-and-names.md`)
- `aria-label` must contain the visible text, not replace it

```html
<!-- ❌ Label in Name failure: aria-label replaces visible text -->
<button aria-label="Course details">Learn more</button>

<!-- ✅ aria-label extends visible text -->
<button aria-label="Learn more about HTML Semántico">Learn more</button>
```

### Eye Tracking (Tobii, Eyegaze)

- Users dwell on elements to activate them; no keyboard or pointer precision
- **Requirements**: large targets (44×44pt minimum), no hover-only UI, no time-limited interactions, minimal cognitive load

### Head Pointer / Mouth Stick

- Like mouse but reduced precision
- **Requirements**: adequate spacing between targets (WCAG 2.5.8), no drag-only interactions (WCAG 2.5.7)

### Dictation (macOS built-in, Google Docs Voice Typing)

- Passive dictation into text fields
- **Requirements**: `autocomplete` attributes, no auto-correcting input values, visible editable boundaries

### Cognitive accessibility (COGA)

See also the full [Cognitive Accessibility (COGA)](#cognitive-accessibility-coga-1) section below.

- Plain language: reading level ≤ grade 8 for general content
- Consistent navigation and labeling (WCAG 3.2.3 / 3.2.4)
- Error recovery: suggest corrections (3.3.3), allow undo (3.3.4)
- No time limits or extend them (2.2.1)
- Accessible authentication — avoid cognitive function tests in login steps unless an alternative, an assisting mechanism, or a 3.3.8 exception applies (WCAG 3.3.8)
- Break complex processes into steps; show progress
- Use icons alongside text for reinforcement

---

## Cognitive Accessibility (COGA)

See also the short [Cognitive accessibility (COGA)](#cognitive-accessibility-coga) list under alternative input methods above.

Cognitive, language, and learning disabilities affect ~15% of people. WCAG addresses them partially — COGA supplemental guidance fills the gaps.

### Top 10 COGA design patterns

| Pattern | What to do | WCAG mapping |
|---------|-----------|---------------|
| Plain language | Reading level ≤ grade 8; short sentences; active voice | 3.1.5 (AAA) |
| Familiar patterns | Standard nav location; known icons; no novel interactions | 3.2.3 / 3.2.4 |
| No time limits | Extend or remove timers; show countdown with `aria-live` | 2.2.1 / 2.2.3 |
| Reduce cognitive load | ≤7 nav items; progressive disclosure; no autoplay | 3.2.2 |
| Support memory | Pre-fill known data; breadcrumbs; undo; don't re-ask (3.3.7) | 3.3.7 (WCAG 2.2) |
| Clear error recovery | Say what happened + exactly what to do; inline validation | 3.3.1 / 3.3.3 |
| Visible labels | Prefer a persistent visible `<label>`; a placeholder alone is a weak label (disappears on input, low contrast): judge against 3.3.2, see `references/form-labels-and-names.md` | 3.3.2 |
| No distractions | `prefers-reduced-motion`; no autoplay audio | 2.2.2 / 2.3.1 |
| Consistent vocabulary | Same word for same thing; glossary available | 3.1.3 (AAA) |
| Multiple input modes | Text + autocomplete; voice input; no drag-only (2.5.7) | 2.1.1 / 2.5.7 |

### Accessible authentication (WCAG 3.3.8 — WCAG 2.2)
```html
<!-- ⚠️ Cognitive function test (transcribing characters): conforms to 3.3.8 only if the step also
     provides an alternative method or an assisting mechanism. Judge the whole process, not this field. -->
<p>Type the characters you see in the image:</p>
<img src="captcha.png" alt="">
<input type="text" name="captcha">

<!-- Options that can support 3.3.8 (confirm they work in the real process) -->
<!-- 1. Allow paste and password managers in password fields -->
<input type="password" autocomplete="current-password">
<!-- 2. Offer another method (e.g. WebAuthn/passkeys, email link) -->
<!-- 3. Codes sent by email/SMS must be pasteable or autofillable, not only retyped -->
<!-- 4. An audio CAPTCHA that still requires transcribing is not an alternative -->
```

> Full pattern database: `data/cognitive-accessibility.csv` (20 patterns)
> Search: `python scripts/search.py cognitive --keyword memory`
