# Site audit execution procedure

Use this procedure for a scoped website evaluation. Record work in the [audit workbook](../templates/site-audit-workbook.md), then summarize verified results in the [report](../templates/audit-report.md). Translate the working copy into the user's language. Keep client material and collected evidence in a separate engagement folder, not in reusable skill resources.

## 1. Agree scope and establish access

Record the target WCAG version and level, included hosts, URL boundaries, exclusions, evaluation dates, auditor and technical/inclusion contacts. Define whether “linked pages” means direct links or recursive discovery, and agree a page limit before estimating effort. A link to another host does not automatically include that platform.

Build a deduplicated inventory of pages, templates, complete user processes and states. Choose a representative manual sample covering distinct functionality and content, common components, essential tasks and a random component; document selection and any discovered gaps. A fixed page count alone does not establish representativeness. List the automatic scan inventory separately from the manual sample. Excluded documents, media or process steps constrain conclusions about their containing pages and complete processes.

Start a small pilot with a home page, an interior page and an identified public form, if available. Record actual URLs; do not invent a form or silently substitute another host. Do not send messages, applications or test submissions to a live service without authorization. If a form is absent, inaccessible or outside scope, record that and retain the gap.

Check in a real browser that the expected site, rather than an access challenge, has loaded. A successful text fetch is not proof of browser access; one successful browser session is not proof that a batch scanner can access the site. Record timeouts, challenge text and affected URLs separately. Do not infer Cloudflare as the cause of a generic timeout. Coordinate any access exception with the site owner; specify scope, duration and removal responsibility without disabling protections yourself.

## 2. Execute automatic checks with existing tooling

Use an available browser extension or an authorized browser automation runner with axe-core; this skill does not install or provide that runner. Record tool/engine version, browser/OS, viewport, date, loaded URL, evaluated state, configuration, disabled rules and iframe limitations.

For WCAG 2.2 AA, select inherited A and AA rules as well as additions. For axe-core versions supporting these tags, the cumulative tag set is `wcag2a`, `wcag2aa`, `wcag21a`, `wcag21aa`, `wcag22aa`. Verify the installed engine's supported tags and rule mapping; `wcag22aa` alone does not cover the inherited criteria. Keep best-practice results separate from normative failures. Save the effective configuration and raw output.

Evaluate relevant states, not just initial page load: expanded navigation, dialogs, validation errors and confirmations where authorized. Reuse results for shared components only with a stated rationale and evidence that the implementation/state is shared; preserve the affected-page list.

Triage violations, incomplete results and suspected false positives. An axe pass is limited to that rule, element and state. No detected violations does not mean the page passes WCAG. Keep raw results and each triage decision traceable to evidence. A blocked page is not a WCAG failure of the target site.

## 3. Execute manual protocols

The following protocols are a starter set, not the complete criterion checklist. Build the criterion matrix from the selected version, include both A and AA for an AA target, and decide how each criterion will be evaluated. The CLI's `--level AA` returns only AA records; it does not include A records. For 2.2, query `python scripts/search.py wcag --wcag-version 2.2 --output json` and select levels A and AA (55 records). Check normative wording and exceptions before deciding a failure.

For every execution, record preconditions, expected behavior, actual steps, observed result, evidence and evaluator. A DOM/accessibility-tree snapshot is not an observation of NVDA speech.

| Protocol | Execution and expected behavior | Typical criteria to investigate |
|---|---|---|
| Keyboard | From a known starting point, use Tab/Shift+Tab and the keys appropriate to each control. Complete the scoped tasks; check reachable controls, logical order, visible and unobscured focus, escape from components and focus return. Record actual key sequences and any blocker. | 2.1.1, 2.1.2, 2.4.3, 2.4.7, 2.4.11 (WCAG 2.2 only) |
| Screen reader | Record NVDA, browser and OS versions. Traverse headings, regions and links, then operate relevant controls/forms in the appropriate reading or interaction mode. Record actual announcements, names, roles, states and dynamic messages. Missing expertise or access means not evaluated. | 1.3.1, 2.4.4, 4.1.2, 4.1.3 |
| Resize and reflow | Check text resizing to 200% and reflow at 320 CSS px width (or 256 CSS px height for vertically written content), with equivalent zoom where suitable. Record viewport and zoom, content loss, overlap and two-dimensional scrolling; apply criterion exceptions. | 1.4.4, 1.4.10 |
| Text spacing | Apply line height 1.5 times font size, paragraph spacing 2 times, letter spacing 0.12 times and word spacing 0.16 times, subject to language/script applicability. Check loss of content or functionality. These are override tolerances, not mandatory default styles. | 1.4.12 |
| Contrast and visual cues | Measure required foreground/background pairs, including relevant interaction states and images/gradients. Record colors, ratio, text size/weight and exceptions; inspect information conveyed only by color. | 1.4.1, 1.4.3, 1.4.11 |
| Forms | Inspect labels, instructions, required fields, accessible names and input purpose. Where authorized, exercise invalid/valid input and recovery; inspect errors and status messages with keyboard and reader. Do not infer server behavior from markup. | 1.3.5, 2.5.3, 3.3.1, 3.3.2, 3.3.3, 4.1.2, 4.1.3 |
| Other applicable criteria | Review images, language, page titles, links, motion, timing, target size, pointer interactions, media and other applicable requirements from the complete matrix. Record exclusions instead of treating them as passes. | Selected A/AA matrix |

When a site offers support controls, record a baseline, activate one feature, repeat the affected tests, then restore baseline. Test combinations relevant to real use and note persistence, reset behavior and regressions. A contrast toggle does not prove contrast compliance. Absence of a panel is not itself a WCAG failure; native browser and assistive-technology use still matters.

## 4. Optional institutional inclusion review

Include this section only when the engagement requests it. Agree observable indicators with the inclusion contact. Keep the basis explicit: WCAG requirement, supplemental guidance, contractual indicator or institution-confirmed fact. Do not convert a recommendation into an AA failure or a legal obligation.

| Dimension | Evidence to collect | Interpretation boundary |
|---|---|---|
| Disability language | Exact passage, URL, context and proposed alternative; for Chile, check current SENADIS guidance and community preferences. | Keyword matches flag candidates; quotation, context and preferred identity terms need human review. |
| Cognitive clarity | Task instructions, jargon, definitions, structure and recovery support; use COGA guidance. | COGA supplements WCAG; not every recommendation is an AA criterion. |
| Readability | Chosen Spanish text corpus, extraction/exclusion rules, tool/version, formula, word/sentence/syllable counts and result. | INFLESZ is a readability indicator, not proof of understanding, inclusion or WCAG conformance. If the method cannot be reproduced, mark it unverified. No INFLESZ calculator is supplied here. |
| Easy Read / sign language | Available adaptations, intended audience, coverage and evidence of validation. | Clear wording is not evidence of a validated Easy Read adaptation. These are not blanket AA requirements; assess any applicable criterion separately. |
| Employment and adjustments | Published instructions, request channels and confirmation of the actual adjustment process with the institution. | An external jobs portal or a missing public statement does not prove institutional practice or legal compliance. |
| Contact, commitment and representation | Available channel alternatives, accessibility of entry points, published policy and contextual review of content. | A listed email/WhatsApp does not prove response quality or accessible end-to-end service. “Not found in reviewed pages” does not mean “does not exist.” |

Verify official legal sources and institutional applicability separately when legal analysis is requested. The skill's jurisdiction table is a starting reference, not a legal opinion.

## 5. Record, review and report

Use separate fields for evidence provenance and outcome. Provenance: observed in browser, tool output, static inspection, institution-reported or unverified. Outcome: passes, fails, requires review, not evaluated or not applicable (with rationale). A candidate finding remains requires review until there is sufficient evidence. A confirmed failure can be reported while other checks remain untested; a pass needs the applicable checks for the stated scope.

Give each finding an ID and link it to page/state IDs, criterion or supplemental basis, reproducible steps, observed barrier, affected users, evidence and recommendation. Justify severity by user impact. Count unique barriers separately from affected instances/pages. Remove personal data from client-facing evidence.

Report dimensions with coverage and evidence gaps, not an invented inclusion score. Assign proposed correction owners for institutional confirmation. Keep a diagnostic, a sampled evaluation and a conformance claim distinct: a clean sample does not establish full-site conformance. WCAG conformance concerns full pages and complete processes, including applicable media and embedded content; exclusions must remain visible.

Before delivery, reconcile the workbook, raw evidence and report; check unresolved items and re-test commitments. Use only actual tool/browser/reader pairings in the report. If PDF/presentation delivery is requested, prepare them from reviewed results, check headings, language, reading order, alternatives and export accessibility, and verify the exported artifacts. This procedure does not generate or validate a PDF automatically.

## Sources

- [WCAG 2.2 normative requirements and conformance](https://www.w3.org/TR/WCAG22/).
- [WCAG-EM evaluation methodology](https://www.w3.org/TR/WCAG-EM/).
- [axe-core API and rule tags](https://github.com/dequelabs/axe-core/blob/develop/doc/API.md) — verify against the installed release.
- [COGA supplemental guidance](https://www.w3.org/TR/coga-usable/).
- [SENADIS disability language recommendations](https://www.senadis.gob.cl/participacion/d/noticias/9329/conoce-las-recomendaciones-para-el-uso-del-lenguaje-en-discapacidad-senadis).
