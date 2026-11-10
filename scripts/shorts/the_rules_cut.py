#!/usr/bin/env python3
"""The Rules (BadCode Short): rough cut 1 from the picked stills, the hymn and the drum and bass drop.

    python3 scripts/shorts/the_rules_cut.py [--drop-in 0.0]

Stills only (no clips yet), 9:16, held still. A1 = the hymn from 0 s; A2 = the Amen drop, hard cut in at the tear
and cut dead for the pen. Writes <media>/cut/edl.json (timeline format, scripts/scene/timeline.py), the stems and
preview.mp4. Line times inside the hymn are ESTIMATES (nobody has listened): Kai nudges them on the timeline page.
"""
import json, pathlib, subprocess, sys

REPO = pathlib.Path(__file__).resolve().parents[2]
SCENE = REPO / 'docs/stories/short-the-rules/scenes/the-rules'
sys.path.insert(0, str(REPO / 'scripts/drive'))
from localmap import localize  # noqa: E402

cfg = localize(json.loads((SCENE / 'scene.json').read_text()))
MEDIA = pathlib.Path(cfg['media'])
CUT = MEDIA / 'cut'; CUT.mkdir(parents=True, exist_ok=True)
HYMN = MEDIA / 'music/4f37afd8-16ec-4b66-9885-54030500a37e-4f37afd8.wav'   # 16.52 s
DROP = MEDIA / 'music/5b008987-305c-4634-8436-9c2aa726c891-5b008987.wav'   # 47.04 s
DROP_IN = float(sys.argv[sys.argv.index('--drop-in') + 1]) if '--drop-in' in sys.argv else 0.0  # where in the drop file to start

W, H, FPS = 1080, 1920, 24
HYMN_END = 16.5
# (beat, still, start, dur)
SHOTS = [('stack', 'ST3-a-a', 0.0, 11.0), ('islands', 'IS4-a-b', 11.0, 2.5), ('window', 'WI4-b-a', 13.5, 3.0),
         ('tear', 'TE4-a-a', HYMN_END, 7.5), ('pen', 'PE4-b-a', HYMN_END + 7.5, 3.0)]
TOTAL = SHOTS[-1][2] + SHOTS[-1][3]
DROP_START, DROP_DUR = HYMN_END, 7.5
LINES = [('stack', 6.0, 2.5, "We can't afford a bed for you,"), ('stack', 8.5, 2.5, 'The purse is far too thin;'),
         ('islands', 11.0, 2.5, 'There is room on all those islands,'), ('window', 13.5, 3.0, 'But you will sleep in a bin.')]
SEE = {'stack': 'The gang look up at THE RULES. Piano intro, then the first two lines.',
       'islands': 'A filing cabinet asleep in a hammock under a palm. Overlay (owed): the tax line.',
       'window': 'Out of the barred pavement-level window: people asleep in shop doorways. The chord dies.',
       'tear': 'The gang rip up the rules. The Amen drop slams in (A2).',
       'pen': 'A blank page and a pen held out to camera. The drop cuts dead: silence.'}


def ff(*a):
    subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', *map(str, a)], check=True)


def main():
    parts = []
    for i, (beat, sid, t, d) in enumerate(SHOTS):
        out = CUT / f'v{i}-{sid}.mp4'
        ff('-loop', '1', '-t', d, '-i', MEDIA / 'moodboard' / f'{sid}.jpg', '-vf',
           f'scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},fps={FPS},scale=in_range=full:out_range=limited,format=yuv420p',
           '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '18', '-color_range', 'tv', '-colorspace', 'bt709', '-color_primaries', 'bt709', '-color_trc', 'bt709', out)
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
    for i, (beat, sid, t, d) in enumerate(SHOTS):
        beats.append({'id': str(i), 'title': beat.title(), 'start': t, 'dur': d, 'see': SEE[beat],
                      'lines': [{'i': k, 'who': 'school', 'name': 'The whole school', 't': lt, 'dur': ld, 'text': tx, 'by': 'kai'}
                                for k, (b, lt, ld, tx) in enumerate(LINES) if b == beat]})
    edl = {'sequence': 'short-the-rules-1-rules-r1', 'title': 'The Rules Timeline',
           'heading': 'The Rules — rough cut 1 (stills, hymn, drop)',
           'intro': 'Rough cut 1: the five picked stills held still, the hymn on A1 and the Amen drop on A2, hard cut in at the tear '
                    'and cut dead for the pen. Line times in the hymn are estimates. Play it, click any shot or sound, leave notes.',
           'fps': FPS, 'total': TOTAL, 'beats': beats,
           'video': [{'file': str(p), 'start': t, 'dur': d, 'beat': str(i), 'source': str(MEDIA / 'moodboard' / f'{sid}.jpg')}
                     for i, (p, (beat, sid, t, d)) in enumerate(zip(parts, SHOTS))],
           'audio': [{'track': 'A1', 'name': 'mus-hymn'}, {'track': 'A2', 'name': 'mus-drop'}],
           'events': [{'stem': 'mus-hymn', 't': 0.0, 'dur': 16.52, 'what': 'The hymn (whole school + upright piano)', 'src': str(HYMN)},
                      {'stem': 'mus-drop', 't': DROP_START, 'dur': DROP_DUR, 'what': f'Amen drop from {DROP_IN:.1f} s of the take, cut dead at the pen', 'src': str(DROP)}],
           'flags': ['Stills held still: no clips yet (animating spends Flow video credits).',
                     'Hymn line times are estimates, not measured by listening.',
                     f'The drop plays from {DROP_IN:.1f} s of the 47 s take: Kai to find the real drop point.',
                     'No text overlay yet: the tax line is owed a fact check.']}
    (CUT / 'edl.json').write_text(json.dumps(edl, indent=1))
    print(json.dumps({'total': TOTAL, 'preview': str(CUT / 'preview.mp4')}))


main()
