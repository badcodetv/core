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
SHOTS = [('card1919', 'card', DATES / 'card-1919.png', 0.0, CARD, None),
         ('veteran', 'clip', VID / 'sb-01-A2-b.mp4', 0.0, 5.6, (0.20, 1.60, 1.0, 'Forget it.')),
         ('card2026', 'card', DATES / 'card-2026.png', 0.0, CARD, None),
         ('nurse', 'clip', VID / 'sb-02-B3-a.mp4', 0.0, 5.6, (2.90, 4.40, 1.0, 'Forget it.')),
         ('button', 'clip', VID / 'sb-03-C3-a.mp4', 0.0, 5.0, None)]
starts, t = [], 0.0
for s in SHOTS: starts.append(round(t, 3)); t += s[4]
TOTAL = round(t, 3)
CAPTION, T_CAP = 'Same bench.', starts[4] + 2.2
T_FADE = TOTAL - 0.8
SEE = {'card1919': 'Title card: 1919.', 'veteran': 'He flicks the soldier away without moving his lips; the soldier limps out of the light.',
       'card2026': 'Title card: 2026.', 'nurse': 'The same flick; the nurse walks off towards the hospital.',
       'button': 'He tips his hat, then turns to the empty seat. "Same bench." Fade to black.'}
TITLES = {'card1919': '1919', 'veteran': 'A. 1919: "Forget it."', 'card2026': '2026', 'nurse': 'B. 2026: "Forget it."', 'button': 'C. Same bench.'}


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
        if kind == 'card':  # a held card with projector flicker and moving grain, like the clips' stock
            ff('-loop', 1, '-t', d, '-i', src, '-vf',
               f"{FIT},noise=alls=18:allf=t,eq=brightness='0.025*sin(2*PI*9*t)',fade=t=in:d=0.15,fade=t=out:st={d - 0.15}:d=0.15,format=yuv420p", *ENC, out)
            sp = CUT / f's{i}-{beat}.wav'
            ff('-f', 'lavfi', '-i', f'anullsrc=r=48000:cl=stereo', '-t', d, sp)
        else:
            ff('-ss', tin, '-t', d, '-i', src, '-an', '-vf', f'{FIT},scale=in_range=full:out_range=limited,format=yuv420p', *ENC, out)
            sp = CUT / f's{i}-{beat}.wav'
            ff('-ss', tin, '-t', d, '-i', src, '-vn', '-af', f'loudnorm=I={SFX_LUFS}:TP=-6,afade=t=in:d=0.05,afade=t=out:st={d - 0.05}:d=0.05',
               '-ar', 48000, '-ac', 2, sp)
        parts.append(out); world.append(sp)
    (CUT / 'list.txt').write_text(''.join(f"file '{p.name}'\n" for p in parts))
    ff('-f', 'concat', '-safe', '0', '-i', CUT / 'list.txt', '-c', 'copy', CUT / 'picture-raw.mp4')
    cap = (f"drawtext=fontfile='{FONT}':text='{CAPTION}':fontsize=110:fontcolor=white@0.92:x=(w-text_w)/2:y=230:"
           f"enable='gte(t,{T_CAP:.2f})',fade=t=out:st={T_FADE:.2f}:d=0.8")
    ff('-i', CUT / 'picture-raw.mp4', '-vf', f'{cap},format=yuv420p', *ENC, CUT / 'picture.mp4')

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
        if s[0] == 'button':
            ln.append({'i': 1, 'who': 'caption', 'name': 'Caption', 't': round(T_CAP, 2), 'dur': round(TOTAL - T_CAP, 2), 'text': CAPTION, 'by': 'claude'})
        beats.append({'id': s[0], 'title': TITLES[s[0]], 'start': starts[i], 'dur': s[4], 'see': SEE[s[0]], 'lines': ln})
    edl = {'sequence': f'shorts-2-same-bench-r{rnd}', 'title': 'Same Bench Timeline',
           'heading': f'BadCode Shorts ▲ Same Bench, rough cut {rnd}',
           'intro': 'Title cards for the dates, your three clips, the fat cat (Algenib) and "Same bench." Note anything: a beat, a shot, a line, a sound, or a single frame.',
           'fps': FPS, 'total': TOTAL, 'beats': beats,
           'video': [{'file': str(parts[i] if s[1] == 'card' else s[2]), 'in': s[3], 'start': starts[i], 'dur': s[4], 'beat': s[0],
                      'source': str(s[2]), 'looped': False} for i, s in enumerate(SHOTS)],
           'audio': [{'track': 'A1', 'name': 'vox-fatcat', 'file': str(vox)}, {'track': 'A2', 'name': 'sfx-world', 'file': str(wst)}],
           'events': [{'stem': 'vox-fatcat', 't': l['t'], 'dur': l['dur'], 'what': 'Forget it. (voice over; his lips never move)', 'src': str(VOICE)}
                      for b in beats for l in b['lines'] if l['who'] == 'fatcat']
                     + [{'stem': 'sfx-world', 't': starts[i], 'dur': s[4], 'what': f"{s[0]}: clip's own sound", 'src': str(s[2])}
                        for i, s in enumerate(SHOTS) if s[1] == 'clip'],
           'flags': ['No plaque on the bench yet: A2-b has none (script 1B\'s pat and LEST WE FORGET plate are not in this cut).',
                     'C: his face changes during the head turn (kept by Jack).', 'No music yet.']}
    (CUT / 'edl.json').write_text(json.dumps(edl, indent=1, ensure_ascii=False))
    print(json.dumps({'total': TOTAL, 'starts': starts, 'preview': str(CUT / 'preview.mp4')}))


if __name__ == '__main__':
    main()
