#!/usr/bin/env python3
"""Priority Lane (BadCode Short): rough cut 6, 2026-11-19 (built on round 5's script, priority_lane_cut_r5.py).

Round 6, Jack's picks and notes of 2026-11-19:
- every voice recast (picks page round 6-7, sound.md "Voices, round 6"): paramedic 1 a, paramedic 2 d, driver d (angry),
  minister d, constable b (radio); each take split into its lines at the word gaps (scripts/word_times.py).
- score c2, percussion only (bec07ebd).
- 6:19 "they're driving with the back door open": beat A's ambulance is now r20-A (LS21-b, inside, doors shut).
- 17:19 "he's eating and talking at the same time": the minister is r20-C (BM20-a, no food).
- 25:19 the flatline logo: "do the flatline style logo animation in Flow… it can just show the screen and then cut to it":
  the monitor push-in (FL18-a, no logo now) cuts to the Flow clip r20-LG (LG20-a: two last beats, then flat) and the
  official logo is laid on once the line is flat (Flow never draws the logo).
- --finish <night35|dashcam|bleach>: a filter over every shot (scripts/shorts/priority_lane_finish.sh), the logo untouched.

Round 5's notes follow.
Round 5, 2026-11-17: every shot rebuilt on Unsplash templates.

Jack's picks (mood boards 18-19): LS18-b losing him, PB18-a his poster at the bus stop (the ambulance races past),
CD18-a the cordon from above (new beat, with the police radio), HD19-b held from the cab (matched to CD18-a),
BM18-a the minister in his car (new line), FL18-a the flatline (a still: push into the screen, logo on it).
Audio: the round 4 crew lines, Suno score and Suno effects; new: the minister's line (Charon) and the constable's
radio (stand-in voice Iapetus). Kai's notes, meeting 2026-11-17: the poster held ~3 s, the cordon spelled out, the
early car shot cut, "Hey Jeffrey … fetch Andrew".

    python3 scripts/shorts/priority_lane_cut_r5.py [--score <id8>]
"""

# style-lint: story=shorts/priority-lane (this short's own picked voices and takes, read from its sound.md)
import glob, json, pathlib, subprocess, sys

REPO = pathlib.Path(__file__).resolve().parents[2]
SCENE = REPO / 'docs/stories/shorts/priority-lane'
sys.path.insert(0, str(REPO / 'scripts/drive'))
from localmap import localize  # noqa: E402

cfg = localize(json.loads((SCENE / 'scene.json').read_text()))
MEDIA = pathlib.Path(cfg['media'])
VID, AUD = MEDIA / 'video', MEDIA / 'audio'
VOX, SUNO = AUD / 'voices', AUD / 'suno-r6'
CAST = AUD / 'casting-r7'
args0 = sys.argv[1:]
FINISH = args0[args0.index('--finish') + 1] if '--finish' in args0 else ''
CUT = MEDIA / ('cut-r6' + (f'-{FINISH}' if FINISH else '')); CUT.mkdir(parents=True, exist_ok=True)
LOGO = MEDIA / 'overlay/badcode-lockup-reversed-420.png'
W, H, FPS, SR = 1080, 1920, 24, 48000

args = sys.argv[1:]
SCORE = args[args.index('--score') + 1] if '--score' in args else 'bec07ebd'
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
# Beat A is intercut (round 4): ambulance -> his poster at the shelter (readable ~2.4 s, under "we're gonna lose him")
# -> the poster-to-car transition (baked: TRANSITION) -> back inside. Beat A keeps its 7.9 s so every line stays put.
# Round 4b (Jack's notes on round 4, 2026-11-14): at 4:05 "keep this clip but play it quickly" -> the shelter shot
# plays at SPEED (its first 3 s, while the poster is readable, in 1.5 s); at 4:21 "remove this part/clip" -> the poster
# close-up no longer holds: it only shows inside the dissolve into the car. The ambulance takes the time back.
SPEED = {}
STILL = MEDIA / 'moodboard/FL18-a.jpg'
SHOTS = [('losing', 'pl-r20-A-LS21-b.mp4', 0.0, 2.4),
         ('losing', 'pl-r5-A2-PB18-a.mp4', 0.3, 3.0),     # his poster at the bus stop, the ambulance races past (~3 s, Kai)
         ('losing', 'pl-r20-A-LS21-b.mp4', 2.4, 2.5),
         ('cordon', 'pl-r5-A3-CD18-a.mp4', 0.4, 4.9),     # the police holding the junction, the radio call
         ('held', 'pl-r5-B-HD19-b.mp4', 1.0, 2.6),
         ('motorcade', 'pl-r20-C-BM20-a.mp4', 0.2, 5.8),
         ('flatline', 'STILL', 0.0, 2.4),
         ('end', 'pl-r20-LG-LG20-a.mp4', 0.0, 5.6)]   # the Flow trace: two last beats, flat by ~4 s; the logo at LOGO_AT
END = 0.0
ZOOM_FROM, ZOOM_TO, ZOOM = 0.2, 2.4, 2.4
SCREEN = (0.565, 0.436)                     # FL18-a's monitor screen centre (measured on the still)
LOGO_AT = 4.0                               # seconds into the end clip, once the line is flat
starts, t = [], 0.0
for s in SHOTS: starts.append(round(t, 3)); t += s[3]
PIC = round(t, 3); TOTAL = round(PIC + END, 3)
BEAT_AT, BEAT_DUR = {}, {}
for s, st in zip(SHOTS, starts):
    BEAT_AT.setdefault(s[0], st); BEAT_DUR[s[0]] = round(BEAT_DUR.get(s[0], 0) + s[3], 3)
A, K, B, C, D, E = (BEAT_AT[k] for k in ('losing', 'cordon', 'held', 'motorcade', 'flatline', 'end'))
# (stem, take, at, from, to, who, text): round 6 takes, cut at the gaps between words (word_times.py)
LINES = [('vox-driver', 'pl-r7-driver-d-angry.wav', A + 0.3, 0.0, 1.3, 'driver', 'Two minutes out!'),
         ('vox-paramedic1', 'pl-r7-paramedic1-a.wav', A + 1.3, 0.4, 3.7, 'paramedic1', "BP 60 over 30! Fucking hurry up, we're gonna lose him!"),
         ('vox-paramedic2', 'pl-r7-paramedic2-d.wav', A + 4.5, 0.0, 1.95, 'paramedic2', "Sats dropping, he's peri-arrest!"),
         ('vox-driver', 'pl-r7-driver-d-angry.wav', A + 6.4, 1.5, 3.1, 'driver', 'Get the fuck out of the way!'),
         ('vox-paramedic2', 'pl-r7-paramedic2-d.wav', B + 0.3, 2.25, 3.15, 'paramedic2', 'Why have we stopped?!'),
         ('vox-paramedic1', 'pl-r7-paramedic1-a.wav', D + 0.15, 4.1, 4.7, 'paramedic1', 'Fifty over twen-')]
RADIO = ('vox-constable', 'pl-r7-constable-b-radio.wav', K + 0.2, 0.0, 3.5, 'constable', "Constable ninety-seven. Junction's blocked, ready for the VIP.")
MINISTER = ('vox-minister', 'pl-r7-minister-d.wav', C + 0.2, 0.0, 2.9, 'minister', "Hey Jeffrey, what time's the plane to the island?")
MINISTER_2 = ('vox-minister', 'pl-r7-minister-d.wav', C + 0.2 + 2.9 + 0.4, 3.7, 5.2, 'minister', "I'm on my way to fetch Andrew.")
FLAT = D + 0.9
# Effects: (stem, key, at, dur, gain dB, loop)
EFX = [('sfx-cabin', 'cabin', 0.0, K, -10, True),
       ('sfx-siren', 'siren', 0.0, B + 0.15, -8, True),
       ('sfx-monitor', 'monitor', 0.0, K, -9, True),
       ('sfx-cars', 'passby', K + 0.6, 3.0, -9, False),
       ('sfx-cars', 'stop', B - 0.1, 2.0, -6, False),
       ('sfx-cars', 'passby', B + 0.4, 2.2, -11, False),
       ('sfx-cabin', 'cabin', D, 3.0, -14, True),
       ('sfx-monitor', 'flatline', FLAT, E + LOGO_AT - FLAT, -12, True)]


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


def finish(path):
    tmp = path.with_suffix('.fin.mp4')
    subprocess.run([str(REPO / 'scripts/shorts/priority_lane_finish.sh'), FINISH, str(path), str(tmp)], check=True)
    tmp.replace(path)


def main():
    vf = (f'scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},fps={FPS},'
          "scale=in_range=full:out_range=limited,format=yuv420p,lutyuv=y='clip(val,18,229)':u='clip(val,16,240)':v='clip(val,16,240)'")
    # the clip(...) pass: the Held shot's headlights still read as full-range whites after the scale (delivery-qc FAIL)
    enc = ['-c:v', 'libx264', '-preset', 'veryfast', '-crf', '18', '-color_range', 'tv', '-colorspace', 'bt709',
           '-color_primaries', 'bt709', '-color_trc', 'bt709']
    parts = []
    for i, (beat, clip, tin, d) in enumerate(SHOTS):
        out = CUT / f'v{i}-{beat}{"-transition" if clip == "TRANSITION" else ""}.mp4'
        if clip == 'TRANSITION':
            # Poster: a slow push centred on his face. Car: starts zoomed so his face lands on the poster face, then
            # eases out (smoothstep over 0.8 s) to the clip's own framing, the face gliding to where it really sits.
            z0 = SCALE * P_PUSH
            pz = f"1+{P_PUSH - 1}*min(1,it/{P_DUR})"
            pzp = (f"zoompan=z='{pz}':x='{P_HEAD[0]}*iw-{P_HEAD[0]}*iw/zoom':y='{P_HEAD[1]}*ih-{P_HEAD[1]}*ih/zoom'"
                   f":d=1:s={W}x{H}:fps={FPS}")
            e = f"(1-(3*pow(min(1,it/0.8),2)-2*pow(min(1,it/0.8),3)))"
            cz = f"1+{z0 - 1}*{e}"
            px = f"({C_HEAD[0]}-({C_HEAD[0]}-{P_HEAD[0]})*(zoom-1)/{z0 - 1})"
            py = f"({C_HEAD[1]}-({C_HEAD[1]}-{P_HEAD[1]})*(zoom-1)/{z0 - 1})"
            czp = (f"zoompan=z='{cz}':x='{C_HEAD[0]}*iw-{px}*iw/zoom':y='{C_HEAD[1]}*ih-{py}*ih/zoom'"
                   f":d=1:s={W}x{H}:fps={FPS}")
            big = f'scale={2 * W}:{2 * H}:force_original_aspect_ratio=increase,crop={2 * W}:{2 * H},fps={FPS},setsar=1,'
            ff('-loop', '1', '-framerate', FPS, '-t', P_DUR, '-i', POSTER, '-ss', 0.0, '-t', C_DUR, '-i', VID / CAR_STILL,
               '-filter_complex', f"[0]{big}{pzp},setsar=1,format=yuv420p[p];[1]{big}{czp},setsar=1,format=yuv420p[c];"
               f"[p][c]xfade=transition=fade:duration={X_DUR}:offset={P_DUR - X_DUR},{vf}", '-t', d, '-an', *enc, out)
        elif beat == 'flatline':
            # Eased push into the screen (smoothstep), the screen's centre travelling to the frame's centre, then the logo on it.
            cx, cy = SCREEN[0] * W, SCREEN[1] * H
            pr = f"min(1,max(0,(it-{ZOOM_FROM})/{ZOOM_TO - ZOOM_FROM}))"
            z = f"1+{ZOOM - 1}*(3*pow({pr},2)-2*pow({pr},3))"
            zp = (f"zoompan=z='{z}':x='({W / 2}+({cx}-{W / 2})*(zoom-1)/{ZOOM - 1})-iw/zoom/2'"
                  f":y='({H / 2}+({cy}-{H / 2})*(zoom-1)/{ZOOM - 1})-ih/zoom/2':d=1:s={W}x{H}:fps={FPS}")
            pre = f'scale={2 * W}:{2 * H}:force_original_aspect_ratio=increase,crop={2 * W}:{2 * H},fps={FPS},'
            zp = zp.replace(f'{W / 2}', f'{W}').replace(f'{H / 2}', f'{H}').replace(f'{cx}', f'{2 * cx}').replace(f'{cy}', f'{2 * cy}')
            ff('-loop', '1', '-framerate', FPS, '-t', d, '-i', STILL, '-filter_complex', f"[0]{pre}{zp},{vf}", '-t', d, '-an', *enc, out)
            if FINISH: finish(out)
        elif beat == 'end':
            # The Flow trace, (finish), then the official logo laid on once the line is flat. The logo is never filtered.
            src = CUT / 'end-src.mp4'
            ff('-ss', tin, '-t', d, '-i', VID / clip, '-an', '-vf', vf, *enc, src)
            if FINISH: finish(src)
            ff('-i', src, '-i', LOGO, '-filter_complex',
               f"[1]scale=560:-1,format=rgba,loop=-1:size=1,fps={FPS},trim=0:{d + 0.5},setpts=N/{FPS}/TB,"
               f"fade=t=in:st={LOGO_AT}:d=0.4:alpha=1[l];[0][l]overlay=(W-w)/2:H*0.36-h/2:eof_action=pass,format=yuv420p",
               '-t', d, '-an', *enc, out)
        elif clip in SPEED:
            ff('-ss', tin, '-t', d * SPEED[clip], '-i', VID / clip, '-an', '-vf', f'setpts=PTS/{SPEED[clip]},{vf}', '-t', d, *enc, out)
        else:
            ff('-ss', tin, '-t', d, '-i', VID / clip, '-an', '-vf', vf, *enc, out)
            if FINISH: finish(out)
        parts.append(out)
    (CUT / 'list.txt').write_text(''.join(f"file '{p.name}'\n" for p in parts))
    ff('-f', 'concat', '-safe', '0', '-i', CUT / 'list.txt', '-c', 'copy', CUT / 'picture.mp4')

    stems, events = {}, []
    for stem, f, at, a0, a1, who, text in LINES:
        cut = (a1 - a0) if a1 else None
        stems.setdefault(stem, []).append((CAST / f, at, cut, 0, False, f'atrim=start={a0},asetpts=PTS-STARTPTS' if a0 else ''))
        dur = cut or float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', CAST / f],
                                          capture_output=True, text=True).stdout)
        events.append({'stem': stem, 't': round(at, 2), 'dur': round(dur, 2), 'what': f'{who}: {text}', 'src': str(CAST / f), 'who': who, 'text': text})
    # The minister through the car glass; the constable on a police radio (stand-in voice, Iapetus).
    glass = 'highpass=f=160,lowpass=f=2400'
    radio = 'volume=1dB'   # round 6: the constable's take is already through the radio filter (priority_lane_cast_r7.sh)
    for (stem, f, at, a0, a1, who, text), filt in ((MINISTER, glass), (MINISTER_2, glass), (RADIO, radio)):
        stems.setdefault(stem, []).append((CAST / f, at, a1 - a0, 0, False, f'atrim=start={a0},asetpts=PTS-STARTPTS,{filt}'))
        events.append({'stem': stem, 't': round(at, 2), 'dur': round(a1 - a0, 2), 'what': f'{who}: {text}', 'src': str(CAST / f), 'who': who, 'text': text})
    for stem, key, at, d, g, loop in EFX:
        src = racing_monitor(SFX[key], d) if key == 'monitor' else take(SFX[key])
        stems.setdefault(stem, []).append((src, at, d, g, False if key == 'monitor' else loop, ''))
        events.append({'stem': stem, 't': round(at, 2), 'dur': round(d, 2), 'what': f'{key} (Suno Sounds {SFX[key]}' + (', one beep laid at a quickening rate)' if key == 'monitor' else ')'), 'src': str(src)})
    # Score: from the top, stops dead on the flatline (Jack's brief: no music over the flatline).
    sc = take(SCORE)
    stems['music-score'] = [(sc, 0.0, FLAT, -7, False, '')]
    events.append({'stem': 'music-score', 't': 0.0, 'dur': round(FLAT, 2), 'what': f'score (Suno r6 {SCORE}), cut dead on the flatline', 'src': str(sc)})

    order = ['vox-paramedic1', 'vox-paramedic2', 'vox-driver', 'vox-constable', 'vox-minister', 'music-score', 'sfx-siren', 'sfx-monitor', 'sfx-cars', 'sfx-cabin']
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

    SEE = {'losing': 'Inside the ambulance (LS18-b); out to his SAVE OUR NHS poster at the bus stop as the ambulance races past (PB18-a), then back inside.',
           'cordon': 'High over the junction (CD18-a): police hold every side, the convoy crosses; the radio: junction blocked for the VIP.',
           'held': 'From the cab (HD19-b): the officer holds his glove up; the convoy crosses beyond him.',
           'motorcade': 'The minister in the back of his car (BM18-a), on the phone, through the glass.',
           'flatline': 'The monitor (FL18-a): the trace flat; we push into the screen.',
           'end': 'Cut to the flatline end card (Flow, LG20-a): two last beats, then flat, and the BadCode logo comes up.'}
    TITLES = {'losing': 'A. Losing him', 'cordon': 'A3. The cordon', 'held': 'B. Held', 'motorcade': 'C. The motorcade', 'flatline': 'D. Flatline', 'end': 'E. The flatline logo'}
    beats = []
    for beat in ('losing', 'cordon', 'held', 'motorcade', 'flatline', 'end'):
        st, d = BEAT_AT[beat], BEAT_DUR[beat]
        bl = [{'i': j, 'who': e['who'], 'name': e['who'].title(), 't': e['t'], 'dur': e['dur'], 'text': e['text'], 'by': 'kai' if e['who'] in ('constable', 'minister') or (j == 0 and beat == 'losing') else 'claude'}
              for j, e in enumerate(e for e in events if 'who' in e and st <= e['t'] < st + d)]
        beats.append({'id': beat, 'title': TITLES[beat], 'start': st, 'dur': d, 'see': SEE[beat], 'lines': bl})
    edl = {'sequence': 'shorts-1-priority-lane-r6', 'title': 'Priority Lane Timeline',
           'heading': 'BadCode Shorts ▲ Priority Lane, rough cut 6' + (f' ({FINISH} finish)' if FINISH else ''),
           'intro': ('Rough cut 6: every voice recast (your round 6-7 picks; the driver angry), the percussion score (c2), your two '
                     'picture notes fixed (inside the ambulance with the doors shut; the minister not eating), and the flatline end card '
                     'made in Flow: the monitor push-in cuts to the trace going flat, then the logo. '
                     + (f'Finish: {FINISH}.' if FINISH else 'No filter yet: pick one on the picks page.') + ' Note anything.'),
           'fps': FPS, 'total': TOTAL, 'beats': beats,
           # The flatline shot carries its push-in and the logo baked in (v3-flatline.mp4), so Premiere gets the finished shot.
           'video': [{'file': str(CUT / f'v{i}-{s[0]}.mp4') if s[0] in ('flatline', 'end') else str(VID / s[1]),
                      'in': 0.0 if s[0] in ('flatline', 'end') else s[2], 'start': starts[i], 'dur': s[3], 'beat': s[0],
                      'source': str(STILL) if s[1] == 'STILL' else str(VID / s[1]), 'looped': False}
                     for i, s in enumerate(SHOTS)],
           'audio': audio,
           'events': [{k: v for k, v in e.items() if k not in ('who', 'text')} for e in events],
           'flags': [f'Runs {TOTAL:.1f} s, about 3 s longer than round 5: the flatline end card is a shot of its own now.',
                     'Voices: plain reads on gemini-3.8-flash-tts (the driver with the style "angry, shouting"), cut at the word gaps.',
                     'The minister is not lip-synced: the clip mouths generic talk and the line plays through the glass.',
                     'The flatline still (FL18-a) keeps its push-in, now without the logo; the logo is on the end card.']}
    (CUT / 'edl.json').write_text(json.dumps(edl, indent=1, ensure_ascii=False))
    print(json.dumps({'total': TOTAL, 'starts': starts, 'preview': str(CUT / 'preview.mp4')}))


if __name__ == '__main__':
    main()
