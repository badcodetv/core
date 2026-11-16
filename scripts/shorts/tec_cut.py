#!/usr/bin/env python3
"""Ten Economic Commandments (BadCode Short #84): rough cut to the rap (2026-11-16).

    python3 scripts/shorts/tec_cut.py [--round N]

The track is Jack's pick, Suno e4cb9be5 (jazz1, 29.0 s, recorded). Whisper sections: intro 0-5, rule one 5-10, rule two
10-15, rule three 15-21, the fix 21-24, beat out to 29. Picture: Jack's seven round-4 stills animated in Omni (clips
ec-NN-tK), cut on the sections; the clips' own sound is dropped. Then the BadCode logo on black for the tail.
Clip 06 (fence bench): the head turns side-on late in both takes, so it is used from its start only.
Writes <media>/cut/r<N>/edl.json (timeline format, scripts/scene/timeline.py), picture.mp4, mix.wav and preview.mp4.
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
SONG = MEDIA / 'audio/tec-r2-jazz-phrasing-v6-w30-e4cb9be5.wav'
LOGO = REPO / 'docs/brand/logo/badcode-stacked-reversed-2400.png'
W, H, FPS = 1080, 1920, 24
TOTAL = 29.0
# (beat, title, clip, in, start, end, what we see, what is heard)
SHOTS = [
    ('intro', '1. Intro', 'ec-01-t1-RU4-1-b.mp4', 0.3, 0.0, 5.0, 'Doorstep, the chalkboard: THE 10 MONEY COMMANDMENTS', '"Money printer manual. Take notes."'),
    ('one', '2. Number one', 'ec-03-t1-SU4-1-a.mp4', 0.5, 5.0, 10.0, 'Subway platform, fanning fresh banknotes', '"Never tell \'em what you printed…"'),
    ('two-a', '3. Number two', 'ec-04-t1-RU4-2-a.mp4', 0.4, 10.0, 12.6, 'Red studio, fisheye, two fingers up', '"Never get high on your own supply…"'),
    ('two-b', '4. The rent', 'ec-05-t1-SU4-3-b.mp4', 0.5, 12.6, 15.0, 'Bridge street, notes falling behind him', '"…banks took the first hit, now the rent\'s sky-high."'),
    ('three-a', '5. Number three', 'ec-06-t2-RU4-3-a.mp4', 0.2, 15.0, 18.0, 'The fence bench with two locals', '"No consignment, cash up front, that\'s law…"'),
    ('three-b', '6. The bailout', 'ec-02-t1-RU4-5-b.mp4', 0.5, 18.0, 21.0, 'Dusk crowd, the mic pushed at the lens', '"…they took the bailout on tick and they ain\'t paid at all."'),
    ('fix', '7. The fix', 'ec-07-t1-FX4-1-b.mp4', 0.3, 21.0, 25.5, 'Night, streetlight, empty gloved hands raised', '"And the fix, from the future? No hand on the printer."'),
]
LOGO_START = 25.5
CLAMP = 'scale=in_range=full:out_range=limited,format=yuv420p,lutyuv=y=clip(val\\,20\\,235)'
ENC = ['-c:v', 'libx264', '-preset', 'veryfast', '-crf', '18', '-pix_fmt', 'yuv420p', '-color_range', 'tv',
       '-colorspace', 'bt709', '-color_primaries', 'bt709', '-color_trc', 'bt709']


def ff(*a):
    subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', *map(str, a)], check=True)


def main():
    ap = argparse.ArgumentParser(); ap.add_argument('--round', type=int, default=1); a = ap.parse_args()
    cut = MEDIA / 'cut' / f'r{a.round}'; cut.mkdir(parents=True, exist_ok=True)
    parts = []
    for i, (key, title, clip, tin, st, en, see, hear) in enumerate(SHOTS):
        d = round(en - st, 3); out = cut / f'v{i}-{key}.mp4'
        ff('-ss', tin, '-i', VID / clip, '-t', d, '-vf', f'scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},fps={FPS},{CLAMP}',
           '-an', *ENC, out)
        parts.append(out)
    ld = round(TOTAL - LOGO_START, 3)
    ff('-f', 'lavfi', '-i', f'color=black:s={W}x{H}:r={FPS}:d={ld}', '-loop', '1', '-i', LOGO, '-filter_complex',
       f"[1]scale={int(W * 0.62)}:-1,format=rgba,fade=t=in:st=0.1:d=0.5:alpha=1[l];[0][l]overlay=(W-w)/2:(H-h)/2:shortest=1,{CLAMP}",
       '-t', ld, *ENC, cut / 'v9-logo.mp4')
    parts.append(cut / 'v9-logo.mp4')
    (cut / 'list.txt').write_text(''.join(f"file '{p.name}'\n" for p in parts))
    ff('-f', 'concat', '-safe', '0', '-i', cut / 'list.txt', '-c', 'copy', cut / 'picture.mp4')
    ff('-i', SONG, '-af', f'aresample=48000,aformat=channel_layouts=stereo,atrim=end={TOTAL},afade=t=out:st={TOTAL - 1.0}:d=1.0,loudnorm=I=-14:TP=-1.5',
       '-ar', 48000, '-ac', 2, cut / 'mus-rap.wav')
    ff('-i', cut / 'picture.mp4', '-i', cut / 'mus-rap.wav', '-map', '0:v', '-map', '1:a', '-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k',
       '-t', TOTAL, cut / 'preview.mp4')
    beats = [{'id': s[0], 'title': s[1], 'start': s[4], 'dur': round(s[5] - s[4], 3), 'see': s[6],
              'lines': [{'i': 0, 'who': 'rap', 'name': 'The rap', 't': s[4], 'dur': round(s[5] - s[4], 3), 'text': s[7], 'by': 'kai'}]}
             for s in SHOTS]
    beats.append({'id': 'logo', 'title': '8. Logo', 'start': LOGO_START, 'dur': ld, 'see': 'The BadCode logo on black, the beat playing out', 'lines': []})
    edl = {'sequence': f'short-ten-economic-commandments-1-tec-r{a.round}', 'title': 'Ten Commandments Timeline',
           'heading': f'BadCode Shorts ▲ Ten Economic Commandments, rough cut {a.round}',
           'intro': 'Your rap (jazz1) with your seven stills animated, cut on the rules, then the logo. Note anything.',
           'fps': FPS, 'total': TOTAL, 'beats': beats,
           'video': [{'file': str(VID / s[2]), 'in': s[3], 'start': s[4], 'dur': round(s[5] - s[4], 3), 'beat': s[0], 'source': str(VID / s[2]),
                      'looped': False} for s in SHOTS] +
                    [{'file': str(cut / 'v9-logo.mp4'), 'in': 0, 'start': LOGO_START, 'dur': ld, 'beat': 'logo', 'source': 'logo card', 'looped': False}],
           'audio': [{'track': 'A1', 'name': 'mus-rap', 'file': str(cut / 'mus-rap.wav')}],
           'events': [{'stem': 'mus-rap', 't': 0, 'dur': TOTAL, 'what': "Jack's pick jazz1, Suno e4cb9be5 (the rap)", 'src': str(SONG)}],
           'flags': ['Clip 06 used from its start: the head turns side-on later.', 'Take 1 of each clip unless noted; take 2 of each is in the video folder.',
                     'RU4-3-a (fence bench): check the phone booth for a fast-food sign.']}
    (cut / 'edl.json').write_text(json.dumps(edl, indent=1, ensure_ascii=False))
    print(json.dumps({'total': TOTAL, 'preview': str(cut / 'preview.mp4')}))


if __name__ == '__main__':
    main()
