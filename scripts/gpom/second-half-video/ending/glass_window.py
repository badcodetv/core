#!/usr/bin/env python3
"""A soft power window darkened over part of a clip (Premiere's 'mask + Lumetri' done in ffmpeg/cv2).

    ~/.cache/badcode-lips/venv/bin/python -I glass_window.py IN.mp4 OUT.mp4 --rect 0,190,368,545 \
        --feather 28 --gain 0.28 --desat 0.8

Scene C, C07 (review round 1): Maddie's reflection in the black glass left of the doorway read as a second robot
waiting inside. The window darkens that glass by (1 - gain) and pulls its saturation down by `desat`, so the warm
beacon hot spot in the reflection goes too; the doorway glow and the step stay outside the window. Every frame,
the same fixed window (the camera does not move in C07)."""
import argparse
import subprocess

import cv2
import numpy as np

ap = argparse.ArgumentParser()
ap.add_argument('src')
ap.add_argument('out')
ap.add_argument('--rect', required=True, help='x0,y0,x1,y1 in 1280x720 pixels')
ap.add_argument('--feather', type=float, default=28)
ap.add_argument('--gain', type=float, default=0.28)
ap.add_argument('--desat', type=float, default=0.8)
a = ap.parse_args()

W, H, FPS = 1280, 720, 24
x0, y0, x1, y1 = (int(v) for v in a.rect.split(','))
m = np.zeros((H, W), np.float32)
m[y0:y1, x0:x1] = 1.0
k = int(a.feather * 3) | 1
m = cv2.GaussianBlur(m, (k, k), a.feather)[..., None]
ENC = ['-an', '-r', str(FPS), '-c:v', 'libx264', '-crf', '15', '-pix_fmt', 'yuv420p', '-color_range', 'tv',
       '-colorspace', 'bt709', '-color_primaries', 'bt709', '-color_trc', 'bt709']
dec = subprocess.Popen(['ffmpeg', '-loglevel', 'error', '-i', a.src, '-vf', f'scale={W}:{H},fps={FPS}', '-f',
                        'rawvideo', '-pix_fmt', 'bgr24', '-'], stdout=subprocess.PIPE)
enc = subprocess.Popen(['ffmpeg', '-loglevel', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'bgr24', '-s', f'{W}x{H}',
                        '-r', str(FPS), '-i', '-', *ENC, a.out], stdin=subprocess.PIPE)
fsz, n = W * H * 3, 0
while True:
    buf = dec.stdout.read(fsz)
    if len(buf) < fsz:
        break
    img = np.frombuffer(buf, np.uint8).reshape(H, W, 3).astype(np.float32)
    grey = img.mean(axis=2, keepdims=True)
    graded = (img + (grey - img) * a.desat) * a.gain
    out = img * (1 - m) + graded * m
    enc.stdin.write(np.clip(out, 0, 255).astype(np.uint8).tobytes())
    n += 1
enc.stdin.close()
enc.wait()
dec.wait()
print(f'{a.out}: {n} frames, window {a.rect} feather {a.feather} gain {a.gain} desat {a.desat}')
