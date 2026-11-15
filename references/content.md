# Accessible content: titles, language, headings, links, images, tables and media

Read this when you write or review page content, or the templates that produce it: page titles, language, headings, link text, alternative text, lists and tables, instructions, plain language, media and downloadable documents.

Each item says whether it is a **requirement** (a WCAG 2.2 success criterion, with ID, level and the version it entered), a **technique** (a W3C technique: one way to meet a criterion) or **guidance**. Nothing fails WCAG for missing guidance, and AAA criteria are named as AAA. The default target is WCAG 2.2 AA ([legal-framework.md](legal-framework.md)).

## Contents

- [Criteria that apply to content](#criteria-that-apply-to-content)
- [Page title](#page-title)
- [Language of the page and of parts](#language-of-the-page-and-of-parts)
- [Headings and structure](#headings-and-structure)
- [Link purpose](#link-purpose)
- [Text alternatives for images](#text-alternatives-for-images)
- [Lists and data tables](#lists-and-data-tables)
- [Instructions that do not rely on sensory characteristics](#instructions-that-do-not-rely-on-sensory-characteristics)
- [Plain language](#plain-language)
- [Media in brief](#media-in-brief)
- [Downloadable documents](#downloadable-documents)
- [Sources](#sources)

## Criteria that apply to content

"Entered" is the WCAG version that added the criterion, taken from W3C's "What's New in WCAG 2.1" and "What's New in WCAG 2.2" (criteria not listed there come from 2.0).

| ID | Name | Level | Entered | Summary |
|----|------|-------|---------|---------|
| 1.1.1 | Non-text Content | A | 2.0 | Non-text content has a text alternative that serves the equivalent purpose (with listed exceptions) |
| 1.2.1 | Audio-only and Video-only (Prerecorded) | A | 2.0 | A text alternative for prerecorded audio-only; a text alternative or audio track for prerecorded video-only |
| 1.2.2 | Captions (Prerecorded) | A | 2.0 | Captions for all prerecorded audio in synchronized media |
| 1.2.3 | Audio Description or Media Alternative (Prerecorded) | A | 2.0 | Audio description or a text alternative for prerecorded video |
| 1.2.4 | Captions (Live) | AA | 2.0 | Captions for all live audio in synchronized media |
| 1.2.5 | Audio Description (Prerecorded) | AA | 2.0 | Audio description for all prerecorded video in synchronized media |
| 1.3.1 | Info and Relationships | A | 2.0 | Headings, lists, tables and other structure are programmatically determinable |
| 1.3.3 | Sensory Characteristics | A | 2.0 | Instructions do not rely solely on shape, color, size, visual location, orientation or sound |
| 1.4.5 | Images of Text | AA | 2.0 | Real text instead of images of text, unless customizable or essential |
| 2.4.1 | Bypass Blocks | A | 2.0 | A mechanism to skip blocks repeated on multiple pages |
| 2.4.2 | Page Titled | A | 2.0 | Web pages have titles that describe topic or purpose |
| 2.4.4 | Link Purpose (In Context) | A | 2.0 | Link purpose can be determined from the link text, or the text with its programmatically determined context |
| 2.4.6 | Headings and Labels | AA | 2.0 | Headings and labels that exist describe topic or purpose |
| 3.1.1 | Language of Page | A | 2.0 | The default human language of each page is programmatically determinable |
| 3.1.2 | Language of Parts | AA | 2.0 | The language of each passage or phrase is programmatically determinable (with exceptions) |

AAA criteria mentioned below, not part of an AA target: 2.4.9 Link Purpose (Link Only), 2.4.10 Section Headings, 3.1.5 Reading Level.

## Page title

- **Requirement (2.4.2 Page Titled, A, 2.0).** Web pages have titles that describe topic or purpose. Failure F25: a title that does not identify the contents.
- **Technique.** A descriptive title (G88) in the `<title>` element (H25). Identifying where the page sits in the site, such as "Shipping – Help – Example Store", is advisory (G127).
- **Single-page apps.** Understanding 2.4.2: "the title of the page should also be changed dynamically to reflect the content or topic of the current view." How a framework announces the title on route change: [framework-examples.md](framework-examples.md#nextjs-app-router--focus-management-on-navigation).
- **Guidance.** Put the specific part first ("Order 1234 – My account – Example Store"). After a form submission with errors, the WAI Forms tutorial suggests adding the error count to the title ([forms.md](forms.md#error-summary-and-focus)).

## Language of the page and of parts

- **Requirement (3.1.1 Language of Page, A, 2.0).** Set the page's default language with `lang` on `<html>` (technique H57). When a page uses several languages, Understanding 3.1.1 says the default is "the language which is used most" (if used equally, the first one used).
- **Requirement (3.1.2 Language of Parts, AA, 2.0).** Mark passages or phrases in another language with `lang` on the element (technique H58), except proper names, technical terms, words of indeterminate language, and words or phrases that have become part of the vernacular of the surrounding text (such as "rendezvous" in English).
- **Caution.** Understanding 3.1.2 notes that when an element is announced by its accessible name (for example in a list of links), language changes inside it may not be exposed, because accessible names are flat strings. It says this limitation is not a failure; check the markup, not only the spoken output.

```html
<html lang="en">
  …
  <p>The French term <span lang="fr">mise en place</span> means "everything in its place".</p>
</html>
```

## Headings and structure

- **Requirement (1.3.1 Info and Relationships, A, 2.0).** Text that looks like a heading is marked as a heading (`<h1>`–`<h6>`), with levels that reflect the structure; regions are marked with landmarks (`<header>`, `<nav>`, `<main>`, `<aside>`, `<footer>`). Native elements and their ARIA equivalents: [semantic-html-and-aria.md](semantic-html-and-aria.md#semantic-html-first).
- **Requirement (2.4.6 Headings and Labels, AA, 2.0).** Headings that exist describe the topic of their section. Understanding 2.4.6: "This success criterion does not require headings or labels"; it requires that, if provided, they be descriptive. Whether they are marked up is 1.3.1.
- **Requirement (2.4.1 Bypass Blocks, A, 2.0).** Headings and landmarks are among the ways to let users skip repeated blocks, together with a skip link.
- **AAA.** 2.4.10 Section Headings, AAA, 2.0: section headings are used to organize the content. Do not report a page without section headings as an AA failure on that basis; report missing heading markup for visual headings under 1.3.1.
- **Guidance.** One `<h1>` that names the page and no skipped levels are common conventions that help navigation; they are not WCAG requirements by themselves.

## Link purpose

- **Requirement (2.4.4 Link Purpose (In Context), A, 2.0).** The purpose of each link can be determined from its text alone, or from its text together with its programmatically determined link context, except where the purpose would be ambiguous to users in general. In HTML, that context is text in the same sentence, paragraph, list item or table cell as the link, or in a header cell associated with the link's table cell.
- **Techniques.** Descriptive link text (G91, H30); link text plus the enclosing sentence, list item, paragraph or table cell (G53, H77, H78, H79, H81); `aria-labelledby` or `aria-label` to add context (ARIA7, ARIA8); visually hidden text inside the link (C7). The preceding heading as context is advisory only (H80).
- **Failures.** F63 (context only in content unrelated to the link); F89 (an image that is the only content of a link, with no accessible name).
- **AAA.** 2.4.9 Link Purpose (Link Only), AAA: purpose from the link text alone. Under an AA target, "Read more" with good context is not a failure, though more specific text is a useful recommendation.
- Repeated link and button names: [form-labels-and-names.md](form-labels-and-names.md#5-repeated-names-lists-tables-repeated-actions).

## Text alternatives for images

**Requirement (1.1.1 Non-text Content, A, 2.0).** All non-text content presented to the user has a text alternative that serves the equivalent purpose, with the exceptions listed in the criterion (controls and input, time-based media, tests, sensory experiences, CAPTCHA, decoration).

Decision tree, following the WAI Images tutorial's "alt decision tree" (summarized; the tutorial says the tree does not cover every case):

1. **Does the image contain text?**
   - The same text is also present as real text nearby, or the text is only a visual effect → `alt=""` (decorative).
   - The text has a function, such as an icon → `alt` conveys the function (functional).
   - The text is not available any other way → `alt` contains the text (image of text; see 1.4.5 below).
2. **Is the image in a link or button, and would the purpose be unclear without it?** → `alt` conveys the destination or action, not the picture (functional). An image that is the only content of a link needs a name (F89).
3. **Does the image add meaning?**
   - A simple photo or graphic → a short `alt` with that meaning (informative).
   - A chart, diagram or other complex information → a short `alt` plus the full information elsewhere on the page, in text or a data table (complex).
   - It repeats nearby real text → `alt=""`.
4. **Is it purely decorative or not intended for users?** → `alt=""` (or a CSS background).
5. **Not covered or unclear** → see the WAI Images tutorial.

- **Requirement (1.4.5 Images of Text, AA, 2.0).** Use real text rather than images of text, unless the image of text can be visually customized to the user's requirements or a particular presentation is essential. Logotypes are considered essential.
- **Guidance.** Generated alternative text (from an AI model or a CMS) is a draft that a person must review before publishing: `prompts/generate-alt-text.md` and [inclusive-practice.md](inclusive-practice.md#ai-assisted-accessible-development).
- Leaving the `alt` attribute out is not the same as `alt=""`: the decision tree uses an empty `alt` attribute to mark an image as decorative, so give every `<img>` an `alt`, empty or not.

## Lists and data tables

- **Requirement (1.3.1, A, 2.0).** Lists are marked as lists (`<ul>`, `<ol>`, `<dl>`); data tables expose their headers.
- **Technique (WAI Tables tutorial).** Header cells use `<th>` and data cells `<td>`; `scope="col"` or `scope="row"` when the direction is not obvious, `colgroup`/`rowgroup` values for headers that span; `id` and `headers` for multi-level tables that cannot be associated otherwise; a `<caption>` that names the table. The tutorial notes that "as a general rule, tables aren't meant to be used for layout purposes".
- **Guidance.** Prefer splitting a complex table into simpler ones over `headers`/`id` markup. Sortable and interactive tables: `examples/components/data-grid.html`.

```html
<table>
  <caption>Opening hours</caption>
  <thead>
    <tr><th scope="col">Day</th><th scope="col">Opens</th><th scope="col">Closes</th></tr>
  </thead>
  <tbody>
    <tr><th scope="row">Monday</th><td>09:00</td><td>18:00</td></tr>
  </tbody>
</table>
```

## Instructions that do not rely on sensory characteristics

- **Requirement (1.3.3 Sensory Characteristics, A, 2.0).** Instructions for understanding and operating content do not rely solely on shape, color, size, visual location, orientation or sound. "Press the round button" or "the button to the right" alone fails; "Press the Next button (lower right)" adds the name. Failures F14 (identifying content only by shape or location) and F26 (a graphical symbol alone); technique G96.
- Color alone is covered by 1.4.1 Use of Color, A, 2.0 ([design-phase.md](design-phase.md#interactive-states)).

## Plain language

Plain language helps everyone, and especially people with cognitive, language and learning disabilities, but it is **guidance** at AA: 3.1.5 Reading Level is AAA. Patterns (short sentences, familiar words, one idea per paragraph, consistent vocabulary): [alternative-input-and-cognitive.md](alternative-input-and-cognitive.md#cognitive-accessibility-coga-1) and `data/cognitive-accessibility.csv`; a prompt for inclusive writing: `prompts/inclusive-ux-writing.md`.

## Media in brief

| Media | Requirement | Level |
|-------|-------------|-------|
| Prerecorded audio only (podcast) | A text alternative (transcript) | 1.2.1 A |
| Prerecorded video only (no audio) | A text alternative or an audio track | 1.2.1 A |
| Prerecorded video with audio | Captions | 1.2.2 A |
| Prerecorded video with audio | Audio description or a text alternative (A); audio description (AA) | 1.2.3 A, 1.2.5 AA |
| Live video with audio | Captions | 1.2.4 AA |

- At AA, prerecorded video in synchronized media needs **audio description** (1.2.5): a text alternative for time-based media can satisfy 1.2.3 (A), but not 1.2.5 (AA). Understanding 1.2.3 says that under 1.2.5 "authors must provide an audio description".
- Auto-playing audio is a separate requirement (1.4.2 Audio Control, A); see [common issues and fixes](audit-process-and-kpis.md#common-issues--fixes).
- A player with captions and description controls: `examples/components/media-player.html`.

## Downloadable documents

PDF, Word, slide decks and spreadsheets linked from a page are content too, and they need their own accessibility review (tags and reading order, headings, alternative text, table headers, language, contrast). This skill does not cover document formats in depth; do not assume a document passes because the web page that links to it does.

## Sources

Consulted on 2026-11-15:

- WCAG 2.2 (W3C Recommendation, 12 December 2024): https://www.w3.org/TR/WCAG22/
- What's New in WCAG 2.1: https://www.w3.org/WAI/standards-guidelines/wcag/new-in-21/
- What's New in WCAG 2.2: https://www.w3.org/WAI/standards-guidelines/wcag/new-in-22/
- Understanding 2.4.2 Page Titled: https://www.w3.org/WAI/WCAG22/Understanding/page-titled.html
- Understanding 3.1.1 Language of Page: https://www.w3.org/WAI/WCAG22/Understanding/language-of-page.html
- Understanding 3.1.2 Language of Parts: https://www.w3.org/WAI/WCAG22/Understanding/language-of-parts.html
- Understanding 2.4.6 Headings and Labels: https://www.w3.org/WAI/WCAG22/Understanding/headings-and-labels.html
- Understanding 2.4.4 Link Purpose (In Context): https://www.w3.org/WAI/WCAG22/Understanding/link-purpose-in-context.html
- Understanding 1.3.3 Sensory Characteristics: https://www.w3.org/WAI/WCAG22/Understanding/sensory-characteristics.html
- Understanding 1.4.5 Images of Text: https://www.w3.org/WAI/WCAG22/Understanding/images-of-text.html
- Understanding 1.2.3 Audio Description or Media Alternative (Prerecorded): https://www.w3.org/WAI/WCAG22/Understanding/audio-description-or-media-alternative-prerecorded.html
- Understanding 3.1.5 Reading Level (AAA): https://www.w3.org/WAI/WCAG22/Understanding/reading-level.html
- WAI Images tutorial, alt decision tree: https://www.w3.org/WAI/tutorials/images/decision-tree/
- WAI Tables tutorial: https://www.w3.org/WAI/tutorials/tables/
