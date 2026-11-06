# Site audit workbook

Template: copy into the engagement folder and translate as needed. Empty fields are not completed tests. Follow the [execution procedure](../references/site-audit-procedure.md). Preserve evidence outside the reusable skill and link it by ID.

## Scope and access

| Field | Agreed value |
|---|---|
| Engagement, auditor, date/time and timezone | [Record] |
| Standard and level | [Explicit version; AA includes A] |
| Hosts and URL boundaries; discovery depth and page cap | [Record] |
| Included processes and states | [Record] |
| Exclusions and effect on conclusions | [Record] |
| Technical and inclusion contacts | [Record roles; keep private details separate] |
| Scope approval reference | [Record or pending] |
| Permitted interactions and test submissions | [Record; no live submission by default] |
| Access result per environment | [Expected content / challenge / timeout / other; evidence ID] |
| Temporary exception owner, expiry and closure | [Only if applicable] |

## Page and state inventory

| Page ID | Actual URL | Template/task | State IDs and preconditions | Auto planned/executed | Manual planned/executed | Selection reason or exclusion |
|---|---|---|---|---|---|---|
| [P01] | [URL] | [Record] | [S01: initial; S02: expanded menu, etc.] | [Record separately] | [Record separately] | [Record] |

Record discovered links separately from evaluated pages. For a pilot, select home, interior and an identified in-scope public form. If no form is identified, retain that pending slot; a contact link alone is not a tested form. For the full sample, document coverage of unique functionality, essential tasks and the random selection component.

## Execution environment

| Run ID | Date/time | Tool/engine and version | Browser/OS and versions | Viewport/zoom | Configuration and exclusions | Raw evidence location |
|---|---|---|---|---|---|---|
| [R01] | [Record] | [Record actual tools] | [Record] | [Record] | [Rule tags, disabled rules, iframe limits, etc.] | [Path/ID] |

## Criterion matrix

Populate every criterion at the target version/level, including inherited A criteria for AA. For 2.2 AA, use the 55 A/AA entries, not the three AAA entries, from `wcag --wcag-version 2.2 --output json`. The table below is a schema, not a completed criterion list.

| Criterion | Page/state coverage | Evaluation method | Run/test/evidence IDs | Outcome | Rationale and remaining checks |
|---|---|---|---|---|---|
| [ID and level] | [IDs] | [Automatic + manual as applicable] | [IDs] | [Not evaluated initially] | [Record] |

Outcomes: **passes**, **fails**, **requires review**, **not evaluated**, **not applicable**. Explain not applicable. Keep incomplete tool results as requires review until triaged. Do not aggregate partial checks into a criterion pass.

## Manual execution record

Duplicate this block for each protocol and page/state. Use protocols in the procedure; a list of intended tests is not evidence of execution.

| Field | Actual record |
|---|---|
| Test ID, protocol, page/state and run | [Record] |
| Preconditions and test data | [Sanitized; identify authorization for submissions] |
| Expected behavior and criterion/basis | [Record] |
| Steps actually performed | [Key sequence/actions, not intended steps] |
| Observed result | [Record; no invented reader announcements] |
| Evidence ID and provenance | [Browser / tool / static / institution-reported / unverified] |
| Outcome and rationale | [Record] |
| Blocker or remaining checks | [Record] |

## Support controls comparison

| Feature | Page/state | Baseline test/evidence | Activated test/evidence | Barrier resolved or unchanged | Regressions | Reset verified |
|---|---|---|---|---|---|---|
| [Feature or not identified in reviewed scope] | [IDs] | [IDs] | [IDs or not evaluated] | [Observed effect] | [Record] | [Record] |

## Optional inclusion indicators

Use only for agreed inclusion scope. Copy indicators from the procedure and agree acceptance conditions with the institution. Recommendations and institutional facts have a separate basis from WCAG failures.

| Indicator | Agreed condition and source | Pages/corpus reviewed | Evidence/provenance | Outcome | Institution question / owner |
|---|---|---|---|---|---|
| [Language / clarity / readability / Easy Read / sign language / employment / contact / commitment / representation] | [Record] | [IDs] | [IDs] | [Record] | [Pending confirmation] |

For INFLESZ, attach corpus, extraction rules, tool/version, formula and counts. An inherited number without these is unverified. No score implies audience understanding or validated Easy Read.

## Findings and triage

| Finding ID | Page/state IDs | Barrier and affected users | WCAG criterion or supplemental basis | Evidence IDs | Provenance | Outcome | Severity and rationale | Recommendation |
|---|---|---|---|---|---|---|---|---|
| [F01] | [IDs] | [Observed barrier] | [Separate requirement from guidance] | [IDs] | [Record] | [Record] | [Record impact] | [Record] |

| Raw tool item ID | Run/page/state | Decision | Evidence and reason | Reviewer |
|---|---|---|---|---|
| [ID] | [IDs] | [Confirmed / false positive / duplicate / requires review] | [Record; preserve raw item] | [Record] |

## Correction plan and delivery

| Priority | Finding IDs | Proposed owner / confirmed owner | Action | Acceptance test | Retest status |
|---|---|---|---|---|---|
| [Record] | [IDs] | [Distinguish] | [Record] | [Steps and expected result] | [Not evaluated initially] |

Before producing the report, record:

- Unique confirmed barriers and affected instances/pages, counted separately.
- Coverage by dimension, blocked pages, untested states and institutional confirmations pending.
- Conclusions limited to the evaluated scope; no extrapolated full-site conformance.
- Report evidence review and privacy review performed by [person/date or not performed].
- PDF/presentation production and accessibility verification [actual status, if requested].
- Presentation session [planned/performed, date and audience]; do not imply it occurred from slide creation.
- Access exception closure [owner, confirmation or pending], if applicable.
