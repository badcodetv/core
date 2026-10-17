#!/usr/bin/env python3
"""Make the clips the re-timed cut needs longer than their source (rough-cut.json `extend` > 0).

Ping-pong (forward, then reversed, repeated: docs/flow/post-production.md §3.3) for Veo clips and
held stills; a held last frame for a move that must not reverse (frame 16's push). Writes
video/rt/<name> starting at the clip's in-point, so the cut uses it from 0. Updates rough-cut.json.

    python3 scripts/gpom/second-half-video/extend.py
"""
import json
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import shots as S  # noqa: E402

RC = S.CLIPS / 'audio' / 'rough-cut.json'
RT = S.OUT / 'rt'
FREEZE = {'sh-16-post.mp4'}
ENC = ['-an', '-r', '24', '-c:v', 'libx264', '-crf', '17', '-pix_fmt', 'yuv420p', '-color_range', 'tv',
       '-colorspace', 'bt709', '-color_primaries', 'bt709', '-color_trc', 'bt709']

rc = json.loads(RC.read_text())
RT.mkdir(exist_ok=True)
for c in rc['clips']:
    name, t, i, d, n, ext = c
    if ext <= 0 or name.startswith('rt/'):
        continue
    src = S.OUT / name
    out = RT / name
    if name in FREEZE:
        vf = f'trim=start={i},setpts=PTS-STARTPTS,tpad=stop_mode=clone:stop_duration={ext + 0.5}'
        cmd = ['ffmpeg', '-loglevel', 'error', '-y', '-i', str(src), '-vf', vf, '-t', str(d), *ENC, str(out)]
    else:
        # forward + reversed, twice over: up to four times the source, then cut to length.
        fc = (f'[0:v]trim=start={i},setpts=PTS-STARTPTS,split[f][r];[r]reverse[b];'
              '[f][b]concat=n=2:v=1[pp];[pp]split[p1][p2];[p1][p2]concat=n=2:v=1[v]')
        cmd = ['ffmpeg', '-loglevel', 'error', '-y', '-i', str(src), '-filter_complex', fc, '-map', '[v]',
               '-t', str(d), *ENC, str(out)]
    subprocess.run(cmd, check=True)
    c[0], c[2], c[5] = f'rt/{name}', 0, 0
    print(f'frame {n:2d} {name} -> rt/ {d:.2f}s')
RC.write_text(json.dumps(rc, indent=1))
