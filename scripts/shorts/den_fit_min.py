#!/usr/bin/env python3
"""The Den: fit the minister's re-shot clips (MINE = the on-face pitch phrase, MINF = "I've got a good feeling").

2026-11-23, Jack: "the lip sycning is still off on the den fix it". For each clip x take: the take's phrases (loudness
runs) placed whole at one onset and one tempo (0.97-1.15); the first phrase must start 0 to +0.12 s after a real mouth
opening (late is forgiven, early is not; a held grin is not an opening). Scored at 24 fps: voice over an open/moving
mouth counts, voice over a shut mouth and a talking mouth with no voice cost. Prints the best few pairs.

    ~/.cache/badcode-lips/venv/bin/python scripts/shorts/den_fit_min.py <mouth-track dir>
"""
# style-lint: story=short-the-den
import json, pathlib, subprocess, sys
import numpy as np

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / 'scripts/drive'))
from localmap import localize  # noqa: E402

REPO = pathlib.Path(__file__).resolve().parents[2]
cfg = localize(json.loads((REPO / 'docs/stories/short-the-den/scenes/the-den/scene.json').read_text()))
AUD = pathlib.Path(cfg['media']) / 'audio'
TR = pathlib.Path(sys.argv[1])
F = 24
# (take, its slice in the file [s0, s1] holding the phrase(s) this clip carries)
# where each family's clips really speak (their own words, transcribed): the first phrase must start inside it
WIN = {'MINE': (0.7, 1.9), 'MINF': (2.5, 3.6)}
JOBS = {'MINE': [('lines/02-minister-pitch--b.wav', 2.2 * 1.07, 5.0 * 1.07), ('lines/02-minister-pitch--a.wav', None, None)],
        'MINF': [('lines/04-minister-feeling--b.wav', 0, None)]}


def env(f):
    x = np.frombuffer(subprocess.run(['ffmpeg', '-loglevel', 'error', '-i', str(f), '-ac', '1', '-ar', '48000', '-f', 'f32le', '-'],
                                     capture_output=True).stdout, np.float32)
    h = 480; r = 20 * np.log10(np.sqrt((x[:len(x) // h * h].reshape(-1, h) ** 2).mean(1)) + 1e-9)
    return r > r.max() - 32  # 100 Hz voice activity


def runs(b, gap=20):
    S, i = [], 0
    while i < len(b):
        if b[i]:
            j = i
            while j < len(b) and (b[j] or b[j:j + gap].any()): j += 1
            S.append((i / 100, j / 100)); i = j
        else: i += 1
    return [s for s in S if s[1] - s[0] > 0.08]


out = []
for fam, takes in JOBS.items():
    for clip in sorted(TR.glob(f'{fam}?-MIN.jpg.json')):
        sc = np.array([np.nan if g is None else g for g in json.loads(clip.read_text())['scaled']], float)
        if np.isnan(sc).mean() > 0.3: out.append((fam, clip.name[:5], 'untracked')); continue
        sc = np.nan_to_num(np.clip(sc, 0, 1)); mo = sc > 0.35
        mv = np.convolve(np.abs(np.diff(sc, prepend=sc[0])), np.ones(5) / 5, 'same'); mv = np.clip(mv / max(1e-6, np.percentile(mv, 90)), 0, 1)
        talk = np.maximum(mo * 0.5 + mv * 0.5, 0)
        opens = [i / F for i in range(1, len(sc)) if sc[i] >= 0.35 and sc[i - 1] < 0.35]
        starts = [q for q in opens if WIN[fam][0] <= q <= WIN[fam][1]]
        talk = talk * (np.arange(len(sc)) / F < WIN[fam][1] + 3.2)  # past the line, an open grin is not speech
        for take, s0, s1 in takes:
            if s0 is None and fam == 'MINE': continue
            act = env(AUD / take); ph = [p for p in runs(act) if p[0] >= (s0 or 0) - 0.05 and (s1 is None or p[1] <= s1 + 0.05)]
            if not ph: continue
            base = ph[0][0]; ph = [(a - base, b - base) for a, b in ph]
            best = None
            for tempo in np.arange(0.97, 1.151, 0.01):
                for o in starts:
                    for d in np.arange(0.0, 0.121, 1 / 48):
                        t0 = o + d; P = [(t0 + a / tempo, t0 + b / tempo) for a, b in ph]
                        if P[-1][1] > 7.95: continue
                        v = np.zeros(len(sc))
                        for a, b in P: v[int(a * F):int(b * F)] = 1
                        lo, hi = int(t0 * F) - 6, int(P[-1][1] * F) + 6
                        s = (v * talk).sum() - (v * (sc < 0.15)).sum() - 0.5 * ((1 - v[lo:hi]) * mv[lo:hi] * (talk[lo:hi] > 0.5)).sum()
                        pd = [round(min((a - q for q in opens if q <= a + 0.05), default=9), 2) for a, _ in P]
                        if best is None or s > best[0]: best = (round(float(s), 1), round(t0, 3), round(float(tempo), 2), pd)
            out.append((fam, clip.name[:5], take.split('/')[-1], best))
for r in sorted(out, key=lambda r: (r[0], -(r[3][0] if len(r) > 3 and r[3] else -99))): print(r)
