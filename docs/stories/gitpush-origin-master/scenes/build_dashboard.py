#!/usr/bin/env python3
"""
GPOM cut 3, beat C5 -- the dashboard goes red.

The payload of the whole scene, and it is drawn in post for one reason: the TRANSITION is the
beat. A cut between two generated screens would not match, and a generated "now it is red" frame
gives no control over when, in what order, or how fast.

Three things make it read as systems failing rather than as a filter over the shot:

  1. 🔴 RECOLOUR REAL PIXELS. Every tile is turned by LERPING ITS OWN PIXELS toward their own
     red/green channel swap. Nothing is drawn and nothing is pasted, so each tile keeps its
     marks, its bloom, its screen texture and its anti-aliased edge. Free bonus: the lerp from
     green to red passes through olive-amber on its own, so "green, then amber, then red" comes
     out of the maths rather than out of a third colour being invented.
  2. 🔴 TILES, NOT A FIELD. A flat green screen recoloured wholesale reads as a filter. Discrete
     panels turning ONE AT A TIME reads as things failing one at a time, which is the meaning.
  3. 🔴 THE ROOM GOES WITH IT. That desk is lit BY the monitor -- the same law that governed
     cut 2's CRT. The spill shifts by however much of the screen has turned. Invisible if you
     skip it, wrong if you skip it.

Four tiles are deliberately LEFT GREEN at the end. Everything red is a resolved state; a few
things still fine is worse, because it is still going.
"""
from PIL import Image, ImageFilter
import numpy as np
import subprocess, tempfile, os

HERE = os.path.dirname(os.path.abspath(__file__))
SRC  = '/mnt/d/badcode-videos/gitpush-origin-master/clips/plant-room/stills/plant-room-dashboard-v2-a.jpg'
DST  = '/mnt/d/badcode-videos/gitpush-origin-master/clips/plant-room/takes/C5-DASHBOARD-1080.mp4'
W, H, FPS, SECS = 1920, 1080, 24, 8
COLS = ROWS = 6
TURN = 10          # frames a single tile takes to go green -> amber -> red
KEEP_GREEN = 4     # tiles that never turn

P = np.asarray(Image.open(SRC).convert('RGB')).astype(np.float32)
green = (P[..., 1] - np.maximum(P[..., 0], P[..., 2])) / 255.0
mask = green > 0.18
ys, xs = np.nonzero(mask)
y0, y1, x0, x1 = ys.min(), ys.max(), xs.min(), xs.max()

# Which tile each screen pixel belongs to, from the bounding box. The tiles are laid out on a
# regular grid, which is exactly why the plate was prompted as a grid: it masks without hand work.
yy, xx = np.mgrid[0:P.shape[0], 0:P.shape[1]]
tcol = np.clip(((xx - x0) * COLS) // max(x1 - x0, 1), 0, COLS - 1)
trow = np.clip(((yy - y0) * ROWS) // max(y1 - y0, 1), 0, ROWS - 1)
tile = (trow * COLS + tcol).astype(np.int32)

swapped = P[..., [1, 0, 2]]           # the tile's own pixels, red where they were green

# The spill: the room is lit by this screen, so it follows the screen.
# First pass at this was far too timid -- the desk's green cast only moved 3/255 across the
# whole clip, which is not a relight, it is a rounding error. A screen this bright in a room
# this dark IS the light source, so the falloff has to be wide and the gain generous.
spill = np.asarray(Image.fromarray((mask * 255).astype(np.uint8))
                   .filter(ImageFilter.GaussianBlur(150))).astype(np.float32) / 255.0
spill = np.clip(spill * 6.0, 0, 1)[..., None] * (~mask)[..., None]

# Onsets. One tile alone, a pause long enough to be noticed, then a quickening cascade --
# the shape of something spreading, not the shape of a timer.
rng = np.random.default_rng(3)
order = rng.permutation(COLS * ROWS)[:COLS * ROWS - KEEP_GREEN]
FIRST, START, LAST = 48, 74, 160                           # 2.0s / 3.1s / 6.7s at 24fps
onset = {order[0]: FIRST}                                  # the first one, alone
rest = order[1:]
for i, k in enumerate(rest):
    # t**0.55 spaces the early ones widely and bunches the late ones -- gaps CLOSE as it
    # spreads, which is what an escalation sounds like. The last turn lands at LAST, so the
    # final ~1.3s is a hold on the finished state rather than a cascade cut off by the edit.
    onset[k] = int(START + (LAST - START) * ((i / max(len(rest) - 1, 1)) ** 0.55))

with tempfile.TemporaryDirectory() as tmp:
    for f in range(FPS * SECS):
        phase = np.zeros(COLS * ROWS, np.float32)
        for k, o in onset.items():
            phase[k] = np.clip((f - o) / TURN, 0, 1)
        p = phase[tile][..., None] * mask[..., None]       # 0 green .. 1 red, per pixel

        out = P * (1 - p) + swapped * p
        red_frac = float(phase.mean())
        k = spill * red_frac * 0.9
        out = out * (1 - k) + out[..., [1, 0, 2]] * k

        Image.fromarray(np.clip(out, 0, 255).astype(np.uint8)) \
             .resize((W, H), Image.LANCZOS).save(f'{tmp}/{f:04d}.png', compress_level=1)

    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-framerate', str(FPS), '-i', f'{tmp}/%04d.png',
                    '-c:v', 'libx264', '-crf', '17', '-pix_fmt', 'yuv420p',
                    '-vf', f'fps={FPS},setsar=1', DST], check=True)
print(f'{DST}  {FPS*SECS} frames, {COLS*ROWS-KEEP_GREEN}/{COLS*ROWS} tiles turn, '
      f'first at {48/FPS:.1f}s, last at {max(onset.values())/FPS:.1f}s')
