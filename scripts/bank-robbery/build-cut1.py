#!/usr/bin/env python3
"""The Bank Robbery, first assembly (2026-10-07): renders the pieces a timeline cannot make by itself and writes
edl-cut1.json for Premiere. Asked for by Jack: "do the narration, then put it all together in premiere".

Entries are [item, start, in, dur, vtrack, atrack], as the Money For Something kits. Picture on V1 with its own
sound on A1; the narrator on A2. Times are snapped to 1/24 s.

What is rendered into <project>/clips/cut1/ (ffmpeg; Premiere's bridge cannot write text):
  hold-*.mp4   a still held with a slow push, to sit under a narrator line where no silent clip exists
  ext-*.mp4    a silent clip with its last frame frozen, where the narrator runs longer than the 8 s clip
  card-*.mp4   scene 4's name cards (a moment of the clip, then a freeze with the name and job) and two title cards
  text-*.mp4   the film's title over the bank, and the two headlines in scene 5
Talking clips are used from the original files, trimmed to the speech (found from the sound level) plus room.
"""
import json, os, subprocess, wave, array, math
H = os.path.dirname(os.path.abspath(__file__))
P = '/mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/bank robbery'
V3, OLD, NAR, OUT = P + '/vids/v3', P + '/vids', P + '/narrator', P + '/clips/cut1'
IMG3, IMG2, IMG1 = P + '/images/scenes-v3', P + '/images/scenes-v2', P + '/images'
os.makedirs(OUT, exist_ok=True)
F = 24; snap = lambda t: round(t * F) / F
FONT = '/mnt/c/Windows/Fonts/impact.ttf'
ENC = ['-c:v', 'libx264', '-crf', '17', '-preset', 'medium', '-pix_fmt', 'yuv420p', '-r', '24', '-c:a', 'aac', '-ar', '48000', '-ac', '2', '-b:a', '192k', '-movflags', '+faststart']
def run(a): subprocess.run(['ffmpeg', '-v', 'error', '-y'] + a, check=True)
def narr_len(n): w = wave.open(f'{NAR}/{n}.wav'); return w.getnframes() / w.getframerate()
NAMES = {os.path.basename(f)[:3]: os.path.basename(f)[:-4] for f in os.listdir(NAR) if f.endswith('.wav')}

def speech(path):
    """(in, out) of the spoken part of a clip, from its sound level, with room either side."""
    raw = subprocess.run(['ffmpeg', '-v', 'error', '-i', path, '-vn', '-ac', '1', '-ar', '16000', '-f', 's16le', '-'], capture_output=True, check=True).stdout
    a = array.array('h', raw); w = 800; db = []
    for i in range(0, len(a) - w, w):
        s = sum(x * x for x in a[i:i + w]) / w; db.append(10 * math.log10(s + 1))
    floor = sorted(db)[int(len(db) * 0.3)]; thr = floor + 9
    on = [d > thr for d in db]; runs = [i for i in range(len(on) - 2) if on[i] and on[i + 1] and on[i + 2]]
    if not runs: return 0.25, 7.75
    a0, a1 = runs[0] * 0.05, (runs[-1] + 3) * 0.05
    if a1 - a0 < 0.8: return 0.25, 7.75
    return max(0.0, a0 - 0.8), min(7.95, a1 + 1.1)

E, N, t = [], [], 0.0        # picture entries, narrator entries, running time
LOG = []
def put(item, inn, dur, note=''):
    global t
    dur = snap(dur); E.append([item, snap(t), snap(inn), dur, 0, 0]); LOG.append((snap(t), dur, item, note)); t = snap(t + dur)
def say(lines, at):
    """place narrator lines one after another from `at`; returns the time the last one ends"""
    for n in lines:
        name = NAMES[n]; d = narr_len(name); N.append([name + '.wav', snap(at), 0, snap(d + 0.04), 0, 1]); at += d + 0.35
    return at - 0.35
def need(lines): return 0.4 + sum(narr_len(NAMES[n]) for n in lines) + 0.35 * (len(lines) - 1) + 0.6

def D(name, src=V3):
    """a talking clip, trimmed to its speech"""
    i, o = speech(f'{src}/{name}.mp4'); put(name + '.mp4', i, o - i, 'talk')
def S(name, dur, inn=0.0, src=V3):
    put(name + '.mp4', inn, dur, 'silent')
def C(name, lines, src=V3, extra=0.0):
    """a silent clip under narrator lines; frozen on its last frame if the lines run past 8 s"""
    d = need(lines) + extra; start = t
    if d <= 7.9: put(name + '.mp4', 0.0, d, 'under narrator')
    else:
        f = f'ext-{name}.mp4'
        if not os.path.exists(f'{OUT}/{f}'):
            run(['-i', f'{src}/{name}.mp4', '-vf', f'tpad=stop_mode=clone:stop_duration={d - 8 + 0.2:.2f}', '-af', f'afade=t=out:st=7:d=1,apad=pad_dur={d - 8 + 0.2:.2f}'] + ENC + [f'{OUT}/{f}'])
        put(f, 0.0, d, 'under narrator, last frame held')
    say(lines, start + 0.4)
def Hd(tag, still, lines=None, dur=None, text=None, text_at=1.0):
    """a still held with a slow push, under narrator lines or for a fixed time"""
    d = need(lines) if lines else dur; start = t; f = f'hold-{tag}.mp4'
    if not os.path.exists(f'{OUT}/{f}'):
        n = int(round((d + 0.3) * F))
        vf = f"scale=-1:1440,crop=2560:1440,zoompan=z='1+0.06*on/{n}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={n}:s=1280x720:fps=24"
        if text: vf += ',' + draw(text, 0.80, 42, text_at)
        run(['-loop', '1', '-framerate', '24', '-i', still, '-f', 'lavfi', '-i', 'anullsrc=r=48000:cl=stereo', '-vf', vf, '-t', f'{d + 0.3:.2f}'] + ENC + [f'{OUT}/{f}'])
    put(f, 0.0, d, 'still held')
    if lines: say(lines, start + 0.4)
def draw(text, y, size, at=0.0, box=True):
    tf = f'{OUT}/_t{abs(hash(text)) % 10**8}.txt'; open(tf, 'w').write(text)
    b = ':box=1:boxcolor=black@0.55:boxborderw=18' if box else ':shadowcolor=black@0.8:shadowx=4:shadowy=4'
    return f"drawtext=fontfile='{FONT}':textfile='{tf}':fontsize={size}:fontcolor=white:x=(w-text_w)/2:y=h*{y}{b}:enable='gte(t,{at})'"
def card(tag, clip, inn, name, job, src=V3, move=1.3, hold=1.3):
    f = f'card-{tag}.mp4'
    if not os.path.exists(f'{OUT}/{f}'):
        vf = f"tpad=stop_mode=clone:stop_duration={hold + 0.2},{draw(name, 0.60, 96, move, box=False)},{draw(job, 0.77, 44, move, box=False)}"
        run(['-ss', f'{inn}', '-t', f'{move}', '-i', f'{src}/{clip}.mp4', '-vf', vf, '-af', f'apad=pad_dur={hold + 0.2}'] + ENC + [f'{OUT}/{f}'])
    put(f, 0.0, move + hold, 'name card')
def black(tag, text, dur=2.6):
    f = f'card-{tag}.mp4'
    if not os.path.exists(f'{OUT}/{f}'):
        run(['-f', 'lavfi', '-i', f'color=c=black:s=1280x720:r=24:d={dur + 0.2}', '-f', 'lavfi', '-i', 'anullsrc=r=48000:cl=stereo', '-vf', draw(text, 0.44, 64, 0.3, box=False), '-t', f'{dur + 0.2}'] + ENC + [f'{OUT}/{f}'])
    put(f, 0.0, dur, 'title card')
def textclip(tag, clip, dur, text, y, size, at, src=V3):
    f = f'text-{tag}.mp4'
    if not os.path.exists(f'{OUT}/{f}'):
        run(['-i', f'{src}/{clip}.mp4', '-t', f'{dur + 0.2}', '-vf', draw(text, y, size, at, box=(size < 80))] + ENC + [f'{OUT}/{f}'])
    put(f, 0.0, dur, 'lettering added')

# ---------------- the cut ----------------
# 1 Breakfast
C('s01-breakfast', ['n01'], src=OLD)
Hd('s01-table', f'{IMG1}/s01-breakfast-a.jpg', ['n02'])
Hd('s01-denise', f'{IMG3}/s01e-denise.jpg', ['n03'])
S('s01b-remote', 5.5); D('s01c-blue'); D('s01d-red-1'); D('s01d-red-2'); D('s01e-denise')
# 2 The second job, and the title
S('s02-spoiler', 5.0, 1.0, src=OLD); S('s02b-shut-shops', 5.5, 0.5)
textclip('title', 's02c-bank-door', 7.0, 'THE BANK ROBBERY', 0.16, 120, 2.0)
# 3 Getting out
black('three-weeks', 'THREE WEEKS EARLIER')
Hd('s03-hearing', f'{IMG3}/s03a-hearing.jpg', ['n04'])
D('s03a-hearing-1'); D('s03a-hearing-2')
Hd('s03-hearing-b', f'{IMG3}/s03a-hearing.jpg', ['n05'])
C('s03-getting-out', ['n06'], src=OLD)
Hd('s03-steps', f'{IMG2}/s03-getting-out.jpg', ['n07', 'n08'])
# 4 The crew: name cards
card('01-ex', 's03-getting-out', 4.5, 'THE EX', 'FORMER CHANCELLOR', src=OLD)
card('02-fixer', 's04b-fixer', 3.0, 'THE FIXER', 'LOBBYIST')
card('03-donor', 's04c-donor', 1.0, 'THE DONOR', 'PARTY DONOR')
card('04-governor', 's04d-governor', 2.0, 'THE GOVERNOR', 'RUNS THE BANK')
card('05-proprietor', 's04e-proprietor', 2.0, 'THE PROPRIETOR', 'OWNS THE NEWSPAPERS')
card('06-presenter', 's04f-presenter', 2.5, 'THE PRESENTER', 'TELEVISION HOST')
card('07-platform', 's04g-platform', 2.0, 'THE PLATFORM', 'OWNS THE INTERNET')
card('08-accountant', 's04h-accountant', 2.0, 'THE ACCOUNTANT', 'ACCOUNTANT')
S('s04-recruiting', 3.0, 0.0, src=OLD)
card('09-drivers', 's04i-drivers-freeze', 2.0, 'MR BLUE AND MR RED', 'POLITICIANS', move=1.0, hold=1.6)
card('10-turquoise', 's04j-turquoise', 1.0, 'MR TURQUOISE', 'ALSO A POLITICIAN')
# 5 The plan
D('s05-plan-a'); D('s05-plan-b')
st = t; textclip('headline-blue', 's05b-blue-side', 6.0, "THEY'RE LETTING THEM IN", 0.80, 54, 3.2); say(['n09'], st + 0.3)
Hd('s05-headline-red', f'{IMG3}/s05c-red-side.jpg', dur=4.8, text='WE DESTROYED THEIR HOMES. NOW YOU TURN THE VICTIMS AWAY', text_at=1.0)
D('s05c-red-side-1'); D('s05c-red-side-2'); D('s05d-twist-1')
Hd('s05-accountant', f'{IMG3}/s05d-twist.jpg', ['n10'])
D('s05-plan-c'); D('s05d-twist-2'); S('s05-plan', 4.5, 2.5, src=OLD)
# 6 The colours
D('s06a-list-1'); D('s06a-list-2'); D('s06a-list-3'); D('s06a-list-4')
Hd('s06-list', f'{IMG3}/s06a-list.jpg', ['n11'])
D('s06-colours-talk')
C('s06-colours', ['n12'], src=OLD)
# 7 The night before
C('s07-night-before', ['n13'], src=OLD)
Hd('s07-party', f'{IMG2}/s07-night-before.jpg', ['n14'])
D('s07b-off-record')
Hd('s07-presenter', f'{IMG3}/s07b-off-record.jpg', ['n15'])
D('s07c-denise-hall')
Hd('s07-hall', f'{IMG3}/s07c-denise-hall.jpg', ['n16'])
# 8 The march
black('bank-holiday', 'BANK HOLIDAY MONDAY')
C('s08b-remote-window', ['n17'])
C('s08a-placards', ['n18'])
D('s08c-megaphones')
Hd('s08-megaphones', f'{IMG3}/s08c-megaphones.jpg', ['n19'])
D('s08d-presenter')
Hd('s08-presenter', f'{IMG3}/s08d-presenter.jpg', ['n20'])
C('s08-march', ['n21'], src=OLD)
# 9 The walk
D('s09a-officer')
C('s09-walk', ['n22'], src=OLD)
Hd('s09-walk', f'{IMG2}/s09-walk.jpg', ['n23'])
C('s09c-pallet', ['n24'])
D('s09d-door')
Hd('s09-door', f'{IMG3}/s09d-door.jpg', ['n25'])
C('s09e-turquoise', ['n26'])
# 10 The hoover
S('s10a-enter', 5.5)
D('s10-hoover-talk'); D('s10c-that-much-1'); D('s10c-that-much-2'); D('s10d-counting')
Hd('s10-counting', f'{IMG3}/s10d-counting.jpg', ['n27'])
# 11 The vault
D('s11-vault-talk')
C('s11-vault', ['n28'], src=OLD)
D('s11b-in')
Hd('s11-in', f'{IMG3}/s11b-in.jpg', ['n29'])
C('s11c-keys', ['n30'])
C('s11d-pricetags', ['n31'])
# 12 The standoff, the SOLD sign, the kebab shop
D('s12a-standoff-talk')
C('s12a-standoff', ['n32'], src=OLD)
D('s12d-lowering')
S('s12b-count', 7.8, 0.1, src=OLD)
S('s12e-sold', 7.0, 0.5)
S('s12f-kebab', 7.8, 0.1)

json.dump({'entries': E, 'narr': N, 'total': t}, open(f'{H}/edl-cut1.json', 'w'), indent=1)
open(f'{H}/edl-cut1.txt', 'w').write(''.join(f'{a:7.2f}  {d:5.2f}  {i:36s} {n}\n' for a, d, i, n in LOG))
used = sorted({e[0] for e in E}); print(len(E), 'picture clips,', len(N), 'narrator lines, total', round(t, 1), 's =', f'{int(t // 60)}:{int(t % 60):02d}')
print(sum(1 for u in used if u.startswith(('hold', 'ext', 'card', 'text'))), 'rendered pieces')
