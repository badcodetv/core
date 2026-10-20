"""mouth-track.py clip.mp4 strip.jpg [--face big|left|right]   (2026-10-20, GPOM cut 3)
Per frame MediaPipe face -> inner-lip gap / face height and mouth centre. Prints a rescaled strip (10th-95th pct of the
clip's own gap; '#' > 55%, '+' > 25%, '.' below) and shut->open moments, and writes a 12 fps TRACKED mouth close-up strip
with timestamps (the skill's step 5, done on a moving head). Writes <strip>.json with the per-frame gap.
run with ~/.cache/badcode-lips/venv/bin/python"""
import sys, json, cv2, numpy as np
import os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'bank-robbery'))
import lips
clip, out = sys.argv[1], sys.argv[2]
face = sys.argv[sys.argv.index('--face') + 1] if '--face' in sys.argv else 'big'
lm = lips.landmarker(); crop = lips.find_crop(clip, lm, face)
cap = cv2.VideoCapture(clip); fps = cap.get(cv2.CAP_PROP_FPS) or 24
frames, g, ctr = [], [], []
while True:
    ok, fr = cap.read()
    if not ok: break
    frames.append(fr)
    fs = lips.detect(lm, fr, crop) if crop else []
    if not fs:  # head left the crop: search the whole frame grid again
        fs = lips.detect(lm, fr, (0, 0, 1, 1))
    if fs:
        size = lambda f: abs(f[152][1] - f[10][1]); f = max(fs, key=size)
        g.append(abs(f[14][1] - f[13][1]) / max(1e-6, size(f)))
        ctr.append(((f[13][0] + f[14][0]) / 2, (f[13][1] + f[14][1]) / 2, size(f)))
    else:
        g.append(None); ctr.append(None)
a = np.array([np.nan if x is None else x for x in g]); lo, hi = np.nanpercentile(a, 10), np.nanpercentile(a, 95)
r = (a - lo) / max(1e-6, hi - lo)
s = ''.join('?' if np.isnan(x) else '#' if x > .55 else '+' if x > .25 else '.' for x in r)
print(f'fps {fps} frames {len(s)} missing {int(np.isnan(a).sum())}')
for i in range(0, len(s), 48): print(f'{i / fps:6.2f} {s[i:i + 48]}')
ons = [i / fps for i in range(1, len(r)) if not np.isnan(r[i]) and not np.isnan(r[i - 1]) and r[i - 1] <= .25 and r[i] > .55 or (i > 1 and not np.isnan(r[i]) and r[i-2] <= .25 and r[i] > .55 and r[i-1] <= .55)]
print('opens:', ' '.join(f'{t:.2f}' for t in sorted(set(round(x, 2) for x in ons))))
# tracked strip
H, W = frames[0].shape[:2]; tiles = []; last = None
for i in range(0, len(frames), 2):
    c = ctr[i] or last
    if c is None: continue
    last = c; side = int(c[2] * H * 0.55); x, y = int(c[0] * W), int(c[1] * H)
    x0, y0 = max(0, x - side // 2), max(0, y - side // 2)
    t = cv2.resize(frames[i][y0:y0 + side, x0:x0 + side], (130, 130))
    cv2.putText(t, f'{i / fps:.2f}', (3, 14), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 255, 255), 1)
    tiles.append(t)
rows = [np.hstack(tiles[k:k + 16] + [np.zeros_like(tiles[0])] * (16 - len(tiles[k:k + 16]))) for k in range(0, len(tiles), 16)]
cv2.imwrite(out, np.vstack(rows))
json.dump({'fps': fps, 'gap': g, 'scaled': [None if np.isnan(x) else float(x) for x in r]}, open(out + '.json', 'w'))
