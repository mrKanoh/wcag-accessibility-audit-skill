# Templates, prompts, examples and resources

What each template, prompt and component example is for, and the core external references (standards, guides, research, communities, libraries, testing tools, disability models).

## Contents

- [Templates & Prompts](#templates--prompts)
  - [Templates (ready to fill)](#templates-ready-to-fill)
  - [Prompts (copy & paste into your assistant)](#prompts-copy--paste-into-your-assistant)
  - [Accessible component examples (`examples/components/`)](#accessible-component-examples-examplescomponents)
- [Comprehensive Resource Repository](#comprehensive-resource-repository)
- [Core References](#core-references)
  - [Official Standards & Specifications](#official-standards--specifications)
  - [Practical Guides (2024–2025)](#practical-guides-20242025)
  - [Academic Research](#academic-research)
  - [Blogs & Communities](#blogs--communities)
  - [Component Libraries & Pattern Libraries](#component-libraries--pattern-libraries)
  - [Testing & Automation](#testing--automation)
  - [Human Rights & Disability Models](#human-rights--disability-models)

---

## Templates & Prompts

### Templates (ready to fill)

| File | Purpose |
|------|---------|
| `templates/audit-report.md` | Complete audit report with finding blocks, severity scale, conformance table, retest plan |
| `templates/site-audit-workbook.md` | Site-audit evidence workbook: scope, page/state inventory, criterion matrix, findings (see `references/site-audit-procedure.md`) |
| `templates/a11y-ci.yml` | GitHub Actions pipeline: jest-axe + axe CLI + pa11y-ci + Playwright + Lighthouse |
| `templates/vpat-2.5-template.md` | Unofficial template based on the VPAT 2.5 structure (not the official ITI VPAT) — covers WCAG 2.x (A/AA/AAA), Section 508, EN 301 549 |

### Prompts (copy & paste into your assistant)

| File | When to use |
|------|-------------|
| `prompts/audit-component.md` | Get a full a11y audit of a component with WCAG SC + code fixes |
| `prompts/sc-to-acceptance-criteria.md` | Convert WCAG success criteria to Gherkin ACs for a user story |
| `prompts/generate-alt-text.md` | Draft alt text for informative or complex images |
| `prompts/review-figma-handoff.md` | Review a design handoff for a11y gaps before dev |
| `prompts/summarize-audit-findings.md` | Exec-friendly summary of raw findings with 90-day plan |
| `prompts/generate-aria-pattern.md` | Generate reference code for an accessible widget in any framework (review and test before shipping) |
| `prompts/remediate-legacy-code.md` | Audit + fix legacy HTML/jQuery/Bootstrap code for accessibility |
| `prompts/generate-vpat-entry.md` | Translate audit findings into VPAT ACR language |
| `prompts/test-with-screen-reader.md` | Generate step-by-step NVDA/VoiceOver/TalkBack test scripts |
| `prompts/mobile-a11y-checklist.md` | React Native, SwiftUI, Jetpack Compose accessibility checklist |
| `prompts/inclusive-ux-writing.md` | Review UI copy for plain language and inclusive terminology |
| `prompts/design-tokens-audit.md` | Audit Figma/Style Dictionary tokens against WCAG contrast requirements |

### Accessible component examples (`examples/components/`)

Patterns as named in `examples/components/README.md` (combobox: as named in the file itself). See that README for features and limits; none of them records a screen reader test.

| File | What it demonstrates |
|------|---------------------|
| `examples/components/date-picker.html` | Full date picker: dialog pattern, roving tabindex, Arrow/Page/Home/End keys, typed input, live region errors |
| `examples/components/toast-notifications.html` | Toast system: `role="status"` (polite) + `role="alert"` (assertive), dismiss, reduced-motion support |
| `examples/components/carousel.html` | Carousel — WAI-ARIA Carousel Pattern |
| `examples/components/tree-view.html` | Tree View — WAI-ARIA Tree Pattern |
| `examples/components/tabs.html` | Tabs — WAI-ARIA Tabs Pattern |
| `examples/components/media-player.html` | Custom Media Player |
| `examples/components/data-grid.html` | Sortable, filterable data table (native `<table>`, not an ARIA grid) |
| `examples/components/combobox.html` | Combobox / Autocomplete — WAI-ARIA Combobox Pattern (1.2) |

---

## Comprehensive Resource Repository

📚 **See [`RESOURCES.md`](../RESOURCES.md) for a complete, curated repository of:**
- Official W3C/WAI standards & guidelines
- Practical implementation guides (2024–2025)
- Academic research & systematic reviews
- Blogs, communities & education
- Testing tools & frameworks (axe, WAVE, Lighthouse, etc.)
- Recommended books & courses
- Legal frameworks by jurisdiction
- Case studies & accessible websites

---

## Core References

### Official Standards & Specifications

- [WCAG 2.2 Recommendation](https://www.w3.org/TR/WCAG22/) — Official W3C standard
- [WCAG 2.2 Quick Reference](https://www.w3.org/WAI/WCAG22/quickref/) — Filterable by level, principle
- [Understanding WCAG 2.2](https://www.w3.org/WAI/WCAG22/Understanding/) — Detailed explanations & techniques
- [WAI-ARIA Authoring Practices Guide (APG)](https://www.w3.org/WAI/ARIA/apg/) — 25+ component patterns with code
- [WCAG Evaluation Methodology (WCAG-EM)](https://w3c.github.io/wai-wcag-em/) — Structured audit framework
- [WCAG2Mobile](https://www.w3.org/WAI/mobile/) — Applying WCAG to mobile apps
- [WCAG2ICT](https://w3c.github.io/wcag2ict/) — Applying WCAG to non-web ICT

### Practical Guides (2024–2025)

- [AllAccessible: WCAG 2.2 Complete Compliance Guide](https://www.allaccessible.org/blog/wcag-22-complete-guide-2025) — 9 new criteria patterns
- [Deque: Beginner's Guide to Web Accessibility](https://www.deque.com/web-accessibility-beginners-guide/) — Entry-level foundations
- [Usercentrics: Mastering WCAG 2.2 & Inclusive Design](https://usercentrics.com/knowledge-hub/mastering-web-app-accessibility-wcag2-2-and-inclusive-design/)

### Academic Research

- [Accessibility Engineering: Systematic Literature Review (152 papers)](https://pmc.ncbi.nlm.nih.gov/articles/PMC9881526/) — 2010–2021 methodologies
- [WCAG 2.2 & ADA 2024: Policy Impact (PRISMA 2020)](https://www.researchgate.net/publication/396366120_Policy_in_Practice_A_Systematic_Review_of_WCAG_22_and_ADA_2024_Effects_on_Web_and_Mobile_Accessibility) — Regulatory compliance effects
- [Cognitive Disabilities: Rapid Evidence Assessment](https://pmc.ncbi.nlm.nih.gov/articles/PMC8869505/) — Specific needs & WCAG gaps
- [Web Accessibility in Universities (UK Study)](https://journals.sagepub.com/doi/full/10.1177/21582440211056614) — 349 institutions; 80% below AA
- [How WCAG Compliance Shapes User Experience](https://www.sciencedirect.com/science/article/pii/S1071581922001756) — Evidence on real-world impact

### Blogs & Communities

- [WebAIM](https://webaim.org/) — 25 years of free resources, 1 monthly newsletter
- [WebAIM Blog](https://webaim.org/blog/feed/) — Weekly updates on standards & tools
- [The A11Y Project](https://www.a11yproject.com/) — Community, events, curriculum
- [Inclusive Components (Heydon Pickering)](https://inclusive-components.design/) — Component patterns with inclusivity focus
- [Paul J. Adam](https://pauljadam.com/) — Specialist in web & mobile accessibility
- [Deque: Accessible Design Hub](https://www.deque.com/accessible-design/)

### Component Libraries & Pattern Libraries

- [WAI-ARIA Authoring Practices Guide (APG)](https://www.w3.org/WAI/ARIA/apg/) — 25+ patterns with live examples
- [React Aria (Adobe)](https://react-spectrum.adobe.com/react-aria/) — Accessible React components & hooks
- [Radix UI](https://www.radix-ui.com/) — Unstyled, accessible component library
- [USWDS (US Web Design System)](https://designsystem.digital.gov/) — Government standards
- [Inclusive Components](https://inclusive-components.design/) — Design-first patterns

### Testing & Automation

- [axe-core (Deque)](https://github.com/dequelabs/axe-core) — De facto standard automated testing engine
- [WAVE (WebAIM)](https://wave.webaim.org/) — Visual accessibility feedback
- [Lighthouse (Google)](https://developers.google.com/web/tools/lighthouse) — Built into Chrome
- [pa11y](https://pa11y.org/) — CLI & CI integration
- [jest-axe](https://github.com/nickcolley/jest-axe) — Jest + Testing Library integration
- [@axe-core/playwright](https://github.com/dequelabs/axe-core-npm/tree/develop/packages/playwright) — Playwright integration
- [cypress-axe](https://github.com/component-driven/cypress-axe) — Cypress integration

### Human Rights & Disability Models

- [UN Convention on the Rights of Persons with Disabilities (CRPD)](https://www.un.org/development/desa/disabilities/convention-on-the-rights-of-persons-with-disabilities.html) — Legal framework
- [WHO International Classification of Functioning (ICF)](https://www.who.int/standards/classifications/international-classification-of-functioning-disability-and-health) — Biopsychosocial model
- [Disability Models in Design (Social, Medical, Identity-First)](https://www.a11yproject.com/) — Frameworks for inclusive thinking
