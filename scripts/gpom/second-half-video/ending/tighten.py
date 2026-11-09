#!/usr/bin/env python3
"""Hold the pauses inside a picked voice take to a ceiling, words untouched (never sped up).

    python3 scripts/gpom/second-half-video/ending/tighten.py D d3-11-maddie 0.45 [--why "..."]

Reads the line's current file from the scene's voices.json, finds the silent runs inside the speech (40 dB under the
loudest 10 ms, as voices.py's `silence`, and never below -35 dB), shortens every run longer than the ceiling to the ceiling (keeping the
centre of the gap, with 15 ms fades at each join), writes <take>-tight.wav beside it and points the row at it, with
the untightened take kept under `untightened`. Done by hand in D rounds 9-10; this is the same edit as a script.
"""
import json
import subprocess
import sys

import numpy as np

import voices as VO

args = sys.argv[1:]
WHY = None
if '--why' in args:
    i = args.index('--why')
    WHY, args = args[i + 1], args[:i] + args[i + 2:]
scene, lid, ceil = args[0], args[1], float(args[2])
SR = 48000
STEP = 0.01


def main():
    path = VO.SCENES / VO.SCENE_DIRS[scene] / 'voices.json'
    doc = json.loads(path.read_text())
    row = doc['lines'][lid]
    src = VO.CLIPS / scene / (row.get('untightened') or row)['file']
    raw = subprocess.run(['ffmpeg', '-loglevel', 'error', '-i', str(src), '-ac', '1', '-ar', str(SR), '-f', 's16le', '-'],
                         capture_output=True, check=True).stdout
    x = np.frombuffer(raw, np.int16).astype(float) / 32768
    hop = int(SR * STEP)
    n = len(x) // hop
    db = 20 * np.log10(np.sqrt((x[:n * hop].reshape(n, hop) ** 2).mean(1)) + 1e-9)
    act = np.where(db > max(db.max() - 40, -35))[0]  # -35 dB floor: breathy room tone sat above max-40 (d3-9 r13)
    keep, cursor, cuts = [], 0, []
    gaps = np.diff(act)
    for i in np.where(gaps * STEP > ceil)[0]:
        g0, g1 = (act[i] + 1) * STEP, act[i + 1] * STEP
        drop0, drop1 = g0 + ceil / 2, g1 - ceil / 2
        keep.append((cursor, drop0))
        cursor = drop1
        cuts.append((round(g0, 2), round(g1, 2)))
    keep.append((cursor, len(x) / SR))
    dst = src.with_name(src.stem + '-tight.wav')
    parts = ''.join(f'[0:a]atrim={a:.3f}:{b:.3f},asetpts=PTS-STARTPTS,afade=t=in:d=0.015,'
                    f'afade=t=out:st={max(0, b - a - 0.015):.3f}:d=0.015[p{i}];' for i, (a, b) in enumerate(keep))
    fc = parts + ''.join(f'[p{i}]' for i in range(len(keep))) + f'concat=n={len(keep)}:v=0:a=1[o]'
    subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', '-i', str(src), '-filter_complex', fc, '-map', '[o]', str(dst)],
                   check=True)
    dur = round(VO.V.duration(dst), 2)
    if 'untightened' not in row:
        row['untightened'] = {'file': row['file'], 'duration': row['duration']}
    row['file'] = f'voices/{dst.name}'
    row['duration'] = dur
    row['tightened'] = WHY or f'pauses held to {ceil} s; words untouched'
    path.write_text(json.dumps(doc, indent=1, ensure_ascii=False) + '\n')
    print(f'{lid}: {row["untightened"]["duration"]} s -> {dur} s; gaps shortened {cuts}')


if __name__ == '__main__':
    main()
