# DECISIONS

Design and scope decisions already taken, with date and reason. Errors and how to prevent them go in `LESSONS.md`, not here.

## 2026-11-06 — Merging to `main` publishes to production

- **Decision:** merging a pull request into `main` counts as publishing. `AGENTS.md` carries the line `- Fusionar publica en producción: sí`, and only Ariel merges.
- **Reason:** `main` is what users clone (the README tells them to clone `main`). There is no separate release channel besides the manual ZIP in `dist/agensi/`.

## 2026-11-14 — WCAG 2.2 AA is the default; WCAG 2.1 AA only when a law or contract requires it

- **Decision:** when designing and building, the skill targets **WCAG 2.2 AA**. It recommends **WCAG 2.1 AA** only when the jurisdiction or the contract names it (for example the US DOJ Title II rule, or EN 301 549 v3.2.1 while it is the version cited in the Official Journal of the EU). W3C states that content that conforms to WCAG 2.2 also conforms to WCAG 2.0 and 2.1 (WCAG 2.2 Abstract, https://www.w3.org/TR/WCAG22/), so meeting 2.2 AA also meets 2.1 AA. The one criterion not carried over is 4.1.1 Parsing, which WCAG 2.2 removed ("Obsolete and removed"); I did not confirm in this pass the W3C erratum that treats it as satisfied for 2.0/2.1.
- **Reason:** WCAG 2.2 is the W3C Recommendation in force (published 5 October 2023, source: https://www.w3.org/WAI/standards-guidelines/wcag/new-in-22/), and ETSI published EN 301 549 v4.1.1 on 2026-09-02, which moves the web requirements from WCAG 2.1 to WCAG 2.2 (Levels A and AA; source: etsi.org, ETSI delivery folder for EN 301 549). That version does not give a presumption of conformity under the EAA until it is cited in the Official Journal of the EU; as of 2026-11-15 this citation was not confirmed (see `data/legal-framework.csv`).
