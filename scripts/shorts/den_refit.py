#!/usr/bin/env python3
"""The Den: picture-side lip-sync refit (Jack, 2026-11-23: "fix the lip syncing").

Rough cut 2 measured on the assembled preview (row-measure.py): every "I'm out" 0.25-0.33 s early against the mouth,
the nurse with 1.2 s of voice over a shut mouth. The voices stay exactly where they are on the timeline; only each
talking shot's in-point into its clip moves. For each shot, every in-point in the clip is scored at 24 fps against the
cut's own voice stem: voice over a moving/open mouth scores, voice over a shut mouth and a talking mouth with no voice
cost, and the first voice onset in the shot must land 0 to +0.15 s after a mouth opening (late is forgiven, early is not).
Clips whose face can't be tracked (INVCa, a wide) fall back to the clip's own audio onset.

    ~/.cache/badcode-lips/venv/bin/python scripts/shorts/den_refit.py <cut dir> <mouth-track dir>  -> prints the in-points
"""
# style-lint: story=short-the-den
import json, pathlib, subprocess, sys
import numpy as np

FPS = 24
cut, tracks = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
edl = json.loads((cut / 'edl.json').read_text())
VID = cut.parent.parent / 'video'
# shot beat -> (clip key, earliest clip time speech may start: MIN2a holds a parted grin until 3.42 s)
SHOTS = {'pitch': ('MIN1a-MIN', 0.0), 'feeling': ('MIN2a-MIN', 3.3), 'outa': ('INVAb-INVA', 0.0),
         'outc': ('INVCa-INVC', 0.0), 'outd': ('INVDa-INVD', 0.0), 'nurse': ('NURSEc-NURSE', 0.0)}


def env(path, start=0.0, dur=None):
    a = ['ffmpeg', '-nostdin', '-loglevel', 'error', '-ss', str(start), *(['-t', str(dur)] if dur else []), '-i', str(path),
         '-ac', '1', '-ar', '48000', '-f', 'f32le', '-']
    x = np.frombuffer(subprocess.run(a, capture_output=True, check=True).stdout, np.float32)
    hop = 48000 // FPS; n = len(x) // hop
    r = np.sqrt((x[:n * hop].reshape(n, hop) ** 2).mean(1) + 1e-12)
    db = 20 * np.log10(r); return db


def active(db):
    return (db > db.max() - 30).astype(float)


def onsets(b):
    return [i for i in range(1, len(b)) if b[i] and not b[i - 1]] + ([0] if len(b) and b[0] else [])


vox = env(cut / 'vox.wav')
out = {}
for v in edl['video']:
    if v['beat'] not in SHOTS: continue
    key, earliest = SHOTS[v['beat']]
    s0, n = round(v['start'] * FPS), round(v['dur'] * FPS)
    va = active(vox[s0:s0 + n])
    von = sorted(onsets(va))
    tj = json.loads((tracks / f'{key}.jpg.json').read_text())
    sc = np.array([np.nan if g is None else g for g in tj['scaled']], float)
    miss = np.isnan(sc).mean()
    if miss > 0.3:  # untracked: the clip's own audio is the mouth (lag 0)
        own = env(VID / f'the-den-{key}.mp4'); m = active(own); mv = m; how = f'own audio ({miss:.0%} untracked)'
    else:
        sc = np.nan_to_num(np.clip(sc, 0, 1), nan=0.0)
        mo = (sc > 0.35).astype(float)
        motion = np.convolve(np.abs(np.diff(sc, prepend=sc[0])), np.ones(5) / 5, 'same')
        mv = np.clip(motion / max(1e-6, np.percentile(motion, 90)), 0, 1)
        m = np.maximum(mo * 0.5 + mv * 0.5, 0); how = 'tracked mouth'
    mon = [i for i in onsets((m > 0.45).astype(float)) if i / FPS >= earliest]
    best = None
    for c in range(0, len(m) - n + 1):
        mm = m[c:c + n]
        if von and mon:
            first = von[0] + c  # clip frame of the first voice onset
            prior = [o for o in mon if o <= first + 1]
            if not prior or (first - max(prior)) / FPS > 0.15 or (first - max(prior)) / FPS < -0.045: continue
            if (c + von[0]) / FPS < earliest: continue
        score = (va * mm).sum() - 1.0 * (va * (1 - mm)).sum() - 0.5 * ((1 - va) * mv[c:c + n] * (mm > 0.5)).sum()
        if best is None or score > best[0]: best = (score, c)
    cur = round(v['in'] * FPS)
    cs = lambda c: (va * m[c:c + n]).sum() - (va * (1 - m[c:c + n])).sum() - 0.5 * ((1 - va) * mv[c:c + n] * (m[c:c + n] > 0.5)).sum()
    out[v['beat']] = {'clip': key, 'how': how, 'in_was': v['in'], 'score_was': round(float(cs(cur)), 1),
                      'in_new': None if best is None else round(best[1] / FPS, 3),
                      'score_new': None if best is None else round(float(best[0]), 1)}
    print(v['beat'], json.dumps(out[v['beat']]))
(cut / 'refit.json').write_text(json.dumps(out, indent=1))
