"""Cut 10B, round 3: Kai's round-2 notes (2026-11-11, feedback/timeline-r10B2/).
 0:26.6 "not reuse this scene here because it's what opened the song" -> k19m-a out, k21m-a (cash crate in the boat stern)
 0:35.8 "human eyes behind the yellow bally" -> h20-a out, h01-b (the crew in the bank lobby, made today)
 0:41.7 "the video should change sooner, just as it kicks into rent-seeking" -> the cut moves to the beat at the line's start"""
import json, pathlib
import numpy as np
HERE = pathlib.Path(__file__).parent
mm = json.load(open(HERE / 'music-map.json'))
beats = np.array(mm['beats'])
pool = {p['ref']: p for p in json.load(open(HERE / 'pool.json'))}
plan = json.load(open(HERE / 'plan-B2.json'))
at = lambda t: next(r for r in plan if r['start'] <= t < r['end'])
r = at(26.6); assert r['clip'] == 'k19m-a'
r.update(clip='k21m-a', **{'in': 2.5}, why='cash crate in the boat (Kai: the girder lunch opened the film, don\'t repeat it)')
r = at(35.8); assert r['clip'] == 'h20-a'
r.update(clip='h01-b', **{'in': 0.5}, why='crew in the bank lobby (Kai: h20-a shows human eyes behind the yellow mask)')
rent = next(l for l in mm['lines'] if l['text'].startswith('Rent seeking'))['start']
cut = float(beats[np.abs(beats - rent).argmin()])
i = next(k for k, x in enumerate(plan) if x['start'] > 41.7)  # the shot after the one playing at Kai's note
plan[i]['start'] = round(cut, 3); plan[i - 1]['end'] = round(cut, 3)
plan[i]['why'] = (plan[i].get('why') or '') + ' (Kai: in on "rent seeking")'
for x in plan:
    d = x['end'] - x['start']; secs = pool[x['clip']]['secs']
    if x['in'] + d > secs - 0.01:
        x['in'] = round(max(0.0, secs - d - 0.02), 3)
(HERE / 'plan-B3.json').write_text(json.dumps(plan, indent=1, ensure_ascii=False))
print(f'"Rent seeking" sung at {rent}; cut now at {cut:.3f} ({plan[i]["clip"]}), was 42.748')
