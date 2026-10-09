#!/usr/bin/env python3
"""The Bank Robbery, cut 7 (2026-10-09): Jack's notes on cut 6.

  "There are still american accents and ai artifacts/ai slop ... Please change the platform to english. the whole
   vault scene is a bit of a mess and looks like ai slop, along with the crowd riot/protest scenes, please redo a
   lot of them ... it doesnt have a film vibe, even if it looks like a collection of comedy skits that tells the
   story, that would still be better."

Cut 7 = a clone of the Premiere sequence `bank robbery - cut 6` with new pieces laid over it IN PLACE: every piece
is rendered to the exact length of the slot it replaces, so the narrator (A2) and the music (A4, A5) do not move
and the film stays 382.29 s. New picture goes on V2 with its sound on A1; a silent WAV is laid on A3 under every
replaced stretch so the old clip sound there is gone. Pieces: <project>/clips/cut7/c7-*.mp4.
Writes edl-cut7.json ({pieces: [[file, start, in, dur, vtrack, atrack]], silence: [[start, dur]]}) and edl-cut7.txt.
Review and shot designs: docs/stories/bank-robbery/review-cut6.md, stills-v7.md.
"""
import json, os, subprocess, array, math
H = os.path.dirname(os.path.abspath(__file__))
P = '/mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/bank robbery'
V7, OUT = P + '/vids/v7', P + '/clips/cut7'
SEARCH = [P + '/clips/cut5', P + '/clips/cut4', P + '/clips/cut3', P + '/clips/cut2', P + '/clips/cut1', P + '/vids/v6', P + '/vids/v5', P + '/vids/v3', P + '/vids']
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
SPJ = f'{H}/speech-cut7.json'      # speech spans per clip; edit a value here by hand to override the detector
SP = json.load(open(SPJ)) if os.path.exists(SPJ) else {}
def speech(clip):
    if clip not in SP: s = segments(find(clip)); SP[clip] = [s[0][0], s[-1][1]] if s else [0.0, 0.0]
    return SP[clip]

PIECES, SIL, NOTES = [], [], []
def render(f, path, inn, d, mode, vf='', slow=1.0):
    """one piece: d seconds of `path` from `inn` (plus spare frames), sound levelled for `mode`"""
    if os.path.exists(f'{OUT}/{f}'): return
    take = d / slow
    if mode == 'talk':
        a, b = speech(os.path.basename(path)[:-4]); lvl = sorted(frames_db(path, a, b - a)); top = lvl[int(len(lvl) * .9)] if lvl else -30
        gain = max(-10.0, min(14.0, TALK_TARGET - top))
    else:
        dd = frames_db(path, inn, take); r = 10 * math.log10(sum(10 ** (v / 10) for v in dd) / len(dd)) if dd else -99
        tgt = {'bed': BED_NARR, 'open': BED_OPEN, 'loud': -26.0}[mode]; gain = max(-34.0, min(6.0, tgt - r))
    v = f'[0:v]trim={inn}:{inn + take},setpts={slow}*(PTS-STARTPTS),scale=1280:720,setsar=1{vf},tpad=stop_mode=clone:stop_duration=0.25[v]'
    a = f'[0:a]atrim={inn}:{inn + take},asetpts=PTS-STARTPTS,atempo={1 / slow:.5f},afade=t=in:d=0.03,afade=t=out:st={max(0.0, d - 0.08):.3f}:d=0.08,volume={gain:.1f}dB,alimiter=limit=0.7:level=disabled,apad=pad_dur=0.25[a]'
    run(['-i', path, '-filter_complex', v + ';' + a, '-map', '[v]', '-map', '[a]'] + ENC + [f'{OUT}/{f}'])
def put(start, end, clip, mode, inn=0.0, note='', vf='', slow=1.0, tag=''):
    start, end = snap(start), snap(end); d = snap(end - start); path = find(clip)
    assert inn + d / slow <= dur_of(path) + 0.05, (clip, inn, d, dur_of(path))
    f = f"c7-{int(round(start * F)):05d}-{os.path.basename(path)[:-4].replace('c5-', '').replace('c4-', '')}{tag}.mp4"
    render(f, path, inn, d, mode, vf, slow)
    PIECES.append([f, start, 0.0, d, 1, 0]); NOTES.append((start, d, f, note))
def talks(start, end, clips, lead=0.25, gap=0.3, note=''):
    """one or more single-speaker clips sharing a stretch: each gets its speech plus a lead and a tail; the last one holds to the end"""
    start, end = snap(start), snap(end); need = [(c, *speech(c)) for c in clips]; t = start
    want = sum(b - a + lead + gap for _, a, b in need); spare = (end - start) - want
    if spare < 0: print(f'  !! {clips} need {want:.2f} s, slot is {end - start:.2f} s: leads and tails squeezed'); lead = max(0.08, lead + spare / len(need) / 2); gap = max(0.1, gap + spare / len(need) / 2)
    for k, (c, a, b) in enumerate(need):
        e = end if k == len(need) - 1 else snap(t + (b - a) + lead + gap)
        inn = max(0.0, min(a - lead, dur_of(find(c)) - (e - t) - 0.02))
        put(t, e, c, 'talk', inn, note or f'talk: {c}'); t = e
def silence(start, end): SIL.append([snap(start), snap(end - start)])

C5 = json.load(open(f'{H}/edl-cut5.json')); E = C5['entries']
def at(name, nth=0): return [e[1] for e in E if e[0] == name][nth]
def end_of(name, nth=0): e = [e for e in E if e[0] == name][nth]; return e[1] + e[3]

# ---------------- breakfast: Mr Blue and Mr Red, each in his own saved voice ----------------
talks(at('c2-t-s01c-blue.mp4'), at('c2-t-s01d-red-1.mp4'), ['s01c-blue'])
talks(at('c2-t-s01d-red-1.mp4'), at('c2-t-s01e-denise-p.mp4'), ['s01d-red'])
silence(at('c2-t-s01c-blue.mp4'), at('c2-t-s01e-denise-p.mp4'))
# ---------------- the plan ----------------
talks(at('c5-t-s05h-table-a.mp4'), at('c5-t-s05h-table-b.mp4'), ['s05h-table-a'])
talks(at('c5-t-s05h-table-b.mp4'), at('c4-paper-blue.mp4'), ['s05h-gov', 's05h-eyes'])
silence(at('c5-t-s05h-table-a.mp4'), at('c4-paper-blue.mp4'))
talks(at('c4-t-s05e-papers-1.mp4'), at('c4-t-s05e-papers-2.mp4'), ['s05e-red'])
talks(at('c4-t-s05e-papers-2.mp4'), at('c5-t-s05d-twist-1.mp4'), ['s05e-platform'])
talks(at('c5-t-s05d-twist-1.mp4'), at('c5-s05d-twist-1.mp4'), ['s05d-donor', 's05d-ex'])
talks(at('c5-t-s05d-twist-2.mp4'), at('c2-t-s06a-list-1.mp4'), ['s05d-bastard2'])
silence(at('c4-t-s05e-papers-1.mp4'), at('c5-s05d-twist-1.mp4')); silence(at('c5-t-s05d-twist-2.mp4'), at('c2-t-s06a-list-1.mp4'))
# ---------------- the night before ----------------
talks(at('c2-t-s07b-off-record.mp4'), at('hold-s07-presenter.mp4'), ['s07b-off-record']); silence(at('c2-t-s07b-off-record.mp4'), at('hold-s07-presenter.mp4'))
# ---------------- the march: one wide for the geography, the window, then the two placards under "they agree on the first line" ----------------
A, B = at('c4-s08a-placards.mp4'), at('c4-t-s08c-megaphones.mp4')
put(A, A + 5.0, 's08h-corridor', 'bed', 0.6, 'new: the street from a first-floor window')
put(A + 5.0, 207.5, 'c4-s08b-remote-window.mp4', 'bed', 0.5, 'the man at the window (as cut 5), earlier')
put(207.5, B, 's08a-placards2', 'bed', 1.0, 'new: two placards in two hands, under "they agree on the first line"')
silence(A, B)
# the Presenter's line runs longer in his own voice than the old slot, so it starts early, over the tail of the two men laughing
PR = 's08d-presenter3'; PS = max(at('c5-s08g-laugh.mp4') + 2.5, at('s08-march.mp4') - (speech(PR)[1] - speech(PR)[0]) - 0.5)
talks(PS, at('s08-march.mp4'), [PR], lead=0.2, note='new: the Presenter at dusk, from the cobbles'); silence(PS, at('s08-march.mp4'))
# the two protesters filming each other: from above, with the pallet going between the phones (was a frozen still)
put(251.25, at('c3-s09c-pallet.mp4'), 's08f-above', 'bed', 0.4, 'new: two phones, one pallet, from a window above'); silence(251.25, at('c3-s09c-pallet.mp4'))
# the door, in the riot's light (was white daylight): one clip slowed a little to fill, the doorman's line near the top
A, B = at('c2-t-s09d-door.mp4'), at('s09e-turquoise.mp4')
put(A, B, 's09d-door2', 'talk', 0.0, 'new: the masks go on in the doorway, lit by the street', slow=snap(B - A) / 7.9); silence(A, B)
# ---------------- the vault: one room, one work lamp ----------------
A, K = at('c2-t-s11-vault-talk.mp4'), at('s11c-keys.mp4'); N28 = at('s11-vault.mp4'); IN = at('c2-t-s11b-in.mp4'); AFTER = at('s11b-in.mp4')
put(A, A + 17 / 24, 's11a-drill', 'loud', 4.5, 'new: he is drilling')
talks(A + 17 / 24, N28, ['s11c-why', 's11d-better'], lead=0.15, gap=0.2)
put(N28, N28 + 1.75, 's11a-drill', 'bed', 5.3, 'still drilling, under "It\'s his bank"', tag='-b')
put(N28 + 1.75, N28 + 3.92, 's11b-key', 'bed', 0.3, 'new: the key, under "He\'s had the key the whole time"')
put(N28 + 3.92, IN, 's11c-why', 'bed', min(speech('s11c-why')[1] + 0.3, 8.0 - (IN - N28 - 3.92) - 0.05), 'he stands there with the drill, under "The drill\'s for you"', tag='-hold')
talks(IN, AFTER, ['s11e-in', 's11f-count'], lead=0.15, gap=0.2)
put(AFTER, AFTER + 5.5, 's11g-top', 'bed', 0.5, 'new: the vault filling, from the ceiling corner, under "And it was"')
put(AFTER + 5.5, K, 's11e-in', 'bed', min(speech('s11e-in')[1] + 0.4, 8.0 - (K - AFTER - 5.5) - 0.05), 'the pallets still going in, the guard watching', tag='-b')
silence(A, K)
# ---------------- the standoff ----------------
talks(at('c4-t-s12g-standoff.mp4'), at('c4-s12g-standoff-balance.mp4'), ['s12j-who', 's12k-he', 's12j-lot'], lead=0.12, gap=0.2); silence(at('c4-t-s12g-standoff.mp4'), at('c4-s12g-standoff-balance.mp4'))

json.dump(SP, open(SPJ, 'w'), indent=0)
PIECES.sort(key=lambda p: p[1]); NOTES.sort()
json.dump({'pieces': PIECES, 'silence': SIL, 'total': C5['total']}, open(f'{H}/edl-cut7.json', 'w'), indent=1)
open(f'{H}/edl-cut7.txt', 'w').write('Cut 7 = cut 6 with these pieces laid over it in place (V2 picture, A1 sound, silence on A3). Start, length, file, what.\n\n' + ''.join(f'{s:8.3f}  {d:6.3f}  {f:44s} {n}\n' for s, d, f, n in NOTES))
print(len(PIECES), 'pieces,', len(SIL), 'silences,', round(sum(p[3] for p in PIECES), 1), 's of new picture')
