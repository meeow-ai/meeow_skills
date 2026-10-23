#!/usr/bin/env python3
"""One still from an image model → <film_dir>/gen/<name>.png. With refs, the model edits from them (keeps characters on-model).

usage: image.py <film_dir> <name> "<prompt>" [ref ...] [--provider grok] [--aspect 9:16]

Providers are small functions (prompt, refs, aspect) → PNG bytes. Add one to PROVIDERS to use another model.
  grok: xAI grok-imagine-image-2.0. Key: $XAI_API_KEY.
"""
import base64
import json
import mimetypes
import os
import sys
from pathlib import Path
from urllib.error import HTTPError
from urllib.request import Request, urlopen


def as_url(ref):
    if ref.startswith(("http://", "https://", "data:")):
        return ref
    p = Path(ref).expanduser()
    return f"data:{mimetypes.guess_type(p.name)[0] or 'image/png'};base64,{base64.b64encode(p.read_bytes()).decode()}"


def post(url, key, payload):
    req = Request(url, json.dumps(payload).encode(), {"Authorization": f"Bearer {key}", "Content-Type": "application/json"})
    try:
        with urlopen(req, timeout=180) as r:
            return json.loads(r.read())
    except HTTPError as e:
        sys.exit(f"{url}: HTTP {e.code}: {e.read().decode(errors='replace')[:500]}")


def xai_key():
    if not os.environ.get("XAI_API_KEY"):
        sys.exit("set XAI_API_KEY (console.x.ai) or add another provider")
    return os.environ["XAI_API_KEY"]


def grok(prompt, refs, aspect):
    payload = {"model": "grok-imagine-image-2.0", "prompt": prompt, "n": 1, "response_format": "b64_json", "aspect_ratio": aspect}
    if refs:
        payload["images"] = [{"url": as_url(r), "type": "image_url"} for r in refs]
    url = "https://api.x.ai/v1/images/" + ("edits" if refs else "generations")
    return base64.b64decode(post(url, xai_key(), payload)["data"][0]["b64_json"])


PROVIDERS = {"grok": grok}


def main():
    args, opt = [], {"--provider": "grok", "--aspect": "9:16"}
    it = iter(sys.argv[1:])
    for a in it:
        if a in opt:
            opt[a] = next(it)
        else:
            args.append(a)
    film, name, prompt, refs = Path(args[0]), args[1], args[2], args[3:]
    out = film / "gen" / f"{name}.png"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_bytes(PROVIDERS[opt["--provider"]](prompt, refs, opt["--aspect"]))
    print(out)


if __name__ == "__main__":
    main()
