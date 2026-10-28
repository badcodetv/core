#!/usr/bin/env python3
"""Scene C's Premiere-style push in post (the hybrid method: Veo's camera is locked, the camera moves here).
Sub-pixel affine per frame (cv2, Lanczos), so there is no zoompan stair-step. (move.py beside it is another
stage's keyed mover; this one is cut_end.py's.)

    ~/.cache/badcode-lips/venv/bin/python -I push.py IN.mp4 OUT.mp4 --in 0.6 --dur 4.2 \
        --z0 1.0 --z1 1.06 --hold 1.5 --cx 0.5 --cy 0.35

Holds at z0 for `hold` seconds, then eases (smoothstep, in and out) to z1 by the end; the zoom centre (cx, cy,
fractions of the frame) stays fixed in frame, clamped so no edge ever shows.
"""
import argparse
import subprocess

import cv2
import numpy as np

ap = argparse.ArgumentParser()
ap.add_argument('src')
ap.add_argument('out')
ap.add_argument('--in', dest='i0', type=float, default=0.0)
ap.add_argument('--dur', type=float, required=True)
ap.add_argument('--z0', type=float, default=1.0)
ap.add_argument('--z1', type=float, required=True)
ap.add_argument('--hold', type=float, default=1.5)
ap.add_argument('--cx', type=float, default=0.5)
ap.add_argument('--cy', type=float, default=0.5)
ap.add_argument('--fps', type=int, default=24)
a = ap.parse_args()

W, H, FPS = 1280, 720, a.fps
n = int(round(a.dur * FPS))
ENC = ['-an', '-r', str(FPS), '-c:v', 'libx264', '-crf', '17', '-pix_fmt', 'yuv420p', '-color_range', 'tv',
       '-colorspace', 'bt709', '-color_primaries', 'bt709', '-color_trc', 'bt709']
dec = subprocess.Popen(['ffmpeg', '-loglevel', 'error', '-ss', f'{a.i0:.4f}', '-i', a.src, '-vf',
                        f'scale={W}:{H},fps={FPS}', '-frames:v', str(n), '-f', 'rawvideo', '-pix_fmt', 'bgr24', '-'],
                       stdout=subprocess.PIPE)
enc = subprocess.Popen(['ffmpeg', '-loglevel', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'bgr24', '-s', f'{W}x{H}',
                        '-r', str(FPS), '-i', '-', *ENC, a.out], stdin=subprocess.PIPE)
fsz = W * H * 3
last = None
for k in range(n):
    buf = dec.stdout.read(fsz)
    if len(buf) < fsz:
        buf = last  # hold the last frame if the source runs a frame short
    last = buf
    t = k / FPS
    u = 0.0 if t <= a.hold else min(1.0, (t - a.hold) / max(1e-6, a.dur - a.hold))
    e = u * u * (3 - 2 * u)
    z = a.z0 + (a.z1 - a.z0) * e
    px, py = a.cx * W, a.cy * H
    tx, ty = px - z * px, py - z * py
    tx = min(0.0, max(W - z * W, tx))
    ty = min(0.0, max(H - z * H, ty))
    M = np.array([[z, 0, tx], [0, z, ty]], np.float32)
    img = np.frombuffer(buf, np.uint8).reshape(H, W, 3)
    enc.stdin.write(cv2.warpAffine(img, M, (W, H), flags=cv2.INTER_LANCZOS4, borderMode=cv2.BORDER_REFLECT).tobytes())
enc.stdin.close()
enc.wait()
dec.wait()
print(f'{a.out}: {n} frames, z {a.z0}->{a.z1} after a {a.hold}s hold')
