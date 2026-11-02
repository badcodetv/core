"""Stupidity Optimised rough 4: rough 3, tighter (Jack, 2 Nov 2026: "trim the existing clips and speed up the speech").

One time map g (rough-3 time -> rough-4 time) drives everything:
  - each voice line plays faster (fast-voices.py), so its span shrinks to the new file's length;
  - a gap between lines shorter than KEEP stays as it is; a longer one keeps KEEP plus SQUEEZE of the rest;
  - the label replay (Scene 15) squeezes less (LABEL_RATE) so the labels stay readable;
  - the film's tail after the last line is capped at TAIL.
V1 clips keep their in-point and lose their tail (with their linked clip sound on A1). Lip-sync clips (V2) and
graphics (V3) are re-timed frame by frame through g into new files, so mouths and on-screen prompts stay on the
faster words. Flashes keep their own speed, centred on the moved cut. Music cues start at g(start) and are re-cut
to their new length with a fade. Nothing in rough 3 or its media is touched.

  python3 scripts/stupidity-optimised/rough4-plan.py rough3-plan.json fast.json out/rough4-plan.json [--no-render]
"""
import json, math, os, subprocess, sys
import numpy as np

KEEP, SQUEEZE, LABEL_RATE, TAIL = 0.3, 0.5, 0.8, 2.5
MIN_PIECE = 6 / 24
FPS = 24
plan_in, fast_path, out = sys.argv[1:4]
RENDER = '--no-render' not in sys.argv
P = json.load(open(plan_in))
FAST = json.load(open(fast_path))
ROOT = '/mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/optimised stupidity/clips/film'
R4 = f'{ROOT}/r4'
os.makedirs(f'{R4}/v2', exist_ok=True); os.makedirs(f'{R4}/gfx', exist_ok=True); os.makedirs(f'{R4}/music', exist_ok=True)


def lin(w):
    return '/mnt/' + w[0].lower() + w[2:].replace('\\', '/')


def win(p):
    return p[5].upper() + ':' + p[6:].replace('/', '\\')


def probe(p):
    return float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', p],
                                capture_output=True, text=True).stdout)


# ---- the time map
voices = sorted([a for a in P['audio'] if a[2] == 1], key=lambda a: a[1])
labels = [v for v in P['video'] if 'gfx-label-' in v[0]]
LAB0, LAB1 = min(v[1] for v in labels), max(v[1] + v[3] for v in labels)
spans = []
for p, t, tr, lv in voices:
    name = os.path.basename(lin(p))[:-4]
    spans.append((t, t + probe(lin(p)), FAST[name]['dur_out'], name))

knots = [(0.0, 0.0)]


def gap_to(t_end):
    """advance the map across a voiceless stretch from the last knot to t_end"""
    o, n = knots[-1]
    gap = t_end - o
    if gap <= 0:
        return
    # the label replay sits inside a gap: squeeze it at LABEL_RATE, the rest normally
    pieces = []
    if o < LAB1 and t_end > LAB0:
        a, b = max(o, LAB0), min(t_end, LAB1)
        pieces = [(o, a, None), (a, b, LABEL_RATE), (b, t_end, None)]
    else:
        pieces = [(o, t_end, None)]
    free = sum(b - a for a, b, r in pieces if r is None)
    free_new = free if free <= KEEP else KEEP + (free - KEEP) * SQUEEZE
    k = free_new / free if free > 0 else 1
    for a, b, r in pieces:
        if b > a:
            knots.append((b, knots[-1][1] + (b - a) * (r if r else k)))


for t0, t1, dnew, name in spans:
    gap_to(t0)
    o, n = knots[-1]
    if t0 > o:  # overlapping lines (none expected)
        knots.append((t0, n + (t0 - o)))
    knots.append((t1, knots[-1][1] + dnew))
end_old = P['total']
o, n = knots[-1]
knots.append((end_old, n + min(TAIL, end_old - o)))
KO = np.array([k[0] for k in knots]); KN = np.array([k[1] for k in knots])
assert np.all(np.diff(KO) >= 0) and np.all(np.diff(KN) >= 0)


def g(t):
    return float(np.interp(t, KO, KN))


def ginv(t):
    return float(np.interp(t, KN, KO))


def q(t):
    return round(t * FPS) / FPS


# ---- frame re-timing through g
def retime(src, dst, t, i, d, alpha):
    """dst plays src[i:i+d] (placed at rough-3 time t) along g: frame k of dst = source time i + ginv(g(t)+k/24) - t"""
    nd = q(g(t + d)) - q(g(t))
    nout = max(1, round(nd * FPS))
    if not RENDER or (os.path.exists(dst) and os.path.getsize(dst) > 0):
        return nd
    pix, bpp = ('rgba', 4) if alpha else ('rgb24', 3)
    fsz = 1280 * 720 * bpp
    dec = subprocess.Popen(['ffmpeg', '-v', 'error', '-ss', f'{i:.4f}', '-t', f'{d + 0.2:.4f}', '-i', src, '-f', 'rawvideo',
                            '-pix_fmt', pix, '-s', '1280x720', '-r', str(FPS), '-'], stdout=subprocess.PIPE)
    enc_args = (['-c:v', 'prores_ks', '-profile:v', '4444', '-pix_fmt', 'yuva444p10le'] if alpha else
                ['-c:v', 'libx264', '-crf', '14', '-pix_fmt', 'yuv420p'])
    enc = subprocess.Popen(['ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', pix, '-s', '1280x720', '-r', str(FPS),
                            '-i', '-'] + enc_args + [dst], stdin=subprocess.PIPE)
    cur, cur_idx = None, -1
    for k in range(nout):
        want = max(0, round((ginv(q(g(t)) + k / FPS) - t) * FPS))
        while cur_idx < want:
            b = dec.stdout.read(fsz)
            if len(b) < fsz:
                break
            cur, cur_idx = b, cur_idx + 1
        enc.stdin.write(cur)
    enc.stdin.close(); enc.wait(); dec.stdout.close(); dec.wait()
    return nd


# ---- video
video = []
V1 = sorted([v for v in P['video'] if v[4] == 0], key=lambda v: v[1])
starts = [q(g(v[1])) for v in V1] + [q(g(P['total']))]
v1 = []
for k, (p, t, i, d, tr) in enumerate(V1):
    v1.append([p, starts[k], i, starts[k + 1] - starts[k], 0, t])
# a piece too short to read joins its neighbour: the earlier clip runs on if its media allows, else the later starts early
merged = []
for v in v1:
    if v[3] < MIN_PIECE - 1e-6 and merged:
        merged[-1][3] += v[3]
        continue
    merged.append(v)
if merged and merged[0][3] < MIN_PIECE - 1e-6 and len(merged) > 1:
    merged[1][1] = merged[0][1]; merged[1][3] += merged[0][3]; merged.pop(0)
for p, t, i, d, tr, t_old in merged:
    video.append([p, t, i, d, 0, t_old])

retimed = []
for p, t, i, d, tr in P['video']:
    if tr == 0:
        continue
    src = lin(p)
    base = os.path.basename(src)
    if 'gfx-flash' in base:  # its own speed, centred on the moved cut
        c = q(g(t + d / 2))
        video.append([p, c - d / 2, i, d, tr, t]); continue
    alpha = base.endswith('.mov')
    stem = base.rsplit('.', 1)[0]
    dst = f'{R4}/{"gfx" if alpha else "v2"}/{stem}-r4-{round(t * FPS)}.{"mov" if alpha else "mp4"}'
    nd = retime(src, dst, t, i, d, alpha)
    video.append([win(dst), q(g(t)), 0, nd, tr, t])
    retimed.append({'src': src, 'dst': dst, 't_r3': t, 'in': i, 'dur_r3': d, 'dur_r4': nd})
    print('retimed', base, f'{d:.2f} -> {nd:.2f}', flush=True)

# ---- audio
audio = []
FV = f'{ROOT}/voices/fast-r4'
for p, t, tr, lv in voices:
    name = os.path.basename(lin(p))[:-4]
    audio.append([win(f'{FV}/{name}.wav'), q(g(t)), 1, lv])
for p, t, tr, lv in [a for a in P['audio'] if a[2] == 2]:
    src = lin(p)
    D = probe(src)
    nd = min(D, q(g(t + D)) - q(g(t)))
    dst = f'{R4}/music/{os.path.basename(src)[:-4]}-r4.wav'
    if RENDER and not os.path.exists(dst):
        fo = min(2.5, nd / 3)
        subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', src, '-t', f'{nd:.3f}', '-af',
                        f'afade=t=out:st={nd - fo:.3f}:d={fo:.3f}', dst], check=True)
    audio.append([win(dst), q(g(t)), 2, lv])

# clip sound levels: the rough 3 level of the piece each rough 4 piece came from
a1_r3 = {round(t * FPS): lv for t, lv in P['a1']}
a1 = []
for p, t, i, d, tr, t_old in video:
    if tr == 0 and p.lower().endswith('.mp4') and '\\gfx\\' not in p:
        a1.append([t, a1_r3.get(round(t_old * FPS))])

total = max(t + d for _, t, _, d, _, _ in video)
plan = {'video': [[p, round(t, 4), round(i, 4), round(d, 4), tr] for p, t, i, d, tr, _ in sorted(video, key=lambda v: (v[4], v[1]))],
        'audio': [[p, round(t, 4), tr, lv] for p, t, tr, lv in sorted(audio, key=lambda a: (a[2], a[1]))],
        'a1': sorted(a1), 'total': round(total, 4), 'knots': knots, 'retimed': retimed}

for tr in (0, 1, 2):
    vs = sorted([v for v in plan['video'] if v[4] == tr], key=lambda v: v[1])
    for a, b in zip(vs, vs[1:]):
        if a[1] + a[3] > b[1] + 0.02:
            print(f'V{tr + 1} overlap @{a[1]:.2f}+{a[3]:.2f} > {b[1]:.2f}')
        if tr == 0 and b[1] - (a[1] + a[3]) > 0.02:
            print(f'V1 gap at {a[1] + a[3]:.2f}')
print('V1 shortest piece', min(v[3] for v in plan['video'] if v[4] == 0))
json.dump(plan, open(out, 'w'), indent=0)
print('video', len(plan['video']), 'audio', len(plan['audio']), 'total', plan['total'], f'({int(total // 60)}:{total % 60:04.1f})')
