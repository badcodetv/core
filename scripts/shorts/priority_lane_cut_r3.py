#!/usr/bin/env python3
"""Priority Lane (BadCode Short): rough cut, round 3 (the ER-drama version), 2026-11-13.

    python3 scripts/shorts/priority_lane_cut_r3.py [--score <id8>] [--sfx key=id8,...]

9:16, 24 fps. Four picked clips (storyboard round 3), the seven picked AI Studio voice lines (sound.md, round 3:
Kore / Algieba / Alnilam / minister Charon), a Suno score (round r6-score) and Suno Sounds effects (r6-sfx), recorded
with `suno.mts record` into <media>/audio/suno-r6/ (never downloaded). The score and each effect are chosen by Suno
song id (first 8 characters); the defaults below are the current picks. Ends on black with the logo.
Writes <media>/cut-r3/edl.json (timeline format, scripts/scene/timeline.py), one stem per track, and preview.mp4.
"""
import glob, json, pathlib, subprocess, sys

REPO = pathlib.Path(__file__).resolve().parents[2]
SCENE = REPO / 'docs/stories/shorts/priority-lane'
sys.path.insert(0, str(REPO / 'scripts/drive'))
from localmap import localize  # noqa: E402

cfg = localize(json.loads((SCENE / 'scene.json').read_text()))
MEDIA = pathlib.Path(cfg['media'])
VID, AUD = MEDIA / 'video', MEDIA / 'audio'
VOX, SUNO = AUD / 'voices', AUD / 'suno-r6'
CUT = MEDIA / 'cut-r3'; CUT.mkdir(parents=True, exist_ok=True)
LOGO = MEDIA / 'overlay/badcode-lockup-reversed-420.png'
W, H, FPS, SR = 1080, 1920, 24, 48000

args = sys.argv[1:]
SCORE = args[args.index('--score') + 1] if '--score' in args else 'c5d8704d'
SFX = {'siren': '956b121e', 'monitor': '0de628b4', 'cabin': '88c2320f', 'stop': '29374f46', 'passby': '3cad4a31', 'flatline': 'cbe45667'}
if '--sfx' in args:
    SFX.update(dict(kv.split('=') for kv in args[args.index('--sfx') + 1].split(',')))


def take(id8):
    hits = [h for h in glob.glob(str(SUNO / f'*-{id8}.wav'))]
    if not hits:
        sys.exit(f'🔴 no recording for {id8} in {SUNO}: run `suno.mts record {id8}` (LISTEN_MEDIA_ROOT={SUNO})')
    return pathlib.Path(hits[0])


# (beat, clip, in, dur). Clip in-points: A from the start (her turn); B where the black car crosses (~1.5-4 s);
# C round the lip-synced line (voice 0.94-3.52 s on the clip's clock); D from the start (flat line 0-4 s).
SHOTS = [('losing', 'pl-r3-A-LS5-b.mp4', 0.0, 7.9),
         ('held', 'pl-r3-B-HD3-b.mp4', 1.5, 2.6),
         ('motorcade', 'pl-04-MIN1-b-charon.mp4', 0.6, 3.3),
         ('flatline', 'pl-r3-D4-FL4-a.mp4', 0.0, 5.6)]
# Jack's note on round 3 (2026-11-13, at 0:19): "zoom into the flatline on the screen then have the badcode logo on it".
# So no black end card: D pushes in on the monitor (ZOOM_*), the screen goes dark in the clip at ~4 s and the logo
# fades up on it (LOGO_AT), in silence.
END = 0.0
ZOOM_FROM, ZOOM_TO, ZOOM = 1.4, 3.2, 3.0
SCREEN = (0.197, 0.459)                     # the monitor screen's centre, as a fraction of the frame (measured on the clip)
LOGO_AT = 4.0
starts, t = [], 0.0
for s in SHOTS: starts.append(round(t, 3)); t += s[3]
PIC = round(t, 3); TOTAL = round(PIC + END, 3)
A, B, C, D = starts
# Voice lines: (stem, file, at, from, to, who, text). Round 3 first build overlapped all three crew lines and buried
# two of them, so they now take turns with ~0.15-0.25 s overlaps, the driver's line split to open and close beat A.
LINES = [('vox-driver', 'a3-driver-two-minutes.wav', A + 0.3, 0.0, 1.12, 'driver', 'Two minutes out!'),
         ('vox-paramedic1', 'a1-paramedic1-bp.wav', A + 1.25, 0.0, 3.2, 'paramedic1', "BP 60 over 30! Fucking hurry up, we're gonna lose him!"),
         ('vox-paramedic2', 'a2-paramedic2-sats.wav', A + 4.2, 0.0, 2.09, 'paramedic2', "Sats dropping, he's peri-arrest!"),
         ('vox-driver', 'a3-driver-two-minutes.wav', A + 6.1, 1.85, 3.55, 'driver', 'Get the fuck out of the way!'),
         ('vox-paramedic2', 'b1-paramedic2-why.wav', B + 0.45, 0.0, None, 'paramedic2', 'Why have we stopped?!'),
         ('vox-paramedic1', 'd1-paramedic1-fifty.wav', D + 0.24, 0.0, 0.76, 'paramedic1', 'Fifty over twen-')]
FLAT = D + 1.0                              # the flatline tone cuts "twen-"
MIN_DUB = AUD / 'dub/pl-04-minister-charon-dub.wav'   # on clip C's own clock
MIN_BED = AUD / 'dub/pl-04-bed.wav'
# Effects: (stem, key, at, dur, gain dB, loop)
EFX = [('sfx-cabin', 'cabin', 0.0, B + 2.6, -10, True),
       ('sfx-siren', 'siren', 0.0, B + 0.15, -8, True),
       ('sfx-monitor', 'monitor', 0.0, C, -9, True),
       ('sfx-cars', 'stop', B - 0.1, 2.0, -6, False),
       ('sfx-cars', 'passby', B + 0.6, 3.0, -9, False),
       ('sfx-cabin', 'cabin', D, 3.5, -14, True),
       ('sfx-monitor', 'flatline', FLAT, D + LOGO_AT - FLAT, -12, True)]   # the tone stops as the logo comes up


def racing_monitor(id8, length):
    """Suno's monitor takes beep at a calm 60 a minute; the patient is crashing. Lay one of its beeps (0.11-0.21 s)
    at an interval that quickens from 0.55 s to 0.32 s (about 110 to 190 a minute)."""
    import numpy as np
    src = take(id8)
    y = np.frombuffer(subprocess.run(['ffmpeg', '-v', 'error', '-i', src, '-ac', '2', '-ar', str(SR), '-f', 'f32le', '-'],
                                     capture_output=True, check=True).stdout, np.float32).reshape(-1, 2)
    beep = y[int(0.10 * SR):int(0.23 * SR)]
    out = np.zeros((int(length * SR), 2), np.float32); t = 0.05
    while t < length - 0.15:
        i = int(t * SR); n = min(len(beep), len(out) - i); out[i:i + n] += beep[:n]
        t += 0.55 - 0.23 * min(1.0, t / length)
    dst = SUNO / f'monitor-racing-{id8}.wav'
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-f', 'f32le', '-ar', str(SR), '-ac', '2', '-i', '-', dst], input=out.tobytes(), check=True)
    return dst


def ff(*a):
    subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', *map(str, a)], check=True)


def ms(x):
    return int(round(x * 1000))


def place(out, pieces):
    """pieces: [(file, at, dur or None, gain_db, loop, filt)] -> one stem the length of the cut."""
    ins, ch = [], []
    for k, (f, at, d, g, loop, filt) in enumerate(pieces):
        ins += (['-stream_loop', '-1'] if loop else []) + ['-i', f]
        tr = f'atrim=0:{d},' if d else ''
        fade = f'afade=t=out:st={max(0, d - 0.06)}:d=0.06,' if d else ''
        ch.append(f'[{k}]asetpts=PTS-STARTPTS,{filt + "," if filt else ""}{tr}asetpts=PTS-STARTPTS,afade=t=in:d=0.01,{fade}volume={g}dB,'
                  f'aresample={SR},aformat=channel_layouts=stereo,adelay=delays={ms(at)}:all=1[p{k}]')
    mix = ''.join(f'[p{k}]' for k in range(len(pieces)))
    ch.append(f'{mix}amix=inputs={len(pieces)}:normalize=0,apad=whole_dur={TOTAL}[o]')
    # ffmpeg 6.1: an atrim after adelay drops the delay, so the length is cut on output (-t) instead
    ff(*ins, '-filter_complex', ';'.join(ch), '-map', '[o]', '-t', TOTAL, '-ar', SR, '-ac', 2, out)


def main():
    vf = (f'scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},fps={FPS},'
          "scale=in_range=full:out_range=limited,format=yuv420p,lutyuv=y='clip(val,18,229)':u='clip(val,16,240)':v='clip(val,16,240)'")
    # the clip(...) pass: the Held shot's headlights still read as full-range whites after the scale (delivery-qc FAIL)
    enc = ['-c:v', 'libx264', '-preset', 'veryfast', '-crf', '18', '-color_range', 'tv', '-colorspace', 'bt709',
           '-color_primaries', 'bt709', '-color_trc', 'bt709']
    parts = []
    for i, (beat, clip, tin, d) in enumerate(SHOTS):
        out = CUT / f'v{i}-{beat}.mp4'
        if beat == 'flatline':
            # Eased push into the screen (smoothstep), the screen's centre travelling to the frame's centre, then the logo on it.
            cx, cy = SCREEN[0] * W, SCREEN[1] * H
            pr = f"min(1,max(0,(it-{ZOOM_FROM})/{ZOOM_TO - ZOOM_FROM}))"
            z = f"1+{ZOOM - 1}*(3*pow({pr},2)-2*pow({pr},3))"
            zp = (f"zoompan=z='{z}':x='({W / 2}+({cx}-{W / 2})*(zoom-1)/{ZOOM - 1})-iw/zoom/2'"
                  f":y='({H / 2}+({cy}-{H / 2})*(zoom-1)/{ZOOM - 1})-ih/zoom/2':d=1:s={W}x{H}:fps={FPS}")
            pre = f'scale={2 * W}:{2 * H}:force_original_aspect_ratio=increase,crop={2 * W}:{2 * H},fps={FPS},'
            zp = zp.replace(f'{W / 2}', f'{W}').replace(f'{H / 2}', f'{H}').replace(f'{cx}', f'{2 * cx}').replace(f'{cy}', f'{2 * cy}')
            ff('-ss', tin, '-t', d, '-i', VID / clip, '-i', LOGO, '-filter_complex',
               f"[0]{pre}{zp}[z];[1]scale=560:-1,format=rgba,loop=-1:size=1,fps={FPS},trim=0:{d + 0.5},setpts=N/{FPS}/TB,"
               f"fade=t=in:st={LOGO_AT}:d=0.5:alpha=1[l];"   # loop the still first, THEN fade (fading one frame then looping it stays invisible)
               f"[z][l]overlay=(W-w)/2:(H-h)/2:eof_action=pass,{vf}", '-t', d, '-an', *enc, out)
        else:
            ff('-ss', tin, '-t', d, '-i', VID / clip, '-an', '-vf', vf, *enc, out)
        parts.append(out)
    (CUT / 'list.txt').write_text(''.join(f"file '{p.name}'\n" for p in parts))
    ff('-f', 'concat', '-safe', '0', '-i', CUT / 'list.txt', '-c', 'copy', CUT / 'picture.mp4')

    stems, events = {}, []
    for stem, f, at, a0, a1, who, text in LINES:
        cut = (a1 - a0) if a1 else None
        stems.setdefault(stem, []).append((VOX / f, at, cut, 0, False, f'atrim=start={a0},asetpts=PTS-STARTPTS' if a0 else ''))
        dur = cut or float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', VOX / f],
                                          capture_output=True, text=True).stdout)
        events.append({'stem': stem, 't': round(at, 2), 'dur': round(dur, 2), 'what': f'{who}: {text}', 'src': str(VOX / f), 'who': who, 'text': text})
    # The minister: his lip-synced dub, softened as if heard through glass, plus his car's room bed.
    glass = 'highpass=f=160,lowpass=f=2400'
    stems['vox-minister'] = [(MIN_DUB, C, None, 0, False, f'atrim=0.6:3.9,asetpts=PTS-STARTPTS,{glass}')]
    events.append({'stem': 'vox-minister', 't': round(C + 0.34, 2), 'dur': 2.58, 'what': "minister: I said raspberry-shaped hors d'oeuvres! (lip-synced, through glass)",
                   'src': str(MIN_DUB), 'who': 'minister', 'text': "I said raspberry-shaped hors d'oeuvres!"})
    for stem, key, at, d, g, loop in EFX:
        src = racing_monitor(SFX[key], d) if key == 'monitor' else take(SFX[key])
        stems.setdefault(stem, []).append((src, at, d, g, False if key == 'monitor' else loop, ''))
        events.append({'stem': stem, 't': round(at, 2), 'dur': round(d, 2), 'what': f'{key} (Suno Sounds {SFX[key]}' + (', one beep laid at a quickening rate)' if key == 'monitor' else ')'), 'src': str(src)})
    stems.setdefault('sfx-cabin', []).append((MIN_BED, C, 3.3, -6, True, ''))
    events.append({'stem': 'sfx-cabin', 't': C, 'dur': 3.3, 'what': "minister's car: its own room bed", 'src': str(MIN_BED)})
    # Score: from the top, stops dead on the flatline (Jack's brief: no music over the flatline).
    sc = take(SCORE)
    stems['music-score'] = [(sc, 0.0, FLAT, -7, False, '')]
    events.append({'stem': 'music-score', 't': 0.0, 'dur': round(FLAT, 2), 'what': f'score (Suno r6 {SCORE}), cut dead on the flatline', 'src': str(sc)})

    order = ['vox-paramedic1', 'vox-paramedic2', 'vox-driver', 'vox-minister', 'music-score', 'sfx-siren', 'sfx-monitor', 'sfx-cars', 'sfx-cabin']
    audio = []
    for k, stem in enumerate(order):
        out = CUT / f'{stem}.wav'; place(out, stems[stem])
        audio.append({'track': f'A{k + 1}', 'name': stem, 'file': str(out)})
    vox = [a for a in audio if a['name'].startswith('vox')]
    rest = [a for a in audio if not a['name'].startswith('vox')]
    ins = sum([['-i', a['file']] for a in audio], [])
    mix = ''.join(f'[{k + 1}:a]' for k in range(len(audio)))
    ff('-i', CUT / 'picture.mp4', *ins, '-filter_complex', f'{mix}amix=inputs={len(audio)}:normalize=0,alimiter=limit=0.89[a]',
       '-map', '0:v', '-map', '[a]', '-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k', '-t', TOTAL, CUT / 'preview.mp4')

    SEE = {'losing': 'Inside the ambulance at full pace: she turns and shouts to the cab, the van sways, the monitor races.',
           'held': 'Through the windscreen: the outrider holds his glove up; the black car glides across.',
           'motorcade': 'The minister in the back of his car, on the phone (lip-synced to Charon).',
           'flatline': 'Back inside: the line goes flat; he sits back. We push in on the flat line, the screen dies, and the BadCode logo comes up on it (Jack, round 3).'}
    TITLES = {'losing': 'A. Losing him', 'held': 'B. Held', 'motorcade': 'C. The motorcade', 'flatline': 'D. Flatline'}
    beats = []
    for i, (beat, clip, tin, d) in enumerate(SHOTS):
        bl = [{'i': j, 'who': e['who'], 'name': e['who'].title(), 't': e['t'], 'dur': e['dur'], 'text': e['text'], 'by': 'kai' if j == 0 and beat == 'losing' else 'claude'}
              for j, e in enumerate(e for e in events if 'who' in e and starts[i] <= e['t'] < starts[i] + d)]
        beats.append({'id': beat, 'title': TITLES[beat], 'start': starts[i], 'dur': d, 'see': SEE[beat], 'lines': bl})
    edl = {'sequence': 'shorts-1-priority-lane-r3', 'title': 'Priority Lane Timeline',
           'heading': 'BadCode Shorts ▲ Priority Lane, round 3 rough cut',
           'intro': ('The ER-drama version: the four picked shots, the picked voices (Kore, Algieba, Alnilam, minister Charon), '
                     f'a Suno score ({SCORE}) and Suno sound effects. Note anything: a beat, a shot, a line, a sound, or a single frame.'),
           'fps': FPS, 'total': TOTAL, 'beats': beats,
           # The flatline shot carries its push-in and the logo baked in (v3-flatline.mp4), so Premiere gets the finished shot.
           'video': [{'file': str(CUT / f'v{i}-{s[0]}.mp4') if s[0] == 'flatline' else str(VID / s[1]), 'in': 0.0 if s[0] == 'flatline' else s[2],
                      'start': starts[i], 'dur': s[3], 'beat': s[0], 'source': str(VID / s[1]), 'looped': False}
                     for i, s in enumerate(SHOTS)],
           'audio': audio,
           'events': [{k: v for k, v in e.items() if k not in ('who', 'text')} for e in events],
           'flags': [f'Runs {TOTAL:.1f} s (14 s was the brief): the three shouted lines need ~6 s even overlapping.',
                     'Score and effects are Suno takes recorded off the page (no downloads); every alternative take is in audio\\suno-r6.',
                     'The minister is filtered as if through glass; say if you want him clean.']}
    (CUT / 'edl.json').write_text(json.dumps(edl, indent=1, ensure_ascii=False))
    print(json.dumps({'total': TOTAL, 'starts': starts, 'preview': str(CUT / 'preview.mp4')}))


if __name__ == '__main__':
    main()
