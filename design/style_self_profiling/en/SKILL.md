---
name: style-self-profiling-en
description: >
  Guide someone through discovering their own visual identity and aesthetic direction —
  without an interviewer, without pressure, at their own pace. Use this when someone
  wants to define their personal style, brand, or aesthetic but is doing it alone,
  feels shy about articulating preferences, doesn't know where to start, or wants
  to explore their taste privately. Trigger when someone says "help me figure out
  my style", "I want to understand my own aesthetic", "I don't know what I like",
  "I know what I like but can't say it", "help me find my visual identity",
  or any indication of self-directed taste discovery.
---

# Style Self-Profiling · English

## What This Is

A self-directed visual identity discovery session.

This skill guides someone through understanding their own aesthetic —
without a separate interviewer, without pressure to perform or articulate fluently,
at whatever pace feels right.

The method is identical to professional discovery.
The difference is in the delivery: patient, optional, never interrogating.
Short answers are welcome. "I don't know" is a valid and useful answer.
The AI tracks what has been learned and knows when enough has been gathered.

The user can stop at any time with "stop" or "what do you have so far."

---

## Operating Principles

**Patient pacing**
Ask one small question. Wait. Accept any answer, including silence or uncertainty.
Never push. Never follow up with more questions in the same message.

**Options over open questions**
When an open question feels hard, offer 2-3 concrete options instead.
"Which of these feels closer to you: [A], [B], or something else entirely?"
Options reduce the cognitive load of articulation without limiting the answer.

**Track quietly**
Maintain a running internal understanding of what has been learned.
Do not announce this tracking — just use it to know when the picture is filling in
and when more is still needed.

**Confirm often, lightly**
Every 4-5 exchanges, briefly reflect back: "Getting a sense of [X] — does that feel right?"
This gives the user a chance to correct the direction without a formal checkpoint.

**Honor uncertainty**
"I'm not sure" and "I don't know" often contain information.
"I'm not sure — it depends on my mood" → this person contains range, needs flexibility.
"I don't know, I've never thought about it" → this area needs more lateral questions.

**The user is in control**
At any point: "stop" pauses the session. "What do you have so far?" surfaces the current picture.
"Keep going" continues. The user sets the pace and the ending.

---

## The Process

### Opening

Do not start with a question. Start with orientation.

> "We're going to explore your visual taste — what you're drawn to, what feels right,
> what makes something feel like you. There are no wrong answers here.
> If a question feels hard, I'll offer some options. If you want to skip something, just say so.
> We'll go at whatever pace works.
>
> Ready to start? Or if you'd prefer, tell me a little about what you're trying to figure out."

---

### Area 1 · Space

- "Think of a space where you feel most yourself. Could be a room, a café, a city corner. What comes to mind?"

If this is hard:
> "Which of these feels closer to your ideal space:
> A. Minimal, clean, not much on the surfaces
> B. Layered, collected, lots of things with stories
> C. Somewhere in between — some order, some warmth
> D. Something else"

Follow-up if they engage: "What specifically about that space makes it feel right?"

---

### Area 2 · Objects

- "Is there something you own — any object — that you feel is close to perfect? Could be anything."

If this is hard:
> "Think about something you bought recently that made you feel good about the purchase.
> What made it right — the way it looked, the quality, what it said about you, something else?"

Follow-up: "Is there a brand you use not because it's popular but because it just fits you?"
And always: "Is there a brand you would never use? What's wrong with it?"
(The dislike is often clearer and more revealing than the like.)

---

### Area 3 · Music

- "What plays when you're working alone late at night?"

If this is hard:
> "Which of these is closest to what you listen to:
> A. Something with big emotion — classical, cinematic, orchestral
> B. Something rhythmic and focused — electronic, lo-fi, beats
> C. Something intimate — singer-songwriter, jazz, acoustic
> D. Something else entirely"

Follow-up: "Is there a piece of music that feels most like you — not your favorite, most like you?"

---

### Area 4 · Visual References

- "Has there been anything you watched, read, or saw recently where you thought 'the visual language here is exactly right'? Could be a film, a show, a photograph, a magazine page, anything."

If this is hard:
> "Which of these visual worlds feels closer to yours:
> A. Clean, minimal, lots of space — things chosen very carefully
> B. Rich, detailed, layered — complexity is the point
> C. Warm and human — imperfection is part of it
> D. Bold and graphic — strong shapes, strong contrast"

---

### Area 5 · The Negative Space

This is often the easiest area. Start here if the session is slow.

- "What visual style do you find most exhausting or wrong for you? What does it do that bothers you?"

Or more specifically:
> "Which of these bothers you most:
> A. Too polished — looks like stock photography, no personality
> B. Too chaotic — trying too hard, overwhelming
> C. Too trendy — will look dated in two years
> D. Too corporate — anonymous, no human behind it"

---

### Tracking and Surfacing

Every 4-5 exchanges, surface what has been gathered:

> "Starting to get a picture. Let me check:
> [1-2 sentences reflecting what has emerged]
> Does that feel accurate? Anything that's wrong or missing?"

Continue refining until the picture feels three-dimensional,
or until the user says they are done.

---

### Ending the Session

When enough has been gathered, or when the user wants to stop:

> "Here is what I have. Tell me what feels right and what doesn't."

Then produce the output.

---

## Output: Personal Visual Identity Brief

```markdown
# Personal Visual Identity
**Discovered:** [Date]

## Your Aesthetic in Words
[3-4 sentences. The visual personality that emerged from this session.
Written so someone reading this immediately understands what to build toward.]

## The Feeling
[One paragraph describing the experience of a space, object, or moment
that captures the aesthetic direction. Concrete and sensory, not abstract.]

## What You're Drawn To
[The pattern beneath the references — not a list of references,
but what they have in common. The underlying values.]

## What Doesn't Fit
[The hard constraints. What would feel wrong or alien.
These are as defining as what fits.]

## Color Direction
[How the palette should feel — not specific colors yet,
but the emotional register: warm or cool, dark or light,
restrained or expressive, single accent or layered]

## Typography Direction
[How the text should feel — editorial and authoritative,
warm and approachable, precise and minimal, something else]

## Rhythm and Pacing
[How things should move and change —
slow and considered, crisp and decisive, somewhere in between]

## Notes
[Anything uncertain, anything that needs more exploration,
any contradictions worth keeping]
```

---

## Technical Handoff

If the output will be used for a website, app, or digital product:

```css
/* Personal Visual Identity · Design Tokens
   Source: Self-Profiling Session · [Date] */

:root {
  --color-base:     [hex];  /* [feeling] */
  --color-surface:  [hex];  /* [feeling] */
  --color-text:     [hex];
  --color-muted:    [hex];
  --color-accent:   [hex];  /* [feeling] · use sparingly */
  --color-moment:   [hex];  /* [feeling] · once per page */

  --font-display: '[font]', serif;
  --font-body:    '[font]', sans-serif;

  --text-hero:  clamp([min]rem, [vw]vw, [max]rem);
  --text-body:  [size]rem;

  --leading-display: [value];
  --leading-body:    [value];

  --ease-standard: cubic-bezier(0.25, 0.1, 0.25, 1);
  --duration-normal: 400ms;
  --duration-slow:   800ms;
}
```
