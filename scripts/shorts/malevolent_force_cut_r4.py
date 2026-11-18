#!/usr/bin/env python3
"""The Malevolent Force (BadCode Short #83): rough cut 4 (2026-11-18).

    python3 scripts/shorts/malevolent_force_cut_r4.py --shelf <clip-with-prices.mp4> --freezer <clip-with-prices.mp4> [--round 4]

Rough cut 3 (malevolent_force_cut_r3.py) with Jack's round-9 picks and notes
(scenes/malevolent-force/picks.md, feedback/horror-r9/):
- music: suspense strings, basses-from-below take 2 (Suno 32ef9301), slowed (pitch kept) to end with the shots;
- a strings stab on every scare, cut from the slasher-stab take (Suno 65f9c223, its opening stab), the music ducked under it;
- shot 4: the shelf with its blank card and the price drawn in the edit, seen first, then the hand passes over: 50p -> £5;
- shot 6: the freezer, both prices seen first, the hand swoops across like a magic trick: £5 -> £50, 10p crossed -> £12.
  (scripts/shorts/price_cards.py drew the prices; the old Flow-written labels and the lightning swap are gone.)
The subtle VHS finish on the shots only; the end card and the logo stay clean.
"""
# style-lint: story=short-malevolent-force (this cut script belongs to one short)
import argparse, json, pathlib, subprocess, sys

sys.path.insert(0, str(pathlib.Path(__file__).parent))
import malevolent_force_cut as r2  # noqa: E402
import malevolent_force_cut_r3 as r3  # noqa: E402

AUDIO = r2.MEDIA / 'audio' / 'r3-strings'
TRACK = AUDIO / 'malevolent-force-r3-strings-basses-from-below-v6-32ef9301.wav'
STAB_SRC, STAB_IN, STAB_DUR = AUDIO / 'malevolent-force-r3-strings-slasher-stab-section-65f9c223.wav', 0.0, 0.7


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--shelf', required=True); ap.add_argument('--freezer', required=True)
    ap.add_argument('--shelf-in', type=float, default=0.0); ap.add_argument('--shelf-dur', type=float, default=5.0)
    ap.add_argument('--freezer-in', type=float, default=0.0); ap.add_argument('--freezer-dur', type=float, default=4.6)
    ap.add_argument('--stabs', default='', help='comma-separated scare times in the cut (s); default: worked out from the shots')
    ap.add_argument('--round', type=int, default=4)
    a = ap.parse_args()
    segs = []
    for s in r3.SEGS:
        if s[1].startswith('4b') or s[1].startswith('6b'):
            continue  # the Flow-written labels (brownout, lightning swap) are replaced by the drawn prices
        if s[1].startswith('4.'):
            s = ('s4', '4. 50p, then the hand: £5', pathlib.Path(a.shelf), a.shelf_in, a.shelf_dur, [], [],
                 'The loaf, 50p on its card. A burnt hand comes down over the card; when it lifts away the card says £5.')
        if s[1].startswith('6.'):
            s = ('s6', '6. The magic trick: £50, 10p → £12', pathlib.Path(a.freezer), a.freezer_in, a.freezer_dur, [], [],
                 'The freezer: £5 and 10p. The hand swoops across both cards; when it has gone they say £50, and 10p crossed out for £12.')
        segs.append(s)
    r3.SEGS[:] = segs
    # Build the picture with rough cut 3's builder (it reads SEGS), then replace its music with the strings and the stabs.
    sys.argv = [sys.argv[0], str(TRACK), '--round', str(a.round)]
    r3.main()
    cut = r2.MEDIA / 'cut' / f'r{a.round}'
    edl = json.loads((cut / 'edl.json').read_text())
    starts = [b['start'] for b in edl['beats']]
    pic_end = next(b['start'] for b in edl['beats'] if b['id'] == 'card'); total = edl['total']
    byname = {b['title']: b for b in edl['beats']}
    if a.stabs:
        stabs = [float(x) for x in a.stabs.split(',')]
    else:  # a stab where each scare lands (seconds into its segment, from the clips' own timing)
        at = {'2b.': 0.15, '3b.': 0.55, '3c.': 0.75, '4. ': 1.45, '5. ': 0.9, '6. ': 1.3}
        stabs = sorted(round(b['start'] + off, 2) for k, off in at.items() for b in edl['beats'] if b['title'].startswith(k))
    stab = cut / 'stab.wav'
    r2.ff('-ss', STAB_IN, '-t', STAB_DUR, '-i', STAB_SRC, '-af', 'afade=t=out:st=0.35:d=0.35', '-ar', 48000, '-ac', 2, stab)
    mdur = float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', TRACK],
                                capture_output=True, text=True).stdout)
    tempo = max(0.5, min(1.0, mdur / pic_end))
    inputs = ['-i', TRACK] + sum((['-i', stab] for _ in stabs), [])
    graph = (f'[0:a]atempo={tempo:.4f},loudnorm=I=-15:TP=-2,afade=t=out:st={max(0, pic_end - 1.0):.2f}:d=1.0,apad=whole_dur={total},atrim=end={total}[m];'
             + ''.join(f'[{i + 1}:a]adelay={int(t * 1000)}|{int(t * 1000)},volume=1.6,apad=whole_dur={total},atrim=end={total}[s{i}];' for i, t in enumerate(stabs))
             + ''.join(f'[s{i}]' for i in range(len(stabs))) + f'amix=inputs={len(stabs)}:normalize=0[st];'
             + '[st]asplit[st1][st2];[m][st1]sidechaincompress=threshold=0.05:ratio=6:attack=5:release=250[md];'
             + '[md][st2]amix=inputs=2:normalize=0,alimiter=limit=0.89[out]')
    mix = cut / 'mus-track.wav'
    r2.ff(*inputs, '-filter_complex', graph, '-map', '[out]', '-ar', 48000, '-ac', 2, mix)
    r2.ff('-i', cut / 'picture.mp4', '-i', mix, '-map', '0:v', '-map', '1:a', '-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k', '-t', total, cut / 'preview.mp4')
    edl['heading'] = f'BadCode Shorts ▲ The Malevolent Force, rough cut {a.round}'
    edl['intro'] = ('Rough cut 4: your strings (basses from below, take 2) with a strings stab on every scare, and the prices drawn in the '
                    'edit: you see them first, then the hand passes over and they change. The subtle VHS finish on every shot. '
                    'Note anything: a beat, a shot, the sound, or a single frame.')
    edl['audio'] = [{'track': 'A1', 'name': 'strings + stabs', 'file': str(mix)}]
    edl['events'] = [{'stem': 'strings + stabs', 't': 0.0, 'dur': pic_end, 'what': f'Suno basses-from-below take 2 at {tempo:.2f}x, pitch kept', 'src': str(TRACK)}] + \
        [{'stem': 'strings + stabs', 't': t, 'dur': STAB_DUR, 'what': 'strings stab (slasher take, opening stab), music ducked under it', 'src': str(STAB_SRC)} for t in stabs]
    edl['flags'] = [f'The strings are {mdur:.1f} s and the shots {pic_end:.1f} s: slowed to {tempo:.2f}x, pitch kept.',
                    f'Stabs at {", ".join(f"{t:.2f}" for t in stabs)} s.',
                    'Prices are drawn in the edit (price_cards.py); the £1 step is gone: one pass of the hand, one change.',
                    'The VHS finish is on the shots only; the end card and the logo are clean.']
    (cut / 'edl.json').write_text(json.dumps(edl, indent=1, ensure_ascii=False))
    print(json.dumps({'total': total, 'shots': pic_end, 'tempo': round(tempo, 3), 'stabs': stabs, 'preview': str(cut / 'preview.mp4')}))


if __name__ == '__main__':
    main()
