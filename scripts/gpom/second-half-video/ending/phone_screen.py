"""Composite a still onto a phone screen that moves in a clip (GPOM ending, scene E, 2026-10-22).

    ~/.cache/badcode-lips/venv/bin/python -I phone_screen.py CLIP INSERT OUT --quad x0,y0,x1,y1,x2,y2,x3,y3
        [--t0 0] [--t1 8] [--fade 0.25] [--dim 0.8] [--skin-from 0.7] [--debug]

The quad is the screen's corners on the clip's first frame (TL, TR, BR, BL, full-res pixels). Each frame the
quad is carried forward by a homography fitted (RANSAC) to Lucas-Kanade features tracked from the previous
frame inside the phone's neighbourhood, so it follows hand shake and tilt. The insert is warped into the quad,
softened a touch and dimmed (a screen in a dark bus, never white), with a faint glow spilling round it; skin
(thumbs over the screen) is keyed back on top. Outside [t0, t1] the frame passes through; it fades out over
`fade` s before t1. --debug draws the tracked quad instead of compositing. Writes OUT (video only) and
OUT.json with the per-frame quads."""
import json
import subprocess
import sys

import cv2
import numpy as np

a = sys.argv[1:]
clip, insert, out = a[0], a[1], a[2]


def opt(k, d):
    return a[a.index(k) + 1] if k in a else d


quad0 = np.array([float(v) for v in opt('--quad', '').split(',')], np.float32).reshape(4, 2)
t0, t1 = float(opt('--t0', 0)), float(opt('--t1', 1e9))
fade, dim = float(opt('--fade', 0.25)), float(opt('--dim', 0.8))
skin_from = float(opt('--skin-from', 0.0))  # thumbs are keyed back only right of this fraction of the screen width
debug = '--debug' in a
white = float(opt('--white-key', 0))  # >0: once the screen goes white (Omni brightens it), find it by luma instead


def order_like(pts, ref):
    """The 4 points reordered to sit nearest the reference quad's corners (TL, TR, BR, BL)."""
    best, bd = pts, 1e18
    for k in range(4):
        for p in (pts, pts[::-1]):
            q = np.roll(p, k, 0)
            d = ((q - ref) ** 2).sum()
            if d < bd:
                best, bd = q, d
    return best.astype(np.float32)

cap = cv2.VideoCapture(clip)
fps = cap.get(cv2.CAP_PROP_FPS) or 24
W, H = int(cap.get(3)), int(cap.get(4))
ins = cv2.imread(insert)
ih, iw = ins.shape[:2]
src_q = np.float32([[0, 0], [iw, 0], [iw, ih], [0, ih]])
ENC = ['-c:v', 'libx264', '-crf', '17', '-pix_fmt', 'yuv420p', '-color_range', 'tv', '-colorspace', 'bt709',
       '-color_primaries', 'bt709', '-color_trc', 'bt709', '-an']
enc = subprocess.Popen(['ffmpeg', '-loglevel', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'bgr24', '-s', f'{W}x{H}',
                        '-r', f'{fps:g}', '-i', '-', *ENC, out], stdin=subprocess.PIPE)

quad = quad0.copy()
prev = None
quads = []
n = 0
while True:
    ok, f = cap.read()
    if not ok:
        break
    t = n / fps
    g = cv2.cvtColor(f, cv2.COLOR_BGR2GRAY)
    if prev is not None:
        # features in the phone's neighbourhood (the quad grown by 25%)
        c = quad.mean(0)
        grown = (quad - c) * 1.25 + c
        mask = np.zeros_like(g)
        cv2.fillConvexPoly(mask, grown.astype(np.int32), 255)
        p0 = cv2.goodFeaturesToTrack(prev, 200, 0.01, 4, mask=mask)
        if p0 is not None and len(p0) >= 8:
            p1, st, _ = cv2.calcOpticalFlowPyrLK(prev, g, p0, None, winSize=(21, 21), maxLevel=3)
            good = st.ravel() == 1
            if good.sum() >= 8:
                Hm, inl = cv2.findHomography(p0[good], p1[good], cv2.RANSAC, 2.0)
                if Hm is not None and inl.sum() >= 6:
                    nq = cv2.perspectiveTransform(quad[None], Hm)[0]
                    # reject wild jumps (a hand sweeping through)
                    if np.abs(nq - quad).max() < 25:
                        quad = nq.astype(np.float32)
    wmask = None
    if white > 0:
        c = quad.mean(0)
        grown = (quad - c) * 1.5 + c
        near = np.zeros_like(g)
        cv2.fillConvexPoly(near, grown.astype(np.int32), 255)
        ycc = cv2.cvtColor(f, cv2.COLOR_BGR2YCrCb)
        wm = ((ycc[..., 0] > white) & (np.abs(ycc[..., 1].astype(int) - 128) < 14)
              & (np.abs(ycc[..., 2].astype(int) - 128) < 18) & (near > 0)).astype(np.uint8)
        wm = cv2.morphologyEx(wm, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8))
        cnts, _ = cv2.findContours(wm, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        if cnts:
            big = max(cnts, key=cv2.contourArea)
            if cv2.contourArea(big) > 0.3 * cv2.contourArea(quad):
                quad = order_like(cv2.boxPoints(cv2.minAreaRect(cv2.convexHull(big))), quad)
                wmask = np.zeros_like(g)
                cv2.drawContours(wmask, [big], -1, 1, -1)
                wmask = cv2.dilate(wmask, np.ones((3, 3), np.uint8))
    prev = g
    quads.append(quad.round(2).tolist())
    if t0 <= t < t1:
        alpha = float(np.clip((t1 - t) / fade, 0, 1)) if fade > 0 else 1.0
        if debug:
            cv2.polylines(f, [quad.astype(np.int32)], True, (0, 0, 255), 2)
        else:
            M = cv2.getPerspectiveTransform(src_q, quad)
            warped = cv2.warpPerspective(ins, M, (W, H), flags=cv2.INTER_AREA, borderMode=cv2.BORDER_CONSTANT)
            warped = cv2.GaussianBlur(warped, (0, 0), 0.8).astype(np.float32)
            # screen look: dimmed, blacks lifted a little, faintly cool
            screen = warped * dim * np.float32([1.03, 1.0, 0.96]) + 6
            m = np.zeros((H, W), np.float32)
            cv2.fillConvexPoly(m, (quad * 4).astype(np.int32), 1.0, lineType=cv2.LINE_AA, shift=2)
            if wmask is not None:  # the white screen itself is the matte (thumbs over it are not white)
                m = wmask.astype(np.float32)
            m = cv2.GaussianBlur(m, (0, 0), 0.7)
            # skin on top of the screen (thumbs) stays
            ycc = cv2.cvtColor(f, cv2.COLOR_BGR2YCrCb).astype(np.float32)
            skin = ((ycc[..., 1] > 137) & (ycc[..., 1] < 178) & (ycc[..., 2] > 80) & (ycc[..., 2] < 128)
                    & (ycc[..., 0] > 45)).astype(np.float32)
            skin = cv2.GaussianBlur(cv2.morphologyEx(skin, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8)), (0, 0), 1.2)
            if skin_from > 0:
                band = np.zeros((H, W), np.float32)
                tl, tr, br, bl = quad
                cv2.fillConvexPoly(band, (np.float32([tl + (tr - tl) * skin_from, tr + (tr - tl) * 0.2,
                                                      br + (br - bl) * 0.2, bl + (br - bl) * skin_from]) * 4
                                          ).astype(np.int32), 1.0, lineType=cv2.LINE_AA, shift=2)
                skin = skin * band
            m = m * (1 - skin)
            glow = cv2.GaussianBlur(screen * (m[..., None] > 0), (0, 0), 14) * 0.18
            ff = f.astype(np.float32)
            comp = ff * (1 - m[..., None]) + screen * m[..., None]
            comp = comp + glow * (1 - m[..., None])
            f = np.clip(ff + (comp - ff) * alpha + 0.5, 0, 255).astype(np.uint8)
    enc.stdin.write(f.tobytes())
    n += 1
enc.stdin.close()
enc.wait()
json.dump({'clip': clip, 'insert': insert, 'fps': fps, 't0': t0, 't1': t1, 'quads': quads}, open(out + '.json', 'w'))
print(f'{out}: {n} frames; quad drift {np.abs(np.array(quads[-1]) - quad0).max():.1f}px')
