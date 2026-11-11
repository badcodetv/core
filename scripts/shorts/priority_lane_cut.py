#!/usr/bin/env python3
"""Priority Lane (BadCode Short): rough cut 1 from the five clips and the two picked voices (2026-11-11).

    python3 scripts/shorts/priority_lane_cut.py

9:16. Picture is timed to the real voice lengths (scene-timeline: 0.4 s lead-in, 0.35 s gap, 0.6 s tail).
A1 = reporter (Enceladus, rep2-e), A2 = minister (Orus, min-b, the lip-synced dub fitted to clip 04 from t=0),
A3 = sfx: each clip's own Omni ambience (no speech in any of them, checked), levelled, and the room bed under 04.
Writes <media>/cut/edl.json (timeline format, scripts/scene/timeline.py), the stems and preview.mp4.
"""
import json, pathlib, subprocess, sys

REPO = pathlib.Path(__file__).resolve().parents[2]
SCENE = REPO / 'docs/stories/shorts/priority-lane'
sys.path.insert(0, str(REPO / 'scripts/drive'))
from localmap import localize  # noqa: E402

cfg = localize(json.loads((SCENE / 'scene.json').read_text()))
MEDIA = pathlib.Path(cfg['media'])
VID, AUD = MEDIA / 'video', MEDIA / 'audio'
CUT = MEDIA / 'cut'; CUT.mkdir(parents=True, exist_ok=True)
REP = AUD / 'casting/rep2-e-enceladus.wav'      # line 1 0.34-5.66 s, line 2 6.38-11.40 s (measured)
MIN_DUB = AUD / 'dub/pl-04-minister-dub.wav'     # placed on clip 04's own clock: voice 0.71-3.46 s
MIN_BED = AUD / 'dub/pl-04-bed.wav'
W, H, FPS = 1080, 1920, 24
LEAD, TAIL = 0.4, 0.6
SFX_LUFS = -30

L1 = (0.30, 5.70)   # reporter line 1 slice (a hair outside the measured speech)
L2 = (6.34, 11.45)  # reporter line 2 slice
MIN_IN, MIN_OUT = 0.35, 4.05                     # clip 04 in/out: mouth speaks 0.67-3.42

# (beat, clip, in, dur)
r1 = LEAD + (L1[1] - L1[0]) + 0.35
r2 = LEAD + (L2[1] - L2[0]) + TAIL + 0.4
SHOTS = [('outside', 'pl-01-OUT1-c.mp4', 0.5, 3.0),
         ('ambulance', 'pl-02-AMB1-a.mp4', 0.5, 2.5),
         ('reporter', 'pl-03-r2-REP1-a.mp4', 0.0, r1),
         ('minister', 'pl-04-MIN1-b.mp4', MIN_IN, MIN_OUT - MIN_IN),
         ('button', 'pl-05-r3-REP1-a.mp4', 1.0, r2)]
starts, t = [], 0.0
for s in SHOTS: starts.append(round(t, 3)); t += s[3]
TOTAL = round(t, 3)
T_REP1 = starts[2] + LEAD
T_MIN = starts[3] - MIN_IN                       # where clip 04's t=0 sits on the timeline
T_REP2 = starts[4] + LEAD
SEE = {'outside': 'The junction: the outrider holds the ambulance at the red light while the motorcade glides through.',
       'ambulance': 'Inside the ambulance: nobody moves, the light stays red.',
       'reporter': 'The BadCode reporter, straight to camera, the motorcade behind him.',
       'minister': 'The minister in the back of the car, furious, on the phone (lip-synced).',
       'button': 'Back to the reporter as the ambulance finally pulls away.'}
TITLES = {'outside': 'The ambulance is held', 'ambulance': 'Inside the ambulance', 'reporter': 'The BadCode reporter',
          'minister': 'The minister', 'button': 'The button'}


def ff(*a):
    subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', *map(str, a)], check=True)


# ffmpeg 6.1: an atrim AFTER adelay drops the delay (the voice lands at 0 s); pad with apad=whole_dur instead.
def ms(x):
    return int(round(x * 1000))


def main():
    parts, sfx_parts = [], []
    for i, (beat, clip, tin, d) in enumerate(SHOTS):
        out = CUT / f'v{i}-{beat}.mp4'
        ff('-ss', tin, '-t', d, '-i', VID / clip, '-an', '-vf',
           f'scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},fps={FPS},scale=in_range=full:out_range=limited,format=yuv420p',
           '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '18', '-color_range', 'tv', '-colorspace', 'bt709', '-color_primaries', 'bt709', '-color_trc', 'bt709', out)
        parts.append(out)
        sp = CUT / f's{i}-{beat}.wav'
        if beat == 'minister':
            ff('-ss', tin, '-t', d, '-i', MIN_BED, '-ar', 48000, '-ac', 2, sp)
        else:
            ff('-ss', tin, '-t', d, '-i', VID / clip, '-vn', '-af', f'loudnorm=I={SFX_LUFS}:TP=-6,afade=t=in:d=0.08,afade=t=out:st={d - 0.08}:d=0.08',
               '-ar', 48000, '-ac', 2, sp)
        sfx_parts.append(sp)
    (CUT / 'list.txt').write_text(''.join(f"file '{p.name}'\n" for p in parts))
    ff('-f', 'concat', '-safe', '0', '-i', CUT / 'list.txt', '-c', 'copy', CUT / 'picture.mp4')
    (CUT / 'slist.txt').write_text(''.join(f"file '{p.name}'\n" for p in sfx_parts))
    sfx = CUT / 'sfx-world.wav'
    ff('-f', 'concat', '-safe', '0', '-i', CUT / 'slist.txt', '-af', f'apad=whole_dur={TOTAL}', '-ar', 48000, '-ac', 2, sfx)
    rep = CUT / 'vox-reporter.wav'
    ff('-i', REP, '-filter_complex',
       f'[0]atrim={L1[0]}:{L1[1]},asetpts=PTS-STARTPTS,adelay={ms(T_REP1)}|{ms(T_REP1)}[a];'
       f'[0]atrim={L2[0]}:{L2[1]},asetpts=PTS-STARTPTS,adelay={ms(T_REP2)}|{ms(T_REP2)}[b];'
       f'[a][b]amix=inputs=2:normalize=0,loudnorm=I=-20.5:TP=-2,apad=whole_dur={TOTAL}',
       '-ar', 48000, '-ac', 2, rep)
    mn = CUT / 'vox-minister.wav'
    ff('-i', MIN_DUB, '-af', f'atrim={MIN_IN}:{MIN_OUT},asetpts=PTS-STARTPTS,adelay=delays={ms(starts[3])}:all=1,apad=whole_dur={TOTAL}',
       '-ar', 48000, '-ac', 2, mn)
    ff('-i', CUT / 'picture.mp4', '-i', rep, '-i', mn, '-i', sfx, '-filter_complex', '[1:a][2:a][3:a]amix=inputs=3:normalize=0[a]',
       '-map', '0:v', '-map', '[a]', '-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k', '-t', TOTAL, CUT / 'preview.mp4')

    script = json.loads((SCENE / 'script.json').read_text())
    lines = {b['id']: b['lines'] for b in script['beats']}
    vt = {'reporter': (T_REP1, L1[1] - L1[0]), 'minister': (starts[3] + (0.71 - MIN_IN), 3.46 - 0.71),
          'button': (T_REP2, L2[1] - L2[0])}
    beats = []
    for i, (beat, clip, tin, d) in enumerate(SHOTS):
        bl = []
        for j, ln in enumerate(lines.get(beat, [])):
            tt, dd = vt[beat]
            bl.append({'i': j, 'who': ln['who'].lower(), 'name': ln['who'].title(), 't': round(tt, 2), 'dur': round(dd, 2),
                       'text': ln['text'], 'by': ln.get('by', 'claude')})
        beats.append({'id': beat, 'title': TITLES[beat], 'start': starts[i], 'dur': d, 'see': SEE[beat], 'lines': bl})
    edl = {'sequence': 'shorts-priority-lane-r1', 'title': 'Priority Lane Timeline',
           'heading': 'BadCode Shorts ▲ Priority Lane, rough cut 1',
           'intro': 'All five shots with the picked voices (reporter: Enceladus; minister: Orus, lip-synced). Note anything: a beat, a shot, a line, a sound, or a single frame.',
           'fps': FPS, 'total': TOTAL,
           'beats': beats,
           'video': [{'file': str(parts[i]), 'start': starts[i], 'dur': s[3], 'beat': s[0], 'source': str(VID / s[1]), 'looped': False}
                     for i, s in enumerate(SHOTS)],
           'audio': [{'track': 'A1', 'name': 'vox-reporter'}, {'track': 'A2', 'name': 'vox-minister'}, {'track': 'A3', 'name': 'sfx-world'}],
           'events': [{'stem': 'vox-reporter', 't': round(T_REP1, 2), 'dur': round(L1[1] - L1[0], 2), 'what': 'reporter line 1', 'src': str(REP)},
                      {'stem': 'vox-minister', 't': round(vt['minister'][0], 2), 'dur': round(vt['minister'][1], 2), 'what': 'minister line (lip-synced)', 'src': str(MIN_DUB)},
                      {'stem': 'vox-reporter', 't': round(T_REP2, 2), 'dur': round(L2[1] - L2[0], 2), 'what': 'reporter line 2 (the button)', 'src': str(REP)}]
                     + [{'stem': 'sfx-world', 't': starts[i], 'dur': s[3], 'what': f'{s[0]}: ' + ('room bed' if s[0] == 'minister' else "clip's own ambience"),
                         'src': str(MIN_BED if s[0] == 'minister' else VID / s[1])} for i, s in enumerate(SHOTS)],
           'flags': [f'Runs {TOTAL:.1f} s, a little over the 20 s target: the reporter reads slowly (line 1 is 5.3 s). Trim or re-voice brisker if it drags.',
                     'Minister line is the picked take sped x1.26 to fit the mouth; unheard by a human yet.',
                     'No music yet (sound.md has none).']}
    (CUT / 'edl.json').write_text(json.dumps(edl, indent=1, ensure_ascii=False))
    print(json.dumps({'total': TOTAL, 'starts': starts, 'preview': str(CUT / 'preview.mp4')}))


if __name__ == '__main__':
    main()
