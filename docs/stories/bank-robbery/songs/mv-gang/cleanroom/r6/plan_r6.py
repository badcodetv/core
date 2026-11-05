"""Cut 6 (5 Nov meeting: "replace the repetitive clips with some more rapping at the camera", not overboard;
Jack picked 14 rap-to-camera stills, round 6). edit-plan-r5.json -> edit-plan-r6.json, same cut points.
1) each rap clip lands on the cut nearest its own lyric line;
2) then the most repeated clips lose their extra uses to the rap clips: any clip used more than MAX times keeps its first MAX,
   the rest go to rap clips round-robin (each rap clip at most RAP_MAX times, never next to another rap clip, the same one never within 8 cuts).
Outro hold and lyric shots Jack picked earlier are left alone."""
import json, pathlib, collections
HERE = pathlib.Path(__file__).parent; SC = HERE.parents[1]
VID = pathlib.Path(json.load(open(SC / 'scene.json'))['media']) / 'video'
P = json.load(open(HERE.parent / 'prompts-r6.json'))
rows = json.load(open(SC / 'edit-plan-r5.json'))
MAX, RAP_MAX = 3, 3
exists = lambda ref: ref.startswith('cn:') or bool(sorted(VID.glob(f'bg-{ref}-*.mp4')))
RAP = [k for k in ["p01-a", "p02-a", "p03-b", "p04-b", "p05-a", "p06-b", "p07-b", "p08-b", "p10-b", "p11-b", "p12-a", "p13-a", "p15-a", "p16-a"] if exists(k)]
keep = lambda r: (r.get('line') and not r['why'].startswith('action')) or r is rows[-1]
uses = collections.Counter()
# 1) on its line
for k in RAP:
    m, s = P[k.split('-')[0]]['t'].split(':'); t = int(m) * 60 + int(s)
    line = P[k.split('-')[0]]['line']
    cand = [i for i, r in enumerate(rows) if abs(r['start'] - t) < 2.5 and not keep(r)]
    if cand:
        i = min(cand, key=lambda i: abs(rows[i]['start'] - t))
        rows[i].update(clip=k, line=line, why=f'rap to camera you picked (round 6), instead of {rows[i]["clip"]}')
        uses[k] += 1
# 2) trim repeats
seen = collections.Counter(); last = {}; j = 0
for i, r in enumerate(rows):
    c = r['clip']
    if c in RAP: last[c] = i; continue
    seen[c] += 1
    if seen[c] > MAX and not keep(r):
        for _ in range(len(RAP)):
            k = RAP[j % len(RAP)]; j += 1
            if uses[k] < RAP_MAX and i - last.get(k, -99) >= 8 and rows[i - 1]['clip'] not in RAP and (i + 1 >= len(rows) or rows[i + 1]['clip'] not in RAP):
                r.update(clip=k, why=f'rap to camera (round 6), instead of a repeat of {c}'); uses[k] += 1; last[k] = i; break
uses2 = collections.Counter()
for r in rows:
    n = uses2[r['clip']]; uses2[r['clip']] += 1
    room = max(0.0, 6.0 - r['dur'] - 0.1)
    r['in'] = round((n * 1.7) % room, 3) if room > 0.2 else 0.0
json.dump(rows, open(SC / 'edit-plan-r6.json', 'w'), indent=1, ensure_ascii=False)
rap = sum(1 for r in rows if r['clip'] in RAP)
print(len(rows), 'cuts;', rap, 'rap-to-camera cuts from', len(RAP), 'clips; most used now:', uses2.most_common(6))
