# meeow_skills

A public library of reusable Claude skills and agent templates — drop them into any project and skip the setup.

---

## What's a skill?

A skill is a plain Markdown file (`SKILL.md`) that tells Claude how to run a specific workflow. Copy the file into your project, reference it in your system prompt or `CLAUDE.md`, and Claude knows what to do.

Each skill has a `trigger` field — a plain-English description of when to load it.

---

## Skills

### `design/`

Skills for creative and brand work. Bilingual (EN / 中文).

| Skill | What it does |
|-------|-------------|
| [`design/client_discovery`](design/client_discovery/SKILL.md) | Full agency discovery session — extracts the client's goals, taste, values, and audience before any design begins. Produces a Client DNA document. |
| [`design/style_profiling/en`](design/style_profiling/en/SKILL.md) | Visual identity session — defines aesthetic direction when the project scope is already known. |
| [`design/style_profiling/cn`](design/style_profiling/cn/SKILL.md) | 视觉风格发现 — 适用于项目方向已定、需要确定视觉语言的场景。 |
| [`design/style_self_profiling/en`](design/style_self_profiling/en/SKILL.md) | Self-directed style discovery — for solo exploration, no interviewer, at your own pace. |
| [`design/style_self_profiling/cn`](design/style_self_profiling/cn/SKILL.md) | 自我风格发现 — 内向者友好，自主探索个人审美，无需访谈压力。 |

### `skills/`

Skills about working with Claude itself.

| Skill | What it does |
|-------|-------------|
| [`skills/multi-agent-design`](skills/multi-agent-design/SKILL.md) | Multi-agent architecture patterns — 4 failure modes and the Orchestrator model. |
| [`skills/meta-skill`](skills/meta-skill/SKILL.md) | How to evaluate, create, and maintain skills in this library. |
| [`skills/stills-to-film`](skills/stills-to-film/SKILL.md) | One coding agent orchestrates an image model + a music model; code animates the stills and renders a vertical short film. No orchestration framework, no video model. |

---

## Templates

### `SOUL/`

Agent personality templates — define how an agent thinks, prioritizes, and communicates.

| Template | Language |
|----------|----------|
| [`SOUL/zh_CN_template`](SOUL/zh_CN_template/SOUL.md) | 中文 |

---

## Usage

**In Claude Code** — add a reference to `CLAUDE.md`:
```
- [client_discovery](design/client_discovery/SKILL.md) — run before any design project
```

**In any Claude chat** — paste the contents of `SKILL.md` into your system prompt or first message.

---

## Contributing

Skills are welcome. One skill per directory, `SKILL.md` as the entry point, frontmatter with `name`, `trigger`, and `last_updated`. See [`skills/meta-skill`](skills/meta-skill/SKILL.md) for the full spec.
