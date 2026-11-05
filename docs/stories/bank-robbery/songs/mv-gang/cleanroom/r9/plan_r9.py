"""Cut 9 (Jack 2026-11-05 on cut 8: "make more cuts and maybe have the clips halfed in time, let some run longer than the others,
lots of action shots and sprinkled in rapping gesturing to the camera shots" + use the clips he screenshotted + 3 notes).
  - Action shots mostly 2 beats (~1.3 s, half of cut 8's bar), with a 4-beat or 6-beat hold every few shots so the length varies.
  - Rap/gesture to camera: one line each (4 beats), sprinkled, always with action either side (~20-25 % of screen time).
  - Beat flurries (1 beat each) only at the four drops, as in cut 8.
  - Jack's screenshot picks are in, the action ones on the longer holds: p16-a, y06-a, p15-a, k22m-b, x04-a, x03m-b, x02-a, p02-a, z03-a.
  - Notes on cut 8: y01-b out (eye shows through the green mask); v07m-b on "grandma freezing"; d10-a (devil-horn shadow in the
    booth) on "It is the devil with the radio station"."""
import json, pathlib, collections
HERE = pathlib.Path(__file__).parent; SC = HERE.parents[1]
VID = pathlib.Path(json.load(open(SC / 'scene.json'))['media']) / 'video'
beats = json.load(open(SC / 'beats-tracked.json'))['beats']
r8 = json.load(open(SC / 'edit-plan-r8.json'))
END, HOLD_END = 209.6, 205.0
exists = lambda ref: ref.startswith('cn:') or bool(sorted(VID.glob(f'bg-{ref}-*.mp4')))
bi = lambda t: min(range(len(beats)), key=lambda i: abs(beats[i] - t))

OUT = {'y01-b', 'cn:pov2-a', 'p10-b'}  # y01: Jack's note at 0:00; pov2 played once in cut 8 (Jack: "only play it once") so it rests; p10 gives its line to d10
# --- fixed shots: (time, beats, clip, why, line, priority) ---
fixed = []
for r in r8:  # cut 8's rap-to-camera shots on their lines
    if r['why'].startswith('rapping') and r['clip'] not in OUT and r['line']:
        fixed.append((r['start'], 4, r['clip'], 'rapping to camera on its line', r['line'], 3))
fixed += [
    (35.92, 4, 'v07m-b', 'grandma freezing (your note)', 'Quantitive easing, grandma freezing', 0),
    (110.54, 4, 'd10-a', 'the devil-horn shadow in the booth (your note)', 'It is the devil with the radio station', 0),
    (26.61, 4, 'p02-a', 'your pick: Grand Central, rapping to camera', 'Earning that dough, but where does it go?', 1),
    (164.05, 4, 'p15-a', 'your pick: the dining car, rapping to camera', 'Crime is asset inflation, passive creation', 1),
    (174.36, 6, 'p16-a', 'your pick: the gang in the boxing ring', 'Hungry people feed a revolution', 1),
]
FLURRY = [7.5, 61.9, 123.7, 187.5]
segs = []  # (beat0, nbeats, clip, why, line)
taken = set()
def free(b0, n, pad=0): return all(b not in taken for b in range(b0 - pad, b0 + n + pad))
for t in FLURRY:
    b0 = bi(t)
    for k in range(4): segs.append((b0 + k, 1, None, 'flurry', '')); taken.add(b0 + k)
rapbeats = []
for t, n, c, why, line, pr in sorted(fixed, key=lambda f: f[5]):
    if not exists(c): continue
    b0 = bi(t - 0.15)
    if not free(b0, n): continue
    if any(abs(b0 - rb) < 4 + 2 and not (b0 >= rb + rn + 2 or rb >= b0 + n + 2) for rb, rn in rapbeats): continue  # 2+ beats of action between
    segs.append((b0, n, c, why, line)); taken.update(range(b0, b0 + n)); rapbeats.append((b0, n))
# --- fill the gaps with action, mostly 2 beats, with longer holds now and then ---
PAT = [2, 2, 2, 4, 2, 2, 2, 1, 1, 2, 2, 2, 6, 2, 2, 2]
LONG_SECTIONS = [(0.0, 7.5), (144.2, 154.7), (175.0, 187.5)]  # intro, break, breath: 4-6 beat holds
last = bi(HOLD_END)
pi = 0
b = 0
while b < last:
    if b in taken: b += 1; continue
    e = b
    while e < last and e not in taken: e += 1
    gap = e - b
    while gap > 0:
        long = any(s <= beats[b] < t for s, t in LONG_SECTIONS)
        n = (4 if pi % 2 else 6) if long else PAT[pi % len(PAT)]
        pi += 1
        n = min(n, gap)
        if gap - n == 1 and n > 1: n += 1  # never leave a 1-beat scrap unless asked
        segs.append((b, n, None, 'action', '')); b += n; gap -= n
    b = e
segs.sort()
rows = []
for b0, n, c, why, line in segs:
    s = 0.0 if not rows else beats[b0]
    rows.append({'start': s, 'clip': c, 'why': why, 'line': line, 'beats': n})
for i, r in enumerate(rows): r['end'] = rows[i + 1]['start'] if i + 1 < len(rows) else HOLD_END
rows.append({'start': HOLD_END, 'end': END, 'clip': 'k01m-a', 'why': 'the walk away from the explosion, held to the end', 'line': 'Robbery! (outro)', 'beats': 0})
# --- pools ---
PICKS = ['y06-a', 'z03-a', 'x04-a', 'k22m-b', 'x03m-b', 'x02-a']  # Jack's screenshot action picks: each on a long hold first
ACTION = [c for c in ['y02-a', 'y03-a', 'y04-a', 'y05-a', 'y06-a', 'z02y-b', 'z03-a', 'z04-b', 'z06y-b', 'k01m-a', 'k04m-a', 'k09m-a',
                      'k10-a', 'k12m-a', 'k13m-b', 'k16-a', 'k19m-a', 'k21m-a', 'k22m-b', 'k23-a', 'k27m-b', 'k29m-a', 'k30m-a',
                      'k31-b', 'k36m-b', 'a01m-a', 'a02m-a', 'a03m-a', 'x02-a', 'x03m-b', 'x04-a', 'x06-a', 'x07m-b', 'd11-a', 'd12-b',
                      'cn:rods3-b', 'cn:safe2-c', 'cn:chase1-a', 'cn:chase3-a', 'cn:safe4-b', 'cn:rods4-a', 'cn:rods2-b'] if exists(c)]
uses = collections.Counter(r['clip'] for r in rows if r['clip'])
def ok(c, i, gapn=10): return all(rows[j]['clip'] != c for j in range(max(0, i - gapn), min(len(rows), i + gapn)))
# picks on the longest action holds, spread across the song
holds = sorted([i for i, r in enumerate(rows) if not r['clip'] and r['beats'] >= 4], key=lambda i: rows[i]['start'])
for k, c in enumerate(PICKS):
    for _ in range(2):
        cand = [i for i in holds if not rows[i]['clip'] and ok(c, i, 25)]
        if not cand: continue
        target = (k + 0.5 + _ * len(PICKS)) / (2 * len(PICKS)) * END
        i = min(cand, key=lambda i: abs(rows[i]['start'] - target))
        rows[i].update(clip=c, why='your pick'); uses[c] += 1
for i, r in enumerate(rows):
    if r['clip']: continue
    pool = sorted(ACTION, key=lambda c: (uses[c], ACTION.index(c)))
    c = next((c for c in pool if uses[c] < 3 and ok(c, i)), None) or next(c for c in pool if ok(c, i, 4))
    r.update(clip=c); uses[c] += 1
# Jack on cut 9: y02-a (the burnout) out, the gunman's body looks attached to the car; the same clip is swapped at all three uses
Y02 = {0: 'a02m-a', 1: 'a03m-a', 2: 'x06-a'}
for k, r in enumerate([r for r in rows if r['clip'] == 'y02-a']): r.update(clip=Y02[k], why=r['why'] + ' (y02 out: body attached to the car)')
seen = collections.Counter()
for r in rows:
    r['start'] = round(r['start'], 3); r['end'] = round(r['end'], 3); r['dur'] = round(r['end'] - r['start'], 3)
    n = seen[r['clip']]; seen[r['clip']] += 1
    room = max(0.0, 6.0 - r['dur'] - 0.1)
    r['in'] = round((n * 1.7) % room, 3) if room > 0.2 else 0.0
    if r['clip'] == 'p03y-b': r['in'] = min(2.6, room)
    if r['clip'] == 'v05y-a': r['in'] = min(2.4, room)
    r['section'] = r['why'].split(' ')[0] if r['why'] == 'flurry' else 'verse'
    r.pop('beats', None)
json.dump(rows, open(SC / 'edit-plan-r9.json', 'w'), indent=1, ensure_ascii=False)
rap = sum(r['dur'] for r in rows if r['why'].startswith(('rapping', 'your pick:')))
durs = [r['dur'] for r in rows]
adj = sum(1 for a, b in zip(rows, rows[1:]) if a['why'].startswith(('rapping', 'your pick:')) and b['why'].startswith(('rapping', 'your pick:')))
print(len(rows), 'cuts; average', round(sum(durs) / len(durs), 2), 's; min', min(durs), 'max', max(durs), '; rap', round(100 * rap / END), '%; rap pairs', adj,
      '; max use', collections.Counter(r['clip'] for r in rows).most_common(3), '; picks', {c: uses[c] for c in PICKS + ['p02-a', 'p15-a', 'p16-a', 'v07m-b', 'd10-a']})
