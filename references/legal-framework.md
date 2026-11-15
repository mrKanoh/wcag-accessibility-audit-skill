# Legal framework

Key jurisdictions, the laws and technical standards they cite, EN 301 549 versions, the EAA, and what to do when a law fixes WCAG 2.1. General information, not legal advice.

## Legal Framework

Compliance is often mandatory. This is general information, not legal advice: confirm the current text with the official source or a lawyer. Rows marked "verified" were checked against official sources on 2026-11-15; the others are not re-verified (see `verified_on` in the CSV). Key jurisdictions:

| Region | Law | Standard | Applies to | Status |
|--------|-----|----------|------------|--------|
| 🇺🇸 USA (federal) | Section 508 (36 CFR part 1194) | WCAG 2.0 A and AA | Federal ICT | Compliance since 2018-01-18 (verified) |
| 🇺🇸 USA (state/local govt) | ADA Title II, DOJ web rule (2024) | WCAG 2.1 AA | State and local government web content and mobile apps | **2027-04-26** (50,000+ people); **2028-04-26** (under 50,000 and special districts); dates extended by DOJ in April 2026 (verified) |
| 🇺🇸 USA (private) | ADA Title III | No technical standard in DOJ rules; DOJ guidance cites WCAG as helpful guidance | Public accommodations | Case law and settlements; the Title II rule does not apply (verified) |
| 🇪🇺 EU | EAA (Directive (EU) 2019/882) | EN 301 549 is the intended harmonised standard | B2C products & services | **Applies since 28 Jun 2025** (Art. 31(2)); Art. 32 transitional measures, including: a period ending 28 Jun 2030 for providers to keep using products lawfully used for similar services before 28 Jun 2025; service contracts agreed before that date continue without alteration until they expire, at most until 28 Jun 2030; self-service terminals (if the Member State allows) until the end of their economically useful life, never more than 20 years after entry into use (verified) |
| 🇪🇺 EU | Web Accessibility Directive (2016/2102) | EN 301 549 v3.2.1 (cited by Decision (EU) 2021/1339) | Public sector websites & apps | In force (Decision (EU) 2021/1339 verified; Directive text not re-read) |
| 🇬🇧 UK | Equality Act + PSBAR 2018 | WCAG 2.2 AA (per GOV.UK guidance) | Public sector | In force (verified) |
| 🇲🇽 Mexico | Acuerdo de Disposiciones generales de accesibilidad Web (DOF 2015-12-03) | WCAG, level AA minimum (version not named) | Federal public administration | In force from 2015-12-04; later reforms not confirmed (verified) |
| 🇨🇦 Canada | ACA | WCAG 2.1 AA | Federal entities | Not re-verified |
| 🇨🇦 Ontario | AODA | WCAG 2.0 AA | Public + large private | Not re-verified |
| 🇦🇺 Australia | DDA + Digital Service Standard | WCAG 2.1 AA | Government | Not re-verified |
| 🇧🇷 Brazil | LBI (Lei 13.146) + eMAG | WCAG 2.1 AA | Public + private collective use | Not re-verified |
| 🇨🇱 Chile | Ley 20.422 + Decreto 1 | WCAG 2.0 AA | Government | Not re-verified |
| 🇪🇸 Spain | RD 1112/2018 (WAD transposition) | EN 301 549 | Public sector | Not re-verified |
| 🇫🇷 France | RGAA 4 + Loi 2005-102 | WCAG 2.1 AA via RGAA | Public + large companies | Not re-verified |

Mexico: NOM-034-STPS-2016 is a workplace safety norm for workers with disabilities, not a web standard.

> Full table with enforcement, notes, `source_url` and `verified_on`: `data/legal-framework.csv`
> Search: `python scripts/search.py legal --jurisdiction "Chile"`

**EN 301 549 versions.** v3.2.1 (2021-03) points to WCAG 2.1 A and AA and is the version cited under the Web Accessibility Directive. ETSI published **v4.1.1 on 2026-09-02**, which moves the web requirements to WCAG 2.2 A and AA. A harmonised standard gives a presumption of conformity under the EAA only once its reference is published in the Official Journal of the EU; as of 2026-11-15 that is not confirmed for v4.1.1 (or for any version under Directive 2019/882). Do not say v4.1.1 already gives a presumption of conformity.

**EAA**: the Directive **applies since 28 June 2025** to digital products and services for EU consumers (e-commerce, banking, transport, e-books, streaming), with a microenterprise exemption for services and the Art. 32 transitional measures, which include: a period ending 28 June 2030 during which providers may keep providing services with products they lawfully used for similar services before 28 June 2025; service contracts agreed before that date, which continue without alteration until they expire (at most until 28 June 2030); and self-service terminals, which may stay in use until the end of their economically useful life and never more than 20 years after entry into use if the Member State allows it. Check national transposition. Companies selling only to other businesses (B2B) are generally outside its consumer-facing scope; check the Directive and national law.

**When a law fixes WCAG 2.1** (for example the US Title II rule), meet that version as the legal floor. Because WCAG 2.2 conforms to 2.1 (W3C), building to 2.2 AA satisfies it; the only criterion not carried over is 4.1.1 Parsing, which 2.2 removed; the WCAG 2.1 change log says 4.1.1 "should be considered as always satisfied for any content using HTML or XML" ([WCAG 2.1](https://www.w3.org/TR/WCAG21/)). Say which version applies to each requirement.
