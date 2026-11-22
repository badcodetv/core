#!/usr/bin/env python3
"""The Starting Gate outro: the BadCode logo spray-painted on the flank of a walking horse (Jack, 2026-11-22: "like the
beer outro, something like that but horse themed, like it is sprayed on the side of a horse and it is moving").

The clip is real-looking footage (Flow); the logo is the official brand file (docs/brand/logo/badcode-stacked-reversed-
2400.png), never redrawn: it is only warped, shaded and textured so it reads as paint on the coat.

  1. Track: corners on the flank (inside an ellipse round the logo's place) are followed frame to frame with
     Lucas-Kanade optical flow; each step's similarity (move, turn, scale) is fitted with RANSAC and chained; the
     chain is smoothed over time so muscle ripple doesn't shake the paint.
  2. Paint: the logo's alpha is softened (a sprayed edge, not a sticker) with a faint speckled overspray halo; its
     colour takes the coat's own light and shade (paint on a barrel-shaped body) and the hair's fine texture shows
     through; opacity just under full.

    ~/.cache/badcode-lips/venv/bin/python scripts/shorts/gate_flank_logo.py <clip.mp4> <out.mp4> \
        --in 0.5 --dur 4.0 --cx 560 --cy 900 --w 420 [--rot 0] [--fade 0.4] [--debug sheet.jpg]

--cx/--cy/--w/--rot place the logo on the first used frame in 1080x1920 output pixels. Writes picture only (no audio).
"""
import argparse, pathlib, subprocess
import cv2
import numpy as np

REPO = pathlib.Path(__file__).resolve().parents[2]
LOGO = REPO / 'docs/brand/logo/badcode-stacked-reversed-2400.png'
W, H, FPS = 1080, 1920, 24


def frames(clip, t0, dur):
    p = subprocess.run(['ffmpeg', '-nostdin', '-loglevel', 'error', '-ss', str(t0), '-i', str(clip), '-t', str(dur + 0.2),
                        '-vf', f'scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},fps={FPS}',
                        '-f', 'rawvideo', '-pix_fmt', 'bgr24', '-'], capture_output=True, check=True).stdout
    fs = np.frombuffer(p, np.uint8).reshape(-1, H, W, 3)
    return fs[:round(dur * FPS)]


def track(fs, cx, cy, rx, ry):
    """Per-frame 2x3 similarity mapping frame 0 to frame i, smoothed."""
    g0 = cv2.cvtColor(fs[0], cv2.COLOR_BGR2GRAY)
    mask = np.zeros_like(g0); cv2.ellipse(mask, (int(cx), int(cy)), (int(rx), int(ry)), 0, 0, 360, 255, -1)
    A = [np.float32([[1, 0, 0], [0, 1, 0]])]
    prev, cur = g0, np.eye(3, dtype=np.float64)
    pts = cv2.goodFeaturesToTrack(prev, 400, 0.01, 7, mask=mask)
    for i in range(1, len(fs)):
        g = cv2.cvtColor(fs[i], cv2.COLOR_BGR2GRAY)
        if pts is None or len(pts) < 40:   # refill inside the ellipse carried to the current place
            m = np.zeros_like(g)
            c = cur @ np.array([cx, cy, 1.0])
            cv2.ellipse(m, (int(c[0]), int(c[1])), (int(rx), int(ry)), 0, 0, 360, 255, -1)
            pts = cv2.goodFeaturesToTrack(prev, 400, 0.01, 7, mask=m)
        nxt, st, _ = cv2.calcOpticalFlowPyrLK(prev, g, pts, None, winSize=(31, 31), maxLevel=4)
        ok = st.ravel() == 1
        M, inl = cv2.estimateAffinePartial2D(pts[ok], nxt[ok], method=cv2.RANSAC, ransacReprojThreshold=2.0)
        if M is None:
            M = np.float32([[1, 0, 0], [0, 1, 0]])
        cur = np.vstack([M, [0, 0, 1]]) @ cur
        A.append(cur[:2].astype(np.float32))
        pts = nxt[ok][inl.ravel() == 1].reshape(-1, 1, 2) if inl is not None else None
        prev = g
    # smooth (scale, angle, tx, ty) over time
    P = np.array([[np.hypot(a[0, 0], a[1, 0]), np.arctan2(a[1, 0], a[0, 0]), a[0, 2], a[1, 2]] for a in A])
    k = cv2.getGaussianKernel(9, 2.0).ravel()
    pad = np.pad(P, ((4, 4), (0, 0)), mode='edge')
    S = np.stack([np.convolve(pad[:, j], k, mode='valid') for j in range(4)], 1)
    out = []
    for s, th, tx, ty in S:
        out.append(np.float32([[s * np.cos(th), -s * np.sin(th), tx], [s * np.sin(th), s * np.cos(th), ty]]))
    return out, P


def paint_layer(cx, cy, w, rot):
    """The logo placed on frame 0 as a full-frame BGRA float layer, with a soft sprayed edge and overspray."""
    lg = cv2.imread(str(LOGO), cv2.IMREAD_UNCHANGED).astype(np.float32) / 255
    h = round(lg.shape[0] * w / lg.shape[1])
    lg = cv2.resize(lg, (int(w), h), interpolation=cv2.INTER_AREA)
    M = cv2.getRotationMatrix2D((w / 2, h / 2), -rot, 1.0); M[0, 2] += cx - w / 2; M[1, 2] += cy - h / 2
    lay = cv2.warpAffine(lg, M, (W, H), flags=cv2.INTER_LINEAR, borderValue=(0, 0, 0, 0))
    a = lay[..., 3]
    soft = cv2.GaussianBlur(a, (0, 0), 1.6)                                   # a sprayed edge
    rng = np.random.default_rng(3)
    speck = (rng.random(a.shape) < 0.18).astype(np.float32)
    halo = np.clip(cv2.GaussianBlur(a, (0, 0), 7) - soft, 0, 1) * speck * 0.35   # faint dotted overspray
    lay[..., 3] = np.clip(np.maximum(soft, halo), 0, 1)
    # colour under the halo: the nearest paint colour (white or red), blurred out
    rgb = cv2.GaussianBlur(lay[..., :3] * a[..., None], (0, 0), 7) / np.maximum(cv2.GaussianBlur(a, (0, 0), 7), 1e-3)[..., None]
    lay[..., :3] = np.where(a[..., None] > 0.05, lay[..., :3], rgb)
    return lay


def composite(frame, lay, opacity=0.9):
    f = frame.astype(np.float32) / 255
    L = cv2.cvtColor(f, cv2.COLOR_BGR2GRAY)
    base = cv2.GaussianBlur(L, (0, 0), 25)
    mean = float(np.sum(base * lay[..., 3]) / max(np.sum(lay[..., 3]), 1e-3))
    shade = np.clip(base / max(mean, 1e-3), 0.65, 1.2)                          # the body's own light and shade
    hair = (L - cv2.GaussianBlur(L, (0, 0), 1.5)) * 2.2                         # fine coat texture through the paint
    paint = lay[..., :3] * (0.9 * shade)[..., None] + hair[..., None]
    paint = paint * np.array([0.95, 0.96, 0.98], np.float32)                   # grey daylight on white paint
    a = (lay[..., 3] * opacity)[..., None]
    return np.clip(f * (1 - a) + paint * a, 0, 1)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('clip'); ap.add_argument('out')
    ap.add_argument('--in', dest='tin', type=float, default=0.0); ap.add_argument('--dur', type=float, default=4.0)
    ap.add_argument('--cx', type=float, required=True); ap.add_argument('--cy', type=float, required=True)
    ap.add_argument('--w', type=float, required=True); ap.add_argument('--rot', type=float, default=0.0)
    ap.add_argument('--fade', type=float, default=0.4, help='fade to black over the last N s')
    ap.add_argument('--opacity', type=float, default=0.9)
    ap.add_argument('--debug', help='write a contact sheet of every 12th frame with the track drawn')
    a = ap.parse_args()
    fs = frames(a.clip, a.tin, a.dur)
    lg = cv2.imread(str(LOGO), cv2.IMREAD_UNCHANGED); lh = a.w * lg.shape[0] / lg.shape[1]
    Ms, raw = track(fs, a.cx, a.cy, a.w * 0.75, lh * 0.7)
    lay0 = paint_layer(a.cx, a.cy, a.w, a.rot)
    enc = subprocess.Popen(['ffmpeg', '-nostdin', '-loglevel', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'bgr24', '-s', f'{W}x{H}',
                            '-r', str(FPS), '-i', '-', '-vf', 'scale=in_range=full:out_range=limited,format=yuv420p,lutyuv=y=clip(val\\,20\\,235)',
                            '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '18', '-pix_fmt', 'yuv420p', '-color_range', 'tv',
                            '-colorspace', 'bt709', '-color_primaries', 'bt709', '-color_trc', 'bt709', a.out], stdin=subprocess.PIPE)
    sheet = []
    n = len(fs)
    for i, (f, M) in enumerate(zip(fs, Ms)):
        lay = cv2.warpAffine(lay0, M, (W, H), flags=cv2.INTER_LINEAR, borderValue=(0, 0, 0, 0))
        img = composite(f, lay, a.opacity)
        t = i / FPS; d = a.dur - t
        if a.fade and d < a.fade:
            img = img * max(0.0, d / a.fade)
        o = (img * 255).astype(np.uint8)
        enc.stdin.write(o.tobytes())
        if a.debug and i % 12 == 0:
            s = o.copy(); c = M @ np.array([a.cx, a.cy, 1.0])
            cv2.circle(s, (int(c[0]), int(c[1])), 8, (0, 255, 255), 3)
            cv2.putText(s, f'{t:.2f}', (20, 60), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 255), 3)
            sheet.append(cv2.resize(s, (270, 480)))
    enc.stdin.close(); enc.wait()
    if a.debug and sheet:
        while len(sheet) % 6:
            sheet.append(np.zeros_like(sheet[0]))
        cv2.imwrite(a.debug, np.vstack([np.hstack(sheet[r:r + 6]) for r in range(0, len(sheet), 6)]))
    drift = np.ptp(raw[:, 2]), np.ptp(raw[:, 3])
    print({'frames': n, 'track_move_px': [round(float(x), 1) for x in drift], 'out': a.out})


if __name__ == '__main__':
    main()
