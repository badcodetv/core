#!/usr/bin/env python3
"""
GPOM cut 3, beat C5 -- the console fails, and a skull comes up.

🔴 KAI'S RULING 2026-08-21, replacing the tile dashboard entirely: this is a TEXT CONSOLE, in
the same register as cut 2's terminal. The reason is not decoration. If cut 3's alarm arrives in
the same green type as cut 2's `git push origin master`, the grammar of the film becomes *the
machine speaks in a green console* -- and the second time it speaks, it is screaming. The tile
dashboard was only ever a picture OF a dashboard.

It is also the better joke, and the joke is the thesis: the most capable system ever built
reports planetary failure through a 1981 text console.

⚠️ This corrects "nothing legible, ever" as written for this beat. That rule was about
TELEMETRY -- numbers a viewer starts reading instead of feeling. A console designed to be read
at a glance, in very few words, is a title card. Cut 2 proved legible type renders clean and
does not trip the filter.

🔴 KAI'S RULING 2026-08-21 (second): C5 happens at the SAME desk C4 arrives at. So the plate is
`stills/C5-desk-b.jpg` -- a dark, unlit monitor in the mezzanine hall with the scissor lift at
frame right -- and this script turns that panel on.

🔴 AND: "the text is too close to the edge of the screen, so it just becomes obviously a black
box overlay." Three separate things were wrong, and only one of them was the text:

  1. THE RECT WAS WRONG. Auto-detection found 1100x511 against a real panel of 631x350 -- it had
     latched onto the room's dark areas, not the screen. A console painted over a box twice the
     size of the monitor cannot look like anything but a box. **Pass the rect explicitly.** A
     measured rectangle is four integers; a detector that can be wrong by 2x is not worth it.
  2. THE FILL WAS FLAT. A real black LCD still reflects the room -- this plate has the ceiling
     strip lights sitting on the panel as soft speculars. Killing them removes the one cue that
     says "this is glass in this room" and leaves a hole in the picture. So the fill is built
     from the plate's OWN high-frequency residual: drop the panel's base level to near-black and
     keep its reflections at ~0.85. Recolour real pixels, never paste -- the same law as cut 2.
  3. NO MARGIN. Type ran to the panel edge, which no console does; every real screen has an
     overscan margin, and its absence is what makes an overlay read as an overlay.

Usage:  build_console.py SRC DST [x0,y0,x1,y1]
        The rect is the LIT AREA inside the bezel. Measure it once with a luminance probe.
"""
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import numpy as np
import subprocess, tempfile, os, sys

SRC  = sys.argv[1] if len(sys.argv) > 1 else '/mnt/c/Users/kai/Desktop/gpom-plant-room/stills/C5-desk-b.jpg'
DST  = sys.argv[2] if len(sys.argv) > 2 else '/mnt/c/Users/kai/Desktop/gpom-plant-room/takes/C5-CONSOLE-v2.mp4'
RECT = sys.argv[3] if len(sys.argv) > 3 else '372,227,1003,577'      # measured on C5-desk-b
FONT = '/mnt/c/Users/kai/Desktop/gpom-s01/assets/Mx437_IBM_VGA_9x16.ttf'
W, H, FPS, SECS = 1920, 1080, 24, 8

GREEN = (150, 255, 170)
RED   = (255,  70,  60)
LINE  = 'AWAITING HUMAN REVIEW'

SKULL = [
    "         ████████         ",
    "       ████████████       ",
    "      ██████████████      ",
    "     ████████████████     ",
    "     ███   ████   ███     ",
    "     ██     ██     ██     ",
    "     ███   ████   ███     ",
    "     ████████████████     ",
    "      ████  ██  ████      ",
    "       ████████████       ",
    "       ██ ██ ██ ██ ██       ",
    "        ██████████        ",
]

CHECKS = ['POWER', 'THERMAL', 'NETWORK FABRIC', 'STORAGE ARRAY', 'COOLING LOOP',
          'SCHEDULER', 'REPLICATION', 'INGEST', 'CONTROL PLANE', 'TELEMETRY']


def blur(a, r):
    """Gaussian through a uint8 round-trip. Offset any signed input before calling."""
    return np.asarray(Image.fromarray(np.clip(a, 0, 255).astype(np.uint8))
                      .filter(ImageFilter.GaussianBlur(r))).astype(np.float32)


P = np.asarray(Image.open(SRC).convert('RGB')).astype(np.float32)
x0, y0, x1, y1 = (int(v) for v in RECT.split(','))
SW, SH = x1 - x0, y1 - y0
print(f'screen {SW}x{SH} at ({x0},{y0}), aspect {SW / SH:.2f}', flush=True)

# ---- what the panel looks like with the backlight down ------------------------------------
# The plate's screen is a flat dark grey (~45) carrying the ceiling strips as soft speculars
# (~65). Black it out by dropping the BASE level only, and keep the reflections -- an LCD's
# specular reflectance does not change when you change what it is displaying, so those
# highlights are the same whatever is on screen, and they are the only thing tying this
# rectangle to this room.
base  = P[y0:y1, x0:x1].mean(2)
lowf  = blur(base, 55)                                   # the panel's broad shading
resid = blur(base - lowf + 128.0, 2) - 128.0             # its reflections, sign preserved
GLASS = 4.5 \
    + np.clip(lowf - np.percentile(lowf, 5), 0, None) * 0.05 \
    + np.clip(resid, 0, None) * 0.85

# The inner rim of a panel sits slightly darker than its centre, and that gradient is most of
# what sells the seam against the bezel. Without it the fill meets the bezel as a hard step.
ry = np.minimum(np.arange(SH), SH - 1 - np.arange(SH))[:, None]
rx = np.minimum(np.arange(SW), SW - 1 - np.arange(SW))[None, :]
RIM = 0.55 + 0.45 * np.clip(np.minimum(ry, rx) / 14.0, 0, 1)
DEAD = (GLASS * RIM)[..., None] * np.array([0.90, 1.04, 0.97], np.float32)   # glass, faintly green

# Feather the rect by ~1px so the composite lands on the bezel's own anti-aliased inner edge.
rect = np.zeros(P.shape[:2], np.uint8)
rect[y0:y1, x0:x1] = 255
alpha = blur(rect, 1.0)[..., None] / 255.0

# 🔴 A 150px blur clipped at 6x is not a light pool, it is the whole room. It covered every
# pixel in frame, so the "desk is lit by the monitor" pass tinted the ceiling, the mezzanine and
# the far cabinets too -- and since it was a raw R/G channel swap on a green-grey room, the
# result was lilac. Keep the falloff LOCAL, and tint by multiplying toward a colour rather than
# swapping channels: a swap is not a light, it is a bug that happens to look coloured.
spill = blur(rect, 110) / 255.0
spill = np.clip(spill * 2.2, 0, 1)[..., None]
spill[y0:y1, x0:x1] = 0.0                                # the panel does not light itself

TINT_GREEN = np.array([0.82, 1.22, 0.94], np.float32)    # console green, bounced off grey steel
TINT_RED   = np.array([1.42, 0.62, 0.64], np.float32)

# ---- type ----------------------------------------------------------------------------------
# 🔴 MARGIN IS NOT DECORATION. Type running to the panel edge is the single clearest tell that a
# screen was pasted on: every real console overscans. 5.5% each way, and everything -- the log,
# the skull, the line -- lives inside that box.
PADX, PADY = int(SW * 0.055), int(SH * 0.055)
IW, IH = SW - 2 * PADX, SH - 2 * PADY

FS = max(10, IH // 20)
font = ImageFont.truetype(FONT, FS)
CH = int(FS * 1.06)
ROWS_ON_SCREEN = IH // CH
# The skull is the POINT of the beat, so it is sized like a title, not like a log line -- the
# same call as cut 2, where the command was set far larger than an authentic 80-column prompt
# because the line IS the title. Fit to whichever of width/height binds first.
SKULL_FS = max(14, min(int(IH / (len(SKULL) + 1.6)), int(IW / len(SKULL[0]) / 0.56)))
skull_font = ImageFont.truetype(FONT, SKULL_FS)
SKULL_CH = int(SKULL_FS * 1.02)


def screen_for(f):
    """One frame of screen content, at the panel's own resolution."""
    img = Image.new('RGB', (SW, SH), (0, 0, 0))
    d = ImageDraw.Draw(img)
    t = f / FPS

    if t < 4.5:
        # The scroll. Monotony reads as "fine" without anyone having to read it -- then the
        # same monotony is what makes a single FAIL land.
        emitted = int(t * (3.2 + 5.5 * max(0.0, (t - 2.6)) ** 2))   # accelerates after 2.6s
        lines = []
        for i in range(max(0, emitted - ROWS_ON_SCREEN), emitted):
            name = CHECKS[i % len(CHECKS)]
            fail = (i >= 6 and i % 7 == 6) or (t > 2.6 and i % 3 == 0) \
                or (t > 3.6 and i % 2 == 0) or t > 4.1
            lines.append((f'[{"FAIL" if fail else " OK "}]  {name}', RED if fail else GREEN))
        for r, (txt, col) in enumerate(lines):
            d.text((PADX, PADY + r * CH), txt, font=font, fill=col)
    else:
        # Cleared. The skull draws in, then the line, then the cursor.
        sk = t - 4.5
        fw = skull_font.getbbox('M')[2] or SKULL_FS
        bw, bh = len(SKULL[0]) * fw, len(SKULL) * SKULL_CH
        ox = PADX + (IW - bw) // 2
        oy = PADY + (IH - bh - 2 * CH) // 2
        for r, row in enumerate(SKULL):
            if sk > 0.10 * r:
                d.text((ox, oy + r * SKULL_CH), row, font=skull_font, fill=RED)
        if sk > 1.4:
            lw = font.getbbox(LINE)[2]
            d.text((PADX + (IW - lw) // 2, oy + bh + CH), LINE, font=font, fill=RED)
        if sk > 2.0 and int((sk - 2.0) * 2) % 2 == 0:
            lw = font.getbbox(LINE)[2]
            d.text((PADX + (IW - lw) // 2 + lw + (font.getbbox('M')[2] or FS),
                    oy + bh + CH), '█', font=font, fill=RED)

    # Scanlines in SCREEN space. Striping the texture and then resampling it aliases into moire.
    a = np.asarray(img).astype(np.float32)
    rows = np.arange(SH)[:, None, None]
    a *= (1.0 - 0.16 * (0.5 + 0.5 * np.cos(2 * np.pi * rows / 3.0)))
    # A photographed screen is never pixel-crisp -- the lens, the panel's own diffusion and the
    # 1376->1920 finish all soften it. Half a pixel here is the difference between type that
    # sits ON the glass and type that sits IN FRONT of it.
    a = np.stack([blur(a[..., c], 0.55) for c in range(3)], axis=2)
    return a


with tempfile.TemporaryDirectory() as tmp:
    for f in range(FPS * SECS):
        S = screen_for(f)
        out = P.copy()
        out[y0:y1, x0:x1] = np.maximum(DEAD, S * RIM[..., None])
        out = P * (1 - alpha) + out * alpha

        # The desk is lit BY this monitor -- which in the plate was OFF, so this pass is adding
        # light, not recolouring it: green while the checks run, red once the skull is up. It
        # also has to FADE, because a screen showing a mostly-black skull frame emits a fraction
        # of what a full page of type does.
        t = f / FPS
        redness = float(np.clip((t - 1.6) / 3.0, 0, 1))
        tint = TINT_GREEN * (1 - redness) + TINT_RED * redness
        amt = spill * (0.34 if t < 4.5 else 0.16)
        out = out * ((1 - amt) + amt * tint * 1.30)

        Image.fromarray(np.clip(out, 0, 255).astype(np.uint8)) \
             .resize((W, H), Image.LANCZOS).save(f'{tmp}/{f:04d}.png', compress_level=1)

    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-framerate', str(FPS), '-i', f'{tmp}/%04d.png',
                    '-c:v', 'libx264', '-crf', '17', '-pix_fmt', 'yuv420p',
                    '-vf', f'fps={FPS},setsar=1', DST], check=True)
print(f'{DST}  screen {SW}x{SH}  font {FS}px  {ROWS_ON_SCREEN} rows  skull {SKULL_FS}px  "{LINE}"')
