#!/usr/bin/env python3
"""Karen music video: bring Kai's Premiere edit back onto the timeline page (no split brain).

    python3 scripts/karen/mv_from_premiere.py <state.json> <render.mp4> <name> [--from r5]

<state.json> is the bridge dump of the sequence (premiere_get_sequence writes it to
<project>/.bridge/state-<sequence>.json). Every V1 clip becomes one edl shot: its id is mapped
back from the media path through catalogue.json, and its beat (section) and "why" are carried
over from the last scripted round where the same clip sits at about the same time; anything
else is marked as Kai's hand edit. The page's preview is <render.mp4> (Premiere's own render)
scaled to 1080p, so the page plays exactly what Premiere made.
Writes <media>/cut-<name>/{edl.json, preview.mp4}.
"""
import json
import pathlib
import subprocess
import sys

args = [a for a in sys.argv[1:] if not a.startswith('--')]
STATE, RENDER, NAME = pathlib.Path(args[0]), pathlib.Path(args[1]), args[2]
FROM = sys.argv[sys.argv.index('--from') + 1] if '--from' in sys.argv else 'r5'
SCENE = pathlib.Path(__file__).resolve().parents[2] / 'docs/stories/karen/scenes/music-video'
MEDIA = pathlib.Path('/mnt/d/badcode-videos/karen-music/clips/recut')
SONG = '/mnt/d/badcode-videos/karen-music/song.wav'

cat = json.loads((SCENE / 'catalogue.json').read_text())['items']
by_path = {i['path']: i['id'] for i in cat}
song = json.loads((SCENE / 'song-map.json').read_text())
prev_edl = json.loads((MEDIA / f'cut-{FROM}' / 'edl.json').read_text())
state = json.loads(STATE.read_text())
out = MEDIA / f'cut-{NAME}'
out.mkdir(parents=True, exist_ok=True)


def clip_id(path):
    if path in by_path:
        return by_path[path]
    p = pathlib.Path(path)
    if p.parent.name in ('from-story', 'recut-cartoon'):
        return p.stem
    raise SystemExit(f'no catalogue id for {path}')


def section(t):
    for s in song['sections']:
        if s['start'] - 0.75 <= t < s['end'] - 0.75:
            return s['id']
    return song['sections'][-1]['id']


video, flags, kept, changed = [], [], 0, 0
for c in state['videoTracks'][0]['items']:
    if c.get('disabled'):
        continue
    cid = clip_id(c['mediaPath'])
    a, b = round(c['start'], 4), round(c['end'], 4)
    match = [v for v in prev_edl['video'] if v['id'] == cid and abs(v['start'] - a) < 1.5]
    exact = [v for v in match if abs(v['start'] - a) < 0.05 and abs(v['start'] + v['dur'] - b) < 0.05]
    if exact:
        why, beat = exact[0]['why'], exact[0]['beat']
        kept += 1
    elif match:
        why, beat = match[0]['why'] + ' (Kai re-trimmed it in Premiere)', match[0]['beat']
        changed += 1
    else:
        why, beat = "Kai's hand edit in Premiere", section(a + 0.01)
        changed += 1
    if c.get('speed', 1) != 1:
        flags.append(f"{a:.2f}s: '{cid}' plays at {c['speed']:.0%} speed")
    video.append({'file': c['mediaPath'], 'start': a, 'dur': round(b - a, 4), 'beat': beat, 'source': c['mediaPath'],
                  'looped': False, 'in': round(c['inPoint'], 3), 'why': why, 'id': cid, 'speed': c.get('speed', 1)})

prev = out / 'preview.mp4'
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', str(RENDER), '-vf', 'scale=1920:1080', '-c:v', 'libx264',
                '-preset', 'veryfast', '-crf', '20', '-pix_fmt', 'yuv420p', '-c:a', 'aac', '-b:a', '192k', str(prev)], check=True)

edl = dict(prev_edl)
seq = state['sequence']['name']
edl.update({'sequence': seq, 'round': NAME,
            'heading': 'All Day to Complain: the final cut',
            'intro': (f"The final cut: Kai's own edit in Premiere (sequence {seq}), brought back onto this page shot for shot. "
                      f"{kept} shots are exactly as round {FROM[1:]} scripted them; {changed} are Kai's hand edits "
                      "(marked in each shot's note). Frozen 2026-11-09."),
            'video': video, 'flags': flags, 'render': str(RENDER)})
for b in edl['beats']:
    n = sum(1 for v in video if v['beat'] == b['id'])
    b['see'] = f"{n} shots. " + b['see'].split('. ', 1)[-1]
(out / 'edl.json').write_text(json.dumps(edl, indent=1))
print(json.dumps({'shots': len(video), 'kept': kept, 'hand_edits': changed, 'flags': flags, 'preview': str(prev)}, indent=1))
