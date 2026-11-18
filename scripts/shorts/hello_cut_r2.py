#!/usr/bin/env python3
"""Hello, I'm BadCode (BadCode Short #17): rough cut 2 (2026-11-18), Jack's round-2 picks on the picks page
(https://claude.ai/artifact/NcX2aNGxH65LjjMdXs2oxa, scenes/hello/picks.md).

    python3 scripts/shorts/hello_cut_r2.py

- Opening: three of Jack's picks as a quick montage: the skatepark at sunset (HO1-d), fireworks over a harbour (HO2-c),
  the neon arcade (HO2-e) ("g and i as well").
- BadCode: the launderette (FG3-b), on the cut, and again after the reel (the slot for Jack's after-the-reel line, held
  silent until the words are written: "we will know what to say once we have the video").
- The horror reel: rough cut 1's, unchanged (real footage, credited, plus Flow stills for the gaps; paced for the
  photosensitivity gate).
- Music: the folktronica take Jack picked (Suno 60a00ad7), from 0, faded out as the reel slows; black and the logo after.
- No voice yet. Stills only, each with a slow push: nothing is animated until the cut is agreed.
Writes <media>/cut/r2/ (rough cut 1's cut/_scratch is imported in Premiere and is never overwritten).
"""
# style-lint: story=short-hello-im-badcode (this cut script belongs to one short)
import json, pathlib, subprocess, sys

sys.path.insert(0, str(pathlib.Path(__file__).parent))
import hello_cut as r1  # noqa: E402  (the reel, push(), seg(), ff())

MEDIA, MB, W, H, FPS = r1.MEDIA, r1.MB, r1.W, r1.H, r1.FPS
CUT = MEDIA / 'cut' / 'r2'; CUT.mkdir(parents=True, exist_ok=True)
WORK = CUT / '_scratch'; WORK.mkdir(exist_ok=True)
MUSIC = MEDIA / 'audio/r2-track/hello-badcode-r2-track-folktronica-laptop-glitch-60a00ad7.wav'
OPENING = [(MB / 'HO1-d.jpg', 1.4, 'skatepark at sunset'), (MB / 'HO2-c.jpg', 1.3, 'fireworks over a harbour'), (MB / 'HO2-e.jpg', 1.3, 'the neon arcade')]
FIG, FIG_D = MB / 'FG3-b.jpg', 2.9
BACK_D = 2.4            # the cut back to BadCode after the reel: Jack's line goes here once the words are written
BLACK_D, LOGO_D = r1.BLACK_D, r1.LOGO_D

# Rough cut 2b (Jack, 2026-11-18: "do the real versus flow by doing a cut 2b"): the same cut with the three openings as REAL
# 2000s footage from research/footage-00s-shortlist.md (credits owed in the description; audio stripped). Run with --real.
FOOT = MEDIA / 'footage/00s'
# 06 at 209.5 s (the shortlist's pick) is a private man's face filling the frame, and 09 is a smeared daytime 640 px photo,
# not the sunset silhouette the shortlist describes. 06 at 60 s puts the rider's face big in the vertical crop. 06 at 229.5 s: the bowl at dusk, empty, streetlights on.
REAL = [(FOOT / '06-skate-marseille-bowl-vespa-2011.webm', 1.4, 'real: the Prado graffiti bowl at dusk, Marseille, 2011 (JC Pieri, CC BY 3.0)', 229.5),
        (FOOT / '05-fw-darling-harbour-2011-portrait.jpg', 1.3, 'real: fireworks over Darling Harbour, Sydney, 2011 (CC BY 2.0, credit per shortlist)', None),
        (FOOT / '10-arcade-southend-monte-carlo-neon-2009_PREVIEW960.jpg', 1.3, 'real: Monte Carlo arcade, Southend, 2009 (Dan Davison, CC BY 2.0)', None)]
if '--real' in sys.argv:
    OPENING = REAL
    CUT = MEDIA / 'cut' / 'r2b'; CUT.mkdir(parents=True, exist_ok=True)
    WORK = CUT / '_scratch'; WORK.mkdir(exist_ok=True)


def clip(src, tin, out, d):
    # Real footage: the audio is stripped (-an), no grade, cropped to fill the vertical frame.
    r1.ff('-ss', tin, '-t', d + 0.1, '-i', src, '-an', '-vf', f'{r1.FILL},fps={FPS},format=yuv420p', '-t', d, *r1.ENC, out)


def main():
    parts, rows, t = [], [], 0.0

    def add(path, d, beat, src, see):
        nonlocal t
        parts.append(path); rows.append({'file': str(path), 'in': 0, 'start': round(t, 3), 'dur': round(d, 3), 'beat': beat, 'source': str(src), 'looped': False, 'see': see}); t += d

    for i, (src, d, see, *tin) in enumerate(OPENING):
        out = WORK / f'p0{i}-open.mp4'
        if tin and tin[0] is not None:
            clip(src, tin[0], out, d)
        else:
            r1.push(src, out, d, 1.0, 1.07, grade=False)
        add(out, d, 'hello', src, see)
    out = WORK / 'p10-fig.mp4'; r1.push(FIG, out, FIG_D, 1.03, 1.10, grade=False); add(out, FIG_D, 'figure', FIG, 'BadCode in the launderette')
    reel_start = t
    for i, (key, kind, src, tin, credit) in enumerate(r1.SHOTS):
        last = i >= len(r1.SHOTS) - 3
        d = r1.REEL + (r1.SLOW / 3 if last else 0)
        out = WORK / f'p{i + 20:02d}-{key}.mp4'
        if kind == 'v':
            r1.seg(src, tin, out, d, speed=0.5 if last else 1.0)
        else:
            r1.push(src, out, d, 1.0, 1.10)
        add(out, d, 'horror', src, 'AI-made (Flow) still' if kind == 'f' else f'real footage, {credit}')
    reel_end = t
    out = WORK / 'p80-back.mp4'; r1.push(FIG, out, BACK_D, 1.12, 1.22, grade=False); add(out, BACK_D, 'back', FIG, 'back to BadCode, closer (slot for Jack\'s line)')
    r1.ff('-f', 'lavfi', '-i', f'color=c=black:s={W}x{H}:r={FPS}:d={BLACK_D}', *r1.ENC, WORK / 'p90-black.mp4'); add(WORK / 'p90-black.mp4', BLACK_D, 'button', 'black', 'black (slot for the last line)')
    r1.ff('-f', 'lavfi', '-i', f'color=c=black:s={W}x{H}:r={FPS}:d={LOGO_D}', '-loop', 1, '-t', LOGO_D, '-i', r1.LOGO, '-filter_complex',
          '[1]scale=640:-1[l];[0][l]overlay=(W-w)/2:(H-h)/2,fade=t=in:d=0.4,format=yuv420p', *r1.ENC, '-t', LOGO_D, WORK / 'p91-logo.mp4')
    add(WORK / 'p91-logo.mp4', LOGO_D, 'button', r1.LOGO, 'the BadCode logo')
    TOTAL = round(t, 3)
    (WORK / 'list.txt').write_text(''.join(f"file '{p.name}'\n" for p in parts))
    r1.ff('-f', 'concat', '-safe', '0', '-i', WORK / 'list.txt', '-c', 'copy', CUT / 'picture.mp4')
    mdur = float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', MUSIC], capture_output=True, text=True).stdout)
    fade_at = max(0.0, min(mdur, reel_end) - 1.5)
    mus = CUT / 'mus-track.wav'
    r1.ff('-i', MUSIC, '-af', f'loudnorm=I=-15:TP=-2,afade=t=out:st={fade_at:.2f}:d=1.5,apad=whole_dur={TOTAL},atrim=end={TOTAL}', '-ar', 48000, '-ac', 2, mus)
    r1.ff('-i', CUT / 'picture.mp4', '-i', mus, '-map', '0:v', '-map', '1:a', '-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k', '-t', TOTAL, CUT / 'preview.mp4')
    beat = lambda b: [r for r in rows if r['beat'] == b]
    span = lambda b: (beat(b)[0]['start'], round(sum(r['dur'] for r in beat(b)), 3))
    beats = [{'id': 'hello', 'title': 'A. The warm opening', 'start': span('hello')[0], 'dur': span('hello')[1], 'see': 'Skatepark at sunset, fireworks over a harbour, the neon arcade. No words yet.', 'lines': []},
             {'id': 'figure', 'title': 'B. BadCode', 'start': span('figure')[0], 'dur': span('figure')[1], 'see': 'BadCode in a launderette at night. No words yet.', 'lines': []},
             {'id': 'horror', 'title': 'C. The horror reel', 'start': span('horror')[0], 'dur': span('horror')[1], 'see': f'{len(r1.SHOTS)} flashes: real footage (credited) and Flow stills for the gaps; slows into silence.', 'lines': []},
             {'id': 'back', 'title': 'D. Back to BadCode', 'start': span('back')[0], 'dur': span('back')[1], 'see': "Closer on BadCode: the slot for Jack's line (\"What do you think in your mind, what the worst-case scenario is?…\").", 'lines': []},
             {'id': 'button', 'title': 'E. Black, then the logo', 'start': span('button')[0], 'dur': span('button')[1], 'see': 'Black (the last line goes here), then the BadCode logo.', 'lines': []}]
    credits = sorted({r['see'].split('real footage, ')[1] for r in rows if 'real footage, ' in r['see']})
    real = OPENING is REAL
    edl = {'sequence': 'short-hello-im-badcode-1-hello-r2' + ('b' if real else ''), 'title': 'Hello Im BadCode Timeline', 'heading': "BadCode Shorts ▲ Hello, I'm BadCode, rough cut 2" + ('b (real 2000s footage in the opening)' if real else ''),
           'intro': ("Your round-2 picks on the timeline: the three openings (skatepark, fireworks, arcade), BadCode in the launderette, the "
                     "real-footage horror reel, back to BadCode, black, the logo, to the folktronica track. Stills with a slow push for now: "
                     "nothing animated until the cut works. No words yet. Note anything."),
           'fps': FPS, 'total': TOTAL, 'beats': beats, 'video': [{k: v for k, v in r.items() if k != 'see'} | {'note': r['see']} for r in rows],
           'audio': [{'track': 'A1', 'name': 'mus-track', 'file': str(mus)}],
           'events': [{'stem': 'mus-track', 't': 0, 'dur': round(min(mdur, TOTAL), 3), 'what': 'Suno folktronica take 1 (Jack\'s pick), faded as the reel slows', 'src': str(MUSIC)}],
           'flags': [f'The track is {mdur:.1f} s; it fades out at {fade_at:.1f} s as the reel slows, so the cut back to BadCode, the black and the logo play in silence.',
                     'Stills only (a slow push on each): animation comes once the cut is agreed.',
                     'No voice: the words wait for the picture (Jack).',
                     'Footage credits owed in the description: ' + '; '.join(credits) + '.']}
    (CUT / 'edl.json').write_text(json.dumps(edl, indent=1, ensure_ascii=False))
    print(json.dumps({'total': TOTAL, 'reel': [round(reel_start, 2), round(reel_end, 2)], 'music': round(mdur, 1), 'preview': str(CUT / 'preview.mp4')}))


if __name__ == '__main__':
    main()
