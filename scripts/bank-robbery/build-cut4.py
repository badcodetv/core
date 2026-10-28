#!/usr/bin/env python3
"""The Bank Robbery, cut 4 (2026-10-08): Jack's notes on cut 3.

  "the montage bit showing everyone should only show a few ... have the name on the screen long enough to be read.
   forget the way of showing stop the boats, it should be a newspaper headline spinning graphic ... the model houses
   arent working. the night before the robbery, they get pissed, this should be funnier ... a compilation of these
   characters drinking, throwing up, playing darts and pool. the person looking out the window ... david lynch type
   of cinematography. [the barrier shot] should be the vibe of the protest/riot ... show real footage of the cafe
   instead of the model where they talk about buying it. the scene with the guns looks like ai slop. the cafe being
   sold should be the cleaner outside in the rain ... she looks up at the sky and the camera pans up. keep the cool
   kebab shop at the end."

Cut 4 = cut 3 (edl-cut2.json + edl-cut3.json's swaps) with the RULES below applied, then every start time worked
out again from the top, because lengths change. Narrator lines keep their offset from the picture they sat on.
Music is cut 3's ten cues, moved with the picture. Writes edl-cut4.json and edl-cut4.txt; new pieces go to
<project>/clips/cut4/ as c4-*.mp4 and m??d-*.wav.
"""
import json, os, re, shutil, subprocess, wave, array, math
import numpy as np
H = os.path.dirname(os.path.abspath(__file__))
P = '/mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/bank robbery'
V5, MUS, NAR, OUT = P + '/vids/v5', P + '/music', P + '/narrator', P + '/clips/cut4'
SEARCH = [OUT, P + '/clips/cut3', P + '/clips/cut2', P + '/clips/cut1', P + '/vids/v3', P + '/vids']
os.makedirs(OUT, exist_ok=True)
F, SR = 24, 48000
snap = lambda t: round(t * F) / F
ENC = ['-c:v', 'libx264', '-crf', '17', '-preset', 'medium', '-pix_fmt', 'yuv420p', '-r', '24', '-c:a', 'aac', '-ar', '48000', '-ac', '2', '-b:a', '192k', '-movflags', '+faststart']
TALK_TARGET, BED_NARR, BED_OPEN, NARR_DB = -19.0, -50.0, -36.0, -3.0
def run(a): subprocess.run(['ffmpeg', '-v', 'error', '-y'] + a, check=True)
def src(name):
    for d in SEARCH:
        if os.path.exists(f'{d}/{name}'): return f'{d}/{name}'
    raise FileNotFoundError(name)
def dur_of(path): return float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', path], capture_output=True, text=True).stdout)
def frames_db(path, ss=0.0, t=None):
    a = ['ffmpeg', '-v', 'error', '-ss', f'{ss}'] + (['-t', f'{t}'] if t else []) + ['-i', path, '-vn', '-ac', '1', '-ar', '16000', '-af', 'highpass=f=120,lowpass=f=4000', '-f', 's16le', '-']
    x = array.array('h', subprocess.run(a, capture_output=True).stdout); w = 800
    return [10 * math.log10(sum(v * v for v in x[i:i + w]) / w / 32768 ** 2 + 1e-10) for i in range(0, len(x) - w, w)]
def rms(path, ss, t):
    d = frames_db(path, ss, t)
    return 10 * math.log10(sum(10 ** (v / 10) for v in d) / len(d)) if d else -99.0
def bed_db(path, inn, dur, narrated):
    r = rms(path, inn, dur)
    return round(max(-30.0, min(0.0, BED_NARR - r)) if narrated else max(-14.0, min(4.0, BED_OPEN - r)), 1)
def segments(path):
    db = frames_db(path)
    if not db: return []
    s = sorted(db); thr = max(s[int(len(s) * .2)] + 7, s[int(len(s) * .95)] - 22); on = [v > thr for v in db]; segs = []; i = 0
    while i < len(on):
        if on[i]:
            j = i
            while j < len(on) and on[j]: j += 1
            if segs and i * .05 - segs[-1][1] < .35: segs[-1][1] = j * .05
            else: segs.append([i * .05, j * .05])
            i = j
        else: i += 1
    return [[round(a, 2), round(b, 2)] for a, b in segs if b - a >= .2]
SPJ = f'{H}/speech-cut4.json'
SP = json.load(open(SPJ)) if os.path.exists(SPJ) else {}
def talk(clip, keep=None, pre=0.0, minseg=0.3):
    """build-cut2.py's T(): a talking clip from vids/v5 with its pauses cut out and its speech levelled. Returns [file, dur]."""
    f = f'c4-t-{clip}.mp4'; path = f'{V5}/{clip}.mp4'
    if clip not in SP: SP[clip] = segments(path)
    segs = [s for s in SP[clip] if s[1] - s[0] >= minseg]
    if keep is not None: segs = [SP[clip][i] for i in keep]
    cuts = []
    for k, (a, b) in enumerate(segs):
        a2, b2 = max(0.0, a - (0.3 if k or not pre else pre)), min(7.95, b + (0.3 if k < len(segs) - 1 else 0.6))
        if cuts and a2 <= cuts[-1][1] + 0.05: cuts[-1][1] = b2
        else: cuts.append([a2, b2])
    d = sum(b - a for a, b in cuts)
    if not os.path.exists(f'{OUT}/{f}'):
        lvl = sorted(v for a, b in segs for v in frames_db(path, a, b - a)); top = lvl[int(len(lvl) * .9)] if lvl else -30
        gain = max(-10.0, min(14.0, TALK_TARGET - top)); fc = []; lab = ''
        for k, (a, b) in enumerate(cuts):
            punch = ',scale=1408:792,crop=1280:720' if k % 2 else ''
            fc.append(f'[0:v]trim={a}:{b},setpts=PTS-STARTPTS,scale=1280:720,setsar=1{punch}[v{k}]')
            fc.append(f'[0:a]atrim={a}:{b},asetpts=PTS-STARTPTS,afade=t=in:d=0.02,afade=t=out:st={b - a - 0.06:.3f}:d=0.06[a{k}]'); lab += f'[v{k}][a{k}]'
        fc.append(f'{lab}concat=n={len(cuts)}:v=1:a=1[vc][am]'); fc.append('[vc]tpad=stop_mode=clone:stop_duration=0.2[v]'); fc.append(f'[am]volume={gain:.1f}dB,alimiter=limit=0.7:level=disabled,apad=pad_dur=0.2[a]')
        run(['-i', path, '-filter_complex', ';'.join(fc), '-map', '[v]', '-map', '[a]'] + ENC + [f'{OUT}/{f}'])
    print(f'  talk {clip}: phrases {SP[clip]} -> {len(cuts)} cut(s), {d:.2f} s')
    return f, snap(d)
def copy(clip):
    f = f'c4-{clip}.mp4'
    if not os.path.exists(f'{OUT}/{f}'): shutil.copyfile(f'{V5}/{clip}.mp4', f'{OUT}/{f}')
    return f

# ---------------- cut 3 as a list ----------------
C2 = json.load(open(f'{H}/edl-cut2.json')); C3 = json.load(open(f'{H}/edl-cut3.json'))
LV = {(l[0], round(l[1], 2)): l[2] for l in C2['levels']}
old = [dict(item=e[0], start=e[1], inn=e[2], dur=e[3], at=e[5], lvl=LV.get((e[5], round(e[1], 2)), 0.0)) for e in C2['entries']]
for new, st, inn, d, _, _, lvl in C3['swaps']:
    e = [x for x in old if abs(x['start'] - st) < 0.02][0]; e.update(item=new, inn=inn, lvl=lvl)
def at_time(t): return max(i for i, e in enumerate(old) if e['start'] <= t + 1e-6)
name_idx = lambda name, nth=0: [i for i, e in enumerate(old) if e['item'] == name][nth]
narr_old = {x[0][:3]: x for x in C2['narr']}

# ---------------- the rules: old index -> list of new entries (or [] to drop) ----------------
R = {}
def U(f, inn, d, narrated=True, db=None, note=''):
    p = src(f); assert inn + d <= dur_of(p) + 0.02, (f, inn, d, dur_of(p))
    return dict(item=f, inn=snap(inn), dur=snap(d), at=2, lvl=db if db is not None else bed_db(p, inn, d, narrated), note=note)
def Tk(f_d, note): return dict(item=f_d[0], inn=0.0, dur=f_d[1], at=0, lvl=0.0, note=note)
# 1 the name cards: four, each on screen 2.7 s (0.6 s of the shot, then 2.1 s frozen with the name)
for tag in ('02-fixer', '04-governor', '06-presenter', '07-platform', '08-accountant', '10-turquoise'): R[name_idx(f'c2b-card-{tag}.mp4')] = []
for tag, oldname in (('01-ex', 'c2b-card-01-ex.mp4'), ('03-donor', 'c2b-card-03-donor.mp4'), ('05-proprietor', 'c2b-card-05-proprietor.mp4'), ('09-drivers', 'c3-card-09-drivers.mp4')):
    R[name_idx(oldname)] = [U(f'c4b-card-{tag}.mp4', 0.0, 2.7, False, db=-6.0, note='name card, 2.7 s')]
# 2 the two headlines: spinning front pages (stills made in Flow, the spin in ffmpeg)
R[name_idx('c2b-text-headline-blue.mp4')] = [U('c4-paper-blue.mp4', 0.0, 5.0, db=0.0, note='spinning front page')]
R[name_idx('c2b-hold-s05-headline-red.mp4')] = [U('c4-paper-red.mp4', 0.0, 4.2, False, db=0.0, note='spinning front page')]
R[name_idx('c2-t-s05c-red-side-1-p.mp4')] = [Tk(talk('s05e-papers-1'), 'talk: which one is true')]
R[name_idx('c2-t-s05c-red-side-2.mp4')] = [Tk(talk('s05e-papers-2'), 'talk: I need them to reply')]
# 3 the night before: a compilation. The narrator's line runs over the first four shots; the bucket plays clear.
NB = name_idx('c3-s07-night-before.mp4')
R[NB] = [U('c3-s07-night-before.mp4', 0.6, 1.8, note='night: laughing'), U(copy('s07d-pints'), 3.6, 2.5, note='night: pints'),
         U(copy('s07e-darts'), 3.0, 2.6, note='night: darts'), U(copy('s07f-pool'), 0.9, 2.5, note='night: pool'),
         U(copy('s07g-bucket'), 0.2, 2.6, False, note='night: the bucket, no narrator')]
# 4 the riot, in the look of the barrier shot (s08-march, which stays)
R[name_idx('s08a-placards.mp4')] = [U(copy('s08a-placards'), 0.5, 7.0, note='riot: placards')]
R[name_idx('s08b-remote-window.mp4')] = [U(copy('s08b-remote-window'), 0.0, old[name_idx('s08b-remote-window.mp4')]['dur'], db=-12.0, note='the window')]
MG = name_idx('c2b-t-s08c-megaphones.mp4'); n18 = narr_old['n18']
R[MG] = [Tk(talk('s08c-megaphones', pre=max(0.3, min(1.3, n18[1] + n18[3] + 0.15 - old[MG]['start']))), 'talk: megaphones')]
R[name_idx('hold-s08-megaphones.mp4')] = [U(copy('s08e-bank'), 0.8, old[name_idx('hold-s08-megaphones.mp4')]['dur'], note='riot: the bank')]
R[name_idx('s09-walk.mp4')] = [U(copy('s09-walk'), 0.3, old[name_idx('s09-walk.mp4')]['dur'], note='riot: the walk')]
# 5 the cafe, not the model: one shot in place of the two model shots, slowed to fit the narrator
PL, PT = name_idx('s05-plan.mp4', 1), name_idx('s11d-pricetags.mp4'); need = old[PL]['dur'] + old[PT]['dur']
if not os.path.exists(f'{OUT}/c4-s11e-cafe-for-sale.mp4'):
    k = (need + 0.3) / 7.9
    run(['-i', f'{V5}/s11e-cafe-for-sale.mp4', '-filter_complex', f'[0:v]setpts={k:.4f}*PTS[v];[0:a]atempo={1 / k:.4f}[a]', '-map', '[v]', '-map', '[a]'] + ENC + [f'{OUT}/c4-s11e-cafe-for-sale.mp4'])
R[PL] = [U('c4-s11e-cafe-for-sale.mp4', 0.0, need, note='the cafe, for sale')]; R[PT] = []
# 6 the standoff. Flow refused to animate the new plate twice (pistols pointed at people in the start frame), so the
#   plate is moved in ffmpeg instead: a slow push with a little drift, a pulsing light and grain. The sound is the
#   old clips' (the three shouted lines and the bell). The faces are dark and far off, so no lips can be read.
STILL = P + '/images/scenes-v5/s12g-standoff.jpg'
ST, SH = name_idx('c2-t-s12a-standoff-talk.mp4'), name_idx('s12a-standoff.mp4')
def moved(f, d, z0, z1, cx, cy, audio, ass):
    if os.path.exists(f'{OUT}/{f}'): return
    N = int(round((d + 0.25) * F))
    vf = (f"scale=2752:1536,zoompan=z='{z0}+{z1 - z0}*on/{N}':x='iw*{cx}-(iw/zoom/2)+5*sin(on/9)':y='ih*{cy}-(ih/zoom/2)+3*sin(on/7)':d={N}:s=1280x720:fps=24,"
          f"eq=brightness='0.045*sin(2*PI*t*1.1)':eval=frame,noise=alls=7:allf=t,format=yuv420p")
    run(['-loop', '1', '-framerate', '24', '-i', STILL, '-ss', f'{ass}', '-i', audio, '-filter_complex', f'[0:v]{vf}[v];[1:a]apad[a]', '-map', '[v]', '-map', '[a]', '-t', f'{d + 0.25:.3f}'] + ENC + [f'{OUT}/{f}'])
moved('c4-t-s12g-standoff.mp4', old[ST]['dur'], 1.0, 1.10, 0.5, 0.5, src('c2-t-s12a-standoff-talk.mp4'), 0.0)
moved('c4-s12g-standoff-balance.mp4', old[SH]['dur'], 1.9, 2.15, 0.5, 0.36, src('s12a-standoff.mp4'), old[SH]['inn'])
R[ST] = [dict(item='c4-t-s12g-standoff.mp4', inn=0.0, dur=old[ST]['dur'], at=0, lvl=0.0, note='talk: who talked (new plate moved in ffmpeg, old sound)')]
R[SH] = [dict(item='c4-s12g-standoff-balance.mp4', inn=0.0, dur=old[SH]['dur'], at=2, lvl=old[SH]['lvl'], note='for balance: the same plate, punched in on the Presenter')]
# 7 the ending: Denise in the rain, the board, the sky. Then the old neon kebab shop, untouched.
R[name_idx('c3-s12b-count.mp4')] = [U(copy('s12h-denise-rain'), 1.0, 4.5, False, db=0.0, note='Denise and the SOLD board')]
R[name_idx('c3-s12e-sold.mp4')] = [U(copy('s12i-denise-face'), 0.3, 7.5, False, db=0.0, note='she looks up; the camera tilts to the sky')]

# ---------------- ripple ----------------
new, t, first = [], 0.0, {}
for i, e in enumerate(old):
    outs = R.get(i, [dict(item=e['item'], inn=e['inn'], dur=e['dur'], at=e['at'], lvl=e['lvl'], note='')])
    first[i] = (t, sum(o['dur'] for o in outs))
    for o in outs: o['start'] = snap(t); new.append(o); t = snap(t + o['dur'])
first[PT] = (first[PL][0] + old[PL]['dur'], old[PT]['dur'])          # the price tags' place inside the cafe shot
TOTAL = t
def mapt(x):
    """an old time -> the new time at the same fraction of the same shot"""
    i = at_time(min(x, old[-1]['start'] + old[-1]['dur'] - 0.01)); e = old[i]; st, d = first[i]
    return st + (x - e['start']) / e['dur'] * d if d else st
narr = []
for key, x in sorted(narr_old.items(), key=lambda kv: kv[1][1]):
    i = at_time(x[1]); narr.append([x[0], snap(first[i][0] + (x[1] - old[i]['start'])), 0, x[3], 0, 1])
levels = [[2, e['start'], e['lvl']] for e in new if e['at'] == 2] + [[1, n[1], NARR_DB] for n in narr]

# ---------------- music: cut 3's cues, moved with the picture ----------------
UNDER, VER = -33.0, 'd'
CUES = [  # stem, tune, old start, old end, source start, fade in, fade out, open LUFS
    ['m01', 'Covert Affair', 0.0, 47.8, 0.0, 0.3, 1.0, -20], ['m02', 'Cool Vibes', 46.9, 70.8, 0.0, 0.8, 0.5, -22],
    ['m03', 'Neon Laser Horizon', 70.59, 90.79, 12.8, 0.05, 0.06, -17], ['m04', 'Marty Gots a Plan', 90.79, 159.3, 0.0, 0.05, 1.0, -22],
    ['m05', 'Covert Affair', 166.5, 185.0, 60.0, 1.0, 1.2, -22], ['m06', 'Volatile Reaction', 184.2, 223.0, 0.0, 0.3, 1.0, -24],
    ['m07', 'Hitman', 222.3, 258.6, 0.0, 0.8, 1.2, -24], ['m08', 'Covert Affair', 257.8, 337.4, 90.0, 1.0, 1.2, -22],
    ['m09', 'Heartbreaking', 336.8, 345.58, 0.0, 0.4, 0.2, -21], ['m10', 'Neon Laser Horizon', 345.5, 351.0, 29.97, 0.03, 0.5, -18]]
KEB = [e for e in new if e['item'] == 's12f-kebab.mp4'][0]['start']
def decode(name, ss, tt):
    raw = subprocess.run(['ffmpeg', '-v', 'error', '-ss', f'{ss}', '-t', f'{tt}', '-i', f'{MUS}/{name}.mp3', '-ac', '2', '-ar', f'{SR}', '-f', 'f32le', '-'], capture_output=True).stdout
    return np.frombuffer(raw, dtype='<f4').reshape(-1, 2).astype(np.float64)
def lufs(name, ss, tt):
    e = subprocess.run(['ffmpeg', '-hide_banner', '-nostats', '-ss', f'{ss}', '-t', f'{tt}', '-i', f'{MUS}/{name}.mp3', '-af', 'ebur128', '-f', 'null', '-'], capture_output=True, text=True).stderr
    return float(re.findall(r'I:\s+(-?[\d.]+) LUFS', e)[-1])
RR = 100; n = int(TOTAL * RR) + 200; sp = np.zeros(n)
spans = sorted([[e['start'], e['start'] + e['dur']] for e in new if e['at'] == 0] + [[x[1], x[1] + x[3]] for x in narr]); merged = []
for a, b in spans:
    a, b = a - 0.3, b + 0.3
    if merged and a - merged[-1][1] < 1.2: merged[-1][1] = max(merged[-1][1], b)
    else: merged.append([a, b])
for a, b in merged: sp[max(0, int(a * RR)):int(b * RR)] = 1.0
k = int(0.8 * RR); sp = np.convolve(sp, np.ones(k) / k, mode='same')
music = []
for i, (stem, name, a0, b0, ss, fi, fo, openl) in enumerate(CUES):
    a = snap(mapt(a0)); b = snap(mapt(b0))
    if stem == 'm03': a = snap(first[name_idx('c2b-card-01-ex.mp4')][0] - 1.2)        # the fill, then the tune on the first card
    if stem == 'm04': b = snap(first[NB][0] + 0.4)                                    # out as the party starts
    if stem == 'm05': a = snap(first[NB][0] + first[NB][1] - 0.4)                     # in as the party ends
    if stem == 'm09': b = snap(KEB + 0.08)
    if stem == 'm10': a, b = KEB, TOTAL
    x = decode(name, ss, b - a); m = len(x); L = lufs(name, ss, b - a); tt = a + np.arange(m) / SR
    duck = np.interp(tt, np.arange(n) / RR, sp); g = 10 ** (((UNDER - L) * duck + (openl - L) * (1 - duck)) / 20)
    if fi: g *= np.clip(np.arange(m) / (fi * SR), 0, 1)
    if fo: g *= np.clip((m - np.arange(m)) / (fo * SR), 0, 1)
    y = np.clip(x * g[:, None], -0.97, 0.97); fn = f"{stem}{VER}-{name.lower().replace(' ', '-')}.wav"
    w = wave.open(f'{OUT}/{fn}', 'wb'); w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes((y * 32767).astype('<i2').tobytes()); w.close()
    music.append([fn, a, 0.0, snap(m / SR), 0, 3 + i % 2])

json.dump(SP, open(SPJ, 'w'), indent=0)
json.dump({'entries': [[e['item'], e['start'], e['inn'], e['dur'], 0, e['at']] for e in new], 'narr': narr, 'levels': levels, 'music': music, 'total': TOTAL}, open(f'{H}/edl-cut4.json', 'w'), indent=1)
open(f'{H}/edl-cut4.txt', 'w').write(''.join(f"{e['start']:7.2f}  {e['dur']:5.2f}  {e['item']:36s} {e['note']}\n" for e in new) + '\n' + ''.join(f'{m[1]:7.2f}  {m[3]:5.2f}  {m[0]}\n' for m in music))
print(len(new), 'picture clips,', len(narr), 'narrator lines,', len(music), 'music stems, total', round(TOTAL, 1), 's =', f'{int(TOTAL // 60)}:{int(TOTAL % 60):02d}')
