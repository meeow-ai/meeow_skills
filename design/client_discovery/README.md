# Client Discovery · Skill Family

## The Problem This Solves

Most creative projects fail at the beginning, not the end.

A developer receives "I want something nice" and guesses.
A designer receives a logo brief with no personality behind it.
An AI receives a prompt with no human context.

The result is technically correct work that feels wrong to the client —
because the client's actual taste, values, and psychology were never extracted.

Professional agencies solve this with a **discovery phase** before any design begins.
A skilled account manager and creative strategist spend hours understanding the client as a human being —
not asking "what color do you like?" but asking what car feels like them,
what brands they would never wear, what music plays at midnight when they are working alone.

From this, a **Client DNA document** is produced. Every designer, developer, and AI
working on the project uses this document to make decisions that feel right
without asking further questions.

This skill family brings that process to any AI conversation.

---

## The Gucci Principle

A client says: "I like Gucci."

A junior designer hears: luxury, logo, expensive, fashionable.

A skilled strategist asks: "Which piece? What specifically about it?"

The client says: "There is a specific item that looks almost cheap,
but is only offered to customers who have been loyal for years. Most people walk past it."

Now the strategist hears: insider recognition, anti-signaling, craftsmanship over display,
quiet luxury, earned credibility.

These are completely different design directions.

**The surface reference is the entry point. The specific detail is the brief.**

This is what professional discovery extracts. This is what this skill family teaches an AI to do.

---

## The Skill Family

```
design/
├── client_discovery/
│   └── SKILL.md              ← Start here. The full agency workflow.
│                                English. Template for everything else.
│
├── style_profiling/
│   ├── en/SKILL.md           ← Visual identity discovery · English
│   └── cn/SKILL.md           ← 视觉风格发现 · 中文版
│
└── style_self_profiling/
    ├── en/SKILL.md           ← Self-directed visual identity discovery · English
    └── cn/SKILL.md           ← 自我风格发现 · 中文版
```

---

## Which Skill to Use

| Situation | Skill |
|-----------|-------|
| Full project discovery — new brand, product, or digital presence | `client_discovery` |
| Focused on visual/aesthetic identity for an existing project | `style_profiling/en` or `cn` |
| Discovering your own aesthetic — alone, no interviewer | `style_self_profiling/en` or `cn` |
| Not sure | Start with `client_discovery` |

---

## What You Get

Every skill in this family produces two outputs:

**1. Client DNA Document**
A structured brief in plain language. Describes the person, their values,
their cultural references translated into design direction, their audience,
their competitive landscape, and what the brand must never be.
Any human or AI can read this and make correct decisions.

**2. Technical Handoff**
CSS design tokens, typography system, motion system, and hard rules
ready to paste into a codebase or pass to an AI developer.

---

## Installation

```bash
# Install the full family
/skill install client_discovery
/skill install style_profiling/en
/skill install style_profiling/cn
/skill install style_self_profiling/en
/skill install style_self_profiling/cn

# Or install only what you need
/skill install client_discovery
```

---

## The Workflow

```
client_discovery    →    style_profiling    →    developer / AI builds
(who they are,           (what it looks          (from Client DNA
 what they need,          like and feels)         + design tokens)
 what the brand is)
```

For smaller projects, `style_profiling` alone may be sufficient.
For anything with real stakes, run `client_discovery` first.

---

*Part of the MeowAI Skill Library · meeow-ai/meeow_skills*
