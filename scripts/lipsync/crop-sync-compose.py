"""Paste LatentSync crops back onto their shot, the partner of crop-sync-prep.py (Stupidity Optimised rough 3,
2026-11-02).

For each shot in shots.json: take base.mp4 (the shot's window, 25 fps, 1280x720), scale each synced crop back down to
its box, and lay it over the base through a soft ellipse mask, so only that speaker's face is replaced and the
crop's edges never show. Crops that overlap (two-handers) each keep to their own ellipse. Output is 24 fps, no audio
(the voices stay on their own track), at <out>/so-NN-ls.mp4, plus <out>/lipsync-r3.json listing each file with its
timeline start t0 (in the sequence the state file came from) so a build script can place it on V2.

A crop whose synced file is missing (still running, or LatentSync failed) is left out; a shot with none is skipped.

  python scripts/lipsync/crop-sync-compose.py work/shots.json OUT_DIR [shot ...]
"""
import json, os, subprocess, sys
import numpy as np
from PIL import Image, ImageFilter

shots = json.load(open(sys.argv[1]))
out_dir = sys.argv[2]
only = {int(s) for s in sys.argv[3:]}
os.makedirs(out_dir, exist_ok=True)
manifest_path = os.path.join(out_dir, 'lipsync-r3.json')
manifest = json.load(open(manifest_path)) if os.path.exists(manifest_path) else {}


def mask_png(w, h, path):
    """White ellipse on black, feathered: the middle of the crop, where the face is."""
    y, x = np.mgrid[0:h, 0:w]
    r = ((x - w / 2) / (0.40 * w)) ** 2 + ((y - h / 2) / (0.44 * h)) ** 2
    m = Image.fromarray(((r < 1) * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(max(4, 0.06 * min(w, h))))
    m.save(path)


for s in shots:
    if only and s['shot'] not in only:
        continue
    crops = [c for c in s['crops'] if os.path.exists(c['synced'])]
    if not crops:
        print('skip', s['shot'], '(nothing synced yet)'); continue
    d = os.path.dirname(s['base'])
    cmd = ['ffmpeg', '-v', 'error', '-y', '-i', s['base']]
    fc, last = [], '0:v'
    for i, c in enumerate(crops):
        x1, y1, x2, y2 = c['box']; w, h = x2 - x1, y2 - y1
        m = os.path.join(d, f"mask-{c['who']}.png"); mask_png(w, h, m)
        cmd += ['-i', c['synced'], '-loop', '1', '-i', m]
        v, k = 1 + 2 * i, 2 + 2 * i
        fc.append(f'[{v}:v]scale={w}:{h}:flags=lanczos,fps=25,format=rgba[c{i}];[{k}:v]format=gray[m{i}];'
                  f'[c{i}][m{i}]alphamerge[a{i}];[{last}][a{i}]overlay={x1}:{y1}:shortest=0:eof_action=pass[o{i}]')
        last = f'o{i}'
    fc.append(f'[{last}]fps=24,format=yuv420p[out]')
    out = os.path.join(out_dir, f"so-{s['shot']:02d}-ls.mp4")
    cmd += ['-filter_complex', ';'.join(fc), '-map', '[out]', '-an', '-c:v', 'libx264', '-crf', '14', '-t',
            f"{s['t1'] - s['t0']:.4f}", out]
    subprocess.run(cmd, check=True)
    manifest[str(s['shot'])] = {'file': out, 't0': s['t0'], 't1': s['t1'], 'who': [c['who'] for c in crops],
                                'missing': [c['who'] for c in s['crops'] if c not in crops]}
    print('done', s['shot'], [c['who'] for c in crops], flush=True)
json.dump(manifest, open(manifest_path, 'w'), indent=1)
