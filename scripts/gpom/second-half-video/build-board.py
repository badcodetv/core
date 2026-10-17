#!/usr/bin/env python3
"""Build the second-half cutting-room board: every frame in story order, with its clip.

Veo frames show the clip (a 640px silent preview), its contact sheet and the plate. Post-only
frames show the plate and what Premiere/ffmpeg will do, so the whole running order reads.
Kai's verdicts go in the page's db, collection `picks` (doc `<key>__<user>`: verdict keep|redo,
note).

    python3 scripts/gpom/second-half-video/build-board.py <out-dir>
Writes <out-dir>/index.html plus media/; publish with every media file in `files`.
"""
import html
import json
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import shots as S  # noqa: E402

out = pathlib.Path(sys.argv[1])
media = out / 'media'
media.mkdir(parents=True, exist_ok=True)
sb = json.loads((S.SCENES / 'second-half-storyboard.json').read_text())['frames']
ao = {str(f['n']): f for f in json.loads((S.SCENES / 'second-half-animation-options.json').read_text())['frames']}
by_n = {}
for s in S.shots():
    by_n.setdefault(s['n'], []).append(s)


def run(cmd):
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def thumb(src, name):
    dst = media / name
    if not dst.exists():
        run(['ffmpeg', '-y', '-i', src, '-vf', 'scale=480:-2', '-q:v', '4', str(dst)])
    return f'media/{name}'


def preview(mp4, name):
    dst = media / name
    if not dst.exists():
        run(['ffmpeg', '-y', '-i', mp4, '-an', '-vf', 'scale=640:-2', '-c:v', 'libx264', '-crf', '27',
             '-preset', 'veryfast', '-pix_fmt', 'yuv420p', '-movflags', '+faststart', str(dst)])
    return f'media/{name}'


def sheet(mp4, name):
    full = pathlib.Path(mp4).with_name(pathlib.Path(mp4).stem + '-sheet.jpg')
    if not full.exists():
        run([str(S.REPO / 'scripts/video-contact-sheet.sh'), mp4, str(full)])
    dst = media / name
    if not dst.exists():
        run(['ffmpeg', '-y', '-i', str(full), '-vf', 'scale=1400:-2', '-q:v', '5', str(dst)])
    return f'media/{name}'


# Claude's first look at each contact sheet, 17 Oct 2026. Kai's verdict overrides.
REVIEW = {
    '01': 'Machines circle. The camera is not quite locked: sky creeps in at the top. Crop in post.',
    '02': 'Works. The machine rolls straight over the lens to full black by about 4s.',
    '03': 'Slow forward creep. Watch the parked cars for reshaping on the far side.',
    '05': 'Good. Steam off the kettle, a figure walks away down the tunnel.',
    '06': 'Good. Big angry gestures, the room holds.',
    '07-1': 'Good. She argues, he folds his arms and turns away.',
    '07-2': 'Good. He throws his arms wide; her shoulder stays still at the edge.',
    '08': 'Fast and red. The plate\'s KILL MODE text is burned in and smears: crop it or cover it with the ffmpeg HUD.',
    '09': 'Uncast take. The bot turns and rolls in the dust, beacon flashing.',
    '09-c': 'Bot cast. Spins harder in the dust; the machines race off behind.',
    '10': 'Dust trails race across the downs into the sun, but the machines themselves read poorly. Possible redo.',
    '12': 'Strong. Blasts keep going, then fire and black smoke. The doors stay untouched.',
    '12-element': 'Clean blast on black, ready to Luma Key three times over 12.',
    '14': 'Good. The doors open, light and smoke pour in, the pair turn to look.',
    '15': 'Bot cast. In the first second the bot jumps back to the doors and shrinks, then creeps in. Same as the uncast take.',
    '15-r2': 'Re-roll with a prompt that starts from the bot already inside. Still shrinks in the first second, less. Suggest a post-only hold or a new plate.',
    '17': 'Good. Slow blink and head tilt, unimpressed.',
    '19': 'SBEMERb (Flow refused SBEMERa). Bot cast. People shift at the bunker door.',
    '20': 'Uncast take. The bot rolls forward; the crowd holds.',
    '20-c': 'Bot cast. The bot rolls further across the floor; the crowd holds.',
    '22': 'Good. One small figure walks away into the white hall.',
    '25': 'Subtle. Check whether the hands actually meet.',
    '26': 'Very still. The steam is faint.',
    '28': 'Good. Rain and streetlights slide past the window.',
    '29': 'Good. The bus pulls away down the wet street.',
}

cards = []
for f in sb:
    n = f['n']
    opt = next(o for o in ao[str(f['anim'])]['options'] if o['id'] == S.ANIM_PICKS[n])
    sid = S.STILL_PICKS.get(n, f['stills'][0] if f['stills'] else None)
    if not sid and f.get('reuse'):
        sid = next(x for x in sb if x['n'] == f['reuse'])['stills'][0]
    card = {'n': n, 'title': f['title'], 'act': f['act'], 'line': f.get('line', ''), 'option': opt['id'],
            'label': opt['label'], 'idea': opt['idea'], 'seconds': opt.get('seconds', ''),
            'still': thumb(S.still_path(sid), f'still-{n:02d}.jpg') if sid else None, 'stillId': sid,
            'clips': []}
    for s in by_n.get(n, []):
        clip = {'key': s['key'], 'label': s['label'], 'motion': s['motion'], 'review': REVIEW.get(s['key'], ''),
                'cast': bool(s['character']) and s['key'] not in ('09', '20'),
                'stillId': s['still']}
        if s['still'] and s['still'] != sid:
            clip['plate'] = thumb(s['src'], f"still-{s['key']}.jpg")
        if pathlib.Path(s['out']).exists():
            clip['video'] = preview(s['out'], f"clip-{s['key']}.mp4")
            clip['sheet'] = sheet(s['out'], f"sheet-{s['key']}.jpg")
            clip['file'] = s['out']
        card['clips'].append(clip)
    if not card['clips']:
        card['post'] = [f"{l['lane']}: {l['does']}" for l in opt['lanes']]
    cards.append(card)

page = (HERE / 'board-template.html').read_text().replace('/*DATA*/null', json.dumps(cards))
(out / 'index.html').write_text(page)
print(json.dumps({'cards': len(cards), 'clips': sum(1 for c in cards for x in c['clips'] if 'video' in x),
                  'files': sorted(str(p.relative_to(out)) for p in media.iterdir())}))
