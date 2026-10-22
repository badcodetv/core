#!/usr/bin/env python3
"""Per-frame picture work for one timeline piece (GPOM ending, stage 4). Premiere-style moves done exactly, in float:

    ~/.cache/badcode-lips/venv/bin/python -I frameops.py spec.json

spec: {"src": clip or still, "still": false, "in": 0.0, "dur": 4.0, "out": "x.mp4",
       "gains": [r, g, b],                         # white-balance match (1.0 = none)
       "zoom": [[t_src, z], ...], "rot": [[t_src, deg], ...],   # keyframes in SOURCE time, cosine-eased between
       "glow": {"xy": [x, y] | null, "env": [per output frame 0..1], "r": 26},   # amber beacon bloom on his words
       "white": [[t_local, a], ...],               # mix to white (linear between points; no flash: >= 1 s ramps)
       "centre": [[t_src, x, y], ...],             # optional: the zoom's centre in pixels (eased), default frame centre;
                                                   # it is moved to the frame centre, so ease it back by z=1
       "grade": [r, g, b]}                         # optional: extra per-channel gain after the match (exposure)
Frames past the source's end hold its last frame (the move keeps running over them). Output 1280x720, 24 fps,
yuv420p, limited range, bt709, no audio. Needs cv2 + numpy (the lips venv has both)."""
import json
import subprocess
import sys

import cv2
import numpy as np

FPS, W, H = 24, 1280, 720
ENC = ['-an', '-r', '24', '-c:v', 'libx264', '-crf', '16', '-preset', 'medium', '-pix_fmt', 'yuv420p',
       '-color_range', 'tv', '-colorspace', 'bt709', '-color_primaries', 'bt709', '-color_trc', 'bt709']


def keyed(keys, t, default):
    """Cosine-eased value between keyframes [[t, v], ...]; flat outside them."""
    if not keys:
        return default
    if t <= keys[0][0]:
        return keys[0][1]
    for (t0, v0), (t1, v1) in zip(keys, keys[1:]):
        if t <= t1:
            u = (t - t0) / max(1e-9, t1 - t0)
            return v0 + (v1 - v0) * (1 - np.cos(np.pi * u)) / 2
    return keys[-1][1]


def linear(keys, t):
    if not keys:
        return 0.0
    ts, vs = zip(*keys)
    return float(np.interp(t, ts, vs))


def frames(spec):
    if spec.get('still'):
        im = cv2.cvtColor(cv2.imread(spec['src']), cv2.COLOR_BGR2RGB)
        im = cv2.resize(im, (W, H), interpolation=cv2.INTER_AREA)
        while True:
            yield im
    cmd = ['ffmpeg', '-loglevel', 'error', '-ss', f"{spec['in']:.4f}", '-i', spec['src'], '-vf',
           f'scale={W}:{H},fps={FPS}', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-']
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    last = None
    while True:
        b = p.stdout.read(W * H * 3)
        if len(b) < W * H * 3:
            break
        last = np.frombuffer(b, np.uint8).reshape(H, W, 3)
        yield last
    p.wait()
    while True:  # hold the last frame
        yield last


def amber_xy(im):
    """Centre of the brightest amber blob (Maddie's beacon)."""
    f = im.astype(np.float32)
    r, g, b = f[..., 0], f[..., 1], f[..., 2]
    score = (r > 170) & (g > 90) & (g < r - 25) & (b < g - 25)
    if score.sum() < 6:
        return None
    ys, xs = np.nonzero(score)
    w = r[ys, xs] + g[ys, xs]
    return [float((xs * w).sum() / w.sum()), float((ys * w).sum() / w.sum())]


def main():
    spec = json.load(open(sys.argv[1]))
    n = int(round(spec['dur'] * FPS))
    gains = np.array(spec.get('gains', [1, 1, 1]), np.float32)
    glow = spec.get('glow')
    enc = subprocess.Popen(['ffmpeg', '-loglevel', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s',
                            f'{W}x{H}', '-r', str(FPS), '-i', '-', *ENC, spec['out']], stdin=subprocess.PIPE)
    src = frames(spec)
    gxy = None
    for k in range(n):
        im = next(src)
        if im is None:
            raise SystemExit(f"{spec['src']}: no frames")
        x = im.astype(np.float32) * gains
        ts = spec['in'] + k / FPS
        if glow:
            if gxy is None:
                gxy = glow.get('xy') or amber_xy(im)
            e = glow['env'][k] if k < len(glow['env']) else 0.0
            if gxy is not None and e > 0.01:
                rad = glow.get('r', 26)
                yy, xx = np.ogrid[:H, :W]
                d2 = ((xx - gxy[0]) ** 2 + (yy - gxy[1]) ** 2) / (2 * rad ** 2)
                m = np.exp(-d2)[..., None] * e
                x = x + m * np.array([255, 150, 40], np.float32) * 0.55
        if spec.get('grade'):
            x = x * np.array(spec['grade'], np.float32)
        z = keyed(spec.get('zoom'), ts, 1.0)
        ck = spec.get('centre')
        cx = keyed([[k[0], k[1]] for k in ck], ts, W / 2) if ck else W / 2
        cy = keyed([[k[0], k[2]] for k in ck], ts, H / 2) if ck else H / 2
        a = keyed(spec.get('rot'), ts, 0.0)
        if abs(z - 1) > 1e-4 or abs(a) > 1e-4:
            M = cv2.getRotationMatrix2D((cx, cy), a, z)
            M[0, 2] += W / 2 - cx
            M[1, 2] += H / 2 - cy
            x = cv2.warpAffine(x, M, (W, H), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REFLECT)
        wa = linear(spec.get('white'), k / FPS)
        if wa > 0:
            x = x * (1 - wa) + 235 * wa
        enc.stdin.write(np.clip(x + 0.5, 0, 255).astype(np.uint8).tobytes())
    enc.stdin.close()
    enc.wait()
    print(json.dumps({'out': spec['out'], 'frames': n, 'glow_xy': gxy}))


if __name__ == '__main__':
    main()
