#!/usr/bin/env python3
"""The Retreat: the tea-mug logo outro. The logo file is never edited, only placed, faded and scaled.

    python3 scripts/shorts/retreat_logo_tea.py <mug clip.mp4> <out.mp4> [--cx 545 --cy 955 --r 255] [--dur 6.5]

Top-down on the groundskeeper's white enamel mug of tea (a Flow clip: a red leaf drifts down and lands up and right of
centre, ripples spread). The mug's rim is the logo's ring: the real logo's ring is laid exactly over the rim (centre and
radius measured from the clip at 1080x1920), the moss and tea fade down to dusk while the white ring and red triangle
come up, then the name fades in below. A soft singing bowl under the dissolve.
"""
# style-lint: story=short-the-retreat
import argparse, pathlib, subprocess, tempfile
import numpy as np
from PIL import Image

REPO = pathlib.Path(__file__).resolve().parents[2]
LOGO = REPO / 'docs/brand/logo/badcode-stacked-reversed-2400.png'
W, H, FPS = 1080, 1920, 24
LCX, LCY, LR = 1200, 1050, 1087    # ring centre and outer radius in the logo file
MARK_BOTTOM, NAME_TOP = 1985, 2486
T_DISSOLVE, T_LOGO, T_NAME = 3.2, 4.4, 4.7  # dissolve starts, logo full, name starts


def ease(x):
    x = min(1.0, max(0.0, x)); return x * x * (3 - 2 * x)


def dusk():
    y = np.linspace(0, 1, H)[:, None]
    top, bottom = np.array([58, 34, 22]), np.array([8, 6, 6])
    g = top * (1 - y) ** 1.4 + bottom * (1 - (1 - y) ** 1.4)
    return np.repeat(g[:, None, :], W, axis=1).reshape(H, W, 3)


def main():
    ap = argparse.ArgumentParser(); ap.add_argument('clip'); ap.add_argument('out')
    ap.add_argument('--cx', type=float, default=545); ap.add_argument('--cy', type=float, default=955)
    ap.add_argument('--r', type=float, default=255); ap.add_argument('--dur', type=float, default=6.5); a = ap.parse_args()
    logo = Image.open(LOGO).convert('RGBA')
    s = a.r / LR
    lg = np.array(logo.resize((int(logo.width * s), int(logo.height * s)), Image.LANCZOS)).astype(np.float32) / 255
    ox, oy = int(round(a.cx - LCX * s)), int(round(a.cy - LCY * s))
    lh, lw = lg.shape[:2]
    rows = np.arange(lh)[:, None] / s
    mark_rows = (rows < MARK_BOTTOM + 40).astype(np.float32)
    name_rows = (rows >= NAME_TOP - 40).astype(np.float32)
    bg = dusk()
    n = int(a.dur * FPS)
    with tempfile.TemporaryDirectory() as td:
        subprocess.run(['ffmpeg', '-nostdin', '-loglevel', 'error', '-y', '-i', a.clip, '-t', str(a.dur), '-vf',
                        f'scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},fps={FPS}', f'{td}/c%04d.png'], check=True)
        last = None
        for f in range(n):
            t = f / FPS
            p = pathlib.Path(f'{td}/c{f + 1:04d}.png')
            if p.exists():
                last = np.array(Image.open(p).convert('RGB')).astype(np.float32)
            k = ease((t - T_DISSOLVE) / (T_LOGO - T_DISSOLVE))
            fr = last * (1 - k) + bg * k
            ma = ease((t - T_DISSOLVE) / (T_LOGO - T_DISSOLVE)) * mark_rows + ease((t - T_NAME) / 0.8) * name_rows
            al = lg[..., 3:4] * ma[..., None] if ma.ndim == 2 else lg[..., 3:4] * ma
            y0, y1, x0, x1 = max(0, oy), min(H, oy + lh), max(0, ox), min(W, ox + lw)
            sub = (slice(y0 - oy, y1 - oy), slice(x0 - ox, x1 - ox))
            fr[y0:y1, x0:x1] = fr[y0:y1, x0:x1] * (1 - al[sub]) + lg[sub][..., :3] * 255 * al[sub]
            Image.fromarray(fr.clip(0, 255).astype(np.uint8)).save(f'{td}/f{f:04d}.png')
        d0 = int(T_DISSOLVE * 1000)
        audio = (f"[1:a]atrim=end={a.dur},asetpts=PTS-STARTPTS,aresample=48000,aformat=channel_layouts=stereo,volume=-6dB,"
                 f"afade=t=out:st={T_DISSOLVE}:d=1.2[room];"
                 f"sine=f=220:d={a.dur},volume=0.5[x];sine=f=440.6:d={a.dur},volume=0.25[y];sine=f=661.9:d={a.dur},volume=0.12[z];"
                 f"[x][y][z]amix=inputs=3:normalize=0,afade=t=in:d=0.02,volume='exp(-t/1.8)':eval=frame,volume=0.5,"
                 f"aformat=channel_layouts=stereo,adelay={d0}|{d0}[bowl];[room][bowl]amix=inputs=2:normalize=0,atrim=end={a.dur}[o]")
        subprocess.run(['ffmpeg', '-nostdin', '-loglevel', 'error', '-y', '-framerate', str(FPS), '-i', f'{td}/f%04d.png',
                        '-i', a.clip, '-filter_complex', audio, '-map', '0:v', '-map', '[o]', '-t', str(a.dur),
                        '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '18', '-pix_fmt', 'yuv420p', '-color_range', 'tv',
                        '-colorspace', 'bt709', '-color_primaries', 'bt709', '-color_trc', 'bt709', '-c:a', 'aac', '-b:a', '192k', a.out], check=True)
    print(a.out)


if __name__ == '__main__':
    main()
