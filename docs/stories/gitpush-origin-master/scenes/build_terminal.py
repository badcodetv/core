#!/usr/bin/env python3
"""
GPOM scene 1, beat B4 -- the terminal.

Composites a real phosphor terminal onto the CRT in the push-in's landing frame,
types `C:\\> git push origin master`, hits Enter, holds, then switches the monitor off.

Everything is driven off a measured mask of the screen, so the type curves onto the
glass instead of sitting on it as a flat rectangle.
"""
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import numpy as np
import os, sys

W, H = 1920, 1080
FPS = 24
HERE = os.path.dirname(os.path.abspath(__file__))
FONT = os.path.join(HERE, 'assets', 'Mx437_IBM_VGA_9x16.ttf')
OUT = os.path.join(HERE, 'frames')
os.makedirs(OUT, exist_ok=True)

PROMPT = 'C:\\> '
CMD = 'git push origin master'

# ---------------------------------------------------------------- the plate
# Two plates. The raw one still carries Flow's chroma fill and is what we key the screen
# geometry out of; the processed one (build_screen.py) has the tube dead and the room's
# green spill already taken down, and is what every frame here is actually built on. Using
# it as the base is what makes the join off the push-in exact rather than approximate.
P = np.asarray(Image.open(os.path.join(HERE, 'plate-1080.png')).convert('RGB')).astype(np.float32)
P_OFF = np.asarray(Image.open(os.path.join(HERE, 'plate-off-1080.png')).convert('RGB')).astype(np.float32)

R, G, B = P[..., 0], P[..., 1], P[..., 2]
mask = (G > 120) & (G - R > 60) & (G - B > 60)

# Geometry comes from the raw chroma region...
gy_, gx_ = np.nonzero(mask)
x0, x1, y0, y1 = gx_.min(), gx_.max(), gy_.min(), gy_.max()

# ...but the COMPOSITE has to reach slightly further than the chroma does. The generated
# screen is a hard-edged fill, so replacing only the keyed pixels leaves a bright green
# rim right around the tube that gives the whole thing away. Dilate past it, then feather,
# so the phosphor tucks under the bezel shadow instead of stopping at a hard line.
# (Eroding does the opposite and makes the rim worse -- learned the expensive way.)
alpha_full = np.asarray(
    Image.fromarray((mask * 255).astype(np.uint8))
    .filter(ImageFilter.MaxFilter(9))
    .filter(ImageFilter.GaussianBlur(3))
).astype(np.float32) / 255.0

ys, xs = np.nonzero(alpha_full > 0.004)
A = alpha_full[ys, xs][:, None]
CX, CY = (x0 + x1) / 2.0, (y0 + y1) / 2.0
HW, HH = (x1 - x0) / 2.0, (y1 - y0) / 2.0

# Quartic fit to the measured bulge: the extent falls off as (1 - k*coord^4).
# Fitted from the real mask -- flat through the middle, dropping fast at the corners,
# which is rounded-corner CRT geometry rather than classic barrel.
KH, KV = 0.2478, 0.1044

# ------------------------------------------------- inverse map, computed once
# For every screen pixel, find where it lands in the flat terminal texture.
u = (xs - CX) / HW
v = (ys - CY) / HH
s, t = u.copy(), v.copy()
for _ in range(6):
    t = np.clip(v / np.maximum(1.0 - KV * s ** 4, 1e-3), -1.0, 1.0)
    s = np.clip(u / np.maximum(1.0 - KH * t ** 4, 1e-3), -1.0, 1.0)

TW, TH = 1230, 974                      # terminal texture, 2x the screen
tx = (s + 1.0) * 0.5 * (TW - 1)
ty = (t + 1.0) * 0.5 * (TH - 1)
tx0, ty0 = np.floor(tx).astype(int), np.floor(ty).astype(int)
fx, fy = (tx - tx0)[:, None], (ty - ty0)[:, None]
tx1_, ty1_ = np.minimum(tx0 + 1, TW - 1), np.minimum(ty0 + 1, TH - 1)


# Scanlines are evaluated per OUTPUT pixel from its curved texture coordinate rather than
# striped into the texture. Striping the texture and then resampling it through the warp
# produced a visible moire across the whole phosphor field -- the stripes aliased against
# the 2:1 downsample. Computed this way they follow the tube's curve and cannot alias.
NLINES, SCAN_DEPTH = 160.0, 0.22
_scan = (1.0 - SCAN_DEPTH * (0.5 + 0.5 * np.cos(2 * np.pi * (t + 1.0) * 0.5 * NLINES)))[:, None]


def sample(tex):
    """Bilinear-sample the flat terminal texture through the inverse map."""
    a = tex[ty0, tx0] * (1 - fx) * (1 - fy)
    a += tex[ty0, tx1_] * fx * (1 - fy)
    a += tex[ty1_, tx0] * (1 - fx) * fy
    a += tex[ty1_, tx1_] * fx * fy
    return a * _scan


# ------------------------------------------------------------ the room spill
# The plate's room is lit by a BRIGHT chroma-green screen. A dark terminal would
# not throw that much light, so the surround has to come down with it -- and go
# out entirely when the monitor dies.
gy, gx = np.mgrid[0:H, 0:W]
d = np.sqrt(((gx - CX) / (HW * 2.6)) ** 2 + ((gy - CY) / (HH * 2.6)) ** 2)
spill = np.clip(1.0 - d, 0.0, 1.0)[..., None] ** 1.5

plate_lit = P.copy()                                   # as generated: full green spill
plate_unlit = P_OFF.copy()                             # monitor dead, room lit by the city


def base_plate(glow):
    """Room lighting for a given screen brightness. glow 1.0 = as generated, 0.0 = dead."""
    out = plate_unlit + (plate_lit - plate_unlit) * glow
    return out


# -------------------------------------------------------------- the terminal
# Sized so the 27-character line fills ~79% of the screen width. That is far larger
# than an authentic 80-column prompt, and deliberately so -- this line is the title of
# the film, not a plot event, so it has to carry the frame.
FS = 64
font = ImageFont.truetype(FONT, FS)
ADV = font.getlength('M')                              # monospace, so one char is enough
LEFT = int(TW * 0.060)
BASE = int(TH * 0.435)
LINEH = int(FS * 1.25)

BG = np.array([10, 26, 14], np.float32)                # dark phosphor field
FG = (95, 255, 120)


def terminal_texture(n_typed, cursor_on, entered):
    """Flat terminal screen: prompt, n_typed characters of the command, block cursor."""
    im = Image.new('RGB', (TW, TH), tuple(int(c) for c in BG))
    d = ImageDraw.Draw(im)
    line = PROMPT + CMD[:n_typed]
    d.text((LEFT, BASE), line, font=font, fill=FG)
    if cursor_on:
        if entered:
            cx0, cy0 = LEFT, BASE + LINEH
        else:
            cx0, cy0 = LEFT + ADV * len(line), BASE
        d.rectangle([cx0, cy0 + int(FS * 0.12), cx0 + ADV - 1, cy0 + int(FS * 0.92)], fill=FG)
    return np.asarray(im).astype(np.float32)


def bloom(tex):
    """Phosphor bloom, then scanlines.

    Gaussian rather than a resize-upscale: the cheap version left faint diagonal
    artefacts across the whole phosphor field, which read as compression on a flat
    dark screen. Scanlines go on AFTER the bloom or the glow washes them out.
    """
    lit = np.clip(tex - 40, 0, None)
    im = Image.fromarray(np.clip(lit, 0, 255).astype(np.uint8))
    tight = np.asarray(im.filter(ImageFilter.GaussianBlur(4))).astype(np.float32)
    wide = np.asarray(im.filter(ImageFilter.GaussianBlur(22))).astype(np.float32)
    out = np.clip(tex + tight * 0.45 + wide * 0.55, 0, 255)

    # gentle vignette toward the tube corners
    yy, xx = np.mgrid[0:TH, 0:TW]
    r = ((xx / (TW - 1) * 2 - 1) ** 2 + (yy / (TH - 1) * 2 - 1) ** 2) ** 0.5
    out *= np.clip(1.0 - 0.16 * r ** 2.2, 0, 1)[..., None]
    return out


# ------------------------------------------------------------------ the beat
# The monitor is OFF for the whole approach and wakes up here. That bookends against the
# switch-off at the other end -- same grammar both ways, and two more places for a thunk.
PRE_OFF = 20         # arrive on a dead tube and sit with it
PON_DOT = 2          # a dot strikes in the centre
PON_LINE = 3         # it opens out into a horizontal line
PON_OPEN = 3         # the line opens vertically, overbright
PON_SETTLE = 9       # brightness settles, the prompt fades up
HOLD_A = 19          # prompt, cursor blinking
TYPE_F = 53          # 22 characters land, ~0.1s each
HOLD_B = 34          # the hesitation, cursor blinking after the command
ENTER_HOLD = 29      # Enter, then nothing happens
COLLAPSE = 4         # picture squeezes to a bright line, blowing out as it goes
TO_DOT = 2           # line closes to a centre dot
DOT_FADE = 14        # dot fades
BLACK = 8            # black

t_pre = PRE_OFF
t_pdot = t_pre + PON_DOT
t_pline = t_pdot + PON_LINE
t_popen = t_pline + PON_OPEN
t_psettle = t_popen + PON_SETTLE
t_holdA = t_psettle + HOLD_A
t_type = t_holdA + TYPE_F
t_holdB = t_type + HOLD_B
t_enter = t_holdB + ENTER_HOLD          # everything from here is the monitor dying
t_coll = t_enter + COLLAPSE
t_dot = t_coll + TO_DOT
t_fade = t_dot + DOT_FADE
TOTAL = t_fade + BLACK

# The dead tube is taken verbatim from the processed landing frame, so frame 0 here IS the
# last frame of the push-in and the join cannot be seen.
DEAD = P_OFF[ys, xs].copy()


def compose(glow, screen_px):
    """Room lit to `glow`, with `screen_px` blended into the tube through the feather."""
    out = base_plate(glow)
    out[ys, xs] = out[ys, xs] * (1 - A) + screen_px * A
    return out


def open_screen(tex, sq, gain):
    """Sample the terminal with the picture squeezed toward the centre line."""
    tt = t / max(sq, 0.02)
    keep = (np.abs(tt) <= 1.0)[:, None]
    ty_ = np.clip((tt + 1.0) * 0.5 * (TH - 1), 0, TH - 1).astype(int)
    return np.where(keep, np.clip(tex[ty_, tx0] * gain, 0, 255), DEAD)


def strike(half_w, half_h, amp):
    """A bright dot or line on a dead tube."""
    px = DEAD.copy()
    halo = (np.abs(xs - CX) <= half_w * 1.25 + 12) & (np.abs(ys - CY) <= half_h + 6)
    core = (np.abs(xs - CX) <= half_w) & (np.abs(ys - CY) <= half_h)
    px[halo] = np.maximum(px[halo], np.array([34, 62, 42], np.float32) * amp)
    px[core] = np.array([175, 255, 205], np.float32) * amp
    return px


print(f'{TOTAL} frames  =  {TOTAL / FPS:.2f}s', flush=True)

for f in range(TOTAL):
    entered = f >= t_holdB
    blink = ((f // 12) % 2) == 0                       # ~2Hz, the DOS rate

    if f < t_holdA:
        n, cur = 0, False
    elif f < t_type:
        n, cur = min(len(CMD), int((f - t_holdA) / TYPE_F * len(CMD)) + 1), True
    else:
        n, cur = len(CMD), blink

    # ---------------------------------------------------------------- powering up
    if f < t_pre:
        out = compose(0.0, DEAD)

    elif f < t_pdot:
        k = (f - t_pre + 1) / PON_DOT
        out = compose(0.10 * k, strike(HW * 0.012, 2.5, k))

    elif f < t_pline:
        k = (f - t_pdot + 1) / PON_LINE
        out = compose(0.10 + 0.55 * k, strike(HW * (0.012 + 0.988 * k ** 0.6), 2.5, 1.0))

    elif f < t_popen:
        k = (f - t_pline + 1) / PON_OPEN
        tex = bloom(terminal_texture(0, False, False))
        out = compose(0.65 + 0.25 * (1 - k), open_screen(tex, k ** 1.4, 1.0 + 3.2 * (1 - k)))

    elif f < t_psettle:
        k = (f - t_popen + 1) / PON_SETTLE
        tex = bloom(terminal_texture(0, k > 0.55, False))
        out = compose(0.90 - 0.52 * k, sample(tex) * (1.0 + 1.9 * (1 - k) ** 2.2))

    # ------------------------------------------------------------------- the line
    elif f < t_holdA:
        out = compose(0.38, sample(bloom(terminal_texture(0, blink, False))))

    elif f < t_enter:
        out = compose(0.38, sample(bloom(terminal_texture(n, cur, entered))))

    # -------------------------------------------------------------- powering down
    elif f < t_coll:
        # a dying CRT dumps its remaining beam current all at once, so the room flares
        k = (f - t_enter + 1) / COLLAPSE
        tex = bloom(terminal_texture(n, False, entered))
        out = compose(0.38 + 0.55 * k, open_screen(tex, (1.0 - k) ** 1.6, 1.0 + 3.0 * k))

    elif f < t_dot:
        k = (f - t_coll + 1) / TO_DOT
        out = compose(0.9 * (1 - k) + 0.12, strike(max(HW * (1.0 - k) ** 1.5, HW * 0.012), 2.5, 1.0))

    else:
        k = min((f - t_dot) / DOT_FADE, 1.0)
        amp = max(1.0 - k, 0.0) ** 1.9
        out = compose(0.12 * amp, strike(HW * 0.012, 2.5, amp) if amp > 0.01 else DEAD)

    Image.fromarray(np.clip(out, 0, 255).astype(np.uint8)).save(
        os.path.join(OUT, f'{f:04d}.png'), compress_level=1)
    if f % 24 == 0:
        print(f'  {f}/{TOTAL}', flush=True)

print('done', flush=True)
