"""Round 8 gesture picks page: eight rapper-style versions (four per man) beside the T3 clip now in `camping song 2 beat 4`.
Each option shows its new start still and its clip. Jack picks one style (or none) with a note.

    python3 build_page.py <out-dir>      → <out-dir>/index.html + <out-dir>/media/*, then publish with db + user
"""
import json, subprocess, sys
from pathlib import Path
HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))
from make_briefs import WRITERS
MEDIA = Path('/mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/songs/camping vid/balaclava')
REPO = HERE.parents[5]
OUT = Path(sys.argv[1]); (OUT / 'media').mkdir(parents=True, exist_ok=True)
jobs = {e['key']: e for e in json.load(open(HERE.parents[1] / 'video-jobs.json'))['extra']}
STYLE = {  # one line each, from the writers' <key>-observed.md
    'em': 'leans into a close wide lens; one hand at a time, snaps and stops dead (finger jab, arms flung wide, slap to the chest)',
    'fc': 'relaxed, leans in, chin dipped; one hand reaches low at the lens or flicks from the wrist; sways, feet never move',
    'mm': 'fisheye from below; leans down over the lens; splayed hand thrust at it, fist punches, knee bounce, head ducks',
    'kl': 'three-quarters on, low close lens; whole arm thrust at the lens, fingers spread, then pulled back; head cocked, sharp tilts on the stresses',
    'ab': 'heavy, amused, weight back; one hand busy (the champagne), the free hand loose: finger to the sky, wrist rolls, shrug',
    'rz': 'pendulum sway, wide knees; lunges his face at a low tilted lens; loose arm swings, nothing held',
    'gf': 'hunched into a low wide lens, off-centre; hands low, palm sweeps across the body, thumb jabs, flat chops',
    'rr': 'the boss: chin up, slow heavy nods and sway; palms spread and held, hands rubbed together, fist to the lens',
}


def small(src: Path, name: str):
    dst = OUT / 'media' / name
    if not dst.exists():
        if src.suffix == '.jpg':
            subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', '-i', str(src), '-vf', 'scale=960:-2', '-q:v', '4', str(dst)], check=True)
        else:
            subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', '-i', str(src), '-an', '-vf', 'scale=960:-2', '-c:v', 'libx264',
                            '-crf', '24', '-preset', 'slow', '-movflags', '+faststart', str(dst)], check=True)
    return f'media/{name}'


groups = {'s02': [], 't06': []}
missing = []
for slot in groups:
    vids = [{'id': 'now', 'src': small(MEDIA / f'video/cb-{slot}t3-{slot}r6-b.mp4', f'{slot}-now.mp4'), 'label': 'now: T3 (in beat 4)'}]
    stills = []
    for k, (rapper, man) in WRITERS.items():
        if man[4] != slot: continue
        key = slot + k; still = jobs[key]['still']
        f = MEDIA / f'video/cb-{key}-{still}.mp4'
        name = rapper.split(' (')[0]
        stills.append({'id': k, 'src': small(MEDIA / f'moodboard/{still}.jpg', f'{key}.jpg'), 'label': f'{name}: start still'})
        if f.exists(): vids.append({'id': k, 'src': small(f, f'{key}.mp4'), 'label': f'{name}: {STYLE[k]}'})
        else: missing.append(f.name)
    who, _, place, line, _ = next(m for _, m in WRITERS.values() if m[4] == slot)
    groups[slot] = [{'slot': f'r8-{slot}', 'title': f'{slot}: {who}, {place}', 'line': line, 'kind': 'video', 'opts': vids},
                    {'slot': f'r8-{slot}-stills', 'title': f'{slot}: the new start stills', 'line': 'Each version starts from its own still, posed the way that rapper moves.', 'kind': 'image', 'opts': stills}]
spec = {'title': 'Rap Gesture Picks', 'eyebrow': 'Camping MV · balaclava rappers · round 8',
        'heading': 'Eight rappers: pick the way they move',
        'intro': ('Eight versions, as asked, clean room: a separate writer for each rapper researched him on the web and watched his '
                  'videos frame by frame, then wrote a NEW start still (round 7 showed the start pose sets the whole gesture: every '
                  'T3 clip just repeated "hand to the temple") and the clip. The rough sleeper under the flyover does Eminem, 50 Cent, '
                  'Method Man and Kendrick Lamar; the rich man on the beach does Action Bronson, RZA, Ghostface Killah and Rick Ross. '
                  '"now" is the T3 clip in camping song 2 beat 4. Pick the style you want (a note helps: e.g. "Method Man for Bob, Rick '
                  'Ross for Tarquin") and it gets written for all 13 rap shots.'),
        'sections': [{'h': "The rough sleeper (Bob's verses)", 'lede': 'Duct-tape mask, under the flyover, "Waitrose door".', 'groups': groups['s02']},
                     {'h': "The rich man (Tarquin's verses)", 'lede': 'Tweed mask, the beach, "tax the rich".', 'groups': groups['t06']}]}
(HERE / 'picks-r8.json').write_text(json.dumps(spec, indent=1))
r = subprocess.run(['python3', str(REPO / 'scripts/scene/build-picks.py'), str(HERE / 'picks-r8.json'), str(OUT / 'index.html')],
                   capture_output=True, text=True, check=True)
print(r.stdout.strip()[:200]); print('missing:', missing)
