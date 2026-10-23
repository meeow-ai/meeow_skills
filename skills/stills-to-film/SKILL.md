---
name: stills-to-film
description: Make a short vertical film (15–60 s, 9:16) by orchestrating models from one coding agent, with no orchestration framework and no video model. An image model makes one still per beat (editing from reference images keeps characters consistent), a music model makes the score, and an HTML page whose render(t) animates the stills (camera moves, captions, sparkles, flash, stamp, a text-reveal card) is rendered frame by frame with Playwright + ffmpeg. Style-free: any look, any story. Use for gag shorts, story teasers, product mini-stories.
trigger: making a short story film from AI stills, or orchestrating image + music models from one coding agent
last_updated: 2026-10-23
---

# stills-to-film

The agent directs and the models are its tools: an image model for the pictures, a music model for the score.
Code does the rest (motion, text, timing), so every fix is an edit and a re-render, not a new generation.
Paid video models aren't needed: the stills carry the acting, the code carries the camera.

Proven on Resume Magic #2 (44.6 s, 6 stills + 1 score, $0 video). That film, rebuilt on this kit, renders
pixel-identical to the hand-built original on 18 sampled frames.

## What you need

- An agent that can read files and run code on a computer: Claude Code, Codex, Grok, Google Antigravity, Meta Muse,
  DeepSeek's agent, Hermes Agent or similar. (Tested on Claude Code.)
  A cloud sandbox works as well as a local machine. If the agent has its own image or music generation tool,
  use that instead of the shipped providers: only `gen/<name>.png` and `gen/score.wav` matter to the render.
- Python 3 with Playwright + Chromium (`pip install playwright && playwright install chromium`), and ffmpeg.
- An image model key (shipped provider: `XAI_API_KEY` for Grok) and a music model key (shipped: `GEMINI_API_KEY`
  for Lyria, plus `pip install google-genai`). Other models: add a provider (see below).

If something is missing, tell the user what and how to get it, and ask before installing anything or spending money.

## Files

```
engine/kit.js     K.shots (Ken Burns + crossfades), K.caps, K.sparkles, K.stamp, K.reveal (wand wipes old text, reveals new), K.pulse
engine/kit.css    1080x1920 frame and the classes the kit drives (.layer .cap .vig #flash #spark .stamp .reveal)
engine/new.py     new.py <film_dir>: copies the template + the kit in (each film keeps its own frozen copy)
engine/image.py   image.py <film_dir> <name> "<prompt>" [refs…] [--provider grok] [--aspect 9:16] → gen/<name>.png
engine/music.py   music.py <film_dir> <seconds> "<prompt>" [--bpm 110] [--provider lyria] → gen/score.wav
engine/render.py  render.py <film_dir> [t…]: with times, review stills + gen/sheet.png; without, film.mp4 (30 fps, -16 LUFS)
template/film.html  a two-shot starter film
```

Models are swappable: a provider is one function in `image.py` / `music.py` (prompt in, bytes out). Shipped and
tested: Grok (`grok-imagine-image-2.0`, generate + edit) and Google Lyria RealTime. Keys come from the environment.

## Recipe

1. **Beats.** Write the story as 5–8 beats, one picture each, plus the viewer takeaway and the last line.
   Hook in the first 2 seconds. A shape that works for gags: problem → helper → transformation → test → twist → payoff.
2. **Scaffold:** `python3 engine/new.py <film_dir>`.
3. **Stills:** one `image.py` call per beat. Make the first still of each character, then edit every later shot from
   it (pass it as a ref, start the prompt "Keep this exact character from the reference image"), or faces drift.
   - Spell out the composition ("seen over her shoulder, the boss across the desk facing camera"), or models default
     to side-by-side.
   - Expression changes: edit the previous still in close-up ("sunglasses slid down to the tip of her nose, jaw dropped").
   - No brand names or logos in prompts.
   Look at every still before using it; retries are cheap, bad stills are not.
4. **Timeline:** in `film.html`, one `.layer` per still; `SHOTS` = [layer, start, end, zoomFrom, zoomTo, panX, panY,
   originY], neighbours overlapping by the 0.4 s crossfade; `CAPS` = [id, in, out]; text cards are plain HTML over a
   blurred still. Everything is a pure function of `t`; `window.DUR` sets the length.
   Reading time: ~3.5 s per line of on-screen text, plus 2–3 s on any card the viewer should finish reading.
5. **Review:** `render.py <film_dir> 0.5 3 6 …` at every cut and every hit, then look at `gen/sheet.png`. Fix, repeat.
6. **Score:** `music.py <film_dir> <DUR + 1.5> "<mood, instruments>" --bpm <n>`. Instrumental; describe instruments
   and mood, not genre names alone.
7. **Render:** `render.py <film_dir>` (~4 s of wall time per film second on a 4-core ARM VPS). Then watch it: check
   frames of the MP4, not the exit code.

## Telling people how it was made

Say what was used, and only that: "one coding agent called an image model and a music model as tools; code renders
every frame". The models aren't sub-agents (they get one request each and decide nothing), and a coding agent is
itself a harness, so the honest claim is "no orchestration framework, no pipeline, no video model".

## Limits

- Motion is camera only (push-ins, pans, crossfades): a storybook feel. Character motion needs cut-out puppets from
  masked parts of a still, or one image-to-video shot from a paid video model.
- Shorts sweet spot is under ~40 s: trim text before trimming beats.
- Lyria RealTime is experimental; behind a SOCKS proxy install `httpx[socks] python-socks` for its websocket.
