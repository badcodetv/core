"""Prepare LatentSync jobs for talking shots on a Premiere timeline, one job per SPEAKER, on a crop of
that speaker's face (upscaled when small). LatentSync syncs only the largest face and refuses faces
under 50x80 px, so a crop is how a two-hander, or a face in a wide shot, gets synced at all.

Built for Stupidity Optimised rough 3 (2026-11-02). Inputs:
  state   the bridge state file of the sequence (V1 picture, A2 voices with clip Volume)
  lines   voice-lines.json ({lines:[{id, shot, who}]}); a line's clip on A2 is named <id>.wav
  faces   faces.json from a face pass: {shot: {samples: [[t, [[x1,y1,x2,y2,score], ...]], ...]}}
  rules   {shot: {who: "L"|"R"|"T"|"B"|"big"}}: which face is whose
  swaps   optional {line id: wav path} to sync to a new take placed at the old line's start

For each shot: window = its speakers' lines +-0.4 s, inside the shot. Writes, under <work>/<shot>/:
  base.mp4 (the window's picture, 25 fps, 1280x720), and per speaker crop-<who>.mp4 + <who>.wav
(only that speaker's lines, silence elsewhere, so the mouth shuts when they are not talking), plus
jobs.json for latentsync-batch.py and shots.json for crop-sync-compose.py.

  python scripts/lipsync/crop-sync-prep.py state.json lines.json faces.json rules.json work/ [swaps.json]
"""
import json, math, os, subprocess, sys
import numpy as np

st, lines, faces, rules, work = [json.load(open(a)) if a.endswith('.json') else a for a in sys.argv[1:6]]
swaps = json.load(open(sys.argv[6])) if len(sys.argv) > 6 else {}
V = sorted(st['videoTracks'][0]['items'], key=lambda c: c['start'])
A2 = {a['name'].rsplit('.', 1)[0]: a for a in st['audioTracks'][1]['items']}
FPS, W, H, SR = 25, 1280, 720, 16000


def level_db(c):
    for comp in c.get('components', []):
        if comp['displayName'] == 'Volume':
            for p in comp['params']:
                if p['name'] == 'Level':
                    return 20 * math.log10(max(p['value'], 1e-6) / 0.17782794)
    return 0.0


def shot_span(shot):
    cs = [c for c in V if c['name'].startswith(f'so-{shot:02d}-') or c['name'].startswith(f'{shot}b.')]
    return min(c['start'] for c in cs), max(c['end'] for c in cs)


def render_base(t0, t1, out):
    parts, k = [], 0
    for c in V:
        a, b = max(c['start'], t0), min(c['end'], t1)
        if b - a < 1e-3:
            continue
        p = f'{out}.p{k}.mp4'; k += 1
        src = c['inPoint'] + (a - c['start'])
        if c['mediaPath'].lower().endswith(('.jpg', '.png')):
            cmd = ['ffmpeg', '-v', 'error', '-y', '-loop', '1', '-t', f'{b - a:.4f}', '-i', c['mediaPath']]
        else:
            cmd = ['ffmpeg', '-v', 'error', '-y', '-ss', f'{src:.4f}', '-t', f'{b - a:.4f}', '-i', c['mediaPath']]
        cmd += ['-an', '-vf', f'scale={W}:{H},setsar=1,fps={FPS}', '-c:v', 'libx264', '-crf', '12', '-pix_fmt', 'yuv420p', p]
        subprocess.run(cmd, check=True); parts.append(p)
    lst = out + '.txt'
    open(lst, 'w').write(''.join(f"file '{p}'\n" for p in parts))
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-f', 'concat', '-safe', '0', '-i', lst, '-c', 'copy', out], check=True)
    for p in parts:
        os.remove(p)
    os.remove(lst)


def decode(path, ss, dur):
    b = subprocess.run(['ffmpeg', '-v', 'error', '-ss', f'{ss:.4f}', '-t', f'{dur:.4f}', '-i', path, '-ac', '1', '-ar', str(SR),
                        '-f', 'f32le', '-'], capture_output=True).stdout
    return np.frombuffer(b, np.float32)


def pick(fs, rule, prev):
    if not fs:
        return None
    if rule == 'big' or len(fs) == 1 and prev is None:
        return max(fs, key=lambda f: (f[2] - f[0]) * (f[3] - f[1]))
    if len(fs) == 1:  # one face found: keep it only if it is near where this speaker was
        f = fs[0]; cx = (f[0] + f[2]) / 2; cy = (f[1] + f[3]) / 2
        return f if abs(cx - prev[0]) < 120 and abs(cy - prev[1]) < 120 else None
    key = {'L': lambda f: f[0] + f[2], 'R': lambda f: -(f[0] + f[2]), 'T': lambda f: f[1] + f[3], 'B': lambda f: -(f[1] + f[3])}[rule]
    return sorted(fs, key=key)[0]


jobs, shots = [], []
for shot_s, who_rules in rules.items():
    shot = int(shot_s)
    ls = [l for l in lines if l['shot'] == shot and l['who'] in who_rules]
    s0, s1 = shot_span(shot)
    t0 = max(s0, min(A2[l['id']]['start'] for l in ls) - 0.4)
    t1 = min(s1, max(A2[l['id']]['start'] + (A2[l['id']]['end'] - A2[l['id']]['start']) for l in ls) + 0.4)
    t0 = round(t0 * 24) / 24; t1 = round(t1 * 24) / 24
    d = os.path.join(work, f'{shot:02d}'); os.makedirs(d, exist_ok=True)
    base = os.path.join(d, 'base.mp4')
    if not os.path.exists(base):
        render_base(t0, t1, base)
    samples = faces[shot_s]['samples']
    crops = []
    for who, rule in who_rules.items():
        boxes, prev = [], None
        for t, fs in samples:
            f = pick([x[:4] for x in fs], rule, prev)
            if f:
                boxes.append(f); prev = ((f[0] + f[2]) / 2, (f[1] + f[3]) / 2)
        if not boxes:
            print('no face for', shot, who); continue
        B = np.array(boxes)
        ux1, uy1, ux2, uy2 = B[:, 0].min(), B[:, 1].min(), B[:, 2].max(), B[:, 3].max()
        fh = float(np.median(B[:, 3] - B[:, 1]))
        cx, cy = (ux1 + ux2) / 2, (uy1 + uy2) / 2
        hw = max((ux2 - ux1) / 2 + 0.9 * fh, 1.3 * fh); hh = max((uy2 - uy1) / 2 + 0.9 * fh, 1.3 * fh)
        x1, x2, y1, y2 = cx - hw, cx + hw, cy - hh, cy + hh
        # keep every other speaker's face out of this crop
        for ow, orule in who_rules.items():
            pass
        others = [x[:4] for t, fs in samples for x in fs if not any(abs(x[0] - b[0]) < 30 and abs(x[1] - b[1]) < 30 for b in boxes)]
        for o in others:
            if o[2] < ux1:
                x1 = max(x1, o[2] + 6)
            elif o[0] > ux2:
                x2 = min(x2, o[0] - 6)
            elif o[3] < uy1:
                y1 = max(y1, o[3] + 6)
            elif o[1] > uy2:
                y2 = min(y2, o[1] - 6)
        x1, y1 = max(0, int(x1)) // 2 * 2, max(0, int(y1)) // 2 * 2
        x2, y2 = min(W, int(x2)) // 2 * 2, min(H, int(y2)) // 2 * 2
        scale = min(4.0, max(1.0, 230 / fh))
        ow_, oh_ = int((x2 - x1) * scale) // 2 * 2, int((y2 - y1) * scale) // 2 * 2
        crop = os.path.join(d, f'crop-{who}.mp4')
        if not os.path.exists(crop):
            subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', base, '-vf', f'crop={x2 - x1}:{y2 - y1}:{x1}:{y1},scale={ow_}:{oh_}:flags=lanczos',
                            '-c:v', 'libx264', '-crf', '12', '-pix_fmt', 'yuv420p', crop], check=True)
        # this speaker's lines only, at their timeline places, silence elsewhere
        n = int(round((t1 - t0) * SR)); buf = np.zeros(n, np.float32)
        for l in ls:
            if l['who'] != who:
                continue
            a = A2[l['id']]
            src, g = (swaps[l['id']], 0.0) if l['id'] in swaps else (a['mediaPath'], level_db(a))
            dur = (a['end'] - a['start']) if l['id'] not in swaps else 60
            x = decode(src, 0 if l['id'] in swaps else a['inPoint'], dur) * 10 ** (g / 20)
            i = int(round((a['start'] - t0) * SR)); x = x[:max(0, n - i)]; buf[i:i + len(x)] += x
        wav = os.path.join(d, f'{who}.wav')
        subprocess.run(['ffmpeg', '-v', 'error', '-y', '-f', 'f32le', '-ar', str(SR), '-ac', '1', '-i', '-', wav], input=buf.tobytes(), check=True)
        jobs.append({'id': f'{shot:02d}-{who}', 'video': os.path.abspath(crop), 'audio': os.path.abspath(wav),
                     'out': os.path.abspath(os.path.join(d, f'synced-{who}.mp4'))})
        crops.append({'who': who, 'box': [x1, y1, x2, y2], 'scale': scale, 'synced': jobs[-1]['out'], 'face_h': fh})
    shots.append({'shot': shot, 't0': t0, 't1': t1, 'base': os.path.abspath(base), 'crops': crops})
    print(shot, f'{t0:.2f}-{t1:.2f}', [(c['who'], c['box'], round(c['scale'], 1)) for c in crops], flush=True)
json.dump(jobs, open(os.path.join(work, 'jobs.json'), 'w'), indent=1)
json.dump(shots, open(os.path.join(work, 'shots.json'), 'w'), indent=1)
