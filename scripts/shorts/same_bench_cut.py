#!/usr/bin/env python3
"""Same Bench (BadCode Short #2): rough cut (2026-11-12).

    python3 scripts/shorts/same_bench_cut.py

9:16. Title card 1919 → A (he flicks the soldier away, lips never move) → title card 2026 → B (the same flick,
the nurse walks off) → C (hat tip, he turns to the empty seat) → caption "Same bench." → fade out.
The cards come from scripts/shorts/same_bench_dates.py (Jack's pick: title cards); the caption is laid in here,
never by Flow. A1 = the fat cat (Algenib, Jack's pick), one take split into its two lines; A2 = the clips' own sound.
Writes <media>/cut/edl.json (timeline format), stems and preview.mp4.
"""
# style-lint: story=short-same-bench (this cut script belongs to one short)
import json, pathlib, subprocess, sys

REPO = pathlib.Path(__file__).resolve().parents[2]
SCENE = REPO / 'docs/stories/short-same-bench/scenes/same-bench'
sys.path.insert(0, str(REPO / 'scripts/drive'))
from localmap import localize  # noqa: E402

cfg = localize(json.loads((SCENE / 'scene.json').read_text()))
MEDIA = pathlib.Path(cfg['media'])
VID, AUD, DATES = MEDIA / 'video', MEDIA / 'audio', MEDIA / 'dates'
CUT = MEDIA / 'cut'; CUT.mkdir(parents=True, exist_ok=True)
FONT = '/mnt/c/Windows/Fonts/BASKVILL.TTF'
VOICE = AUD / 'casting/cat-a-algenib.wav'
W, H, FPS = 1080, 1920, 24
SFX_LUFS = -34
CARD = 1.2

# (beat, kind, source, in, dur, line-or-None as (take_in, take_out, offset_in_shot, text))
# Round 2 (Jack, timeline r1, 2026-11-12: "it doesnt really convey the message"): a silent-film dialogue card with the
# ask before each "Forget it.", B and C re-rolled from his notes, the "Same bench." caption removed, the logo at the end.
CLIP_B = VID / ('sb-02-r2-B3-a.mp4' if (VID / 'sb-02-r2-B3-a.mp4').exists() else 'sb-02-B3-a.mp4')
CLIP_C = VID / ('sb-03-r2-C3-a.mp4' if (VID / 'sb-03-r2-C3-a.mp4').exists() else 'sb-03-C3-a.mp4')
LOGO = REPO / 'docs/brand/logo/badcode-stacked-reversed-2400.png'
SHOTS = [('card1919', 'card', DATES / 'card-1919.png', 0.0, 1.6, None),
         ('veteran-in', 'clip', VID / 'sb-01-A2-b.mp4', 0.0, 0.8, None),
         ('ask1919', 'card', DATES / 'card-say-1919.png', 0.0, 3.6, None),
         ('veteran', 'clip', VID / 'sb-01-A2-b.mp4', 0.8, 3.9, (0.20, 1.60, 0.15, 'Forget it.')),
         ('card2026', 'card', DATES / 'card-2026.png', 0.0, 1.6, None),
         ('nurse-in', 'clip', CLIP_B, 0.0, 0.8, None),
         ('ask2026', 'card', DATES / 'card-say-2026.png', 0.0, 3.6, None),
         ('nurse', 'clip', CLIP_B, 0.8, 3.9, (2.90, 4.40, 0.15, 'Forget it.')),
         ('button', 'clip', CLIP_C, 0.0, 4.4, None),
         ('logo', 'logo', LOGO, 0.0, 1.8, None)]
starts, t = [], 0.0
for s in SHOTS: starts.append(round(t, 3)); t += s[4]
TOTAL = round(t, 3)
SEE = {'card1919': 'Title card: 1919.', 'veteran-in': 'The soldier beside him on the bench.', 'ask1919': 'Dialogue card: "They promised us homes fit for heroes."',
       'veteran': 'He flicks the soldier away without moving his lips; the soldier limps out of the light.',
       'card2026': 'Title card: 2026.', 'nurse-in': 'The nurse beside him on the bench.', 'ask2026': 'Dialogue card: "You clapped for us every Thursday."',
       'nurse': 'The same flick; the nurse walks off towards the hospital.',
       'button': 'He tips his hat, then turns to the empty seat on the right, where they sat (mirrored).', 'logo': 'The BadCode logo and name.'}
TITLES = {'card1919': '1919', 'veteran-in': 'A. The soldier', 'ask1919': '"Homes fit for heroes."', 'veteran': 'A. "Forget it."',
          'card2026': '2026', 'nurse-in': 'B. The nurse', 'ask2026': '"You clapped for us…"', 'nurse': 'B. "Forget it."',
          'button': 'C. The next one', 'logo': 'BadCode'}


def ff(*a):
    subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', *map(str, a)], check=True)


ENC = ['-c:v', 'libx264', '-preset', 'veryfast', '-crf', '18', '-pix_fmt', 'yuv420p', '-color_range', 'tv',
       '-colorspace', 'bt709', '-color_primaries', 'bt709', '-color_trc', 'bt709']
FIT = f'scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},fps={FPS}'


def main():
    subprocess.run([sys.executable, str(REPO / 'scripts/shorts/same_bench_dates.py'), str(MEDIA)], check=True, capture_output=True)
    parts, world = [], []
    for i, (beat, kind, src, tin, d, _) in enumerate(SHOTS):
        out = CUT / f'v{i}-{beat}.mp4'
        if kind == 'logo':  # the real logo files (docs/brand), never drawn by Flow
            ff('-f', 'lavfi', '-i', f'color=c=0x0b0b0b:s={W}x{H}:r={FPS}:d={d}', '-loop', 1, '-t', d, '-i', src, '-filter_complex',
               f"[1]scale=640:-1[l];[0][l]overlay=(W-w)/2:(H-h)/2,fade=t=in:d=0.3,format=yuv420p", *ENC, '-t', d, out)
            sp = CUT / f's{i}-{beat}.wav'
            ff('-f', 'lavfi', '-i', 'anullsrc=r=48000:cl=stereo', '-t', d, sp)
        elif kind == 'card':  # a held card with projector flicker and moving grain, like the clips' stock
            ff('-loop', 1, '-t', d, '-i', src, '-vf',
               f"{FIT},noise=alls=18:allf=t,eq=brightness='0.025*sin(2*PI*9*t)',fade=t=in:d=0.12,fade=t=out:st={d - 0.12}:d=0.12,format=yuv420p", *ENC, out)
            sp = CUT / f's{i}-{beat}.wav'
            ff('-f', 'lavfi', '-i', f'anullsrc=r=48000:cl=stereo', '-t', d, sp)
        else:
            # Round 3 (Jack, timeline r2: "he should look to where a person would be like in the last two clips"):
            # C is mirrored so he turns to screen right, where the soldier and the nurse sat.
            flip = 'hflip,' if beat == 'button' else ''
            ff('-ss', tin, '-t', d, '-i', src, '-an', '-vf', f'{flip}{FIT},scale=in_range=full:out_range=limited,format=yuv420p', *ENC, out)
            sp = CUT / f's{i}-{beat}.wav'
            ff('-ss', tin, '-t', d, '-i', src, '-vn', '-af', f'loudnorm=I={SFX_LUFS}:TP=-6,afade=t=in:d=0.05,afade=t=out:st={d - 0.05}:d=0.05',
               '-ar', 48000, '-ac', 2, sp)
        parts.append(out); world.append(sp)
    (CUT / 'list.txt').write_text(''.join(f"file '{p.name}'\n" for p in parts))
    ff('-f', 'concat', '-safe', '0', '-i', CUT / 'list.txt', '-c', 'copy', CUT / 'picture-raw.mp4')
    ff('-i', CUT / 'picture-raw.mp4', '-c', 'copy', CUT / 'picture.mp4')

    (CUT / 'slist.txt').write_text(''.join(f"file '{p.name}'\n" for p in world))
    wst = CUT / 'sfx-world.wav'
    ff('-f', 'concat', '-safe', '0', '-i', CUT / 'slist.txt', '-af', f'apad=whole_dur={TOTAL}', '-ar', 48000, '-ac', 2, wst)
    vox = CUT / 'vox-fatcat.wav'
    fc, k = [], 0
    for i, s in enumerate(SHOTS):
        if s[5]:
            a, b, off, _ = s[5]
            fc.append(f'[0]atrim={a}:{b},asetpts=PTS-STARTPTS,afade=t=in:d=0.03,afade=t=out:st={b - a - 0.05}:d=0.05,'
                      f'adelay=delays={int((starts[i] + off) * 1000)}:all=1[d{k}]'); k += 1
    ff('-i', VOICE, '-filter_complex', ';'.join(fc) + ';' + ''.join(f'[d{j}]' for j in range(k)) +
       f'amix=inputs={k}:normalize=0,loudnorm=I=-16:TP=-1.5,apad=whole_dur={TOTAL}', '-ar', 48000, '-ac', 2, vox)
    ff('-i', CUT / 'picture.mp4', '-i', vox, '-i', wst, '-filter_complex', '[1:a][2:a]amix=inputs=2:normalize=0[a]',
       '-map', '0:v', '-map', '[a]', '-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k', '-t', TOTAL, CUT / 'preview.mp4')

    notes = SCENE / 'cut-notes.json'
    rnd = json.loads(notes.read_text()).get('round', 1) if notes.exists() else 1
    beats = []
    for i, s in enumerate(SHOTS):
        ln = []
        if s[5]:
            a, b, off, text = s[5]
            ln.append({'i': 0, 'who': 'fatcat', 'name': 'Fat cat', 't': round(starts[i] + off, 2), 'dur': round(b - a, 2), 'text': text, 'by': 'kai'})
        if s[0].startswith('ask'):
            ln.append({'i': 0, 'who': 'card', 'name': 'Dialogue card', 't': starts[i], 'dur': s[4], 'by': 'claude',
                       'text': 'They promised us homes fit for heroes.' if s[0] == 'ask1919' else 'You clapped for us every Thursday.'})
        beats.append({'id': s[0], 'title': TITLES[s[0]], 'start': starts[i], 'dur': s[4], 'see': SEE[s[0]], 'lines': ln})
    edl = {'sequence': f'shorts-2-same-bench-r{rnd}', 'title': 'Same Bench Timeline',
           'heading': f'BadCode Shorts ▲ Same Bench, rough cut {rnd}',
           'intro': 'Round 2 on your notes: a silent-film card with what each of them was promised before every "Forget it.", B and C re-rolled, no caption, the logo at the end. Note anything.',
           'fps': FPS, 'total': TOTAL, 'beats': beats,
           'video': [{'file': str(parts[i] if s[1] in ('card', 'logo') else s[2]), 'in': s[3], 'start': starts[i], 'dur': s[4], 'beat': s[0],
                      'source': str(s[2]), 'looped': False} for i, s in enumerate(SHOTS)],
           'audio': [{'track': 'A1', 'name': 'vox-fatcat', 'file': str(vox)}, {'track': 'A2', 'name': 'sfx-world', 'file': str(wst)}],
           'events': [{'stem': 'vox-fatcat', 't': l['t'], 'dur': l['dur'], 'what': 'Forget it. (voice over; his lips never move)', 'src': str(VOICE)}
                      for b in beats for l in b['lines'] if l['who'] == 'fatcat']
                     + [{'stem': 'sfx-world', 't': starts[i], 'dur': s[4], 'what': f"{s[0]}: clip's own sound", 'src': str(s[2])}
                        for i, s in enumerate(SHOTS) if s[1] == 'clip'],
           'flags': ['"Homes fit for heroes" is the real 1918 government promise (a slogan, not a person): checked wording before posting.',
                     'No plaque on the bench (A2-b has none).', 'No music yet.']}
    (CUT / 'edl.json').write_text(json.dumps(edl, indent=1, ensure_ascii=False))
    print(json.dumps({'total': TOTAL, 'starts': starts, 'preview': str(CUT / 'preview.mp4')}))


if __name__ == '__main__':
    main()
