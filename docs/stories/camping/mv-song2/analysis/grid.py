"""Check the beat grid against the actual drums (2026-11-07, Jack: "the cutting/trimming does not match the beat").
librosa's beat list (beats-new.json) is quantised to its 23 ms hop and was never checked for phase. This fits ONE steady grid
to the percussive onsets at 5.8 ms resolution, measures drift, then finds where the kick and the snare sit in the bar.

    ~/.venvs/whisper/bin/python grid.py      → grid.json
"""
import json, numpy as np, librosa
from pathlib import Path
HERE = Path(__file__).parent
SONG = '/mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/songs/camping vid/action/song 2 maybe (audio).wav'
SR, HOP = 22050, 128
y, _ = librosa.load(SONG, sr=SR, mono=True)
_, perc = librosa.effects.hpss(y, margin=2.0)
S = np.abs(librosa.stft(perc, n_fft=1024, hop_length=HOP))
f = librosa.fft_frequencies(sr=SR, n_fft=1024)
def env(lo, hi):
    e = np.diff(np.log1p(S[(f >= lo) & (f < hi)].sum(0)), prepend=0)
    e = np.maximum(e, 0); return e / (e.max() + 1e-9)
kick, snare, full = env(30, 150), env(1500, 6000), env(30, 11000)
fps = SR / HOP; T = np.arange(len(full)) / fps

def comb(e, period, phase):  # mean onset strength at grid points
    t = np.arange(phase, T[-1], period); idx = np.round(t * fps).astype(int); idx = idx[idx < len(e)]
    w = 3; return np.mean([e[max(0, i - w):i + w + 1].max() for i in idx])

best = (0, None, None)
for period in np.arange(0.340, 0.356, 0.0002):
    for phase in np.arange(0, period, 0.003):
        s = comb(full, period, phase)
        if s > best[0]: best = (s, period, phase)
_, P, PH = best
# local drift: per 32-beat window, best phase offset against the global grid
drift = []
for k in range(0, int(T[-1] / P) - 32, 16):
    t0 = PH + k * P
    offs = np.arange(-0.04, 0.0401, 0.002)
    sc = []
    for o in offs:
        t = t0 + o + np.arange(32) * P; idx = np.round(t * fps).astype(int); idx = idx[(idx >= 0) & (idx < len(full))]
        sc.append(np.mean([full[max(0, i - 2):i + 3].max() for i in idx]))
    drift.append([round(t0, 2), round(float(offs[int(np.argmax(sc))]) * 1000)])
# where kick and snare sit, by grid position mod 8 (two bars of 4 at 172, or one bar of 4 at 86)
n = int((T[-1] - PH) / P)
grid = PH + np.arange(n) * P
def at(e, t): i = int(round(t * fps)); return float(e[max(0, i - 3):i + 4].max())
K = np.array([at(kick, t) for t in grid]); Sn = np.array([at(snare, t) for t in grid])
pos = {m: {'kick': round(float(K[m::8].mean()), 3), 'snare': round(float(Sn[m::8].mean()), 3)} for m in range(8)}
old = np.array(json.load(open(HERE / 'beats-new.json'))['beats'])
err = [(b - grid[np.argmin(abs(grid - b))]) * 1000 for b in old]
out = {'period': round(P, 5), 'bpm': round(60 / P, 2), 'phase': round(PH, 4), 'beats': [round(t, 4) for t in grid],
       'by_position_mod8': pos, 'drift_ms_per_16_beats': drift,
       'old_beats_vs_grid_ms': {'mean': round(float(np.mean(err)), 1), 'abs_mean': round(float(np.mean(np.abs(err))), 1),
                                'max': round(float(np.max(np.abs(err))), 1)}}
json.dump(out, open(HERE / 'grid.json', 'w'), indent=1)
print(json.dumps({k: v for k, v in out.items() if k not in ('beats', 'drift_ms_per_16_beats')}, indent=1))
d = [x[1] for x in drift]; print('drift ms: min', min(d), 'max', max(d), 'median', np.median(d))
