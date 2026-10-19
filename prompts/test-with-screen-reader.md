# Prompt: Step-by-step screen reader test script

Use when you need to run a structured manual test with NVDA, VoiceOver, or TalkBack
and want the assistant to generate a reproducible test script.

---

## Prompt (copy & paste)

```
Generate a step-by-step screen reader test script for the following component/flow.

**Screen reader:** [NVDA + Firefox / VoiceOver + Safari / TalkBack + Chrome]
**Component/flow:** [e.g., "login form", "checkout flow steps 1–3", "navigation menu"]
**URL or description:** [URL or paste markup]

For each test step provide:
1. **Action**: exactly what the tester does (key press or gesture)
2. **Expected announcement**: what the screen reader should say verbatim (or describe)
3. **Pass/Fail criteria**: what counts as passing
4. **WCAG SC**: the criterion this step verifies

**Structure the script in these sections:**
- Page entry (page title announced, skip link present)
- Landmark navigation (navigate by regions)
- Heading structure (navigate by headings)
- Interactive elements (each button, link, input)
- Form interaction (fill, validate, submit)
- Dynamic content (modals, alerts, toasts, live regions)
- Error states (trigger each error, verify announcement)

**Format each test case as:**
## TC-[N]: [Short description]
- Keys: [exact keys]
- Expected: "[exact announcement]"
- Criterion: [SC ID]
- Notes: [any NVDA/VO-specific quirks]

**Screen reader key reference:**
- NVDA browse mode: H (heading), B (button), F (form field), Tab (focusable)
- NVDA insert+F7: elements list
- VoiceOver: VO+Right (next), VO+U (rotor), VO+Space (activate)
- TalkBack: swipe right (next), double-tap (activate)
```

---

## Tips

- Run one section at a time for complex flows.
- Use NVDA 2023.x with Firefox (most commonly tested pair for WCAG conformance).
- Record the actual announcement vs expected for your audit report.
- Check `data/screen-reader-keys.csv` for complete shortcut reference.
