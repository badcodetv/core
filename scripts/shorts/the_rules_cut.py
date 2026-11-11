#!/usr/bin/env python3
"""The Rules (BadCode Short): rough cut 2, Flow clips cut on the sung words, the hymn and the drop (sound: docs/stories/short-the-rules/sound.md).

    python3 scripts/shorts/the_rules_cut.py [--drop-in 0.0]

Round 2 (Kai's timeline r1 notes, 2026-11-11): cut on the words (stack 0-3.2, bed 3.2-6.1, purse 6.1-7.9,
islands 7.9-11, bin 11-16.6), the gang go mental from 16.6 (riot, then the climb), end on the pen held out to camera.
Each shot is a Flow clip trimmed from its start to the slot, scaled 720x1280 -> 1080x1920. A1 = the hymn from 0 s;
A2 = the Amen drop, hard in at the tear, cut dead for the pen. Writes <media>/cut/edl.json (timeline format,
scripts/scene/timeline.py), the stems and preview.mp4.
"""
import json, pathlib, subprocess, sys

REPO = pathlib.Path(__file__).resolve().parents[2]
SCENE = REPO / 'docs/stories/short-the-rules/scenes/the-rules'
sys.path.insert(0, str(REPO / 'scripts/drive'))
from localmap import localize  # noqa: E402

cfg = localize(json.loads((SCENE / 'scene.json').read_text()))
MEDIA = pathlib.Path(cfg['media'])
CUT = MEDIA / 'cut'; CUT.mkdir(parents=True, exist_ok=True)
CLIPS = MEDIA / 'video'
HYMN = MEDIA / 'music/4f37afd8-16ec-4b66-9885-54030500a37e-4f37afd8.wav'   # 16.52 s
DROP = MEDIA / 'music/5b008987-305c-4634-8436-9c2aa726c891-5b008987.wav'   # 47.04 s
DROP_IN = float(sys.argv[sys.argv.index('--drop-in') + 1]) if '--drop-in' in sys.argv else 0.0  # where in the drop file to start
ROUND = 2

W, H, FPS = 1080, 1920, 24
# (beat, clip file, start, dur): Kai's word timings
SHOTS = [('stack', 'tr-r01-ST3-a-a.mp4', 0.0, 3.2),
         ('bed', 'tr-b1-BD5-a-a.mp4', 3.2, 2.9),
         ('purse', 'tr-b2-PU5-a-b.mp4', 6.1, 1.8),
         ('islands', 'tr-02-IS4-a-b.mp4', 7.9, 3.1),
         ('bin', 'tr-b3-BI5-a-a.mp4', 11.0, 5.6),
         ('riot', 'tr-r04a-TE4-a-a.mp4', 16.6, 6.0),
         ('climb', 'tr-c1-CL3-c-a.mp4', 22.6, 6.0),
         ('pen', 'tr-05-PE4-b-a.mp4', 28.6, 4.0)]
TOTAL = SHOTS[-1][2] + SHOTS[-1][3]
DROP_START = 16.6
DROP_DUR = SHOTS[-1][2] - DROP_START          # cut dead for the pen
LINES = [('bed', 3.2, 2.9, "We can't afford a bed for you,"), ('purse', 6.1, 1.8, 'The purse is far too thin;'),
         ('islands', 7.9, 3.1, 'There is room on all those islands,'), ('bin', 11.0, 5.6, 'But you will sleep in a bin.')]
SEE = {'stack': 'The gang face camera at the foot of THE RULES; a tube flickers. Piano intro.',
       'bed': 'Night, a high street: people asleep in the bank doorway; one pulls the sleeping bag closer.',
       'purse': 'Old hands at a till open a purse: a few coppers. Shut again.',
       'islands': 'A filing cabinet asleep in a hammock under a palm. Overlay (owed): the tax line.',
       'bin': 'Rain in an alley: someone asleep on cardboard beside the big green bins.',
       'riot': 'The gang go mental: tearing the rules chest-on to camera, paper thrown up. The Amen drop slams in (A2).',
       'climb': 'They climb the shelving and tear the archive apart; paper pours down.',
       'pen': 'A blank page and a pen held out to camera. The drop cuts dead: silence.'}


def ff(*a):
    subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', *map(str, a)], check=True)


def main():
    parts = []
    for i, (beat, clip, t, d) in enumerate(SHOTS):
        out = CUT / f'r{ROUND}-v{i}-{beat}.mp4'
        ff('-i', CLIPS / clip, '-t', d, '-an', '-vf',
           f'scale={W}:{H}:force_original_aspect_ratio=increase:flags=lanczos,crop={W}:{H},fps={FPS},format=yuv420p',
           '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '18', '-color_range', 'tv', '-colorspace', 'bt709',
           '-color_primaries', 'bt709', '-color_trc', 'bt709', out)
        parts.append(out)
    (CUT / 'list.txt').write_text(''.join(f"file '{p.name}'\n" for p in parts))
    ff('-f', 'concat', '-safe', '0', '-i', CUT / 'list.txt', '-c', 'copy', CUT / 'picture.mp4')
    hymn = CUT / 'mus-hymn.wav'; drop = CUT / 'mus-drop.wav'
    ff('-i', HYMN, '-af', f'apad,atrim=0:{TOTAL}', '-ar', 48000, '-ac', 2, hymn)
    ff('-ss', DROP_IN, '-t', DROP_DUR, '-i', DROP, '-af',
       f'adelay={int(DROP_START * 1000)}|{int(DROP_START * 1000)},apad,atrim=0:{TOTAL}', '-ar', 48000, '-ac', 2, drop)
    ff('-i', CUT / 'picture.mp4', '-i', hymn, '-i', drop, '-filter_complex', '[1:a][2:a]amix=inputs=2:normalize=0[a]',
       '-map', '0:v', '-map', '[a]', '-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k', '-t', TOTAL, CUT / 'preview.mp4')
    beats = []
    for i, (beat, clip, t, d) in enumerate(SHOTS):
        beats.append({'id': str(i), 'title': beat.title(), 'start': t, 'dur': d, 'see': SEE[beat],
                      'lines': [{'i': k, 'who': 'school', 'name': 'The whole school', 't': lt, 'dur': ld, 'text': tx, 'by': 'kai'}
                                for k, (b, lt, ld, tx) in enumerate(LINES) if b == beat]})
    edl = {'sequence': f'short-the-rules-1-rules-r{ROUND}', 'title': 'The Rules Timeline',
           'heading': f'The Rules — rough cut {ROUND} (clips on the words, riot, climb, pen)',
           'intro': 'Rough cut 2: your notes from round 1. Every shot is now a moving clip, cut on the sung words; the gang go '
                    'mental from 16.6 s (the riot, then the new climb) and it ends on the pen. Hymn on A1, Amen drop on A2. '
                    'Play it, click any shot or sound, leave notes.',
           'fps': FPS, 'total': TOTAL, 'beats': beats,
           'video': [{'file': str(p), 'start': t, 'dur': d, 'beat': str(i), 'source': str(CLIPS / clip)}
                     for i, (p, (beat, clip, t, d)) in enumerate(zip(parts, SHOTS))],
           'audio': [{'track': 'A1', 'name': 'mus-hymn'}, {'track': 'A2', 'name': 'mus-drop'}],
           'events': [{'stem': 'mus-hymn', 't': 0.0, 'dur': 16.52, 'what': 'The hymn (whole school + upright piano)', 'src': str(HYMN)},
                      {'stem': 'mus-drop', 't': DROP_START, 'dur': DROP_DUR, 'what': f'Amen drop from {DROP_IN:.1f} s of the take, cut dead at the pen', 'src': str(DROP)}],
           'flags': [f'The drop plays from {DROP_IN:.1f} s of the 47 s take: Kai finds the real drop point in Premiere.',
                     'Line times are Kai\'s word timings from round 1.',
                     'Riot clip: the rust mask\'s triangle is faint in places.',
                     'No text overlay yet: the tax line is owed a fact check.']}
    (CUT / 'edl.json').write_text(json.dumps(edl, indent=1))
    print(json.dumps({'total': TOTAL, 'preview': str(CUT / 'preview.mp4')}))


main()
