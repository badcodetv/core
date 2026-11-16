#!/usr/bin/env python3
"""True Scale (BadCode Short #88): rough cut, both versions back to back (2026-11-16).

    python3 scripts/shorts/true_scale_cut.py [--round N]

Jack, 2026-11-16: "please do v2 in the same timeline so its just one after another" and, on the picks, voices and line:
"you decide". So: version 1 (the graphic one: Bob flash, 134,210, a home, 303,185 + 267,894) then a one-second slate,
then version 2 (Nearest Wins, the pub quiz). Picture is the picked STILLS with eased pushes (ffmpeg stand-in, no clips
yet), timed to the real voice lengths (lead-in 0.3 s, tail 0.5 s). The numbers on version 1's graphic beats are drawn
here (the 3D render is owed). No music yet (sound.md is EMPTY). Every voice line is its own WAV (AI Studio), placed whole.
Writes <media>/cut/r<N>/edl.json (timeline format, scripts/scene/timeline.py), stems, picture.mp4 and preview.mp4.
"""
# style-lint: story=short-true-scale (this cut script belongs to one short)
import argparse, json, pathlib, subprocess, sys

REPO = pathlib.Path(__file__).resolve().parents[2]
SCENE = REPO / 'docs/stories/short-true-scale/scenes/true-scale'
sys.path.insert(0, str(REPO / 'scripts/drive'))
from localmap import localize  # noqa: E402

cfg = localize(json.loads((SCENE / 'scene.json').read_text()))
MEDIA = pathlib.Path(cfg['media'])
MB, VOX = MEDIA / 'moodboard', MEDIA / 'audio' / 'voices'
LINES = REPO / 'docs/stories/short-true-scale/voices/lines'
W, H, FPS = 1080, 1920, 24
BOLD = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
LEAD, TAIL, GAP = 0.3, 0.5, 0.25

# (beat key, title, still, [voice line stems in order], min seconds, on-screen numbers [(text, size, y)], what we see)
SHOTS = [
    ('bob', 'v1 1. Bob', 'BO4-c', ['v1-01-narrator'], 3.0, [], 'Through a rainy windscreen, Bob on his bench looks back.'),
    ('crowd', 'v1 2. 134,210', 'CR1-a', ['v1-02-narrator'], 3.5, [('134,210', 150, 0.30), ('homeless households in England', 52, 0.40)],
     'A car park of suitcases from above: every homeless household in England.'),
    ('home', 'v1 3. A home', 'HM4-a', [], 2.2, [], 'One warm lit window on a cold terrace.'),
    ('homes', 'v1 4. 303,185 + 267,894', 'EM1-a', ['v1-03-narrator'], 4.5,
     [('303,185', 140, 0.24), ('long-term empty homes', 50, 0.33), ('+ 267,894', 110, 0.44), ('second homes', 50, 0.52)],
     'Dark terraces from the air, one small teal patch: the homes nobody lives in.'),
    ('slate', 'VERSION 2', None, [], 1.0, [('VERSION 2', 90, 0.48)], 'Slate between the two versions (review only).'),
    ('nw1', 'v2 1. Tiebreaker', 'NW1-a', ['v2-01-landlady'], 3.0, [], 'The landlady on the mic, the meat raffle on the bar.'),
    ('nw2', 'v2 2. The guesses', 'NW2-a1', ['v2-02-builder'], 2.5, [], 'A builder shouts "50,000"; Bob writes in the corner.'),
    ('nw3', 'v2 3. The answer', 'NW3-a', ['v2-03-landlady'], 3.0, [], 'The landlady reads the answer; the room groans.'),
    ('nw4', "v2 4. How'd you know?", 'NW4-b1', ['v2-04-builder', 'v2-05-bob'], 3.0, [], 'Bob\'s "300,000" sheet; the pub turned to him.'),
    ('nw5', 'v2 5. The prize', 'NW5-b1', ['v2-06-landlady'], 3.0, [], 'Bob walks out into the rain; the pub glows behind him.'),
]
WHO = {'narrator': 'BadCode (Iapetus)', 'landlady': 'Landlady (Gacrux)', 'builder': 'Builder (Fenrir)', 'bob': 'Bob (Algenib)'}


def ff(*a):
    subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', *map(str, a)], check=True)


def dur(p):
    return float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', p],
                                capture_output=True, text=True).stdout)


ENC = ['-c:v', 'libx264', '-preset', 'veryfast', '-crf', '18', '-pix_fmt', 'yuv420p', '-color_range', 'tv',
       '-colorspace', 'bt709', '-color_primaries', 'bt709', '-color_trc', 'bt709']


def main():
    ap = argparse.ArgumentParser(); ap.add_argument('--round', type=int, default=1); a = ap.parse_args()
    cut = MEDIA / 'cut' / f'r{a.round}'; cut.mkdir(parents=True, exist_ok=True)
    t, starts, durs, placed = 0.0, [], [], []  # placed: (stem, t, dur, text, who)
    for key, title, still, vox, mn, nums, see in SHOTS:
        lt, inner = t + LEAD, 0.0
        for v in vox:
            d = dur(VOX / f'{v}.wav'); placed.append((v, round(lt, 3), round(d, 3))); lt += d + GAP; inner += d + GAP
        d = max(mn, (LEAD + inner - GAP + TAIL) if vox else mn)
        starts.append(round(t, 3)); durs.append(round(d, 3)); t += d
    total = round(t, 3)
    parts = []
    for i, (key, title, still, vox, mn, nums, see) in enumerate(SHOTS):
        d, n = durs[i], int(round(durs[i] * FPS))
        txt = ''.join(f",drawtext=fontfile={BOLD}:text='{s}':fontcolor=white:fontsize={sz}:x=(w-text_w)/2:y=h*{y}"
                      f":shadowcolor=black@0.7:shadowx=3:shadowy=3:alpha='min(1,t/0.4)'" for s, sz, y in nums)
        out = cut / f'v{i:02d}-{key}.mp4'
        if still is None:
            ff('-f', 'lavfi', '-i', f'color=black:s={W}x{H}:r={FPS}:d={d}', '-vf', txt.lstrip(',') + ',scale=in_range=full:out_range=limited,format=yuv420p,lutyuv=y=clip(val\\,20\\,235)', *ENC, out)
        else:
            z = f"1+0.05*(3*pow(on/{n},2)-2*pow(on/{n},3))"
            ff('-loop', 1, '-t', d, '-i', MB / f'{still}.jpg', '-vf',
               f"scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},"
               f"zoompan=z='{z}':x='iw/2-iw/zoom/2':y='ih/2-ih/zoom/2':d=1:s={W}x{H}:fps={FPS}{txt},"
               'scale=in_range=full:out_range=limited,format=yuv420p,lutyuv=y=clip(val\\,20\\,235)', '-frames:v', n, *ENC, out)
        parts.append(out)
    (cut / 'list.txt').write_text(''.join(f"file '{p.name}'\n" for p in parts))
    ff('-f', 'concat', '-safe', '0', '-i', cut / 'list.txt', '-c', 'copy', cut / 'picture.mp4')
    stems = {}
    for who in WHO:
        mine = [(s, st, d) for s, st, d in placed if s.endswith(who)]
        if not mine: continue
        inputs, chain = [], ''
        for k, (s, st, d) in enumerate(mine):
            inputs += ['-i', VOX / f'{s}.wav']
            chain += f'[{k}]aresample=48000,aformat=channel_layouts=stereo,loudnorm=I=-16:TP=-1.5,adelay=delays={int(st * 1000)}:all=1[a{k}];'
        chain += ''.join(f'[a{k}]' for k in range(len(mine))) + f'amix=inputs={len(mine)}:normalize=0,apad=whole_dur={total},atrim=end={total}'
        stems[who] = cut / f'vox-{who}.wav'
        ff(*inputs, '-filter_complex', chain, '-ar', 48000, '-ac', 2, stems[who])
    ins = []
    for p in stems.values(): ins += ['-i', p]
    ff(*ins, '-filter_complex', ''.join(f'[{k}]' for k in range(len(stems))) + f'amix=inputs={len(stems)}:normalize=0,loudnorm=I=-14:TP=-1.5',
       '-ar', 48000, '-ac', 2, cut / 'mix.wav')
    ff('-i', cut / 'picture.mp4', '-i', cut / 'mix.wav', '-map', '0:v', '-map', '1:a', '-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k',
       '-t', total, cut / 'preview.mp4')
    beats = []
    for i, (key, title, still, vox, mn, nums, see) in enumerate(SHOTS):
        lines = [{'i': j, 'who': s.split('-')[-1], 'name': WHO[s.split('-')[-1]], 't': st, 'dur': d,
                  'text': (LINES / f'{s}.txt').read_text().strip(), 'by': 'claude' if s != 'v2-05-bob' else 'claude (Jack: "you decide")'}
                 for j, (s, st, d) in enumerate([p for p in placed if p[0] in vox])]
        beats.append({'id': key, 'title': title, 'start': starts[i], 'dur': durs[i], 'see': see, 'lines': lines})
    video = [{'file': str((MB / f'{s[2]}.jpg') if s[2] else cut / parts[i].name), 'in': 0, 'start': starts[i], 'dur': durs[i],
              'beat': s[0], 'source': str(MB / f'{s[2]}.jpg') if s[2] else 'slate', 'looped': False} for i, s in enumerate(SHOTS)]
    edl = {'sequence': f'short-true-scale-1-true-scale-r{a.round}', 'title': 'True Scale Timeline',
           'heading': f'BadCode Shorts ▲ True Scale, rough cut {a.round}: version 1 then version 2',
           'intro': ('Both versions back to back (Jack: "one after another"). Version 1: Bob, 134,210, a home, 303,185 + 267,894 '
                     '(stills with pushes; the numbers drawn on; the 3D render is still to make). Then a slate, then version 2: '
                     'Nearest Wins, the pub quiz. Picks, Bob\'s line and the voices are Claude\'s calls (Jack: "you decide"): '
                     'note anything you\'d change.'),
           'fps': FPS, 'total': total, 'beats': beats, 'video': video,
           'audio': [{'track': f'A{k + 1}', 'name': f'vox-{w}', 'file': str(p)} for k, (w, p) in enumerate(stems.items())],
           'events': [{'stem': f"vox-{s.split('-')[-1]}", 't': st, 'dur': d, 'what': (LINES / f'{s}.txt').read_text().strip(),
                       'src': str(VOX / f'{s}.wav')} for s, st, d in placed],
           'flags': ['Stills with eased pushes stand in for clips; nothing animated yet.',
                     'No music or room sound yet (sound.md EMPTY).',
                     'Version 1\'s numbers are drawn text over mood-board stills; the true-scale 3D render is owed.',
                     'The VERSION 2 slate is for review only.']}
    (cut / 'edl.json').write_text(json.dumps(edl, indent=1, ensure_ascii=False))
    print(json.dumps({'total': total, 'starts': starts, 'durs': durs, 'preview': str(cut / 'preview.mp4')}))


if __name__ == '__main__':
    main()
