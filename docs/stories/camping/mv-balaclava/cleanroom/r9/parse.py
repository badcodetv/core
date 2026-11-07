"""Parse g1/g2.md into ../prompts-r9.json (stills, ids <shot>g, run by ../run_stills.mts ROUND=-r9) and clips-r9.json.
`python3 parse.py jobs <shot=a|b ...>` adds video jobs <shot>g to ../../video-jobs.json (start frame <shot>gr9-<take>)."""
import json, re, sys
from pathlib import Path
HERE = Path(__file__).parent; SCENE = HERE.parents[1]
fix = lambda p: p.strip() if p.strip().endswith('Thanks.') else p.strip() + '\n\nThanks.'
stills, clips = {}, {}
for w in ('g1', 'g2'):
    for m in re.finditer(r'=== SHOT (\w+) ===\s*STILL:\s*(.*?)\s*CLIP:\s*(.*?)(?=\n=== SHOT|\Z)', (HERE / f'{w}.md').read_text(), re.S):
        i = m.group(1) + 'g'
        stills[i] = {'run': fix(m.group(2)), 'writer': w}; clips[i] = {'motion': fix(m.group(3)), 'writer': w}
(HERE.parent / 'prompts-r9.json').write_text(json.dumps(stills, indent=1))
(HERE / 'clips-r9.json').write_text(json.dumps(clips, indent=1))
print(len(stills), sorted(stills), [len(stills[k]['run'].split()) for k in sorted(stills)], [len(clips[k]['motion'].split()) for k in sorted(clips)])
if sys.argv[1:2] == ['jobs']:
    vj = json.load(open(SCENE / 'video-jobs.json')); have = {e['key'] for e in vj['extra']}
    for a in sys.argv[2:]:
        s, t = a.split('='); k = s + 'g'
        if k in have: continue
        vj['extra'].append({'key': k, 'n': 0, 'still': f'{k}r9-{t}', 'motion': clips[k]['motion'], 'character': None,
                            'why': 'r9 Ghostface style for all rap clips (Jack 2026-11-07 night), sealed writer ' + clips[k]['writer']})
    json.dump(vj, open(SCENE / 'video-jobs.json', 'w'), indent=1); print('jobs added')
