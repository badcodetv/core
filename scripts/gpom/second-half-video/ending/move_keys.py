"""A Premiere-style camera move over a clip, done exactly (sub-pixel, cubic), plus an optional fade to black.

    ~/.cache/badcode-lips/venv/bin/python -I move_keys.py IN OUT --in 0 --dur 14 \
        --keys "0:1.4:740:410,1.5:1.4:740:410,9.5:1:640:360" [--fade-out 12.6:1.3] [--fade-in 0:0.5]

Keys are time:scale:cx:cy (output time from --in, scale 1 = the full frame, cx/cy = the source pixel at the
centre of the output). Between keys every value eases with a smoothstep (ease in and out); before the first
and after the last key it holds. The centre is clamped so the frame never shows an edge. --fade-out T:D fades
to black from T over D s (--fade-in likewise from black). Writes OUT, video only, BT.709 limited range."""
import subprocess
import sys

import cv2
import numpy as np

a = sys.argv[1:]
src, out = a[0], a[1]


def opt(k, d=None):
    return a[a.index(k) + 1] if k in a else d


i0, dur = float(opt('--in', 0)), float(opt('--dur'))
keys = [tuple(float(v) for v in k.split(':')) for k in opt('--keys').split(',')]
fo = [float(v) for v in opt('--fade-out').split(':')] if opt('--fade-out') else None
fi = [float(v) for v in opt('--fade-in').split(':')] if opt('--fade-in') else None


def at(t):
    if t <= keys[0][0]:
        return keys[0][1:]
    for (ta, *va), (tb, *vb) in zip(keys, keys[1:]):
        if t <= tb:
            u = (t - ta) / (tb - ta)
            e = u * u * (3 - 2 * u)
            return tuple(x + (y - x) * e for x, y in zip(va, vb))
    return keys[-1][1:]


cap = cv2.VideoCapture(src)
fps = cap.get(cv2.CAP_PROP_FPS) or 24
W, H = int(cap.get(3)), int(cap.get(4))
cap.set(cv2.CAP_PROP_POS_FRAMES, int(round(i0 * fps)))
n = int(round(dur * fps))
ENC = ['-c:v', 'libx264', '-crf', '17', '-pix_fmt', 'yuv420p', '-color_range', 'tv', '-colorspace', 'bt709',
       '-color_primaries', 'bt709', '-color_trc', 'bt709', '-an']
enc = subprocess.Popen(['ffmpeg', '-loglevel', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'bgr24', '-s', f'{W}x{H}',
                        '-r', f'{fps:g}', '-i', '-', *ENC, out], stdin=subprocess.PIPE)
last = None
for k in range(n):
    ok, f = cap.read()
    if not ok:
        f = last  # past the source's end: hold the last frame (the caller should not ask for this)
    last = f
    t = k / fps
    z, cx, cy = at(t)
    hw, hh = W / 2 / z, H / 2 / z
    cx, cy = min(max(cx, hw), W - hw), min(max(cy, hh), H - hh)
    M = np.float32([[z, 0, W / 2 - z * cx], [0, z, H / 2 - z * cy]])
    g = cv2.warpAffine(f, M, (W, H), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REFLECT)
    gain = 1.0
    if fo and t >= fo[0]:
        gain *= max(0.0, 1 - (t - fo[0]) / fo[1])
    if fi and t < fi[0] + fi[1]:
        gain *= min(1.0, max(0.0, (t - fi[0]) / fi[1]))
    if gain < 1:
        g = (g.astype(np.float32) * gain + 0.5).astype(np.uint8)
    enc.stdin.write(g.tobytes())
enc.stdin.close()
enc.wait()
print(f'{out}: {n} frames, keys {keys}')
