"""Cut 2 (Jack's timeline notes, round 1): edit-plan.json → edit-plan-r2.json.
- swaps (Jack's notes + Colour Noir action clips back in), then every cut snapped to the song's tracked beats.
Clip refs: '<shot>-<take>' = gang/video/bg-<ref>-*.mp4 ; 'cn:<name>' = noir/video/<name>.mp4"""
import json, pathlib
HERE = pathlib.Path(__file__).parent; SC = HERE.parent
plan = json.load(open(SC / 'edit-plan.json'))
hits = json.load(open(SC / 'hits.json'))['hits']  # percussive onset peaks (time, strength)
SWAP = {  # (start, old) -> (new, why)
    (3.90, 'a01-b'): ('cn:rods3-b', "Jack: 'same scene twice' at 0:05 — a hot rod from Colour Noir instead"),
    (59.48, 'x01-a'): ('cn:safe2-c', "Jack: 'there is no one in the drivers seat' (x01-a) — dropped everywhere"),
    (126.48, 'x01-a'): ('cn:chase3-a', "x01-a dropped; the motorcycle cop chase on 'call the police'"),
    (194.00, 'x01-a'): ('cn:rods4-a', 'x01-a dropped; hot rods through the water tunnel'),
    (35.92, 'v07-b'): ('v07f-b', "Jack: triangle on the left eye — the grandma clip mirrored"),
    (61.86, 'c01-b'): ('a02-b', 'c01-b refused by Flow (as cut 1)'),
    (123.74, 'c01-b'): ('a02-a', 'c01-b refused by Flow (as cut 1)'),
    (87.80, 'd02-a'): ('cn:pov2-a', 'Colour Noir action (driver past a theatre crowd and a cop) instead of the flashbulb twice; mask3-a left out: black rings, triangle on the right eye'),
    (98.70, 'x02-a'): ('cn:pov1-b', 'Colour Noir action instead of a repeat of x02'),
    (105.36, 'a03-a'): ('cn:chase1-a', 'Colour Noir action instead of a repeat of a03'),
    (144.18, 'x02-a'): ('cn:safe1-b', 'Colour Noir action (the safe out of the wall) instead of a repeat'),
    (188.46, 'x03-b'): ('cn:safe4-b', 'Colour Noir action instead of a repeat of x03'),
    (199.14, 'x07-b'): ('cn:rods2-b', "Colour Noir hot rods on the bridge, instead of a repeat of x07; mask1-b left out: the green robber's triangle is on his right eye"),
}
def snap(t):
    # the strongest drum hit from 0.33 s before to 0.2 s after the line starts; none → keep the line start
    if t == 0: return 0.0
    near = [h for h in hits if t - 0.33 <= h[0] <= t + 0.2]
    return max(near, key=lambda h: h[1])[0] if near else t
rows = []
for r in plan:
    new, why = SWAP.get((r['start'], r['clip']), (r['clip'], ''))
    rows.append({'start_line': r['start'], 'start': round(snap(r['start']), 3), 'clip': new, 'line': r['line'], 'why': why})
END = 209.6
for i, r in enumerate(rows):
    r['end'] = rows[i + 1]['start'] if i + 1 < len(rows) else END
    r['dur'] = round(r['end'] - r['start'], 3)
    r['shift'] = round(r['start'] - r['start_line'], 3)
json.dump(rows, open(SC / 'edit-plan-r2.json', 'w'), indent=1, ensure_ascii=False)
print(len(rows), 'cuts; longest', max(r['dur'] for r in rows), '; snapped', sum(1 for r in rows if r['shift']),
      '; max shift', max(abs(r['shift']) for r in rows), '; cn clips', sum(r['clip'].startswith('cn:') for r in rows))
