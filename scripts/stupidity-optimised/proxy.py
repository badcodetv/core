"""Offline watch copy of a rough plan (rough3-plan.py / rough4-plan.py output), for measuring and for Gemini to watch.
Never for Jack: he watches the Premiere timeline. 640x360, V1 with V2 and V3 laid over it, A1 (clip sound at the plan's
level, None = muted), A2 voices and A3 music at their clip Volume.

  python3 scripts/stupidity-optimised/proxy.py plan.json OUT_DIR   ->  OUT_DIR/proxy.mp4, mix.wav, A1/A2/A3.wav
"""
import json, os, subprocess, sys
import numpy as np

P = json.load(open(sys.argv[1])); out = sys.argv[2]; os.makedirs(out, exist_ok=True)
SR, FPS = 48000, 24
END = P['total']


def lin(w):
    return '/mnt/' + w[0].lower() + w[2:].replace('\\', '/')


def dec(path, ss, dur):
    b = subprocess.run(['ffmpeg', '-v', 'error', '-ss', f'{ss:.4f}', '-t', f'{dur:.4f}', '-i', path, '-vn', '-ac', '2', '-ar', str(SR),
                        '-f', 'f32le', '-'], capture_output=True).stdout
    return np.frombuffer(b, np.float32).reshape(-1, 2)


N = int(END * SR) + SR
mix = np.zeros((N, 2), np.float32)
a1 = {round(t * FPS): lv for t, lv in P['a1']}
tracks = {'A1': [], 'A2': [], 'A3': []}
for p, t, i, d, tr in P['video']:
    if tr == 0 and p.lower().endswith('.mp4') and '\\gfx\\' not in p:
        lv = a1.get(round(t * FPS))
        if lv is not None:
            tracks['A1'].append((lin(p), t, i, d, lv))
for p, t, tr, lv in P['audio']:
    if lv is not None:
        tracks['A2' if tr == 1 else 'A3'].append((lin(p), t, 0, 60, lv))
for name, items in tracks.items():
    buf = np.zeros((N, 2), np.float32)
    for path, t, i, d, lv in items:
        a = dec(path, i, d) * (10 ** (lv / 20))
        k = int(round(t * SR)); a = a[:N - k]; buf[k:k + len(a)] += a
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-f', 'f32le', '-ar', str(SR), '-ac', '2', '-i', '-', f'{out}/{name}.wav'],
                   input=buf.tobytes())
    mix += buf
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-f', 'f32le', '-ar', str(SR), '-ac', '2', '-i', '-', f'{out}/mix.wav'], input=mix.tobytes())

# picture: V1 as segments, concatenated
V1 = sorted([v for v in P['video'] if v[4] == 0], key=lambda v: v[1])
lst = open(f'{out}/v.txt', 'w')
for k, (p, t, i, d, tr) in enumerate(V1):
    seg = f'{out}/seg{k:03d}.mp4'; path = lin(p); nf = round(d * FPS)
    if path.lower().endswith(('.jpg', '.png')):
        cmd = ['ffmpeg', '-v', 'error', '-y', '-loop', '1', '-t', f'{d:.4f}', '-i', path]
        vf = f"scale=1280:720,zoompan=z='1+0.09*on/{max(nf, 1)}':d=1:s=640x360:fps=24,setsar=1"
    else:
        cmd = ['ffmpeg', '-v', 'error', '-y', '-ss', f'{i:.4f}', '-t', f'{d + 0.1:.4f}', '-i', path]
        vf = 'scale=640:360,fps=24,setsar=1'
    subprocess.run(cmd + ['-an', '-vf', vf, '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '24', '-frames:v', str(nf), seg],
                   check=True)
    lst.write(f"file '{seg}'\n")
lst.close()
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-f', 'concat', '-safe', '0', '-i', f'{out}/v.txt', '-c', 'copy', f'{out}/v1.mp4'],
               check=True)
# V2 then V3 over it
over = sorted([v for v in P['video'] if v[4] > 0], key=lambda v: (v[4], v[1]))
cmd = ['ffmpeg', '-v', 'error', '-y', '-i', f'{out}/v1.mp4']
fc, last = [], '0:v'
for k, (p, t, i, d, tr) in enumerate(over):
    cmd += ['-ss', f'{i:.4f}', '-t', f'{d:.4f}', '-itsoffset', f'{t:.4f}', '-i', lin(p)]
    fc.append(f'[{k + 1}:v]scale=640:360,format=yuva420p[s{k}];[{last}][s{k}]overlay=eof_action=pass:repeatlast=0[o{k}]')
    last = f'o{k}'
cmd += ['-i', f'{out}/mix.wav', '-filter_complex', ';'.join(fc), '-map', f'[{last}]', '-map', f'{len(over) + 1}:a',
        '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '26', '-c:a', 'aac', '-b:a', '128k', '-t', f'{END:.3f}', f'{out}/proxy.mp4']
subprocess.run(cmd, check=True)
for f in os.listdir(out):
    if f.startswith('seg'):
        os.remove(os.path.join(out, f))
print('done', f'{out}/proxy.mp4')
