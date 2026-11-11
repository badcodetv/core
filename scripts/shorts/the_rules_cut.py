#!/usr/bin/env python3
"""The Rules (BadCode Short): the FINAL cut (round 5 = Premiere r3, frozen 2026-11-11), Flow clips cut on the sung words, the hymn and the drop (sound: docs/stories/short-the-rules/sound.md).

    python3 scripts/shorts/the_rules_cut.py [--drop-in SECONDS]

Round 5 (final): SHOTS, the drop and every fade are Kai's Premiere r3, frame for frame (see SHOTS below).
History:

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
DROP = MEDIA / 'music/rules-r3-concrete-stairwell-distortion-v6-w75-feb1a0c7.wav'   # 60 s, round dnb-r3 pick (Kai 2026-11-11)
ROUND = 5

W, H, FPS = 1080, 1920, 24
F = 1 / FPS
# (beat, clip file, start, dur, in): round 5 = Premiere r3 as Kai froze it ("it's a cut", 2026-11-11; dump
# feedback/premiere-r3-final/state.json + transitions.json), in frames. `in` = the frame of the Flow clip the shot starts on.
# A .jpg is a still held as a placeholder until its clip exists.
SHOTS = [('stack', 'tr-r01-ST3-a-a.mp4', 0, 64, 0),
         ('bed', 'tr-b1-BD5-a-a.mp4', 64, 41, 0),
         ('purse', 'tr-b2-PU5-a-b.mp4', 105, 74, 0),
         ('islands', 'tr-02-IS4-a-b.mp4', 179, 69, 0),
         ('bin', 'tr-b3-BI5-a-a.mp4', 248, 131, 0),
         ('riot', 'tr-r04a-TE4-a-a.mp4', 379, 69, 0),
         ('hang', 'tr-h1-HR7-d-b.mp4', 448, 68, 4),    # Kai moved hang-and-rip before the climb in r3
         ('climb', 'tr-c1-CL3-c-a.mp4', 516, 70, 5),
         ('pen', 'tr-05-PE4-b-a.mp4', 586, 76, 3)]
SHOTS = [(b, c, s * F, d * F, i * F) for b, c, s, d, i in SHOTS]
TOTAL = 662 * F                               # 27.583 s
# Kai's r3 sound: the drop moved to A2, in before the riot, from 22.17 s into the take; the old Amen is gone.
DROP_START = 356 * F                          # 14.833 s, under the end of the bin
DROP_IN = float(sys.argv[sys.argv.index('--drop-in') + 1]) if '--drop-in' in sys.argv else 532 * F
DROP_DUR = TOTAL - DROP_START
HYMN_DUR = 396 * F                            # 16.5 s
# Kai's fades (Premiere transitions, read from the saved .prproj), (from, to) in seconds on the sequence
HYMN_FADE = (345 * F, 396 * F)
DROP_FADE_IN = (356 * F, 386 * F)
DROP_FADE_OUT = (639 * F, 662 * F)
PIC_FADE = (638 * F, 662 * F)                 # cross dissolve to black on the pen
LINES = [('bed', 3.2, 2.9, "We can't afford a bed for you,"), ('purse', 6.1, 1.8, 'The purse is far too thin;'),
         ('islands', 7.9, 3.1, 'There is room on all those islands,'), ('bin', 11.0, 5.6, 'But you will sleep in a bin.')]
SEE = {'stack': 'The gang face camera at the foot of THE RULES; a tube flickers. Piano intro.',
       'bed': 'Night, a high street: people asleep in the bank doorway; one pulls the sleeping bag closer.',
       'purse': 'Old hands at a till open a purse: a few coppers. Shut again.',
       'islands': 'A filing cabinet asleep in a hammock under a palm. Overlay (owed): the tax line.',
       'bin': 'Rain in an alley: someone asleep on cardboard beside the big green bins.',
       'riot': 'The gang go mental: tearing the rules chest-on to camera, paper thrown up. The drop is already up (A2).',
       'climb': 'They climb the shelving and tear the archive apart; paper pours down.',
       'hang': 'Two rip paper right up in the lens while two hang off the top racks and one hauls himself up behind (clip from HR7-d-b).',
       'pen': 'A blank page and a pen held out to camera. The drop plays out under it.'}


def ff(*a):
    subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', *map(str, a)], check=True)


def fade(t, d):
    a, b = PIC_FADE
    return f',fade=t=out:st={a - t:.4f}:d={b - a:.4f}' if t < b and t + d > a else ''


def main():
    parts = []
    for i, (beat, clip, t, d, cin) in enumerate(SHOTS):
        out = CUT / f'r{ROUND}-v{i}-{beat}.mp4'
        src = ['-loop', '1', '-t', d, '-i', CLIPS / clip] if clip.endswith('.jpg') else ['-ss', cin, '-i', CLIPS / clip]
        rng = ',scale=in_range=full:out_range=limited' if clip.endswith('.jpg') else ''
        ff(*src, '-t', d, '-an', '-vf',
           f'scale={W}:{H}:force_original_aspect_ratio=increase:flags=lanczos,crop={W}:{H},fps={FPS}{rng}{fade(t, d)},format=yuv420p',
           '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '18', '-color_range', 'tv', '-colorspace', 'bt709',
           '-color_primaries', 'bt709', '-color_trc', 'bt709', out)
        parts.append(out)
    (CUT / 'list.txt').write_text(''.join(f"file '{p.name}'\n" for p in parts))
    ff('-f', 'concat', '-safe', '0', '-i', CUT / 'list.txt', '-c', 'copy', CUT / 'picture.mp4')
    hymn = CUT / 'mus-hymn.wav'; drop = CUT / 'mus-drop.wav'
    ff('-i', HYMN, '-af', f'atrim=0:{HYMN_DUR},afade=t=out:st={HYMN_FADE[0]}:d={HYMN_FADE[1] - HYMN_FADE[0]},apad,atrim=0:{TOTAL}',
       '-ar', 48000, '-ac', 2, hymn)
    ff('-ss', DROP_IN, '-t', DROP_DUR, '-i', DROP, '-af',
       f'afade=t=in:st=0:d={DROP_FADE_IN[1] - DROP_FADE_IN[0]},'
       f'afade=t=out:st={DROP_FADE_OUT[0] - DROP_START}:d={DROP_FADE_OUT[1] - DROP_FADE_OUT[0]},'
       f'adelay={int(DROP_START * 1000)}|{int(DROP_START * 1000)},apad,atrim=0:{TOTAL}', '-ar', 48000, '-ac', 2, drop)
    ff('-i', CUT / 'picture.mp4', '-i', hymn, '-i', drop, '-filter_complex', '[1:a][2:a]amix=inputs=2:normalize=0[a]',
       '-map', '0:v', '-map', '[a]', '-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k', '-t', TOTAL, CUT / 'preview.mp4')
    beats = []
    for i, (beat, clip, t, d, cin) in enumerate(SHOTS):
        beats.append({'id': str(i), 'title': beat.title(), 'start': t, 'dur': d, 'see': SEE[beat],
                      'lines': [{'i': k, 'who': 'school', 'name': 'The whole school', 't': lt, 'dur': ld, 'text': tx, 'by': 'kai'}
                                for k, (b, lt, ld, tx) in enumerate(LINES) if b == beat]})
    edl = {'sequence': f'short-the-rules-1-rules-r{ROUND}', 'title': 'The Rules Timeline',
           'heading': f'The Rules — cut {ROUND}, FINAL (Premiere r3 as you froze it)',
           'intro': 'Final cut = Premiere r3 exactly as you left it on 2026-11-11 ("it\'s a cut"): your trims, the hymn fading '
                    'out under the bin, the concrete-stairwell drop fading in from 22.2 s into its take, and the pen dissolving '
                    'to black. Frozen; the release master is exported from Premiere itself.',
           'fps': FPS, 'total': TOTAL, 'beats': beats,
           # Premiere gets the Flow clip itself from its first frame (handles for Kai's trims), not the upscaled copy
           'video': [{'file': str(CLIPS / clip), 'in': cin, 'start': t, 'dur': d, 'beat': str(i), 'preview': str(p)}
                     for i, (p, (beat, clip, t, d, cin)) in enumerate(zip(parts, SHOTS))],
           'audio': [{'track': 'A1', 'name': 'mus-hymn', 'file': str(HYMN), 'dur': HYMN_DUR},
                     {'track': 'A2', 'name': 'mus-drop', 'file': str(DROP), 'at': DROP_START, 'in': DROP_IN, 'dur': DROP_DUR}],
           'events': [{'stem': 'mus-hymn', 't': 0.0, 'dur': HYMN_DUR, 'what': 'The hymn (whole school + upright piano), fading out from 14.38 s', 'src': str(HYMN)},
                      {'stem': 'mus-drop', 't': DROP_START, 'dur': DROP_DUR, 'what': f'Concrete-stairwell drop (dnb-r3) from {DROP_IN:.2f} s of the take, fading in over 1.25 s, out with the pen', 'src': str(DROP)}],
           'flags': ['Line times are where the words are sung; your cuts now land a little before them.',
                     'Riot clip: the rust mask\'s triangle is faint in places.',
                     'No text overlay yet: the tax line is owed a fact check.']}
    (CUT / 'edl.json').write_text(json.dumps(edl, indent=1))
    print(json.dumps({'total': TOTAL, 'preview': str(CUT / 'preview.mp4')}))


main()
