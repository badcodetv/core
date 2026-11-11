"""Check one cut-10 edit plan.  python3 validate.py plan-A.json
A plan is a JSON list of shots in order: {"start": s, "end": s, "clip": ref, "in": s, "why": "..."}.
Exit 0 = valid (prints stats); exit 1 = the problems, one per line."""
import json, pathlib, sys
HERE = pathlib.Path(__file__).parent
pool = {p['ref']: p for p in json.load(open(HERE / 'pool.json'))}
mm = json.load(open(HERE / 'music-map.json'))
END = mm['end']
plan = json.load(open(sys.argv[1]))
bad = []
t = 0.0
for i, r in enumerate(plan):
    for k in ('start', 'end', 'clip', 'in'):
        if k not in r:
            bad.append(f'shot {i}: no "{k}"')
    if bad:
        break
    if abs(r['start'] - t) > 0.002:
        bad.append(f'shot {i} ({r["clip"]}): starts at {r["start"]}, the previous shot ended at {t} (no gaps or overlaps)')
    d = r['end'] - r['start']
    if d < 0.3:
        bad.append(f'shot {i} ({r["clip"]}): {d:.2f} s is shorter than 0.3 s')
    p = pool.get(r['clip'])
    if not p:
        bad.append(f'shot {i}: clip "{r["clip"]}" is not in pool.json')
    elif r['in'] < 0 or r['in'] + d > p['secs'] + 0.01:
        bad.append(f'shot {i} ({r["clip"]}): in {r["in"]} + {d:.2f} s runs past the clip\'s {p["secs"]} s')
    t = r['end']
if abs(t - END) > 0.01:
    bad.append(f'the cut ends at {t}, it must end at {END}')
if bad:
    print('\n'.join(bad)); sys.exit(1)
cuts = [r['start'] for r in plan[1:]]
grid = sorted(set(mm['beats'] + [round((a + b) / 2, 3) for a, b in zip(mm['beats'], mm['beats'][1:])]))
on = sum(min(abs(c - g) for g in grid) <= 0.045 for c in cuts)
hit = sum(min(abs(c - h) for h in mm['strong_hits']) <= 0.06 for c in cuts)
from collections import Counter
uses = Counter(r['clip'] for r in plan)
print(json.dumps({'shots': len(plan), 'cuts_on_beat_or_half_beat': f'{on}/{len(cuts)}', 'cuts_on_a_strong_hit': f'{hit}/{len(cuts)}',
                  'mean_shot_s': round(END / len(plan), 2), 'clips_used': len(uses), 'most_repeated': uses.most_common(3),
                  'new_crew_clips_used': sum(1 for r in plan if r['clip'].startswith('h'))}))
