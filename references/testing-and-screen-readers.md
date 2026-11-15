# Testing: automation, manual checks and screen readers

Recipes for automated checks (CLI, unit, end-to-end, Storybook, CI) and quickstarts for the main screen readers.

## Contents

- [Testing: Automation + Manual](#testing-automation--manual)
  - [Automated — recipes](#automated--recipes)
  - [Jest + Testing Library + jest-axe](#jest--testing-library--jest-axe)
  - [Playwright + axe](#playwright--axe)
  - [Cypress + cypress-axe](#cypress--cypress-axe)
  - [Storybook a11y addon](#storybook-a11y-addon)
  - [GitHub Actions](#github-actions)
- [Screen Reader Testing](#screen-reader-testing)
  - [NVDA quickstart (Windows)](#nvda-quickstart-windows)
  - [VoiceOver (macOS) — VO = Control+Option](#voiceover-macos--vo--controloption)
  - [VoiceOver (iOS)](#voiceover-ios)
  - [TalkBack (Android)](#talkback-android)

---

## Testing: Automation + Manual

### Automated — recipes

```bash
# axe-core CLI
npx @axe-core/cli https://example.com --tags wcag2a,wcag2aa,wcag21a,wcag21aa,wcag22aa

# pa11y (wraps axe + HTML_CodeSniffer)
npx pa11y https://example.com --standard WCAG2AA

# Lighthouse
npx lighthouse https://example.com --only-categories=accessibility
```

### Jest + Testing Library + jest-axe
```ts
import { render } from '@testing-library/react';
import { axe, toHaveNoViolations } from 'jest-axe';
expect.extend(toHaveNoViolations);

test('modal has no a11y violations', async () => {
  const { container } = render(<MyModal open />);
  expect(await axe(container)).toHaveNoViolations();
});
```

### Playwright + axe
```ts
import { test } from '@playwright/test';
import AxeBuilder from '@axe-core/playwright';

test('homepage has no axe violations for the selected rules', async ({ page }) => {
  await page.goto('/');
  const results = await new AxeBuilder({ page })
    .withTags(['wcag2a', 'wcag2aa', 'wcag21a', 'wcag21aa', 'wcag22aa'])
    .analyze();
  expect(results.violations).toEqual([]);
});
```

### Cypress + cypress-axe
```js
cy.visit('/');
cy.injectAxe();
cy.checkA11y(null, { runOnly: { type: 'tag', values: ['wcag2a', 'wcag2aa', 'wcag21a', 'wcag21aa', 'wcag22aa'] } });
```

### Storybook a11y addon
```js
// .storybook/main.js
export default { addons: ['@storybook/addon-a11y'] };
```

### GitHub Actions
```yaml
- name: a11y tests
  run: |
    npm ci
    npm test -- --testPathPatterns=a11y   # Jest 30 flag (plural); Jest 29 and older: --testPathPattern
    npx playwright test --grep @a11y
```

> Reminder: automated scans catch ~20–40% of issues. Always pair with keyboard and real AT.

---

## Screen Reader Testing

| Reader | OS | Pair with | Cost |
|--------|-----|-----------|------|
| **NVDA** | Windows | Firefox or Chrome | Free |
| **JAWS** | Windows | Chrome or Edge | Paid |
| **Narrator** | Windows | Edge | Built-in |
| **VoiceOver** | macOS / iOS | Safari | Built-in |
| **TalkBack** | Android | Chrome | Built-in |

### NVDA quickstart (Windows)
- **Insert** is the NVDA modifier key (or CapsLock in laptop layout).
- **Ctrl** silences speech.
- **H / Shift+H** next/previous heading.
- **F / B / L / T / K** next form field / button / list / table / link.
- **Insert+F7** elements list (headings, links, form fields).
- **Insert+Space** toggle browse / focus mode.

### VoiceOver (macOS) — VO = Control+Option
- **VO+Right/Left** next/prev element
- **VO+U** rotor (headings, links, form controls…)
- **VO+Space** activate
- **VO+Command+H** next heading
- **VO+Shift+M** context menu

### VoiceOver (iOS)
- Swipe right/left → navigate; double-tap → activate
- Three-finger swipe → scroll
- Two-finger rotation → rotor
- Three-finger triple-tap → screen curtain

### TalkBack (Android)
- Swipe right/left → navigate
- Double-tap → activate
- Two-finger swipe → scroll
- Swipe up then right → global context menu

> Full shortcut catalog: `data/screen-reader-keys.csv`
