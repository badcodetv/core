#!/usr/bin/env python3
"""Ten Economic Commandments: rough cut 3, the 62-second version (2026-11-20).

    python3 scripts/shorts/tec_cut_r3.py [--round N] [--picks picks.json]

Jack, 2026-11-20: "Build a 62 second version but also add the clips from the last version of this as well on top of
everything." Read as: keep every rapping location from rough cut 2 AND bring back rough cut 1's clips (ec-0N-tK, the
seven round-4 stills animated), intercut. (A guess at "on top of": in addition, not a layer over the picture.)

Length: the song (e689e000) starts one beat before its first downbeat (1.358 s in; the first word is at ~2.0 s), so
all ten rules and the fix (ends 60.98 s in the song) land by 59.6 s, the beat-out is dropped, and the logo card takes
the last bar to 62.0 s while the song fades.
Picture: each two-bar rule = bar 1 BadCode rapping at that rule's rough-cut-2 location (the number word on the cut),
bar 2 a rough-cut-1 clip chosen by what the line is about. Rule five has one bar: rapper only. Intro = the chalkboard
doorstep (rough cut 1's opener), then the skyline. The fix = the empty gloved hands (rough cut 1's fix shot).
Everything gets nightfever (Jack's finish, round 4); the logo card is never filtered.
"""
# style-lint: story=short-ten-economic-commandments (this cut script belongs to one short)
import argparse, json, pathlib, subprocess, sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from tec_cut_r2 import ff, clip_for, bar, MEDIA, VID, SONG, LOGO, FINISH, W, H, FPS, CLAMP, ENC, BAR, D0, SEE  # noqa: E402

TOTAL = 62.0
O = round(D0 - BAR / 4, 3)  # song in-point: one beat before the first downbeat


def t(i):  # timeline time of song bar i
    return round(bar(i) - O, 3)


SEE1 = {'ec-01-t1-RU4-1-b.mp4': 'Doorstep, the chalkboard (rough cut 1)', 'ec-03-t1-SU4-1-a.mp4': 'Subway, fanning banknotes (rough cut 1)',
        'ec-04-t1-RU4-2-a.mp4': 'Red studio, fisheye, two fingers up (rough cut 1)', 'ec-02-t1-RU4-5-b.mp4': 'Dusk crowd, mic at the lens (rough cut 1)',
        'ec-05-t1-SU4-3-b.mp4': 'Bridge street, notes falling (rough cut 1)', 'ec-06-t1-RU4-3-a.mp4': 'The fence bench (rough cut 1)',
        'ec-03-t2-SU4-1-a.mp4': 'Subway, banknotes, take 2 (rough cut 1)', 'ec-05-t2-SU4-3-b.mp4': 'Bridge street, notes falling, take 2 (rough cut 1)',
        'ec-02-t2-RU4-5-b.mp4': 'Dusk crowd, mic, take 2 (rough cut 1)', 'ec-06-t2-RU4-3-a.mp4': 'The fence bench, take 2 (rough cut 1)',
        'ec-07-t1-FX4-1-b.mp4': 'Streetlight, empty gloved hands (rough cut 1)', 'ec-r5-fix1-a-U5-fix1.mp4': 'The Empire State skyline at dusk'}

# (beat, title, [(location key, default take) or clip file, in-point, start bar], what is heard). Start bar None = 0 s.
BEATS = [
    ('intro', '1. Intro', [('ec-01-t1-RU4-1-b.mp4', 0.3, None), ('ec-r5-fix1-a-U5-fix1.mp4', 0.0, 1)], '"Uh. Money printer manual. Take notes."'),
    ('uno', '2. Rule Uno', [(('fix1-a', 'a'), 0.4, 2), ('ec-03-t1-SU4-1-a.mp4', 0.5, 3)], '"Rule number Uno: never say how much you made…"'),
    ('two', '3. Number two', [(('r3-press2-a', 'a'), 0.4, 4), ('ec-04-t1-RU4-2-a.mp4', 0.4, 5)], '"Never show \'em your next move…"'),
    ('three', '4. Number three', [(('vibe3-b', 'a'), 0.4, 6), ('ec-02-t1-RU4-5-b.mp4', 0.5, 7)], '"Never trust nobody with the press…"'),
    ('four', '5. Number four', [(('r10-bailout2-b', 'a'), 0.4, 8), ('ec-05-t1-SU4-3-b.mp4', 0.5, 9)], '"Never get high on your own supply…"'),
    ('five', '6. Number five', [(('vibe2-b', 'a'), 0.4, 10)], '"Never print where you sleep…"'),
    ('six', '7. Number six', [(('vibe6-b', 'a'), 0.4, 11), ('ec-06-t1-RU4-3-a.mp4', 0.2, 12)], '"No credit? Forget it…"'),
    ('seven', '8. Number seven', [(('vibe8-a', 'a'), 0.4, 13), ('ec-03-t2-SU4-1-a.mp4', 0.5, 14)], '"Keep your money and your assets apart…"'),
    ('eight', '9. Number eight', [(('vibe9-b', 'a'), 0.4, 15), ('ec-05-t2-SU4-3-b.mp4', 0.5, 16)], '"Hold none of it yourself…"'),
    ('nine', '10. Number nine', [(('vibe7-a', 'a'), 0.4, 17), ('ec-02-t2-RU4-5-b.mp4', 0.5, 18)], '"Keep the auditors out…"'),
    ('ten', '11. Number ten', [(('vibe4-b', 'a'), 0.4, 19), ('ec-06-t2-RU4-3-a.mp4', 0.2, 20)], '"Cash up front, that\'s law… they ain\'t paid it all."'),
    ('fix', '12. The fix', [('ec-07-t1-FX4-1-b.mp4', 0.3, 21)], '"And the fix, from the future? No hand on the printer."'),
]
LOGO_BAR = 22


def main():
    ap = argparse.ArgumentParser(); ap.add_argument('--round', type=int, default=3); ap.add_argument('--picks')
    a = ap.parse_args()
    picks = json.loads(pathlib.Path(a.picks).read_text()) if a.picks else {}
    cut = MEDIA / 'cut' / f'r{a.round}'; cut.mkdir(parents=True, exist_ok=True)
    shots = [(key, src, tin, b) for key, _, ss, _ in BEATS for src, tin, b in ss]
    parts, vids = [], []
    for i, (key, src, tin, b) in enumerate(shots):
        st = 0.0 if b is None else t(b)
        en = t(shots[i + 1][3]) if i + 1 < len(shots) else t(LOGO_BAR)
        if isinstance(src, tuple):
            loc, take = src; take = picks.get(loc, take); clip = clip_for(loc, take); see = SEE[loc]
        else:
            clip = src; see = SEE1[clip]
        d = round(en - st, 3); raw = cut / f'raw{i:02d}.mp4'; out = cut / f'v{i:02d}-{key}.mp4'
        ff('-ss', tin, '-i', VID / clip, '-t', d, '-vf', f'scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},fps={FPS}',
           '-an', '-c:v', 'libx264', '-crf', '14', '-preset', 'veryfast', raw)
        subprocess.run([str(FINISH), 'nightfever', str(raw), str(out)], check=True); raw.unlink()
        ff('-i', out, '-vf', CLAMP, *ENC, cut / f'c{i:02d}.mp4'); (cut / f'c{i:02d}.mp4').replace(out)
        parts.append(out)
        vids.append({'file': str(VID / clip), 'in': tin, 'start': st, 'dur': d, 'beat': key, 'source': str(VID / clip), 'looped': False, 'see': see})
    ls = t(LOGO_BAR); ld = round(TOTAL - ls, 3)
    ff('-f', 'lavfi', '-i', f'color=black:s={W}x{H}:r={FPS}:d={ld}', '-loop', '1', '-i', LOGO, '-filter_complex',
       f"[1]scale={int(W * 0.62)}:-1,format=rgba,fade=t=in:st=0.1:d=0.4:alpha=1[l];[0][l]overlay=(W-w)/2:(H-h)/2:shortest=1,{CLAMP}",
       '-t', ld, *ENC, cut / 'v99-logo.mp4')
    parts.append(cut / 'v99-logo.mp4')
    (cut / 'list.txt').write_text(''.join(f"file '{p.name}'\n" for p in parts))
    ff('-f', 'concat', '-safe', '0', '-i', cut / 'list.txt', '-c', 'copy', cut / 'picture.mp4')
    ff('-ss', O, '-i', SONG, '-af', f'aresample=48000,aformat=channel_layouts=stereo,atrim=end={TOTAL},afade=t=in:d=0.03,'
       f'afade=t=out:st={ls}:d={round(TOTAL - ls, 3)},loudnorm=I=-14:TP=-1.5', '-ar', 48000, '-ac', 2, cut / 'mus-rap.wav')
    ff('-i', cut / 'picture.mp4', '-i', cut / 'mus-rap.wav', '-map', '0:v', '-map', '1:a', '-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k',
       '-t', TOTAL, cut / 'preview.mp4')
    beats = []
    for key, title, ss, hear in BEATS:
        mine = [v for v in vids if v['beat'] == key]; st = mine[0]['start']; d = round(sum(v['dur'] for v in mine), 3)
        beats.append({'id': key, 'title': title, 'start': st, 'dur': d, 'see': ' / '.join(v['see'] for v in mine),
                      'lines': [{'i': 0, 'who': 'rap', 'name': 'The rap', 't': st, 'dur': d, 'text': hear, 'by': 'jack'}]})
    beats.append({'id': 'logo', 'title': '13. Logo', 'start': ls, 'dur': ld, 'see': 'The BadCode logo on black, the song fading', 'lines': []})
    for v in vids:
        v.pop('see')
    edl = {'sequence': f'short-ten-economic-commandments-1-tec-r{a.round}', 'title': 'Ten Commandments Timeline',
           'heading': f'BadCode Shorts ▲ Ten Economic Commandments, rough cut {a.round} (62 s)',
           'intro': 'The 62-second version: all ten rules and the fix, no beat-out. Each rule cuts from BadCode rapping on location '
                    'to a clip from rough cut 1 on the next bar. Nightfever on. Note anything.',
           'fps': FPS, 'total': TOTAL, 'beats': beats,
           'video': vids + [{'file': str(cut / 'v99-logo.mp4'), 'in': 0, 'start': ls, 'dur': ld, 'beat': 'logo', 'source': 'logo card', 'looped': False}],
           'audio': [{'track': 'A1', 'name': 'mus-rap', 'file': str(cut / 'mus-rap.wav')}],
           'events': [{'stem': 'mus-rap', 't': 0, 'dur': TOTAL, 'what': f"Jack's pick, Suno e689e000, from {O} s in, faded under the logo", 'src': str(SONG)}],
           'flags': ['"Add the clips from the last version on top of everything" read as: intercut rough cut 1\'s clips with the rapping, '
                     'rapper on the number, rough-cut-1 clip on the next bar. If you meant a layer over the picture, say so.',
                     'Dropped for length: the beat-out (stoop upright, Wall Street b) and the Empire State fix shot; the fix is the gloved hands now.',
                     'Rapping takes are my default (a) until the round-5 picks on the stills page are in.',
                     'Rough cut 1 clips 01-t2, 04-t2 and 07-t2 are unused. Fence bench (06): used from its start, the head turns side-on later.',
                     'Logo is 2.1 s (one bar) because of the 62 s limit.']}
    (cut / 'edl.json').write_text(json.dumps(edl, indent=1, ensure_ascii=False))
    print(json.dumps({'total': TOTAL, 'shots': len(vids), 'logo_at': ls, 'preview': str(cut / 'preview.mp4')}))


if __name__ == '__main__':
    main()
