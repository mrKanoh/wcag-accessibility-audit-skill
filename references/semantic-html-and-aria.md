# Semantic HTML and WAI-ARIA

Native HTML elements first, then the ARIA roles, states and properties to use when no native element provides the semantics.

## Semantic HTML First

**Rule of thumb**: semantic HTML > ARIA. Only reach for ARIA when no native element provides the semantics.

```html
<header>       <!-- role=banner at top-level -->
<nav aria-label="Primary">
<main>         <!-- exactly one per page -->
<aside>        <!-- role=complementary -->
<footer>       <!-- role=contentinfo at top-level -->
<section aria-labelledby="h">  <!-- region if labeled -->
<article>
<h1>…<h6>      <!-- never skip levels; one h1 per page -->
<button type="button">   <!-- actions -->
<a href="/x">            <!-- navigation -->
<ul><li>        <dl><dt><dd>
<table><caption><thead><th scope="col">
<label for="id">  <fieldset><legend>
<details><summary>        <!-- native disclosure -->
<dialog>                  <!-- showModal(): page behind becomes inert; check Tab and Escape in your target browsers -->
```

**Common mistake**: using `<div onclick>` for a button — breaks keyboard, SR, and focus. Always prefer `<button>`.

> Full element reference: `data/semantic-html.csv`

---

## WAI-ARIA Quick Reference

### Three rules of ARIA
1. Don't use ARIA if a native element exists.
2. Don't change native semantics unless you really must.
3. All interactive ARIA controls must be keyboard-operable and have an accessible name.

### Essential roles
```html
role="dialog"      aria-modal="true"
role="alertdialog"
role="alert"                             <!-- assertive live region -->
role="status"                            <!-- polite live region -->
role="tablist" role="tab" role="tabpanel"
role="combobox" role="listbox" role="option"
role="grid" role="row" role="gridcell"
role="progressbar" role="slider" role="switch"
role="tree" role="treeitem"
role="menu" role="menuitem"
```
`role="menu"` is for application menus; for site navigation use `nav` + a list of links, with a disclosure button (`aria-expanded`, `aria-controls`) for submenus ([APG Disclosure Navigation](https://www.w3.org/WAI/ARIA/apg/patterns/disclosure/examples/disclosure-navigation/): the menu role implies complex, application-style keyboard behaviour that assistive technology expects and that site navigation neither provides nor needs). A `<select>` that navigates as soon as its value changes causes a change of context that fails 3.2.2 unless the user is told beforehand ([G13](https://www.w3.org/WAI/WCAG22/Techniques/general/G13)); a «Go» submit button ([G80](https://www.w3.org/WAI/WCAG22/Techniques/general/G80)) is the robust option. See [Understanding 3.2.2](https://www.w3.org/WAI/WCAG22/Understanding/on-input.html).

### Essential properties & states
```html
aria-label="Close"
aria-labelledby="heading-id"
aria-describedby="hint-id"
aria-expanded="true|false"
aria-selected="true|false"
aria-checked="true|false|mixed"
aria-hidden="true"                 <!-- never on focusable elements -->
aria-live="polite|assertive"
aria-invalid="true"
aria-required="true"
aria-modal="true"
aria-disabled="true"
aria-sort="ascending|descending"
aria-current="page|step|date|true"
aria-haspopup="menu|listbox|dialog|grid|tree"
aria-activedescendant="id"
aria-controls="id"
aria-owns="id"
```

> Full component patterns: `data/aria-patterns.csv`
