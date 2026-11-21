#!/usr/bin/env python3
"""The Queue: the phone-charging logo ending (Jack, 2026-11-21: "The phone charging").

On the lad's phone the charging ring fills, clockwise from 12 o'clock, and becomes the BadCode ring; the red triangle
pops in; the name fades in beneath. Made from the official stacked logo file only (docs/brand/logo/
badcode-stacked-reversed-2400.png): the reveal is a mask over the real pixels, nothing redrawn.

    python3 scripts/shorts/queue_logo.py <clip.mp4> <out.mp4> --cx X --cy Y --r R [--in S] [--dur D]

cx, cy, r: the phone's own ring (centre and outer radius, in the 1080x1920 frame) the logo ring is laid on.
"""
# style-lint: story=short-the-queue
import argparse, pathlib, subprocess, tempfile
import numpy as np
from PIL import Image

REPO = pathlib.Path(__file__).resolve().parents[2]
LOGO = REPO / 'docs/brand/logo/badcode-stacked-reversed-2400.png'
MARK_ROWS, NAME_ROWS = (114, 1985), (2486, 2895)   # measured from the file
RING_C, RING_R = (1200, 1050), 1087                # ring centre and outer radius in the file
FPS, W, H = 24, 1080, 1920


def frames(scale, tmp, dur):
    src = np.asarray(Image.open(LOGO)).astype(np.float32)
    rgb, a = src[..., :3], src[..., 3] / 255
    red = (rgb[..., 0] > 150) & (rgb[..., 1] < 110)          # the triangle
    yy, xx = np.mgrid[0:src.shape[0], 0:src.shape[1]]
    ang = (np.degrees(np.arctan2(xx - RING_C[0], -(yy - RING_C[1]))) + 360) % 360   # 0 at 12 o'clock, clockwise
    is_mark = (yy >= MARK_ROWS[0]) & (yy <= MARK_ROWS[1])
    is_name = yy >= NAME_ROWS[0] - 20
    n = int(dur * FPS)
    size = (int(src.shape[1] * scale), int(src.shape[0] * scale))
    for i in range(n):
        t = i / FPS
        fill = min(1, t / 1.2) * 360                          # 0-1.2 s: the ring fills
        m = np.zeros_like(a)
        m[is_mark & ~red & (ang <= fill)] = 1
        if t >= 1.3: m[red & is_mark] = min(1, (t - 1.3) / 0.15)  # 1.3 s: the triangle pops in (not the name's red o)
        if t >= 1.6: m[is_name] = min(1, (t - 1.6) / 0.5)     # 1.6 s: the name fades in
        out = np.dstack([rgb, a * m * 255]).astype(np.uint8)
        Image.fromarray(out, 'RGBA').resize(size, Image.LANCZOS).save(f'{tmp}/f{i:04d}.png')
    return size


def main():
    ap = argparse.ArgumentParser(); ap.add_argument('clip'); ap.add_argument('out')
    ap.add_argument('--cx', type=float, required=True); ap.add_argument('--cy', type=float, required=True)
    ap.add_argument('--r', type=float, required=True); ap.add_argument('--in', dest='tin', type=float, default=0.0)
    ap.add_argument('--dur', type=float, default=3.2)
    ap.add_argument('--cover', type=float, default=0, help='radius of a black disc laid over the phone\'s own ring first')
    ap.add_argument('--zoom', type=float, default=1.0, help='crop in on the phone (centred on cx, cy) after the overlay')
    a = ap.parse_args()
    scale = a.r / RING_R
    with tempfile.TemporaryDirectory() as tmp:
        size = frames(scale, tmp, a.dur)
        x = int(a.cx - RING_C[0] * scale); y = int(a.cy - RING_C[1] * scale)
        vf = f'scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},fps={FPS}'
        cover = ''
        if a.cover:
            c = int(a.cover); d = Image.new('RGBA', (2 * c, 2 * c), (0, 0, 0, 0))
            from PIL import ImageDraw
            ImageDraw.Draw(d).ellipse([0, 0, 2 * c - 1, 2 * c - 1], fill=(0, 0, 0, 255)); d.save(f'{tmp}/cover.png')
            cover = f'[b0];movie={tmp}/cover.png[cv];[b0][cv]overlay={int(a.cx - c)}:{int(a.cy - c)}'
        zw, zh = int(W / a.zoom) // 2 * 2, int(H / a.zoom) // 2 * 2
        zx = int(min(max(a.cx - zw / 2, 0), W - zw)); zy = int(min(max(a.cy - zh / 2, 0), H - zh))
        zoom = f',crop={zw}:{zh}:{zx}:{zy},scale={W}:{H}:flags=lanczos' if a.zoom > 1 else ''
        subprocess.run(['ffmpeg', '-nostdin', '-loglevel', 'error', '-y', '-ss', str(a.tin), '-i', a.clip, '-framerate', str(FPS),
                        '-i', f'{tmp}/f%04d.png', '-filter_complex',
                        f'[0:v]{vf}{cover}[b];[b][1:v]overlay={x}:{y}:shortest=1{zoom},format=yuv420p[v]', '-map', '[v]', '-an',
                        '-t', str(a.dur), '-c:v', 'libx264', '-crf', '18', '-preset', 'veryfast', a.out], check=True)
    print(a.out)


if __name__ == '__main__':
    main()
