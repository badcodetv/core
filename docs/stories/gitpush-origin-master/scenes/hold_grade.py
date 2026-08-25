#!/usr/bin/env python3
"""
Hold a Veo clip's colour steady, and deliver it at 1080p.

🔴 VEO'S PRICE FOR PARALLAX IS COLOUR DRIFT. Measured across GPOM cut 3, every clip moved:
the exterior flight brightened 177 -> 200 over 8s, one station take DARKENED by 15, one row
take brightened by 13. It is smooth and monotonic, never a jump — which is exactly why it is
correctable, and exactly why it is easy to miss by eye until two clips are cut together and
the join flashes.

The method, and both halves matter:

  1. Anchor on a HIGH PERCENTILE, never the mean. 🔴 The mean measures what is IN SHOT, not
     how the shot is lit. On C4 the camera crabs past rack ends, so big dark objects wipe
     through frame and the mean swings 64 -> 48 -> 68 with no exposure change at all.
     Holding that mean drove a 1.4x gain on the darkest frames and pushed clipped pixels
     from 0.22% to 1.85% — the "fix" was wrecking the shot. A high percentile tracks the
     light sources instead, which is the thing that actually drifts.
  2. GUARD IT. If the measured drift is small, do nothing: a correction applied to noise is
     pure risk. And clamp the gain, so a shot this cannot model degrades to roughly-right
     rather than to blown highlights.
  3. SMOOTH THE CORRECTION AS HARD AS THE DRIFT ITSELF. A per-frame gain computed from a
     per-frame measurement flickers, and a fix you can see is worse than the drift.

Flow returns 1280x720 whatever the tier, so this also carries the 1.5x upscale to 1080p —
done once, here, rather than at concat time where it would resample twice.

  python3 hold_grade.py in.mp4 out.mp4
"""
from PIL import Image
import numpy as np
import subprocess, tempfile, glob, os, sys

W, H, FPS = 1920, 1080, 24


def hold(src, dst):
    with tempfile.TemporaryDirectory() as tmp:
        subprocess.run(['ffmpeg', '-v', 'error', '-i', src, '-vsync', '0',
                        os.path.join(tmp, '%04d.png')], check=True)
        files = sorted(glob.glob(os.path.join(tmp, '*.png')))

        anchor = np.array([np.percentile(np.asarray(Image.open(f).convert('RGB'))
                           .astype(np.float32).reshape(-1, 3), 90, axis=0) for f in files])
        target = anchor[:6].mean(0)
        drift = float(np.abs(anchor[:6].mean(0) - anchor[-6:].mean(0)).max())

        if drift < 3.0:
            gain = np.ones_like(anchor)               # nothing worth correcting; do not touch it
        else:
            w = 9                                     # smooth the CORRECTION, not the footage
            pad = np.pad(target[None, :] / np.maximum(anchor, 1e-3),
                         ((w // 2, w // 2), (0, 0)), mode='edge')
            k = np.ones(w) / w
            gain = np.stack([np.convolve(pad[:, c], k, mode='valid') for c in range(3)], 1)
            gain = np.clip(gain, 0.88, 1.14)          # a shot this cannot model degrades gently

        out = os.path.join(tmp, 'fix')
        os.makedirs(out)
        for i, f in enumerate(files):
            A = np.asarray(Image.open(f).convert('RGB')).astype(np.float32) * gain[i]
            Image.fromarray(np.clip(A, 0, 255).astype(np.uint8)) \
                 .resize((W, H), Image.LANCZOS).save(f'{out}/{i:04d}.png', compress_level=1)

        subprocess.run(['ffmpeg', '-v', 'error', '-y', '-framerate', str(FPS),
                        '-i', f'{out}/%04d.png', '-c:v', 'libx264', '-crf', '17',
                        '-pix_fmt', 'yuv420p', '-vf', f'fps={FPS},setsar=1', dst], check=True)
        print(f'{dst}  p90 drift {drift:.1f}/255, '
              f'{"held" if drift >= 3.0 else "LEFT ALONE (below threshold)"}, '
              f'gain {gain.min():.3f}..{gain.max():.3f}, {len(files)} frames at {W}x{H}')


if __name__ == '__main__':
    hold(sys.argv[1], sys.argv[2])
