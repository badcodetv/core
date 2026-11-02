#!/usr/bin/env python3
"""Name each harvested clip by its FIRST FRAME: image-to-video starts on its plate.

Same method and threshold as scripts/gaze-board/match_clips.py (correct matches score 35-61,
runners-up 1800+). A plate matching several clips keeps the newest; the rest go to inbox/dupes,
never deleted, because they are paid for.

    python3 scripts/scene/match.py <scene-dir>            # report
    python3 scripts/scene/match.py <scene-dir> --apply    # move into video/
"""
import json
import os
import pathlib
import shutil
import subprocess
import sys
import tempfile

sys.path.insert(0, str(pathlib.Path(__file__).parent))
sys.path.insert(0, str(pathlib.Path(__file__).parents[1] / 'provenance'))
from scene import Scene  # noqa: E402
from shots import shots as all_shots  # noqa: E402
from prov import write_card  # noqa: E402

THRESHOLD = 400


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


def main(scene_dir, apply):
    inbox = Scene(scene_dir).video / 'inbox'
    # What run.mts actually asked Flow for, per shot (written at submit). Older harvests have none.
    used = json.loads((inbox / 'settings.json').read_text()) if (inbox / 'settings.json').exists() else {}
    shots = all_shots(scene_dir)
    plates = {s['key']: sig(s['src'], False) for s in shots}
    by_key = {s['key']: s for s in shots}
    claims = {}
    for c in sorted(inbox.glob('raw-*.mp4')):
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
        keep, extra = (None, files) if out.exists() else (files[0], files[1:])
        if apply:
            if keep:
                shutil.move(str(keep), out)
                print(f'  -> {out.name}')
                # The recipe card (docs/provenance): the settings run.mts submitted with (or, for a
                # harvest from before settings.json, the scene's own), the job's prompt, its plate.
                s = by_key[k]
                st = used.get(k) or {'model': s['model'], 'aspect': s['aspect'], 'mode': s['mode'],
                                     'durationSeconds': s['duration'], 'count': 1, 'source': 'scene settings (no submit record)'}
                write_card(out, kind='video', engine='google-flow', tool='scripts/scene/run.mts', model=st['model'],
                           prompt=s['motion'], parent=s['src'], why=s.get('why') or s.get('label') or None,
                           inputs={'start': s['src'], 'character': s.get('character'), 'scene': str(pathlib.Path(scene_dir).resolve()),
                                   'key': k, 'frame': s.get('n'), 'option': s.get('option')},
                           settings={kk: vv for kk, vv in st.items() if kk != 'model'})
            for e in extra:
                (inbox / 'dupes').mkdir(parents=True, exist_ok=True)
                shutil.move(str(e), inbox / 'dupes' / f'{k}-{e.name}')
    print(json.dumps({'have': sorted(k for k in by_key if pathlib.Path(by_key[k]['out']).exists())}))


if __name__ == '__main__':
    main(sys.argv[1], '--apply' in sys.argv)
