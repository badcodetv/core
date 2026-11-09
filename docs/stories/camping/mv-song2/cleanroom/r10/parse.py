"""Parse the sealed writers' st/du/re/ly.md into prompts-r10.json (stills: run + refs) and clips-r10.json (motion).
A ref naming another shot (e.g. st01.jpg) is resolved at run time: copy that shot's picked still into REFDIR under that name."""
import json, re
from pathlib import Path
H = Path(__file__).parent
stills, clips = {}, {}
for w in ('st', 'du', 're', 'ly', 'fx'):
    f = H / f'{w}.md'
    if not f.exists():
        print('missing', f.name); continue
    for m in re.finditer(r'=== SHOT (\S+) ===\s*REFS:\s*(.*?)\s*\n\s*STILL:\s*(.*?)\s*CLIP:\s*(.*?)(?=\n=== SHOT|\Z)', f.read_text(), re.S):
        i, refs, st, cl = m.groups()
        refs = [] if refs.strip().lower() in ('none', '-', '') else [r.strip() for r in refs.split(',') if r.strip()]
        fix = lambda p: p.strip() if p.strip().endswith('Thanks.') else p.strip() + '\n\nThanks.'
        stills[i] = {'run': fix(st), 'refs': refs, 'writer': w}
        clips[i] = {'motion': fix(cl), 'writer': w}
(H / 'prompts-r10.json').write_text(json.dumps(stills, indent=1))
(H / 'clips-r10.json').write_text(json.dumps(clips, indent=1))
for k, v in stills.items():
    print(k, v['refs'], len(v['run'].split()), len(clips[k]['motion'].split()))
