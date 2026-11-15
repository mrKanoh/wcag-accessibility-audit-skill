# WCAG criteria and versions

WCAG principles, the most commonly failed Level A and AA criteria, the WCAG 2.2 additions, and the status of the WCAG 3.0 draft.

## WCAG Principles (POUR)

| Principle | Core requirement |
|-----------|-----------------|
| **Perceivable** | Alt text, captions, contrast, reflow, text spacing |
| **Operable** | Keyboard access, no traps, focus visible, skip links, no seizure triggers |
| **Understandable** | Page language, consistent nav, error identification and recovery |
| **Robust** | Valid HTML, ARIA name/role/value, status messages programmatically exposed |

### High-impact criteria, Levels A and AA (most commonly failed)

| ID | Level | Criterion | Requirement |
|----|-------|-----------|-------------|
| 1.1.1 | A | Non-text Content | `alt` for informative; `alt=""` for decorative |
| 1.3.1 | A | Info and Relationships | Semantic structure preserved programmatically |
| 1.4.3 | AA | Contrast (Minimum) | 4.5:1 text / 3:1 large (18pt or 14pt bold) |
| 1.4.10 | AA | Reflow | Usable at 320 CSS px with no horizontal scroll |
| 1.4.11 | AA | Non-text Contrast | 3:1 vs adjacent colors for visual info needed to identify UI components and states (e.g. an author-styled focus indicator) and graphics needed to understand content; exceptions: inactive components, user-agent default appearance not modified by the author, essential graphics |
| 1.4.12 | AA | Text Spacing | Supports line-height 1.5, paragraph 2×, letter 0.12×, word 0.16× |
| 2.1.1 | A | Keyboard | All functionality operable by keyboard |
| 2.1.2 | A | No Keyboard Trap | Focus must never get stuck |
| 2.4.3 | A | Focus Order | Logical focus sequence |
| 2.4.7 | AA | Focus Visible | A keyboard focus indicator must be visible (sets no contrast ratio; see 1.4.11 / 2.4.13) |
| 3.3.1 | A | Error Identification | Errors described in text |
| 4.1.2 | A | Name, Role, Value | Interactive elements expose name/role/state |
| 4.1.3 | AA | Status Messages | Dynamic updates announced without focus move |

### WCAG 2.2 additions (new since 2.1)

| ID | Level | Criterion | What changed |
|----|-------|-----------|--------------|
| 2.4.11 | AA | **Focus Not Obscured (Minimum)** | Focused element can't be entirely hidden by author-created content such as sticky UI (no contrast requirement) |
| 2.4.12 | AAA | Focus Not Obscured (Enhanced) | …or *partially* hidden |
| 2.4.13 | AAA | Focus Appearance | Indicator area ≥ a 2 CSS px perimeter of the unfocused component, and 3:1 between the same pixels focused vs unfocused; exceptions: user-agent indicator, or indicator and its background not modified by the author |
| 2.5.7 | AA | **Dragging Movements** | Drag operations need a single-pointer alternative |
| 2.5.8 | AA | **Target Size (Minimum)** | Pointer targets ≥ 24×24 CSS px (exceptions apply) |
| 3.2.6 | A | **Consistent Help** | Help mechanisms in consistent relative order |
| 3.3.7 | A | **Redundant Entry** | Don't force re-entry of already-provided info |
| 3.3.8 | AA | **Accessible Authentication (Minimum)** | No step of an authentication process requires a cognitive function test unless that step offers an alternative method, an assisting mechanism (e.g. password manager, paste), object recognition, or identifying the user's own non-text content |
| 3.3.9 | AAA | Accessible Authentication (Enhanced) | Same as 3.3.8, but only the alternative and the assisting mechanism remain as exceptions (object recognition and personal content are not) |

> Criteria catalog (59 rows, not complete: no 2.1 AAA criteria; `versions` shows 2.1 / 2.2; `--wcag-version 2.1|2.2` filters by it, and `--level AA` means exactly AA, not A+AA): `data/wcag-criteria.csv`

---

## WCAG 3.0 — Draft status

WCAG 3.0 is an **incomplete W3C Working Draft** and **not a standard**. WCAG 2.1/2.2 AA remains the compliance target. The draft says it still has several years of work and that details will change; it also states that WCAG 3 does not replace WCAG 2, which will still be required in many places for a long time.

Sources (check them for the current status; reviewed 2026-10-01 against the 10 September 2026 Working Draft):
- Draft: https://www.w3.org/TR/wcag-3.0/
- Introduction: https://www.w3.org/WAI/standards-guidelines/wcag/wcag3-intro/

### What not to state as fact
- No WCAG 3 success criteria with fixed numbers (such as "3.1.1"): requirements in the draft are named (for example "Text contrast sufficient (minimum)") and may change.
- Bronze, Silver and Gold **do** appear in section 4.1.4 of the draft, as the 4th–6th *reporting tiers* above conformance (the 3rd tier is conformance), but the number of supplemental requirements and assertions for each is still **TBD**. Section 4 is informative and exploratory, and the draft's editor's notes say the model is still under discussion (an alternative proposal uses scoring, with Bronze/Silver/Gold awarded after conformance). Present them as proposed reporting tiers in development, not as a finalized conformance target, and do not say what is required to reach them.
- The draft does not use A/AA/AAA levels in the way WCAG 2 does; do not map WCAG 2 levels onto WCAG 3 tiers.
- No contrast algorithm or thresholds: the draft says the contrast algorithm is yet to be determined. APCA is **not** confirmed as the WCAG 3 algorithm, so do not quote APCA Lc values as WCAG 3 requirements.
- No finalization date.

### How to prepare now
1. **Keep targeting WCAG 2.2 AA** (2.1 AA where a law requires it). Contrast compliance is measured with the WCAG 2.x ratios (1.4.3, 1.4.6, 1.4.11).
2. **Follow the draft** at the links above before answering any WCAG 3 question, and label anything from it as draft.
3. If a user asks about APCA, explain that it is a separate contrast model that is not part of WCAG 2.x conformance and not confirmed for WCAG 3.

> The CLI command `python scripts/search.py wcag3` and the MCP resource `wcag://draft-wcag3` return only a draft-status notice with these links; they contain no criteria.
