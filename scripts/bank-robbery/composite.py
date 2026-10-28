#!/usr/bin/env python3
"""The Bank Robbery, the composite test (2026-10-18): a REAL background plate with only the person made by AI.

Jack: "the setting should be real, but the ai person is the only thing ai". Method:
  1. a still made in Flow with a frame of the real plate as the reference and the Character placed in it, so the
     person is lit and placed for that street (Nano Banana 2);
  2. that still animated in Flow, Frames mode, camera locked (Omni Flash);
  3. here: the person cut out of every frame of the Flow clip (rembg, u2net_human_seg, local and free), the matte
     smoothed over time so the edge does not boil, the person's colour pulled toward the plate's, and laid over the
     REAL plate footage; the plate's own grain is left alone and a matching grain is put on the person.
Every background pixel in the output is the real footage.

usage: ~/.cache/badcode-matte/venv/bin/python -I composite.py <plate.mp4> <plate_start_s> <ai_clip.mp4> <ai_start_s> <seconds> <out.mov>
"""
import subprocess, sys
import cv2, numpy as np
from rembg import remove, new_session

PLATE, P0, AI, A0, D, OUT = sys.argv[1], float(sys.argv[2]), sys.argv[3], float(sys.argv[4]), float(sys.argv[5]), sys.argv[6]
W, H, FPS = 1280, 720, 24
N = int(round(D * FPS))

def frames(src, t0):
    vf = f'scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},fps={FPS}'
    raw = subprocess.run(['ffmpeg', '-v', 'error', '-ss', f'{t0:.3f}', '-i', src, '-t', f'{D + 0.2:.3f}', '-vf', vf, '-f', 'rawvideo', '-pix_fmt', 'bgr24', '-'], capture_output=True).stdout
    fs = [np.frombuffer(raw[i * W * H * 3:(i + 1) * W * H * 3], np.uint8).reshape(H, W, 3) for i in range(len(raw) // (W * H * 3))]
    return (fs + [fs[-1]] * N)[:N]

plate, ai = frames(PLATE, P0), frames(AI, A0)
seg = new_session('u2net_human_seg')

# colour: move the person's LAB mean and spread a third of the way toward the plate's, so the light reads as the same day
def lab_stats(img, mask=None):
    lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB).astype(np.float32)
    px = lab[mask > 0.5] if mask is not None else lab.reshape(-1, 3)
    return px.mean(0), px.std(0) + 1e-3
pm, ps = lab_stats(plate[N // 2])

enc = subprocess.Popen(['ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'bgr24', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-',
                        '-c:v', 'libx264', '-crf', '14', '-preset', 'medium', '-pix_fmt', 'yuv420p', '-an', OUT], stdin=subprocess.PIPE)
prev = None; rng = np.random.default_rng(3)
for i in range(N):
    f = ai[i]
    m = np.asarray(remove(f, session=seg, only_mask=True), np.float32) / 255
    m = cv2.erode(m, np.ones((3, 3), np.uint8), 1)                 # pull the edge in off the AI background
    m = cv2.GaussianBlur(m, (0, 0), 1.4)                           # a soft edge, as a lens gives
    if prev is not None: m = 0.6 * m + 0.4 * prev                 # steady the edge frame to frame
    prev = m
    if i == 0:
        am, as_ = lab_stats(f, m)
    lab = cv2.cvtColor(f, cv2.COLOR_BGR2LAB).astype(np.float32)
    k = 0.33
    lab = (lab - am) * (1 + k * (ps / as_ - 1)) + am + k * (pm - am)
    person = cv2.cvtColor(np.clip(lab, 0, 255).astype(np.uint8), cv2.COLOR_LAB2BGR).astype(np.float32)
    person += rng.normal(0, 3.0, person.shape[:2])[..., None]     # grain on the person, like the plate's
    a = m[..., None]
    out = person * a + plate[i].astype(np.float32) * (1 - a)
    enc.stdin.write(np.clip(out, 0, 255).astype(np.uint8).tobytes())
enc.stdin.close(); enc.wait()
print('composite frames', N)
