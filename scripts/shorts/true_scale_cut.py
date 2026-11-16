#!/usr/bin/env python3
"""True Scale (BadCode Short #88), version 2 "Nearest Wins": rough cut (2026-11-16).

    python3 scripts/shorts/true_scale_cut.py [--round N]

Round history: r1 cut v1 + v2 from stills; r2 v2 only from five clips; r3 faster dialogue, stats card, fruit-machine logo
(see git history for those scripts). Round 4 (this): Jack, "reshoot" for lip sync, then "just use the skill we have been
using for things like bank robbery": the talking shots are re-shot with the exact words in the prompt
(cleanroom/anim-r2-talk.json) and dubbed by the lip-sync-dub skill's procedure. Mouth openings were read BY EYE from 12 fps
mouth strips with timestamps burned in (scratch mouth/s01a..s04.jpg, 2026-11-16); each phrase is laid about 0.03 s after
its opening (never early) by scripts/lipsync/place-dub.py, tempo 0.85-1.30. Phrase cuts inside our TTS takes come from
Whisper on the takes. Never LatentSync (Kai/Jack 2026-11-16). Brand-like crisp packets in clips 2 and 5 are blurred.
Then the stats card and the BadCode logo as a fruit machine (scripts/shorts/fruit_machine_logo.py). No music yet.
Writes <media>/cut/r<N>/edl.json (timeline format, scripts/scene/timeline.py), the dialogue stem, picture.mp4, preview.mp4.
"""
# style-lint: story=short-true-scale (this cut script belongs to one short)
import argparse, json, pathlib, subprocess, sys

REPO = pathlib.Path(__file__).resolve().parents[2]
SCENE = REPO / 'docs/stories/short-true-scale/scenes/true-scale'
sys.path.insert(0, str(REPO / 'scripts/drive'))
from localmap import localize  # noqa: E402

cfg = localize(json.loads((SCENE / 'scene.json').read_text()))
MEDIA = pathlib.Path(cfg['media'])
VID, VOX = MEDIA / 'video', MEDIA / 'audio' / 'voices'
W, H, FPS = 1080, 1920, 24
VO, V3 = 'v2-01-landlady', 'v2-03-landlady'
STATS = ['In England:', '', '303,185 homes have stood empty', 'for six months or more.', '', '267,894 more are second homes.', '',
         '134,210 households are homeless,', 'living in temporary accommodation.']
SOURCE = 'MHCLG, October 2025 · gov.uk, December 2025'
STATS_DUR, LOGO_DUR = 5.0, 4.2
REGULAR = '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
# (beat, title, clip, in, out, punch-in, blurs (720x1280), phrases [(take, from, to, at (clip time), tempo)], what we see)
#   mouth readings (12 fps strips): 01a "Tiebreaker" opens 0.66, a held grin 3.25-3.6, "Nearest..." 3.75-5.08 ·
#   01b opens 0.66, speech to 5.16 · 03a 1.58-3.16 then 4.25-7.08 · 03b face down to 4.1, "Table nine" 4.33, Bob's B
#   closure 5.25-5.33 then open 5.41 · 04 Bob 4.00-4.95 (the lad's mouth is out of frame)
SHOTS = [
    ('nw1', '1. Tiebreaker', 'ts-01a-t1-NW7-1-a.mp4', 0.5, 5.4, 1.0, [], [(VO, 0.0, 0.98, 0.69, 1.17), (VO, 1.82, 3.44, 3.78, 1.25)],
     'The quizmaster: "Tiebreaker! Nearest wins the meat raffle."'),
    ('nw1b', '1b. The question', 'ts-01b-t2-NW7-1-a.mp4', 0.4, 5.4, 1.18, [], [(VO, 4.12, 8.74, 0.69, 1.03)],
     '"How many homes in England have been empty six months or more?" (punched in)'),
    ('nw2', '2. The guesses', 'ts-02-NW6-2b1.mp4', 0.3, 3.0, 1.0, [(280, 900, 510, 1140)], [('v2-02-builder', 0.0, None, 0.5, 1.10)],
     'Wide: the loud table shouts "Fifty thousand, tops!"; Bob writes in the corner.'),
    ('nw3', '3. The answer', 'ts-03a-t1-NW6-3a.mp4', 1.3, 7.5, 1.0, [], [(V3, 0.0, 2.58, 1.61, 1.30), (V3, 3.16, 7.16, 4.28, 1.30)],
     'She holds up 303,185: "Three hundred and three thousand. Not counting two hundred and sixty-seven thousand second homes."'),
    ('nw3b', '3b. Table nine', 'ts-03b-t2-NW6-3a.mp4', 1.4, 6.0, 1.18, [], [(V3, 9.0, 9.84, 1.70, 1.0), (V3, 11.22, 12.66, 4.36, 1.08)],
     '"Nearest... table nine. Bob." (punched in)'),
    ('nw4', "4. How'd you know?", 'ts-04-t1-NW7-4-a.mp4', 0.6, 5.5, 1.0, [],
     [('v2-04-builder', 0.0, 0.94, 1.15, 1.0), ('v2-05-bob', 0.0, 1.5, 4.03, 1.30)], '"How\'d you know that?" Bob: "I sleep opposite one."'),
    ('nw5', '5. The prize', 'ts-05-NW6-5a2.mp4', 0.0, 3.3, 1.0, [(300, 670, 420, 780), (190, 1040, 380, 1180)],
     [('v2-06-landlady', 0.0, None, 0.3, 1.25)], 'Bob sets the meat raffle down and goes. "...Right. Picture round."'),
]


def ff(*a):
    subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', *map(str, a)], check=True)


def dur(p):
    return float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', p],
                                capture_output=True, text=True).stdout)


ENC = ['-c:v', 'libx264', '-preset', 'veryfast', '-crf', '18', '-pix_fmt', 'yuv420p', '-color_range', 'tv',
       '-colorspace', 'bt709', '-color_primaries', 'bt709', '-color_trc', 'bt709']
CLAMP = 'scale=in_range=full:out_range=limited,format=yuv420p,lutyuv=y=clip(val\\,20\\,235)'


def main():
    ap = argparse.ArgumentParser(); ap.add_argument('--round', type=int, default=4); a = ap.parse_args()
    cut = MEDIA / 'cut' / f'r{a.round}'; cut.mkdir(parents=True, exist_ok=True)
    starts, durs, t = [], [], 0.0
    for s in SHOTS:
        starts.append(round(t, 3)); durs.append(round(s[4] - s[3], 3)); t += s[4] - s[3]
    speech_end = round(t, 3); total = round(speech_end + STATS_DUR + LOGO_DUR, 3)
    parts, dubs, events = [], [], []
    for i, (key, title, clip, tin, tout, scale, blurs, phrases, see) in enumerate(SHOTS):
        d, src = durs[i], VID / clip
        chain, last = '', '0:v'
        for k, (x0, y0, x1, y1) in enumerate(blurs):
            chain += f'[{last}]split[m{k}][s{k}];[s{k}]crop={x1 - x0}:{y1 - y0}:{x0}:{y0},boxblur=16:2[c{k}];[m{k}][c{k}]overlay={x0}:{y0}[b{k}];'
            last = f'b{k}'
        zoom = f'scale=iw*{scale}:ih*{scale},crop=iw/{scale}:ih/{scale}:(iw-iw/{scale})/2:(ih-ih/{scale})*0.35,' if scale != 1 else ''
        chain += (f'[{last}]trim=start={tin}:duration={d},setpts=PTS-STARTPTS,{zoom}scale={W}:{H}:force_original_aspect_ratio=increase,'
                  f'crop={W}:{H},fps={FPS},{CLAMP}[v]')
        out = cut / f'v{i}-{key}.mp4'
        ff('-i', src, '-filter_complex', chain, '-map', '[v]', '-an', *ENC, out)
        parts.append(out)
        spec = {'duration': d, 'phrases': []}  # the skill's place-dub.py, times relative to this shot
        for take, fr, to, at, tempo in phrases:
            to = to if to is not None else dur(VOX / f'{take}.wav')
            spec['phrases'].append({'src': str(VOX / f'{take}.wav'), 'from': max(0, fr - 0.03), 'to': to + 0.05,
                                    'at': round(at - tin, 3), 'tempo': tempo})
            events.append({'stem': 'vox-dialogue', 't': round(starts[i] + at - tin, 3), 'dur': round((to - fr) / tempo, 3),
                           'what': f'{take} {fr:.2f}-{to:.2f} s x{tempo}', 'src': str(VOX / f'{take}.wav')})
        (cut / f'dub-{key}.json').write_text(json.dumps(spec, indent=1))
        subprocess.run(['python3', str(REPO / 'scripts/lipsync/place-dub.py'), str(cut / f'dub-{key}.json'), str(cut / f'dub-{key}.wav'),
                        '--lufs', '-16'], check=True, capture_output=True)
        dubs.append(cut / f'dub-{key}.wav')
    # the stats, plain text on black, then the BadCode logo landing like a fruit machine
    (cut / 'stats.txt').write_text('\n'.join(STATS))
    ff('-f', 'lavfi', '-i', f'color=black:s={W}x{H}:r={FPS}:d={STATS_DUR}', '-vf',
       f"drawtext=fontfile={REGULAR}:textfile={cut / 'stats.txt'}:fontcolor=white:fontsize=42:line_spacing=16:x=110:y=(h-text_h)/2-60:alpha='min(1,t/0.5)',"
       f"drawtext=fontfile={REGULAR}:text='{SOURCE}':fontcolor=0x9a9a9a:fontsize=30:x=110:y=h*0.74:alpha='min(1,t/0.5)',{CLAMP}",
       *ENC, cut / 'v8-stats.mp4')
    subprocess.run(['python3', str(REPO / 'scripts/shorts/fruit_machine_logo.py'), str(cut / 'v9-logo.mp4'), '--seconds', str(LOGO_DUR)],
                   check=True, capture_output=True)
    parts += [cut / 'v8-stats.mp4', cut / 'v9-logo.mp4']
    (cut / 'list.txt').write_text(''.join(f"file '{p.name}'\n" for p in parts))
    ff('-f', 'concat', '-safe', '0', '-i', cut / 'list.txt', '-c', 'copy', cut / 'picture.mp4')
    (cut / 'dubs.txt').write_text(''.join(f"file '{p.name}'\n" for p in dubs))
    ff('-f', 'concat', '-safe', '0', '-i', cut / 'dubs.txt', '-af', f'apad=whole_dur={total},atrim=end={total}', '-ar', 48000, '-ac', 2,
       cut / 'vox-dialogue.wav')
    ff('-i', cut / 'vox-dialogue.wav', '-af', 'loudnorm=I=-14:TP=-1.5', '-ar', 48000, '-ac', 2, cut / 'mix.wav')
    ff('-i', cut / 'picture.mp4', '-i', cut / 'mix.wav', '-map', '0:v', '-map', '1:a', '-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k',
       '-t', total, cut / 'preview.mp4')
    beats = [{'id': s[0], 'title': s[1], 'start': starts[i], 'dur': durs[i], 'see': s[8],
              'lines': [{'i': j, 'who': 'dialogue', 'name': 'Dialogue', 't': e['t'], 'dur': e['dur'], 'text': e['what'], 'by': 'claude'}
                        for j, e in enumerate([e for e in events if starts[i] <= e['t'] < starts[i] + durs[i]])]} for i, s in enumerate(SHOTS)]
    beats += [{'id': 'stats', 'title': '6. The numbers', 'start': speech_end, 'dur': STATS_DUR, 'see': ' '.join(x for x in STATS if x), 'lines': []},
              {'id': 'logo', 'title': '7. Logo (fruit machine)', 'start': round(speech_end + STATS_DUR, 3), 'dur': LOGO_DUR,
               'see': 'Three reels spin and stop on the mark, "bad", "code"; the bulbs and frame blink.', 'lines': []}]
    edl = {'sequence': f'short-true-scale-1-nearest-wins-r{a.round}', 'title': 'True Scale Timeline',
           'heading': f'BadCode Shorts ▲ True Scale: Nearest Wins, rough cut {a.round}',
           'intro': ('Talking shots re-shot with the words and dubbed the Bank Robbery way (mouths read by eye, voice never early). '
                     'Then the numbers in plain text and the logo as a fruit machine. Music to come (picks page). Note anything.'),
           'fps': FPS, 'total': total, 'beats': beats,
           'video': [{'file': str(VID / s[2]), 'in': s[3], 'start': starts[i], 'dur': durs[i], 'beat': s[0], 'source': str(VID / s[2]),
                      'looped': False} for i, s in enumerate(SHOTS)] +
                    [{'file': str(cut / 'v8-stats.mp4'), 'in': 0, 'start': speech_end, 'dur': STATS_DUR, 'beat': 'stats', 'source': 'stats card', 'looped': False},
                     {'file': str(cut / 'v9-logo.mp4'), 'in': 0, 'start': round(speech_end + STATS_DUR, 3), 'dur': LOGO_DUR, 'beat': 'logo',
                      'source': 'scripts/shorts/fruit_machine_logo.py', 'looped': False}],
           'audio': [{'track': 'A1', 'name': 'vox-dialogue', 'file': str(cut / 'vox-dialogue.wav')}],
           'events': events,
           'flags': ['Talking shots dubbed by the lip-sync-dub skill: openings read by eye at 12 fps, phrases ~0.03 s after, x0.85-1.30.',
                     'Lines past the cap overrun the mouth by ~0.2 s (3a, Bob): late, never early.', 'No music yet.']}
    (cut / 'edl.json').write_text(json.dumps(edl, indent=1, ensure_ascii=False))
    print(json.dumps({'total': total, 'starts': starts, 'durs': durs, 'preview': str(cut / 'preview.mp4')}))


if __name__ == '__main__':
    main()
