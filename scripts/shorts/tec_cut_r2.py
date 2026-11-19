#!/usr/bin/env python3
"""Ten Economic Commandments: rough cut to the all-ten rap (2026-11-19).

    python3 scripts/shorts/tec_cut_r2.py [--round N] [--picks picks.json]

The track is Jack's pick, Suno e689e000 ("a number gets its bar", 74.4 s, recorded). scripts/beat-grid.py: 89.1 BPM,
bar 2.6935 s, first downbeat 2.0317 s. Whisper puts each rule's number word just before a downbeat, so every rule cuts on
the downbeat nearest its number (rules two to four were missed by Whisper and are placed from their line starts).
Picture: BadCode rapping on location (clips ec-r8-*, clean-room motion cleanroom/perform-r8.json), one location per rule,
chosen by what the rule is about; until Jack's round-5 picks are read, take a (the big one) for every rule.
Each shot gets the nightfever finish (scripts/shorts/tec_finish.sh, Jack's pick, round 4); the logo card is never filtered.
--picks: a JSON {"<location key>": "a"|"b"} from the stills page, round 5, overriding the default take.
Writes <media>/cut/r<N>/edl.json (timeline format), picture.mp4, mus-rap.wav and preview.mp4.
"""
# style-lint: story=short-ten-economic-commandments (this cut script belongs to one short)
import argparse, json, pathlib, subprocess, sys

REPO = pathlib.Path(__file__).resolve().parents[2]
SCENE = REPO / 'docs/stories/short-ten-economic-commandments/scenes/ten-economic-commandments'
sys.path.insert(0, str(REPO / 'scripts/drive'))
from localmap import localize  # noqa: E402

cfg = localize(json.loads((SCENE / 'scene.json').read_text()))
MEDIA = pathlib.Path(cfg['media'])
VID = MEDIA / 'video'
SONG = MEDIA / 'audio/tec-all10-a-number-gets-its-bar-v6-w25-e689e000.wav'
LOGO = REPO / 'docs/brand/logo/badcode-stacked-reversed-2400.png'
FINISH = REPO / 'scripts/shorts/tec_finish.sh'
W, H, FPS = 1080, 1920, 24
TOTAL = 74.4
BAR, D0 = 2.6935, 2.0317


def bar(i):
    return round(D0 + i * BAR, 3)


# (beat, title, location key, default take, clip file or None for an r8 location, in, start bar, what is heard)
SHOTS = [
    ('intro', '1. Intro', None, None, 'ec-r5-fix1-a-U5-fix1.mp4', 0.0, None, '"Money printer manual. Take notes."'),
    ('uno', '2. Rule Uno', 'fix1-a', 'a', None, 0.4, 2, '"Rule number Uno: never say how much you made…"'),
    ('two', '3. Number two', 'r3-press2-a', 'a', None, 0.4, 4, '"Never show \'em your next move…"'),
    ('three', '4. Number three', 'vibe3-b', 'a', None, 0.4, 6, '"Never trust nobody with the press…"'),
    ('four', '5. Number four', 'r10-bailout2-b', 'a', None, 0.4, 8, '"Never get high on your own supply…"'),
    ('five', '6. Number five', 'vibe2-b', 'a', None, 0.4, 10, '"Never print where you sleep…"'),
    ('six', '7. Number six', 'vibe6-b', 'a', None, 0.4, 11, '"No credit? Forget it…"'),
    ('seven', '8. Number seven', 'vibe8-a', 'a', None, 0.4, 13, '"Keep your money and your assets apart…"'),
    ('eight', '9. Number eight', 'vibe9-b', 'a', None, 0.4, 15, '"Hold none of it yourself…"'),
    ('nine', '10. Number nine', 'vibe7-a', 'a', None, 0.4, 17, '"Keep the auditors out…"'),
    ('ten', '11. Number ten', 'vibe4-b', 'a', None, 0.4, 19, '"Cash up front, that\'s law… they ain\'t paid it all."'),
    ('fix', '12. The fix', 'fix1-a', 'b', None, 0.4, 21, '"And the fix, from the future? No hand on the printer."'),
    ('out1', '13. Beat out', 'vibe2-a', 'b', None, 0.4, 22, 'The beat'),
    ('out2', '14. Beat out', 'r3-press2-a', 'b', None, 0.4, 24, 'The beat'),
]
LOGO_BAR = 25
SEE = {'fix1-a': 'Empire State, the top deck at night', 'r3-press2-a': 'Wall Street platform, the sign on the column',
       'vibe3-b': 'Walkway under the elevated track', 'r10-bailout2-b': 'Small between marble columns',
       'vibe2-b': 'Sitting on the stoop, leaning in', 'vibe2-a': 'Sitting on the stoop, upright', 'vibe6-b': 'Bodega doorway, neon',
       'vibe8-a': 'Leaning on the yellow cab', 'vibe9-b': 'Over the fire-escape rail', 'vibe7-a': 'Snowy court through the fence',
       'vibe4-b': 'Boombox at the graffiti door'}
CLAMP = 'scale=in_range=full:out_range=limited,format=yuv420p,lutyuv=y=clip(val\\,20\\,235)'
ENC = ['-c:v', 'libx264', '-preset', 'veryfast', '-crf', '18', '-pix_fmt', 'yuv420p', '-color_range', 'tv',
       '-colorspace', 'bt709', '-color_primaries', 'bt709', '-color_trc', 'bt709']


def ff(*a):
    subprocess.run(['ffmpeg', '-nostdin', '-loglevel', 'error', '-y', *map(str, a)], check=True)


def clip_for(loc, take):
    m = sorted(VID.glob(f'ec-r8-{loc}-{take}-*.mp4'))
    if not m:
        raise SystemExit(f'no clip for {loc} take {take}')
    return m[0].name


def main():
    ap = argparse.ArgumentParser(); ap.add_argument('--round', type=int, default=2); ap.add_argument('--picks')
    a = ap.parse_args()
    picks = json.loads(pathlib.Path(a.picks).read_text()) if a.picks else {}
    cut = MEDIA / 'cut' / f'r{a.round}'; cut.mkdir(parents=True, exist_ok=True)
    rows, parts = [], []
    for i, (key, title, loc, take, clip, tin, b, hear) in enumerate(SHOTS):
        st = 0.0 if b is None else bar(b)
        en = bar(SHOTS[i + 1][6]) if i + 1 < len(SHOTS) else bar(LOGO_BAR)
        if loc:
            take = picks.get(loc, take); clip = clip_for(loc, take)
        d = round(en - st, 3); raw = cut / f'raw{i:02d}-{key}.mp4'; out = cut / f'v{i:02d}-{key}.mp4'
        ff('-ss', tin, '-i', VID / clip, '-t', d, '-vf', f'scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},fps={FPS}',
           '-an', '-c:v', 'libx264', '-crf', '14', '-preset', 'veryfast', raw)
        subprocess.run([str(FINISH), 'nightfever', str(raw), str(out)], check=True); raw.unlink()
        ff('-i', out, '-vf', CLAMP, *ENC, cut / f'c{i:02d}.mp4'); (cut / f'c{i:02d}.mp4').replace(out)
        parts.append(out)
        rows.append((key, title, clip, tin, st, d, SEE.get(loc, 'The Empire State skyline at dusk (round-2 pick)'), hear))
    ls = bar(LOGO_BAR); ld = round(TOTAL - ls, 3)
    ff('-f', 'lavfi', '-i', f'color=black:s={W}x{H}:r={FPS}:d={ld}', '-loop', '1', '-i', LOGO, '-filter_complex',
       f"[1]scale={int(W * 0.62)}:-1,format=rgba,fade=t=in:st=0.1:d=0.5:alpha=1[l];[0][l]overlay=(W-w)/2:(H-h)/2:shortest=1,{CLAMP}",
       '-t', ld, *ENC, cut / 'v99-logo.mp4')
    parts.append(cut / 'v99-logo.mp4')
    (cut / 'list.txt').write_text(''.join(f"file '{p.name}'\n" for p in parts))
    ff('-f', 'concat', '-safe', '0', '-i', cut / 'list.txt', '-c', 'copy', cut / 'picture.mp4')
    ff('-i', SONG, '-af', f'aresample=48000,aformat=channel_layouts=stereo,atrim=end={TOTAL},afade=t=out:st={TOTAL - 1.5}:d=1.5,loudnorm=I=-14:TP=-1.5',
       '-ar', 48000, '-ac', 2, cut / 'mus-rap.wav')
    ff('-i', cut / 'picture.mp4', '-i', cut / 'mus-rap.wav', '-map', '0:v', '-map', '1:a', '-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k',
       '-t', TOTAL, cut / 'preview.mp4')
    beats = [{'id': r[0], 'title': r[1], 'start': r[4], 'dur': r[5], 'see': r[6],
              'lines': [{'i': 0, 'who': 'rap', 'name': 'The rap', 't': r[4], 'dur': r[5], 'text': r[7], 'by': 'jack'}]} for r in rows]
    beats.append({'id': 'logo', 'title': '15. Logo', 'start': ls, 'dur': ld, 'see': 'The BadCode logo on black, the beat playing out', 'lines': []})
    edl = {'sequence': f'short-ten-economic-commandments-1-tec-r{a.round}', 'title': 'Ten Commandments Timeline',
           'heading': f'BadCode Shorts ▲ Ten Economic Commandments, rough cut {a.round}',
           'intro': 'All ten rules, BadCode rapping on location, one place per rule, cut on the bar, nightfever on. Note anything.',
           'fps': FPS, 'total': TOTAL, 'beats': beats,
           'video': [{'file': str(VID / r[2]), 'in': r[3], 'start': r[4], 'dur': r[5], 'beat': r[0], 'source': str(VID / r[2]),
                      'looped': False} for r in rows] +
                    [{'file': str(cut / 'v99-logo.mp4'), 'in': 0, 'start': ls, 'dur': ld, 'beat': 'logo', 'source': 'logo card', 'looped': False}],
           'audio': [{'track': 'A1', 'name': 'mus-rap', 'file': str(cut / 'mus-rap.wav')}],
           'events': [{'stem': 'mus-rap', 't': 0, 'dur': TOTAL, 'what': "Jack's pick, Suno e689e000 (all ten rules)", 'src': str(SONG)}],
           'flags': ['Takes are my default (a for the rules) until the round-5 picks are read.',
                     'Rules two to four: Whisper missed the number words, so their cuts are placed from the line starts.',
                     'Bodega: Flow lit the neon as LOTTO / ATM.']}
    (cut / 'edl.json').write_text(json.dumps(edl, indent=1, ensure_ascii=False))
    print(json.dumps({'total': TOTAL, 'preview': str(cut / 'preview.mp4')}))


if __name__ == '__main__':
    main()
