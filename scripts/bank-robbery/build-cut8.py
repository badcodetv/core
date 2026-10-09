#!/usr/bin/env python3
"""The Bank Robbery, cut 8 (2026-10-09): Jack's fourteen notes on cut 7 (docs/stories/bank-robbery/review-cut7.md).

Cut 8 = a clone of the Premiere sequence `bank robbery - cut 7`, in two steps:
  1. new pieces laid over it IN PLACE at cut 7's times (V2 picture, A1 sound, a silent WAV on A3), each rendered to
     the length of the slot it fills; pieces are <project>/clips/cut8/c8-*.mp4;
  2. four stretches REMOVED and everything after them pulled earlier (REMOVE below). The music stems that cross a
     removed stretch are re-rendered with that stretch cut out (m??f-*.wav) and laid again.
Writes edl-cut8.json and edl-cut8.txt. Times in both are CUT 7 times (before the removals); `shift(t)` gives cut 8's.
"""
import json, os, subprocess, array, math
H = os.path.dirname(os.path.abspath(__file__))
P = '/mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/bank robbery'
V7, OUT = P + '/vids/v8', P + '/clips/cut8'
SEARCH = [P + '/vids/v7', P + '/clips/cut7', P + '/clips/cut5', P + '/clips/cut4', P + '/clips/cut3', P + '/clips/cut2', P + '/clips/cut1', P + '/vids/v6', P + '/vids/v5', P + '/vids/v3', P + '/vids']
os.makedirs(OUT, exist_ok=True)
F = 24
snap = lambda t: round(t * F) / F
ENC = ['-c:v', 'libx264', '-crf', '17', '-preset', 'medium', '-pix_fmt', 'yuv420p', '-r', '24', '-c:a', 'aac', '-ar', '48000', '-ac', '2', '-b:a', '192k', '-movflags', '+faststart']
TALK_TARGET, BED_NARR, BED_OPEN = -19.0, -50.0, -36.0
def run(a): subprocess.run(['ffmpeg', '-v', 'error', '-y'] + a, check=True)
def dur_of(p): return float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', p], capture_output=True, text=True).stdout)
def find(name):
    if os.path.exists(f'{V7}/{name}.mp4'): return f'{V7}/{name}.mp4'
    for d in SEARCH:
        if os.path.exists(f'{d}/{name}'): return f'{d}/{name}'
    raise FileNotFoundError(name)
def frames_db(path, ss=0.0, t=None):
    a = ['ffmpeg', '-v', 'error', '-ss', f'{ss}'] + (['-t', f'{t}'] if t else []) + ['-i', path, '-vn', '-ac', '1', '-ar', '16000', '-af', 'highpass=f=120,lowpass=f=4000', '-f', 's16le', '-']
    x = array.array('h', subprocess.run(a, capture_output=True).stdout); w = 800
    return [10 * math.log10(sum(v * v for v in x[i:i + w]) / w / 32768 ** 2 + 1e-10) for i in range(0, len(x) - w, w)]
def segments(path):
    db = frames_db(path)
    if not db: return []
    s = sorted(db); thr = max(s[int(len(s) * .2)] + 7, s[int(len(s) * .95)] - 22); on = [v > thr for v in db]; segs = []; i = 0
    while i < len(on):
        if on[i]:
            j = i
            while j < len(on) and on[j]: j += 1
            if segs and i * .05 - segs[-1][1] < .45: segs[-1][1] = j * .05
            else: segs.append([i * .05, j * .05])
            i = j
        else: i += 1
    return [[round(a, 2), round(b, 2)] for a, b in segs if b - a >= .2]
SPJ = f'{H}/speech-cut8.json'      # speech spans per clip; edit a value here by hand to override the detector
SP = json.load(open(SPJ)) if os.path.exists(SPJ) else {}
def speech(clip):
    if clip not in SP: s = segments(find(clip)); SP[clip] = [s[0][0], s[-1][1]] if s else [0.0, 0.0]
    return SP[clip]

REMOVE = [(177.875, 190.375), (258.25, 6370 / 24), (7025 / 24, 7247 / 24)]   # cut 7 times: the whisper and Denise counting; the two-man pallet; "that much"
def shift(t): return t - sum(b - a for a, b in REMOVE if t >= b - 1e-6)
CROP = ',crop=1184:666,scale=1280:720'   # the strongroom stills came back with a rounded film-frame border; crop it off
VF = {}
PIECES, SIL, NOTES = [], [], []
def render(f, path, inn, d, mode, vf='', slow=1.0, extra=None, mute=False):
    """one piece: d seconds of `path` from `inn` (plus spare frames), sound levelled for `mode`.
    extra = [(file, ss, t, at, gain_db)]: other sound mixed in at `at` seconds (a spoken line made outside Flow)"""
    if os.path.exists(f'{OUT}/{f}'): return
    take = d / slow
    if mute: gain = -91.0
    elif mode == 'talk':
        a, b = speech(os.path.basename(path)[:-4]); lvl = sorted(frames_db(path, a, b - a)); top = lvl[int(len(lvl) * .9)] if lvl else -30
        gain = max(-10.0, min(14.0, TALK_TARGET - top))
    else:
        dd = frames_db(path, inn, take); r = 10 * math.log10(sum(10 ** (v / 10) for v in dd) / len(dd)) if dd else -99
        tgt = {'bed': BED_NARR, 'open': BED_OPEN, 'loud': -26.0}[mode]; gain = max(-34.0, min(6.0, tgt - r))
    v = f'[0:v]trim={inn}:{inn + take},setpts={slow}*(PTS-STARTPTS),scale=1280:720,setsar=1{vf},tpad=stop_mode=clone:stop_duration=0.25[v]'
    a = f'[0:a]atrim={inn}:{inn + take},asetpts=PTS-STARTPTS,atempo={1 / slow:.5f},afade=t=in:d=0.03,afade=t=out:st={max(0.0, d - 0.08):.3f}:d=0.08,volume={gain:.1f}dB,alimiter=limit=0.7:level=disabled,apad=pad_dur=0.25[a0]'
    ins, mix = ['-i', path], '[a0]'
    for k, (xf, ss, t, at, g) in enumerate(extra or []):
        lvl = sorted(frames_db(xf, ss, t)); top = lvl[int(len(lvl) * .9)] if lvl else -30; xg = max(-10.0, min(14.0, TALK_TARGET - top)) + g
        ins += ['-i', xf]; a += f';[{k + 1}:a]atrim={ss}:{ss + t},asetpts=PTS-STARTPTS,aresample=48000,aformat=channel_layouts=stereo,afade=t=in:d=0.02,afade=t=out:st={max(0.0, t - 0.05):.3f}:d=0.05,volume={xg:.1f}dB,adelay={int(at * 1000)}:all=1[x{k}]'; mix += f'[x{k}]'
    a += f';{mix}amix=inputs={1 + len(extra or [])}:normalize=0:duration=first[a]' if extra else ';[a0]anull[a]'
    run(ins + ['-filter_complex', v + ';' + a, '-map', '[v]', '-map', '[a]'] + ENC + [f'{OUT}/{f}'])
def put(start, end, clip, mode, inn=0.0, note='', vf='', slow=1.0, tag='', extra=None, mute=False):
    start, end = snap(start), snap(end); d = snap(end - start); path = find(clip)
    assert inn + d / slow <= dur_of(path) + 0.05, (clip, inn, d, dur_of(path))
    f = f"c8-{int(round(start * F)):05d}-{os.path.basename(path)[:-4].replace('c5-', '').replace('c4-', '')}{tag}.mp4"
    render(f, path, inn, d, mode, vf or VF.get(clip, ''), slow, extra, mute)
    PIECES.append([f, snap(shift(start)), 0.0, d, 1, 0]); NOTES.append((snap(shift(start)), d, f, note))
def talks(start, end, clips, lead=0.25, gap=0.3, note=''):
    """one or more single-speaker clips sharing a stretch: each gets its speech plus a lead and a tail; the last one holds to the end"""
    start, end = snap(start), snap(end); need = [c if isinstance(c, tuple) else (c, *speech(c)) for c in clips]; t = start
    want = sum(b - a + lead + gap for _, a, b in need); spare = (end - start) - want
    if spare < 0: print(f'  !! {[n[0] for n in need]} need {want:.2f} s, slot is {end - start:.2f} s: leads and tails squeezed'); lead = max(0.08, lead + spare / len(need) / 2); gap = max(0.1, gap + spare / len(need) / 2)
    for k, (c, a, b) in enumerate(need):
        e = end if k == len(need) - 1 else snap(t + (b - a) + lead + gap)
        inn = max(0.0, min(a - lead, dur_of(find(c)) - (e - t) - 0.02))
        put(t, e, c, 'talk', inn, note or f'talk: {c}'); t = e
def silence(start, end): SIL.append([snap(shift(start)), snap(end - start)])


NAR = P + '/narrator'
C5 = json.load(open(f'{H}/edl-cut5.json')); E = C5['entries']
def at(name, nth=0): return [e[1] for e in E if e[0] == name][nth]
def span(path):
    """first and last moment of speech in a spoken-line WAV"""
    s = segments(path); return (max(0.0, s[0][0] - 0.05), s[-1][1] + 0.08)
for c in ['s11a-drill2', 's11c-why2', 's11d-better2', 's11b-key2', 's11h-open', 's11e-in2', 's11f-count2', 's11g-full']: VF[c] = CROP

# ---------------- the hearing: her question spoken outside Flow over the old picture (she has her back to us), his answer in his own voice ----------------
A, B = at('c2-t-s03a-hearing-1.mp4'), at('s03a-hearing-2.mp4')
qa, qb = span(f'{NAR}/v8-panel-q.wav'); QD = snap(min(5.5, qb - qa + 0.55))
put(A, A + QD, 'c2-t-s03a-hearing-1.mp4', 'bed', 0.0, 'the panel\'s question, spoken in AI Studio speech, over the old picture', mute=True, extra=[(f'{NAR}/v8-panel-q.wav', qa, qb - qa, 0.2, 0.0)], tag='-q')
talks(A + QD, B, ['s03a-ex'], note='talk: the Ex answers, his own voice')
# ---------------- the garage: one speaker a clip ----------------
G0, G1, G2 = at('c2-t-s06a-list-1.mp4'), at('c5-t-s06-colours-talk.mp4'), at('c5-s06-colours-talk.mp4')
talks(G0, G1, ['s06-names', 's06-why', 's06-taken'], lead=0.06, gap=0.1)
talks(G1, G2, ['s06-thirteen', 's06-fourteen'], lead=0.12, gap=0.2)
# ---------------- Denise in the hall: hoovering, not counting ----------------
put(at('hold-s07-hall.mp4'), at('c2b-card-bank-holiday.mp4'), 's07c-hoovering', 'bed', 1.5, 'new: she hoovers'); silence(at('hold-s07-hall.mp4'), at('c2b-card-bank-holiday.mp4'))
# ---------------- "Nobody films it": from inside the crowd ----------------
put(251.25, at('c3-s09c-pallet.mp4'), 's08j-phones', 'bed', 0.3, slow=1.25, note= 'new: every phone points across the street, the pallet goes by behind them')
# ---------------- the door: already masked; the doorman's line kept from cut 7 ----------------
A, B = at('c2-t-s09d-door.mp4'), at('s09e-turquoise.mp4')
DOOR7 = P + '/clips/cut7/c7-06370-s09d-door2-b.mp4'; ds = segments(DOOR7)[0]
put(A, B, 's09d-door3', 'bed', 0.0, 'new: four men already in masks, standing in the doorway', slow=snap(B - A) / 7.9, extra=[(DOOR7, max(0.0, ds[0] - 0.05), ds[1] - ds[0] + 0.12, 0.25, 0.0)])
# ---------------- the hall ----------------
T, EN, HV, BL, TM = at('s09e-turquoise.mp4'), at('s10a-enter.mp4'), at('c2-t-s10-hoover-talk.mp4'), at('c5-t-s10e-bleach.mp4'), at('c2-t-s10c-that-much-1.mp4')
put(T, EN, 's09e-turquoise2', 'bed', 0.6, 'new: the pistol is in his hand')
put(EN, HV, 's10a-enter2', 'open', 1.2, 'new: from behind her')
put(HV, BL, 's10-hoover2', 'open', 1.5, 'new: the hoover goes round planted shoes')
talks(BL, TM, ['s10e-bleach2'], note='talk: "Shift." The cloth is already under her hand')
silence(T, TM)
LK, VA = at('s10d-counting.mp4'), at('c2-t-s11-vault-talk.mp4')
put(LK, VA, 's10d-looking2', 'bed', 1.5, 'new: she looks at the money, in the hall'); silence(LK, VA)
# ---------------- the strongroom (was the steel vault) ----------------
A, K = VA, at('s11c-keys.mp4'); N28 = at('s11-vault.mp4'); IN = at('c2-t-s11b-in.mp4'); AFTER = at('s11b-in.mp4')
put(A, A + 17 / 24, 's11a-drill2', 'loud', 2.0, 'new: he is drilling')
talks(A + 17 / 24, N28, ['s11c-why2', 's11d-better2'], lead=0.15, gap=0.2)
put(N28, N28 + 1.75, 's11a-drill2', 'bed', 4.0, 'still drilling, under "It\'s his bank"', tag='-b')
put(N28 + 1.75, N28 + 3.92, 's11b-key2', 'bed', 0.4, 'the key, under "He\'s had the key the whole time"')
put(N28 + 3.92, IN, 's11h-open', 'bed', 1.0, 'he looks at the drill, under "The drill\'s for you"')
ga, gb = span(f'{NAR}/v8-guard-q.wav'); GD = snap(gb - ga + 0.4)
put(IN, IN + GD, 's11e-in2', 'bed', 0.3, 'the guard\'s question, spoken in AI Studio speech (his back is to us)', mute=True, extra=[(f'{NAR}/v8-guard-q.wav', ga, gb - ga, 0.12, 0.0)], tag='-q')
talks(IN + GD, AFTER, ['s11f-count2'], lead=0.12, gap=0.2)
put(AFTER, AFTER + 4.5, 's11e-in2', 'bed', 3.2, 'the bricks going onto the shelves, under "And it was"', tag='-b')
put(AFTER + 4.5, K, 's11g-full', 'bed', 2.0, 'the strongroom full, the door closing')
silence(A, K)
# ---------------- the standoff: the fake fight, again ----------------
S0, S1 = at('c4-t-s12g-standoff.mp4'), at('c4-s12g-standoff-balance.mp4')
talks(S0, S1, [('s12j-mess', *SP['s12j-mess#1']), ('s12k-inherit', *SP['s12k-inherit#1']), ('s12j-mess', *SP['s12j-mess#2']), ('s12k-inherit', *SP['s12k-inherit#2'])], lead=0.08, gap=0.12)

# ---------------- narrator line 29, Jack's wording ----------------
# n29c = n29b (the new take) with the silence trimmed off both ends and played 4% faster, so it ends before line 30 starts
NARR = [['n29c-s11-crime-number.wav', snap(shift(322.708)), 0.0, round(dur_of(f'{NAR}/n29c-s11-crime-number.wav') - 0.02, 3), 1]]
# ---------------- music: the ten stems, with the removed stretches cut out of the three that cross one ----------------
C7 = json.load(open(P + '/.bridge/state-bank robbery - cut 7.json')); MUSIC = []
for ti in (3, 4):
    for c in C7['audioTracks'][ti]['items']:
        s, e = c['start'], c['end']; keep = [[s, e]]
        for a, b in REMOVE:
            nk = []
            for x, y in keep:
                if b <= x or a >= y: nk.append([x, y])
                else: nk += [[x, a]] * (a - x > 1.0) + [[b, y]] * (y - b > 1.0)
            keep = nk
        if keep == [[s, e]]: MUSIC.append([c['name'], snap(shift(s)), 0.0, snap(e - s), ti]); continue
        f = c['name'].replace('e-', 'f-', 1); o = f'{OUT}/{f}'; parts = ''.join(f'[0:a]atrim={x - s}:{y - s},asetpts=PTS-STARTPTS[p{i}];' for i, (x, y) in enumerate(keep))
        chain = '[p0]' + ('afade=t=in:d=0.4' if keep[0][0] > s else 'anull') + '[m0];'
        for i in range(1, len(keep)): chain += f'[m{i - 1}][p{i}]acrossfade=d=0.3:c1=tri:c2=tri[m{i}];'
        if not os.path.exists(o): run(['-i', c['mediaPath'], '-filter_complex', (parts + chain).rstrip(';'), '-map', f'[m{len(keep) - 1}]', '-ar', '48000', o])
        MUSIC.append([f, snap(shift(keep[0][0])), 0.0, snap(dur_of(o) - 0.05), ti])

json.dump(SP, open(SPJ, 'w'), indent=0)
PIECES.sort(key=lambda p: p[1]); NOTES.sort()
json.dump({'pieces': PIECES, 'silence': SIL, 'narr': NARR, 'music': MUSIC, 'remove_cut7_times': REMOVE, 'total': shift(C5['total'])}, open(f'{H}/edl-cut8.json', 'w'), indent=1)
open(f'{H}/edl-cut8.txt', 'w').write('Cut 8 = cut 7 with three stretches removed (cut 7 times: ' + ', '.join(f'{a:.2f} to {b:.2f}' for a, b in REMOVE) + ') and these pieces laid over it (V2 picture, A1 sound, silence on A3). CUT 8 start, length, file, what.\n\n' + ''.join(f'{s:8.3f}  {d:6.3f}  {f:44s} {n}\n' for s, d, f, n in NOTES))
print(len(PIECES), 'pieces,', len(SIL), 'silences,', round(sum(p[3] for p in PIECES), 1), 's of new picture; n29b', NARR[0][3], 's; total', shift(C5['total']))
