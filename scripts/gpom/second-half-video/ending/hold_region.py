#!/usr/bin/env python3
"""Hold one region of a camera-locked clip still: every frame before --until shows that region as it is AT --until
(a feathered box), so something Veo/Omni moved (Maddie sliding down the hill in C06, Kai at794, 4 Nov) stays put
while the rest of the shot (the building's light, the crowd, the grass) keeps playing. From --until on, the clip
plays untouched, so there is no join.

    ~/.cache/badcode-lips/venv/bin/python -I hold_region.py IN.mp4 OUT.mp4 --until 5.0 --box 285,345,755,625 --feather 14
"""
import argparse
import subprocess

import cv2
import numpy as np

ap = argparse.ArgumentParser()
ap.add_argument('src')
ap.add_argument('out')
ap.add_argument('--until', type=float, required=True, help='seconds: the frame whose region is held before it')
ap.add_argument('--box', required=True, help='x0,y0,x1,y1 in pixels')
ap.add_argument('--feather', type=int, default=14)
ap.add_argument('--fps', type=int, default=24)
a = ap.parse_args()

W, H, FPS = 1280, 720, a.fps
ENC = ['-an', '-r', str(FPS), '-c:v', 'libx264', '-crf', '17', '-pix_fmt', 'yuv420p', '-color_range', 'tv',
       '-colorspace', 'bt709', '-color_primaries', 'bt709', '-color_trc', 'bt709']
raw = subprocess.run(['ffmpeg', '-loglevel', 'error', '-i', a.src, '-vf', f'scale={W}:{H},fps={FPS}', '-f', 'rawvideo',
                      '-pix_fmt', 'bgr24', '-'], capture_output=True, check=True).stdout
fr = np.frombuffer(raw, np.uint8).reshape(-1, H, W, 3)
k = int(round(a.until * FPS))
x0, y0, x1, y1 = (int(v) for v in a.box.split(','))
mask = np.zeros((H, W), np.float32)
mask[y0:y1, x0:x1] = 1.0
f = a.feather
mask = cv2.GaussianBlur(cv2.erode(mask, np.ones((f, f), np.uint8)), (0, 0), f / 2)[..., None]
held = fr[k].astype(np.float32)
enc = subprocess.Popen(['ffmpeg', '-loglevel', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'bgr24', '-s', f'{W}x{H}',
                        '-r', str(FPS), '-i', '-', *ENC, a.out], stdin=subprocess.PIPE)
for i, x in enumerate(fr):
    if i < k:
        x = (x.astype(np.float32) * (1 - mask) + held * mask).round().clip(0, 255).astype(np.uint8)
    enc.stdin.write(np.ascontiguousarray(x).tobytes())
enc.stdin.close()
enc.wait()
print(f'{a.out}: {len(fr)} frames, region {a.box} held at frame {k} for frames 0-{k - 1}')
