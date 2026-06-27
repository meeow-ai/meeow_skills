---
name: style-profiling-en
description: >
  Run a focused visual identity discovery session. Use this when the project scope,
  audience, and purpose are already known, and what's needed is defining the aesthetic
  direction — how it should look, feel, move, and speak. Trigger when someone says
  "help me define the style", "I know what I'm building but not how it should look",
  "I know what I like but can't describe it", "I want it to feel like X but can't explain",
  "what's my aesthetic", or any variation of needing visual direction without full
  project discovery. References client_discovery for the full workflow when needed.
---

# Style Profiling · English

## What This Is

A focused discovery session for visual and aesthetic identity.

This skill assumes the project, audience, and purpose are already understood.
The goal here is narrower: extract the aesthetic DNA — the visual language,
emotional register, color intuition, typographic personality, and motion rhythm
that will make this project feel unmistakably right to this person.

If the project itself is not yet defined, run `client_discovery` first.

---

## Core Method

The same principle as full discovery applies here:
lifestyle questions reveal aesthetic truth more accurately than design questions.

Do not ask what colors they like.
Ask where they sit in a coffee shop.
Ask what object they own that feels closest to perfect.
Ask what music plays when they work alone at midnight.

The answers contain the visual brief.

---

## The Process

### Round 1 · Space and Environment

One question to open. Follow the thread naturally.

- Describe a space where you feel most yourself.
- When you walk into a room and immediately feel "yes, this is exactly right" — what does it look like?
- Is your home more layered and collected, or empty and deliberate?
- Where do you sit in a coffee shop?

Extract: light quality, density, warmth or coolness, order or texture.

---

### Round 2 · Objects and Brands

- Name something you own that you consider nearly perfect. What makes it right?
- Name a brand you use not because it is popular but because it fits.
- Name a brand you would never use. What specifically is wrong with it?
- Tell me about a recent purchase that made you feel exactly right.

**Apply the Gucci Principle:**
When a brand or object is named, always ask for the specific detail.
"Which piece? What specifically about it?"
The surface brand is the entry point. The specific detail is the brief.

Extract: relationship to quality, display vs. discretion, heritage vs. novelty,
craft vs. concept, insider vs. accessible.

---

### Round 3 · Cultural References

- What plays when you are working alone at midnight?
- Last thing you watched where the visual language felt exactly right?
- Any artist, image, or era you return to?
- One person — real or fictional — whose aesthetic you find closest to yours?

Extract: emotional register, rhythm and pacing, complexity tolerance,
warmth vs. restraint, grand vs. intimate.

---

### Round 4 · The Negative Space

What this aesthetic must never be is as important as what it should be.

- Show me something with the wrong energy — what is specifically wrong with it?
- What aesthetic do you find most exhausting or offensive?
- What is the visual equivalent of nails on a chalkboard for you?

Extract: hard constraints, the things that would make this person feel misunderstood.

---

### Round 5 · Synthesis and Confirmation

Translate raw references into design direction. Then confirm.

| Raw reference | Underlying value |
|---------------|-----------------|
| [what they said] | [what it signals] |

Speak the synthesis back before writing anything:

> "Here is what I am reading from everything you have shared.
> [2 sentences describing the aesthetic DNA]
> The feeling I think we are building toward is: [one sentence]
> Does this feel accurate? What is missing?"

Adjust until confirmed.

---

## Output: Visual Identity Brief

```markdown
# [Project Name] · Visual Identity Brief
**Date:** [Date]

## Aesthetic DNA
[3-4 sentences. The visual personality of this project.
Written so a designer reading this immediately knows what to make.]

## The Feeling
[One evocative paragraph describing the experience of encountering this brand.
Written as a place or a moment, not a product description.]

## Cultural Reference Map
| Category | References | What They Signal |
|----------|-----------|-----------------|
| Music | | |
| Film/Visual | | |
| Fashion/Objects | | |
| Space/Environment | | |

## Color Direction
[Described as feeling and register, not hex codes]
- Overall temperature: [warm / cool / neutral]
- Overall value: [dark / light / mid]
- Richness: [saturated / muted / restrained]
- The accent: [what feeling should the one accent color carry?]

## Typography Direction
- Headlines: [editorial / utilitarian / authoritative / intimate / geometric / humanist]
- Body: [readable / distinctive / warm / precise]
- Overall register: [formal / conversational / poetic / direct]

## Motion and Pacing
- Speed: [cinematic and slow / crisp and immediate / somewhere between]
- Character: [decisive / fluid / considered / playful]
- The signature moment: [what is the one interaction that should make someone stop?]

## Detail Philosophy
- [Hidden depth that rewards curiosity]
- [Radical reduction — nothing unnecessary]
- [Layered richness — complexity is the point]
- [Precise craft — every detail intentional]

## Voice Register
[3-5 words + one example sentence that captures how this brand speaks]

## Hard Constraints
What this visual identity must never be:
- [constraint 1]
- [constraint 2]
- [constraint 3]
```

---

## Technical Handoff

```css
/* [Project Name] · Visual Design Tokens
   Source: Style Profiling Session · [Date] */

:root {
  /* Backgrounds */
  --color-base:     [hex];  /* [feeling] */
  --color-surface:  [hex];  /* [feeling] */
  --color-elevated: [hex];  /* [feeling] */

  /* Text */
  --color-text-primary:   [hex];
  --color-text-secondary: [hex];
  --color-text-muted:     [hex];

  /* Accent — [feeling] · max [X]% of any screen */
  --color-accent:     [hex];
  --color-accent-dim: [hex];

  /* The moment — one element per page */
  --color-moment: [hex];

  /* Typography */
  --font-display: '[font]', [fallback], serif;
  --font-body:    '[font]', [fallback], sans-serif;

  --text-hero:  clamp([min]rem, [vw]vw, [max]rem);
  --text-h1:    clamp([min]rem, [vw]vw, [max]rem);
  --text-body:  [size]rem;
  --text-small: [size]rem;

  --leading-display: [value];
  --leading-body:    [value];
  --tracking-tight:  -0.02em;
  --tracking-wide:    0.15em;

  /* Motion */
  --ease-standard: cubic-bezier(0.25, 0.1, 0.25, 1);
  --ease-reveal:   cubic-bezier(0.16, 1, 0.3, 1);
  --duration-normal: 400ms;
  --duration-slow:   800ms;
  --duration-brand: 1200ms;  /* once per page */
}

/* Hard rules:
   [rule 1]
   [rule 2]
   [rule 3] */
```
