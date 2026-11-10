"""Patch a small region of a phone screen in a Flow clip from a clean still, tracked (GPOM E round 9, at28).

    ~/.cache/badcode-lips/venv/bin/python -I phone_patch.py CLIP STILL OUT --at X,Y --r RX,RY --screen x0,y0,x1,y1

Omni draws the tiny robot on her phone as a glowing white disc in every take. The still the screen came from
(D's real last frame placed on the phone) shows it right, so: align the still to frame 0 (ORB + RANSAC homography
inside the screen box), track the screen from frame 0 to every frame (Lucas-Kanade + RANSAC similarity), and blend
the still's pixels into a soft ellipse around the robot. The rest of the screen, its glare and her hands stay Omni's.
"""
import subprocess, sys
import cv2, numpy as np
a = sys.argv[1:]
clip, still, out = a[0], a[1], a[2]
cx, cy = map(float, a[a.index('--at') + 1].split(','))
rx, ry = map(float, a[a.index('--r') + 1].split(','))
sx0, sy0, sx1, sy1 = map(int, a[a.index('--screen') + 1].split(','))
cap = cv2.VideoCapture(clip); fps = cap.get(cv2.CAP_PROP_FPS) or 24
frames = []
while True:
    ok, f = cap.read()
    if not ok: break
    frames.append(f)
H_, W_ = frames[0].shape[:2]
A = cv2.resize(cv2.imread(still), (W_, H_), interpolation=cv2.INTER_AREA)
mk = np.zeros((H_, W_), np.uint8); mk[sy0:sy1, sx0:sx1] = 255
g0 = cv2.cvtColor(frames[0], cv2.COLOR_BGR2GRAY); ga = cv2.cvtColor(A, cv2.COLOR_BGR2GRAY)
orb = cv2.ORB_create(3000)
k1, d1 = orb.detectAndCompute(ga, mk); k2, d2 = orb.detectAndCompute(g0, mk)
m = sorted(cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True).match(d1, d2), key=lambda x: x.distance)[:300]
H0, inl = cv2.findHomography(np.float32([k1[x.queryIdx].pt for x in m]), np.float32([k2[x.trainIdx].pt for x in m]),
                             cv2.RANSAC, 2.0)
print('still->frame0 inliers', int(inl.sum()), 'of', len(m))
p0 = cv2.goodFeaturesToTrack(g0, 300, 0.01, 5, mask=mk)
yy, xx = np.mgrid[0:H_, 0:W_]
mask0 = np.clip(1.6 - np.sqrt(((xx - cx) / rx) ** 2 + ((yy - cy) / ry) ** 2) * 1.6, 0, 1).astype(np.float32)
mask0 = cv2.GaussianBlur(mask0, (0, 0), 2)
ENC = ['-c:v', 'libx264', '-crf', '14', '-pix_fmt', 'yuv420p', '-color_range', 'tv', '-colorspace', 'bt709',
       '-color_primaries', 'bt709', '-color_trc', 'bt709', '-an']
enc = subprocess.Popen(['ffmpeg', '-loglevel', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'bgr24', '-s', f'{W_}x{H_}',
                        '-r', f'{fps:g}', '-i', '-', *ENC, out], stdin=subprocess.PIPE)
M = np.eye(3, dtype=np.float64)
for i, f in enumerate(frames):
    if i:
        g = cv2.cvtColor(f, cv2.COLOR_BGR2GRAY)
        p1, st, _ = cv2.calcOpticalFlowPyrLK(g0, g, p0, None, winSize=(21, 21), maxLevel=3)
        good = st.ravel() == 1
        M2, _ = cv2.estimateAffinePartial2D(p0[good], p1[good], method=cv2.RANSAC, ransacReprojThreshold=1.5)
        if M2 is not None: M = np.vstack([M2, [0, 0, 1]])
    T = M @ H0
    src = cv2.warpPerspective(A, T, (W_, H_), flags=cv2.INTER_LINEAR).astype(np.float32)
    w = cv2.warpPerspective(mask0, M, (W_, H_))[..., None]
    o = f.astype(np.float32) * (1 - w) + src * w
    enc.stdin.write(np.clip(o, 0, 255).astype(np.uint8).tobytes())
enc.stdin.close(); enc.wait(); print(out, len(frames), 'frames')
