"""Second look at each sung shot's slip, on the exact window the shot now plays: search frame by frame, and only leave the nominal 2-frame slip for a clearly better one. Updates build-r7.json."""
import json, os
import numpy as np, wave
b = json.load(open('build-r7.json')); m = json.load(open('mouth-r7.json'))
w = wave.open(os.path.expanduser('~/.cache/badcode-scenes/mv-colour-noir/stems/vocals16.wav'))
a = np.frombuffer(w.readframes(w.getnframes()), dtype=np.int16).astype(float)
vox = lambda t: np.sqrt((a[int(t*16000):int(t*16000)+640]**2).mean())
for r in b:
    if not r['lip']: continue
    g = np.array(m[r['name']]['gap']); ts = np.arange(r['start'], r['end'], .04); e = np.array([vox(t) for t in ts])
    base = r['start'] - r['songStart']
    def corr(s):
        idx = ((base + s + (ts - r['start'])) * 25).astype(int)
        if idx.min() < 0 or idx.max() >= len(g): return None
        return float(np.corrcoef(g[idx], e)[0, 1]) if g[idx].std() > 0 and e.std() > 0 else None
    nom = r['slip']; cn = corr(nom)
    cand = {f/24: corr(f/24) for f in range(-6, 13)}
    cand = {k: v for k, v in cand.items() if v is not None}
    best = max(cand, key=cand.get)
    if cn is None or cand[best] - (cn or 0) >= .12: nom = best
    # voice a touch behind the mouth, never ahead
    r['slip'] = round(nom, 3); r['inPoint'] = round((base + nom) * 24) / 24
    r['corr'] = round(corr(nom) or 0, 2)
    print(r['name'], round(r['start'], 2), 'dur', round(r['end']-r['start'], 2), 'slip', r['slip'], 'corr', r['corr'])
json.dump(b, open('build-r7.json', 'w'), indent=0)
