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
ROUND = 3

W, H, FPS = 1080, 1920, 24
F = 1 / FPS
# (beat, clip file, start, dur): round 3 = Kai's hand edit in Premiere (sequence short-the-rules-1-rules-r2,
# 2026-11-11, dump feedback/premiere-r2-kai/state.json), in frames. Every clip plays from its first frame.
# A .jpg is a still held as a placeholder until its clip exists.
SHOTS = [('stack', 'tr-r01-ST3-a-a.mp4', 0, 64),
         ('bed', 'tr-b1-BD5-a-a.mp4', 64, 41),
         ('purse', 'tr-b2-PU5-a-b.mp4', 105, 74),
         ('islands', 'tr-02-IS4-a-b.mp4', 179, 69),
         ('bin', 'tr-b3-BI5-a-a.mp4', 248, 131),
         ('riot', 'tr-r04a-TE4-a-a.mp4', 379, 65),
         ('climb', 'tr-c1-CL3-c-a.mp4', 444, 72),
         ('hang', '../moodboard/HR2-a-a.jpg', 516, 67),
         ('pen', 'tr-05-PE4-b-a.mp4', 583, 68)]
SHOTS = [(b, c, s * F, d * F) for b, c, s, d in SHOTS]
DROP_START = 379 * F                          # Kai: the drop lands on the riot
DROP_IN = float(sys.argv[sys.argv.index('--drop-in') + 1]) if '--drop-in' in sys.argv else 274 * F  # Kai's drop point, 11.42 s into the take
DROP_DUR = 274 * F                            # to 27.21 s, a frame past the pen
TOTAL = DROP_START + DROP_DUR
LINES = [('bed', 3.2, 2.9, "We can't afford a bed for you,"), ('purse', 6.1, 1.8, 'The purse is far too thin;'),
         ('islands', 7.9, 3.1, 'There is room on all those islands,'), ('bin', 11.0, 5.6, 'But you will sleep in a bin.')]
SEE = {'stack': 'The gang face camera at the foot of THE RULES; a tube flickers. Piano intro.',
       'bed': 'Night, a high street: people asleep in the bank doorway; one pulls the sleeping bag closer.',
       'purse': 'Old hands at a till open a purse: a few coppers. Shut again.',
       'islands': 'A filing cabinet asleep in a hammock under a palm. Overlay (owed): the tax line.',
       'bin': 'Rain in an alley: someone asleep on cardboard beside the big green bins.',
       'riot': 'The gang go mental: tearing the rules chest-on to camera, paper thrown up. The Amen drop slams in (A2).',
       'climb': 'They climb the shelving and tear the archive apart; paper pours down.',
       'hang': 'Two hang off the top shelves while the rest rip paper at the camera. STILL for now (HR2-a-a): its clip is owed.',
       'pen': 'A blank page and a pen held out to camera. The drop plays out under it.'}


def ff(*a):
    subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', *map(str, a)], check=True)


def main():
    parts = []
    for i, (beat, clip, t, d) in enumerate(SHOTS):
        out = CUT / f'r{ROUND}-v{i}-{beat}.mp4'
        src = ['-loop', '1', '-t', d, '-i', CLIPS / clip] if clip.endswith('.jpg') else ['-i', CLIPS / clip]
        rng = ',scale=in_range=full:out_range=limited' if clip.endswith('.jpg') else ''
        ff(*src, '-t', d, '-an', '-vf',
           f'scale={W}:{H}:force_original_aspect_ratio=increase:flags=lanczos,crop={W}:{H},fps={FPS}{rng},format=yuv420p',
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
           'heading': f'The Rules — cut {ROUND} (Kai\'s Premiere edit)',
           'intro': 'Cut 3 is your own edit from Premiere, carried back: tighter (27.2 s), the drop lands on the riot at 15.8 s '
                    'from 11.4 s into the take, and the new hang-and-rip shot fills your gap before the pen (a still for now, '
                    'its clip is next). Play it, click any shot or sound, leave notes.',
           'fps': FPS, 'total': TOTAL, 'beats': beats,
           # Premiere gets the Flow clip itself from its first frame (handles for Kai's trims), not the upscaled copy
           'video': [{'file': str(CLIPS / clip), 'in': 0.0, 'start': t, 'dur': d, 'beat': str(i), 'preview': str(p)}
                     for i, (p, (beat, clip, t, d)) in enumerate(zip(parts, SHOTS))],
           'audio': [{'track': 'A1', 'name': 'mus-hymn', 'file': str(HYMN)},
                     {'track': 'A2', 'name': 'mus-drop', 'file': str(DROP), 'at': DROP_START, 'in': DROP_IN, 'dur': DROP_DUR}],
           'events': [{'stem': 'mus-hymn', 't': 0.0, 'dur': 16.52, 'what': 'The hymn (whole school + upright piano)', 'src': str(HYMN)},
                      {'stem': 'mus-drop', 't': DROP_START, 'dur': DROP_DUR, 'what': f'Amen drop from {DROP_IN:.2f} s of the take (Kai\'s drop point), through the pen', 'src': str(DROP)}],
           'flags': ['Hang-and-rip (21.5-24.3 s) is the still HR2-a-a held until its clip is made and approved.',
                     'Line times are where the words are sung; your cuts now land a little before them.',
                     'Your fades on the hymn and the drop (Premiere transitions) are not in this preview.',
                     'Riot clip: the rust mask\'s triangle is faint in places.',
                     'No text overlay yet: the tax line is owed a fact check.']}
    (CUT / 'edl.json').write_text(json.dumps(edl, indent=1))
    print(json.dumps({'total': TOTAL, 'preview': str(CUT / 'preview.mp4')}))


main()
