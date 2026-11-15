# Audit process, common fixes and KPIs

The structured audit framework, the most common issues with their fixes, and the KPIs to measure accessibility over time. For a full site audit, read [site-audit-procedure.md](site-audit-procedure.md).

## Audit Methodology

For a site audit, read [the audit execution procedure](site-audit-procedure.md) and fill [the audit workbook](../templates/site-audit-workbook.md). They define scope, page/state inventory, manual protocols and evidence status. Include the optional institutional inclusion review only when requested. These resources guide an auditor; they do not add a crawler, run axe or operate a screen reader.

Structured audit framework (matches professional curriculum):

```
1. Scope       Sample pages (home, template types, auth, checkout, top 10 by traffic)
2. Standard    WCAG 2.1/2.2 level (usually AA); jurisdictional overlays (Section 508, EN 301 549, EAA)
3. Automated   axe DevTools + Lighthouse + WAVE → baseline violations
4. Keyboard    Tab through every flow; verify reachability + visible focus
5. Screen AT   NVDA+Firefox, VoiceOver+Safari, TalkBack+Chrome
6. Visual      Zoom 200% & 400%; reflow 320 px; text-spacing override
7. Manual SC   Check non-automatable criteria (1.3.1 structure, 2.4.3 order, 3.3.x errors, 2.5.x target size, 2.4.11 focus obscured)
8. Findings    One row per issue: URL · element · criterion · severity · steps · recommendation
9. Severity    Critical / Serious / Moderate / Minor (align to Deque or internal scale)
10. Report     Executive summary, remediation plan, VPAT/ACR update, retest plan
```

**Sampling guidance**: choose representative templates rather than every page. Re-audit the same sample after remediation to measure regression.

**ACR/VPAT**: maintain a current Accessibility Conformance Report mapping every WCAG SC → Supports / Partially Supports / Does Not Support / Not Applicable with rationale.

---

## Accessibility KPIs

Measure what you ship, not only what you scan.

| KPI | Target | Cadence |
|-----|--------|---------|
| Axe violations per 1k DOM nodes | < 1.0 | Per build |
| WCAG AA conformance rate (pages) | 100% | Quarterly |
| Critical issues open | 0 | Weekly |
| MTTR (mean time to remediate) | < 14 days | Monthly |
| Keyboard task completion rate | ≥ 95% | Per release |
| Screen reader task success rate | ≥ 90% | Per release |
| Focus-visible coverage | 100% | Per build |
| Alt text presence on informative images | 100% | Per build |
| VPAT/ACR freshness | ≤ 180 days | Quarterly |
| Accessibility AC coverage in user stories | ≥ 90% | Sprint |

> Full KPI catalog: `data/kpis.csv`

---

## Common Issues & Fixes

| Issue | Fix |
|-------|-----|
| Missing alt text | Descriptive `alt` for informative; `alt=""` for decorative |
| Poor color contrast | ≥ 4.5:1 body, 3:1 large (1.4.3) |
| No keyboard support | `<button>`; or `tabindex="0"` + Enter/Space handlers |
| Invisible focus | `:focus-visible { outline: 2px solid; }`; never `outline: none` |
| Missing form labels | `<label for="id">` or `aria-label` / `aria-labelledby` |
| Bad heading hierarchy | h1→h2→h3 in order |
| ARIA misuse | Semantic HTML first |
| Focus trapped in modal | Tab wraps inside; Escape closes; focus returns to the trigger (or a logical element if it is gone) |
| Unlabeled icon button | `aria-label` on `<button>` + `aria-hidden="true"` on SVG |
| Auto-playing audio (1.4.2) | Audio that plays automatically for more than 3 seconds needs a mechanism to pause or stop it, or a volume control independent of the system volume. Prefer no autoplay. Moving or auto-updating visuals are a separate rule (2.2.2) |
| AJAX content not announced | `aria-live="polite"` region; inject content into it |
| Color as sole conveyor | Add text, icon, or pattern |
| Sticky header hides focus (2.4.11) | `scroll-padding-top: <header-height>` |
| Small tap targets (2.5.8) | ≥ 24×24 CSS px; spacing can satisfy |
| Drag-only reorder (2.5.7) | Provide ↑/↓ buttons or menu |
| Password or code paste/autofill blocked (3.3.8, F109) | Allow paste; allow password managers and autofill |
