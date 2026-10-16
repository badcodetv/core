#!/usr/bin/env python3
"""Draw a kill-bot HUD over a POV still — a mood-board mock-up of the ffmpeg text layer.

Usage: python3 scripts/gpom/hud-mockup.py <in.jpg> <out.jpg> <mode> [tint]
mode: patrol | signal | kill | wave | bars | voices.
wave/bars/voices make the audio waveform the hero of the signal moment (Kai, 16 Oct 2026). tint: a hex colour for the HUD (default #ff3b2f).
The film's real HUD is an ffmpeg overlay (docs/video-fx/hybrid-method.md: only ffmpeg
writes on-screen text); this only shows what it could look like.
"""
import math, random, sys
from PIL import Image, ImageDraw, ImageFont

MONO = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"


def hud(src, out, mode, tint="#ff3b2f"):
    im = Image.open(src).convert("RGB")
    W, H = im.size
    layer = Image.new("RGBA", im.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    _text = d.text
    d.text = lambda *a, **k: _text(*a, stroke_width=2, stroke_fill=(0, 0, 0, 170), **k)
    c = tuple(int(tint[i:i + 2], 16) for i in (1, 3, 5))
    col, dim = c + (235,), c + (120,)
    f = ImageFont.truetype(MONO, max(14, H // 40))
    big = ImageFont.truetype(MONO, max(22, H // 20))
    m, L, w = W // 30, W // 14, max(2, W // 500)
    for x, y, sx, sy in ((m, m, 1, 1), (W - m, m, -1, 1), (m, H - m, 1, -1), (W - m, H - m, -1, -1)):
        d.line([(x, y), (x + sx * L, y)], fill=col, width=w)
        d.line([(x, y), (x, y + sy * L)], fill=col, width=w)
    cx, cy, r = W // 2, H // 2, H // 16
    d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=dim, width=w)
    for a in range(0, 360, 90):
        x, y = cx + math.cos(math.radians(a)) * r, cy + math.sin(math.radians(a)) * r
        x2, y2 = cx + math.cos(math.radians(a)) * r * 1.6, cy + math.sin(math.radians(a)) * r * 1.6
        d.line([(x, y), (x2, y2)], fill=dim, width=w)
    tx = m + L // 3
    d.text((tx, m + L // 3), "UNIT KB-07  PATROL", font=f, fill=col)
    d.text((tx, m + L // 3 + f.size * 1.4), "SECTOR SWN-04  ORGANIC LIFE: 0  (1,826 DAYS)", font=f, fill=dim)
    d.text((W - m - L // 3, m + L // 3), "AUDIO  ON", font=f, fill=col, anchor="ra")
    # the muffled waveform: low amplitude in patrol, a burst in signal/kill
    bx0, bx1, by = W // 4, W * 3 // 4, H - m - L // 2
    if mode in ("wave", "bars", "voices"):
        bx1 = bx0  # the hero band replaces the small trace
    if bx1 > bx0: d.rectangle([bx0, by - H // 14, bx1, by + H // 14], outline=dim, width=1)
    random.seed(7)
    pts = []
    for i in range(bx1 - bx0):
        t = i / (bx1 - bx0)
        amp = 3 if mode == "patrol" else (H // 16) * math.exp(-((t - 0.55) ** 2) / 0.02) + 3
        pts.append((bx0 + i, by + math.sin(i * 0.35) * amp * random.uniform(0.3, 1.0)))
    if len(pts) > 1:
        d.line(pts, fill=col, width=max(1, w - 1))
        d.text((bx0, by - H // 14 - f.size * 1.3), "AUDIO TRACE  0.4-1.2 kHz  (MUFFLED)", font=f, fill=dim)
    if mode in ("signal", "kill"):
        for k in range(3):
            rr = r * (2.2 + k * 0.9)
            d.ellipse([cx - rr, cy - rr, cx + rr, cy + rr], outline=c + (160 - k * 45,), width=w)
        d.text((cx, cy - r * 3.7), "ORGANIC SIGNAL DETECTED", font=big, fill=col, anchor="mm")
        d.text((cx, cy - r * 3.7 + big.size * 1.2), "BEARING 214  RANGE 1.3 km  CONFIDENCE 0.97", font=f, fill=dim, anchor="mm")
    if mode in ("wave", "bars", "voices"):
        # the hero waveform: a wide band across the middle of the frame
        x0, x1, y0 = W // 10, W * 9 // 10, H // 2
        band = H // 5
        d.rectangle([x0, y0 - band, x1, y0 + band], fill=(0, 0, 0, 150), outline=dim, width=1)
        for gx in range(x0, x1, (x1 - x0) // 24):
            d.line([(gx, y0 - band), (gx, y0 + band)], fill=c + (40,), width=1)
        d.line([(x0, y0), (x1, y0)], fill=c + (70,), width=1)
        random.seed(11)
        def env(t):  # two overlapping voices, muffled: bursts of syllables
            a = sum(math.exp(-((t - p) ** 2) / 0.0009) * h for p, h in ((.18, .5), (.24, .8), (.31, .6), (.45, .9), (.52, 1), (.58, .7), (.71, .85), (.77, .6), (.86, .95)))
            return min(1.0, a)
        if mode == "bars":
            n = 96
            bw = (x1 - x0) / n
            for i in range(n):
                t = i / n
                h = band * 0.92 * env(t) * random.uniform(0.55, 1.0) + 2
                d.rectangle([x0 + i * bw + 1, y0 - h, x0 + (i + 1) * bw - 2, y0 + h], fill=c + (220,))
        else:
            pts = []
            for i in range(x1 - x0):
                t = i / (x1 - x0)
                a = band * 0.9 * env(t) + 2
                pts.append((x0 + i, y0 + math.sin(i * 0.55) * a * random.uniform(0.4, 1.0)))
            d.line(pts, fill=col, width=w)
        d.text((x0, y0 - band - big.size * 0.9), "ORGANIC SIGNAL DETECTED", font=big, fill=col, anchor="lm")
        d.text((x1, y0 - band - big.size * 0.9), "BEARING 214  RANGE 1.3 km", font=f, fill=dim, anchor="rm")
        d.text((x0, y0 + band + f.size * 1.2), "SOURCE: SUBSURFACE   FILTER: MUFFLED   CONFIDENCE 0.97", font=f, fill=dim, anchor="lm")
        if mode == "voices":
            for p, lab in ((.24, "VOICE A  ♀"), (.52, "VOICE B  ♂"), (.86, "VOICE A  ♀")):
                vx = x0 + p * (x1 - x0)
                d.line([(vx, y0 - band), (vx, y0 + band)], fill=col, width=1)
                d.text((vx + 6, y0 - band + 6), lab, font=f, fill=col)
            d.text((x1, y0 + band + f.size * 1.2), "PATTERN: HUMAN x2 (DISPUTE)", font=f, fill=col, anchor="ra")
    if mode == "kill":
        d.rectangle([cx - W // 6, H * 2 // 3 - big.size, cx + W // 6, H * 2 // 3 + big.size], fill=c + (215,))
        d.text((cx, H * 2 // 3), "KILL MODE  ENGAGED", font=big, fill=(0, 0, 0, 255), anchor="mm")
    Image.alpha_composite(im.convert("RGBA"), layer).convert("RGB").save(out, quality=90)


if __name__ == "__main__":
    hud(*sys.argv[1:5])
