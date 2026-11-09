#!/usr/bin/env python3
"""picture-warp.py <src.mp4> <in> <dur> <voice.wav> <voice_at> <out.mp4> [--lo 0.88] [--hi 1.14] [--pad 0.5] [--plot p.png]
(2026-11-06, GPOM scene A round 19, Kai at3436: "the synchronisation between them is off")

The voice stays whole and untouched (Kai r7: cutting audio up reads as choppy). Instead the PICTURE is re-timed, a little
and smoothly, so the mouth follows the voice syllable by syllable: dynamic time warping between the tracked mouth gap and
the voice loudness, then the path is smoothed and its local rate clamped to [lo, hi] (default 0.88-1.14 of real speed)
so the head never looks sped up or floaty. Frames are SAMPLED (no interpolation: minterpolate read as floaty, Karen r8).
The output is exactly <dur> long at 24 fps and starts on the frame nearest <in>; the warp may borrow up to <pad> s
of source before and after the cut. Prints the before/after mouth-voice offset per voiced run.
run with ~/.cache/badcode-lips/venv/bin/python"""
import sys, os, subprocess, json
import numpy as np, cv2, librosa

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lips

a = sys.argv[1:]
src, cin, dur, vwav, vat, out = a[0], float(a[1]), float(a[2]), a[3], float(a[4]), a[5]
opt = lambda k, d: float(a[a.index(k) + 1]) if k in a else d
LO, HI, PAD = opt('--lo', 0.88), opt('--hi', 1.14), opt('--pad', 0.5)
FPS = 24

cap = cv2.VideoCapture(src); sfps = cap.get(cv2.CAP_PROP_FPS) or 24
frames = []
while True:
    ok, fr = cap.read()
    if not ok: break
    frames.append(fr)
# resample source to 24 fps index space
N = len(frames); srcdur = N / sfps
idx = lambda t: min(N - 1, max(0, int(round(t * sfps))))
lm = lips.landmarker(); crop = lips.find_crop(src, lm, 'big')
g = []
for fr in frames:
    fs = lips.detect(lm, fr, crop) if crop else []
    if not fs: fs = lips.detect(lm, fr, (0, 0, 1, 1))
    if fs:
        size = lambda f: abs(f[152][1] - f[10][1]); f = max(fs, key=size)
        g.append(abs(f[14][1] - f[13][1]) / max(1e-6, size(f)))
    else: g.append(np.nan)
g = np.array(g); g = np.where(np.isnan(g), np.nanmedian(g), g)
lo_, hi_ = np.percentile(g, 10), np.percentile(g, 95)
m_src = np.clip((g - lo_) / max(1e-6, hi_ - lo_), 0, 1.3)

n = int(round(dur * FPS))
s0 = max(0.0, cin - PAD); s1 = min(srcdur, cin + dur + PAD)
J = np.arange(int(s0 * FPS), int(s1 * FPS))            # candidate source frames (24 fps grid)
mj = np.array([m_src[idx(j / FPS)] for j in J])
y, sr = librosa.load(vwav, sr=16000, offset=vat, duration=dur, mono=True)
hop = sr // FPS
db = np.array([20 * np.log10(np.sqrt(np.mean(y[i * hop:(i + 1) * hop] ** 2)) + 1e-6) if i * hop < len(y) else -120 for i in range(n)])
thr = max(db.max() - 30, -55)
v = np.clip((db - thr) / 30, 0, 1)
# smooth both a touch, then compare shapes (mouth gap leads loudness by ~1 frame physiologically; ignore)
sm = lambda x: np.convolve(x, np.ones(3) / 3, 'same')
mz, vz = sm(mj), sm(v)
mz = (mz - mz.mean()) / (mz.std() + 1e-6); vz = (vz - vz.mean()) / (vz.std() + 1e-6)

# DP: output frame i -> source position j (index into J). steps 0/1/2 with a penalty off 1. start near cin.
INF = 1e18; M = len(J); j_in = int(round(cin * FPS)) - J[0]
cost = np.abs(vz[:, None] - mz[None, :]) ** 1.0
D = np.full((n, M), INF); B = np.zeros((n, M), np.int8)
lam = 0.35
for j in range(M):
    D[0, j] = cost[0, j] + 0.08 * abs(j - j_in)
for i in range(1, n):
    for st, pen in ((1, 0.0), (0, lam), (2, lam)):
        prev = np.full(M, INF)
        if st == 0: prev = D[i - 1]
        else: prev[st:] = D[i - 1][:-st]
        cand = prev + pen + cost[i]
        better = cand < D[i]
        D[i][better] = cand[better]; B[i][better] = st
j = int(np.argmin(D[-1])); path = [j]
for i in range(n - 1, 0, -1):
    j -= B[i, j]; path.append(j)
path = np.array(path[::-1], float)
# smooth and clamp the local rate
k = 11
p = np.convolve(np.pad(path, (k // 2, k // 2), mode='edge'), np.ones(k) / k, 'valid')
for _ in range(3):
    d = np.clip(np.diff(p), LO, HI)
    p = np.concatenate([[p[0]], p[0] + np.cumsum(d)])
    # keep it close to the DTW path overall (re-anchor its mean)
    p += np.mean(path - p) * 0.5
    p = np.concatenate([[p[0]], p[0] + np.cumsum(np.clip(np.diff(p), LO, HI))])
p = np.clip(p, 0, M - 1)
src_t = (J[0] + p) / FPS

# report: per voiced run, offset of mouth vs voice before (straight) and after (warped)
def report(times):
    mm = np.array([m_src[idx(t)] for t in times])
    out_ = []
    vr = v > 0.2
    i = 0
    while i < n:
        if vr[i]:
            j2 = i
            while j2 < n and vr[j2]: j2 += 1
            if j2 - i >= 4:
                best = (0, -9)
                for L in range(-6, 7):
                    xs = [mm[q + L] if 0 <= q + L < n else 0 for q in range(max(0, i - 3), min(n, j2 + 3))]
                    ys = v[max(0, i - 3):min(n, j2 + 3)]
                    c = float(np.corrcoef(xs, ys)[0, 1]) if np.std(xs) > 0 else -9
                    if c > best[1]: best = (L, c)
                out_.append((round(i / FPS, 2), round(-best[0] / FPS, 3), round(best[1], 2)))
            i = j2
        else: i += 1
    return out_
straight = cin + np.arange(n) / FPS
rb = report(straight)
if '--anchors' in a:
    # piecewise-linear: move each voiced run's mouth burst to sit 0.03 s ahead of its voice, rate clamped [LO, HI]
    ts = [0.0] + [t for t, late, c in rb if c > 0.3] + [dur]
    sh = [0.0] + [(-late) + 0.03 for t, late, c in rb if c > 0.3] + [None]
    sh[-1] = sh[-2]
    tt = np.arange(n) / FPS
    want = cin + tt + np.interp(tt, ts, sh)
    # clamp rate forward from the first anchor
    src_t = [want[0]]
    for i in range(1, n):
        src_t.append(src_t[-1] + float(np.clip(want[i] - src_t[-1], LO / FPS, HI / FPS)))
    src_t = np.clip(np.array(src_t), 0, srcdur - 1 / sfps)
ra = report(src_t)
rate = np.diff(src_t) * FPS
print(json.dumps({'runs_before(t, voice_late_s, corr)': rb, 'runs_after': ra,
                  'rate_min': round(float(rate.min()), 3), 'rate_max': round(float(rate.max()), 3),
                  'src_start': round(float(src_t[0]), 3), 'src_end': round(float(src_t[-1]), 3)}))
H, W = frames[0].shape[:2]
pr = subprocess.Popen(['ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'bgr24', '-s', f'{W}x{H}', '-r', str(FPS),
                       '-i', '-', '-c:v', 'libx264', '-crf', '14', '-pix_fmt', 'yuv420p', out], stdin=subprocess.PIPE)
for t in src_t:
    pr.stdin.write(frames[idx(t)].tobytes())
pr.stdin.close(); pr.wait()
json.dump({'src': src, 'in': cin, 'dur': dur, 'voice': vwav, 'voice_at': vat, 'map': [round(float(x), 4) for x in src_t],
           'lo': LO, 'hi': HI, 'before': rb, 'after': ra}, open(out + '.warp.json', 'w'))
