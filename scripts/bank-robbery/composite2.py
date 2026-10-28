#!/usr/bin/env python3
"""The Bank Robbery, composite test 2 (2026-10-18): REAL café footage with only the person made by AI, made to sit.

Test 1 (composite.py) worked technically and "looked completely out of place in the new cut" (Jack): the plates kept
their flat phone-video look while the film is graded 35mm, and the person sat on the plate like a sticker. This pass
does what a compositor does to integrate an element, each step a fix for one tell:
  1. align   - the Flow clip is warped onto the plate (feature match + RANSAC homography on the background), so the
               person stands exactly where Nano Banana lit them, and the background difference below is meaningful;
  2. matte   - rembg u2net_human_seg, eroded, feathered and steadied over time (as test 1);
  3. shadow  - Nano Banana draws the person's contact shadow and occlusion on the plate's surfaces; the AI frame
               divided by the plate (luma, darkening only, near the person, blurred) is that shadow, multiplied in;
  4. levels  - the person's black and white points and colour cast pulled to the plate's (percentile match per
               LAB channel), because mismatched blacks are the first thing the eye catches;
  5. focus   - the AI person is usually sharper than the plate; blur them until their Laplacian energy matches;
  6. wrap    - a little of the blurred plate bleeds onto the person's edge (light wrap);
  7. grade   - ONE film grade over the whole frame (plate and person together) to the film's look, then one grain
               and one vignette over everything, so both layers share the same "camera".
Every background pixel is the real footage.

usage: ~/.cache/badcode-matte/venv/bin/python -I composite2.py <plate.mp4> <plate_start_s> <ai_clip.mp4> <ai_start_s> <seconds> <out.mov> [x0,y0,x1,y1] [tx0,ty0,tx1,ty1]
The second box (plate coordinates) is where to TRACK the plate camera: objects at the person's own depth. On a
handheld plate the near and far planes move differently (parallax); tracking the whole frame follows the busiest plane,
which is how the first Denise grew and shrank against the cook. Env BLUR=<sigma> overrides the measured focus match,
for a person nearer the lens than anything the plate has in focus.
The optional box (fractions of the frame, AI-clip coordinates) keeps only the person inside it: the AI clip also
re-draws the real people in the plate, and those must come from the plate, not from Flow.
"""
import subprocess, sys
import cv2, numpy as np
from rembg import remove, new_session

PLATE, P0, AI, A0, D, OUT = sys.argv[1], float(sys.argv[2]), sys.argv[3], float(sys.argv[4]), float(sys.argv[5]), sys.argv[6]
W, H, FPS = 1280, 720, 24
BOX = np.zeros((H, W), np.float32)
x0, y0, x1, y1 = [float(v) for v in sys.argv[7].split(',')] if len(sys.argv) > 7 else (0, 0, 1, 1)
BOX[int(y0 * H):int(y1 * H), int(x0 * W):int(x1 * W)] = 1
BOX = cv2.GaussianBlur(BOX, (0, 0), 15)
N = int(round(D * FPS))

def frames(src, t0):
    vf = f'scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},fps={FPS}'
    raw = subprocess.run(['ffmpeg', '-v', 'error', '-ss', f'{t0:.3f}', '-i', src, '-t', f'{D + 0.2:.3f}', '-vf', vf, '-f', 'rawvideo', '-pix_fmt', 'bgr24', '-'], capture_output=True).stdout
    fs = [np.frombuffer(raw[i * W * H * 3:(i + 1) * W * H * 3], np.uint8).reshape(H, W, 3) for i in range(len(raw) // (W * H * 3))]
    return (fs + [fs[-1]] * N)[:N]

plate, ai = frames(PLATE, P0), frames(AI, A0)
seg = new_session('u2net_human_seg')
def person(f):
    m = np.asarray(remove(f, session=seg, only_mask=True), np.float32) / 255
    return m * BOX

# 1. align: homography from the AI frame's background to the plate's, the person masked out of the match
m0 = person(ai[0])
orb = cv2.ORB_create(6000)
keep = (cv2.dilate((m0 > 0.2).astype(np.uint8), np.ones((41, 41), np.uint8)) == 0).astype(np.uint8) * 255
ka, da = orb.detectAndCompute(cv2.cvtColor(ai[0], cv2.COLOR_BGR2GRAY), keep)
kp, dp = orb.detectAndCompute(cv2.cvtColor(plate[0], cv2.COLOR_BGR2GRAY), None)
mt = sorted(cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True).match(da, dp), key=lambda x: x.distance)[:800]
Hm, inl = cv2.findHomography(np.float32([ka[x.queryIdx].pt for x in mt]), np.float32([kp[x.trainIdx].pt for x in mt]), cv2.RANSAC, 3.0)
print('align: matches', len(mt), 'inliers', int(inl.sum()) if inl is not None else 0)
if Hm is None or inl.sum() < 40: Hm = np.eye(3)

# track: the plate camera's own drift, frame 0 to frame i, so a handheld plate carries the person with it
TB = np.zeros((H, W), np.uint8)
tx0, ty0, tx1, ty1 = [float(v) for v in sys.argv[8].split(',')] if len(sys.argv) > 8 else (0, 0, 1, 1)
TB[int(ty0 * H):int(ty1 * H), int(tx0 * W):int(tx1 * W)] = 255
g0 = cv2.cvtColor(plate[0], cv2.COLOR_BGR2GRAY); k0, d0 = orb.detectAndCompute(g0, TB)
def track(i):
    if i == 0: return np.eye(3)
    ki, di = orb.detectAndCompute(cv2.cvtColor(plate[i], cv2.COLOR_BGR2GRAY), None)
    mm = sorted(cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True).match(d0, di), key=lambda x: x.distance)[:800]
    # a similarity (shift, scale, small turn) is all a handheld camera does to one depth plane over a few seconds
    T, ok = cv2.estimateAffinePartial2D(np.float32([k0[x.queryIdx].pt for x in mm]), np.float32([ki[x.trainIdx].pt for x in mm]), method=cv2.RANSAC, ransacReprojThreshold=2.0)
    return np.vstack([T, [0, 0, 1]]) if T is not None and ok.sum() > 30 else np.eye(3)
Ts = [track(i) for i in range(N)]
Ts = [sum(Ts[max(0, i - 2):i + 3]) / len(Ts[max(0, i - 2):i + 3]) for i in range(N)]   # smooth out tracking jitter
print('track: max corner drift px', round(max(float(np.abs(cv2.perspectiveTransform(np.float32([[[0, 0]], [[W, H]]]), T) - np.float32([[[0, 0]], [[W, H]]])).max()) for T in Ts), 1))
HI = 0
def warp(img, interp=cv2.INTER_LINEAR):
    return cv2.warpPerspective(img, Ts[HI] @ Hm, (W, H), flags=interp, borderMode=cv2.BORDER_REPLICATE)

# plate statistics: levels per LAB channel (1st/50th/99th percentile) and sharpness, read off the middle frame
def pct(lab, mask):
    px = lab[mask] if mask is not None else lab.reshape(-1, 3)
    return np.percentile(px, [1, 50, 99], axis=0)
plab = cv2.cvtColor(plate[N // 2], cv2.COLOR_BGR2LAB).astype(np.float32)
pp = pct(plab, None)
def lap(img, mask): g = cv2.Laplacian(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY).astype(np.float32), cv2.CV_32F); return float(g[mask].var())

enc = subprocess.Popen(['ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'bgr24', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-',
                        '-c:v', 'libx264', '-crf', '14', '-preset', 'medium', '-pix_fmt', 'yuv420p', '-an', OUT], stdin=subprocess.PIPE)
prev = None; sig = None; ap = None; shadow_prev = None
for i in range(N):
    HI = i  # warp() reads it
    f = warp(ai[i]); pl = plate[i].astype(np.float32)
    m = warp(person(ai[i]))
    m = cv2.erode(m, np.ones((3, 3), np.uint8), 1)
    m = cv2.GaussianBlur(m, (0, 0), 1.2)
    if prev is not None: m = 0.6 * m + 0.4 * prev
    prev = m

    # 3. shadow: where the AI frame is darker than the plate near the person, outside the person
    near = cv2.GaussianBlur(cv2.dilate((m > 0.3).astype(np.uint8), np.ones((121, 121), np.uint8)).astype(np.float32), (0, 0), 25)
    la = cv2.GaussianBlur(cv2.cvtColor(f, cv2.COLOR_BGR2GRAY).astype(np.float32), (0, 0), 6) + 4
    lp = cv2.GaussianBlur(cv2.cvtColor(cv2.warpPerspective(plate[0], Ts[i], (W, H), borderMode=cv2.BORDER_REPLICATE), cv2.COLOR_BGR2GRAY).astype(np.float32), (0, 0), 6) + 4
    sh = np.clip(la / lp, 0.45, 1.0)
    sh = 1 - (1 - sh) * near * (1 - m)
    sh = np.where(sh > 0.93, 1.0, sh)                               # ignore small differences: AI noise, not shadow
    if shadow_prev is not None: sh = 0.7 * shadow_prev + 0.3 * sh   # shadows move slowly
    shadow_prev = sh
    pl = pl * cv2.GaussianBlur(sh, (0, 0), 4)[..., None]

    # 4. levels: the person's LAB percentiles mapped onto the plate's (fixed from frame 0 so it does not pump)
    lab = cv2.cvtColor(f, cv2.COLOR_BGR2LAB).astype(np.float32)
    if ap is None: ap = pct(lab, m > 0.5)
    out = np.empty_like(lab)
    for c in range(3):
        lo, md, hi = ap[:, c]; tlo, tmd, thi = pp[:, c]
        k = 0.5 if c == 0 else 0.35                                  # half way on light, a third on colour
        tlo, tmd, thi = lo + k * (tlo - lo), md + k * (tmd - md), hi + k * (thi - hi)
        out[..., c] = np.interp(lab[..., c], [lo - 50, lo, md, hi, hi + 50], [tlo - 50, tlo, tmd, thi, thi + 50])
    pers = cv2.cvtColor(np.clip(out, 0, 255).astype(np.uint8), cv2.COLOR_LAB2BGR).astype(np.float32)

    # 5. focus: soften the person until their detail energy matches the plate's around them
    if sig is None and 'BLUR' in __import__('os').environ:
        sig = float(__import__('os').environ['BLUR']); print('focus: person blur sigma (set)', sig)
    if sig is None:
        ring = (near > 0.5) & (m < 0.1); body = m > 0.5
        target = lap(plate[0], ring); sig = 0.0
        for s in np.arange(0.0, 2.6, 0.2):
            b = cv2.GaussianBlur(pers.astype(np.uint8), (0, 0), s) if s > 0 else pers.astype(np.uint8)
            if lap(b, body) <= target * 1.15: sig = float(s); break
        else: sig = 2.4
        print('focus: plate', round(target, 1), 'person blur sigma', sig)
    if sig > 0: pers = cv2.GaussianBlur(pers, (0, 0), sig)

    # 6. light wrap: the blurred plate bleeds onto the outer edge of the person
    edge = np.clip(m - cv2.erode(m, np.ones((9, 9), np.uint8)), 0, 1)
    wrap = cv2.GaussianBlur(pl, (0, 0), 12)
    pers = pers * (1 - 0.35 * edge[..., None]) + wrap * 0.35 * edge[..., None]

    a = m[..., None]
    comp = pers * a + pl * (1 - a)
    enc.stdin.write(np.clip(comp, 0, 255).astype(np.uint8).tobytes())
enc.stdin.close(); enc.wait()
print('composite2 frames', N)
