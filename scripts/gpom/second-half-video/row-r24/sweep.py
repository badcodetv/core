#!/usr/bin/env python3
"""sweep.py <workdir> <line> <out-subdir> <clip.mp4,...> <take.wav,...> : rowwarp every take onto every clip (free),
rank by mouth score. Clip speech span from its own audio. Run with the badcode-lips venv. GPOM scene A round 24."""
import json, os, subprocess, sys
from concurrent.futures import ThreadPoolExecutor
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rowwarp as RW
work, line, sub, clips, takes = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4].split(','), sys.argv[5].split(',')
od = f'{work}/{sub}'; os.makedirs(od, exist_ok=True)
LPY = os.path.expanduser('~/.cache/badcode-lips/venv/bin/python')
HERE = os.path.dirname(os.path.abspath(__file__))


def job(ct):
    c, t = ct
    cn, tn = os.path.basename(c)[:-4], os.path.basename(t)[:-4]
    mj = f'{work}/{os.path.basename(c)}-strip.jpg.json'
    cw = json.load(open(f'{work}/clips.json'))[os.path.basename(c)]['words']
    c0, c1 = RW.speech_span(RW.load(c), floor=24)[0], cw[-1][2] + 0.05
    out = f'{od}/{line}--{cn}--{tn}.wav'
    r = subprocess.run([LPY, f'{HERE}/rowwarp.py', 'fit', t, c, mj, f'{max(0, c0 - 0.03):.3f}', f'{c1 + 0.03:.3f}', out,
                        '--json', out + '.json'], capture_output=True, text=True)
    if r.returncode:
        return cn, tn, None, r.stderr[-300:]
    return cn, tn, json.loads(r.stdout.strip().splitlines()[-1]), ''


res = list(ThreadPoolExecutor(8).map(job, [(c, t) for c in clips for t in takes]))
rows = []
for cn, tn, j, err in res:
    if not j:
        print('FAIL', cn, tn, err); continue
    b = j['best']
    rows.append((b['score'], cn, tn, b['delta'], b['corr'], b['shut'], b['early'], j['warp_cost'], max(j['raw']), min(j['raw']), j['end_drift'], j['clamped'], j['pieces'], j['resid']))
for r in sorted(rows, reverse=True):
    print(f'{r[0]:6.3f} {r[1]:24s} {r[2]:14s} d{r[3]:+.3f} corr {r[4]:.2f} shut {r[5]:.2f} early {r[6]} wc {r[7]:.3f} raw {r[9]:.2f}-{r[8]:.2f} drift {r[10]:+.2f} clamped {r[11]}/{r[12]} resid {r[13]}')
json.dump(rows, open(f'{od}/{line}-sweep.json', 'w'))
