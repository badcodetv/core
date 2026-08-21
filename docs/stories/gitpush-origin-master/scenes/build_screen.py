#!/usr/bin/env python3
"""
GPOM scene 1 -- kill the chroma green everywhere before the terminal beat.

Flow generates the CRT as a chroma-key fill, which is what we key against and is NOT what
should be on screen: the monitor is OFF for the whole approach and only powers on once we
arrive. This walks every frame of the push-in and turns that screen off.

  🔴 Veo ANIMATES the screen brightening as the camera closes in. Measured across the clip:
  at frame 1 it is a dim desaturated green, by frame 60 it is saturated chroma. A fixed
  threshold therefore keys 0% of it early, 33% at frame 60, 75% at frame 90 -- and a
  partial key on a flat fill is a ragged green blob, which is exactly what it looked like.

So there are two rules here, and the first version broke both:

  1. SOFT key, on a ratio that survives the brightness ramp. No hard threshold anywhere.
  2. RECOLOUR the real pixels; never paste a synthetic screen over them. Pasting a shape
     means inventing an edge, and an invented edge does not match the tube's real bezel
     shadow, corner rounding or anti-aliasing -- it reads immediately as an overlay.

Emits the processed frames, and `plate-off-1080.png`: the landing frame, which is the
plate build_terminal.py powers back up.
"""
from PIL import Image, ImageFilter
import numpy as np
import os, glob

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, 'pushin_src')
OUT = os.path.join(HERE, 'pushin_off')
os.makedirs(OUT, exist_ok=True)

files = sorted(glob.glob(os.path.join(SRC, '*.png')))
assert files, 'no source frames -- extract the push-in first'
print(f'{len(files)} frames', flush=True)

def smoothstep(x, lo, hi):
    k = np.clip((x - lo) / (hi - lo), 0.0, 1.0)
    return k * k * (3.0 - 2.0 * k)


def greenness(P):
    return (P[..., 1] - np.maximum(P[..., 0], P[..., 2])) / 255.0


# PASS 1 -- measure. A fixed ramp cannot work because the screen's saturation climbs by 9x
# across the clip while the room's own faint cast stays put, so the thresholds are derived
# per frame: the screen is the top of the distribution, the room is the middle of it.
print('measuring...', flush=True)
hi_s, mid_s = [], []
for f in files:
    g = greenness(np.asarray(Image.open(f).convert('RGB')).astype(np.float32))
    a_, b_ = np.percentile(g, [99.9, 50])
    hi_s.append(a_)
    mid_s.append(b_)


def smooth(v, w=5):
    """Moving average. Per-frame thresholds jump around; a jumping threshold flickers."""
    v = np.asarray(v, np.float32)
    pad = np.pad(v, (w // 2, w // 2), mode='edge')
    return np.convolve(pad, np.ones(w) / w, mode='valid')


hi_s, mid_s = smooth(hi_s), smooth(mid_s)

# PASS 2 -- process.
for i, f in enumerate(files):
    P = np.asarray(Image.open(f).convert('RGB')).astype(np.float32)
    R, G, B = P[..., 0], P[..., 1], P[..., 2]

    # LO has to clear the room's median by a real margin: at the widest point of the clip
    # the two are only 3x apart, and keying into the room desaturates the whole office.
    LO = max(0.55 * hi_s[i], mid_s[i] + 0.025)
    HI = max(0.85 * hi_s[i], LO + 0.020)
    a = smoothstep(greenness(P), LO, HI)[..., None]

    # What the tube looks like with no beam on it. R and B are untouched by the chroma
    # fill, so their average is the honest brightness underneath the green -- which makes
    # this a dark grey mirror that still carries the plate's own shading and reflections
    # rather than a flat fill.
    under = ((R + B) * 0.5)[..., None]
    dead = np.clip(under * 0.92 + 5.0, 0, 255)
    dead = dead * np.array([0.94, 1.02, 0.99], np.float32)     # the faintest green cast, as glass has

    out = P * (1 - a) + dead * a

    # Despill. Along the tube's anti-aliased edge the greenness sits between LO and HI, so
    # those pixels are only partly keyed and keep some of their green -- which shows up as a
    # thin green rim right around the screen. Clamp green to the other two channels across a
    # slightly dilated band so the edge cannot stay tinted.
    band = np.asarray(
        Image.fromarray((a[..., 0] * 255).astype(np.uint8))
        .filter(ImageFilter.MaxFilter(9))
        .filter(ImageFilter.GaussianBlur(2))
    ).astype(np.float32) / 255.0
    band = np.clip(band * 1.6, 0, 1)
    capped = np.minimum(out[..., 1], np.maximum(out[..., 0], out[..., 2]) * 1.03 + 2.0)
    out[..., 1] = out[..., 1] * (1 - band) + capped * band

    # The office was lit by that monitor, so with it off some light has to leave the room.
    # Driven by how much green was actually removed and blurred wide, so it tracks the
    # screen as it grows. Kept deliberately gentle: the previous version overdid this and
    # the relight itself became visible.
    spill = np.asarray(
        Image.fromarray((a[..., 0] * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(70))
    ).astype(np.float32) / 255.0
    spill = np.clip(spill * 2.4, 0, 1)[..., None]

    gray = out.mean(axis=2, keepdims=True)
    out = out * (1 - spill * 0.45) + gray * (spill * 0.45)
    out *= (1 - spill * 0.10)

    Image.fromarray(np.clip(out, 0, 255).astype(np.uint8)).save(
        os.path.join(OUT, f'{i:04d}.png'), compress_level=1)

    if i % 32 == 0:
        print(f'  {i}/{len(files)}', flush=True)

last = Image.open(os.path.join(OUT, f'{len(files) - 1:04d}.png')).convert('RGB')
last.resize((1920, 1080), Image.LANCZOS).save(os.path.join(HERE, 'plate-off-1080.png'))
print('done -- plate-off-1080.png written', flush=True)
