# Accessibility Conformance Report template (based on VPAT® 2.5)

> **Unofficial template** — delete this line before publishing. Fill every `[PLACEHOLDER]`.
> This is not the official VPAT®. The VPAT® name and form belong to the Information Technology Industry Council (ITI); this file only follows the VPAT 2.5 structure. For an official ACR, download the current form from https://www.itic.org/policy/accessibility/vpat

---

## Cover Page

| Field | Value |
|-------|-------|
| **Name of Product / Version** | [Product Name v0.0] |
| **Report Date** | [YYYY-MM-DD] |
| **Product Description** | [Brief description of what the product does and its primary users] |
| **Contact Information** | [Name, email, organization] |
| **Notes** | [Optional: scope limitations, testing environments, exclusions] |
| **Evaluation Methods Used** | Automated (axe-core), keyboard-only, screen reader (NVDA+Firefox, VoiceOver+Safari, TalkBack+Chrome), manual SC checks |

---

## Applicable Standards / Guidelines

This report covers conformance with the following accessibility standards/guidelines:

- [ ] Web Content Accessibility Guidelines 2.0 — Levels A, AA, AAA
- [ ] Web Content Accessibility Guidelines 2.1 — Levels A, AA, AAA (choose when the buyer or a law requires 2.1)
- [ ] Web Content Accessibility Guidelines 2.2 — Levels A, AA, AAA ✅ **(primary)**
- [ ] Revised Section 508 standards (36 CFR Part 1194; incorporates WCAG 2.0 A and AA)
- [ ] EN 301 549 Accessibility requirements for ICT products and services: v3.2.1 (2021-03, WCAG 2.1; the version cited under the Web Accessibility Directive) or v4.1.1 (2026-09, WCAG 2.2; Official Journal citation not confirmed as of 2026-11-15)

---

## Terms

The following are the terms used for conformance levels in this report:

| Term | Meaning |
|------|---------|
| **Supports** | The functionality fully meets the criterion without known exceptions |
| **Partially Supports** | The functionality meets the criterion in some but not all ways, or the product does not fully meet the criterion |
| **Does Not Support** | The majority of product functionality does not meet the criterion |
| **Not Applicable** | The criterion is not relevant to this product |
| **Not Evaluated** | The criterion was not evaluated and no claim is made |

---

## WCAG 2.x Report

### Table 1: Success Criteria, Level A

| Criteria | Conformance Level | Remarks and Explanations |
|----------|------------------|--------------------------|
| **1.1.1 Non-text Content** (Level A) | [Supports / Partially Supports / Does Not Support / Not Applicable] | [Explanation: all informative images have alt text; decorative images have alt=""] |
| **1.2.1 Audio-only and Video-only (Prerecorded)** (Level A) | | |
| **1.2.2 Captions (Prerecorded)** (Level A) | | |
| **1.2.3 Audio Description or Media Alternative (Prerecorded)** (Level A) | | |
| **1.3.1 Info and Relationships** (Level A) | | |
| **1.3.2 Meaningful Sequence** (Level A) | | |
| **1.3.3 Sensory Characteristics** (Level A) | | |
| **1.4.1 Use of Color** (Level A) | | |
| **1.4.2 Audio Control** (Level A) | | |
| **2.1.1 Keyboard** (Level A) | | |
| **2.1.2 No Keyboard Trap** (Level A) | | |
| **2.1.4 Character Key Shortcuts** (Level A — WCAG 2.1) | | |
| **2.2.1 Timing Adjustable** (Level A) | | |
| **2.2.2 Pause, Stop, Hide** (Level A) | | |
| **2.3.1 Three Flashes or Below Threshold** (Level A) | | |
| **2.4.1 Bypass Blocks** (Level A) | | |
| **2.4.2 Page Titled** (Level A) | | |
| **2.4.3 Focus Order** (Level A) | | |
| **2.4.4 Link Purpose (In Context)** (Level A) | | |
| **2.5.1 Pointer Gestures** (Level A — WCAG 2.1) | | |
| **2.5.2 Pointer Cancellation** (Level A — WCAG 2.1) | | |
| **2.5.3 Label in Name** (Level A — WCAG 2.1) | | |
| **2.5.4 Motion Actuation** (Level A — WCAG 2.1) | | |
| **3.1.1 Language of Page** (Level A) | | |
| **3.2.1 On Focus** (Level A) | | |
| **3.2.2 On Input** (Level A) | | |
| **3.2.6 Consistent Help** (Level A — WCAG 2.2) | | |
| **3.3.1 Error Identification** (Level A) | | |
| **3.3.2 Labels or Instructions** (Level A) | | |
| **3.3.7 Redundant Entry** (Level A — WCAG 2.2) | | |
| **4.1.1 Parsing** (Level A — Obsolete in WCAG 2.2) | Supports | Always satisfied for HTML/XML content in WCAG 2.0/2.1 per the W3C erratum; removed in WCAG 2.2 |
| **4.1.2 Name, Role, Value** (Level A) | | |

---

### Table 2: Success Criteria, Level AA

| Criteria | Conformance Level | Remarks and Explanations |
|----------|------------------|--------------------------|
| **1.2.4 Captions (Live)** (Level AA) | | |
| **1.2.5 Audio Description (Prerecorded)** (Level AA) | | |
| **1.3.4 Orientation** (Level AA — WCAG 2.1) | | |
| **1.3.5 Identify Input Purpose** (Level AA — WCAG 2.1) | | |
| **1.4.3 Contrast (Minimum)** (Level AA) | | |
| **1.4.4 Resize Text** (Level AA) | | |
| **1.4.5 Images of Text** (Level AA) | | |
| **1.4.10 Reflow** (Level AA — WCAG 2.1) | | |
| **1.4.11 Non-text Contrast** (Level AA — WCAG 2.1) | | |
| **1.4.12 Text Spacing** (Level AA — WCAG 2.1) | | |
| **1.4.13 Content on Hover or Focus** (Level AA — WCAG 2.1) | | |
| **2.4.5 Multiple Ways** (Level AA) | | |
| **2.4.6 Headings and Labels** (Level AA) | | |
| **2.4.7 Focus Visible** (Level AA) | | |
| **2.4.11 Focus Not Obscured (Minimum)** (Level AA — WCAG 2.2) | | |
| **2.5.7 Dragging Movements** (Level AA — WCAG 2.2) | | |
| **2.5.8 Target Size (Minimum)** (Level AA — WCAG 2.2) | | |
| **3.1.2 Language of Parts** (Level AA) | | |
| **3.2.3 Consistent Navigation** (Level AA) | | |
| **3.2.4 Consistent Identification** (Level AA) | | |
| **3.3.3 Error Suggestion** (Level AA) | | |
| **3.3.4 Error Prevention (Legal, Financial, Data)** (Level AA) | | |
| **3.3.8 Accessible Authentication (Minimum)** (Level AA — WCAG 2.2) | | |
| **4.1.3 Status Messages** (Level AA — WCAG 2.1) | | |

---

### Table 3: Success Criteria, Level AAA (Optional)

> Fill only if AAA conformance is claimed.

| Criteria | Conformance Level | Remarks and Explanations |
|----------|------------------|--------------------------|
| **1.2.6 Sign Language (Prerecorded)** (Level AAA) | | |
| **1.2.7 Extended Audio Description (Prerecorded)** (Level AAA) | | |
| **1.2.8 Media Alternative (Prerecorded)** (Level AAA) | | |
| **1.2.9 Audio-only (Live)** (Level AAA) | | |
| **1.3.6 Identify Purpose** (Level AAA — WCAG 2.1) | | |
| **1.4.6 Contrast (Enhanced)** (Level AAA) | | |
| **1.4.7 Low or No Background Audio** (Level AAA) | | |
| **1.4.8 Visual Presentation** (Level AAA) | | |
| **1.4.9 Images of Text (No Exception)** (Level AAA) | | |
| **2.1.3 Keyboard (No Exception)** (Level AAA) | | |
| **2.2.3 No Timing** (Level AAA) | | |
| **2.2.4 Interruptions** (Level AAA) | | |
| **2.2.5 Re-authenticating** (Level AAA) | | |
| **2.2.6 Timeouts** (Level AAA — WCAG 2.1) | | |
| **2.3.2 Three Flashes** (Level AAA) | | |
| **2.3.3 Animation from Interactions** (Level AAA — WCAG 2.1) | | |
| **2.4.8 Location** (Level AAA) | | |
| **2.4.9 Link Purpose (Link Only)** (Level AAA) | | |
| **2.4.10 Section Headings** (Level AAA) | | |
| **2.4.12 Focus Not Obscured (Enhanced)** (Level AAA — WCAG 2.2) | | |
| **2.4.13 Focus Appearance** (Level AAA — WCAG 2.2) | | |
| **2.5.5 Target Size (Enhanced)** (Level AAA) | | |
| **2.5.6 Concurrent Input Mechanisms** (Level AAA — WCAG 2.1) | | |
| **3.1.3 Unusual Words** (Level AAA) | | |
| **3.1.4 Abbreviations** (Level AAA) | | |
| **3.1.5 Reading Level** (Level AAA) | | |
| **3.1.6 Pronunciation** (Level AAA) | | |
| **3.2.5 Change on Request** (Level AAA) | | |
| **3.3.5 Help** (Level AAA) | | |
| **3.3.6 Error Prevention (All)** (Level AAA) | | |
| **3.3.9 Accessible Authentication (Enhanced)** (Level AAA — WCAG 2.2) | | |

---

## Revised Section 508 Report (US Federal)

### Chapter 3: Functional Performance Criteria (FPC)

| Criteria | Conformance Level | Remarks and Explanations |
|----------|------------------|--------------------------|
| 302.1 Without Vision | | |
| 302.2 With Limited Vision | | |
| 302.3 Without Perception of Color | | |
| 302.4 Without Hearing | | |
| 302.5 With Limited Hearing | | |
| 302.6 Without Speech | | |
| 302.7 With Limited Manipulation | | |
| 302.8 With Limited Reach and Strength | | |
| 302.9 With Limited Language, Cognitive, and Learning Abilities | | |

### Chapter 4: Hardware

> Not Applicable — software/web product.

### Chapter 5: Software

| Criteria | Conformance Level | Remarks and Explanations |
|----------|------------------|--------------------------|
| 502.2.1 User Control of Accessibility Features | | |
| 502.2.2 No Disruption of Accessibility Features | | |
| 502.3 Accessibility Services | | |
| 502.4 Platform Accessibility Features | | |
| 503.2 User Preferences | | |
| 503.3 Alternative User Interfaces | | |
| 503.4 User Controls for Captions and Audio Description | | |

### Chapter 6: Support Documentation and Services

| Criteria | Conformance Level | Remarks and Explanations |
|----------|------------------|--------------------------|
| 601.1 Scope | | |
| 602.2 Accessibility and Compatibility Features | | |
| 602.3 Electronic Support Documentation | See WCAG 2.x sections | |
| 602.4 Alternate Formats for Non-Electronic Support Docs | | |
| 603.2 Support Services | | |
| 603.3 User Training | | |

---

## EN 301 549 Report (EU)

> EN 301 549 v3.2.1 incorporates WCAG 2.1 Level A and AA by reference (Clause 9); v4.1.1 moves this to WCAG 2.2. State which version you report against. Complete the WCAG 2.x sections above. Additional clauses:

| Criteria | Conformance Level | Remarks and Explanations |
|----------|------------------|--------------------------|
| 11.1.2 Two-Way Voice Communication | Not Applicable | |
| 11.8.1 Content Technology | | |
| 12.1.2 Accessible Documentation | | |
| 12.2.2 Technical Support Information | | |
| 12.2.4 Accessible Documentation (Support) | | |

---

## Legal Notice

> *(Optional — consult your legal team)*
>
> This VPAT is provided for informational purposes and represents [Organization]'s good-faith assessment of accessibility conformance at the time of evaluation. It does not constitute a warranty or guarantee. Conformance may vary based on user environment, assistive technology versions, and browser configurations. [Organization] is committed to ongoing accessibility improvements.

---

## Appendix: Testing Environment

| Component | Details |
|-----------|---------|
| OS | Windows 11 / macOS Sonoma |
| Browsers | Chrome [version], Firefox [version], Safari [version], Edge [version] |
| Screen readers | NVDA [version] + Firefox, VoiceOver macOS + Safari, TalkBack [version] + Chrome |
| Automated tools | axe-core [version], Lighthouse [version] |
| Evaluation date | [YYYY-MM-DD] |

---

*VPAT® is a registered trademark of the Information Technology Industry Council (ITI). This unofficial template follows the VPAT 2.5 structure; it is not published or endorsed by ITI.*
*Reference: https://www.itic.org/policy/accessibility/vpat*
