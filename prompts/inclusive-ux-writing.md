# Prompt: Inclusive UX writing review

Use when you want the assistant to review UI copy (labels, errors, CTAs, microcopy)
for plain language, inclusive terminology, and cognitive accessibility.

---

## Prompt (copy & paste)

```
Review the following UI copy for inclusive language and plain language principles.

For each text string, evaluate:
1. **Reading level** — is it ≤ 8th grade? Rewrite if not.
2. **Inclusive language** — does it avoid ableist, gendered, or exclusionary terms?
3. **Error messages** — do they explain what happened AND what to do next?
4. **Action labels** — are CTAs specific? (not "Click here" or "Submit")
5. **Cognitive load** — is it the shortest way to say this? Remove filler words.
6. **Assumptions** — does the copy assume able-bodiedness, tech literacy, or specific devices?

**Inclusive language checks:**
- Avoid: "sanity check", "blind spot", "dummy data", "master/slave", "whitelist/blacklist"
- Prefer: "quick check", "gap", "sample data", "primary/replica", "allowlist/blocklist"
- Avoid ableist metaphors: "falls on deaf ears", "turn a blind eye", "lame"
- Use person-first OR identity-first language as the community prefers
- Avoid gendered defaults: "he or she" → "they"; "guys" → "everyone" / "folks"
- Avoid cultural assumptions: not everyone has a "zip code", "social security number", or "credit score"

**Error message formula:**
[What went wrong] + [Why if non-obvious] + [Exactly what to do next]
Bad: "Invalid input"
Good: "Email address is missing the @ symbol. Check your email and try again."

**CTA formula:**
[Verb] + [Object] + [Context if needed]
Bad: "Submit" | "Click here" | "Learn more"
Good: "Create your account" | "Download accessibility guide (PDF, 2MB)" | "Read our refund policy"

**Copy to review:**
[PASTE UI COPY HERE — labels, errors, placeholders, tooltips, CTAs]
```

---

## Tips

- Review in batches of 10–20 strings for best output quality.
- Include context: where does this copy appear? What's the user trying to do?
- For error messages, also verify the technical implementation uses `role="alert"`.
- If reviewing Spanish copy, give the assistant `data/glossary-es.csv` (or the relevant terms)
  when it cannot read repository files.
