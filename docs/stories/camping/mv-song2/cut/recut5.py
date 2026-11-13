"""`camping song 2 beat 5` (Jack 2026-11-07 night): "do Ghostface Killah for all clips ... make a new sequence, also those 4 bits
where it flashes to black to the beat ... get rid of and do your own version but only do it for the start and end where bob is
running through the tunnel". From edl-beat4.json:

1. Every T3 rap piece (cb-<shot>t3*-) becomes that shot's Ghostface clip (round 9 `cb-<shot>g-…`, t06 = round 8 `cb-t06gf-…`),
   same slot; in point kept but pulled back to end inside the clip; a slot split in two carries on through the clip.
2. The black-flash stutters go. Middle ones closed up: 103.68 (the rap clip runs on), 124.84 and 130.28 (the next shot starts
   on the first flash's beat, its in point moved back to keep its own frame on the old beat).
3. Start and end (Bob running through the tunnel, clips/2.mp4): no black, an accelerating run cut on the 88 BPM grid
   (beat 0.682 s), each piece further into the run, landing on the same downbeat as before:
   start 10.96-13.68: back view 2 beats, running at us 1 beat, his face an eighth, the shout an eighth → m12 on 13.68;
   end 186.24-187.60: back view 1 beat, running at us an eighth, the face an eighth → 16.mov on 187.60.
Writes edl-beat5.json; build5.py makes the Premiere scripts."""
import json, os, re
from pathlib import Path
HERE = Path(__file__).parent
PRE = '/mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/songs/camping vid/balaclava/video/premiere/'
RUN = '/mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/songs/camping vid/clips/2.mp4'
R9 = HERE.parents[1] / 'mv-balaclava/cleanroom/r9'
picks = json.load(open(R9 / 'picks.json'))  # shot -> take
USE = 7.9
fr = lambda s: round(s * 25) / 25
e = json.load(open(HERE / 'edl-beat4.json'))


def gf(shot):
    return PRE + ('cb-t06gf-t06gfr8-a.mp4' if shot == 't06' else f'cb-{shot}g-{shot}gr9-{picks[shot]}.mp4')


log = []
for tr in ('V1', 'V2', 'V3'):
    out = []
    for x in e[tr]:
        x = dict(x)
        m = re.search(r'/cb-(\w\d\d)t3[bc]?-', x['src'] or '')
        if m:
            d = x['end'] - x['start']
            x['src'] = gf(m.group(1)); x['in'] = fr(max(0.0, min(x['in'], USE - d)))
        out.append(x)
    e[tr] = out

V = e['V1']
is_flash = lambda x: x['src'] and (x['end'] - x['start']) < 0.2 and os.path.basename(x['src']) in ('2.mp4', '5.mp4', '14.mp4')
def window(a, b):  # drop every V1 piece inside [a, b)
    return [x for x in V if not (x['start'] >= a - 0.01 and x['end'] <= b + 0.01)]

# middle stutters
V = window(103.68, 105.04)
for x in V:
    if abs(x['end'] - 103.68) < 0.01: x['end'] = 105.04; log.append('103.68: rap clip runs on to 105.04')
V = window(124.84, 126.20)
for x in V:
    if abs(x['start'] - 126.20) < 0.01: x['in'] = fr(x['in'] - 1.36); x['start'] = 124.84; log.append(f"124.84: {os.path.basename(x['src'])} starts on the old first flash")
V = window(130.28, 131.64)
for x in V:
    if abs(x['start'] - 131.64) < 0.01: x['in'] = fr(max(0.0, x['in'] - 1.36)); x['start'] = 130.28; log.append(f"130.28: {os.path.basename(x['src'])} starts on the old first flash")
# start and end: the tunnel run
V = window(10.96, 13.68) + [dict(start=s, end=t, src=RUN, **{'in': i}) for s, t, i in
                             [(10.96, 12.32, 0.0), (12.32, 13.00, 2.0), (13.00, 13.36, 3.6), (13.36, 13.68, 6.4)]]
V = window(186.24, 187.60) + [dict(start=s, end=t, src=RUN, **{'in': i}) for s, t, i in
                               [(186.24, 186.92, 1.0), (186.92, 187.28, 2.5), (187.28, 187.60, 7.0)]]
V.sort(key=lambda x: x['start'])
left = [x for x in V if is_flash(x)]
assert not left, left
# a rap slot split in two carries on through the clip
for a, b in zip(V, V[1:]):
    if a['src'] == b['src'] and '/cb-' in (a['src'] or '') and abs(a['end'] - b['start']) < 0.01:
        nxt = fr(a['in'] + a['end'] - a['start']); d = b['end'] - b['start']
        b['in'] = nxt if nxt + d <= USE else fr(max(0.0, USE - d))
for a, b in zip(V, V[1:]):
    assert a['end'] <= b['start'] + 0.01, (a, b)
e['V1'] = V
json.dump(e, open(HERE / 'edl-beat5.json', 'w'), indent=1)
gfs = sorted({os.path.basename(x['src']) for t in e.values() for x in t if x['src'] and ('g-' in x['src'] or 'gf-' in x['src'])})
print(len(V), 'V1 pieces;', '\n'.join(log)); print('ghostface files:', gfs)
print('missing:', sorted({os.path.basename(x['src']) for t in e.values() for x in t if x['src'] and not os.path.exists(x['src'])}))
