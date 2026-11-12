#!/usr/bin/env python3
"""Hello, I'm BadCode (BadCode Short #17): rough cut 1 (2026-11-12).

    python3 scripts/shorts/hello_cut.py

9:16. Jack's structure (2026-11-12): warm hook "Hello. I'm from the future." → the masked figure "It didn't go
well." → a rapid-fire horror reel of real footage (free, licence-checked: docs/footage/) and Flow stills for the
gaps, to cinematic music → the music slows to nothing → black, "Here's what to do next." → the BadCode logo.

ROUGH: the voice (Sadaltager, temp profile) and the music (ffmpeg synth) are placeholders until voice casting and
a Suno round; the hook and figure stills are placeholders until Jack picks. Working files go in cut/_scratch
(shorts-release §1a). Writes <media>/cut/edl.json (timeline format), stems and preview.mp4.
"""
# style-lint: story=short-hello-im-badcode (this cut script belongs to one short)
import json, pathlib, subprocess, sys

REPO = pathlib.Path(__file__).resolve().parents[2]
SCENE = REPO / 'docs/stories/short-hello-im-badcode/scenes/hello'
sys.path.insert(0, str(REPO / 'scripts/drive'))
from localmap import localize  # noqa: E402

cfg = localize(json.loads((SCENE / 'scene.json').read_text()))
MEDIA = pathlib.Path(cfg['media'])
MB, FC, FN = MEDIA / 'moodboard', MEDIA / 'footage/commons', MEDIA / 'footage/nasa'
VO = MEDIA / 'audio/temp'
CUT = MEDIA / 'cut'; CUT.mkdir(parents=True, exist_ok=True)
WORK = CUT / '_scratch'; WORK.mkdir(exist_ok=True)
LOGO = REPO / 'docs/brand/logo/badcode-stacked-reversed-2400.png'
W, H, FPS = 1080, 1920, 24
REEL = 0.5    # one flash. 0.38 s FAILED the photosensitivity gate (4 flashes/s): hard cuts between unlike pictures count

# The reel, the four themes Jack asked for (AI, climate, cost of living, war) interleaved, ordered as one descent from
# bright to dark (measured YAVG 129 → 16) so neighbouring cuts don't strobe: rough 1 in random order FAILED the
# photosensitivity gate (4 flashes/s at 8.8 s). The descent also lands in the black.
# (key, kind, source, in, credit)   kind: v = video segment, s = still push-in, f = Flow still (AI-made)
SHOTS = [
    ('pylons', 'f', MB / 'R-pylons.jpg', 0, None),
    ('burnt', 'v', FC / 'lahaina-broll.webm', 48.5, 'FEMA (public domain)'),
    ('flood', 'v', FC / 'lagrange-flood.webm', 45.5, 'Colton Brugger, CC BY 3.0'),
    ('ashburn', 's', FC / 'ashburn-dcs.jpg', 0, 'Wikimedia Commons (CC0)'),
    ('ruins', 'v', FC / 'lahaina-broll.webm', 744.5, 'FEMA (public domain)'),
    ('nsa', 's', FC / 'nsa-utah-dc.jpg', 0, 'EFF (CC0)'),
    ('car', 'v', FC / 'lahaina-broll.webm', 240.5, 'FEMA (public domain)'),
    ('cables', 'v', FN / 'aitken-large.mp4', 104.5, 'NASA (public domain)'),
    ('racks', 'v', FN / 'aitken-large.mp4', 120.5, 'NASA (public domain)'),
    ('tornado', 'v', FC / 'elreno-tornado.webm', 2.0, 'Ray Bohac, CC BY 3.0'),
    ('tornado2', 'v', FC / 'elreno-tornado.webm', 102.0, 'Ray Bohac, CC BY 3.0'),
    ('highstreet', 'f', MB / 'R-highstreet.jpg', 0, None),
    ('drone', 'f', MB / 'R-drone.jpg', 0, None),
    ('robotarm', 's', FC / 'nersc-robot-arm.jpg', 0, 'Derrick Coetzee (CC0)'),
    ('meter', 'f', MB / 'R-meter.jpg', 0, None),
    ('foodbank', 'f', MB / 'R-foodbank.jpg', 0, None),
    ('dcbuild', 'f', MB / 'R-dcbuild.jpg', 0, None),
    ('eaton', 'v', FC / 'eaton-firestorm.webm', 0.3, 'USDA Forest Service (public domain)'),
    ('missile', 'f', MB / 'R-missile.jpg', 0, None),
    ('robots', 'f', MB / 'R-robots.jpg', 0, None),
    ('fermilab', 's', FC / 'fermilab-racks.jpg', 0, 'Fermilab / US DOE (public domain)'),
    ('embers', 'v', FC / 'eaton-firestorm.webm', 4.5, 'USDA Forest Service (public domain)'),
]
HOOK, HOOK_D = MB / 'A3-a.jpg', 4.0      # placeholder: Frutiger Aero bubble meadow
FIG, FIG_D = MB / 'B3-b.jpg', 2.9        # placeholder: the figure at the 2016 festival
SLOW = 1.2                               # the last reel shots slow down with the music
BLACK_D, LOGO_D = 3.6, 2.2

ENC = ['-c:v', 'libx264', '-preset', 'veryfast', '-crf', '20', '-pix_fmt', 'yuv420p', '-color_range', 'tv',
       '-colorspace', 'bt709', '-color_primaries', 'bt709', '-color_trc', 'bt709']
FILL = f'scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H}'
GRADE = 'eq=contrast=1.12:saturation=0.8:brightness=-0.02,noise=alls=10:allf=t'


def ff(*a):
    subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', *map(str, a)], check=True)


def push(src, out, d, z0=1.0, z1=1.08, grade=True):
    n = max(2, round(d * FPS))
    vf = (f'{FILL},scale={W * 2}:{H * 2},zoompan=z=\'{z0}+({z1}-{z0})*on/{n}\':x=\'iw/2-(iw/zoom/2)\':y=\'ih/2-(ih/zoom/2)\''
          f':d={n}:s={W}x{H}:fps={FPS}' + (f',{GRADE}' if grade else '') + ',format=yuv420p')
    ff('-loop', 1, '-t', d + 0.2, '-i', src, '-vf', vf, '-frames:v', n, *ENC, out)


def seg(src, tin, out, d, speed=1.0):
    crop = 'crop=iw:ih*0.86:0:0,' if 'lagrange' in src.name else ''   # above the county's burned-in banner
    slow = f',setpts={1 / speed:.3f}*PTS' if speed != 1 else ''
    ff('-ss', tin, '-t', d * speed + 0.1, '-i', src, '-an', '-vf', f'{crop}{FILL},fps={FPS}{slow},{GRADE},format=yuv420p',
       '-t', d, *ENC, out)


def main():
    parts, starts, beats_t = [], [], {}
    t = 0.0

    def add(path, d, beat):
        nonlocal t
        parts.append(path); starts.append(round(t, 3)); beats_t.setdefault(beat, round(t, 3)); t += d

    push(HOOK, WORK / 'p00-hook.mp4', HOOK_D, 1.0, 1.06, grade=False); add(WORK / 'p00-hook.mp4', HOOK_D, 'hello')
    push(FIG, WORK / 'p01-fig.mp4', FIG_D, 1.04, 1.12, grade=False); add(WORK / 'p01-fig.mp4', FIG_D, 'figure')
    reel_rows = []
    for i, (key, kind, src, tin, credit) in enumerate(SHOTS):
        last = i >= len(SHOTS) - 3
        d = REEL + (SLOW / 3 if last else 0)            # the reel decelerates into the silence
        out = WORK / f'p{i + 2:02d}-{key}.mp4'
        if kind == 'v':
            seg(src, tin, out, d, speed=0.5 if last else 1.0)
        else:
            push(src, out, d, 1.0, 1.10)
        add(out, d, 'horror'); reel_rows.append((key, kind, src, tin, credit, starts[-1], d))
    reel_end = t
    ff('-f', 'lavfi', '-i', f'color=c=black:s={W}x{H}:r={FPS}:d={BLACK_D}', *ENC, WORK / 'p90-black.mp4'); add(WORK / 'p90-black.mp4', BLACK_D, 'button')
    ff('-f', 'lavfi', '-i', f'color=c=black:s={W}x{H}:r={FPS}:d={LOGO_D}', '-loop', 1, '-t', LOGO_D, '-i', LOGO, '-filter_complex',
       '[1]scale=640:-1[l];[0][l]overlay=(W-w)/2:(H-h)/2,fade=t=in:d=0.4,format=yuv420p', *ENC, '-t', LOGO_D, WORK / 'p91-logo.mp4')
    add(WORK / 'p91-logo.mp4', LOGO_D, 'button')
    TOTAL = round(t, 3)
    (WORK / 'list.txt').write_text(''.join(f"file '{p.name}'\n" for p in parts))
    ff('-f', 'concat', '-safe', '0', '-i', WORK / 'list.txt', '-c', 'copy', WORK / 'picture.mp4')

    # Voice (temp): line 1 on the hook, line 2 on the figure, line 3 in the black after the music has died.
    t_l1, t_l2, t_l3 = 0.35, beats_t['figure'] + 0.15, reel_end + 0.9
    vox = CUT / 'vox-badcode.wav'
    ff('-i', VO / 'vo-l1.wav', '-i', VO / 'vo-l2.wav', '-i', VO / 'vo-l3.wav', '-filter_complex',
       f'[0]adelay={int(t_l1 * 1000)}:all=1[a];[1]adelay={int(t_l2 * 1000)}:all=1[b];[2]adelay={int(t_l3 * 1000)}:all=1[c];'
       f'[a][b][c]amix=inputs=3:normalize=0,loudnorm=I=-16:TP=-1.5,apad=whole_dur={TOTAL}', '-ar', 48000, '-ac', 2, '-t', TOTAL, vox)

    # Music (TEMP, synthesised): a warm pad on the hook, a cold drone under the figure, the reel's drone with a hit on
    # every cut, then it slows and sinks to nothing before "Here's what to do next."
    mus = CUT / 'mus-temp.wav'
    fig_t = beats_t['figure']
    hits = [r[5] for r in reel_rows]
    pad = f"aevalsrc='0.06*(sin(2*PI*261.6*t)+sin(2*PI*329.6*t)+sin(2*PI*392*t))*(1+0.3*sin(2*PI*0.5*t))':s=48000:d={TOTAL}"
    drone = f"aevalsrc='0.22*(sin(2*PI*55*t)+0.6*sin(2*PI*82.4*t)+0.4*sin(2*PI*58.3*t))':s=48000:d={TOTAL}"
    boom = "aevalsrc='0.9*sin(2*PI*48*t)*exp(-9*t)+0.25*(random(0)*2-1)*exp(-30*t)':s=48000:d=0.45"
    fc = [f"[0]afade=t=out:st={fig_t - 0.3}:d=0.4[pad]",
          f"[1]volume='if(lt(t,{fig_t}),0,if(lt(t,{reel_end - SLOW}),0.6+0.4*(t-{fig_t})/{reel_end - fig_t},1))':eval=frame,"
          f"lowpass=f=3000,afade=t=out:st={reel_end - SLOW}:d={SLOW + 0.15}[dr]"]
    ins = ['-f', 'lavfi', '-i', pad, '-f', 'lavfi', '-i', drone]
    for k, h in enumerate(hits):
        ins += ['-f', 'lavfi', '-i', boom]
        g = 1.0 if h < reel_end - SLOW else 0.5
        fc.append(f"[{k + 2}]volume={g},adelay={int(h * 1000)}:all=1[h{k}]")
    mix = '[pad][dr]' + ''.join(f'[h{k}]' for k in range(len(hits)))
    fc.append(f"{mix}amix=inputs={len(hits) + 2}:normalize=0,alimiter=limit=0.8,apad=whole_dur={TOTAL}[m]")
    ff(*ins, '-filter_complex', ';'.join(fc), '-map', '[m]', '-ar', 48000, '-ac', 2, '-t', TOTAL, mus)

    ff('-i', WORK / 'picture.mp4', '-i', vox, '-i', mus, '-filter_complex', '[1:a][2:a]amix=inputs=2:normalize=0[a]',
       '-map', '0:v', '-map', '[a]', '-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k', '-t', TOTAL, CUT / 'preview.mp4')

    credits = sorted({r[4] for r in reel_rows if r[4]})
    beats = [
        {'id': 'hello', 'title': 'A. "Hello. I\'m from the future."', 'start': 0, 'dur': HOOK_D,
         'see': 'Placeholder hook: Frutiger Aero bubble meadow (A3-a).', 'lines': [{'i': 0, 'who': 'badcode', 'name': 'BadCode (temp voice)', 't': t_l1, 'dur': 3.68, 'text': "Hello. I'm from the future.", 'by': 'kai'}]},
        {'id': 'figure', 'title': 'B. "It didn\'t go well."', 'start': fig_t, 'dur': FIG_D,
         'see': 'Placeholder figure: the masked figure at the 2016 festival (B3-b).', 'lines': [{'i': 0, 'who': 'badcode', 'name': 'BadCode (temp voice)', 't': t_l2, 'dur': 2.6, 'text': "It didn't go well.", 'by': 'kai'}]},
        {'id': 'horror', 'title': 'C. The horror reel', 'start': beats_t['horror'], 'dur': round(reel_end - beats_t['horror'], 3),
         'see': f'{len(SHOTS)} flashes: real footage (green, credited) and Flow stills for the gaps; slows into silence.', 'lines': []},
        {'id': 'button', 'title': 'D. "Here\'s what to do next." + logo', 'start': round(reel_end, 3), 'dur': round(TOTAL - reel_end, 3),
         'see': 'Black, the voice, then the BadCode logo.', 'lines': [{'i': 0, 'who': 'badcode', 'name': 'BadCode (temp voice)', 't': round(t_l3, 2), 'dur': 3.12, 'text': "Here's what to do next.", 'by': 'jack'}]},
    ]
    video = [{'file': str(parts[0]), 'in': 0, 'start': starts[0], 'dur': HOOK_D, 'beat': 'hello', 'source': str(HOOK), 'looped': False},
             {'file': str(parts[1]), 'in': 0, 'start': starts[1], 'dur': FIG_D, 'beat': 'figure', 'source': str(FIG), 'looped': False}]
    for (key, kind, src, tin, credit, st, d), p in zip(reel_rows, parts[2:]):
        video.append({'file': str(p), 'in': 0, 'start': st, 'dur': round(d, 3), 'beat': 'horror', 'source': str(src), 'looped': False,
                      'note': ('AI-made (Flow) still' if kind == 'f' else f'real footage, {credit}')})
    video += [{'file': str(parts[-2]), 'in': 0, 'start': starts[-2], 'dur': BLACK_D, 'beat': 'button', 'source': 'black', 'looped': False},
              {'file': str(parts[-1]), 'in': 0, 'start': starts[-1], 'dur': LOGO_D, 'beat': 'button', 'source': str(LOGO), 'looped': False}]
    edl = {'sequence': 'shorts-17-hello-im-badcode-r1', 'title': 'Hello Im BadCode Timeline',
           'heading': "BadCode Shorts ▲ Hello, I'm BadCode, rough cut 1",
           'intro': "Your structure: hook, the figure, a rapid-fire horror reel of real footage, the music dies, \"Here's what to do next.\", logo. "
                    'The voice and music are placeholders; the hook and figure stills are placeholders. Note anything.',
           'fps': FPS, 'total': TOTAL, 'beats': beats, 'video': video,
           'audio': [{'track': 'A1', 'name': 'vox-badcode', 'file': str(vox)}, {'track': 'A2', 'name': 'mus-temp', 'file': str(mus)}],
           'events': [{'stem': 'vox-badcode', 't': l['t'], 'dur': l['dur'], 'what': l['text'] + ' (temp voice)', 'src': str(VO)} for b in beats for l in b['lines']]
                     + [{'stem': 'mus-temp', 't': 0, 'dur': TOTAL, 'what': 'TEMP synth score: warm pad, drone with a hit on every cut, slows to nothing', 'src': 'ffmpeg'}],
           'flags': ['Voice is a temp Gemini voice (Sadaltager): cast it with voice-casting.', 'Music is a temp ffmpeg synth: a Suno round in this short\'s own sound is owed.',
                     'Hook (A3-a) and figure (B3-b) are placeholders; the figure\'s mask is to be fixed on the pick.',
                     'Footage credits owed in the description: ' + '; '.join(credits) + '.',
                     'Flow-made stills in the reel (high street, food bank, robots, drone, data-centre build, missile, pylons, meter) are AI images cut between real footage, never composited into it.']}
    (CUT / 'edl.json').write_text(json.dumps(edl, indent=1, ensure_ascii=False))
    print(json.dumps({'total': TOTAL, 'reel': [round(beats_t['horror'], 2), round(reel_end, 2)], 'preview': str(CUT / 'preview.mp4')}))


if __name__ == '__main__':
    main()
