"""Round 7 gesture picks page: per rap shot, the clip now in `camping song 2 beat 2` (r6) and the five pattern options
T1-T5 side by side; Jack picks one per shot (or none) with a note. Preview copies (960 wide).

    python3 build_page.py <out-dir>      → <out-dir>/index.html + <out-dir>/media/*.mp4, then publish with db + user
"""
import json, subprocess, sys
from pathlib import Path
HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parent / 'r6'))
from make_briefs import SHOTS
V = Path('/mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/songs/camping vid/balaclava/video')
REPO = HERE.parents[5]
OUT = Path(sys.argv[1]); (OUT / 'media').mkdir(parents=True, exist_ok=True)
picks6 = json.load(open(HERE.parent / 'r6/picks.json'))
PAT = {'t1': 'T1 UK freestyle oner', 't2': 'T2 fisheye in the face', 't3': 'T3 locked, understated', 't4': 'T4 phone take', 't5': 'T5 timecoded accents'}


def small(src: Path, name: str):
    dst = OUT / 'media' / name
    if not dst.exists():
        subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', '-i', str(src), '-an', '-vf', 'scale=960:-2', '-c:v', 'libx264',
                        '-crf', '24', '-preset', 'slow', '-movflags', '+faststart', str(dst)], check=True)
    return f'media/{name}'


groups = {'rough': [], 'posh': []}
missing = []
for i, ((who, _), place, line) in SHOTS.items():
    still = f'{i}r6-{picks6[i]}'
    opts = [{'id': 'now', 'src': small(V / f'cb-{i}v-{still}.mp4', f'{i}-now.mp4'), 'label': 'now (in beat 2)'}]
    for t, lab in PAT.items():
        f = V / f'cb-{i}{t}-{still}.mp4'
        if f.exists(): opts.append({'id': t, 'src': small(f, f'{i}-{t}.mp4'), 'label': lab})
        else: missing.append(f.name)
    if len(opts) < 2: continue  # only the shots that were tried (Jack: "just do a few ... like 5")
    groups['rough' if i[0] in 'ms' else 'posh'].append(
        {'slot': i, 'title': f'{i}: {place}', 'line': line, 'kind': 'video', 'opts': opts})
spec = {'title': 'Rap Gesture Picks', 'eyebrow': 'Camping MV · balaclava rappers · round 7',
        'heading': 'Pick the gesturing for each rap shot',
        'intro': ('Five examples, as asked: the same shot (m12, under the flyover) from the same start frame, once in each of the five '
                  'prompt patterns from today\'s web research, each written by its own sealed writer. "now" is the clip in camping song 2 '
                  'beat 2 (the terrible gesturing). T1 handheld UK freestyle, T2 lens pushed into his face, T3 still camera and '
                  'understated, T4 a mate filming on a phone, T5 one timed gesture per two seconds. s01 also has a T1 take. Pick the '
                  'pattern you want (or none, with a note) and it gets written for all 13 shots.'),
        'sections': [s for s in [{'h': 'The rough sleeper (Bob\'s verses)', 'lede': 'Duct-tape mask.', 'groups': groups['rough']},
                     {'h': 'The rich man (Tarquin\'s verses)', 'lede': 'Tweed mask.', 'groups': groups['posh']}] if s['groups']]}
(HERE / 'picks-r7.json').write_text(json.dumps(spec, indent=1))
r = subprocess.run(['python3', str(REPO / 'scripts/scene/build-picks.py'), str(HERE / 'picks-r7.json'), str(OUT / 'index.html')],
                   capture_output=True, text=True, check=True)
print(r.stdout.strip()[:200]); print('missing:', missing)
