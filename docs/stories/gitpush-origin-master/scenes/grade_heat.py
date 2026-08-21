#!/usr/bin/env python3
"""
The heat grade -- GPOM cut 3, beat C1 (the exterior).

Kai's note was "it's a bit grey"; the first attempt matched another plate's colour statistics and
that plate turned out to be the CEILING, not the target. So this drives warmth directly instead:
amber white balance, saturation around luma, a touch of contrast.

Two things make it work, and both were paid for:

  1. 🔴 SKY AND WHITE WALLS ARE PROTECTED. Bright, near-neutral pixels take ~28% of the grade,
     everything else takes all of it. At uniform full strength the sky milks over and the
     buildings stop separating from the horizon -- see GRADE-100.jpg in the scratch folder.
  2. 🔴 STOP BEFORE THE SKY TAKES COLOUR. One step warmer than this (WARM-3) turns the sky
     yellow, and that changes the MEANING: golden hour is pretty, midday heat is oppressive.

The same numbers apply to a clip -- grading a video costs exactly what grading a still costs.
That is why the look never goes into a Veo prompt: the prompt is a motion instruction, and a
look word there costs an 8-second render per attempt and drifts across the clip.

  stills:  python3 grade_heat.py in.jpg out.jpg
  video:   ffmpeg -i in.mp4 -vf "eq=contrast=1.06:saturation=1.60,colorbalance=rs=.06:bs=-.11" \\
                  -c:a copy out.mp4          # approximate; unprotected, so check the sky
"""
from PIL import Image, ImageFilter
import numpy as np
import sys

# WARM-2, accepted by Kai 2026-08-21.
GAIN, SATX, CONTRAST, PROTECT = (1.10, 1.010, 0.85), 1.60, 1.06, 0.72


def grade(path_in, path_out):
    S = np.asarray(Image.open(path_in).convert('RGB')).astype(np.float32)

    lum, sat = S.mean(2), S.max(2) - S.min(2)
    prot = np.clip((lum - 170) / 60, 0, 1) * np.clip(1 - (sat - 6) / 22, 0, 1)
    prot = np.asarray(
        Image.fromarray((prot * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(6))
    ).astype(np.float32) / 255.0

    out = S * np.array(GAIN, np.float32)
    L = out.mean(2, keepdims=True)
    out = L + (out - L) * SATX
    out = (out - 128) * CONTRAST + 128

    k = (1.0 - PROTECT * prot)[..., None]
    out = S * (1 - k) + out * k
    Image.fromarray(np.clip(out, 0, 255).astype(np.uint8)).save(path_out, quality=95)
    print(f'{path_out}  (protected {prot.mean():.0%} of frame)')


if __name__ == '__main__':
    grade(sys.argv[1], sys.argv[2])
