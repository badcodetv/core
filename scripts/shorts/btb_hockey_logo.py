#!/usr/bin/env python3
"""By the Balls outro: the BadCode logo printed in the centre circle of an arcade air hockey table (Jack, 2026-11-23,
timeline r1 at475: "lets do a hockey arcade badcode logo thanks").

The clip is real-looking footage (Flow, HOCKEYa: camera locked, a puck glides past above the circle); the logo is the
official brand file (docs/brand/logo/badcode-stacked.svg, the dark version for a white table, rendered to PNG with sharp).
The camera does not move, so no tracking: the logo is squashed to the table's perspective (the circle's own ellipse
ratio) and multiplied into the surface, so the table's sheen, light and air holes show through it like printing.

    ~/.cache/badcode-lips/venv/bin/python scripts/shorts/btb_hockey_logo.py <clip.mp4> <out.mp4> --in 0.4 --dur 3.75 \
        [--cx 545 --cy 1392 --w 520 --squash 0.43 --fade 0.4]
Writes picture only (no audio), 1080x1920 at 24 fps.
"""
# style-lint: story=short-by-the-balls
import argparse, pathlib, subprocess
import cv2
import numpy as np

REPO = pathlib.Path(__file__).resolve().parents[2]
SVG = REPO / 'docs/brand/logo/badcode-stacked.svg'
W, H, FPS = 1080, 1920, 24


def logo_rgba(width, squash, cache):
    if not cache.exists():
        subprocess.run(['node', '-e', f"require('sharp')('{SVG}',{{density:900}}).resize(2400).png().toFile('{cache}')"],
                       check=True, cwd=REPO)
    im = cv2.imread(str(cache), cv2.IMREAD_UNCHANGED)  # BGRA
    h = int(round(im.shape[0] * width / im.shape[1] * squash))
    im = cv2.resize(im, (width, h), interpolation=cv2.INTER_AREA)
    return im.astype(np.float32) / 255.0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('clip'); ap.add_argument('out')
    ap.add_argument('--in', dest='tin', type=float, default=0.4); ap.add_argument('--dur', type=float, default=3.75)
    ap.add_argument('--cx', type=int, default=545); ap.add_argument('--cy', type=int, default=1392)
    ap.add_argument('--w', type=int, default=520); ap.add_argument('--squash', type=float, default=0.43)
    ap.add_argument('--fade', type=float, default=0.4)
    a = ap.parse_args()
    out = pathlib.Path(a.out)
    lg = logo_rgba(a.w, a.squash, out.parent / 'badcode-stacked-2400.png')
    lh, lw = lg.shape[:2]; x0, y0 = a.cx - lw // 2, a.cy - lh // 2
    alpha = cv2.GaussianBlur(lg[..., 3], (0, 0), 0.8)[..., None] * 0.92   # a printed edge, not a sticker
    ink = lg[..., :3]
    n = round(a.dur * FPS)
    rd = subprocess.Popen(['ffmpeg', '-nostdin', '-loglevel', 'error', '-ss', str(a.tin), '-i', a.clip, '-vf',
                           f'scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},fps={FPS},tpad=stop_mode=clone:stop_duration=4',
                           '-frames:v', str(n), '-f', 'rawvideo', '-pix_fmt', 'bgr24', '-'], stdout=subprocess.PIPE)
    wr = subprocess.Popen(['ffmpeg', '-nostdin', '-loglevel', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'bgr24', '-s', f'{W}x{H}',
                           '-r', str(FPS), '-i', '-', '-vf', 'scale=in_range=full:out_range=limited,format=yuv420p,lutyuv=y=clip(val\\,20\\,235)',
                           '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '18', '-pix_fmt', 'yuv420p', '-color_range', 'tv',
                           '-colorspace', 'bt709', '-color_primaries', 'bt709', '-color_trc', 'bt709', str(out)], stdin=subprocess.PIPE)
    for i in range(n):
        buf = rd.stdout.read(W * H * 3)
        if len(buf) < W * H * 3: break
        f = np.frombuffer(buf, np.uint8).reshape(H, W, 3).astype(np.float32) / 255.0
        reg = f[y0:y0 + lh, x0:x0 + lw]
        f[y0:y0 + lh, x0:x0 + lw] = reg * (1 - alpha) + (reg * ink) * alpha   # multiply: the table shows through the print
        t = i / FPS; k = min(1.0, max(0.0, (a.dur - t) / a.fade))           # fade to black at the end
        wr.stdin.write((np.clip(f * k, 0, 1) * 255).astype(np.uint8).tobytes())
    wr.stdin.close(); wr.wait(); rd.wait()
    print(out)


if __name__ == '__main__':
    main()
