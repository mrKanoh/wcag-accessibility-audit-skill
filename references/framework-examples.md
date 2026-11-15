# Framework code examples (web)

Accessible patterns written for specific web frameworks: Next.js, Angular, Svelte, Astro, SolidJS and Vue 3. Each snippet says whether it was compiled or checked against documentation.

## Contents

- [Stack-Specific Code Examples](#stack-specific-code-examples)
  - [Next.js App Router — Focus management on navigation](#nextjs-app-router--focus-management-on-navigation)
  - [Angular — Accessible reactive form](#angular--accessible-reactive-form)
  - [Svelte 5 — Modal dialog with native `<dialog>`](#svelte-5--modal-dialog-with-native-dialog)
  - [Astro — Accessible island with ARIA](#astro--accessible-island-with-aria)
  - [SolidJS — Accessible toggle button](#solidjs--accessible-toggle-button)
- [Vue 3 Accessibility Examples](#vue-3-accessibility-examples)
  - [Accessible reactive form (Composition API)](#accessible-reactive-form-composition-api)
  - [Accessible modal (Vue 3 + native `<dialog>`)](#accessible-modal-vue-3--native-dialog)
  - [Accessible toggle button (Vue 3)](#accessible-toggle-button-vue-3)
  - [Live region (Vue 3)](#live-region-vue-3)

---

## Stack-Specific Code Examples

### Next.js App Router — Focus management on navigation
Next.js already ships a route announcer for client-side transitions (`next/link`): it reads `document.title`, then the `<h1>`, then the pathname (<https://nextjs.org/docs/architecture/accessibility>, checked 2026-11-06). Do not add a second live region for the same announcement. Give every page a unique, descriptive title; that is what gets announced. If you also want focus to move to the new page's heading (a design choice, not a WCAG requirement), use a small client component and test with a screen reader that title announcement plus the heading read-out is not too verbose:
```tsx
// app/route-focus.tsx — render <RouteFocus /> once inside <body> in app/layout.tsx
'use client';
import { usePathname } from 'next/navigation';
import { useEffect, useRef } from 'react';

export function RouteFocus() {
  const pathname = usePathname();
  const prevPathname = useRef(pathname);

  useEffect(() => {
    // Only act when the path actually changed; this also survives React Strict Mode,
    // which runs effects twice in development and would defeat a "first render" flag.
    if (prevPathname.current === pathname) return;
    prevPathname.current = pathname;
    const h1 = document.querySelector<HTMLElement>('main h1');
    if (h1) {
      h1.setAttribute('tabindex', '-1'); // focusable by script, not in the tab order
      h1.focus();
    }
  }, [pathname]);

  return null;
}
```
The component assumes each page renders a `<main id="main-content">` containing one `<h1>`, with the skip link before it; `app/layout.tsx` stays a Server Component so it can still export `metadata`:
```tsx
// app/layout.tsx (excerpt)
<body>
  <a href="#main-content" className="skip-link">Skip to main content</a>
  <RouteFocus />
  <main id="main-content">{children}</main> {/* each page renders its own <h1> */}
</body>
```

### Angular — Accessible reactive form
```typescript
// login.component.ts
import { Component } from '@angular/core';
import { ReactiveFormsModule, FormBuilder, Validators } from '@angular/forms';

@Component({
  selector: 'app-login',
  standalone: true,
  imports: [ReactiveFormsModule],
  template: `
    <form [formGroup]="form" (ngSubmit)="submit()" novalidate>
      <div>
        <label for="email">Email <span aria-hidden="true">*</span></label>
        <input
          id="email"
          type="email"
          formControlName="email"
          autocomplete="email"
          [attr.aria-invalid]="email.invalid && email.touched"
          [attr.aria-describedby]="email.invalid && email.touched ? 'email-error' : null"
          aria-required="true"
        />
        @if (email.invalid && email.touched) {
          <span id="email-error" role="alert">
            {{ email.hasError('required') ? 'Email is required' : 'Enter a valid email' }}
          </span>
        }
      </div>
      <button type="submit">Log in</button>
    </form>
  `
})
export class LoginComponent {
  form = this.fb.group({ email: ['', [Validators.required, Validators.email]] });
  get email() { return this.form.controls.email; }
  constructor(private fb: FormBuilder) {}
  submit() {
    if (this.form.invalid) {
      this.form.markAllAsTouched();                 // reveal every error on submit
      document.getElementById('email')?.focus();    // with several fields, focus the first invalid one
      return;
    }
    /* … */
  }
}
```
Do not disable the submit button while the form is invalid: a disabled button hides why the form cannot be sent. Let the user submit and show the errors. `@if` is Angular's built-in template control flow and needs no import. It was introduced in Angular 17 as a developer preview and is stable from Angular 18 (blog.angular.dev/introducing-angular-v17-4d7033312e4b and angular.dev/roadmap, checked 2026-11); on older versions add `NgIf` to `imports` and use `*ngIf`. Not compiled; syntax per angular.dev/guide/templates/control-flow.

### Svelte 5 — Modal dialog with native `<dialog>`
```svelte
<script>
  import { onMount } from 'svelte';
  let { open = false, onClose } = $props();
  let dialogEl;

  $effect(() => {
    if (open) dialogEl?.showModal();
    else dialogEl?.close();
  });
</script>

<dialog
  bind:this={dialogEl}
  aria-labelledby="dialog-title"
  aria-describedby="dialog-desc"
  on:close={onClose}
  on:click|self={onClose}
>
  <h2 id="dialog-title">Confirm action</h2>
  <p id="dialog-desc">This cannot be undone.</p>
  <menu>
    <li><button on:click={onClose}>Cancel</button></li>
    <li><button class="primary">Confirm</button></li>
  </menu>
</dialog>

<!-- showModal() makes the page behind inert. Initial focus follows the HTML dialog focusing steps (an autofocus element, else the dialog's focus delegate, else the dialog). On close, the HTML spec's close steps restore focus to the element that was focused before opening (html.spec.whatwg.org, interactive elements, checked 2026-11), but MDN does not state it: verify Tab, Escape, initial focus and focus return in your target browsers, and choose the initial focus for your content and task. closedby="any" (light dismiss) has limited browser support: check it before relying on it. Not compiled. -->
```

### Astro — Accessible island with ARIA
```astro
---
// Card.astro
export interface Props { title: string; href: string; description: string; }
const { title, href, description } = Astro.props;
---
<article aria-labelledby={`card-title-${title.replace(/\s/g,'-')}`}>
  <h3 id={`card-title-${title.replace(/\s/g,'-')}`}>
    <a href={href}>{title}</a>
  </h3>
  <p>{description}</p>
</article>
```

### SolidJS — Accessible toggle button
```tsx
import { createSignal } from 'solid-js';

export function ThemeToggle() {
  const [isDark, setIsDark] = createSignal(false);

  const toggle = () => {
    const next = !isDark();
    setIsDark(next);
    document.documentElement.dataset.theme = next ? 'dark' : 'light';
  };

  return (
    <button
      type="button"
      aria-pressed={isDark()}
      onClick={toggle}
    >
      <span aria-hidden="true">{isDark() ? '🌙' : '☀️'}</span> Dark mode
    </button>
  );
}
```

---

## Vue 3 Accessibility Examples

### Accessible reactive form (Composition API)
```vue
<script setup lang="ts">
import { ref, computed } from 'vue';

const email = ref('');
const touched = ref(false);
const isInvalid = computed(() => touched.value && !/^[^@]+@[^@]+\.[^@]+$/.test(email.value));
const errorId = 'email-error';
const hintId  = 'email-hint';
</script>

<template>
  <form @submit.prevent="handleSubmit" novalidate>
    <div>
      <label for="email">
        Email address <span aria-hidden="true">*</span>
      </label>
      <input
        id="email"
        v-model="email"
        type="email"
        autocomplete="email"
        aria-required="true"
        :aria-invalid="isInvalid || undefined"
        :aria-describedby="[hintId, isInvalid ? errorId : ''].filter(Boolean).join(' ')"
        @blur="touched = true"
      />
      <span :id="hintId">We will never share your email.</span>
      <span
        v-if="isInvalid"
        :id="errorId"
        role="alert"
      >
        Enter a valid email address.
      </span>
    </div>
    <button type="submit" :disabled="isInvalid">Subscribe</button>
  </form>
</template>
```

### Accessible modal (Vue 3 + native `<dialog>`)
```vue
<script setup lang="ts">
import { ref, watch, onMounted } from 'vue';
const props = defineProps<{ open: boolean }>();
const emit  = defineEmits<{ (e: 'close'): void }>();
const dialogEl = ref<HTMLDialogElement | null>(null);

// showModal() makes the page behind inert and contains Tab; Escape fires `cancel` then `close`.
// On close, the HTML spec's close steps restore focus to the element focused before showModal();
// MDN does not state it, so verify focus return in your target browsers.
function sync(val: boolean) {
  const el = dialogEl.value;
  if (!el) return;
  if (val && !el.open) el.showModal();
  else if (!val && el.open) el.close();
}
onMounted(() => sync(props.open));          // the component may mount with open = true
watch(() => props.open, sync);

// Emit only from the dialog's own `close` event (Escape, Cancel and backdrop all end up there).
// The parent sets open = false; sync() then finds the dialog already closed, so there is no second emit.
function requestClose() { dialogEl.value?.close(); }

// Click on the backdrop targets the <dialog> itself (the content lives in the inner div)
function onBackdropClick(e: MouseEvent) {
  if (e.target === dialogEl.value) requestClose();
}
</script>

<template>
  <dialog
    ref="dialogEl"
    aria-labelledby="modal-title"
    aria-describedby="modal-desc"
    @close="emit('close')"
    @click="onBackdropClick"
  >
    <div>
      <h2 id="modal-title">Confirm action</h2>
      <p id="modal-desc">This cannot be undone.</p>
      <button type="button" autofocus @click="requestClose">Cancel</button>
      <button type="button" class="primary">Confirm</button>
    </div>
  </dialog>
</template>
```
Same pattern as the Svelte example above: no Teleport or hand-written focus trap is needed because `showModal()` puts the dialog in the top layer. `autofocus` on Cancel (the least destructive action, because this cannot be undone) is a choice per task. Inert background, Escape and the `close` event are documented on MDN; focus return on close is defined in the HTML spec's close steps but not stated on MDN, so verify Tab, Escape and focus return in your target browsers, and if the opener is removed from the DOM while the dialog is open, move focus to a logical element yourself. The backdrop click handler is ours: `showModal()` does not close on outside clicks by default (`closedby="any"` is the native alternative, with limited browser support: check it before relying on it). Not compiled; verified against developer.mozilla.org/docs/Web/HTML/Reference/Elements/dialog (2026-11).

### Accessible toggle button (Vue 3)
```vue
<script setup lang="ts">
import { ref } from 'vue';
const isDark = ref(false);
function toggle() {
  isDark.value = !isDark.value;
  document.documentElement.dataset.theme = isDark.value ? 'dark' : 'light';
}
</script>

<template>
  <button
    type="button"
    :aria-pressed="isDark"
    @click="toggle"
  >
    <span aria-hidden="true">{{ isDark ? '🌙' : '☀️' }}</span> Dark mode
  </button>
</template>
```

### Live region (Vue 3)
```vue
<script setup lang="ts">
import { ref } from 'vue';
const announcement = ref('');
function save() {
  // ... save logic ...
  announcement.value = 'Document saved successfully.';
  setTimeout(() => { announcement.value = ''; }, 3000);
}
</script>

<template>
  <!-- Visually hidden live region -->
  <div aria-live="polite" aria-atomic="true" class="sr-only">
    {{ announcement }}
  </div>
  <button type="button" @click="save">Save</button>
</template>
```
