#!/usr/bin/env python3
"""Sponsor a Chancellor (BadCode Short): rough cut 1 (2026-11-11).

    python3 scripts/shorts/sponsor_chancellor_cut.py

9:16. A: the black-and-white appeal (01-A then the chained 01-B) under the narration (Achernar, nar-c), its long pauses
tightened (never sped). B: her flat (02). C: the doormat (03). D: the nan reads the flyer, "Poor bastard..."
(Vindemiatrix, nan-b, lip-synced onto 04-r2 by scripts/lipsync/place-dub.py, dub/04-r2-nan.json).
A1 = narrator, A2 = nan, A3 = each clip's own Omni ambience (04-r2's own "Poor bloke" muted out).
Writes <media>/cut/edl.json (timeline format, scripts/scene/timeline.py), the stems, overlay.mov and preview.mp4.
"""
import json, pathlib, subprocess, sys

REPO = pathlib.Path(__file__).resolve().parents[2]
SCENE = REPO / 'docs/stories/short-sponsor-a-chancellor/scenes/sponsor-a-chancellor'
sys.path.insert(0, str(REPO / 'scripts/drive'))
from localmap import localize  # noqa: E402

cfg = localize(json.loads((SCENE / 'scene.json').read_text()))
MEDIA = pathlib.Path(cfg['media'])
VID, AUD = MEDIA / 'video', MEDIA / 'audio'
CUT = MEDIA / 'cut'; CUT.mkdir(parents=True, exist_ok=True)
NAR = AUD / 'casting/nar-c-achernar.wav'
NAN_DUB = AUD / 'dub/sac-04-r2-nan-dub.wav'          # on clip 04-r2's own clock: voice 2.41-2.80, 3.70-4.95
LOGO = REPO / 'docs/brand/logo'
W, H, FPS = 1080, 1920, 24
LEAD = 0.4
SFX_LUFS = -30
FONT = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'

# Narration phrases, measured (silencedetect -40 dB): (from, to, gap after)
NAR_PH = [(0.40, 2.06, 0.50, 'This is Crispin.'),
          (3.25, 7.18, 0.60, 'Crispin only earns £100,000 a year.'),
          (8.58, 9.22, 0.25, 'Tonight,'),
          (9.98, 13.06, 0.60, 'his second home has no second home.'),
          (14.78, 16.68, 0.25, 'For just £3 a month,'),
          (17.37, 19.08, 0.0, 'you can help.')]
nar_at, t = [], LEAD
for f, to, gap, _ in NAR_PH:
    nar_at.append(round(t, 3)); t += (to - f) + gap
NAR_END = t
D_IN, D_OUT = 0.6, 6.0                                 # 04-r2: mouth 2.38-4.13, then she holds

# (beat, clip, in, dur)
SHOTS = [('appeal', 'sac-01-A-AP1-b.mp4', 0.0, 8.0),
         ('appeal', 'sac-01-B-AP1-b-end.mp4', 0.04, round(NAR_END + 0.5 - 8.0, 3)),
         ('room', 'sac-02-RM2-b-a.mp4', 1.0, 2.0),
         ('post', 'sac-03-PO2-b-b.mp4', 0.8, 2.8),
         ('nan', 'sac-04-r2-NA1-a.mp4', D_IN, D_OUT - D_IN)]
starts, t = [], 0.0
for s in SHOTS: starts.append(round(t, 3)); t += s[3]
TOTAL = round(t, 3)
T_CARD = nar_at[4]                                     # the "£3 a month" band comes up on "For just £3 a month"
SEE = {'appeal': 'The black-and-white charity appeal: Crispin at the rainy conservatory glass, a slow blink, his hand slides down the pane.',
       'room': 'Pull back: the nan in her armchair in the cold flat, the telly on.',
       'post': 'The doormat: junk mail, a draught, the SPONSOR A CHANCELLOR flyer.',
       'nan': 'She reads the flyer and pities him (lip-synced).'}
TITLES = {'appeal': 'A. The appeal', 'room': 'B. Her flat', 'post': 'C. The junk mail', 'nan': 'D. Poor bastard'}


def ff(*a):
    subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', *map(str, a)], check=True)


def ms(x):
    return int(round(x * 1000))


ENC = ['-c:v', 'libx264', '-preset', 'veryfast', '-crf', '18', '-pix_fmt', 'yuv420p', '-color_range', 'tv',
       '-colorspace', 'bt709', '-color_primaries', 'bt709', '-color_trc', 'bt709']


def main():
    parts, sfx_parts = [], []
    for i, (beat, clip, tin, d) in enumerate(SHOTS):
        out = CUT / f'v{i}-{beat}.mp4'
        ff('-ss', tin, '-t', d, '-i', VID / clip, '-an', '-vf',
           f'scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},fps={FPS},scale=in_range=full:out_range=limited,format=yuv420p', *ENC, out)
        parts.append(out)
        sp = CUT / f's{i}-{beat}.wav'
        mute = f",volume=enable='between(t,{2.2 - tin:.2f},{4.4 - tin:.2f})':volume=0" if beat == 'nan' else ''
        ff('-ss', tin, '-t', d, '-i', VID / clip, '-vn', '-af',
           f'loudnorm=I={SFX_LUFS}:TP=-6{mute},afade=t=in:d=0.08,afade=t=out:st={d - 0.08}:d=0.08', '-ar', 48000, '-ac', 2, sp)
        sfx_parts.append(sp)
    (CUT / 'list.txt').write_text(''.join(f"file '{p.name}'\n" for p in parts))
    ff('-f', 'concat', '-safe', '0', '-i', CUT / 'list.txt', '-c', 'copy', CUT / 'picture-raw.mp4')

    # Overlay (also its own alpha layer for Premiere V2): the appeal's "£3 a month" band, and the logo end card.
    logo = OVL_LOGO()
    band = (f"drawbox=x=0:y=1500:w={W}:h=260:color=black@0.85:t=fill:enable='between(t,{T_CARD:.2f},{NAR_END + 0.5:.2f})',"
            f"drawtext=fontfile={FONT}:text='SPONSOR A CHANCELLOR':fontcolor=white:fontsize=64:x=(w-text_w)/2:y=1540:enable='between(t,{T_CARD:.2f},{NAR_END + 0.5:.2f})',"
            f"drawtext=fontfile={FONT}:text='Just £3 a month':fontcolor=white:fontsize=58:x=(w-text_w)/2:y=1640:enable='between(t,{T_CARD + 0.4:.2f},{NAR_END + 0.5:.2f})'")
    t_logo = TOTAL - 1.2
    ff('-i', CUT / 'picture-raw.mp4', '-i', logo, '-filter_complex',
       f"[0]{band}[b];[1]format=rgba[l];[b][l]overlay=(W-w)/2:H-h-260:enable='gte(t,{t_logo:.2f})',scale=in_range=full:out_range=limited,format=yuv420p[v]",
       '-map', '[v]', *ENC, CUT / 'picture.mp4')
    ff('-f', 'lavfi', '-i', f'color=c=black@0.0:s={W}x{H}:r={FPS}:d={TOTAL},format=rgba', '-i', logo, '-filter_complex',
       f"[0]{band}[b];[1]format=rgba[l];[b][l]overlay=(W-w)/2:H-h-260:format=auto:enable='gte(t,{t_logo:.2f})'[o]",
       '-map', '[o]', '-t', TOTAL, '-c:v', 'prores_ks', '-profile:v', '4444', '-pix_fmt', 'yuva444p10le', '-alpha_bits', '16', CUT / 'overlay.mov')

    (CUT / 'slist.txt').write_text(''.join(f"file '{p.name}'\n" for p in sfx_parts))
    sfx = CUT / 'sfx-world.wav'
    ff('-f', 'concat', '-safe', '0', '-i', CUT / 'slist.txt', '-af', f'apad=whole_dur={TOTAL}', '-ar', 48000, '-ac', 2, sfx)
    nar = CUT / 'vox-narrator.wav'
    fc = ';'.join(f'[0]atrim={f}:{to},asetpts=PTS-STARTPTS,adelay=delays={ms(a)}:all=1[n{k}]' for k, ((f, to, _, _), a) in enumerate(zip(NAR_PH, nar_at)))
    fc += ';' + ''.join(f'[n{k}]' for k in range(len(NAR_PH))) + f'amix=inputs={len(NAR_PH)}:normalize=0,loudnorm=I=-18:TP=-2,apad=whole_dur={TOTAL}'
    ff('-i', NAR, '-filter_complex', fc, '-ar', 48000, '-ac', 2, nar)
    nan = CUT / 'vox-nan.wav'
    ff('-i', NAN_DUB, '-af', f'atrim={D_IN}:{D_OUT},asetpts=PTS-STARTPTS,adelay=delays={ms(starts[4])}:all=1,apad=whole_dur={TOTAL}',
       '-ar', 48000, '-ac', 2, nan)
    ff('-i', CUT / 'picture.mp4', '-i', nar, '-i', nan, '-i', sfx, '-filter_complex', '[1:a][2:a][3:a]amix=inputs=3:normalize=0[a]',
       '-map', '0:v', '-map', '[a]', '-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k', '-t', TOTAL, CUT / 'preview.mp4')

    script = json.loads((SCENE / 'script.json').read_text())
    lines = {b['id']: b['lines'] for b in script['beats']}
    nan_t = starts[4] + 2.41 - D_IN
    vt = {'appeal': [(nar_at[0], NAR_PH[0][1] - NAR_PH[0][0]), (nar_at[1], NAR_PH[1][1] - NAR_PH[1][0]),
                     (nar_at[2], nar_at[5] + NAR_PH[5][1] - NAR_PH[5][0] - nar_at[2])],
          'nan': [(nan_t, 4.95 - 2.41)]}
    beats, seen = [], set()
    for i, (beat, clip, tin, d) in enumerate(SHOTS):
        if beat in seen:
            beats[-1]['dur'] = round(beats[-1]['dur'] + d, 3); continue
        seen.add(beat)
        bl = []
        for j, ln in enumerate(lines.get(beat, [])):
            tt, dd = vt[beat][min(j, len(vt[beat]) - 1)]
            bl.append({'i': j, 'who': ln['who'].lower(), 'name': ln['who'].title(), 't': round(tt, 2), 'dur': round(dd, 2),
                       'text': ln['text'], 'by': ln.get('by', 'claude')})
        beats.append({'id': beat, 'title': TITLES[beat], 'start': starts[i], 'dur': d, 'see': SEE[beat], 'lines': bl})
    edl = {'sequence': 'short-sponsor-a-chancellor-r1', 'title': 'Sponsor a Chancellor Timeline',
           'heading': 'BadCode Shorts ▲ Sponsor a Chancellor, rough cut 1',
           'intro': 'All five clips with the picked voices (narrator: Achernar; nan: Vindemiatrix, lip-synced). Note anything: a beat, a shot, a line, a sound, or a single frame.',
           'fps': FPS, 'total': TOTAL, 'beats': beats,
           'video': [{'file': str(VID / s[1]), 'in': s[2], 'start': starts[i], 'dur': s[3], 'beat': s[0], 'source': str(VID / s[1]), 'looped': False}
                     for i, s in enumerate(SHOTS)],
           'audio': [{'track': 'A1', 'name': 'vox-narrator', 'file': str(nar)}, {'track': 'A2', 'name': 'vox-nan', 'file': str(nan)},
                     {'track': 'A3', 'name': 'sfx-world', 'file': str(sfx)}],
           'events': [{'stem': 'vox-narrator', 't': a, 'dur': round(to - f, 2), 'what': txt, 'src': str(NAR)} for (f, to, _, txt), a in zip(NAR_PH, nar_at)]
                     + [{'stem': 'vox-nan', 't': round(nan_t, 2), 'dur': 2.54, 'what': 'Poor bastard... (lip-synced)', 'src': str(NAN_DUB)}]
                     + [{'stem': 'sfx-world', 't': starts[i], 'dur': s[3], 'what': f"{s[0]}: clip's own ambience", 'src': str(VID / s[1])} for i, s in enumerate(SHOTS)],
           'flags': [f'Runs {TOTAL:.1f} s: the appeal is {NAR_END + 0.5:.1f} s of it (the narration with its pauses tightened, not sped).',
                     "Her telly is side-on in 02, so the advert can't be seen on it: the pull-back is a plain cut for now.",
                     'No letterbox clatter or sad charity piano yet (sound.md has no music); the "£3 a month" band and logo are placeholder ffmpeg text.']}
    (CUT / 'edl.json').write_text(json.dumps(edl, indent=1, ensure_ascii=False))
    print(json.dumps({'total': TOTAL, 'starts': starts, 'nar_end': round(NAR_END, 2), 'preview': str(CUT / 'preview.mp4')}))


def OVL_LOGO():
    for name in ('badcode-lockup-reversed-420.png',):
        p = MEDIA.parent / 'priority-lane/overlay' / name
        if p.exists():
            return p
    raise SystemExit('logo not found')


if __name__ == '__main__':
    main()
