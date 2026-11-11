"""Cut 10B, round 2 (Kai 2026-11-11 picked B: "this is a really good edit").
His notes: 1:57 the man in front has human eyes (h09-a) -> h13-b, the new airfield crew clip, made after the editors ran;
2:43 swap this (k36m-b) with the snowy scene further down (h11-b); the end: "much less aggressive… just almost cut the audio off"
(assemble.py --fade 0.12); "the timing is maybe half a beat off… timing it around the snare rather than the kick drum".
Measured: in this song the kick is on beats 1 and 3 of each bar, the snare on 2 and 4, hi-hats on the half beats; 47 of B's
94 cuts sat on a half beat. Every cut now moves to the nearest KICK (beat 1 or 3); where that would make a shot shorter
than 0.6 s it takes the nearest beat instead. Each shot keeps its clip and its in-point."""
import json, pathlib
import numpy as np
HERE = pathlib.Path(__file__).parent
mm = json.load(open(HERE / 'music-map.json'))
beats = np.array(mm['beats']); i0 = list(beats).index(mm['bars'][0])
kicks = np.array([b for i, b in enumerate(beats) if (i - i0) % 2 == 0])
plan = json.load(open(HERE / 'plan-B.json'))
pool = {p['ref']: p for p in json.load(open(HERE / 'pool.json'))}
END = mm['end']

# Kai's two notes
for r in plan:
    if r['start'] <= 117.55 < r['end'] and r['clip'] == 'h09-a':
        r.update(clip='h13-b', **{'in': 0.3}, why='crew at the airfield (Kai: h09-a showed human eyes)')
a = next(r for r in plan if r['start'] <= 163.4 < r['end'])
b = next(r for r in plan if r['clip'] == 'h11-b' and r['start'] > a['end'])
assert a['clip'] == 'k36m-b', a
a['clip'], b['clip'] = b['clip'], a['clip']; a['in'], b['in'] = b['in'], a['in']
a['why'] = 'the snowy field here (Kai: swap with the snow scene further down)'; b['why'] = "swapped from 2:43 (Kai's note)"

# snap every cut to the kick
cuts = [r['start'] for r in plan[1:]]
new, prev = [], 0.0
for k, c in enumerate(cuts):
    nxt = cuts[k + 1] if k + 1 < len(cuts) else END
    cand = sorted(kicks, key=lambda x: abs(x - c))[:2] + sorted(beats, key=lambda x: abs(x - c))[:2]
    if abs(c - 10.82) < 0.05:  # the drop Kai named ("the very moment that the music drops") stays exactly on it
        new.append(c); prev = c; continue
    pick = next((x for x in cand if x - prev >= 0.6 and nxt - x >= 0.3 and END - x >= 0.6), c)
    new.append(round(float(pick), 3)); prev = pick
for r, s in zip(plan[1:], new):
    r['start'] = s
for r, nx in zip(plan, plan[1:]):
    r['end'] = nx['start']
plan[-1]['end'] = END
for r in plan:  # keep in + dur inside the clip
    d = r['end'] - r['start']; secs = pool[r['clip']]['secs']
    if r['in'] + d > secs - 0.01:
        r['in'] = round(max(0.0, secs - d - 0.02), 3)
(HERE / 'plan-B2.json').write_text(json.dumps(plan, indent=1, ensure_ascii=False))
moved = sum(abs(a - b) > 0.01 for a, b in zip(cuts, new))
onkick = sum(np.abs(kicks - x).min() < 0.01 for x in new)
print(f'{moved} of {len(cuts)} cuts moved; {onkick} now on a kick, {len(new) - onkick} on a snare beat (to keep a shot over 0.6 s)')
