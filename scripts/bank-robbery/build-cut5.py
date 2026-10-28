#!/usr/bin/env python3
"""The Bank Robbery, cut 5 (2026-10-08, late): Jack's notes on cut 4.

  "put the clip of the man eating whilst pushing the money back that was great. keep only the exciting ones in the
   montage ... also any of the videos that look cool, so it is not just videos of man with text on the screen.
   them moving the model stuff around, just remove all of those scenes. there needs to be a panning shot of the
   cafe being open at the beginning ... the still with the guns works keep that ... show the full English
   breakfast, things right-wingers will like ... then the narrator talking about being proud to be British ... a
   compilation of ww2 footage, pints, football and other English stuff ... quick but eye-grabbing. When Denise sees
   people robbing the bank, she should look at them, barely acknowledge them, then keep hoovering, ask someone to
   move, and she cleans whatever is behind them ... with bleach and a rag. We need to take the piss more out of the
   left and the right wing ... then the powerful people, as the politicians laugh at them for falling for it."

Cut 5 = cut 4 (edl-cut4.json) with the rules below, every start time worked out again. New pieces are in
<project>/clips/cut5/ (c5-*.mp4, ww2-*.mp4, m??e-*.wav). The pieces made with plain ffmpeg commands (name cards,
the cropped garage shots) are listed in assembly.md; this script makes the talking pieces, the pan, the two
pushed stills and the music, and writes edl-cut5.json and edl-cut5.txt.
"""
import glob, json, os, re, shutil, subprocess, wave, array, math
import numpy as np
H = os.path.dirname(os.path.abspath(__file__))
P = '/mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/bank robbery'
V6, IMG6, MUS, NAR, OUT = P + '/vids/v6', P + '/images/scenes-v6', P + '/music', P + '/narrator', P + '/clips/cut5'
SEARCH = [OUT, P + '/clips/cut4', P + '/clips/cut3', P + '/clips/cut2', P + '/clips/cut1', P + '/vids/v3', P + '/vids']
F, SR = 24, 48000
snap = lambda t: round(t * F) / F
ENC = ['-c:v', 'libx264', '-crf', '17', '-preset', 'medium', '-pix_fmt', 'yuv420p', '-r', '24', '-c:a', 'aac', '-ar', '48000', '-ac', '2', '-b:a', '192k', '-movflags', '+faststart']
SIL = ['-f', 'lavfi', '-i', 'anullsrc=r=48000:cl=stereo']
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
def bed_db(path, inn, dur, narrated):
    d = frames_db(path, inn, dur); r = 10 * math.log10(sum(10 ** (v / 10) for v in d) / len(d)) if d else -99.0
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
SPJ = f'{H}/speech-cut5.json'
SP = json.load(open(SPJ)) if os.path.exists(SPJ) else {}
def talk(clip, keep=None, tail=0.6, lead=0.3, minseg=0.3):
    """a talking clip from vids/v6 with its pauses cut out and its speech levelled (build-cut2.py's T())"""
    f = f'c5-t-{clip}.mp4'; path = f'{V6}/{clip}.mp4'
    if clip not in SP: SP[clip] = segments(path)
    segs = [s for s in SP[clip] if s[1] - s[0] >= minseg]
    if keep is not None: segs = [SP[clip][i] for i in keep]
    cuts = []
    for k, (a, b) in enumerate(segs):
        a2, b2 = max(0.0, a - (lead if not k else 0.3)), min(7.95, b + (0.3 if k < len(segs) - 1 else tail))
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
    return dict(item=f, inn=0.0, dur=snap(d), at=0, lvl=0.0, note='talk')
def copy(clip):
    f = f'c5-{clip}.mp4'
    if not os.path.exists(f'{OUT}/{f}'): shutil.copyfile(f'{V6}/{clip}.mp4', f'{OUT}/{f}')
    return f
def push(still, f, d=1.6):
    """a still with a fast push, for a one-second flash"""
    if not os.path.exists(f'{OUT}/{f}'):
        N = int(d * F)
        run(['-loop', '1', '-framerate', '24', '-i', f'{IMG6}/{still}.jpg'] + SIL + ['-vf', f"scale=2752:1536,zoompan=z='1+0.14*on/{N}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={N}:s=1280x720:fps=24,noise=alls=6:allf=t,format=yuv420p", '-t', f'{d}'] + ENC + [f'{OUT}/{f}'])
    return f
def U(f, inn, d, narrated=True, db=None, note=''):
    p = src(f); assert inn + d <= dur_of(p) + 0.03, (f, inn, d, dur_of(p))
    return dict(item=f, inn=snap(inn), dur=snap(d), at=2, lvl=db if db is not None else bed_db(p, inn, d, narrated), note=note)
def nlen(n): w = wave.open(f'{NAR}/{n}.wav'); return w.getnframes() / w.getframerate()

C4 = json.load(open(f'{H}/edl-cut4.json'))
LV = {round(l[1], 2): l[2] for l in C4['levels'] if l[0] == 2}
old = [dict(item=e[0], start=e[1], inn=e[2], dur=e[3], at=e[5], lvl=LV.get(round(e[1], 2), 0.0)) for e in C4['entries']]
idx = lambda name, nth=0: [i for i, e in enumerate(old) if e['item'] == name][nth]
def at_time(t): return max(i for i, e in enumerate(old) if e['start'] <= t + 1e-6)
keep = lambda e: dict(item=e['item'], inn=e['inn'], dur=e['dur'], at=e['at'], lvl=e['lvl'], note='')

# ---------------- scene 0: the cafe open, then proud to be British ----------------
if not os.path.exists(f'{OUT}/c5-s00a-cafe-pan.mp4'):       # the pan is done here, over a locked clip (hybrid method)
    run(['-i', f'{V6}/s00a-cafe-open.mp4', '-vf', "scale=1728:972:flags=lanczos,crop=1280:720:x='(in_w-1280)*(0.5-0.5*cos(PI*min(t/6.0\\,1)))':y='(in_h-720)*0.55',format=yuv420p", '-t', '6.4'] + ENC + [f'{OUT}/c5-s00a-cafe-pan.mp4'])
PRE = [U('c5-s00a-cafe-pan.mp4', 0.3, 5.5, False, note='the cafe, open: a pan')]
N00 = 'n00-s00-proud'; need = 0.15 + nlen(N00) + 0.4
WW2 = sorted(os.path.basename(p) for p in glob.glob(f'{OUT}/ww2-*.mp4'))
WW2 = [w for w in WW2 if w[:6] in ('ww2-01', 'ww2-02', 'ww2-03', 'ww2-05', 'ww2-06')]   # 04 is soft, 07 is a spare
flash = [(copy('s00b-full-english'), 0.2), (copy('s00d-fry'), 4.6), (copy('s00c-tea'), 1.0), (copy('s00e-pint'), 2.6), (copy('s00f-football'), 0.3)]
flash += [(w, 0.3) for w in WW2[:2]] + [(push('s00g-flags', 'c5-s00g-flags.mp4'), 0.0)] + [(w, 0.3) for w in WW2[2:]] + [(push('s00h-chippy', 'c5-s00h-chippy.mp4'), 0.0)]
each = need / len(flash); tt = 0.0
for k, (f, inn) in enumerate(flash):
    d = snap(tt + each) - snap(tt) if k < len(flash) - 1 else snap(need) - snap(tt); tt += each
    PRE.append(U(f, inn, d, db=(-60.0 if f.startswith('ww2') else None), note='proud: ' + f))

# ---------------- the rules ----------------
R = {}
# the montage: the name over the MOVING shot, five people, and two shots with no lettering at all
R[idx('c4b-card-01-ex.mp4')] = [U('c5-card-01-ex.mp4', 0.0, 2.1, False, db=-6.0, note='name over the moving shot')]
R[idx('c4b-card-03-donor.mp4')] = [U('c5-card-03-donor.mp4', 0.0, 2.1, False, db=-6.0, note='name over the moving shot'), U('s13-fountain.mp4', 2.0, 0.9, False, db=-8.0, note='no lettering: the fountain')]
R[idx('c4b-card-05-proprietor.mp4')] = [U('c5-card-05-proprietor.mp4', 0.0, 2.1, False, db=-6.0, note='name over the moving shot'), U('c5-card-10-turquoise.mp4', 0.0, 2.1, False, db=-6.0, note='name over the moving shot')]
R[idx('s04-recruiting.mp4')] = [U('s04-recruiting.mp4', 0.0, 1.2, False, db=-8.0, note='no lettering: the row')]
R[idx('c4b-card-09-drivers.mp4')] = [U('c5-card-09-drivers.mp4', 0.0, 2.1, False, db=-6.0, note='name over the moving shot')]
# the plan with no model town anywhere
R[idx('c2-t-s05-plan-a.mp4')] = [talk('s05h-table-a')]
R[idx('c2-t-s05-plan-b.mp4')] = [talk('s05h-table-b')]
R[idx('c2-t-s05-plan-c.mp4')] = []                           # "And her?" pointed at a figure on the model
R[idx('s05-plan.mp4')] = []                                  # the Ex pushing the model crowds together
for a, b in (('c2-t-s05d-twist-1.mp4', 'c5-t-s05d-twist-1.mp4'), ('s05d-twist-1.mp4', 'c5-s05d-twist-1.mp4'), ('hold-s05-accountant.mp4', 'c5-hold-s05-accountant.mp4'),
             ('c2-t-s05d-twist-2.mp4', 'c5-t-s05d-twist-2.mp4'), ('c2-t-s06-colours-talk.mp4', 'c5-t-s06-colours-talk.mp4'), ('s06-colours-talk.mp4', 'c5-s06-colours-talk.mp4'), ('s06-colours.mp4', 'c5-s06-colours.mp4')):
    e = old[idx(a)]; R[idx(a)] = [dict(keep(e), item=b, note='cropped and shaded: no model in frame')]
# the men upstairs, laughing (after "It's got BANK written on it")
BK = idx('c4-s08e-bank.mp4'); R[BK] = [keep(old[BK]), U(copy('s08g-laugh'), 3.4, 4.0, False, note='the two of them laughing at the street (the clip cuts itself closer at 3 s; this is the close half)')]
# the walk: the old clip back (the man eating as he pushes the money), then the line cut 2 dropped, now with pictures
WK = idx('c4-s09-walk.mp4'); n23 = [f[:-4] for f in os.listdir(NAR) if f.startswith('n23')][0]; need23 = 0.15 + nlen(n23) + 0.4
R[WK] = [U('s09-walk.mp4', 0.4, old[WK]['dur'], note='the old walk: eating as he pushes'), U('c4-s09-walk.mp4', 0.3, 4.6, note='the walk, riot look'),
         U('c5-s08f-argue.mp4', 0.3, snap(need23 - 4.6), db=-16.0, note='red scarf and blue scarf, filming each other (a push on the still; Flow refused the clip)')]
# Denise and the bleach
HV = idx('c2-t-s10-hoover-talk.mp4'); R[HV] = [keep(old[HV]), dict(talk('s10e-bleach', tail=2.6), note='talk: Shift. Then the bleach')]

# ---------------- ripple ----------------
new, t, first = [], 0.0, {}
for o in PRE: o['start'] = snap(t); new.append(o); t = snap(t + o['dur'])
OPEN_END = t
for i, e in enumerate(old):
    outs = R.get(i, [keep(e)]); first[i] = (t, sum(o['dur'] for o in outs))
    for o in outs: o['start'] = snap(t); new.append(o); t = snap(t + o['dur'])
TOTAL = t
def mapt(x):
    i = at_time(min(x, old[-1]['start'] + old[-1]['dur'] - 0.01)); e = old[i]; st, d = first[i]
    return st + (x - e['start']) / e['dur'] * d if d else st
narr = [[N00 + '.wav', snap(PRE[1]['start'] + 0.15), 0, snap(nlen(N00) + 0.04), 0, 1]]
for x in sorted(C4['narr'], key=lambda x: x[1]):
    i = at_time(x[1]); narr.append([x[0], snap(first[i][0] + (x[1] - old[i]['start'])), 0, x[3], 0, 1])
walk2 = [e for e in new if e['item'] == 'c4-s09-walk.mp4'][0]
narr.append([n23 + '.wav', snap(walk2['start'] + 0.15), 0, snap(nlen(n23) + 0.04), 0, 1]); narr.sort(key=lambda x: x[1])
levels = [[2, e['start'], e['lvl']] for e in new if e['at'] == 2]

# ---------------- music: cut 4's cues, moved with the picture; the first one now starts under the cafe ----------------
UNDER, VER = -33.0, 'e'
PARAM = {'m01': ('Covert Affair', 0.0, 0.3, 1.0, -20), 'm02': ('Cool Vibes', 0.0, 0.8, 0.5, -22), 'm03': ('Neon Laser Horizon', 12.8, 0.05, 0.06, -17), 'm04': ('Marty Gots a Plan', 0.0, 0.05, 1.0, -22),
         'm05': ('Covert Affair', 60.0, 1.0, 1.2, -22), 'm06': ('Volatile Reaction', 0.0, 0.3, 1.0, -24), 'm07': ('Hitman', 0.0, 0.8, 1.2, -24), 'm08': ('Covert Affair', 90.0, 1.0, 1.2, -22),
         'm09': ('Heartbreaking', 0.0, 0.4, 0.2, -21), 'm10': ('Neon Laser Horizon', 29.97, 0.03, 0.5, -18)}
KEB = [e for e in new if e['item'] == 's12f-kebab.mp4'][0]['start']
NB0 = first[idx('c3-s07-night-before.mp4')][0]; NB1 = first[idx('c4-s07g-bucket.mp4')][0] + first[idx('c4-s07g-bucket.mp4')][1]
def decode(name, ss, d):
    raw = subprocess.run(['ffmpeg', '-v', 'error', '-ss', f'{ss}', '-t', f'{d}', '-i', f'{MUS}/{name}.mp3', '-ac', '2', '-ar', f'{SR}', '-f', 'f32le', '-'], capture_output=True).stdout
    return np.frombuffer(raw, dtype='<f4').reshape(-1, 2).astype(np.float64)
def lufs(name, ss, d):
    e = subprocess.run(['ffmpeg', '-hide_banner', '-nostats', '-ss', f'{ss}', '-t', f'{d}', '-i', f'{MUS}/{name}.mp3', '-af', 'ebur128', '-f', 'null', '-'], capture_output=True, text=True).stderr
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
for i, m in enumerate(C4['music']):
    stem = m[0][:3]; name, ss, fi, fo, openl = PARAM[stem]; a = snap(mapt(m[1])); b = snap(mapt(m[1] + m[3]))
    if stem == 'm01': a = 0.0
    if stem == 'm03': a = snap(first[idx('c4b-card-01-ex.mp4')][0] - 1.2)
    if stem == 'm04': b = snap(NB0 + 0.4)
    if stem == 'm05': a = snap(NB1 - 0.4)
    if stem == 'm09': b = snap(KEB + 0.08)
    if stem == 'm10': a, b = KEB, TOTAL
    x = decode(name, ss, b - a); mm = len(x); L = lufs(name, ss, b - a); tt = a + np.arange(mm) / SR
    duck = np.interp(tt, np.arange(n) / RR, sp); g = 10 ** (((UNDER - L) * duck + (openl - L) * (1 - duck)) / 20)
    if fi: g *= np.clip(np.arange(mm) / (fi * SR), 0, 1)
    if fo: g *= np.clip((mm - np.arange(mm)) / (fo * SR), 0, 1)
    y = np.clip(x * g[:, None], -0.97, 0.97); fn = f"{stem}{VER}-{name.lower().replace(' ', '-')}.wav"
    w = wave.open(f'{OUT}/{fn}', 'wb'); w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes((y * 32767).astype('<i2').tobytes()); w.close()
    music.append([fn, a, 0.0, snap(mm / SR), 0, 3 + i % 2])

json.dump(SP, open(SPJ, 'w'), indent=0)
json.dump({'entries': [[e['item'], e['start'], e['inn'], e['dur'], 0, e['at']] for e in new], 'narr': narr, 'levels': levels, 'music': music, 'total': TOTAL, 'ww2': WW2}, open(f'{H}/edl-cut5.json', 'w'), indent=1)
open(f'{H}/edl-cut5.txt', 'w').write(''.join(f"{e['start']:7.2f}  {e['dur']:5.2f}  {e['item']:36s} {e['note']}\n" for e in new) + '\n' + ''.join(f'{m[1]:7.2f}  {m[3]:5.2f}  {m[0]}\n' for m in music))
print(len(new), 'picture clips,', len(narr), 'narrator lines,', len(music), 'music stems, total', round(TOTAL, 1), 's =', f'{int(TOTAL // 60)}:{int(TOTAL % 60):02d}')
