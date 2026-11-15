# Inclusive practice: disability models, research, handoff and AI

Models of disability and inclusive language, inclusive user research, the designer-to-developer handoff, and how to use AI assistants without over-trusting them.

## Disability Models & Inclusive Mindset

Design decisions depend on which model of disability you implicitly assume. Prefer **Social** and **Human Rights (CRPD)** models; use **Biopsychosocial (WHO ICF)** when discussing context and interaction.

| Model | View | Design implication |
|-------|------|--------------------|
| **Medical** | Impairment to fix | Assistive devices; risk of pathologizing users |
| **Social** | Barriers disable people, not impairments | Remove barriers; universal design |
| **Biopsychosocial (ICF)** | Interaction of body, activity, participation, environment | Consider context & situational limitations |
| **Human Rights (CRPD)** | Access is a right | Accessibility is mandatory, not charity |
| **Charity** (avoid) | Pity-driven | Paternalistic design |
| **Identity / Affirmative** | Disability as valued identity | Co-design with disabled users |

> Full table: `data/disability-models.csv`

**Language**: use person-first ("person with a disability") or identity-first ("Deaf person", "autistic person") as the community prefers; avoid "suffers from", "wheelchair-bound", "handicapped", "special needs", "normal".

**Global statistics (WHO 2023)**: ~1.3 billion people — 16% of the world's population — live with a significant disability. Plan for permanent, temporary, and situational impairments.

---

## Inclusive Research & Interviews

- Recruit across disability categories: vision (blind, low-vision, color-blind), hearing (Deaf, HoH), motor (switch, voice, limited dexterity), cognitive (dyslexia, ADHD, memory), speech, seizure sensitivity.
- Ask about **assistive tech** (AT), customization (zoom level, magnifier, reduced motion) and environment (lighting, bandwidth, noise).
- Provide accessible recruitment materials (captioned videos, plain language, screen-reader-friendly forms).
- Offer **choice of modality** (video with captions, audio only, async written, in-person).
- Compensate equitably; avoid extractive research.
- Reflect findings back to participants; credit collaboration.

**Consent**: explicit recorded consent; right to pause/withdraw without penalty.

---

## Designer → Developer Handoff

Handoff artifacts a designer must include:
- **Semantic structure**: headings, landmarks, lists marked in the design
- **Focus order**: numbered arrows through interactive elements
- **Keyboard spec**: which keys do what for each custom component
- **ARIA annotations**: role, accessible name, states
- **Component states**: default / hover / active / focus / selected / disabled / error
- **Contrast-audited tokens**: every pair with ratio documented
- **Motion**: `prefers-reduced-motion` alternative
- **Target size**: ≥ 24×24 CSS px (ideally 44×44 for touch)
- **Errors & status**: inline + live region pattern

> Full phase-by-phase checklist: `data/handoff-checklist.csv` (Research → Design → Dev → QA → Release).

What each of these decisions requires and a wireframe/mockup review checklist: [design-phase.md](design-phase.md).

---

## AI-Assisted Accessible Development

- **Generate alt text drafts** with vision models; review & edit — never ship unreviewed.
- **Explain ARIA patterns** but verify against the [APG](https://www.w3.org/WAI/ARIA/apg/) — LLMs can hallucinate roles/states.
- **Translate WCAG to user stories**: convert each failing SC to acceptance criteria.
- **Summarize audit findings** into exec-friendly language while preserving SC IDs.
- **Accessibility code review**: use LLMs to flag likely issues (missing labels, `div`-as-button, color-only meaning) as a *supplement*, not a replacement, for real testing.
- **Caution**: LLMs often suggest ARIA where semantic HTML would be correct. Apply Rule #1 of ARIA.
