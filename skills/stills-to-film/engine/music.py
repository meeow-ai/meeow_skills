#!/usr/bin/env python3
"""Instrumental score from a music model → <film_dir>/gen/score.wav. Make it ~1.5 s longer than the film; render.py fades the tail.

usage: music.py <film_dir> <seconds> "<mood, instruments, tempo feel>" [--bpm 110] [--provider lyria]

  lyria: Google Lyria RealTime (free, experimental), key $GEMINI_API_KEY or $GOOGLE_API_KEY. Needs: pip install google-genai.
         Behind a SOCKS proxy also install httpx[socks] python-socks (the websocket goes through it).
"""
import asyncio
import os
import sys
import wave
from pathlib import Path

RATE, CH, WIDTH = 48000, 2, 2


async def lyria(seconds, prompt, bpm):
    from google import genai
    from google.genai import types
    key = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
    client = genai.Client(api_key=key, http_options={"api_version": "v1alpha"})
    need, buf = int(seconds * RATE * CH * WIDTH), bytearray()
    async with client.aio.live.music.connect(model="models/lyria-realtime-exp") as s:
        await s.set_weighted_prompts(prompts=[types.WeightedPrompt(text=prompt, weight=1.0)])
        await s.set_music_generation_config(config=types.LiveMusicGenerationConfig(bpm=bpm, temperature=1.0))
        await s.play()

        async def collect():
            while len(buf) < need:
                async for msg in s.receive():
                    for c in (msg.server_content.audio_chunks if msg.server_content else None) or []:
                        buf.extend(c.data)
                    if len(buf) >= need:
                        return
        await asyncio.wait_for(collect(), timeout=seconds + 30)
    return bytes(buf[:need])


PROVIDERS = {"lyria": lyria}


def main():
    args, opt = [], {"--bpm": "110", "--provider": "lyria"}
    it = iter(sys.argv[1:])
    for a in it:
        if a in opt:
            opt[a] = next(it)
        else:
            args.append(a)
    film, seconds, prompt = Path(args[0]), float(args[1]), args[2]
    pcm = asyncio.run(PROVIDERS[opt["--provider"]](seconds, prompt, int(opt["--bpm"])))
    out = film / "gen" / "score.wav"
    out.parent.mkdir(parents=True, exist_ok=True)
    with wave.open(str(out), "wb") as w:
        w.setnchannels(CH); w.setsampwidth(WIDTH); w.setframerate(RATE); w.writeframes(pcm)
    print(out, f"{len(pcm) / (RATE * CH * WIDTH):.1f}s")


if __name__ == "__main__":
    main()
