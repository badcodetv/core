#!/usr/bin/env python3
"""Infinite Yous (short #68): rough cut r<N> to the locked track, outside Premiere (scene-timeline stage 4).

Writes <media>/cut/r<N>/preview.mp4 (720x1280, 24 fps, the track as the only sound) and edl.json in the
timeline format (scripts/scene/timeline.py), for build-timeline.py.

  python3 scripts/infinite-yous/cut.py [N]

The picture is timed to the track (Suno 92821b14, 15.0 s), measured 2026-11-15 by RMS in 0.1 s windows:
ticking 0-3.5, the arpeggio smear 3.5-6.4, accents every second from 6.5, the big tom at 11.3,
pad + brass held to ~13.8, fade to 15.0.
"""
import json, pathlib, subprocess, sys

N = int(sys.argv[1]) if len(sys.argv) > 1 else 1
REPO = pathlib.Path(__file__).resolve().parents[2]
SCENE = REPO / 'docs/stories/short-infinite-yous/scenes/infinite-yous'
MEDIA = pathlib.Path(subprocess.run(['python3', REPO / 'scripts/drive/localmap.py', 'path',
                                     json.loads((SCENE / 'scene.json').read_text())['media']],
                                    capture_output=True, text=True, check=True).stdout.strip())
V, M = MEDIA / 'video', MEDIA / 'moodboard'
SONG = MEDIA / 'audio/infinite-yous-r2-instrumental-taxi-meter-synth-p-92821b14.wav'
LOGO = REPO / 'docs/brand/logo/badcode-stacked-reversed-2400.png'
OUT = MEDIA / f'cut/r{N}'
OUT.mkdir(parents=True, exist_ok=True)
FPS, W, H, TOTAL = 24, 720, 1280, 15.0

# Beat boundaries (seconds). The kick ramp's contact frame (0.55 s in) lands on the tom at 11.3.
KICK = V / 'iy-04-ka-ramp-r1.mov'
KICK_CONTACT = 0.55
T = {'line': 0.0, 'split': 3.5, 'squeeze': 6.5, 'cab': 11.3 - KICK_CONTACT, 'logo': None, 'end': TOTAL}
kick_dur = float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', KICK],
                                capture_output=True, text=True).stdout)
T['logo'] = round((T['cab'] + kick_dur) * FPS) / FPS
fr = lambda a, b: round(b * FPS) - round(a * FPS)  # frames between two times
base = f'fps={FPS},scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},setsar=1'

inputs, parts = [], []
def inp(*a):
    inputs.extend(a)
    return sum(1 for x in inputs if x == '-i') - 1

# A. The line: clip 1 from the top (he grins, keys up, then turns for his car).
# r3+: the talking close-up (iy-01t-a, muted, dubbed) for the line, cut before he mouths the prompt's "Thanks" at 2.0,
# then the wide clip 1 from 1.5 s (keys spun, laughing, turning for his car).
n = fr(T['line'], T['split'])
if N >= 3:
    TALK = 2.0
    i = inp('-i', V / 'iy-01t-a-TK1-b.mp4')
    j = inp('-ss', '1.5', '-i', V / 'iy-01-LI1-b.mp4')
    parts.append(f'[{i}:v]{base},trim=end_frame={fr(0, TALK)},setpts=PTS-STARTPTS[a0]')
    parts.append(f'[{j}:v]{base},trim=end_frame={n - fr(0, TALK)},setpts=PTS-STARTPTS[a1]')
    parts.append('[a0][a1]concat=n=2:v=1:a=0[a]')
else:
    i = inp('-i', V / 'iy-01-LI1-b.mp4')
    parts.append(f'[{i}:v]{base},trim=end_frame={n},setpts=PTS-STARTPTS[a]')

# B. The split: five tall strips of clip 1 (from 0.4 s, while he faces camera), each a few frames later than the last,
# each window drifting sideways so the versions slide apart, thin bright lines between them (SP1-a is the look).
n = fr(T['split'], T['squeeze'])
sw = W // 5
i = inp('-i', V / 'iy-01-LI1-b.mp4')
parts.append(f'[{i}:v]{base},split=5' + ''.join(f'[s{k}]' for k in range(5)))
for k in range(5):
    off = 0.4 + k * 0.17
    x = f"'max(0,min({W - sw},{W // 2 - sw // 2}+({k - 2})*40*t))'"
    tint = ['', ',hue=h=8', ',hue=h=-8', ',eq=brightness=0.03', ',hue=s=1.15'][k]
    parts.append(f'[s{k}]trim=start={off},setpts=PTS-STARTPTS,crop={sw - 4}:{H}:{x}:0{tint},'
                 f'pad={sw}:{H}:2:0:color=0xF2F2F2,trim=end_frame={n}[st{k}]')
parts.append(''.join(f'[st{k}]' for k in range(5)) + f'hstack=5,trim=end_frame={n},setpts=PTS-STARTPTS[b]')

# C. Only one. r1: SQ2-a held with a push-in. r2+: three clean-room stills cut on the accents (grip 6.5, squeeze 7.5,
# a white flash into one at 8.5), each with a slow push; "There's only one" lands on C3.
def still(path, n, z0, z1):
    i = inp('-loop', '1', '-framerate', str(FPS), '-i', path)
    return (f"[{i}:v]scale={W * 2}:{H * 2}:force_original_aspect_ratio=increase,crop={W * 2}:{H * 2},"
            f"zoompan=z='{z0}+{z1 - z0}*on/{n}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={n}:s={W}x{H}:fps={FPS},"
            f"trim=end_frame={n},setpts=PTS-STARTPTS")
if N == 1:
    n = fr(T['squeeze'], T['cab'])
    i = inp('-loop', '1', '-framerate', str(FPS), '-i', M / 'SQ2-a.jpg')
    parts.append(f"[{i}:v]scale={W * 2}:{H * 2}:force_original_aspect_ratio=increase,crop={W * 2}:{H * 2},"
                 f"zoompan=z='1+0.12*pow(on/{n},2)':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={n}:s={W}x{H}:fps={FPS},"
                 f"trim=end_frame={n},setpts=PTS-STARTPTS[c]")
else:
    C = [('CL1-a', T['squeeze'], 7.5, 1.0, 1.04), ('CL2-b', 7.5, 8.5, 1.04, 1.12), ('CL3-b', 8.5, T['cab'], 1.0, 1.05)]
    for k, (nm, a, b, z0, z1) in enumerate(C):
        flash = ",fade=t=in:st=0:d=0.15:color=white" if k == 2 else ""
        parts.append(still(M / f'{nm}.jpg', fr(a, b), z0, z1) + f"{flash}[c{k}]")
    parts.append('[c0][c1][c2]concat=n=3:v=1:a=0[c]')

# D. Into the cab: Jack's pick, the dancer kick ramp, whole.
n = fr(T['cab'], T['logo'])
i = inp('-i', KICK)
parts.append(f'[{i}:v]{base},trim=end_frame={n},setpts=PTS-STARTPTS[d]')

# E. Headlights: clip 5's clear wall (after the car has gone), the official logo on the wall, fading up as the light passes.
n = fr(T['logo'], T['end'])
i = inp('-ss', '4.6', '-i', V / 'iy-05-LO1-b.mp4')
j = inp('-loop', '1', '-framerate', str(FPS), '-i', LOGO)
parts.append(f'[{i}:v]{base},trim=end_frame={n},setpts=PTS-STARTPTS[ew]')
parts.append(f"[{j}:v]scale={int(W * 0.5)}:-1,format=rgba,colorchannelmixer=aa=0.92,"
             f"fade=t=in:st=0.25:d=0.6:alpha=1,trim=end_frame={n},setpts=PTS-STARTPTS[lg]")
parts.append(f'[ew][lg]overlay=x=(W-w)/2:y=H*0.30:shortest=1[e]')

parts.append('[a][b][c][d][e]concat=n=5:v=1:a=0,scale=in_range=full:out_range=limited,format=yuv420p[v]')
k = inp('-i', SONG)
CAST = MEDIA / 'audio/casting'
VOX = ([('vox-lad', MEDIA / 'audio/dub/iy-01t-a-dub.wav', 0.0, 'lad a (Puck, brisk take 2), lip-synced to iy-01t-a x1.20: "One version of me gets home fine."'),
        ('vox-figure', CAST / 'sci2-d-enceladus.wav', 8.2, 'figure round 2 d (Enceladus, stand-in): "There\'s only one."')] if N >= 3 else
       [('vox-lad', CAST / 'lad-b-achird.wav', 0.3, 'lad b (Achird): "One version of me gets home fine."'),
        ('vox-figure', CAST / 'sci-a-charon.wav', 8.7, 'figure a (Charon): "There\'s only one."')] if N >= 2 else [])
amix = f'[{k}:a]aresample=48000,aformat=channel_layouts=stereo'
if VOX:
    duck = '+'.join(f"between(t,{t + 0.2:.2f},{t + 3.3:.2f})" for _, _, t, _ in VOX)
    amix += f",volume='if({duck},0.5,1)':eval=frame[mus]"
    labs = ['[mus]']
    for q, (_, f, t, _) in enumerate(VOX):
        vi = inp('-i', f)
        parts.append(f'[{vi}:a]aresample=48000,aformat=channel_layouts=stereo,adelay={int(t * 1000)}|{int(t * 1000)},volume=1.6[vx{q}]')
        labs.append(f'[vx{q}]')
    parts.append(amix)
    parts.append(''.join(labs) + f'amix=inputs={len(labs)}:normalize=0:duration=first,alimiter=limit=0.8:level=false[aout]')
else:
    parts.append(amix + '[aout]')
preview = OUT / 'preview.mp4'
subprocess.run(['ffmpeg', '-v', 'error', '-y', *map(str, inputs), '-filter_complex', ';'.join(parts),
                '-map', '[v]', '-map', '[aout]', '-t', str(TOTAL), '-c:v', 'libx264', '-crf', '18', '-preset', 'medium',
                '-color_range', 'tv', '-colorspace', 'bt709', '-color_primaries', 'bt709', '-color_trc', 'bt709', '-c:a', 'aac', '-b:a', '256k', preview], check=True)

beats = [
    ('line', 'A. The line', T['line'], T['split'], 'talking close-up iy-01t-a (TK1-b) lip-synced 0-2.0, then clip 1 wide from 1.5 s' if N >= 3 else 'clip 1 (LI1-b, option 1b): keys spun, the grin, he turns for his car', 'meter tick'),
    ('split', 'B. The split', T['split'], T['squeeze'], 'built in the edit (2a): clip 1 in five strips, offset 4 frames each, drifting apart', 'the arpeggio smears'),
    ('squeeze', 'C. Only one', T['squeeze'], T['cab'], 'SQ2-a held, push-in' if N == 1 else 'clean-room stills CL1-a grip (6.5), CL2-b squeeze (7.5), white flash into CL3-b one (8.5)', 'accents every second'),
    ('cab', 'D. Into the cab', T['cab'], T['logo'], "Jack's pick iy-04-ka-ramp-r1 (dancer kick, ramped); contact on the 11.3 s tom", 'the gated tom'),
    ('logo', 'E. Headlights', T['logo'], T['end'], 'clip 5 clear wall from 4.6 s + the official stacked logo fading up', 'pad, brass swell, whoosh'),
]
src = {'line': V / ('iy-01t-a-TK1-b.mp4' if N >= 3 else 'iy-01-LI1-b.mp4'), 'split': V / 'iy-01-LI1-b.mp4', 'squeeze': M / 'SQ2-a.jpg', 'cab': KICK,
       'logo': V / 'iy-05-LO1-b.mp4'}
if N == 1:
    FLAGS = ['The lines are not heard yet.', 'C is the SQ2-a still with a push-in.']
elif N == 2:
    FLAGS = ['Voices are stand-ins until Jack picks (voice page): lad b, figure a.',
             "The lad's lips don't match his line (clip 1 has no talking); the figure has no mouth."]
else:
    FLAGS = ['Lad: Jack\'s pick a (Puck), a brisk retake fitted to the talking clip at x1.20 ("home" lands 0.12 s after his lips close). '
             'Figure: round-2 take d as a stand-in until Jack picks.']
if N >= 2:
    FLAGS.append('CL2-b: his goggles sit over the top of the mask (ring and triangle still show, no skin).')
edl = {
    'sequence': f'short-infinite-yous-1-infinite-yous-r{N}', 'title': 'Infinite Yous: rough cut',
    'heading': 'BadCode Shorts ▲ Infinite Yous', 'fps': FPS, 'total': TOTAL,
    'intro': f'Rough cut {N}: every beat cut to the locked track (Suno 92821b14). Note any beat, shot or moment.',
    'beats': [{'id': b, 'title': t, 'start': s, 'dur': e - s, 'see': see, 'act': f'track: {hear}', 'lines': []}
              for b, t, s, e, see, hear in beats],
    'video': [{'file': str(preview), 'source': str(src[b]), 'start': s, 'dur': e - s, 'beat': b, 'looped': False}
              for b, t, s, e, see, hear in beats],
    'audio': [{'track': 'A1', 'name': 'mus-track'}] + [{'track': f'A{q + 2}', 'name': st} for q, (st, _, _, _) in enumerate(VOX)],
    'events': [{'stem': 'mus-track', 't': 0, 'dur': TOTAL, 'what': 'the locked track, 92821b14' + (', ducked under the lines' if VOX else ''), 'src': str(SONG)}]
              + [{'stem': st, 't': t, 'dur': float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', f], capture_output=True, text=True).stdout), 'what': w, 'src': str(f)} for st, f, t, w in VOX],
    'flags': [
        *FLAGS,
        'E: the logo fades up rather than being lit by a moving headlight; clip 5\'s own sweep is in its first 4 s, under a car.',
    ],
}
(OUT / 'edl.json').write_text(json.dumps(edl, indent=1))
print(json.dumps({k: round(v, 3) for k, v in T.items()}), '->', preview)
