#!/usr/bin/env python3
"""Scaffold a film folder: copies template/film.html + the kit (kit.js, kit.css) in, so each film is frozen and self-contained.

usage: new.py <film_dir>
"""
import shutil
import sys
from pathlib import Path

SKILL = Path(__file__).resolve().parent.parent
film = Path(sys.argv[1])
if (film / "film.html").exists():
    sys.exit(f"{film}/film.html exists; not overwriting")
(film / "gen").mkdir(parents=True, exist_ok=True)
shutil.copy(SKILL / "template/film.html", film / "film.html")
for f in ("kit.js", "kit.css"):
    shutil.copy(SKILL / "engine" / f, film / f)
print(f"{film}/film.html  (+ kit.js, kit.css, gen/)")
