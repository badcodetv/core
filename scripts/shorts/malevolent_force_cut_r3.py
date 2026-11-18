#!/usr/bin/env python3
"""The Malevolent Force (BadCode Short #83): rough cut 3, the "more horror" cut (2026-11-18).

    python3 scripts/shorts/malevolent_force_cut_r3.py <track.wav> [--round 3]

Rough cut 2 (malevolent_force_cut.py) plus Jack's round-8 picks on the horror picks page
(https://claude.ai/artifact/4tizwo1we4aYm9KMtxjbVK, scenes/malevolent-force/picks.md):
- shot 2: the door swings open, then a half-second of the figure behind it (door b);
- shot 3: the aisle, the figure peeking from the back door and scuttling back (peek b), then leaping off the shelving (top a);
- shot 4: the burnt hand holds the 50p card and snatches up (hand c), then the brownout clip: £1 in the dark, £5 in the light;
- shot 5: the mirror take (mirror b);
- shot 6: the burnt hand snatches up from the freezer (hand b), then the lightning: £50, and 10p struck for £12.
The subtle VHS finish (scripts/shorts/vhs_finish.sh, Jack's pick) goes over the shots only; the end card and the logo stay
clean (the logo is never altered). vibes1 is 15 s and the picture is longer: until the suspense-strings track exists the
music is slowed (pitch kept) to end with the picture. Writes <media>/cut/r<N>/ like rough cut 2.
"""
# style-lint: story=short-malevolent-force (this cut script belongs to one short)
import argparse, json, pathlib, subprocess, sys

from PIL import Image

sys.path.insert(0, str(pathlib.Path(__file__).parent))
import malevolent_force_cut as r2  # noqa: E402  (helpers, constants, the card and logo)

VID, MB, W, H, FPS, ENC, ff = r2.VID, r2.MB, r2.W, r2.H, r2.FPS, r2.ENC, r2.ff
DUPES = VID / 'inbox' / 'dupes'
SPIN_BLUR = [(632, 280, 720, 1050)]  # the brand-like crisp spinner on the right of the door shots

# (beat, title, clip, in, dur, blurs, label swaps [(edit, clip second)], what we see)
SEGS = [
    ('s1', '1. The only lit shop', VID / 'mf-01-w2-FO2-c.mp4', 0.6, 1.6, [(566, 738, 648, 822)], [],
     'The only lit corner shop on a dead terrace at 3am; its lights dip.'),
    ('s2', '2. The door opens by itself', VID / 'mf-02-PR2-e.mp4', 1.4, 1.4, SPIN_BLUR, [],
     'From inside, the glass door swings wider onto the black street.'),
    ('s2', '2b. Something behind the door', VID / 'mf-d2-b-JS2-door-b.mp4', 1.4, 0.5, SPIN_BLUR, [],
     'For half a second, a dark shape stands behind the door frame.'),
    ('s3', '3. The aisle', VID / 'mf-03-w2-PR2-c.mp4', 1.0, 0.7, [], [],
     'Down the aisle, the back door eases open. Nobody there.'),
    ('s3', '3b. It peeks, then scuttles back', VID / 'mf-p3-b-JS3-peek2-a.mp4', 1.9, 1.0, [], [],
     'In the back doorway, the black figure leans out, then jerks back into the dark.'),
    ('s3', '3c. It was on the shelving', VID / 'mf-t3-a-JS3-top-b.mp4', 1.7, 1.3, [], [],
     'High on the shelving it crouches; the light blinks; it drops into the aisle in a smear of smoke.'),
    ('s4', '4. The hand takes the 50p', DUPES / 'h4-a-raw-002--h4-a2.mp4', 0.9, 2.0, [], [],
     'A burnt hand holds the 50p card, lightning crackling round it, then snatches up into the dark.'),
    ('s4', '4b. £1, then £5', VID / 'mf-04-b-PR2-b.mp4', 1.3, 1.9, [], [('PR2-b-1pound.jpg', 1.45, 2.2), ('PR2-b-5pound.jpg', 2.95, 4.2)],
     'In the dark the card says £1. The light comes back: £5.'),
    ('s5', '5. The mirror', VID / 'mf-m5-b-JS5-mirror-b.mp4', 0.6, 1.6, [], [],
     'The convex mirror rocks; something was in the reflection.'),
    ('s6', '6. The hand at the freezer', DUPES / 'h6-a-raw-005--h6-a.mp4', 1.2, 1.6, [], [],
     'The burnt hand hangs over the £5 card, then whips up into the dark.'),
    ('s6', '6b. Lightning: £50, 10p → £12', VID / 'mf-06-f4b-swap.mp4', 1.4, 3.0, [], [],
     'The freezer lid. Lightning. £50, and the 10p crossed out for £12. Nothing else has changed.'),
]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('track'); ap.add_argument('--round', type=int, default=3)
    a = ap.parse_args()
    track = pathlib.Path(a.track)
    cut = r2.MEDIA / 'cut' / f'r{a.round}'; cut.mkdir(parents=True, exist_ok=True)
    starts, t, parts, notes = [], 0.0, [], []
    for s in SEGS: starts.append(round(t, 3)); t += s[4]
    pic_end = round(t, 3); logo_at = round(pic_end + r2.CARD_DUR, 3); total = round(logo_at + r2.LOGO_DUR, 3)
    for i, (beat, title, src, tin, d, blurs, swaps, _) in enumerate(SEGS):
        inputs, chain, last = ['-i', src], '', '0:v'
        for j, (ed, at, ts) in enumerate(swaps):
            p = cut / f'label-{i}-{j}.png'
            box = r2.label_patch(r2.SHELF_STILL, MB / ed, src, ts, p, cut)
            inputs += ['-i', p]
            chain += f"[{last}][{j + 1}:v]overlay=0:0:enable='gte(t,{at})'[o{j}];"
            last = f'o{j}'
            notes.append(f'{title}: label {ed} from {at:.2f} s (clip time), box {box}')
        for k, (x0, y0, x1, y1) in enumerate(blurs):
            w, h = x1 - x0, y1 - y0
            chain += f'[{last}]split[b{k}m][b{k}s];[b{k}s]crop={w}:{h}:{x0}:{y0},boxblur=14:2[b{k}c];[b{k}m][b{k}c]overlay={x0}:{y0}[bl{k}];'
            last = f'bl{k}'
        chain += (f'[{last}]trim=start={tin}:duration={d},setpts=PTS-STARTPTS,'
                  f'scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},fps={FPS},'
                  'scale=in_range=full:out_range=limited,format=yuv420p,lutyuv=y=clip(val\\,22\\,232)[v]')
        out = cut / f'seg{i:02d}.mp4'
        ff(*inputs, '-filter_complex', chain, '-map', '[v]', '-an', *ENC, out)
        parts.append(out)
    # The shots, joined, then the subtle VHS finish over them only.
    (cut / 'shots.txt').write_text(''.join(f"file '{p.name}'\n" for p in parts))
    ff('-f', 'concat', '-safe', '0', '-i', cut / 'shots.txt', '-c', 'copy', cut / 'shots-clean.mp4')
    subprocess.run([str(pathlib.Path(__file__).parent / 'vhs_finish.sh'), str(cut / 'shots-clean.mp4'), str(cut / 'shots-vhs.mp4')], check=True)
    ff('-i', cut / 'shots-vhs.mp4', '-vf', 'scale=in_range=full:out_range=limited,format=yuv420p', *ENC, cut / 'shots.mp4')
    # The card and the logo: rough cut 2's, rebuilt here by running its builder pieces.
    card, logo = cut / 'v-card.mp4', cut / 'v-logo.mp4'
    font = '/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf'
    (cut / 'card.txt').write_text(r2.CARD)
    ff('-f', 'lavfi', '-i', f'color=black:s={W}x{H}:r={FPS}:d={r2.CARD_DUR}', '-vf',
       f"drawtext=fontfile={font}:textfile={cut / 'card.txt'}:fontcolor=white:fontsize=62:line_spacing=30:"
       f"x=(w-text_w)/2:y=(h-text_h)/2:alpha='min(1,t/0.6)',scale=in_range=full:out_range=limited,format=yuv420p,lutyuv=y=clip(val\\,22\\,232)", *ENC, card)
    fr = cut / 'logo-frames'; fr.mkdir(exist_ok=True)
    lg = Image.open(r2.LOGO).convert('RGBA'); lw = int(W * 0.62); lg = lg.resize((lw, int(lg.height * lw / lg.width)))
    base = Image.new('RGB', (W, H), r2.GROUND); withlogo = base.copy(); withlogo.paste(lg, ((W - lw) // 2, (H - lg.height) // 2), lg)
    flash = Image.new('RGB', (W, H), (232, 240, 255))
    for k in range(int(round(r2.LOGO_DUR * FPS))):
        s = k / FPS
        lit = 1.0 if 0.30 <= s < 0.38 else (0.12 if 0.38 <= s < 0.50 else (max(0.0, 1.0 - (s - 0.50) / 0.45) ** 1.6 if s >= 0.50 else 0.0))
        Image.blend(withlogo if s >= 0.50 else base, flash, lit).save(fr / f'{k:04d}.png')
    ff('-framerate', FPS, '-i', fr / '%04d.png', '-vf', 'scale=in_range=full:out_range=limited,format=yuv420p,lutyuv=y=clip(val\\,22\\,232)', *ENC, logo)
    (cut / 'list.txt').write_text(''.join(f"file '{p.name}'\n" for p in (cut / 'shots.mp4', card, logo)))
    ff('-f', 'concat', '-safe', '0', '-i', cut / 'list.txt', '-c', 'copy', cut / 'picture.mp4')
    # The music: slowed (pitch kept) to end with the shots, faded over its last second; card and logo in silence.
    mdur = float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', track],
                                capture_output=True, text=True).stdout)
    tempo = max(0.5, min(1.0, mdur / pic_end))
    stem = cut / 'mus-track.wav'
    ff('-i', track, '-af', f'atempo={tempo:.4f},loudnorm=I=-14:TP=-1.5,afade=t=out:st={max(0, pic_end - 1.0):.2f}:d=1.0,'
       f'apad=whole_dur={total},atrim=end={total}', '-ar', 48000, '-ac', 2, stem)
    ff('-i', cut / 'picture.mp4', '-i', stem, '-map', '0:v', '-map', '1:a', '-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k',
       '-t', total, cut / 'preview.mp4')
    beats = [{'id': f'b{i + 1:02d}', 'title': s[1], 'start': starts[i], 'dur': s[4], 'see': s[7], 'lines': []} for i, s in enumerate(SEGS)]
    beats.append({'id': 'card', 'title': 'End card', 'start': pic_end, 'dur': r2.CARD_DUR, 'see': r2.CARD.replace('\n', ' '),
                  'lines': [{'i': 0, 'who': 'card', 'name': 'End card (on screen)', 't': pic_end, 'dur': r2.CARD_DUR,
                             'text': r2.CARD.replace('\n', ' '), 'by': 'kai'}]})
    beats.append({'id': 'logo', 'title': 'Lightning, then the logo', 'start': logo_at, 'dur': r2.LOGO_DUR,
                  'see': 'Black; lightning flashes twice; as the second flash fades the BadCode logo is standing there.', 'lines': []})
    video = [{'file': str(s[2]), 'in': s[3], 'start': starts[i], 'dur': s[4], 'beat': f'b{i + 1:02d}', 'source': str(s[2]), 'looped': False}
             for i, s in enumerate(SEGS)]
    video += [{'file': str(card), 'in': 0, 'start': pic_end, 'dur': r2.CARD_DUR, 'beat': 'card', 'source': str(card), 'looped': False},
              {'file': str(logo), 'in': 0, 'start': logo_at, 'dur': r2.LOGO_DUR, 'beat': 'logo', 'source': str(r2.LOGO), 'looped': False}]
    edl = {'sequence': f'short-malevolent-force-1-malevolent-force-r{a.round}', 'title': 'Malevolent Force Timeline',
           'heading': f'BadCode Shorts ▲ The Malevolent Force, rough cut {a.round} (more horror)',
           'intro': ('Rough cut 3: your horror picks cut in. The burnt hand takes the 50p and the freezer card; the figure is behind '
                     'the door, peeks from the back room, drops off the shelving and passes through the mirror. The subtle VHS '
                     'finish is on every shot (not the card or logo). Music is still vibes1, slowed to fit, until the suspense '
                     'strings are made. Note anything: a beat, a shot, the sound, or a single frame.'),
           'fps': FPS, 'total': total, 'beats': beats, 'video': video,
           'audio': [{'track': 'A1', 'name': 'mus-track', 'file': str(stem)}],
           'events': [{'stem': 'mus-track', 't': 0.0, 'dur': pic_end,
                       'what': f'Suno track {track.stem} (vibes1) at {tempo:.2f}x speed, pitch kept, faded over its last second', 'src': str(track)}],
           'flags': [f'vibes1 is {mdur:.1f} s and the shots are {pic_end:.1f} s: slowed to {tempo:.2f}x until the strings exist.',
                     'No strings stabs yet under the scares: they come with the suspense-strings track.',
                     'The VHS finish is on the shots only; the end card and the logo are clean.',
                     'Blurred: the "BREAD £50" card in shot 1; the brand-like spinner in both door shots.',
                     *notes]}
    (cut / 'edl.json').write_text(json.dumps(edl, indent=1, ensure_ascii=False))
    print(json.dumps({'total': total, 'shots': pic_end, 'tempo': round(tempo, 3), 'preview': str(cut / 'preview.mp4'), 'edl': str(cut / 'edl.json')}))


if __name__ == '__main__':
    main()
