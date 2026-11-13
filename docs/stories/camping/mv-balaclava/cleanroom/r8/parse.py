"""Parse the eight rapper writers' <key>.md into ../prompts-r8.json (stills, run verbatim by ../run_stills.mts with ROUND=-r8)
and clips-r8.json (motion). `python3 parse.py jobs <id=a|b …>` adds one video job per version to ../../video-jobs.json once the
stills are picked (start frame = <id>r8-<take>). Idempotent."""
import json, re, sys
from pathlib import Path
HERE = Path(__file__).parent
SCENE = HERE.parents[1]
from make_briefs import WRITERS
stills, clips = {}, {}
for k, (rapper, man) in WRITERS.items():
    f = HERE / f'{k}.md'
    if not f.exists(): print('missing', f.name); continue
    m = re.search(r'===\s*(\w+).*?===\s*STILL:\s*(.*?)\s*CLIP:\s*(.*)', f.read_text(), re.S)
    if not m: print('unparsed', f.name); continue
    i = man[4] + k
    fix = lambda p: p.strip() if p.strip().endswith('Thanks.') else p.strip() + '\n\nThanks.'
    stills[i] = {'run': fix(m.group(2)), 'writer': k, 'rapper': rapper, 'ref': 'rough' if man[4] == 's02' else 'posh'}
    clips[i] = {'motion': fix(m.group(3)), 'writer': k, 'rapper': rapper}
(HERE.parent / 'prompts-r8.json').write_text(json.dumps(stills, indent=1))
(HERE / 'clips-r8.json').write_text(json.dumps(clips, indent=1))
print(len(stills), sorted(stills))

if sys.argv[1:2] == ['jobs']:
    pick = dict(a.split('=') for a in sys.argv[2:])
    vj = json.load(open(SCENE / 'video-jobs.json'))
    have = {e['key'] for e in vj['extra']}
    for i, take in pick.items():
        if i in have: continue
        vj['extra'].append({'key': i, 'n': 0, 'still': f'{i}r8-{take}', 'motion': clips[i]['motion'], 'character': None,
                            'why': f"r8 rapper-style options (Jack 2026-11-07 \"gesture like action bronson, eminem ...\"), {clips[i]['rapper']}, sealed writer"})
    json.dump(vj, open(SCENE / 'video-jobs.json', 'w'), indent=1)
    print('jobs added:', list(pick))
