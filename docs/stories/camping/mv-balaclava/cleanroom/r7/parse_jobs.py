"""Parse the five pattern writers' t1-t5.md into clips-r7.json and add one video job per shot per pattern (key <shot><t>,
e.g. s01t3) to ../../video-jobs.json, start frame = the round-6 pick. Idempotent."""
import json, re
from pathlib import Path
HERE = Path(__file__).parent
SCENE = HERE.parents[1]
picks = json.load(open(HERE.parent / 'r6/picks.json'))
clips = {}
for t in ('t1', 't2', 't3', 't4', 't5'):
    f = HERE / f'{t}.md'
    if not f.exists(): print('missing', f.name); continue
    for m in re.finditer(r'=== CLIP (\w+) ===\s*(.*?)(?=\n=== CLIP|\Z)', f.read_text(), re.S):
        p = m.group(2).strip()
        if not p.rstrip().endswith('Thanks.'): p += '\n\nThanks.'
        clips[f'{m.group(1)}{t}'] = {'shot': m.group(1), 'pattern': t.upper(), 'motion': p}
(HERE / 'clips-r7.json').write_text(json.dumps(clips, indent=1))
vj = json.load(open(SCENE / 'video-jobs.json'))
have = {e['key'] for e in vj['extra']}
for k, c in clips.items():
    if k in have: continue
    vj['extra'].append({'key': k, 'n': 0, 'still': f"{c['shot']}r6-{picks[c['shot']]}", 'motion': c['motion'], 'character': None,
                        'why': f"r7 gesture options (Jack 2026-11-07 \"terrible gesturing\"), pattern {c['pattern']}, sealed writer"})
json.dump(vj, open(SCENE / 'video-jobs.json', 'w'), indent=1)
print(len(clips), 'clips;', len({v['shot'] for v in clips.values()}), 'shots')
