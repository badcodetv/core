#!/usr/bin/env python3
"""
GPOM scene 1 -- kill the chroma green everywhere before the terminal beat.

Flow generates the CRT as a flat chroma-key fill, which is exactly what we want to key
against but is NOT what should be on screen: the monitor is OFF for the whole approach
and only powers on once we arrive. This walks every frame of the push-in, keys the green
out, puts a dead tube in its place, and takes the room's green cast down with it -- the
office is lit by that monitor, so with it off the only light is the city through the glass.

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


def key(P):
    """Chroma mask for the generated screen fill."""
    R, G, B = P[..., 0], P[..., 1], P[..., 2]
    return (G > 110) & (G - R > 55) & (G - B > 55)


def dead_screen(mask, ys, xs):
    """
    A switched-off CRT is not black -- it is a dark grey mirror with a slight sheen.
    Rendered in the mask's own normalised coordinates so it tracks as the camera closes in.

    Geometry comes from the raw chroma bbox, but it is EVALUATED at the dilated pixel set
    the composite actually writes to -- those are not the same pixels.
    """
    my, mx = np.nonzero(mask)
    x0, x1, y0, y1 = mx.min(), mx.max(), my.min(), my.max()
    w, h = max(x1 - x0, 1), max(y1 - y0, 1)
    u = (xs - x0) / w * 2 - 1
    v = (ys - y0) / h * 2 - 1

    base = np.array([15.0, 17.5, 16.5])
    sheen = np.clip(0.55 - 0.42 * u - 0.50 * v, 0, 1) ** 2.4        # soft glare, upper left
    vign = np.clip(1.0 - 0.45 * (u ** 2 + v ** 2) ** 1.1, 0, 1)

    px = base[None, :] * vign[:, None]
    px += np.array([16.0, 19.0, 18.0])[None, :] * sheen[:, None]
    return px


for i, f in enumerate(files):
    im = Image.open(f).convert('RGB')
    P = np.asarray(im).astype(np.float32)
    H, W = P.shape[:2]
    mask = key(P)

    if mask.sum() < 50:
        Image.fromarray(P.astype(np.uint8)).save(os.path.join(OUT, f'{i:04d}.png'), compress_level=1)
        continue

    # Dilate past the chroma before feathering -- the fill has a hard edge, and replacing
    # only the keyed pixels leaves a bright green rim right around the tube.
    alpha = np.asarray(
        Image.fromarray((mask * 255).astype(np.uint8))
        .filter(ImageFilter.MaxFilter(7))
        .filter(ImageFilter.GaussianBlur(2))
    ).astype(np.float32) / 255.0

    ys, xs = np.nonzero(alpha > 0.004)
    A = alpha[ys, xs][:, None]

    # Take the room's green cast down. Weighted by distance from the screen, because the
    # spill is strongest on the nearest desk edges and falls away across the room.
    spill = np.asarray(
        Image.fromarray((mask * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(90))
    ).astype(np.float32) / 255.0
    spill = np.clip(spill * 3.2, 0, 1)[..., None]

    gray = P.mean(axis=2, keepdims=True)
    out = P * (1 - spill * 0.80) + gray * (spill * 0.80) * 0.66

    # a touch cooler where the spill was, so the room reads as lit by the city not the tube
    out[..., 2] += spill[..., 0] * 5.0
    out[..., 0] += spill[..., 0] * 1.5

    dead = dead_screen(mask, ys, xs)
    out[ys, xs] = out[ys, xs] * (1 - A) + dead * A

    Image.fromarray(np.clip(out, 0, 255).astype(np.uint8)).save(
        os.path.join(OUT, f'{i:04d}.png'), compress_level=1)

    if i % 32 == 0:
        print(f'  {i}/{len(files)}', flush=True)

# the landing frame, at delivery resolution, is the plate the terminal beat powers up
last = Image.open(os.path.join(OUT, f'{len(files) - 1:04d}.png')).convert('RGB')
last.resize((1920, 1080), Image.LANCZOS).save(os.path.join(HERE, 'plate-off-1080.png'))
print('done -- plate-off-1080.png written', flush=True)
