#!/usr/bin/env python3
"""True Scale (BadCode Short #88), version 2 "Nearest Wins": rough cut (2026-11-16).

    python3 scripts/shorts/true_scale_cut.py [--round N]

Jack, 2026-11-16: "scrap version one and just do version two" (round 2 of this script; round 1 cut v1 + v2 from stills,
see git history). Five Omni clips (stills NW7-1-a, NW6-2b1, NW6-3a, NW7-4-a, NW6-5a2), the clips' own sound dropped. The
voice lines (AI Studio: landlady Sulafat, builder Achird, Bob Algenib) run back to back with a small gap; the picture cuts
at fixed points chosen against them (a clip that has to run past its 8 s holds its last frame, flagged `looped`).
Brand-like crisp packets in clips 2 and 5 are blurred. Each line is levelled on its own file first, then placed (loudnorm
in the same graph as adelay dropped the delays: round 1's stacked voices). No music yet.
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
VID, VOX = MEDIA / 'video', MEDIA / 'audio' / 'voices'
LINES = REPO / 'docs/stories/short-true-scale/voices/lines'
W, H, FPS = 1080, 1920, 24
LEAD, GAP, TAIL = 0.3, 0.25, 0.6
ORDER = ['v2-01-landlady', 'v2-02-builder', 'v2-03-landlady', 'v2-04-builder', 'v2-05-bob', 'v2-06-landlady']
WHO = {'landlady': 'Landlady (Sulafat)', 'builder': 'Builder (Achird)', 'bob': 'Bob (Algenib)'}
# (beat, title, clip, in, picture ends at, blur boxes on the 720x1280 clip, what we see)
#   ends: ('t', s) absolute · ('len', s) after its start · ('after', line, pad) · ('end', 0)
SHOTS = [
    ('nw1', '1. Tiebreaker', 'ts-01-NW7-1-a.mp4', 0.0, ('t', 8.0), [], 'The quizmaster lifts the sheet and asks the tiebreaker.'),
    ('nw2', '2. The guesses', 'ts-02-NW6-2b1.mp4', 0.3, ('after', 'v2-02-builder', 0.35),
     [(280, 900, 510, 1140)], 'Wide across the room: the loud table shouts its guess; Bob writes in the corner.'),
    ('nw3', '3. The answer', 'ts-03-NW6-3a.mp4', 0.0, ('len', 8.0), [], 'The quizmaster holds up 303,185; the room groans.'),
    ('nw4', "4. How'd you know?", 'ts-04-NW7-4-a.mp4', 0.0, ('after', 'v2-05-bob', 0.4), [],
     'Bob stands behind his "300,000" sheet; the room turns to him. "How\'d you know that?" "I sleep opposite one."'),
    ('nw5', '5. The prize', 'ts-05-NW6-5a2.mp4', 0.0, ('end', 0), [(300, 670, 420, 780), (190, 1040, 380, 1180)],
     'Bob sets the meat raffle down for the next table and goes. "...Right. Picture round."'),
]


def ff(*a):
    subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', *map(str, a)], check=True)


def dur(p):
    return float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', p],
                                capture_output=True, text=True).stdout)


ENC = ['-c:v', 'libx264', '-preset', 'veryfast', '-crf', '18', '-pix_fmt', 'yuv420p', '-color_range', 'tv',
       '-colorspace', 'bt709', '-color_primaries', 'bt709', '-color_trc', 'bt709']


def main():
    ap = argparse.ArgumentParser(); ap.add_argument('--round', type=int, default=2); a = ap.parse_args()
    cut = MEDIA / 'cut' / f'r{a.round}'; cut.mkdir(parents=True, exist_ok=True)
    t, placed = LEAD, {}
    for s in ORDER:
        d = dur(VOX / f'{s}.wav'); placed[s] = (round(t, 3), round(d, 3)); t += d + GAP
    total = round(t - GAP + TAIL, 3)
    starts, durs, t = [], [], 0.0
    for key, title, clip, tin, end, blurs, see in SHOTS:
        if end[0] == 't': e = end[1]
        elif end[0] == 'len': e = t + end[1]
        elif end[0] == 'after': e = sum(placed[end[1]]) + end[2]
        else: e = total
        starts.append(round(t, 3)); durs.append(round(e - t, 3)); t = e
    parts, looped = [], []
    for i, (key, title, clip, tin, end, blurs, see) in enumerate(SHOTS):
        d, src = durs[i], VID / clip
        over = max(0.0, tin + d - dur(src) + 0.05); looped.append(over > 0)
        chain, last = '', '0:v'
        for k, (x0, y0, x1, y1) in enumerate(blurs):
            chain += f'[{last}]split[m{k}][s{k}];[s{k}]crop={x1 - x0}:{y1 - y0}:{x0}:{y0},boxblur=16:2[c{k}];[m{k}][c{k}]overlay={x0}:{y0}[b{k}];'
            last = f'b{k}'
        chain += (f'[{last}]trim=start={tin},setpts=PTS-STARTPTS,' + (f'tpad=stop_mode=clone:stop_duration={over:.3f},' if over else '') +
                  f'trim=duration={d},setpts=PTS-STARTPTS,scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},fps={FPS},'
                  'scale=in_range=full:out_range=limited,format=yuv420p,lutyuv=y=clip(val\\,20\\,235)[v]')
        out = cut / f'v{i}-{key}.mp4'
        ff('-i', src, '-filter_complex', chain, '-map', '[v]', '-an', *ENC, out)
        parts.append(out)
    (cut / 'list.txt').write_text(''.join(f"file '{p.name}'\n" for p in parts))
    ff('-f', 'concat', '-safe', '0', '-i', cut / 'list.txt', '-c', 'copy', cut / 'picture.mp4')
    stems = {}
    for who in WHO:
        mine = [(s, *placed[s]) for s in ORDER if s.endswith(who)]
        inputs, chain = [], ''
        for k, (s, st, d) in enumerate(mine):
            lv = cut / f'lvl-{s}.wav'
            ff('-i', VOX / f'{s}.wav', '-af', 'loudnorm=I=-16:TP=-1.5', '-ar', 48000, '-ac', 2, lv)
            inputs += ['-i', lv]
            chain += f'[{k}]adelay=delays={int(st * 1000)}:all=1,apad=whole_dur={total}[a{k}];'
        chain += ''.join(f'[a{k}]' for k in range(len(mine))) + f'amix=inputs={len(mine)}:normalize=0:duration=longest,atrim=end={total}'
        stems[who] = cut / f'vox-{who}.wav'
        ff(*inputs, '-filter_complex', chain, '-ar', 48000, '-ac', 2, stems[who])
    ins = []
    for p in stems.values(): ins += ['-i', p]
    ff(*ins, '-filter_complex', ''.join(f'[{k}]' for k in range(len(stems))) + f'amix=inputs={len(stems)}:normalize=0,loudnorm=I=-14:TP=-1.5',
       '-ar', 48000, '-ac', 2, cut / 'mix.wav')
    ff('-i', cut / 'picture.mp4', '-i', cut / 'mix.wav', '-map', '0:v', '-map', '1:a', '-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k',
       '-t', total, cut / 'preview.mp4')
    beats = []
    for i, (key, title, clip, tin, end, blurs, see) in enumerate(SHOTS):
        s0, s1 = starts[i], starts[i] + durs[i]
        lines = [{'i': j, 'who': s.split('-')[-1], 'name': WHO[s.split('-')[-1]], 't': placed[s][0], 'dur': placed[s][1],
                  'text': (LINES / f'{s}.txt').read_text().strip(), 'by': 'claude'}
                 for j, s in enumerate([s for s in ORDER if s0 <= placed[s][0] < s1])]
        beats.append({'id': key, 'title': title, 'start': s0, 'dur': durs[i], 'see': see, 'lines': lines})
    edl = {'sequence': f'short-true-scale-1-nearest-wins-r{a.round}', 'title': 'True Scale Timeline',
           'heading': f'BadCode Shorts ▲ True Scale: Nearest Wins, rough cut {a.round}',
           'intro': ('Version 2 only (Jack: "scrap version one"). Five clips from the diverse-crowd stills, the subtler voices '
                     '(landlady Sulafat, builder Achird; Bob unchanged), crisp packets blurred. No music yet. Note anything.'),
           'fps': FPS, 'total': total, 'beats': beats,
           'video': [{'file': str(VID / s[2]), 'in': s[3], 'start': starts[i], 'dur': durs[i], 'beat': s[0],
                      'source': str(VID / s[2]), 'looped': looped[i]} for i, s in enumerate(SHOTS)],
           'audio': [{'track': f'A{k + 1}', 'name': f'vox-{w}', 'file': str(p)} for k, (w, p) in enumerate(stems.items())],
           'events': [{'stem': f"vox-{s.split('-')[-1]}", 't': placed[s][0], 'dur': placed[s][1],
                       'what': (LINES / f'{s}.txt').read_text().strip(), 'src': str(VOX / f'{s}.wav')} for s in ORDER],
           'flags': ['No music or pub room sound yet.',
                     'Mouths are not synced to the voices yet (lip-sync-dub to follow on the speaking shots).',
                     'The landlady\'s answer line runs ~13 s: the first thing to trim.']}
    (cut / 'edl.json').write_text(json.dumps(edl, indent=1, ensure_ascii=False))
    print(json.dumps({'total': total, 'starts': starts, 'durs': durs, 'looped': looped, 'preview': str(cut / 'preview.mp4')}))


if __name__ == '__main__':
    main()
