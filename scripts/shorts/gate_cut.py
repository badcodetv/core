#!/usr/bin/env python3
"""The Starting Gate: rough cut from the picked clips and the commentator (comm-b).

    python3 scripts/shorts/gate_cut.py [--round N]

Writes <media>/cut/rN/: one piece per shot (whole frames only), the commentary stem, the clips' own sound (no speech in
the picked clips: checked), the mix, preview.mp4 and edl.json in the timeline format (scripts/scene/timeline.py).
The commentary is voice-over (BadCode is masked): each line is laid whole at its time, never cut up.
"""
import argparse, json, pathlib, subprocess, sys

REPO = pathlib.Path(__file__).resolve().parents[2]
SCENE = REPO / 'docs/stories/short-starting-gate/scenes/starting-gate'
sys.path.insert(0, str(REPO / 'scripts/drive'))
from localmap import localize  # noqa: E402

cfg = localize(json.loads((SCENE / 'scene.json').read_text()))
MEDIA = pathlib.Path(cfg['media'])
VID, CAST = MEDIA / 'video', MEDIA / 'audio/casting'
VOICE = 'comm-b'  # Jack's pick, 2026-11-22
LOGO = REPO / 'docs/brand/logo/badcode-stacked-reversed-2400.png'
# Round 2's photo-finish outro (scripts/shorts/gate_outro.py) was dropped in round 3 (Jack r2 at794: "this is weird change
# it, all the horses morph and change, maybe make it more of a simple clip, also where is the badcode outro").
# Round 3's box clip (OUTc) and round 4's breakout (BURSTb, Jack: "remove the horse outro, it is ai slop") are out. Round 5:
# "like the beer outro ... horse themed, like it is sprayed on the side of a horse and it is moving": WAGES walks side-on,
# the camera tracking with him, the official logo file painted onto his flank (scripts/shorts/gate_flank_logo.py).
OUT_CLIP, OUT_IN, OUT_DUR = 'starting-gate-FLANKb-FLANK.mp4', 3.5, 4.0   # Claude's pick, round 5: the settled stretch
FLANK = dict(cx=700, cy=900, w=380, opacity=0.94, fade=0.4)                 # the logo on the barrel at OUT_IN, 1080x1920 px
FLANK_PY = pathlib.Path.home() / '.cache/badcode-lips/venv/bin/python'
ROOM_DB = {'outro': 6}   # the clip's own sound per shot (default -12 dB): the flank clip is quiet (-31.5 LUFS), so up
W, H, FPS = 1080, 1920, 24
CLAMP = 'scale=in_range=full:out_range=limited,format=yuv420p,lutyuv=y=clip(val\\,20\\,235)'
ENC = ['-c:v', 'libx264', '-preset', 'veryfast', '-crf', '18', '-pix_fmt', 'yuv420p', '-color_range', 'tv',
       '-colorspace', 'bt709', '-color_primaries', 'bt709', '-color_trc', 'bt709']
VF = f'scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},fps={FPS}'
LINES = {'01-off': "New money's been printed, the gates are open... and they're off!",
         '02-break': "Shares flies out! Houses right on its tail! And Wages... Wages hasn't left the stalls.",
         '03-home': "Houses home in seven years! And Wages is away! Eleven years... and nine months.",
         '04-onegate': "Next race. One gate. Everybody out at once."}
# (beat, title, clip, in, dur, hold-first-frame s, [(line, at s into the shot)], what we see)
# Timing: "and they're off" (3.36 s into line 1) lands 0.06 s after the stalls' clang (GATEa 2.2 s, shown at 0.6 s);
# the field in ONEGATEe starts moving ~2.2 s in, so its first frame is held 2.3 s to break on "Everybody out at once"
# (round 2: ONEGATEa left a ghost row at the gate, Jack r1 at728 "ai slop the horse teleported").
SHOTS = [
    ('box', '1. The commentator', 'starting-gate-BOXa-BOX.mp4', 0.5, 3.0, 0, [('01-off', 0.3)], 'BadCode in the box, binoculars up'),
    ('gate', '2. And they\'re off', 'starting-gate-GATEa-GATE.mp4', 1.6, 3.0, 0, [], 'The stalls clang open; SHARES and HOUSES go, WAGES stays'),
    ('break', '3. The break', 'starting-gate-BREAKb-BREAK.mp4', 0.0, 5.0, 0, [('02-break', 0.2)], 'SHARES and HOUSES thunder past; WAGES alone in its stall'),
    ('stall', '4. Wages in the stall', 'starting-gate-STALLa-STALL.mp4', 0.0, 4.3, 0, [], 'WAGES chewing hay as the sky turns over'),
    ('winners', '5. Houses home', 'starting-gate-WINNERSb-WINNERS.mp4', 0.0, 3.2, 0, [('03-home', 0.1)], 'HOUSES and its owners, champagne'),
    ('trot', '6. Wages is away', 'starting-gate-TROTb-TROT.mp4', 1.0, 5.3, 0, [], 'WAGES trots alone along the flooded course'),
    ('onegate', '7. One gate', 'starting-gate-ONEGATEe-ONEGATE.mp4', 0.0, 7.5, 2.3, [('04-onegate', 0.2)], 'Next race: everybody out at once'),
    ('outro', '8. The logo on Wages', OUT_CLIP, OUT_IN, OUT_DUR, 0, [], 'WAGES walks side-on with the BadCode logo sprayed on his flank; fade to black'),
]


def ff(*a):
    subprocess.run(['ffmpeg', '-nostdin', '-loglevel', 'error', '-y', *map(str, a)], check=True)


def dur(p):
    return float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', str(p)],
                                capture_output=True, text=True, check=True).stdout)


def main():
    ap = argparse.ArgumentParser(); ap.add_argument('--round', type=int, default=1); a = ap.parse_args()
    cut = MEDIA / 'cut' / f'r{a.round}'; cut.mkdir(parents=True, exist_ok=True)
    t, parts, vids, beats, vox, room, events = 0.0, [], [], [], [], [], []
    for n, (bid, title, src, cin, sd, hold, lines, see) in enumerate(SHOTS):
        st = round(t, 3); fr = round(sd * FPS); sd = fr / FPS
        pf = cut / f'v{n:02d}-{bid}.mp4'
        if src:
            vf = VF + (f',tpad=start_mode=clone:start_duration={hold}' if hold else '') + f',tpad=stop_mode=clone:stop_duration=4,{CLAMP}'
            if bid == 'outro':
                subprocess.run([str(FLANK_PY), str(REPO / 'scripts/shorts/gate_flank_logo.py'), str(VID / src), str(pf), '--in', str(cin),
                                '--dur', str(sd), *[x for k, v in FLANK.items() for x in (f'--{k}', str(v))]], check=True)
            else:
                ff('-ss', cin, '-i', VID / src, '-vf', vf, '-frames:v', fr, '-an', *ENC, pf)
            room.append((st, VID / src, cin, sd, hold, ROOM_DB.get(bid, -12)))
            events.append({'stem': 'amb-room', 't': st, 'dur': sd, 'what': f"{title}: the clip's own sound", 'src': src})
        else:
            # the last frame of the shot before fades to black as the logo fades in (a dissolve, not a hard cut)
            lastpng = cut / f'v{n:02d}-from.png'
            ff('-sseof', -0.05, '-i', parts[-1], '-frames:v', 1, '-update', 1, lastpng)
            ff('-f', 'lavfi', '-i', f'color=black:s={W}x{H}:r={FPS}:d={sd}', '-loop', 1, '-r', FPS, '-i', lastpng, '-loop', 1, '-i', LOGO,
               '-filter_complex',
               f"[1]scale=in_range=limited:out_range=full,format=rgba,fade=t=out:st=0:d=0.6:alpha=1[p];"
               f"[2]scale=640:-1,format=rgba,fade=t=in:st=0.3:d=0.6:alpha=1[l];"
               f"[0][p]overlay=0:0:shortest=1[b];[b][l]overlay=(W-w)/2:(H-h)/2:shortest=1,{CLAMP}",
               '-frames:v', fr, *ENC, pf)
        ls = []
        for k, at in lines:
            w = CAST / f'{k}--{VOICE}.wav'; d = round(dur(w), 3); lt = round(st + at, 3)
            vox.append((lt, w)); ls.append({'i': len(ls), 'who': 'badcode', 'name': 'BadCode (commentator)', 't': lt, 'dur': d,
                                           'text': LINES[k], 'by': 'claude (draft; line 1 Jack\'s wording)'})
            events.append({'stem': 'vox-badcode', 't': lt, 'dur': d, 'what': f'{title}: the commentator', 'src': str(w)})
        parts.append(pf)
        vids.append({'file': str(pf), 'in': cin, 'start': st, 'dur': sd, 'beat': bid, 'source': str(src), 'looped': False})
        beats.append({'id': bid, 'title': title, 'start': st, 'dur': sd, 'see': see, 'lines': ls})
        t = st + sd
    total = round(t, 3)
    (cut / 'list.txt').write_text(''.join(f"file '{p.name}'\n" for p in parts))
    ff('-f', 'concat', '-safe', '0', '-i', cut / 'list.txt', '-c', 'copy', cut / 'picture.mp4')
    ins, fl = [], []
    for k, (at, w) in enumerate(vox):
        ins += ['-i', w]; fl.append(f'[{k}]aresample=48000,aformat=channel_layouts=stereo,adelay={int(at * 1000)}|{int(at * 1000)}[s{k}]')
    fl.append(f"{''.join(f'[s{k}]' for k in range(len(vox)))}amix=inputs={len(vox)}:normalize=0,apad=whole_dur={total},atrim=end={total}[o]")
    ff(*ins, '-filter_complex', ';'.join(fl), '-map', '[o]', '-ar', 48000, cut / 'vox-badcode.wav')
    ins, fl = [], []
    for k, (at, s, iin, ilen, hold, db) in enumerate(room):
        ins += ['-ss', iin, '-t', ilen, '-i', s]
        d0 = int((at + hold) * 1000)
        fl.append(f'[{k}:a]asetpts=PTS-STARTPTS,aresample=48000,aformat=channel_layouts=stereo,afade=t=in:d=0.1,'
                  f'afade=t=out:st={max(0, ilen - hold - 0.15)}:d=0.15,atrim=end={max(0.2, ilen - hold)},volume={db}dB,adelay={d0}|{d0}[f{k}]')
    fl.append(f"{''.join(f'[f{k}]' for k in range(len(room)))}amix=inputs={len(room)}:normalize=0,apad=whole_dur={total},atrim=end={total}[o]")
    ff(*ins, '-filter_complex', ';'.join(fl), '-map', '[o]', '-ar', 48000, cut / 'amb-room.wav')
    audio = [{'track': 'A1', 'name': 'vox-badcode', 'file': str(cut / 'vox-badcode.wav')},
             {'track': 'A2', 'name': 'amb-room', 'file': str(cut / 'amb-room.wav')}]
    ff('-i', audio[0]['file'], '-i', audio[1]['file'], '-filter_complex',
       '[0][1]amix=inputs=2:normalize=0,loudnorm=I=-14:TP=-1.5,alimiter=limit=0.84:level=0[o]', '-map', '[o]', '-ar', 48000, '-ac', 2, cut / 'mix.wav')
    ff('-i', cut / 'picture.mp4', '-i', cut / 'mix.wav', '-map', '0:v', '-map', '1:a', '-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k', '-t', total, cut / 'preview.mp4')
    edl = {'sequence': f'short-starting-gate-1-starting-gate-r{a.round}', 'title': 'Starting Gate Timeline',
           'heading': f'BadCode Shorts ▲ The Starting Gate, rough cut {a.round}',
           'intro': 'A horse race where new money is the starting gun: SHARES and HOUSES fly out, WAGES stays in its stall for eleven years and nine months; next race, one gate for everyone.',
           'fps': FPS, 'total': total, 'beats': beats, 'video': vids, 'audio': audio, 'events': events,
           'flags': ['No music yet. Room sound is the clips\' own (no speech in any picked clip).',
                     'The commentary runs at its natural pace: about 34 s against the script\'s 17. Trim notes welcome (which pauses, which lines).',
                     'The way out (one gate) is Claude\'s: no BadCode government policy on record.',
                     'Outro: the logo sprayed on WAGES\' flank as he walks (round 5, Jack: "like the beer outro ... sprayed on the side of a horse").']}
    (cut / 'edl.json').write_text(json.dumps(edl, indent=1, ensure_ascii=False))
    print(json.dumps({'total': total, 'preview': str(cut / 'preview.mp4')}))


if __name__ == '__main__':
    main()
