#!/usr/bin/env python3
"""build_row.py <work>: GPOM scene A round 24, the row (beats 6-7) re-cut and re-synced (Kai r23 at3998/at4169/at4248/at4325).

Five shots, shot / reverse shot, every line on the face that says it:
  1 Sandra (6-0 v3)        "Derek. You've left the seat up"  -> 'Again.' runs on over Derek (Kai at3201: one sentence)
  2 Derek (7d-0 r19)       reacts under 'Again.', "I'm really sorry, love."
  3 Sandra (L07-0-b)       "Five years underground, and you still can't put a seat down."      (at4169: cut to Sandra)
  4 Derek (7d-1)           cut back to him ALREADY gesticulating, "But the world ended, Sandra!" (at4248: no jump)
  5 Sandra (7-2 v3)        "Yeah, the world ended. Doesn't mean you get to stop having manners." (at4325)
Every voice is a cast-voice take fitted WORD BY WORD to its clip (fitline.py / wordwarp.py: forced-aligned word starts
of the clip's own audio, checked against the lip closures; never early, +0.04 s; speech x0.87-1.18, pauses free).
0.2 s between lines (ROW18_GAP, Kai's minimum that still reads). Writes row-r24/: the voices, row-spec.json,
preview-row.mp4, all carded. Offsets are seconds from the start of beat 6."""
import json, os, shutil, subprocess, sys
import numpy as np, soundfile as sf

REPO = '/home/kai/projects/badcode/badcode'
CL = '/mnt/d/badcode-videos/gitpush-origin-master/clips/second-half'
V = f'{CL}/video'
OUT = f'{CL}/cut3/row-r24'
FPS, GAP, TAIL, CUT_PRE = 24, 0.2, 0.6, 0.15
TILE = 'aecho=0.8:0.5:35|60:0.22|0.12'  # cut3.py C.TILE: the tiled lavatory
ROOM = f'{CL}/audio/sfx/fs767306-room-tiled-public-bathroom.mp3'
PROV = f'{REPO}/scripts/provenance/prov.py'
HERE = os.path.dirname(os.path.abspath(__file__))
fr = lambda t: round(t * FPS) / FPS

work = sys.argv[1]
FITS = {  # line: (fit wav in the work dir, who, stem, text, shot clip (muted), raw clip it was fitted on)
    1: ('L1/cut3-lip-6-0-v3--6-0-b.wav', 'Sandra', 'vox-sandra', "Derek. You've left the seat up again."),
    2: ('L2/cut3-lip-7d-0-r19--7d-0c-fast-e.wav', 'Derek', 'vox-derek', "I'm really sorry, love."),
    3: ('L3/L07-0-b--7-0-f.wav', 'Sandra', 'vox-sandra', "Five years underground, and you still can't put a seat down."),
    4: ('L4/cut3-lip-7d-1--7d-1c-e.wav', 'Derek', 'vox-derek', 'But the world ended, Sandra!'),
    5: ('L5/cut3-lip-7-2-v3-t1--07-2-master.wav', 'Sandra', 'vox-sandra',
        "Yeah, the world ended. Doesn't mean you get to stop having manners."),
}
MUTED = {1: f'{V}/cut3-lip-6-0-v3-muted.mp4', 2: f'{V}/cut3-lip-7d-0-r19-muted.mp4', 3: f'{V}/cut3-lip-7-0-r24-muted.mp4',
         4: f'{V}/cut3-lip-7d-1-muted.mp4', 5: f'{V}/cut3-lip-7-2-v3-muted.mp4'}


def card(path, **kw):
    cmd = [sys.executable, PROV, 'card', path]
    for k, v in kw.items():
        if isinstance(v, dict):
            for a, b in v.items():
                cmd += [f'--{k}', f'{a}={b}']
        else:
            cmd += [f'--{k.replace("_", "-")}', str(v)]
    subprocess.run(cmd, check=True, capture_output=True)


def words(j):
    """(word, start, end) in CLIP time from a fit plan."""
    return [(r['word'], r['placed'], r['placed'] + (r['take'][1] - r['take'][0]) / r['tempo']) for r in j['rows']]


os.makedirs(OUT, exist_ok=True)
# ---- the new muted shot (line 3: Sandra, raw L07-0-b, an existing Omni take; no new credits)
if not os.path.exists(MUTED[3]):
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', f'{V}/cut3-lip-raw/L07-0-b.mp4', '-an', '-c:v', 'copy', MUTED[3]], check=True)
    card(MUTED[3], kind='video', engine='ffmpeg', tool='ffmpeg -c:v copy -an', parent=f'{V}/cut3-lip-raw/L07-0-b.mp4',
         why="round 24 (Kai r23 at4169): Sandra on screen for 'Five years underground, and you still can't put a seat down.'; "
             'muted twin of the existing Omni take L07-0-b, the clip whose mouth best fits a cast-voice take word by word')
# ---- the fitted voices
fit = {}
for n, (src, who, stem, text) in FITS.items():
    j = json.load(open(f'{work}/{src}.json'))
    dst = f"{OUT}/r24-line{n}-{who.lower()}-{os.path.basename(src)[:-4]}.wav"
    shutil.copyfile(f'{work}/{src}', dst)
    j['out'] = dst
    json.dump(j, open(dst + '.plan.json', 'w'), indent=1)
    s = j['summary']
    card(dst, kind='voice', engine='ffmpeg rubberband', tool='scripts/gpom/second-half-video/row-r24/fitline.py (wordwarp.py)',
         parent=j['take'], why=f"round 24 (Kai r23): {who}'s line '{text}' fitted word by word to the clip {os.path.basename(j['clip'])}",
         input={'clip': j['clip'], 'plan': dst + '.plan.json'},
         setting={'lag': j['lag'], 'late': 0.04, 'tempo_range': f"{s['tempo_lo']}-{s['tempo_hi']}",
                  'max_late': s['max_late'], 'pause_added': s['added'], 'clip_time_of_t0': j['origin']})
    fit[n] = dict(j=j, file=dst, who=who, stem=stem, text=text, w=words(j))

# ---- the edit
W = {n: f['w'] for n, f in fit.items()}
o = {n: fit[n]['j']['origin'] for n in fit}
shots, voices = [], []
# 1: Sandra 6-0 from its first frame; cut after 'up' (her mouth closes on it), 'Again.' runs on over Derek
up_end = W[1][-2][2]
c1 = fr(up_end + 0.04)
again_end = W[1][-1][2]
shots.append(dict(n=1, who='Sandra', file=MUTED[1], **{'in': 0.0}, out=c1, offset=0.0, beat='6'))
voices.append(dict(line=1, who='Sandra', stem='vox-sandra', file=fit[1]['file'], **{'in': 0.0},
                   dur=round(again_end + 0.15 - o[1], 4), offset=round(0.0 + o[1], 4), text=fit[1]['text'],
                   note="'Derek. You've left the seat up' on her face; 'Again.' straight on (0.1 s) over Derek"))
# 2: Derek 7d-0 r19: under 'Again.', 0.2 s, his line, cut 0.2 s after it (to Sandra's first word, minus her lead)
im = W[2][0][1]
t_im = again_end + GAP
i2 = im - (t_im - c1)
assert i2 >= 0.62, ('Derek must be shut-mouthed before his line (shut 0.62-2.42 s)', i2)
love_end_tl = c1 + (W[2][-1][2] - i2)
five = W[3][0][1]
c2 = fr(love_end_tl + GAP - five)
shots.append(dict(n=2, who='Derek', file=MUTED[2], **{'in': round(i2, 4)}, out=round(i2 + c2 - c1, 4), offset=c1, beat='7'))
voices.append(dict(line=2, who='Derek', stem='vox-derek', file=fit[2]['file'], **{'in': round(i2 + o[2] * 0, 4)},
                   dur=round(W[2][-1][2] + 0.15 - i2, 4), offset=c1, text=fit[2]['text']))
# 3: Sandra L07-0-b from its first frame
down_end_tl = c2 + W[3][-1][2]
but = W[4][0][1]
i4 = round((but - 0.17) * FPS) / FPS  # he is already gesticulating (arms out from frame 0); 'But' 0.17 s after the cut
c3 = fr(down_end_tl + GAP - (but - i4))
shots.append(dict(n=3, who='Sandra', file=MUTED[3], **{'in': 0.0}, out=round(c3 - c2, 4), offset=c2, beat='7'))
voices.append(dict(line=3, who='Sandra', stem='vox-sandra', file=fit[3]['file'], **{'in': 0.0},
                   dur=round(W[3][-1][2] + 0.15 - o[3], 4), offset=round(c2 + o[3], 4), text=fit[3]['text']))
# 4: Derek 7d-1, already gesticulating
sandra_end_tl = c3 + (W[4][-1][2] - i4)
yeah = W[5][0][1]
c4 = fr(sandra_end_tl + GAP - yeah)
shots.append(dict(n=4, who='Derek', file=MUTED[4], **{'in': i4}, out=round(i4 + c4 - c3, 4), offset=c3, beat='7'))
voices.append(dict(line=4, who='Derek', stem='vox-derek', file=fit[4]['file'], **{'in': i4},
                   dur=round(W[4][-1][2] + 0.15 - i4, 4), offset=c3, text=fit[4]['text']))
# 5: Sandra 7-2 v3 from its first frame, held TAIL after 'manners'
end = fr(c4 + W[5][-1][2] + TAIL)
shots.append(dict(n=5, who='Sandra', file=MUTED[5], **{'in': 0.0}, out=round(end - c4, 4), offset=c4, beat='7'))
voices.append(dict(line=5, who='Sandra', stem='vox-sandra', file=fit[5]['file'], **{'in': 0.0},
                   dur=round(W[5][-1][2] + 0.15 - o[5], 4), offset=round(c4 + o[5], 4), text=fit[5]['text']))
for s in shots:
    s['dur'] = round(s['out'] - s['in'], 4)
    s['clip_len'] = float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', s['file']],
                                         capture_output=True, text=True).stdout)
    assert s['out'] <= s['clip_len'] + 0.5 / FPS, s
# where each line's words land, timeline (offset from beat 6)
for v in voices:
    j = fit[v['line']]['j']
    shift = v['offset'] - v['in'] + j['origin']  # timeline of clip time 0 for this voice's clip
    v['words'] = [[w, round(a + v['offset'] - v['in'] - j['origin'] * 0 + 0, 3)] for w, a, _ in []]
    shot = next(s for s in shots if s['n'] == v['line'])
    clip0 = shot['offset'] - shot['in']  # timeline time of the clip's frame 0
    v['word_starts'] = [[w, round(clip0 + a, 3)] for w, a, _ in fit[v['line']]['w']]
    v['on_face'] = [w for w, a, _ in fit[v['line']]['w'] if shot['offset'] - 1e-6 <= clip0 + a < shot['offset'] + shot['dur']]
    del v['words']

spec = dict(
    about='GPOM scene A round 24: the row (beats 6-7) re-cut and re-synced. Offsets in seconds from the start of beat 6 '
          '(A-d21: 166.25 s). Shots on V1 in order; each voice is one file (cast voice, fitted word by word to its clip), '
          'laid from `in` for `dur` at `offset` on its stem, through the TILE echo at -16 LUFS like every row dub in cut3.py. '
          'Room tone: the tiled lavatory (fs767306, from 10 s, rms -42) under the whole row.',
    fps=FPS, total=end, beat7_start=c1, gap_between_lines=GAP, tail=TAIL, chain=[TILE], lufs=-16, room_tone=dict(file=ROOM, src_in=10, rms=-42),
    shots=shots, voices=voices, made_by='scripts/gpom/second-half-video/row-r24/build_row.py')
json.dump(spec, open(f'{OUT}/row-spec.json', 'w'), indent=1)
card(f'{OUT}/row-spec.json', kind='cut', engine='python', tool='scripts/gpom/second-half-video/row-r24/build_row.py',
     why='round 24 row spec (Kai r23 at3998/at4169/at4248/at4325) for cut3.py to place beats 6-7')

# ---- preview: picture + voices (TILE, -16 LUFS each) + room tone
tmp = f'{work}/preview'
os.makedirs(tmp, exist_ok=True)
parts = []
for s in shots:
    p = f"{tmp}/shot{s['n']}.mp4"
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-ss', f"{s['in']:.4f}", '-i', s['file'], '-t', f"{s['dur']:.4f}", '-an',
                    '-vf', f'scale=1280:720,setsar=1,fps={FPS}', '-c:v', 'libx264', '-crf', '16', '-pix_fmt', 'yuv420p', p], check=True)
    parts.append(p)
open(f'{tmp}/list.txt', 'w').write(''.join(f"file '{p}'\n" for p in parts))
pic = f'{tmp}/picture.mp4'
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-f', 'concat', '-safe', '0', '-i', f'{tmp}/list.txt', '-c', 'copy', pic], check=True)
SR = 48000
mix = np.zeros((int((end + 1) * SR), 2), np.float32)
for v in voices:
    p = f"{tmp}/v{v['line']}.wav"
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-ss', f"{max(0, v['in'] - fit[v['line']]['j']['origin']):.4f}", '-i', v['file'],
                    '-t', f"{v['dur']:.4f}", '-af', f'{TILE},loudnorm=I=-16:TP=-1.5:LRA=11', '-ar', str(SR), '-ac', '2', p], check=True)
    y, _ = sf.read(p, dtype='float32')
    a = int(round(v['offset'] * SR))
    if a < 0:
        y, a = y[-a:], 0
    mix[a:a + len(y)] += y[:len(mix) - a]
r = f'{tmp}/room.wav'
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-ss', '10', '-i', ROOM, '-t', f'{end:.3f}', '-ar', str(SR), '-ac', '2', r], check=True)
y, _ = sf.read(r, dtype='float32')
y *= 10 ** (-42 / 20) / (np.sqrt(np.mean(y ** 2)) + 1e-9)
mix[:len(y)] += y
mix = mix[:int(end * SR)]
sf.write(f'{tmp}/mix.wav', mix, SR, subtype='PCM_24')
prev = f'{OUT}/preview-row.mp4'
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', pic, '-i', f'{tmp}/mix.wav', '-c:v', 'copy', '-c:a', 'aac', '-b:a', '256k',
                '-shortest', prev], check=True)
card(prev, kind='cut', engine='ffmpeg', tool='scripts/gpom/second-half-video/row-r24/build_row.py',
     input={'spec': f'{OUT}/row-spec.json'}, why='round 24: stand-alone preview of the row (beats 6-7), picture + voices + room tone')
print(json.dumps(dict(total=end, cuts=[s['offset'] for s in shots],
                      lines=[(v['line'], v['offset'], v['word_starts'][0]) for v in voices]), indent=0))
