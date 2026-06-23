# Design Handoff Template
## For developers and AI — technical translation of the brand brief

---

## How to Use This

After completing the brand memo with the client, translate the findings
into this technical document. This is FOR THE DEVELOPER, not the client.
Use jargon freely here. This is the bridge between feeling and code.

---

## CSS Custom Properties Template

```css
/* ============================================
   [PROJECT NAME] — Design Token System
   Generated from brand discovery session
   Date: [DATE]
   ============================================ */

:root {

  /* --- BACKGROUNDS ---
     Described by feeling, then technical value.
     [FEELING]: [HEX] */
  --color-void:        [hex];   /* [feeling — e.g. "deep night, warm not cold"] */
  --color-depth:       [hex];   /* [feeling — e.g. "card surface, slightly lifted"] */
  --color-surface:     [hex];   /* [feeling — e.g. "elevated elements, interaction layer"] */

  /* --- TEXT ---
     Never pure white or pure black unless the brand demands it. */
  --color-primary:     [hex];   /* [feeling — e.g. "aged ivory, not clinical white"] */
  --color-secondary:   [hex];   /* [feeling — e.g. "muted, secondary info"] */
  --color-ghost:       [hex];   /* [feeling — e.g. "barely there, placeholder"] */

  /* --- THE ACCENT ---
     Use sparingly. This is the hardware on the bag.
     State the maximum % of screen this color should occupy. */
  --color-accent:      [hex];   /* [feeling] · MAX [X]% of any screen */
  --color-accent-dim:  [hex];   /* hover state, subtle version */

  /* --- THE PULSE ---
     One element per page. Maximum.
     This is the declaration color — the red bomber jacket. */
  --color-pulse:       [hex];   /* [feeling] · ONE ELEMENT PER PAGE */

  /* --- THE EASTER EGG ---
     The hidden warmth. For the cat. For the thing only curious people find. */
  --color-secret:      [hex];   /* [feeling] · easter egg elements only */

  /* --- BORDERS --- */
  --border-default:    rgba([r],[g],[b], 0.06);
  --border-accent:     rgba([r],[g],[b], 0.20);

  /* ============================================
     TYPOGRAPHY
     ============================================ */

  /* Fonts */
  --font-editorial:    '[Font Name]', '[Fallback]', serif;
  --font-clean:        '[Font Name]', '[Fallback]', sans-serif;

  /* Scale — always use clamp() for fluid type */
  --text-hero:         clamp([min]rem, [vw]vw, [max]rem);
  --text-headline:     clamp([min]rem, [vw]vw, [max]rem);
  --text-subhead:      [size]rem;
  --text-body:         [size]rem;
  --text-caption:      [size]rem;
  --text-eyebrow:      [size]rem;  /* small all-caps label */

  /* Tracking (letter-spacing) */
  --tracking-tight:    -0.02em;   /* headlines */
  --tracking-normal:   0.02em;    /* body */
  --tracking-wide:     0.15em;    /* eyebrow labels, all-caps */
  --tracking-xwide:    0.30em;    /* very sparse labels */

  /* Leading (line-height) */
  --leading-editorial: [value];   /* tight, confident — typically 1.05–1.15 */
  --leading-body:      [value];   /* generous — typically 1.7–1.9 */

  /* ============================================
     MOTION
     Source: brand pacing — [describe the rhythm here]
     ============================================ */

  /* Easing curves */
  --ease-silk:         cubic-bezier(0.25, 0.1, 0.25, 1);     /* standard transitions */
  --ease-reveal:       cubic-bezier(0.16, 1, 0.3, 1);         /* content appearing */
  --ease-exit:         cubic-bezier(0.4, 0, 1, 1);            /* content leaving */

  /* Durations */
  --duration-instant:  [ms]ms;    /* micro-interactions */
  --duration-normal:   [ms]ms;    /* standard transitions */
  --duration-slow:     [ms]ms;    /* deliberate reveals */
  --duration-cinematic:[ms]ms;    /* THE signature moment — use once per page */

  /* ============================================
     SPACING
     ============================================ */
  --space-xs:  0.25rem;
  --space-sm:  0.5rem;
  --space-md:  1rem;
  --space-lg:  2rem;
  --space-xl:  4rem;
  --space-2xl: 6rem;

}
```

---

## Hard Rules for Developers

These rules come directly from the brand brief and must never be violated:

```
/* COPY THESE INTO YOUR PROJECT'S README OR CONTRIBUTING.md */

BRAND RULES — [PROJECT NAME]
Generated: [DATE]
Source: Brand discovery session

1. [Rule derived from brief — e.g. "No pure white (#ffffff) anywhere. Ever."]
2. [Rule — e.g. "--color-accent touches maximum 10% of any screen"]
3. [Rule — e.g. "--color-pulse is ONE element per page, not one per section"]
4. [Rule — e.g. "All headlines use --font-editorial, all functional text uses --font-clean"]
5. [Rule — e.g. "The easter egg element uses --duration-cinematic exclusively"]
6. [Rule — e.g. "No gradient backgrounds. Flat layers only."]
7. [Rule — e.g. "No pure black text. Use --color-primary (aged ivory) on dark, --color-void on light"]
```

---

## Typography Usage Guide

```
HEADLINE:     var(--font-editorial) · var(--text-hero) · var(--leading-editorial)
              letter-spacing: var(--tracking-tight)
              
SUBHEAD:      var(--font-editorial) · var(--text-headline) · var(--leading-editorial)

EYEBROW:      var(--font-clean) · var(--text-eyebrow) · var(--tracking-xwide)
              text-transform: uppercase · color: var(--color-accent)

BODY:         var(--font-clean) · var(--text-body) · var(--leading-body)
              color: var(--color-secondary)

CAPTION:      var(--font-clean) · var(--text-caption) · var(--tracking-wide)
              color: var(--color-ghost)
```

---

## Motion Usage Guide

```
STANDARD HOVER:    transition: [property] var(--duration-normal) var(--ease-silk)
CONTENT REVEAL:    transition: opacity var(--duration-slow) var(--ease-reveal),
                               transform var(--duration-slow) var(--ease-reveal)
THE SIGNATURE:     transition: [property] var(--duration-cinematic) var(--ease-reveal)
                   /* Used ONCE per page. The thing that makes people stop. */
```

---

## Color Usage Cheatsheet

```
PAGE BACKGROUND:    var(--color-void)
CARD/SURFACE:       var(--color-depth) or var(--color-surface)
PRIMARY TEXT:       var(--color-primary)
SECONDARY TEXT:     var(--color-secondary)
SUBTLE TEXT:        var(--color-ghost)
BORDERS:            var(--border-default) standard · var(--border-accent) hover/emphasis
ACCENT (sparingly): var(--color-accent) · hover: var(--color-accent-dim)
PULSE (once/page):  var(--color-pulse)
EASTER EGG:         var(--color-secret)
```

---

## Component Notes

*Add project-specific notes here after discovery is complete.*

Example entries:
- Navigation: [behavior description]
- Hero section: [content and layout direction]  
- Card components: [style direction]
- The signature moment: [what is the one thing that makes people stop?]
- The easter egg: [where does it live? what triggers it? what does it reveal?]

---

## Font Loading

```html
<!-- Add to <head> — adjust font names based on brief -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=[Editorial+Font]:ital,wght@0,300;0,400;1,300;1,400&family=[Clean+Font]:wght@300;400&display=swap" rel="stylesheet">
```

---

## Accessibility Notes

*Always include — brand aesthetics must never compromise accessibility.*

- Minimum contrast ratio: 4.5:1 for body text, 3:1 for large text (WCAG AA)
- Check all color combinations: `--color-primary` on `--color-void`, etc.
- Motion: respect `prefers-reduced-motion` — wrap cinematic animations
- Font sizes: minimum 16px body text on mobile

```css
@media (prefers-reduced-motion: reduce) {
  * {
    --duration-cinematic: 0ms !important;
    --duration-slow: 0ms !important;
    animation-duration: 0.01ms !important;
    transition-duration: 0.01ms !important;
  }
}
```
