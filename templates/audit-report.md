# Accessibility Audit Report

> **Template** — delete this line before publishing. Fill every `[PLACEHOLDER]` section.

Use the [execution procedure](../references/site-audit-procedure.md) and [workbook](site-audit-workbook.md) to establish coverage and evidence before writing conclusions. Example tools and pairings below are not performed tests; replace them with actual runs or mark them not evaluated.

---

## Cover

| Field | Value |
|-------|-------|
| **Product / URL** | [Product name and base URL] |
| **Audit scope** | [Pages and flows audited — list URLs or describe sampling] |
| **Standard** | WCAG 2.1 / 2.2 Level AA (or specify) |
| **Legal overlay** | [Section 508 / EAA / EN 301 549 / AODA / other] |
| **Auditor(s)** | [Name(s)] |
| **Date** | [YYYY-MM-DD] |
| **Retest date** | [Target retest YYYY-MM-DD] |
| **Report version** | 1.0 |

---

## Executive Summary

[2–4 sentence plain-language summary for non-technical stakeholders.]

| Severity | Count |
|----------|-------|
| Critical | [n] |
| Serious | [n] |
| Moderate | [n] |
| Minor | [n] |
| **Total** | **[n]** |

**Conclusion for the evaluated scope**: [Describe confirmed barriers, coverage and limits. A sampled diagnostic is not a full-site conformance claim. State exclusions affecting full pages and complete processes; do not infer conformity from a clean scan.]

**Evidence gaps**: [Blocked pages, untested states/criteria, pending manual or institutional verification.]

---

## Methodology

| Step | Tool / Method |
|------|--------------|
| Automated scan | axe DevTools + Lighthouse |
| Keyboard-only | Chrome (no mouse) |
| Screen reader | NVDA 20xx + Firefox · VoiceOver + Safari · TalkBack + Chrome |
| Visual checks | Colour Contrast Analyser · browser zoom 200% · text-spacing bookmarklet |
| Manual SC checks | 1.3.1, 2.4.3, 2.4.11, 2.5.3, 2.5.8, 3.1.1, 3.3.x |

**Pages sampled**: [n] of [total] (representative templates selected).

**Inventory and selection**: [Link page/state inventory, automatic coverage, manual sample, selection rationale and complete-process coverage.]

## Optional Inclusion Profile

Include only when contracted. Keep WCAG requirements, supplemental guidance and agreed institutional indicators distinct. Do not treat absence in reviewed pages as proof of institutional absence.

| Dimension | Agreed basis | Evaluated coverage | Outcome and evidence IDs | Pending institutional verification |
|----------|--------------|--------------------|--------------------------|------------------------------------|
| [Language, cognitive clarity, readability, employment, contact, commitment, etc.] | [Source/indicator] | [Pages/corpus] | [Passes / Fails / Requires review / Not evaluated / Not applicable, with rationale] | [Record] |

---

## Severity Scale

| Level | Definition |
|-------|-----------|
| **Critical** | Blocks access entirely for one or more disability groups (WCAG A/AA failure) |
| **Serious** | Significantly impairs access; workaround very difficult (WCAG A/AA failure) |
| **Moderate** | Causes notable friction; imperfect workaround exists |
| **Minor** | Minor friction; easy workaround; often best-practice gap |

---

## Findings

> One row per unique issue. Duplicate the block for each finding.

---

### Finding [#001]

| Field | Detail |
|-------|--------|
| **Title** | [Short descriptive title] |
| **URL(s)** | [Page URL] |
| **Element** | [CSS selector or XPath, e.g. `#nav > button.hamburger`] |
| **WCAG SC** | [e.g. 1.3.1 Info and Relationships (Level A)] |
| **Severity** | [Critical / Serious / Moderate / Minor] |
| **Affects** | [e.g. Screen reader users, Keyboard-only users] |
| **Tool found** | [axe / Manual / NVDA / VoiceOver] |
| **State / test / evidence IDs** | [Link reproducible test and sanitized evidence] |
| **Evidence provenance** | [Observed in browser / tool output / static inspection / institution-reported / unverified] |
| **Outcome and basis** | [Confirmed failure / requires review; WCAG requirement or supplemental indicator] |

**Description**

[What is wrong and why it fails the criterion. Be specific.]

**Steps to reproduce**

1. Navigate to [URL]
2. [Action]
3. [Observe]

**Impact**

[Describe the real-world impact on a user with a disability.]

**Recommendation**

[Concrete code or design change. Include a before/after snippet where helpful.]

```html
<!-- Before (inaccessible) -->
<div onclick="openMenu()">☰</div>

<!-- After (accessible) -->
<button type="button" aria-expanded="false" aria-controls="main-menu">
  <svg aria-hidden="true" focusable="false">…</svg>
  <span class="sr-only">Menu</span>
</button>
```

**Effort estimate**: [Low 0–2h / Medium 2–8h / High 8h+]

---

*(repeat Finding block for each issue)*

---

## Positive Findings

[Optional. List patterns done well — reinforces good practice and balances the report.]

- [e.g. Skip link implemented and visible on focus]
- [e.g. All form fields have associated labels]

---

## Remediation Roadmap

| Priority | Finding(s) | Owner | Target sprint |
|----------|-----------|-------|--------------|
| P0 (Critical) | #001, #002 | [Team] | [Sprint / Date] |
| P1 (Serious) | #003–#007 | [Team] | [Sprint / Date] |
| P2 (Moderate) | #008–#015 | [Team] | [Sprint / Date] |
| P3 (Minor) | #016–#020 | [Team] | [Sprint / Date] |

---

## WCAG [version] [level] Evaluation Summary

> Expand this illustrative subset to the complete target criterion matrix, including A for an AA target. Record passes, fails, requires review, not evaluated or justified not applicable, and link evidence/coverage from the workbook. A pass needs the applicable checks for the stated scope; excluded content is not a pass.

| SC | Criterion | Result |
|----|-----------|--------|
| 1.1.1 | Non-text Content | [Outcome, coverage and evidence IDs] |
| 1.3.1 | Info and Relationships | |
| 1.4.3 | Contrast (Minimum) | |
| 1.4.10 | Reflow | |
| 1.4.11 | Non-text Contrast | |
| 1.4.12 | Text Spacing | |
| 2.1.1 | Keyboard | |
| 2.1.2 | No Keyboard Trap | |
| 2.4.1 | Bypass Blocks | |
| 2.4.3 | Focus Order | |
| 2.4.7 | Focus Visible | |
| 2.4.11 | Focus Not Obscured (2.2) | |
| 2.5.3 | Label in Name | |
| 2.5.8 | Target Size (2.2) | |
| 3.1.1 | Language of Page | |
| 3.3.1 | Error Identification | |
| 3.3.2 | Labels or Instructions | |
| 3.3.8 | Accessible Authentication (2.2) | |
| 4.1.2 | Name, Role, Value | |
| 4.1.3 | Status Messages | |

---

## Retest Plan

After remediation, retest:

- [ ] All Critical and Serious findings resolved
- [ ] Automated scan clean (zero critical/serious)
- [ ] Keyboard walkthrough of all core flows
- [ ] Screen reader walkthrough with NVDA + Firefox
- [ ] Update ACR/VPAT

**Retest date**: [YYYY-MM-DD]
**Retest auditor**: [Name]

---

## Appendix

### Tools Used

| Tool | Version | Purpose |
|------|---------|---------|
| axe DevTools | [x.x] | Automated violations |
| Lighthouse | [x.x] | Accessibility score |
| NVDA | [x.x] | Screen reader (Windows) |
| VoiceOver | macOS [version] | Screen reader (Mac) |
| TalkBack | Android [version] | Screen reader (Android) |
| Colour Contrast Analyser | [x.x] | Contrast measurement |
| Chrome DevTools | [version] | Focus / accessibility tree inspection |

### Screen Reader Pairings Tested

Replace example rows with actual pairings and evidence IDs, or state not evaluated. An accessibility-tree inspection alone is not a screen-reader test.

| Reader | Browser | OS |
|--------|---------|-----|
| NVDA | Firefox | Windows 11 |
| VoiceOver | Safari | macOS Sonoma |
| TalkBack | Chrome | Android 14 |

### References

- [WCAG 2.2 Understanding](https://www.w3.org/WAI/WCAG22/Understanding/)
- [WAI-ARIA APG](https://www.w3.org/WAI/ARIA/apg/)
- [Deque Severity Ratings](https://dequeuniversity.com/rules/axe/)
- [Legal framework applicable]: [e.g. EAA effective 28 Jun 2025]
