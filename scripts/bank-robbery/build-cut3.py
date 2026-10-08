#!/usr/bin/env python3
"""The Bank Robbery, cut 3 (2026-10-08): the re-made shots and music. Asked for by Jack: "use the new stuff, but
i liked the old kebab badcode ending, dont replace that. use royalty free music, for the mood of each scene for
now, we'll do suno stuff later. use anything that fits and would improve it."

Cut 3 is cut 2 with nothing moved: every cut point and the length (351.0 s) are the same. It reads edl-cut2.json
and writes edl-cut3.json:

  swaps   five re-made shots, each overwritten at the old shot's start with the same length (V1 + A3).
          Files are copied to <project>/clips/cut3/c3-*.mp4, because the v3 files of the same name are already
          in the project. The kebab shop is NOT swapped: Jack kept the old neon ending.
  music   ten stems on A4 and A5 (alternating, so neighbours can overlap for a crossfade), one per stretch of
          the film. Each stem is already trimmed, faded and ducked: it sits at UNDER LUFS while anyone speaks
          (narrator or cast, from edl-cut2.json) and rises to its OPEN level where nobody does. Volume in
          Premiere stays at 0 dB. All ten are Kevin MacLeod (incompetech.com), CC BY 4.0: credit owed in the film.
"""
import json, os, re, shutil, subprocess, wave, zlib
import numpy as np
H = os.path.dirname(os.path.abspath(__file__))
P = '/mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/bank robbery'
V4, MUS, OUT = P + '/vids/v4', P + '/music', P + '/clips/cut3'
os.makedirs(OUT, exist_ok=True)
F, SR = 24, 48000
snap = lambda t: round(t * F) / F
C2 = json.load(open(f'{H}/edl-cut2.json'))
TOTAL = C2['total']
def run(a): subprocess.run(['ffmpeg', '-v', 'error', '-y'] + a, check=True)
ENC = ['-c:v', 'libx264', '-crf', '17', '-preset', 'medium', '-pix_fmt', 'yuv420p', '-r', '24', '-c:a', 'aac', '-ar', '48000', '-ac', '2', '-b:a', '192k', '-movflags', '+faststart']

# ---------------- the re-made shots ----------------
# [new file, source in v4, the cut 2 item it replaces, in]. The length and the A3 level come from cut 2.
SWAPS = [
    ['c3-s07-night-before.mp4', 's07-night-before', 's07-night-before.mp4', 0.0],
    ['c3-s09c-pallet.mp4', 's09c-pallet', 's09c-pallet.mp4', 0.0],
    ['c3-s12b-count.mp4', 's12b-count', 's12b-count.mp4', 2.3],      # she counts for 2.2 s, then looks up at the window
    ['c3-s12e-sold.mp4', 's12e-sold', 's12e-sold.mp4', 1.0],         # the hand is on the board until 5 s; after 6 s the lamp jumps
]
for new, v4, old, inn in SWAPS:
    if not os.path.exists(f'{OUT}/{new}'): shutil.copyfile(f'{V4}/{v4}.mp4', f'{OUT}/{new}')
# the Mr Blue and Mr Red name card, made as build-cut2.py's card() makes it (0.6 s of the clip, then the freeze)
WF = '/mnt/c/Windows/Fonts/'; CREAM = '0xEFE6D0'
def draw(text, y, size, at, font, color, shadow):
    tf = f'{OUT}/_t{zlib.crc32(text.encode())}.txt'; open(tf, 'w').write(text)
    return f"drawtext=fontfile='{WF + font}':textfile='{tf}':fontsize={size}:fontcolor={color}:x=(w-text_w)/2:y=h*{y}:shadowcolor=black@0.7:shadowx={shadow}:shadowy={shadow}:enable='gte(t,{at})'"
CARD, move, hold, freeze_at = 'c3-card-09-drivers.mp4', 0.6, 1.3, 3.0
if not os.path.exists(f'{OUT}/{CARD}'):
    vf = (f"scale=1280:720,setsar=1,tpad=stop_mode=clone:stop_duration={hold + 0.2},{draw('MR BLUE AND MR RED', 0.54, 128, move, 'FRADMCN.TTF', 'white', 3)},"
          f"drawbox=x=(iw-96)/2:y=ih*0.765:w=96:h=5:color={CREAM}:t=fill:enable='gte(t,{move})',{draw('POLITICIANS', 0.80, 38, move, 'GILB____.TTF', CREAM, 2)}")
    run(['-ss', f'{freeze_at - move}', '-t', f'{move}', '-i', f'{V4}/s04i-drivers-freeze.mp4', '-vf', vf, '-af', f'apad=pad_dur={hold + 0.2}'] + ENC + [f'{OUT}/{CARD}'])
SWAPS.append([CARD, None, 'c2b-card-09-drivers.mp4', 0.0])
LEVEL = {round(l[1], 2): l[2] for l in C2['levels'] if l[0] == 2}
swaps = []
for new, _, old, inn in SWAPS:
    e = [x for x in C2['entries'] if x[0] == old]; assert len(e) == 1, old
    swaps.append([new, e[0][1], snap(inn), e[0][3], 0, 2, LEVEL[round(e[0][1], 2)]])

# ---------------- music ----------------
UNDER = -33.0     # LUFS while anyone speaks (the narrator plays at about -16). The first pass was -36 and the
                  # listening model only noticed the music where nobody spoke.
VER = 'b'         # stems are m01b-*.wav: Premiere locks a file that is on a timeline, so a re-make needs a new name
# [stem, file, timeline start, timeline end, source start, fade in, fade out, open level LUFS, what it is for]
CUES = [
    ['m01-covert-affair', 'Covert Affair', 0.0, 47.8, 0.0, 0.3, 1.0, -20, 'breakfast, the spoiler and the title: cool walking bass and a muted horn'],
    ['m02-cool-vibes', 'Cool Vibes', 46.9, 70.8, 0.0, 0.8, 0.5, -22, 'the hearing and getting out: plucked strings, polite'],
    ['m03-neon-laser-horizon', 'Neon Laser Horizon', 70.59, 90.79, 12.8, 0.05, 0.06, -17, 'the name cards: the 80s montage, cut dead on the meeting room'],
    ['m04-marty-gots-a-plan', 'Marty Gots a Plan', 90.79, 159.3, 0.0, 0.05, 1.0, -22, 'the plan and the colours: sneaky woodwinds'],
    # 158.9 to 166.9, the party, has no music: the party makes its own noise
    ['m05-covert-affair', 'Covert Affair', 166.5, 185.0, 60.0, 1.0, 1.2, -22, 'off the record, and Denise in the hall'],
    ['m06-volatile-reaction', 'Volatile Reaction', 184.2, 223.0, 0.0, 0.3, 1.0, -24, 'the march: drums and tension'],
    ['m07-hitman', 'Hitman', 222.3, 258.6, 0.0, 0.8, 1.2, -24, 'the walk: the beat lands as the pallet comes in (235 s)'],
    ['m08-covert-affair', 'Covert Affair', 257.8, 337.4, 90.0, 1.0, 1.2, -22, 'inside the bank, the vault and the standoff: back to the cool'],
    ['m09-heartbreaking', 'Heartbreaking', 336.8, 345.58, 0.0, 0.4, 0.2, -21, 'Denise counts; the SOLD board: one guitar'],
    ['m10-neon-laser-horizon', 'Neon Laser Horizon', 345.5, 351.0, 29.97, 0.03, 0.5, -18, 'the kebab shop: the last bars of the montage tune, to its final chord'],
]
def decode(name, ss, t):
    raw = subprocess.run(['ffmpeg', '-v', 'error', '-ss', f'{ss}', '-t', f'{t}', '-i', f'{MUS}/{name}.mp3', '-ac', '2', '-ar', f'{SR}', '-f', 'f32le', '-'], capture_output=True).stdout
    return np.frombuffer(raw, dtype='<f4').reshape(-1, 2).astype(np.float64)
def lufs(name, ss, t):
    e = subprocess.run(['ffmpeg', '-hide_banner', '-nostats', '-ss', f'{ss}', '-t', f'{t}', '-i', f'{MUS}/{name}.mp3', '-af', 'ebur128', '-f', 'null', '-'], capture_output=True, text=True).stderr
    return float(re.findall(r'I:\s+(-?[\d.]+) LUFS', e)[-1])
# who is speaking, at 100 Hz: the cast (A1) and the narrator (A2), each widened by 0.3 s, gaps under 1.2 s closed
R = 100; n = int(TOTAL * R) + 200; sp = np.zeros(n)
spans = sorted([[e[1], e[1] + e[3]] for e in C2['entries'] if e[5] == 0] + [[x[1], x[1] + x[3]] for x in C2['narr']])
merged = []
for a, b in spans:
    a, b = a - 0.3, b + 0.3
    if merged and a - merged[-1][1] < 1.2: merged[-1][1] = max(merged[-1][1], b)
    else: merged.append([a, b])
for a, b in merged: sp[max(0, int(a * R)):int(b * R)] = 1.0
k = int(0.8 * R); sp = np.convolve(sp, np.ones(k) / k, mode='same')          # 0.8 s ramps either side
music = []
for i, (stem, name, a, b, ss, fi, fo, openl, why) in enumerate(CUES):
    stem = stem[:3] + VER + stem[3:]
    a, b = snap(a), snap(b); x = decode(name, ss, b - a); m = len(x); L = lufs(name, ss, b - a)
    tt = a + np.arange(m) / SR
    duck = np.interp(tt, np.arange(n) / R, sp)                                # 1 while someone speaks
    db = (UNDER - L) * duck + (openl - L) * (1 - duck)
    g = 10 ** (db / 20)
    if fi: g *= np.clip(np.arange(m) / (fi * SR), 0, 1)
    if fo: g *= np.clip((m - np.arange(m)) / (fo * SR), 0, 1)
    y = np.clip(x * g[:, None], -0.97, 0.97)
    w = wave.open(f'{OUT}/{stem}.wav', 'wb'); w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
    w.writeframes((y * 32767).astype('<i2').tobytes()); w.close()
    music.append([f'{stem}.wav', a, 0.0, snap(m / SR), 3 + i % 2, name, round(L, 1), openl, why])
    print(f'{stem:26s} {a:7.2f} {b:7.2f}  src {ss:5.1f}  measured {L:6.1f} LUFS  A{4 + i % 2}  {why}')
json.dump({'from': 'edl-cut2.json', 'total': TOTAL, 'swaps': swaps, 'music': music, 'under_lufs': UNDER,
           'credit': 'Music: "Covert Affair", "Cool Vibes", "Neon Laser Horizon", "Marty Gots a Plan", "Volatile Reaction", "Hitman" and "Heartbreaking" by Kevin MacLeod (incompetech.com). Licensed under Creative Commons: By Attribution 4.0. http://creativecommons.org/licenses/by/4.0/'},
          open(f'{H}/edl-cut3.json', 'w'), indent=1)
for s in swaps: print('swap', s)
