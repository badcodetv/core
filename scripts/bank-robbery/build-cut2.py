#!/usr/bin/env python3
"""The Bank Robbery, cut 2 (2026-10-08): the tightening pass. Asked for by Jack after watching cut 1: "way too
long, a lot of dead air in the clips, the volume clips are too loud when there is narration".

Entries are [item, start, in, dur, vtrack, atrack], as build-cut1.py. What is different from cut 1:

  Talking clips  rendered to <project>/clips/cut2/c2-t-*.mp4 with the pauses INSIDE the clip cut out (each kept
                 phrase has 0.3 s before and 0.3 s after, 0.6 s after the last; alternate phrases are punched in 10% so the jump
                 reads as a change of shot) and the speech levelled to one loudness. V1 + A1.
  Under narrator the original 8 s clips, moving, with in and out set; no frozen last frames, and a held still
                 only where no footage exists. V1 + A3, so the whole bed has one track.
  Narrator       A2, lines 0.35 s apart, starting 0.15 s after the cut, 0.4 s clear after. Six lines are left out (see CUT below).
  Name cards     re-rendered at 1.7 s (were 2.6 s) as c2-card-*.mp4.
  Levels         written to edl-cut2.json as `levels`: [atrack, start, dB] for every A1/A3 clip, and the narrator
                 at NARR_DB. Bed clips under the narrator sit about 30 dB under him.

Speech positions come from speech.json (made by the level scan in this session; re-made here if missing).
"""
import json, os, subprocess, wave, array, math, zlib
H = os.path.dirname(os.path.abspath(__file__))
P = '/mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/bank robbery'
V3, OLD, NAR, C1, OUT = P + '/vids/v3', P + '/vids', P + '/narrator', P + '/clips/cut1', P + '/clips/cut2'
IMG3 = P + '/images/scenes-v3'
os.makedirs(OUT, exist_ok=True)
F = 24; snap = lambda t: round(t * F) / F
# Lettering, second pass (2026-10-08, review-cut1.md finding 10: Impact is the meme font). Names and titles are
# Franklin Gothic Demi Cond, the small line is Gill Sans Bold in cream, the newspaper headline is Franklin Gothic
# Heavy on a paper strip and the platform's is Segoe UI Bold on a white post. Files are c2b-*, because Premiere
# locks a file that is on a timeline.
WF = '/mnt/c/Windows/Fonts/'
FONTS = {'name': WF + 'FRADMCN.TTF', 'small': WF + 'GILB____.TTF', 'paper': WF + 'FRAHV.TTF', 'post': WF + 'segoeuib.ttf'}
CREAM, INK = '0xEFE6D0', '0x111111'
ENC = ['-c:v', 'libx264', '-crf', '17', '-preset', 'medium', '-pix_fmt', 'yuv420p', '-r', '24', '-c:a', 'aac', '-ar', '48000', '-ac', '2', '-b:a', '192k', '-movflags', '+faststart']
NARR_DB, TALK_TARGET, BED_NARR, BED_OPEN = -3.0, -19.0, -50.0, -36.0
REDO = os.environ.get('REDO') == '1'          # re-render the talking pieces
# Four pieces came out one frame shorter than their place on the timeline (a black frame in the first render).
# Every piece is now rendered with 0.2 s of spare last frame; these four were re-made under a new name because
# Premiere locks a file that is on a timeline.
PADDED = {'s01e-denise', 's05c-red-side-1', 's09a-officer', 's10d-counting'}
CUT = ['n06', 'n07', 'n11', 'n13', 'n20', 'n23']          # narrator lines left out of cut 2
def run(a): subprocess.run(['ffmpeg', '-v', 'error', '-y'] + a, check=True)
def narr_len(n): w = wave.open(f'{NAR}/{NAMES[n]}.wav'); return w.getnframes() / w.getframerate()
NAMES = {f[:3]: f[:-4] for f in os.listdir(NAR) if f.endswith('.wav')}

def src(name):
    for d in (OUT, C1, V3, OLD):
        if os.path.exists(f'{d}/{name}'): return f'{d}/{name}'
    raise FileNotFoundError(name)
def frames_db(path, ss=0.0, t=None):
    a = ['ffmpeg', '-v', 'error', '-ss', f'{ss}'] + (['-t', f'{t}'] if t else []) + ['-i', path, '-vn', '-ac', '1', '-ar', '16000', '-af', 'highpass=f=120,lowpass=f=4000', '-f', 's16le', '-']
    x = array.array('h', subprocess.run(a, capture_output=True).stdout); w = 800
    return [10 * math.log10(sum(v * v for v in x[i:i + w]) / w / 32768 ** 2 + 1e-10) for i in range(0, len(x) - w, w)]
def rms(path, ss, t):
    d = frames_db(path, ss, t)
    return 10 * math.log10(sum(10 ** (v / 10) for v in d) / len(d)) if d else -99.0
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
SPJ = f'{H}/speech-cut2.json'
SP = json.load(open(SPJ)) if os.path.exists(SPJ) else {}

E, N, LV, LOG, t = [], [], [], [], 0.0
def put(item, inn, dur, atrack, note=''):
    global t
    dur = snap(dur); E.append([item, snap(t), snap(inn), dur, 0, atrack]); LOG.append((snap(t), dur, item, note)); t = snap(t + dur)
def say(lines, at):
    """narrator lines one after another from `at`; returns when the last one ends"""
    for n in lines:
        d = narr_len(n); N.append([NAMES[n] + '.wav', snap(at), 0, snap(d + 0.04), 0, 1]); at += d + 0.35
    return at - 0.35
def need(lines, lead=0.15, tail=0.4): return lead + sum(narr_len(n) for n in lines) + 0.35 * (len(lines) - 1) + tail

# The first "whose fault it is" was reported clipped on its last word (listening model, cut 2). The megaphone's
# tail now gets 0.45 s after the first phrase and the second phrase 0.15 s before it, so the length is the same.
EDGE = {'s08c-megaphones': {0: (None, 0.45), 1: (0.15, None)}}
RENAME = {'s08c-megaphones': 'c2b-t-s08c-megaphones.mp4'}
def T(name, keep=None, pre=0.0, minseg=0.3):
    """a talking clip with its pauses cut out. keep = indexes of the phrases to use (default all >= minseg);
    pre = seconds of the clip to leave on before the first phrase (cover for a narrator line that runs over)."""
    f = RENAME.get(name) or f"c2-t-{name}{'-p' if name in PADDED else ''}.mp4"; path = src(name + '.mp4')
    if name not in SP: SP[name] = segments(path)
    segs = [s for s in SP[name] if s[1] - s[0] >= minseg]
    if keep is not None: segs = [SP[name][i] for i in keep]
    cuts = []
    for k, (a, b) in enumerate(segs):
        eb, ea = EDGE.get(name, {}).get(k, (None, None))
        a2, b2 = max(0.0, a - (eb or (0.3 if k or not pre else pre))), min(7.95, b + (ea or (0.3 if k < len(segs) - 1 else 0.6)))
        if cuts and a2 <= cuts[-1][1] + 0.05: cuts[-1][1] = b2
        else: cuts.append([a2, b2])
    dur = sum(b - a for a, b in cuts)
    if REDO or not os.path.exists(f'{OUT}/{f}'):
        lvl = sorted(v for a, b in segs for v in frames_db(path, a, b - a)); top = lvl[int(len(lvl) * .9)] if lvl else -30
        gain = max(-10.0, min(14.0, TALK_TARGET - top)); fc = []; lab = ''
        for k, (a, b) in enumerate(cuts):
            punch = ',scale=1408:792,crop=1280:720' if k % 2 else ''
            fc.append(f'[0:v]trim={a}:{b},setpts=PTS-STARTPTS,scale=1280:720,setsar=1{punch}[v{k}]')
            fc.append(f'[0:a]atrim={a}:{b},asetpts=PTS-STARTPTS,afade=t=in:d=0.02,afade=t=out:st={b - a - 0.06:.3f}:d=0.06[a{k}]'); lab += f'[v{k}][a{k}]'
        fc.append(f'{lab}concat=n={len(cuts)}:v=1:a=1[vc][am]'); fc.append('[vc]tpad=stop_mode=clone:stop_duration=0.2[v]'); fc.append(f'[am]volume={gain:.1f}dB,alimiter=limit=0.7:level=disabled,apad=pad_dur=0.2[a]')
        run(['-i', path, '-filter_complex', ';'.join(fc), '-map', '[v]', '-map', '[a]'] + ENC + [f'{OUT}/{f}'])
    put(f, 0.0, dur, 0, f'talk, {len(cuts)} phrase(s) of {len(SP[name])}')
    return dur
def bed_db(item, inn, dur, narrated):
    r = rms(src(item), inn, dur)
    return round(max(-30.0, min(0.0, BED_NARR - r)) if narrated else max(-14.0, min(4.0, BED_OPEN - r)), 1)
def U(item, inn, dur, narrated=True, db=None, note=None):
    """a moving clip (or a held still) on V1 with its sound on A3, the bed track"""
    st = snap(t); put(item + '.mp4', inn, dur, 2, note or ('under narrator' if narrated else 'no words'))
    LV.append([2, st, db if db is not None else bed_db(item + '.mp4', inn, dur, narrated)])
def under(lines, covers, lead=0.15):
    """narrator lines over a run of clips; the last cover takes whatever time is left"""
    L = need(lines, lead); start = t; left = L
    for k, (item, inn, dur) in enumerate(covers):
        d = left if dur is None else dur
        assert d > 0.4, (lines, item, d)
        U(item, inn, d); left -= d
    assert abs(left) < 0.01, (lines, left)
    say(lines, start + lead)
def draw(text, y, size, at=0.0, font='name', color='white', x='(w-text_w)/2', shadow=3):
    """y is a fraction of the height, or pixels if 1 or more"""
    tf = f'{OUT}/_t{zlib.crc32(text.encode())}.txt'; open(tf, 'w').write(text)
    sh = f':shadowcolor=black@0.7:shadowx={shadow}:shadowy={shadow}' if shadow else ''
    return f"drawtext=fontfile='{FONTS[font]}':textfile='{tf}':fontsize={size}:fontcolor={color}:x={x}:y={y if isinstance(y, str) or y >= 1 else f'h*{y}'}{sh}:enable='gte(t,{at})'"
def box(x, y, w, h, color, at=0.0): return f"drawbox=x={x}:y={y}:w={w}:h={h}:color={color}:t=fill:enable='gte(t,{at})'"
def lettered(f, inputs, vf, dur):
    """a piece of cut 1 made again with the new lettering; same length, so it takes the same in and out"""
    if not os.path.exists(f'{OUT}/{f}'): run(inputs + ['-vf', vf, '-t', f'{dur:.2f}'] + ENC + [f'{OUT}/{f}'])
SILENT = ['-f', 'lavfi', '-i', 'anullsrc=r=48000:cl=stereo']
lettered('c2b-text-title.mp4', ['-i', f'{V3}/s02c-bank-door.mp4'], 'scale=1280:720,setsar=1,' + draw('THE BANK ROBBERY', 0.09, 150, 2.0), 7.2)
for tag, text in (('three-weeks', 'THREE WEEKS EARLIER'), ('bank-holiday', 'BANK HOLIDAY MONDAY')):
    lettered(f'c2b-card-{tag}.mp4', ['-f', 'lavfi', '-i', 'color=c=black:s=1280x720:r=24:d=2.8'] + SILENT, draw(text, '(h-text_h)/2', 54, 0.3, 'small', CREAM, shadow=0), 2.8)
lettered('c2b-text-headline-blue.mp4', ['-i', f'{V3}/s05b-blue-side.mp4'], 'scale=1280:720,setsar=1,' + ','.join([
    box(190, 498, 900, 150, '0xECE5D3', 3.2), box(210, 512, 860, 6, INK, 3.2), box(210, 630, 860, 2, INK, 3.2),
    draw("THEY'RE LETTING THEM IN", 542, 64, 3.2, 'paper', INK, shadow=0)]), 6.2)
_n = int(round(5.1 * F))
lettered('c2b-hold-s05-headline-red.mp4', ['-loop', '1', '-framerate', '24', '-i', f'{IMG3}/s05c-red-side.jpg'] + SILENT,
    f"scale=-1:1440,crop=2560:1440,zoompan=z='1+0.06*on/{_n}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={_n}:s=1280x720:fps=24," + ','.join([
    box(230, 490, 820, 160, 'white', 1.0), box(256, 516, 64, 64, '0xD8232A', 1.0),
    draw('We destroyed their homes.', 512, 40, 1.0, 'post', INK, 344, 0), draw('Now you turn the victims away.', 566, 40, 1.0, 'post', INK, 344, 0)]), 5.1)
def card(tag, clip, freeze_at, name, job, move=0.7, hold=1.0):
    """scene 4 name card: `move` seconds of the clip ending on `freeze_at`, then the freeze with the lettering"""
    f = f'c2b-card-{tag}.mp4'
    if not os.path.exists(f'{OUT}/{f}'):
        vf = f"scale=1280:720,setsar=1,tpad=stop_mode=clone:stop_duration={hold + 0.2},{draw(name, 0.54, 128, move)},{box('(iw-96)/2', 'ih*0.765', 96, 5, CREAM, move)},{draw(job, 0.80, 38, move, 'small', CREAM, shadow=2)}"
        run(['-ss', f'{freeze_at - move}', '-t', f'{move}', '-i', src(clip + '.mp4'), '-vf', vf, '-af', f'apad=pad_dur={hold + 0.2}'] + ENC + [f'{OUT}/{f}'])
    st = snap(t); put(f, 0.0, move + hold, 2, 'name card'); LV.append([2, st, -6.0])

# ---------------- the cut ----------------
# 1 Breakfast
under(['n01'], [('s01-breakfast', 0.0, 4.4), ('hold-s01-table', 0.0, None)])
under(['n02'], [('s01c-blue', 0.1, 3.55), ('s01-breakfast', 4.1, None)])
st = t; U('hold-s01-denise', 0.0, 3.2); U('s01b-remote', 0.6, 4.8, db=-8.0, note='narrator, then the remote and the telly'); say(['n03'], st + 0.15)
T('s01c-blue'); T('s01d-red-1'); T('s01d-red-2'); T('s01e-denise', minseg=0.25)
# 2 The second job, and the title
U('s02-spoiler', 1.5, 2.4, False); U('s02b-shut-shops', 1.0, 2.2, False); U('c2b-text-title', 1.6, 3.6, False)
# 3 Getting out
U('c2b-card-three-weeks', 0.2, 1.5, False)
under(['n04'], [('hold-s03-hearing', 0.0, None)])
T('s03a-hearing-1'); T('s03a-hearing-2')
st = t; U('s03a-hearing-2', 5.95, 2.05); say(['n05'], st + 0.05)
under(['n08'], [('s03-getting-out', 0.0, 7.9), ('hold-s03-steps', 0.0, None)])
# 4 The crew: name cards
card('01-ex', 's03-getting-out', 5.8, 'THE EX', 'FORMER CHANCELLOR')
card('02-fixer', 's04b-fixer', 4.3, 'THE FIXER', 'LOBBYIST')
card('03-donor', 's04c-donor', 2.3, 'THE DONOR', 'PARTY DONOR')
card('04-governor', 's04d-governor', 3.3, 'THE GOVERNOR', 'RUNS THE BANK')
card('05-proprietor', 's04e-proprietor', 3.3, 'THE PROPRIETOR', 'OWNS THE NEWSPAPERS')
card('06-presenter', 's04f-presenter', 3.8, 'THE PRESENTER', 'TELEVISION HOST')
card('07-platform', 's04g-platform', 3.3, 'THE PLATFORM', 'OWNS THE INTERNET')
card('08-accountant', 's04h-accountant', 3.3, 'THE ACCOUNTANT', 'ACCOUNTANT')
U('s04-recruiting', 0.0, 1.7, False, db=-8.0, note='the row, before the buzzer')
card('09-drivers', 's04i-drivers-freeze', 3.0, 'MR BLUE AND MR RED', 'POLITICIANS', move=0.6, hold=1.3)
card('10-turquoise', 's04j-turquoise', 2.3, 'MR TURQUOISE', 'ALSO A POLITICIAN')
# 5 The plan
T('s05-plan-a'); T('s05-plan-b')
st = t; U('c2b-text-headline-blue', 0.8, 5.0, db=-14.0); say(['n09'], st + 0.15)
U('c2b-hold-s05-headline-red', 0.5, 3.4, False)
T('s05c-red-side-1'); T('s05c-red-side-2'); T('s05d-twist-1')
under(['n10'], [('s05d-twist-1', 6.1, 1.8), ('hold-s05-accountant', 0.0, None)])
T('s05-plan-c'); T('s05d-twist-2'); U('s05-plan', 3.0, 2.2, False)
# 6 The colours (the Turquoise row is cut down to its first joke)
T('s06a-list-1'); T('s06a-list-2', keep=[0]); T('s06-colours-talk')
under(['n12'], [('s06-colours-talk', 5.9, 1.7), ('s06-colours', 0.0, None)])
# 7 The night before
under(['n14'], [('s07-night-before', 0.0, None)])
T('s07b-off-record')
under(['n15'], [('hold-s07-presenter', 0.0, None)])
T('s07c-denise-hall')
under(['n16'], [('hold-s07-hall', 0.0, None)])
# 8 The march: the narrator starts on the card and runs over the placards, the window and the megaphones' first second
st = t; U('c2b-card-bank-holiday', 0.2, 1.5); U('s08a-placards', 0.0, 7.0); U('s08b-remote-window', 0.0, 7.9, db=-12.0)
e = say(['n17', 'n18'], st + 0.2); over = e + 0.15 - t
T('s08c-megaphones', pre=max(0.3, min(1.3, over)))
under(['n19'], [('hold-s08-megaphones', 0.0, None)])
T('s08d-presenter', keep=[0])
under(['n21'], [('s08-march', 0.0, None)])
# 9 The walk
T('s09a-officer')
under(['n22'], [('s09-walk', 0.0, None)])
under(['n24'], [('s09c-pallet', 0.0, None)])
T('s09d-door', keep=[1])
under(['n25'], [('s09d-door', 3.05, 4.9), ('hold-s09-door', 0.0, None)])
st = t; U('s09e-turquoise', 0.0, need(['n26']), db=-6.0); say(['n26'], st + 0.15)
# 10 The hoover
U('s10a-enter', 1.0, 3.3, False)
T('s10-hoover-talk'); T('s10c-that-much-1'); T('s10c-that-much-2'); T('s10d-counting')
under(['n27'], [('s10d-counting', 3.3, None)])
# 11 The vault
T('s11-vault-talk')
st = t; U('s11-vault', 0.0, 7.95); say(['n28'], st + 0.1)
T('s11b-in')
under(['n29'], [('s11b-in', 6.85, 1.1), ('s10-hoover', 0.0, 6.3), ('s10a-enter', 4.4, None)])
under(['n30', 'n31'], [('s11c-keys', 0.0, 7.95), ('s05-plan', 5.5, 1.8), ('s11d-pricetags', 0.0, None)])
# 12 The standoff, the SOLD sign, the kebab shop
T('s12a-standoff-talk')
under(['n32'], [('s12a-standoff', 1.3, None)])
T('s12d-lowering')
U('s12b-count', 0.8, 4.5, False); U('s12e-sold', 1.0, 4.0, False); U('s12f-kebab', 0.5, 5.5, False)

for e in E:                                  # nothing may ask for more of a file than it has
    d = float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', src(e[0])], capture_output=True, text=True).stdout)
    assert e[2] + e[3] <= d + 0.02, (e, d)
for n in N: LV.append([1, n[1], NARR_DB])
json.dump(SP, open(SPJ, 'w'), indent=0)
json.dump({'entries': E, 'narr': N, 'levels': LV, 'total': t, 'cut_lines': CUT}, open(f'{H}/edl-cut2.json', 'w'), indent=1)
open(f'{H}/edl-cut2.txt', 'w').write(''.join(f'{a:7.2f}  {d:5.2f}  {i:36s} {n}\n' for a, d, i, n in LOG))
print(len(E), 'picture clips,', len(N), 'narrator lines, total', round(t, 1), 's =', f'{int(t // 60)}:{int(t % 60):02d}')
print('new pieces:', len([f for f in os.listdir(OUT) if f.endswith('.mp4')]))
