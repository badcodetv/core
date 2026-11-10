#!/usr/bin/env python3
"""check.py <fit.wav> [shot_in shot_dur] : measure a fitted voice on its clip the way the cut will play it: a mini edl
(the muted clip as one shot at timeline 0.5 s, the voice laid at 0.5 + origin), then row-measure (lag, early, strip).
Reads <fit.wav>.json (clip, origin). Run with the badcode-lips venv. GPOM scene A round 24."""
import json, os, subprocess, sys
import numpy as np, soundfile as sf
fit = sys.argv[1]; j = json.load(open(fit + '.json'))
i0 = float(sys.argv[2]) if len(sys.argv) > 2 else 0.0
dur = float(sys.argv[3]) if len(sys.argv) > 3 else None
T0 = 0.5
y, sr = sf.read(fit, dtype='float32')
lead = T0 + j['origin'] - i0
if lead >= 0:
    y = np.vstack([np.zeros((int(round(lead * sr)), y.shape[1]), np.float32), y])
else:
    y = y[int(round(-lead * sr)):]
stem = fit[:-4] + '.stem.wav'
sf.write(stem, y, sr, subtype='PCM_24')
if dur is None:
    dur = j['rows'][-1]['placed'] + 0.35 - i0
od = fit[:-4] + '.m'
e = dict(video=[dict(file=j['clip'], **{'in': i0}, dur=dur, start=T0, tag=os.path.basename(j['clip']))],
         audio=[dict(name='vox-x', file=stem)])
json.dump(e, open(fit[:-4] + '.edl.json', 'w'))
r = subprocess.run([sys.executable, '/home/kai/projects/badcode/badcode/scripts/lipsync/row-measure.py', fit[:-4] + '.edl.json',
                    '0', str(T0 + dur + 0.1), '--out', od, '--map', f"{os.path.basename(j['clip'])[:8]}=vox-x"],
                   capture_output=True, text=True)
print('\n'.join(l for l in r.stdout.splitlines() if l.strip()))
print('strip:', od)
