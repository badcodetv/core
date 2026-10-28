#!/usr/bin/env python3
"""The Bank Robbery, cut 9 (2026-10-12): Jack's notes on cut 8 ("a lot of dead air ... fast and funny, only pause for
comedic effect ... new narrator ... chill lofi music ... the newspaper bit trimmed, empty dinghies on it").

Cut 9 is a NEW timeline, not a clone. Every picture piece is a time range of ONE file: cut 8 exported from Premiere with
the narrator and music tracks muted (clips/cut9/cut8-stem-no-narrator-no-music.mp4), so picture, grade and production
sound are cut 8's. BLOCKS below lists what is kept, in order, in CUT 8 TIMES. A block with a narrator line is as long as
the line (its shots are shortened from their ends in proportion); a talk block is cut to its words (words-cut8.json,
faster-whisper word times of the cut 8 render) with a lead and a tail.
Narrator: narrator/v9/*.wav (new voice, br-narration-v9.json). Music: music/lofi, one pre-ducked stem per cue.
Writes clips/cut9/c9-*.mov, m9-*.wav, edl-cut9.json, edl-cut9.txt, and a preview mix clips/cut9/preview-cut9.mp4.
"""
import json, os, subprocess, sys
H = os.path.dirname(os.path.abspath(__file__))
P = '/mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/bank robbery'
OUT, STEM, NAR, MUS = P + '/clips/cut9', P + '/clips/cut9/cut8-stem-no-narrator-no-music.mp4', P + '/narrator/v9', P + '/music/lofi'
F = 24
fr = lambda t: int(round(t * F))
W = json.load(open(H + '/words-cut8.json'))
def run(a): subprocess.run(['ffmpeg', '-v', 'error', '-y'] + a, check=True)
def dur(p): return float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', p], capture_output=True, text=True).stdout)
def words(lo, hi, lead=0.2, tail=0.3):
    """the stretch of cut 8 between lo and hi cut down to the words spoken in it"""
    w = [x for x in W if lo <= (x[0] + x[1]) / 2 <= hi]; assert w, (lo, hi)
    return (max(lo, w[0][0] - lead), min(hi, w[-1][1] + tail))

# ---- the plan. ('n', line, [ranges], offset) narrator over shots; ('t', [ranges]) picture with its own sound; ('x', file, length) a made piece
PAPER = 2.5
BLOCKS = [
 ('scene', 'cafe'),
 ('t', [(2.6, 5.5)], 'the cafe, open'),
 ('n', 'n00-proud', [(5.5, 19.0)], 0.17, 'proud to be British: kept whole'),
 ('n', 'n01-greasy-spoon', [(19.0, 23.42), (23.42, 28.54)], 0.15, ''),
 ('n', 'n02-they-own', [(28.54, 35.96)], 0.15, ''),
 ('n', 'n03-lottery-ticket', [(35.96, 39.17), (39.17, 43.96)], 0.15, ''),
 ('t', [words(43.96, 46.21, 0.2, 0.15)], 'She should bloody well earn it'),
 ('t', [words(46.21, 53.17, 0.15, 0.2)], 'feminist rights / hate crime'),
 ('t', [words(53.17, 56.63, 0.25, 0.55)], 'Thanks for the advice'),
 ('scene', 'plan'),
 ('t', [(61.6, 63.5)], 'title'),
 ('t', [(65.0, 66.2)], 'three weeks earlier'),
 ('n', 'n04-long-stint', [(66.33, 70.5)], 0.15, ''),
 ('t', [words(70.5, 75.25, 0.15, 0.2)], 'the panel asks'),
 ('t', [words(75.25, 79.83, 0.15, 0.3)], 'food bank ... or consultancy (the pause is the joke)'),
 ('n', 'n05-inside-government', [(79.83, 81.88)], 0.12, ''),
 ('n', 'n08-bin-bag', [(81.88, 89.79)], 0.12, ''),
 ('t', [(91.3, 92.8)], 'card: the Ex'), ('t', [(93.4, 94.9)], 'card: the Donor'), ('t', [(96.4, 97.9)], 'card: the Proprietor'),
 ('t', [(98.5, 100.0)], 'card: Mr Turquoise'), ('t', [(101.75, 103.3)], 'card: Mr Blue and Mr Red'),
 ('t', [words(103.33, 109.04, 0.2, 0.2)], 'the biggest vault'),
 ('t', [words(109.04, 113.04, 0.15, 0.15)], 'I am the security'),
 ('t', [words(113.04, 114.88, 0.15, 0.3)], 'the problem is eyes'),
 ('n', 'n09-distraction', [('x', 'c9-paper-blue.mov', PAPER), ('x', 'c9-paper-red.mov', PAPER)], 0.12, 'two front pages, one photograph'),
 ('t', [words(124.08, 126.88, 0.1, 0.2)], 'which one is true'),
 ('t', [words(126.88, 133.79, 0.12, 0.3)], 'I need them to reply'),
 ('t', [words(133.79, 135.38, 0.1, 0.12)], 'how much do we take'),
 ('t', [words(135.38, 138.13, 0.15, 0.12)], 'Nothing ... we put it in (pause kept)'),
 ('n', 'n10-accountant', [(138.13, 142.58)], 0.4, ''),
 ('t', [words(142.58, 144.54, 0.12, 0.25)], 'You bastard'),
 ('t', [words(144.54, 149.58, 0.15, 0.2)], 'Mr Blue, Mr Red, Mr Turquoise'),
 ('t', [(149.62, 151.42)], 'why am I Mr Turquoise'), ('t', [(151.42, 152.5)], 'Blue was taken'),
 ('t', [(152.5, 153.96)], 'Thirteen years'), ('t', [words(153.96, 156.42, 0.1, 0.4)], 'Fourteen'),
 ('n', 'n12-fake-fight', [(156.42, 165.92)], 0.12, ''),
 ('scene', 'night'),
 ('n', 'n14-they-agree', [(165.92, 167.6), (167.71, 170.0), (170.21, 172.5), (172.79, 174.9)], 0.12, 'the drunk compilation'),
 ('t', [(175.29, 177.75)], 'the bucket'),
 ('n', 'n16-real-jobs', [(177.88, 182.92)], 0.15, 'Denise hoovering'),
 ('scene', 'march'),
 ('n', 'n17-bank-holiday', [(182.95, 184.0), (184.42, 187.6), (195.0, 197.4), (189.42, 192.2)], 0.12, 'card, the crowd from above, the placards, the man at the window'),
 ('t', [words(199.33, 203.33, 0.25, 0.2)], 'whose fault it is'),
 ('n', 'n19-bank-written-on-it', [(203.33, 209.67)], 0.12, ''),
 ('t', [(210.1, 211.8)], 'the two of them laughing at the window'),
 ('t', [words(213.5, 217.38, 0.15, 0.2)], 'both sides'),
 ('n', 'n21-corridor', [(217.38, 223.04)], 0.12, ''),
 ('t', [words(223.04, 228.46, 0.3, 0.3)], 'mind how you go, sir'),
 ('scene', 'bank'),
 ('n', 'n22-lasers', [(228.46, 235.5)], 0.12, 'the walk'),
 ('n', 'n23-nobody-films-it', [(235.5, 238.75), (238.75, 245.75)], 0.12, 'the walk, the phones'),
 ('n', 'n25-hobby', [(245.85, 254.6)], 1.15, 'the door; Morning, Governor first'),
 ('n', 'n26-turquoise-gun', [(254.67, 261.63)], 0.12, ''),
 ('t', [(261.63, 264.1)], 'Denise comes in'), ('t', [(265.1, 268.2)], 'the hoover round the shoes'), ('t', [(268.4, 271.3)], 'Shift.'),
 ('n', 'n27-only-person', [(273.04, 277.17)], 0.12, ''),
 ('t', [(277.17, 280.96)], 'why am I drilling / it looks better'),
 ('n', 'n28-his-bank', [(280.96, 282.71), (282.71, 284.88), (284.88, 288.92)], 0.1, ''),
 ('t', [words(288.92, 293.63, 0.15, 0.3)], 'you are putting it in / count it in the morning'),
 ('n', 'n29-crime-number', [(293.63, 298.13), (298.13, 303.42)], 0.4, ''),
 ('n', 'n30-just-early', [(303.42, 311.38), (311.38, 315.2)], 0.12, 'the keys, then the flat above the cafe'),
 ('n', 'n31-above-a-cafe', [(315.2, 321.08)], 0.25, 'for sale'),
 ('scene', 'ending'),
 ('t', [(336.9, 340.38)], 'Denise in the rain, SOLD'), ('t', [(340.38, 347.88)], 'she looks up; the camera goes to the sky'),
 ('t', [(347.88, 353.3)], 'the badcode kebab shop'),
]
NTAIL = 0.3   # picture held after a narrator line ends
# ---- music: cue per scene: file, where in the tune to start, level under speech and in the clear (LUFS-ish gain in dB on a -14 LUFS tune)
CUES = {'cafe': ('01-cafe-holiznacc0-busking-in-the-sunlight.mp3', 10.2), 'plan': ('02-plan-holiznacc0-busted-jazz.mp3', 10.0),
        'night': ('03-night-holiznacc0-happy-but-a-little-off.mp3', 8.0), 'march': ('04-march-holiznacc0-never-sleeping.mp3', 11.0),
        'bank': ('05-bank-holiznacc0-cellar-door.mp3', 11.0), 'ending': ('06-ending-holiznacc0-all-the-way-sad.mp3', 0.0)}

os.makedirs(OUT, exist_ok=True)
pieces, narr, scenes, notes, speech = [], [], [], [], []   # pieces: [file, start_frames, length_frames]
t = 0  # frames
def piece(src, n, label):
    global t
    if src[0] == 'x': f = src[1]
    else:
        a = src[0]; f = f"c9-{len(pieces):03d}-{fr(a):05d}.mov"; o = f'{OUT}/{f}'; d = n / F
        if not os.path.exists(o):
            run(['-ss', f'{a:.4f}', '-i', STEM, '-t', f'{d + 0.5:.4f}', '-vf', f'fps=24,trim=end_frame={n + 6},setpts=PTS-STARTPTS', '-af', f'afade=t=in:d=0.008,afade=t=out:st={d - 0.05:.3f}:d=0.05,volume=4.5dB,alimiter=limit=0.84:level=disabled,apad=pad_dur=0.3', '-t', f'{d + 0.25:.4f}',
                 '-c:v', 'libx264', '-crf', '14', '-preset', 'medium', '-pix_fmt', 'yuv420p', '-c:a', 'pcm_s16le', '-ar', '48000', o])
    pieces.append([f, t, n]); notes.append((t / F, n / F, f, label)); t += n
for b in BLOCKS:
    if b[0] == 'scene': scenes.append([b[1], t]); continue
    if b[0] == 't':
        for r in b[1]: speech.append((t / F, t / F + r[1] - r[0])) if 'card' not in b[2] and 'title' not in b[2] else None; piece(r, fr(r[1] - r[0]), b[2])
        continue
    _, line, shots, off, label = b
    nd = dur(f'{NAR}/{line}.wav'); need = off + nd + NTAIL
    lens = [(s[2] if s[0] == 'x' else s[1] - s[0]) for s in shots]; total = sum(lens)
    k = min(1.0, need / total) if not any(s[0] == 'x' for s in shots) else 1.0
    if line == 'n00-proud': k = 1.0
    assert total * k >= off + nd - 0.05, (line, total, need)
    narr.append([line + '.wav', round(t / F + off, 4), round(nd, 3)]); speech.append((t / F + off, t / F + off + nd))
    for s, L in zip(shots, lens): piece(s, fr(L * k), label or line)
TOTAL = t
# ---- music stems, ducked under speech by a volume envelope from the plan
scenes.append(['end', TOTAL]); music = []
for i, (name, s0) in enumerate(scenes[:-1]):
    s1 = scenes[i + 1][1]; f, inn = CUES[name]; a = max(0.0, s0 / F - (0.0 if i == 0 else 0.6)); b = s1 / F + (0.8 if i < len(scenes) - 2 else 0.0); d = b - a
    env = '+'.join(f'between(t,{max(0, x - a - 0.25):.2f},{y - a + 0.35:.2f})' for x, y in speech if y > a and x < b) or '0'
    o = f'm9-{i + 1:02d}-{name}.wav'; fo = 0.8 if i < len(scenes) - 2 else 2.5
    run(['-ss', f'{inn}', '-i', f'{MUS}/{f}', '-t', f'{d:.3f}', '-af', f"loudnorm=I=-14.5:TP=-2:LRA=11,aresample=48000,volume='if(gt({env},0),0.24,0.52)':eval=frame,asetnsamples=480,afade=t=in:d={0.05 if i == 0 else 0.6},afade=t=out:st={d - fo:.3f}:d={fo}", '-ac', '2', '-c:a', 'pcm_s16le', f'{OUT}/{o}'])
    music.append([o, round(a, 4), round(d, 3), 2 + i % 2])
json.dump({'pieces': [[f, s / F, n / F] for f, s, n in pieces], 'narr': narr, 'music': music, 'total': TOTAL / F, 'scenes': [[n, s / F] for n, s in scenes]}, open(H + '/edl-cut9.json', 'w'), indent=1)
open(H + '/edl-cut9.txt', 'w').write('Cut 9. start, length, file, what (picture pieces are ranges of the cut 8 stem; the number in the name is the cut 8 frame).\n\n' + ''.join(f'{s:8.3f}  {d:6.3f}  {f:26s} {n}\n' for s, d, f, n in notes) + '\nNarrator:\n' + ''.join(f'{s:8.3f}  {d:6.3f}  {f}\n' for f, s, d in narr) + '\nMusic:\n' + ''.join(f'{s:8.3f}  {d:6.3f}  {f}  A{tr + 1}\n' for f, s, d, tr in music))
print(len(pieces), 'pieces', len(narr), 'narrator lines', len(music), 'cues; total', round(TOTAL / F, 2), 's =', f'{int(TOTAL / F // 60)}:{TOTAL / F % 60:04.1f}')
for n, s in scenes: print(f'  {n:8s} {s / F:7.2f}')
if '--preview' in sys.argv:
    lst = OUT + '/preview.txt'; open(lst, 'w').write(''.join(f"file '{OUT}/{f}'\noutpoint {n / F:.5f}\n" for f, s, n in pieces))
    ins = ['-f', 'concat', '-safe', '0', '-i', lst]; fc = '[0:a]volume=1.0[a0];'; mix = '[a0]'
    for k, (f, s, d) in enumerate(narr): ins += ['-i', f'{NAR}/{f}']; fc += f'[{k + 1}:a]adelay={int(s * 1000)}:all=1[n{k}];'; mix += f'[n{k}]'
    for k, (f, s, d, tr) in enumerate(music): ins += ['-i', f'{OUT}/{f}']; fc += f'[{len(narr) + 1 + k}:a]adelay={int(s * 1000)}:all=1[m{k}];'; mix += f'[m{k}]'
    fc += f'{mix}amix=inputs={1 + len(narr) + len(music)}:normalize=0:duration=first[a]'
    run(ins + ['-filter_complex', fc, '-map', '0:v', '-map', '[a]', '-c:v', 'libx264', '-crf', '20', '-preset', 'veryfast', '-pix_fmt', 'yuv420p', '-r', '24', '-c:a', 'aac', '-b:a', '192k', OUT + '/preview-cut9.mp4'])
    print('preview', dur(OUT + '/preview-cut9.mp4'))
