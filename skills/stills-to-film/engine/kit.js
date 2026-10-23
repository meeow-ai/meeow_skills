// story-stills kit: pure functions of t (seconds). A film calls these from window.render(t); render.py screenshots each frame.
const K = (() => {
  const $ = (id) => document.getElementById(id);
  const clamp = (x) => Math.max(0, Math.min(1, x));
  const ease = (x) => (x = clamp(x), x * x * (3 - 2 * x));
  const pulse = (t, at, w) => Math.max(1 - Math.abs(t - at) / w, 0);  // 0→1→0 triangle centred on `at`

  // shots: [layerId, start, end, zoomFrom, zoomTo, panX, panY (px over the shot), originY]; crossfade xf seconds
  function shots(t, list, xf = 0.4) {
    for (const [id, a, b, z0, z1, px, py, oy] of list) {
      const el = $(id), k = ease((t - a) / (b - a));
      el.style.opacity = Math.min(clamp((t - a) / xf), clamp((b - t) / xf));
      const img = el.querySelector('img');
      if (!img) continue;
      img.style.transformOrigin = '50% ' + oy;
      img.style.transform = `translate(${px * k}px,${py * k}px) scale(${z0 + (z1 - z0) * k})`;
    }
  }

  // captions: [id, in, out]; fade f seconds, slight rise on entry
  function caps(t, list, f = 0.3) {
    for (const [id, a, b] of list) {
      const e = $(id);
      e.style.opacity = Math.min(clamp((t - a) / f), clamp((b - t) / f));
      e.style.marginTop = (1 - clamp((t - a) / f)) * 24 + 'px';
    }
  }

  // drifting sparkles in #spark; returns draw(t, amount 0..1)
  function sparkles(n = 60) {
    const box = $('spark');
    for (let i = 0; i < n; i++) {
      const s = document.createElement('div');
      s.className = 'sp'; s.textContent = i % 3 ? '✦' : '·';
      s.style.fontSize = (14 + (i * 37) % 34) + 'px';
      s.dataset.x = (i * 97) % 1080; s.dataset.y = (i * 211) % 1920; s.dataset.p = (i * 0.618) % 1;
      box.appendChild(s);
    }
    return (t, amount) => [...box.children].forEach((s) => {
      const ph = (t * 0.25 + +s.dataset.p) % 1;
      s.style.left = (+s.dataset.x + Math.sin(t * 2 + +s.dataset.p * 9) * 30) + 'px';
      s.style.top = (+s.dataset.y - ph * 400) + 'px';
      s.style.opacity = amount * Math.sin(Math.PI * ph);
    });
  }

  // rubber stamp thump at time `at`
  function stamp(id, t, at, rot = -12) {
    const st = clamp((t - at) / 0.2);
    $(id).style.opacity = st * 0.92;
    $(id).style.transform = `translate(-50%,40%) rotate(${rot}deg) scale(${2.2 - 1.2 * st})`;
  }

  // reveal card: item i starts at start + i*step. Fade in → wand wipes label + honest line, reveals .now → label folds
  // shut → each <mark> underlines gold in turn. Earlier items dim slightly as the next one arrives.
  function reveal(t, card, start, step) {
    [...card.querySelectorAll('.item')].forEach((it, i) => {
      const a = start + i * step;
      const k = clamp((t - a) / 0.4), w = ease((t - a - 1.0) / 0.8), next = clamp((t - a - step) / 0.4);
      it.style.opacity = k * (1 - 0.25 * next);
      it.style.transform = `translateY(${(1 - ease(k)) * 30}px)`;
      const x = w * 100, was = it.querySelector('.was'), fold = ease((t - a - 1.9) / 0.4);
      for (const el of [it.querySelector('.honest'), was]) {
        if (!el) continue;
        el.style.clipPath = `inset(0 0 0 ${x}%)`;
        el.style.filter = `blur(${w * 3}px)`;
      }
      if (was) {
        was.style.height = (1 - fold) * 38 + 'px';
        it.querySelector('.box').style.marginTop = (1 - fold) * 8 + 'px';
      }
      it.querySelector('.now').style.clipPath = `inset(-10px ${100 - x}% -10px 0)`;
      const wand = it.querySelector('.wand');
      wand.style.left = x + '%';
      wand.style.opacity = w > 0 && w < 1 ? 1 : 0;
      it.querySelectorAll('mark').forEach((m, j) => {
        const h = ease((t - a - 2.0 - j * 0.35) / 0.4);
        m.style.backgroundSize = `${h * 100}% 3px`;
        m.style.color = `rgb(${239 + 16 * h},${230 - 17 * h},${210 - 103 * h})`;
        m.style.textShadow = `0 0 ${18 * h}px rgba(255,190,80,${0.75 * h})`;
      });
    });
  }

  return { $, clamp, ease, pulse, shots, caps, sparkles, stamp, reveal };
})();
