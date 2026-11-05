"""Cut 7 (Jack 2026-11-05 on cut 6: "let the clips play for a bit longer … sparingly cut fast … more of them rapping at the camera
throughout, not so its overpowering, just so there is a good mix"). Recipe from r7/research.md §1–2 (graded WEAK there: a guide).
  - Shots on the bar (4 beats ≈ 2.6 s); performance holds a line or couplet; intro, break and outro hold 2 bars.
  - Three flurries only, each a bar or two cut on the beat, each followed by a held shot: the first "Robbery!" (0:07.5),
    the end of chorus 1 (1:20), the run into the outro (3:07.5).
  - About 35–40 % of screen time is rapping to camera: verse openers, punchlines, the hooks (gang shots), back to camera every few bars.
  - Rejected clips never come back; their fixes take their place where they exist.
  - No clip used more than twice; a repeat uses a different stretch of the clip."""
import json, pathlib, collections
HERE = pathlib.Path(__file__).parent; SC = HERE.parents[1]
VID = pathlib.Path(json.load(open(SC / 'scene.json'))['media']) / 'video'
bt = json.load(open(SC / 'beats-tracked.json')); beats = bt['beats']; ph = bt.get('downbeat_phase', 0)
hits = json.load(open(SC / 'hits.json'))['hits']
lines = [(s['start'], s['text'].strip()) for s in json.load(open(SC / 'song-transcript.json'))['segments'] if 'Music' not in s['text']]
r6 = json.load(open(SC / 'edit-plan-r6.json'))
END = 209.6
exists = lambda ref: ref.startswith('cn:') or bool(sorted(VID.glob(f'bg-{ref}-*.mp4')))
REJECT = {'k02m-b', 'k02-b', 'k06-b', 'k11-a', 'k26m-a', 'k26-a', 'cn:pov1-b', 'cn:safe1-b', 'p08-b', 'v05m-b', 'v11m-b'}
FIX = {'k02m-b': 'z01', 'k06-b': 'z02', 'k11-a': 'z03', 'k26m-a': 'z04', 'cn:pov1-b': 'z05', 'cn:safe1-b': 'z06', 'p08-b': 'z07',
       'v05m-b': 'v05x-a', 'v11m-b': 'v11x-a'}
def fix_of(c):
    f = FIX.get(c)
    if not f: return None
    if '-' in f: return f if exists(f) else None
    for t in 'ab':
        if exists(f'{f}-{t}'): return f'{f}-{t}'
    return None
# --- the bar grid ---
SECTIONS = [(0.0, 7.5, 'intro', 2), (7.5, 20.1, 'drop', 1), (20.1, 61.9, 'verse', 1), (61.9, 82.8, 'chorus', 1), (82.8, 123.7, 'verse', 1),
            (123.7, 144.2, 'chorus', 1), (144.2, 154.7, 'break', 2), (154.7, 175.0, 'verse', 1), (175.0, 187.5, 'breath', 2), (187.5, END, 'outro', 2)]
FLURRY = [(7.5, 4), (80.2, 4), (187.5, 4)]  # (start, beats) cut on every beat
HOLD_END = 205.0
def snap(t):
    near = [h for h in hits if abs(h[0] - t) <= 0.12]
    return max(near, key=lambda h: h[1])[0] if near else t
bars = [b for i, b in enumerate(beats) if (i - ph) % 4 == 0]
cuts = []
for s, e, name, n in SECTIONS:
    bs = [b for b in bars if s - 0.3 <= b < e - 0.3]
    if s == 0.0: bs = [0.0] + [b for b in bs if b > 0.5]
    # a performance line may hold 2 bars: decided at assignment; here the grid is every n bars
    for i in range(0, len(bs), n): cuts.append((bs[i], name))
for fs, nb in FLURRY:
    i0 = min(range(len(beats)), key=lambda i: abs(beats[i] - fs))
    span = beats[i0:i0 + nb + 1]
    cuts = [c for c in cuts if not (span[0] - 0.05 <= c[0] < span[-1] - 0.05)] + [(b, 'flurry') for b in span[:-1]]
cuts = sorted({round(snap(t) if t else 0.0, 3): n for t, n in cuts}.items())
cuts = [(t, n) for t, n in cuts if t < HOLD_END - 0.3] + [(HOLD_END, 'outro')]
# --- pools ---
P7 = json.load(open(HERE.parent / 'prompts-r7.json'))
P6 = json.load(open(HERE.parent / 'prompts-r6.json'))
def tsec(s): m, x = s.split(':'); return int(m) * 60 + int(x)
def pick(sid):
    for t in 'ab':
        if exists(f'{sid}-{t}'): return f'{sid}-{t}'
# line-anchored rap clips, best first: new q picks, then round-6 p clips, then the older lyric shots (with the two clip fixes on the noted lines)
anchored = []
for sid, p in P7.items():
    if sid[0] == 'q' and pick(sid): anchored.append((tsec(p['t']) + 0.5, pick(sid), p['line'], 1))
if pick('z07'): anchored.append((89.7, pick('z07'), 'The right and the left both witness the theft', 1))
anchored.append((175.0, 'v05x-a', 'Hungry people feed a revolution', 1)); anchored.append((185.6, 'v11x-a', "don't just eat cake", 1))
for r in r6:
    c, w = r['clip'], r['why']
    if c[0] == 'p' and 'instead of a repeat' not in w and c not in REJECT and exists(c): anchored.append((r['start'], c, r['line'], 2))
    elif r.get('line') and not w.startswith('action') and c[0] != 'p' and exists(c) and c not in REJECT: anchored.append((r['start'], c, r['line'], 3))
GROUP = [c for c in ['p06-b', 'p12-a', 'p16-a', 'p05-a', pick('q07'), pick('q12'), 'c03g-a', 'c04g-a'] if c and exists(c)]
ACTION = [c for c in ['k01m-a', 'k03m-a', 'k04m-a', 'k07-a', 'k09m-a', 'k10-a', 'k12m-a', 'k13m-b', 'k16-a', 'k18m-a', 'k19m-a', 'k21m-a',
                      'k22m-b', 'k23-a', 'k24-a', 'k27m-b', 'k29m-a', 'k30m-a', 'k31-b', 'k36m-b', 'cn:rods3-b', 'cn:safe2-c', 'cn:pov2-a',
                      'cn:chase1-a', 'cn:chase3-a', 'cn:safe4-b', 'cn:rods4-a', 'cn:rods2-b', 'a01m-a', 'a02m-a', 'a03m-a',
                      'x02-a', 'x03m-b', 'x04-a', 'x06-a', 'x07m-b'] if exists(c)]
FIXAT = [(t, pick(z)) for t, z in [(2.0, 'z01'), (9.0, 'z02'), (18.0, 'z04'), (42.0, 'z03'), (66.0, 'z05'), (69.0, 'z06')] if pick(z)]
# --- assign ---
rows = [{'start': t, 'section': n, 'clip': None, 'line': '', 'why': ''} for t, n in cuts]
for i, r in enumerate(rows): r['end'] = rows[i + 1]['start'] if i + 1 < len(rows) else END
rows[-1].update(clip='k01m-a', line='Robbery! (outro)', why='the walk away from the explosion, held to the end')
uses = collections.Counter({'k01m-a': 1})
rowat = lambda t: next((i for i, r in enumerate(rows) if r['start'] - 0.2 <= t < r['end']), None)
for t, c in FIXAT:  # each fix near where Jack noted the shot
    i = rowat(t)
    while i is not None and rows[i]['clip']: i += 1
    if i is not None: rows[i].update(clip=c, why='action (fix for your note)'); uses[c] += 1
for t, c, line, pri in sorted(anchored, key=lambda a: a[3]):  # rap clips on their own lines
    i = rowat(t)
    if i is None or rows[i]['clip'] or rows[i]['section'] == 'flurry' or uses[c] >= 1: continue
    if rows[i]['section'] in ('verse', 'break', 'breath', 'chorus') and any('rapping' in rows[j]['why'] for j in (i - 1, i + 1) if 0 <= j < len(rows)): continue
    rows[i].update(clip=c, line=line, why='rapping to camera on its line'); uses[c] += 1
def take(pool, i, maxuse=2):
    for c in pool:
        if uses[c] < maxuse and all(rows[j]['clip'] != c for j in range(max(0, i - 8), min(len(rows), i + 8))): return c
    return None
for i, r in enumerate(rows):  # the hooks and the outro: the gang together every third shot
    if r['clip'] or r['section'] not in ('chorus', 'outro', 'drop'): continue
    near = [rows[j]['why'] for j in range(max(0, i - 2), i)]
    if not any('rapping' in w for w in near):
        c = take(GROUP, i)
        if c: r.update(clip=c, why='the gang rapping to camera'); uses[c] += 1
for i, r in enumerate(rows):
    if not r['clip']:
        c = take(ACTION, i) or take(ACTION, i, 3); r.update(clip=c, why='action'); uses[c] += 1
# merge: a performance shot whose next row is an action shot in a verse may hold 2 bars if the clip allows (≤ 5.9 s)
out = []
for r in rows:
    if out and out[-1]['why'].startswith('rapping') and out[-1]['section'] in ('verse',) and r['section'] == 'verse' \
            and r['end'] - out[-1]['start'] <= 5.4 and not r['why'].startswith('rapping') and not r['line'] and len(out) % 3 == 0:
        uses[r['clip']] -= 1; out[-1]['end'] = r['end']; continue
    out.append(r)
rows = out
# long holds over 5.9 s split in two clips
fin = []
for r in rows:
    d = r['end'] - r['start']
    if d > 5.9:
        mid = r['start'] + d / 2
        a = dict(r, end=mid); b = dict(r, start=mid, clip=take(ACTION, len(fin)) or r['clip'], why='action', line='')
        uses[b['clip']] += 1; fin += [a, b]
    else: fin.append(r)
rows = fin
seen = collections.Counter()
for r in rows:
    r['start'] = round(r['start'], 3); r['end'] = round(r['end'], 3); r['dur'] = round(r['end'] - r['start'], 3)
    n = seen[r['clip']]; seen[r['clip']] += 1
    room = max(0.0, 6.0 - r['dur'] - 0.1)
    r['in'] = round((n * 2.1) % room, 3) if room > 0.2 else 0.0
json.dump(rows, open(SC / 'edit-plan-r7.json', 'w'), indent=1, ensure_ascii=False)
perf = sum(r['dur'] for r in rows if r['why'].startswith('rapping') or 'gang rapping' in r['why'])
durs = [r['dur'] for r in rows]
print(len(rows), 'cuts; average', round(sum(durs) / len(durs), 2), 's; rapping to camera', round(100 * perf / END), '% of screen time;',
      'flurry cuts', sum(1 for r in rows if r['section'] == 'flurry'), '; max use', seen.most_common(3), '; fixes in:', [c for _, c in FIXAT])
