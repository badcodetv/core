"""Cut 3 (Jack 2026-11-04: "the cuts should be timed to the beat and way more fast paced than it is, think action movie"):
edit-plan-r2.json (the lyric shots) + the r3 action clips -> edit-plan-r3.json.

Pace, from r3/research.md section 5 (a guide, not a gate):
  verses: a cut every 2 beats (~1.3 s), the lyric shot held 2 beats on its line;
  choruses and the post-drop intro: every beat (~0.65 s), half-beat flurries on "Robbery!";
  the break: 2 beats; drums out 2:55-3:07: a bar a shot (the breath before the end);
  the outro: every beat, flurries on each "Robbery!", the walk-away from the explosion held to the end.
Each cut snaps to the strongest drum hit within 0.12 s of its beat (hits.json).
Clips repeat; a repeat uses a different stretch of the 6 s clip (in-point), never the same one twice running.
Clip refs: '<shot>-<take>' = gang/video/bg-<ref>-*.mp4 ; 'cn:<name>' = noir/video/<name>.mp4"""
import json, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
HERE = pathlib.Path(__file__).parent; SC = HERE.parents[1]
VID = pathlib.Path(json.load(open(SC / 'scene.json'))['media']) / 'video'
beats = json.load(open(SC / 'beats-tracked.json'))['beats']
hits = json.load(open(SC / 'hits.json'))['hits']
r2 = json.load(open(SC / 'edit-plan-r2.json'))
END = 209.6

def exists(ref):
    return ref.startswith('cn:') or bool(sorted(VID.glob(f'bg-{ref}-*.mp4')))

# --- sections: (start, end, beats per shot, name) ---
SECTIONS = [(0.0, 7.5, 4, 'intro'), (7.5, 20.1, 1, 'drop'), (20.1, 61.9, 2, 'verse'), (61.9, 82.8, 1, 'chorus'),
            (82.8, 123.7, 2, 'verse'), (123.7, 144.2, 1, 'chorus'), (144.2, 154.7, 2, 'break'), (154.7, 175.0, 2, 'verse'),
            (175.0, 187.5, 4, 'breath'), (187.5, END, 1, 'outro')]
FLURRY = [7.5, 61.9, 72.5, 123.7, 134.4, 188.5, 194.0, 199.1]  # "Robbery!" hits: two half-beat cuts there
HOLD_END = ('k01-a', 205.0)  # the walk away from the explosion, held to the end

def snap(t):
    near = [h for h in hits if abs(h[0] - t) <= 0.12]
    return max(near, key=lambda h: h[1])[0] if near else t

grid = []
for s, e, n, name in SECTIONS:
    bs = [b for b in beats if s - 0.05 <= b < e - 0.05]
    if s == 0.0: bs = [0.0] + [b for b in bs if b > 0.3]
    for i in range(0, len(bs), n):
        grid.append((bs[i], name))
        if any(abs(bs[i] - f) < 0.35 for f in FLURRY) and i + 1 < len(bs):
            grid.append(((bs[i] + bs[i + 1]) / 2, name))  # half-beat flurry
grid = sorted({round(snap(t) if t else 0.0, 3): name for t, name in grid}.items())
grid = [(t, n) for t, n in grid if t < HOLD_END[1] - 0.2] + [(HOLD_END[1], 'outro')]

# --- the lyric shots from cut 2 (Jack's picks), each on the cut nearest its line ---
lyric = [(r['start_line'], r['clip'], r['line'], r.get('why', '')) for r in r2 if not r['clip'].startswith('cn:') and r['clip'][0] in 'vcdfe']
# Round 3d (Jack: "improve the gesturing of the existing rapping videos"): a rap clip redone with big gestures is '<shot>g-<take>'; use it where it exists.
def gest(c):
    if c.startswith('cn:') or '-' not in c: return c
    s, t = c.split('-', 1); g = f'{s}g-{t}'
    return g if exists(g) else c
lyric = [(t, gest(c), l, w) for t, c, l, w in lyric]
# Jack's picked gesture stills (g08-g12, round 3c), each on its own line.
P3 = json.load(open(HERE.parent / 'prompts-r3.json'))
GLINE = {'g08-b': 'just look at the hand', 'g09-b': 'state level manipulation', 'g10-b': 'own supply', 'g11-b': 'for the working man', 'g12-b': 'time to give'}
for g, words in GLINE.items():
    if not exists(g): continue
    hit = [x for x in lyric if words in x[2]]
    if hit:  # the picked gesture still takes that line's place
        t, c, l, w = hit[0]; lyric = [x for x in lyric if x is not hit[0]] + [(t, g, l, 'gesture still you picked (round 3c), instead of ' + c)]
    else:
        p = P3[g.split('-')[0]]; m, s_ = p['t'].split(':'); lyric.append((int(m) * 60 + int(s_), g, p['line'], 'gesture still you picked (round 3c)'))
ACTION = [k for k in ['k01-a', 'k02-b', 'k03-a', 'k04-a', 'k06-b', 'k07-a', 'k09-a', 'k10-a', 'k11-a', 'k12-a', 'k13-b', 'k14-a', 'k16-a',
                      'k18-a', 'k19-a', 'k21-a', 'k22-b', 'k23-a', 'k24-a', 'k26-a', 'k27-b', 'k29-a', 'k30-a', 'k31-b', 'k36-b'] if exists(k)]
NOIR = ['cn:rods3-b', 'cn:safe2-c', 'cn:pov2-a', 'cn:pov1-b', 'cn:chase1-a', 'cn:chase3-a', 'cn:safe1-b', 'cn:safe4-b', 'cn:rods4-a', 'cn:rods2-b']
GANG = [gest(c) for c in ['a01-a', 'a01-b', 'a02-a', 'a02-b', 'a03-a', 'a03-b', 'c02-b', 'c03-a', 'c03-b', 'c04-a', 'd01-a', 'x02-a', 'x03-b', 'x04-a', 'x06-a', 'x07-b'] if exists(c)]
POOL = ACTION + ACTION + NOIR + GANG  # the new action twice as often

rows = [{'start': t, 'section': n, 'clip': None, 'line': '', 'why': ''} for t, n in grid]
for t, clip, line, why in lyric:
    if not exists(clip): continue
    i = min(range(len(rows)), key=lambda i: abs(rows[i]['start'] - t) + (5 if rows[i]['clip'] else 0))
    if abs(rows[i]['start'] - t) < 1.4 and not rows[i]['clip']:
        rows[i].update(clip=clip, line=line, why=why or 'lyric shot (cut 2)')
rows[-1].update(clip=HOLD_END[0], line='Robbery! (outro)', why='the walk away from the explosion, held to the end')

used_at, uses, k = {}, {}, 0
for i, r in enumerate(rows):
    if r['clip']: used_at[r['clip']] = i; continue
    for _ in range(len(POOL)):
        c = POOL[k % len(POOL)]; k += 1
        if i - used_at.get(c, -99) >= 12 and (i == 0 or rows[i - 1]['clip'] != c): break
    r.update(clip=c, why='action')
    used_at[c] = i

# Round 5 (mask fix, r3/mask-audit.md): each clip with a wrong mask -> its '<shot>m-<take>' remake, where it exists.
if 'r5' in sys.argv:
    from make_mask_jobs import OLD
    SWAP = {o: f"{s}m-{o.split('-')[1]}" for s, olds in OLD.items() for o in olds}
    SWAP['v07f-b'] = 'v07m-b'
    KEEP_OLD = {'d02-b', 'k31-b'}  # remake worse than the old clip (r3/mask-clip-check.md)
    for o in KEEP_OLD: SWAP.pop(o, None)
    for r in rows:
        n = SWAP.get(r['clip'])
        if n and exists(n): r['clip'] = n; r['why'] = (r['why'] + '; mask fixed').strip('; ')
for i, r in enumerate(rows):
    r['end'] = rows[i + 1]['start'] if i + 1 < len(rows) else END
    r['dur'] = round(r['end'] - r['start'], 3)
    n = uses.get(r['clip'], 0); uses[r['clip']] = n + 1
    room = max(0.0, 6.0 - r['dur'] - 0.1)
    r['in'] = round((n * 1.7) % room, 3) if room > 0.2 else 0.0  # a different stretch of the clip each time
import sys
json.dump(rows, open(SC / ('edit-plan-r5.json' if 'r5' in sys.argv else 'edit-plan-r4.json' if 'r4' in sys.argv else 'edit-plan-r3.json'), 'w'), indent=1, ensure_ascii=False)
durs = [r['dur'] for r in rows]
print(len(rows), 'cuts; average', round(sum(durs) / len(durs), 2), 's; shortest', min(durs), '; longest', max(durs),
      '; lyric shots', sum(1 for r in rows if r['why'] and r['why'] != 'action'), '; action clips available', len(ACTION),
      '; distinct clips', len(uses))
