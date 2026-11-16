#!/usr/bin/env python3
"""The Malevolent Force (BadCode Short #83): rough cut (2026-11-16).

    python3 scripts/shorts/malevolent_force_cut.py <track.wav> [--round N]

9:16, Jack's six picked shots (1 a2, 2 a, 3 a2, 4 b, 5 b, 6 b-swap) cut to ONE instrumental Suno track (vibes1; no
voice: Jack, "No voice, one end card"), then the end card ("Based on true events. Coming to a shop near you.").
- Shot 4: the shelf label changes on the light: 50p, then £1 when the tube browns out, then £5 when it comes back. The
  new labels are edits of the same still (pr-1b-b, pr-5-b); only the label area is pasted over the clip, colour-matched
  to the frame it sits in, so nothing else changes.
- Shot 6 is already swapped (mf-06-f4b-swap: £5/10p to £50/10p crossed £12 on the flash).
- Blurs: the "BREAD £50" card in shot 1's window (it would spoil the end), the brand-like crisp packets in shot 2.
- The clips' own Omni sound is dropped. Writes <media>/cut/r<N>/edl.json (timeline format, scripts/scene/timeline.py),
  the music stem, picture.mp4 and preview.mp4.
"""
# style-lint: story=short-malevolent-force (this cut script belongs to one short)
import argparse, json, pathlib, subprocess, sys

import numpy as np
from PIL import Image, ImageDraw, ImageFilter

REPO = pathlib.Path(__file__).resolve().parents[2]
SCENE = REPO / 'docs/stories/short-malevolent-force/scenes/malevolent-force'
sys.path.insert(0, str(REPO / 'scripts/drive'))
from localmap import localize  # noqa: E402

cfg = localize(json.loads((SCENE / 'scene.json').read_text()))
MEDIA = pathlib.Path(cfg['media'])
VID, MB = MEDIA / 'video', MEDIA / 'moodboard'
W, H, FPS = 1080, 1920, 24
CW, CH = 720, 1280  # Omni clip size
CARD = 'Based on true events.\nComing to a shop near you.'
CARD_DUR = 2.6

# (beat key, title, clip, in, dur, blur boxes on the 720x1280 clip [(x0,y0,x1,y1)], what we see)
SHOTS = [('price50', '1. The only lit shop', 'mf-01-w2-FO2-c.mp4', 0.6, 2.0, [(566, 738, 648, 822)],
          'The only lit corner shop on a dead terrace at 3am; its lights dip.'),
         ('price50', '2. The door opens by itself', 'mf-02-PR2-e.mp4', 1.4, 2.2, [(632, 280, 720, 1050)],
          'From inside, the glass door swings wider onto the black street.'),
         ('price50', '3. The aisle', 'mf-03-w2-PR2-c.mp4', 1.0, 2.0, [],
          'Down the aisle, the stockroom door at the back eases open. Nobody there.'),
         ('climb', '4. 50p, £1, £5', 'mf-04-b-PR2-b.mp4', 0.2, 3.8, [],
          'One loaf, 50p. The tube browns out: £1. It comes back: £5.'),
         ('climb', '5. The mirror', 'mf-05-b-FO2-d.mp4', 0.8, 2.0, [],
          'The convex mirror rocks; the aisle is empty, blank notes on the floor.'),
         ('force', '6. Lightning: £50, 10p → £12', 'mf-06-f4b-swap.mp4', 1.2, 3.6, [],
          'The freezer lid: £5 and 10p. Lightning. £50, and the 10p crossed out for £12. Nothing else has changed.')]
# Shot 4's label swaps: (edited still, from clip second, sample second for the colour match)
SHELF_STILL = MB / 'PR2-b.jpg'
SHELF_SWAPS = [('pr-1b-b.jpg', 1.45, 2.2), ('pr-5-b.jpg', 2.95, 4.2)]
EDITS = pathlib.Path.home() / '.cache/badcode/mf-r4/edit'
LABEL_AREA = (230, 760, 500, 990)  # where shot 4's label sits on the 720x1280 clip; the edits relit other areas too


def ff(*a):
    subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', *map(str, a)], check=True)


ENC = ['-c:v', 'libx264', '-preset', 'veryfast', '-crf', '18', '-pix_fmt', 'yuv420p', '-color_range', 'tv',
       '-colorspace', 'bt709', '-color_primaries', 'bt709', '-color_trc', 'bt709']


def frame(clip, t, out):
    ff('-ss', t, '-i', clip, '-frames:v', 1, out)
    return np.asarray(Image.open(out).convert('RGB'), float)


def label_patch(still, edit, clip, t_sample, out, work):
    """The edited label, cut out of the edit, colour-matched to the clip at t_sample, as an RGBA overlay."""
    st = np.asarray(Image.open(still).convert('RGB').resize((CW, CH)), float)
    ed = np.asarray(Image.open(edit).convert('RGB').resize((CW, CH)), float)
    d = np.abs(st - ed).mean(2)
    keep = np.zeros_like(d); x0, y0, x1, y1 = LABEL_AREA; keep[y0:y1, x0:x1] = 1; d *= keep  # the label only
    sm = np.asarray(Image.fromarray((d > 45).astype(np.uint8) * 255).filter(ImageFilter.MaxFilter(9)))
    ys, xs = np.nonzero(sm)
    m = Image.new('L', (CW, CH), 0)
    ImageDraw.Draw(m).rectangle([xs.min() - 18, ys.min() - 18, xs.max() + 18, ys.max() + 18], 255)
    m = np.asarray(m.filter(ImageFilter.GaussianBlur(7)), float) / 255
    fr = frame(clip, t_sample, work / f'{out.stem}-sample.png')
    sel = m > 0.5
    o = ed.copy()
    for c in range(3):
        a, b = np.polyfit(st[..., c][sel], fr[..., c][sel], 1)
        o[..., c] = np.clip(a * ed[..., c] + b, 0, 255)
    Image.fromarray(np.dstack([o, m * 255]).astype(np.uint8), 'RGBA').save(out)
    return [int(xs.min()), int(ys.min()), int(xs.max()), int(ys.max())]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('track'); ap.add_argument('--round', type=int, default=1)
    a = ap.parse_args()
    track = pathlib.Path(a.track)
    cut = MEDIA / 'cut' / f'r{a.round}'; cut.mkdir(parents=True, exist_ok=True)
    starts, t = [], 0.0
    for s in SHOTS: starts.append(round(t, 3)); t += s[4]
    pic_end = round(t, 3); total = round(pic_end + CARD_DUR, 3)
    parts, notes = [], []
    for i, (beat, title, clip, tin, d, blurs, _) in enumerate(SHOTS):
        src = VID / clip
        inputs, chain, last = ['-i', src], '', '0:v'
        if i == 3:  # the shelf label swaps
            for j, (ed, at, ts) in enumerate(SHELF_SWAPS):
                p = cut / f'shelf-{j}.png'
                box = label_patch(SHELF_STILL, EDITS / ed, src, ts, p, cut)
                inputs += ['-i', p]
                chain += f"[{last}][{j + 1}:v]overlay=0:0:enable='gte(t,{at})'[o{j}];"
                last = f'o{j}'
                notes.append(f'shot 4 label {ed} from {at:.2f} s (clip time), box {box}')
        for k, (x0, y0, x1, y1) in enumerate(blurs):
            w, h = x1 - x0, y1 - y0
            chain += f'[{last}]split[b{k}m][b{k}s];[b{k}s]crop={w}:{h}:{x0}:{y0},boxblur=14:2[b{k}c];[b{k}m][b{k}c]overlay={x0}:{y0}[bl{k}];'
            last = f'bl{k}'
        n = int(round(d * FPS))
        chain += (f'[{last}]trim=start={tin}:duration={d},setpts=PTS-STARTPTS,'
                  f'scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},fps={FPS},'
                  'scale=in_range=full:out_range=limited,format=yuv420p,lutyuv=y=clip(val\\,22\\,232)[v]')
        out = cut / f'v{i}.mp4'
        ff(*inputs, '-filter_complex', chain, '-map', '[v]', '-an', *ENC, out)
        parts.append(out)
    # The end card: white text on black, faded in.
    font = '/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf'
    (cut / 'card.txt').write_text(CARD)
    ff('-f', 'lavfi', '-i', f'color=black:s={W}x{H}:r={FPS}:d={CARD_DUR}', '-vf',
       f"drawtext=fontfile={font}:textfile={cut / 'card.txt'}:fontcolor=white:fontsize=62:line_spacing=30:"
       f"x=(w-text_w)/2:y=(h-text_h)/2:alpha='min(1,t/0.6)',scale=in_range=full:out_range=limited,format=yuv420p,lutyuv=y=clip(val\\,22\\,232)", *ENC, cut / 'v6-card.mp4')
    parts.append(cut / 'v6-card.mp4')
    (cut / 'list.txt').write_text(''.join(f"file '{p.name}'\n" for p in parts))
    ff('-f', 'concat', '-safe', '0', '-i', cut / 'list.txt', '-c', 'copy', cut / 'picture.mp4')
    # The music: one stem from t=0, its own ending kept, faded over its last second; the card plays in silence after it.
    mdur = float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', track],
                                capture_output=True, text=True).stdout)
    stem = cut / 'mus-track.wav'
    ff('-i', track, '-af', f'loudnorm=I=-14:TP=-1.5,afade=t=out:st={max(0, mdur - 1.0):.2f}:d=1.0,apad=whole_dur={total},atrim=end={total}',
       '-ar', 48000, '-ac', 2, stem)
    ff('-i', cut / 'picture.mp4', '-i', stem, '-map', '0:v', '-map', '1:a', '-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k',
       '-t', total, cut / 'preview.mp4')
    beats = [{'id': f's{i + 1}', 'title': s[1], 'start': starts[i], 'dur': s[4], 'see': s[6], 'lines': []} for i, s in enumerate(SHOTS)]
    beats.append({'id': 'card', 'title': '7. End card', 'start': pic_end, 'dur': CARD_DUR, 'see': CARD.replace('\n', ' '),
                  'lines': [{'i': 0, 'who': 'card', 'name': 'End card (on screen)', 't': pic_end, 'dur': CARD_DUR,
                             'text': CARD.replace('\n', ' '), 'by': 'kai'}]})
    video = [{'file': str(VID / s[2]), 'in': s[3], 'start': starts[i], 'dur': s[4], 'beat': f's{i + 1}', 'source': str(VID / s[2]), 'looped': False}
             for i, s in enumerate(SHOTS)]
    video.append({'file': str(cut / 'v6-card.mp4'), 'in': 0, 'start': pic_end, 'dur': CARD_DUR, 'beat': 'card',
                  'source': str(cut / 'v6-card.mp4'), 'looped': False})
    edl = {'sequence': f'short-malevolent-force-1-malevolent-force-r{a.round}', 'title': 'Malevolent Force Timeline',
           'heading': f'BadCode Shorts ▲ The Malevolent Force, rough cut {a.round}',
           'intro': ('Your six picked shots, your picked music (vibes1, instrumental) and the end card. The shelf label goes 50p, £1 '
                     'in the dark, £5 when the light comes back; the freezer goes £5/10p to £50/£12 on the lightning. Note '
                     'anything: a beat, a shot, the sound, or a single frame.'),
           'fps': FPS, 'total': total, 'beats': beats, 'video': video,
           'audio': [{'track': 'A1', 'name': 'mus-track', 'file': str(stem)}],
           'events': [{'stem': 'mus-track', 't': 0.0, 'dur': round(min(mdur, total), 3),
                       'what': f'Suno track {track.stem} (vibes1), faded over its last second', 'src': str(track)}],
           'flags': [f'The music is {mdur:.1f} s; the end card ({pic_end:.1f}-{total:.1f} s) plays in silence after it.',
                     'Blurred: the "BREAD £50" card in shot 1\'s window; the brand-like crisp packets on the spinner in shot 2.',
                     'Not blurred: the packets on the aisle shelves in shot 3 look brand-like but read as no brand at this size.',
                     *notes]}
    (cut / 'edl.json').write_text(json.dumps(edl, indent=1, ensure_ascii=False))
    print(json.dumps({'total': total, 'starts': starts, 'picture_end': pic_end, 'music': round(mdur, 2),
                      'preview': str(cut / 'preview.mp4'), 'edl': str(cut / 'edl.json')}))


if __name__ == '__main__':
    main()
