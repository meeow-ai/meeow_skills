#!/usr/bin/env python3
"""Render a story-stills film: <film_dir>/film.html (window.render(t), window.DUR) → <film_dir>/film.mp4, 1080x1920, 30 fps.
Audio: <film_dir>/gen/score.wav if present (fade in/out, -16 LUFS), else silent.

usage: render.py <film_dir>            full render
       render.py <film_dir> t1 t2 ...  review stills only → <film_dir>/gen/check-<t>.png + gen/sheet.png contact sheet
"""
import subprocess
import sys
from pathlib import Path
from playwright.sync_api import sync_playwright

FPS = 30
film = Path(sys.argv[1]).resolve()
times = sys.argv[2:]
(film / "gen").mkdir(exist_ok=True)

with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={"width": 1080, "height": 1920})
    pg.goto((film / "film.html").as_uri())
    pg.wait_for_timeout(1500)
    pg.evaluate("document.fonts.ready")
    if times:
        shots = []
        for t in times:
            pg.evaluate(f"render({t})")
            shots.append(film / "gen" / f"check-{t}.png")
            pg.screenshot(path=str(shots[-1]))
        b.close()
        cols = min(len(shots), 5)
        rows = -(-len(shots) // cols)
        args = sum((["-i", str(s)] for s in shots), [])
        grid = "".join(f"[{i}]scale=432:768[s{i}];" for i in range(len(shots)))
        lay = "|".join(f"{(i % cols) * 432}_{(i // cols) * 768}" for i in range(len(shots)))
        subprocess.run(["ffmpeg", "-v", "error", "-y", *args, "-filter_complex",
                        grid + "".join(f"[s{i}]" for i in range(len(shots))) + f"xstack=inputs={len(shots)}:layout={lay}:fill=black"
                        if len(shots) > 1 else "[0]scale=432:768", str(film / "gen" / "sheet.png")], check=True)
        print(film / "gen" / "sheet.png", f"({rows}x{cols})")
        sys.exit(0)
    dur = float(pg.evaluate("window.DUR"))
    score = film / "gen" / "score.wav"
    audio = (["-i", str(score), "-af", f"afade=in:d=0.3,afade=out:st={dur - 1.5}:d=1.5,loudnorm=I=-16:TP=-1.5", "-c:a", "aac", "-b:a", "192k"]
             if score.exists() else ["-an"])
    enc = subprocess.Popen(
        ["ffmpeg", "-v", "error", "-y", "-f", "image2pipe", "-framerate", str(FPS), "-i", "-", *audio[:2], "-t", str(dur),
         "-c:v", "libx264", "-crf", "18", "-preset", "medium", "-pix_fmt", "yuv420p", "-vf", f"fade=out:st={dur - 0.6}:d=0.6",
         *audio[2:], "-movflags", "+faststart", str(film / "film.mp4")], stdin=subprocess.PIPE)
    for i in range(int(dur * FPS)):
        pg.evaluate(f"render({i / FPS})")
        enc.stdin.write(pg.screenshot(type="jpeg", quality=95))
    enc.stdin.close()
    enc.wait()
    b.close()
print(film / "film.mp4")
