#!/usr/bin/env python3
"""Name each harvested clip by its FIRST FRAME: image-to-video starts on its plate.

Same method and threshold as scripts/gaze-board/match_clips.py (correct matches score 35-61,
runners-up 1800+). A plate matching several clips keeps the newest (lowest raw number, as the
gallery lists newest first); the rest go to inbox/dupes, never deleted, because they are paid for.

    python3 scripts/gpom/opening-video/match.py            # report
    python3 scripts/gpom/opening-video/match.py --apply    # move into video/
"""
import json
import os
import pathlib
import shutil
import subprocess
import sys
import tempfile

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import shots as S  # noqa: E402

INBOX = S.OUT / 'inbox'
DUPES = INBOX / 'dupes'
THRESHOLD = 400
APPLY = '--apply' in sys.argv


def sig(path, is_video):
    with tempfile.NamedTemporaryFile(suffix='.gray', delete=False) as t:
        tmp = t.name
    cmd = ['ffmpeg', '-v', 'error', '-y', '-i', str(path)] + (['-frames:v', '1'] if is_video else [])
    subprocess.run(cmd + ['-vf', 'scale=32:32', '-f', 'rawvideo', '-pix_fmt', 'gray', tmp], check=True)
    data = pathlib.Path(tmp).read_bytes()
    os.unlink(tmp)
    return list(data[:1024])


def dist(a, b):
    return sum((x - y) ** 2 for x, y in zip(a, b)) / len(a)


shots = [s for s in S.shots() if s['src']]
plates = {s['key']: sig(s['src'], False) for s in shots}
by_key = {s['key']: s for s in shots}
claims = {}
for c in sorted(INBOX.glob('raw-*.mp4')):
    try:
        v = sig(c, True)
    except subprocess.CalledProcessError:
        print(f'UNREADABLE {c.name}')
        continue
    ranked = sorted((dist(v, p), k) for k, p in plates.items())
    d, k = ranked[0]
    # A re-roll shares its plate with the original, so several keys tie: prefer one still missing.
    ties = [kk for dd, kk in ranked if dd < THRESHOLD and dd <= d + 5]
    k = next((kk for kk in ties if not pathlib.Path(by_key[kk]['out']).exists()), k)
    print(f'{c.name}: {k} ({d:.0f})' + ('' if d < THRESHOLD else '  NO MATCH'))
    if d < THRESHOLD:
        claims.setdefault(k, []).append(c)

for k, files in claims.items():
    out = pathlib.Path(by_key[k]['out'])
    files.sort()
    if out.exists():
        keep, extra = None, files
    else:
        keep, extra = files[0], files[1:]
    if APPLY:
        if keep:
            shutil.move(str(keep), out)
            print(f'  -> {out.name}')
        for e in extra:
            DUPES.mkdir(parents=True, exist_ok=True)
            shutil.move(str(e), DUPES / f'{k}-{e.name}')
print(json.dumps({'have': sorted(k for k in by_key if pathlib.Path(by_key[k]['out']).exists())}))
