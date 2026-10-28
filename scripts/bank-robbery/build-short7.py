#!/usr/bin/env python3
"""The Bank Robbery SHORT, cut 7 (2026-10-19): cut 6b with Jack's notes on it: "at 9 seconds, the camera goes all over the
place still, instead of simply zooming out of it revealing the cafe. 20 secs she stops talking but the narrater keeps
talking. 26 seconds his phone morphs into a mug ... the two clips at 1 min 20 secs and 1 mins 24 secs of the people
protesting ... there are a lot of duplicate faces, please diversify both crowds". So: the reveal is one fixed-point
zoom out from the painting (cut 6's crop was centred on a painting that touches the top of the frame, so it was
clamped and slid sideways while it zoomed); a dub whose clip has a pause in the middle is split at the take's own
pause and each half laid on its run of mouth movement; Barry's second line re-shot with the phone already face down
and his hands already round the mug (c02p); both crowds re-shot from new stills, same camera and light, every
front-row face a different person.

(cut 5 notes follow) The Bank Robbery SHORT, cut 5 (2026-10-18, later): cut 4 with Jack's two notes: "some of the audio cuts off early,
please listen and fix it" and "put transitions that fit and make it look cinematic, so it is not only hard cuts".
Audio: each TTS line is sliced from where its sound really starts and ends (silencedetect), not from the transcriber's
word times, which put first words late and last words early; every dub is placed in Premiere at its whole file length;
the battle runs on under the painting into the cafe sound with no hole; the crowd's roar dies over 3 s; the music cues
cross over 1.5 s. Picture: dissolves and dips to black at the changes of place and time (TRANS), true crossfades from
the source clips' own handles where a piece has them; hard cuts kept inside conversations and on the jokes. A fade out
at the end. After the film, the composite test (real plate, AI person), easy to delete: COMPOSITE.

(cut 4 notes follow) The Bank Robbery SHORT, cut 4 (2026-10-18): cut 3 with Jack's notes on it (short-shots.md, "Cut 4"): the archive trimmed
to 6 s with battle sound under it (it was silent), Barry and Denise re-shot in the cafe of the wide so the painting stays
the painting, a real Freddo, the bank seen from the cafe window, the printing room re-made from real banknote-printing
footage, a real-looking side door, the deposit shown (two new vault shots), a new estate agent's window for the slot
machine, the crowd faded out instead of cut dead, voices up, colour tagged for delivery.

(cut 3 notes follow) The Bank Robbery SHORT, cut 3 (2026-10-15 night): cut 2 with Jack's notes (short.md, "Cut 3"): the action archive ending
on a frame repainted as the cafe painting, the new cafe wide, the bank at dawn and the side door in place of the bus shot,
real pound notes on the press, the protest without politicians (a chant and a reply, TTS crowds), the vault back.

(cut 2 notes follow) The Bank Robbery SHORT, cut 2 (2026-10-15 evening): cut 1 with the 15 October meeting's changes (short.md, "Cut 2").

Jack: "dont change the videos, just mute the videos and use [AI Studio] text to speech for each character as they are
talking ... whilst keeping our main narrator." So every talk piece is cut 1's picture with its sound muted, and the
character's TTS line (brs-voices.json, voices/short2) is laid on a dub track where the mouth moves, stretched to the
clip's speech within 0.8-1.25x. New: the archive opening, the reveal without the jolt, the deposit reveal on the press
still, the newspaper drops, the side-door line, the slot machine window. Gone: the deposit dialogue, the walk, the vault.

(cut 1 notes follow)

Pieces are rendered files (clips/short/s-NNN-*.mov, 1280x720, 24 fps, PCM audio), laid end to end. Sources:
  - new Omni clips in vids/short/ (brs-clips.json); a talk clip is cut to its words (faster-whisper on the clip's own
    audio) with a lead and a tail; a silent clip is cut to the narrator line laid over it;
  - four pieces of cut 10 (clips/cut10/c10-*.mov): the megaphones, the walk, the vault, the kebab neon;
  - two made pieces: the Dunkirk push-in and painting reveal, and the estate agent's window whose prices double (ffmpeg text).
Narrator: narrator/short/*.wav (brs-narration.json, take 2). Music: music/lofi, one pre-ducked stem per scene.
Writes clips/short/*, edl-short.json, edl-short.txt; --preview also writes clips/short/preview-short.mp4.
usage: python3 build-short.py [--preview]
"""
import json, os, subprocess, sys
H = os.path.dirname(os.path.abspath(__file__))
P = '/mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/bank robbery'
OUT, V, IMG, NAR, MUS, C10 = P + '/clips/short7t', P + '/vids/short', P + '/images/short', P + '/narrator/short', P + '/music/lofi', P + '/clips/cut10'
V3, I3, ARC, V7, V8 = P + '/vids/short3', P + '/images/short3', P + '/clips/short3/archive', P + '/vids/v7', P + '/vids/v8'
V4, I4 = P + '/vids/short4', P + '/images/short4'
V7 = P + '/vids/short7'
NAR2, VOX, C9, C5 = P + '/narrator/short2', P + '/voices/short2', P + '/clips/cut9', P + '/clips/cut5'
F = 24
fr = lambda t: int(round(t * F))
os.makedirs(OUT, exist_ok=True)
def run(a):
    r = subprocess.run(['ffmpeg', '-v', 'error', '-y'] + a, capture_output=True, text=True)
    if r.returncode: sys.exit('ffmpeg failed: ' + r.stderr[-1200:])
def dur(p): return float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', p], capture_output=True, text=True).stdout)
ENC = ['-c:v', 'libx264', '-crf', '14', '-preset', 'medium', '-pix_fmt', 'yuv420p', '-r', '24', '-c:a', 'pcm_s16le', '-ar', '48000', '-ac', '2']
TAG = ['-colorspace', 'bt709', '-color_primaries', 'bt709', '-color_trc', 'bt709', '-color_range', 'tv']   # cut 4: tagged, the delivery check's colour fail
FIT = 'scale=1280:720:force_original_aspect_ratio=increase,crop=1280:720,setsar=1,fps=24'

# ---- word times of every talk clip, cached (the whisper venv is the one the cut 8 transcript used)
WCACHE = H + '/words-short.json'
def src(clip): return clip if clip.startswith('/') else f'{V}/{clip}.mp4'
WORDS = json.load(open(WCACHE)) if os.path.exists(WCACHE) else {}
def words(clip):
    if clip not in WORDS:
        code = ("import sys,json,subprocess,numpy as np\nfrom faster_whisper import WhisperModel\n"
                "a=np.frombuffer(subprocess.run(['ffmpeg','-loglevel','error','-i',sys.argv[1],'-ac','1','-ar','16000','-f','f32le','-'],capture_output=True).stdout,np.float32)\n"
                "m=WhisperModel('small.en',device='cpu',compute_type='int8')\nsegs,_=m.transcribe(a,word_timestamps=True)\n"
                "print(json.dumps([[w.start,w.end,w.word.strip()] for s in segs for w in s.words]))")
        r = subprocess.run([os.path.expanduser('~/.cache/badcode-whisper/venv/bin/python'), '-c', code, src(clip)], capture_output=True, text=True)
        WORDS[clip] = json.loads(r.stdout.strip().splitlines()[-1]); json.dump(WORDS, open(WCACHE, 'w'), indent=1)
    return WORDS[clip]

pieces, narr, notes, speech, scenes, dub = [], [], [], [], [], []
t = 0  # frames
def add(f, n, label, talk=False):
    global t
    pieces.append([f, t, n]); notes.append((t / F, n / F, f, label))
    if talk: speech.append((t / F, (t + n) / F))
    t += n
META = {}   # cut 5: piece file -> (source, in, length, vf, af), for transitions with real handles
def cut(src, a, d, name, vf='', af=''):
    """a range of a source file as its own piece, d seconds long"""
    o = f'{OUT}/{name}.mov'; META[name + '.mov'] = (src, a, d, vf, af)
    if not (os.path.exists(o) and os.path.getsize(o) > 0):
        v = FIT + (',' + vf if vf else '')
        if src in FLICK or name in FLICK: v += ',' + flicker(t / F)
        sd = dur(src); short = a + d + 0.05 - sd   # the source runs out before the piece does: hold its last frame
        if short > 0 and 'tpad' not in v: v += f',tpad=stop_mode=clone:stop_duration={short + 0.2:.2f}'
        run(['-ss', f'{a:.3f}', '-i', src, '-t', f'{d:.3f}', '-vf', v, '-af', f'apad,afade=t=in:d=0.01,afade=t=out:st={max(0, d - 0.06):.3f}:d=0.06' + (',' + af if af else ''), '-t', f'{d:.3f}'] + ENC + [o])
    return name + '.mov', fr(d)
def talk(clip, label, lead=0.12, tail=0.25, gain='volume=3dB', upto=None, keep=False, gap=0.55):
    """a talk clip cut to its words. Whisper stretches a first word back to 0 s, so a word longer than 0.6 s is taken
    to start 0.8 s before it ends. upto: stop at the word that starts with this. Silences longer than gap inside the
    line are closed to 0.25 s (a jump cut on a locked camera) unless keep=True, for a pause that is the joke."""
    w = [list(x) for x in words(clip)]
    if upto: w = w[:next(i for i, x in enumerate(w) if x[2].lower().startswith(upto)) + 1]
    if w[0][1] - w[0][0] > 0.8: w[0][0] = w[0][1] - 0.8
    runs = [[w[0]]]
    for x in w[1:]:
        if not keep and x[0] - runs[-1][-1][1] > gap: runs.append([x])
        else: runs[-1].append(x)
    end = dur(f'{V}/{clip}.mp4')
    for k, r in enumerate(runs):
        a = max(0.0, r[0][0] - (lead if k == 0 else 0.12)); b = min(end, r[-1][1] + (tail if k == len(runs) - 1 else 0.13))
        f, n = cut(f'{V}/{clip}.mp4', a, b - a, f's-{len(pieces):03d}-{clip}', af=gain + ',alimiter=limit=0.84:level=disabled')
        add(f, n, label + ': ' + ' '.join(x[2] for x in r), talk=True)
def nwav(line):
    for d in (P + '/narrator/short6', NAR2): 
        if os.path.exists(f'{d}/{line}.wav'): return f'{d}/{line}.wav'
    return f'{NAR}/{line}.wav'
def over(line, shots, off=0.15, tail=0.3, label='', af=''):
    """narrator line over one or more silent shots: [(clip, start_in_clip, weight)], shared out by weight"""
    nd = dur(nwav(line)); need = off + nd + tail; tw = sum(s[2] for s in shots)
    narr.append([line + '.wav', round(t / F + off, 4), round(nd, 3)]); speech.append((t / F + off, t / F + off + nd))
    for clip, a, wgt in shots:
        d = need * wgt / tw
        if clip.startswith('c10-'): f, n = cut(f'{C10}/{clip}.mov', a, d, f's-{len(pieces):03d}-{clip}', af='volume=-6dB')
        elif clip.startswith('/'): f, n = cut(clip, a, d, f's-{len(pieces):03d}-' + os.path.basename(clip)[:-4], af='volume=-6dB' + (',' + af.format(st=max(0, d - 1.2)) if af else ''))
        elif clip.endswith('.mov'): f, n = clip, fr(d)
        else: f, n = cut(f'{V}/{clip}.mp4', a, d, f's-{len(pieces):03d}-{clip}', af='volume=-8dB')
        add(f, n, label or line)
def silent(clip, a, d, label, vf='', gain='volume=-4dB'):
    p = f'{C10}/{clip}.mov' if clip.startswith('c10-') else src(clip)
    f, n = cut(p, a, d, f's-{len(pieces):03d}-' + os.path.basename(p)[:-4], vf=vf, af=gain); add(f, n, label)

# ---- made piece 1: Dunkirk with grain (cut 2: the hand-held jolt is gone, Kai's 'camera jitter'), pushing in on the soldier's face in its last second
FACE = (0.468, 0.31)          # the shouting soldier, as a fraction of the frame (d01 and d02 share the composition)
PAINT = (0.127, 0.0, 0.507, 0.48)  # the painting's box in c01-cafe-wide (x0, y0, x1, y1), read off the still
def zoomcrop(z0, z1, T, cx, cy):
    """scale up per frame from zoom z0 to z1 over T seconds (eased), then a fixed 1280x720 crop centred on (cx, cy), clamped"""
    z = f'({z0}+({z1}-{z0})*(1-cos(PI*min(t/{T},1)))/2)'
    return (f"scale=w='trunc(1280*{z}/2)*2':h='trunc(720*{z}/2)*2':eval=frame,"
            f"crop=1280:720:x='max(0,min(iw-1280,{cx}*iw-640))':y='max(0,min(ih-720,{cy}*ih-360))',setsar=1")
CANVAS = (0.182, 0.02, 0.454, 0.365)   # the painting's canvas in c01b-cafe-wide (x0, y0, x1, y1), read off the still
def anchorzoom(z0, T, px, py):
    """cut 7: a zoom out from z0 to 1 over T seconds about one fixed point (px, py), so the framed thing grows smaller
    in place and nothing slides; geometric in scale (an even speed to the eye), eased in and out"""
    e = f'(1-cos(PI*min(t/{T},1)))/2'; z = f'pow({z0},1-{e})'
    return (f"scale=w='trunc(1280*{z}/2)*2':h='trunc(720*{z}/2)*2':eval=frame:flags=lanczos,"
            f"crop=1280:720:x='{px}*(iw-1280)':y='{py}*(ih-720)',setsar=1")
def reveal():
    """cut 7 (Jack: 'the camera goes all over the place still, instead of simply zooming out of it revealing the cafe').
    The last archive shot, the same frame repainted, then the cafe clip framed on its painting and one zoom out about a
    fixed point to the whole room, ending still. Cut 4-6 centred the crop on the canvas, which touches the top of the
    frame, so the crop was clamped and the picture slid while it zoomed: that was the 'all over the place'."""
    o = f'{OUT}/s-reveal7.mov'
    if not (os.path.exists(o) and os.path.getsize(o) > 0):
        we, pa, cf = f'{ARC}/wa-end-alamein-soldier-through-smoke.mp4', f'{I3}/a01-painting.jpg', f'{V3}/c01b-cafe-wide.mp4'
        cx, cy = (CANVAS[0] + CANVAS[2]) / 2, (CANVAS[1] + CANVAS[3]) / 2
        h0 = min(1.0, (CANVAS[3] - CANVAS[1]) * 1.06)                     # a 16:9 window just round the canvas
        x0, y0 = min(max(0.0, cx - h0 / 2), 1 - h0), min(max(0.0, cy - h0 / 2), 1 - h0)
        px, py = round(x0 / (1 - h0), 4), round(y0 / (1 - h0), 4)          # the point that stays put
        fc = (f"[0:v]{FIT},noise=alls=10:allf=t,tpad=stop_mode=clone:stop_duration=0.4,trim=0:1.9,setpts=PTS-STARTPTS,fps=24,settb=1/24[w];"
              f"[1:v]scale=1280:720,setsar=1,loop=loop=-1:size=1:start=0,fps=24,trim=0:1.8,setpts=PTS-STARTPTS,{zoomcrop(1.0, 1.03, 1.8, 0.5, 0.5)},fps=24,settb=1/24[pt];"
              f"[2:v]{FIT},trim=0:3.8,setpts=PTS-STARTPTS,{anchorzoom(round(1 / h0, 4), 3.0, px, py)},fps=24,settb=1/24[cafe];"
              f"[w][pt]xfade=transition=fade:duration=0.5:offset=1.4[a1];[a1][cafe]xfade=transition=fade:duration=0.4:offset=2.8[v];"
              f"[3:a]atrim=4.0:8.0,asetpts=PTS-STARTPTS,aresample=48000,aformat=channel_layouts=stereo,volume=3dB,afade=t=out:st=1.6:d=2.2[ba];"
              f"[2:a]atrim=0:5.5,asetpts=PTS-STARTPTS,volume=-3dB,afade=t=in:d=1.0,adelay=1100:all=1[ca];"
              f"[ba][ca]amix=inputs=2:normalize=0:duration=longest,apad,atrim=0:6.6[a]")
        run(['-i', we, '-i', pa, '-i', cf, '-i', BATTLE, '-filter_complex', fc, '-map', '[v]', '-map', '[a]', '-t', '6.6'] + ENC + [o])
    return 's-reveal7.mov', fr(6.6)

# ---- cut 2: the character voices (brs-voices.json), the take per line picked on a faster-whisper check
# (words-short2-tts.json): word-perfect first, then the take whose length is nearest the clip's own speech
PICK = {'v04-barry': 2, 'v05-denise': 2, 'v06-barry': 2, 'v07-denise': 2, 'v08-barry': 2, 'v09-denise': 1, 'v10-barry': 1,
        'v13-ex': 1, 'v14-red': 2, 'v17-red-chant': 1, 'v18-blue': 2, 'v24-barry': 2, 'v25-denise': 1}
TTSW = json.load(open(H + '/words-short2-tts.json'))
MEGA = 'highpass=f=450,lowpass=f=3400,acompressor=threshold=0.1:ratio=6:attack=2:release=60,volume=4dB,aecho=0.8:0.5:45:0.18'
def sound_span(p):
    """where the take's sound really starts and ends (-40 dB, 0.15 s): the transcriber's first word can start 0.6 s
    late and its last word end 0.25 s early, and slicing on those clipped 'Nine hundred' and 'Another boat' (cut 4)"""
    r = subprocess.run(['ffmpeg', '-v', 'info', '-i', p, '-af', 'silencedetect=n=-40dB:d=0.15', '-f', 'null', '-'], capture_output=True, text=True).stderr
    import re
    ss = [float(x) for x in re.findall(r'silence_start: ([\d.]+)', r)]; se = [float(x) for x in re.findall(r'silence_end: ([\d.]+)', r)]
    D = dur(p); a = se[0] if ss and ss[0] < 0.05 and se else 0.0
    trailing = ss and ss[-1] > a + 0.3 and (len(se) < len(ss) or se[-1] >= D - 0.03)   # the last silence runs to the end of the file
    b = ss[-1] if trailing else D
    return a, b
TAKEGAIN = {}
def take_gain(p, target=-16.0):
    """cut 7: the takes measured -11.7 to -19.7 LUFS, so the quiet ones sank under the music (0:21, 0:41, 1:58).
    Every take is brought to one loudness before it is cut up; the per-line DUBGAIN then sits on a level base."""
    if p not in TAKEGAIN:
        import re
        r = subprocess.run(['ffmpeg', '-v', 'info', '-i', p, '-af', 'ebur128', '-f', 'null', '-'], capture_output=True, text=True).stderr
        TAKEGAIN[p] = round(target - float(re.findall(r'I:\s+(-?[\d.]+) LUFS', r)[-1]), 2)
    return f'volume={TAKEGAIN[p]}dB'
def tts(line):
    p = f'{VOX}/take{PICK[line]}/{line}.wav'; w = TTSW[p]; a, b = sound_span(p)
    return p, a, max(w[-1][1], b)   # the sound's own start: a word time of 0.00 over half a second of silence put the voice in late
def dubline(line, at, span, fx=''):
    """write the line stretched toward span seconds (0.8-1.25x) and lay it at `at` seconds on the dub track"""
    p, t0, t1 = tts(line); d = t1 - t0; tempo = max(0.8, min(1.25, d / span)); nd = d / tempo
    o = f'dub-{line}.wav'
    run(['-ss', f'{max(0, t0 - 0.06):.3f}', '-t', f'{min(dur(p) - max(0, t0 - 0.06), d + 0.3):.3f}', '-i', p, '-af', f'atempo={tempo:.4f},{take_gain(p)}' + (',' + fx if fx else '') + ',areverse,silenceremove=start_periods=1:start_threshold=-45dB,areverse,aresample=48000', '-ac', '2', '-c:a', 'pcm_s16le', f'{OUT}/{o}'])
    dub.append([o, round(at, 4), round(dur(f'{OUT}/{o}'), 3), line, round(tempo, 3)]); speech.append((at, at + nd)); return nd   # cut 5: placed at the file's whole length
def tts_pauses(p, a, b, d=0.22):
    """silences inside a take between a and b (-40 dB, at least d s): [(start, end)]"""
    import re
    r = subprocess.run(['ffmpeg', '-v', 'info', '-i', p, '-af', f'silencedetect=n=-40dB:d={d}', '-f', 'null', '-'], capture_output=True, text=True).stderr
    ss = [float(x) for x in re.findall(r'silence_start: ([\d.]+)', r)]; se = [float(x) for x in re.findall(r'silence_end: ([\d.]+)', r)]
    return [(x, y) for x, y in zip(ss, se) if x > a + 0.2 and y < b - 0.2]
def dubchunk(line, k, p, c0, c1, at, span, fx=''):
    """one phrase of a take (c0-c1 s), stretched toward span (0.8-1.25x), laid at `at`"""
    d = c1 - c0; tempo = max(0.8, min(1.25, d / span)); nd = d / tempo; o = f'dub-{line}-{k}.wav'
    run(['-ss', f'{max(0, c0 - 0.04):.3f}', '-t', f'{d + 0.08:.3f}', '-i', p, '-af', f'atempo={tempo:.4f},{take_gain(p)}' + (',' + fx if fx else '') + ',afade=t=in:d=0.02,areverse,silenceremove=start_periods=1:start_threshold=-45dB,afade=t=in:d=0.03,areverse,aresample=48000', '-ac', '2', '-c:a', 'pcm_s16le', f'{OUT}/{o}'])
    dub.append([o, round(at, 4), round(dur(f'{OUT}/{o}'), 3), line, round(tempo, 3)]); speech.append((at, at + nd)); return nd
def dubtalk(clip, line, label, lead=0.15, tail=0.35, upto=None, fx='', gap=0.9):
    """cut 1's picture of a talk clip, muted, one continuous range round the mouth's words; the TTS line laid where
    the mouth moves. If the stretched line runs past the words the range is lengthened, holding the last frame if
    the clip runs out. Cut 7 (Jack: 'she stops talking but the [voice] keeps talking'): where the mouth stops for more
    than `gap` s mid-line, the take is cut at its own longest pauses into as many phrases, and each phrase is laid on
    its own run of mouth movement, so the voice stops when the mouth does."""
    w = [list(x) for x in words(clip)]
    if upto: w = w[:next(i for i, x in enumerate(w) if x[2].lower().startswith(upto)) + 1]
    if w[0][1] - w[0][0] > 0.8: w[0][0] = w[0][1] - 0.8
    runs = [[w[0]]]
    for x in w[1:]:
        if x[0] - runs[-1][-1][1] > gap: runs.append([x])
        else: runs[-1].append(x)
    s0, s1 = w[0][0], w[-1][1]; end = dur(src(clip))
    p, t0, t1 = tts(line)
    cuts = sorted(sorted(tts_pauses(p, t0, t1), key=lambda q: q[0] - q[1])[:len(runs) - 1]) if len(runs) > 1 else []
    if len(runs) > 1 and len(cuts) == len(runs) - 1:
        bounds = [t0] + [x for q in cuts for x in q] + [t1]; chunks = [(bounds[2 * i], bounds[2 * i + 1]) for i in range(len(runs))]
        last = runs[-1][0][0] + (chunks[-1][1] - chunks[-1][0]) / max(0.8, min(1.25, (chunks[-1][1] - chunks[-1][0]) / max(0.3, runs[-1][-1][1] - runs[-1][0][0])))
        a = max(0.0, s0 - lead); b = max(s1, last) + tail; hold = max(0.0, b - end)
        f, n = cut(src(clip), a, b - a, f's-{len(pieces):03d}-{os.path.basename(clip)[:-4] if clip.startswith("/") else clip}', vf=f'tpad=stop_mode=clone:stop_duration={hold + 0.1:.2f}' if hold > 0 else '', af='volume=0')
        for k, (r, (c0, c1)) in enumerate(zip(runs, chunks)):
            dubchunk(line, k, p, c0, c1, t / F + (r[0][0] - a), max(0.3, r[-1][1] - r[0][0]), fx)
        add(f, n, f'{label} (dub {line}, in {len(runs)} phrases)', talk=True); return
    nd = (t1 - t0) / max(0.8, min(1.25, (t1 - t0) / (s1 - s0)))
    a = max(0.0, s0 - lead); b = max(s1, s0 + nd) + tail; hold = max(0.0, b - end)
    f, n = cut(src(clip), a, b - a, f's-{len(pieces):03d}-{os.path.basename(clip)[:-4] if clip.startswith("/") else clip}', vf=f'tpad=stop_mode=clone:stop_duration={hold + 0.1:.2f}' if hold > 0 else '', af='volume=0')
    dubline(line, t / F + (s0 - a), s1 - s0, fx); add(f, n, f'{label} (dub {line})', talk=True)
LIPS = H + '/lips-short.json'
LIPRUNS = json.load(open(LIPS)) if os.path.exists(LIPS) else {}
def lipruns(clip, merge=0.6):
    """where the lips really move (lips.py, MediaPipe on the picture), runs closer than `merge` s joined"""
    if clip not in LIPRUNS:
        r = subprocess.run([os.path.expanduser('~/.cache/badcode-lips/venv/bin/python'), H + '/lips.py', clip], capture_output=True, text=True)
        LIPRUNS[clip] = json.loads(r.stdout.strip().splitlines()[-1]); json.dump(LIPRUNS, open(LIPS, 'w'), indent=1)
    out = []
    for a, b in LIPRUNS[clip]:
        if out and a - out[-1][1] < merge: out[-1][1] = b
        else: out.append([a, b])
    return out
COVERPOS = {}
def lipsync(clip, line, label, cover, upto=None, cvf=''):
    """cut 7b (Jack: "at 20 secs she speaks but her lips dont move ... they speak when their mouths are closed"). The
    picture follows the lips and the voice keeps its own pacing (no stretching beyond 1.15x; the 0.8x smear is gone).
    The take is cut into sentences at its pauses (>= 0.25 s). A sentence goes on the face when a lip run starts within
    0.6 s of where the voice would naturally say it and is long enough to carry it; the face stays up while the lips
    move. When the lips stop and the voice has more to say, the line carries over ONE cutaway where no mouth can be read
    (`cover`: the listener, the cafe wide, the press), the classic cover for a dubbed line, and comes back to the face
    only if a later lip run can carry a whole sentence. No cutaway shorter than 0.6 s."""
    runs = lipruns(clip)[:upto] if upto else lipruns(clip)
    p, t0, t1 = tts(line); sil = tts_pauses(p, t0, t1, d=0.25)
    edges = [t0] + [x for q in sil for x in q] + [t1]; ph = [(edges[2 * i], edges[2 * i + 1]) for i in range(len(edges) // 2)]
    fits = lambda r, d: d / 1.15 <= (r[1] - r[0]) + 0.35
    segs, places = [], []          # segs: [kind, T0, T1, src0]  (src0: clip time at T0, face only)
    T, ri = 0.0, 0
    def face_from(Tstart, src0): segs.append(['face', Tstart, Tstart, src0])
    def cover_from(Tstart): segs.append(['cover', Tstart, Tstart, None])
    for k, (a, b) in enumerate(ph):
        d = b - a; gap = 0.0 if k == 0 else min(0.45, a - ph[k - 1][1]); say = T + gap
        if k == 0:
            if runs: face_from(0.0, runs[0][0] - 0.2); say = 0.2       # every line opens on its speaker while the lips move
            else: cover_from(0.0)
        cur = segs[-1]
        if cur[0] == 'face':
            src_say = cur[3] + (say - cur[1])
            r = runs[ri] if ri < len(runs) else None
            if r and -0.3 <= r[0] - src_say <= 0.6 and (fits(r, d) or k == 0):
                at = max(say, cur[1] + (r[0] - cur[3])) if k else say
                tempo = max(1.0, min(1.15, d / ((r[1] - r[0]) + 0.35))); nd = d / tempo
                places.append((k, at, tempo)); T = at + nd; ri += 1
                lips_end_T = cur[1] + (r[1] + 0.1 - cur[3])
                if T > lips_end_T + 0.25: cur[2] = lips_end_T; cover_from(lips_end_T)   # the lips stop first: carry the rest away
                else: cur[2] = T
                continue
            cur[2] = max(cur[2], say if say - cur[2] < 0.6 else cur[2]); cover_from(cur[2])   # no run here: cut away
            cur = segs[-1]
        # on a cutaway: come back to the face if a later run can carry this whole sentence
        nxt = next((j for j in range(ri, len(runs)) if fits(runs[j], d)), None)
        if nxt is not None and k > 0 and say - 0.2 - cur[1] >= 0.6:   # the cutaway must stand on its own first
            cur[2] = say - 0.2; r = runs[nxt]; face_from(say - 0.2, r[0] - 0.2)
            tempo = max(1.0, min(1.15, d / ((r[1] - r[0]) + 0.35))); nd = d / tempo
            places.append((k, say, tempo)); T = say + nd; ri = nxt + 1; segs[-1][2] = T
            lips_end_T = segs[-1][1] + (r[1] + 0.1 - segs[-1][3])
            if T > lips_end_T + 0.25: segs[-1][2] = lips_end_T; cover_from(lips_end_T)
            continue
        places.append((k, say, 1.0)); T = say + d; cur[2] = T
    segs[-1][2] = T + 0.3
    out = []                                                       # no cutaway under 0.6 s: hold the face instead
    for sg in segs:
        if sg[2] - sg[1] < 0.05: continue
        if sg[0] == 'cover' and sg[2] - sg[1] < 0.6 and out and out[-1][0] == 'face': out[-1][2] = sg[2]; continue
        if out and out[-1][0] == sg[0] == 'cover': out[-1][2] = sg[2]; continue
        if out and out[-1][0] == sg[0] == 'face' and abs(sg[3] - (out[-1][3] + sg[1] - out[-1][1])) <= 0.5: out[-1][2] = sg[2]; continue   # one continuous shot, not a jump cut
        out.append(sg)
    if os.environ.get('LIPDEBUG'): print('LIPSYNC', line, [[k, round(a_, 2), round(b_, 2), None if c is None else round(c, 2)] for k, a_, b_, c in out], 'runs', runs)
    t_line = t / F
    for kind, T0, T1, src0 in out:
        if kind == 'face':
            f, n = cut(clip, max(0.0, src0), T1 - T0, f's-{len(pieces):03d}-{os.path.basename(clip)[:-4]}', af='volume=0'); add(f, n, f'{label} (lips)', talk=True)
        else:
            csrc, c0 = cover[:2]; cvf = cover[2] if len(cover) > 2 else cvf; ck = (csrc, c0); pos = COVERPOS.get(ck, c0)
            if pos + (T1 - T0) > dur(csrc) - 0.15: pos = c0 if c0 + (T1 - T0) <= dur(csrc) - 0.15 else max(0.0, dur(csrc) - (T1 - T0) - 0.15)   # a seek past the end gives a piece with no picture
            COVERPOS[ck] = pos + (T1 - T0) * (0.5 if 'setpts=2.0' in cvf else 1.0) + 0.1
            f, n = cut(csrc, pos, T1 - T0, f's-{len(pieces):03d}-{os.path.basename(clip)[:-4]}-x-{os.path.basename(csrc)[:-4]}', vf=cvf, af='volume=0'); add(f, n, f'{label}: the line carries over a cutaway', talk=True)
    for k, at, tempo in places:
        a, b = ph[k]; dubchunk(line, k, p, a, b, t_line + at, (b - a) / tempo)
def phrases(w):
    """words -> phrases at sentence or clause ends, or at gaps over 0.3 s"""
    out = [[w[0]]]
    for x in w[1:]:
        if out[-1][-1][2][-1:] in '.,?!' or x[0] - out[-1][-1][1] > 0.3: out.append([x])
        else: out[-1].append(x)
    return [(p[0][0], p[-1][1]) for p in out]
def snap(path, ph, n=-35):
    """move each phrase's edges onto the real sound edges (silencedetect): faster-whisper word times can be 0.2 s off
    on a short phrase, which put several lines at the 0.8x/1.25x stretch limits"""
    import re
    r = subprocess.run(['ffmpeg', '-v', 'info', '-i', path, '-af', f'silencedetect=n={n}dB:d=0.08', '-f', 'null', '-'], capture_output=True, text=True).stderr
    ss = [float(x) for x in re.findall(r'silence_start: ([\d.]+)', r)]; se = [float(x) for x in re.findall(r'silence_end: ([\d.]+)', r)]
    out = []
    for a, b in ph:
        a2 = min(se, key=lambda x: abs(x - a), default=a); b2 = min(ss, key=lambda x: abs(x - b), default=b)
        out.append((a2 if abs(a2 - a) < 0.35 else a, b2 if abs(b2 - b) < 0.35 and b2 > (a2 if abs(a2 - a) < 0.35 else a) + 0.15 else b))
    return out
ROOM = 'aecho=0.8:0.25:28|45:0.10|0.06'   # a breath of cafe room on a dry TTS line (research 2026-10-19: much of "sounds dubbed" is acoustics)
import re
def ownsync(clip, line, label, lag, mode='auto'):
    """cut 7b (Jack: "for some clips you have matched the lip syncing perfectly and some are completly messed around").
    Measured (short-shots.md, "Cut 7b"): the clips that synced are the ones whose OWN generated speech says the dub's
    words AND sits on the moving lips (Frames mode with the exact line in the prompt does both; Ingredients mode often
    improvised other words). For those, the clip's own speech is the timing map: each phrase of the take is stretched
    onto the matching phrase of the clip's speech, shifted by the measured audio-to-lips lag (`lag`, from cross-
    correlating speech with lip movement; kept late-ish, as late audio is far less visible than early)."""
    w = words(clip); p, t0, t1 = tts(line)
    (c0, c1), = snap(src(clip), [(w[0][0], w[-1][1])]); c0 = max(0.0, c0 - 0.08); c1 = min(dur(src(clip)), c1 + 0.1); W0 = c0
    o = f'dub-{line}-0.wav'; raw = f'{OUT}/dtw-{line}.wav'
    r = subprocess.run([os.path.expanduser('~/.cache/badcode-lips/venv/bin/python'), H + '/dtwsync.py', p, f'{t0:.3f}', f'{t1:.3f}', src(clip), f'{c0:.3f}', f'{c1:.3f}', raw, mode], check=True, capture_output=True, text=True)
    print('SYNC', line, r.stdout.strip().splitlines()[-1])
    run(['-i', raw, '-af', f'{take_gain(p)},{ROOM},aresample=48000', '-ac', '2', '-c:a', 'pcm_s16le', f'{OUT}/{o}'])
    a = max(0.0, c0 - 0.3); at = t / F + (W0 - a) + lag; dd = dur(f'{OUT}/{o}')   # the warped file's time 0 is W0
    dub.append([o, round(at, 4), round(dd, 3), line, 1.0]); speech.append((t / F + (c0 - a) + lag, t / F + (c1 - a) + lag))
    b = c1 + 0.35; end = dur(src(clip)); hold = max(0.0, b - end)
    f, n = cut(src(clip), a, b - a, f's-{len(pieces):03d}-{os.path.basename(clip)[:-4]}', vf=f'tpad=stop_mode=clone:stop_duration={hold + 0.1:.2f}' if hold > 0 else '', af='volume=0')
    add(f, n, f'{label} (own-speech DTW sync, lag {lag:+.2f} s)', talk=True)
CAFEPANS = [f'{P}/vids/short7/cd2-urn.mp4', f'{P}/vids/short7/cd1-painting.mp4', f'{P}/vids/short7/cd4-table.mp4', f'{P}/vids/short7/cd3-window.mp4']   # the window shows the bank: it comes last, after the narrator has pointed at it
PANPOS = [0]
def cafepans(line, label, shot_len=2.4):
    """cut 7b (Jack: "in shots where it is [hard] to lip sync, just show panning shots of the cafe as they are talking").
    The line at its own speed over the cafe's details (no mouth anywhere in them); each detail clip is camera-locked
    (Omni animates steam and rain) and the pan is done here, a slow even slide across a 1.12x frame."""
    p, t0, t1 = tts(line); d = t1 - t0; need = d + 0.6; t_line = t / F
    k = 0; left = need
    while left > 0.05:
        L = shot_len if left > shot_len * 1.6 else left   # no scrap of a shot at the end
        srcc = CAFEPANS[PANPOS[0] % len(CAFEPANS)]; dirn = 1 if PANPOS[0] % 2 == 0 else -1; PANPOS[0] += 1
        x = f"(iw-1280)*({0.5 - 0.5 * dirn}+{dirn}*t/{L:.3f})"
        f, n = cut(srcc, 0.5, L, f's-{len(pieces):03d}-{os.path.basename(srcc)[:-4]}-pan', vf=f"scale=1434:806,crop=1280:720:x='{x}':y='(ih-720)/2'", af='volume=-14dB')
        add(f, n, f'{label}: the line over the cafe ({os.path.basename(srcc)[:-4]}, a slow pan)', talk=True); left -= L; k += 1
    dubchunk(line, 0, p, t0, t1, t_line + 0.3, d, ROOM)
def denise_cutaway():
    """cut 7: the v07 take says three sentences ("It's not the boat, Barry, it's the landlord. / Put mine up twice this
    year. / And the council's put my rates up for the privilege.") and the c03b mouth says two, with a 1.9 s pause
    between. So: Denise for the first, a cutaway to Barry listening (the last second of his own c02p clip, mouth shut and the mug still in his hands, at half speed) for
    the second, Denise again for the third. Each sentence on a picture that can carry it."""
    clip, line = f'{V4}/c03b-denise4.mp4', 'v07-denise'
    w = words(clip); r1 = [x for x in w if x[0] < 4.0]; r2 = [x for x in w if x[0] >= 4.0]
    p, t0, t1 = tts(line); tw = TTSW[p]; sil = tts_pauses(p, t0, t1, d=0.08)
    ends = [next(x[1] for x in tw if x[2].lower().startswith(k)) for k in ('landlord', 'year')]   # the take's pauses are 0.1 and 0.35 s
    cuts = [min(sil, key=lambda q: abs(q[0] - e)) for e in ends]
    b = [t0] + [x for q in cuts for x in q] + [t1]; A, B, C = (b[0], b[1]), (b[2], b[3]), (b[4], b[5])
    a = r1[0][0] - 0.15; span1 = r1[-1][1] - r1[0][0]; nA = (A[1] - A[0]) / max(0.8, min(1.25, (A[1] - A[0]) / span1))
    f, n = cut(clip, a, r1[0][0] - a + nA + 0.15, f's-{len(pieces):03d}-c03b-denise4a', af='volume=0')
    dubchunk(line, 0, p, A[0], A[1], t / F + 0.15, span1); add(f, n, 'Denise (dub v07, sentence 1)', talk=True)
    nB = B[1] - B[0]
    f, n = cut(f'{V7}/c02p-barry7.mp4', 7.0, nB + 0.45, f's-{len(pieces):03d}-c02p-barry7-listens', vf='setpts=2.0*PTS', af='volume=0')   # his own clip's last second, mouth shut, mug in hands, at half speed
    dubchunk(line, 1, p, B[0], B[1], t / F + 0.2, nB); add(f, n, 'Barry listening, cutaway (dub v07, sentence 2, Denise off)', talk=True)
    a2 = r2[0][0] - 0.2; span2 = r2[-1][1] - r2[0][0]; nC = (C[1] - C[0]) / max(0.8, min(1.25, (C[1] - C[0]) / span2))
    f, n = cut(clip, a2, 0.2 + max(span2, nC) + 0.35, f's-{len(pieces):03d}-c03b-denise4b', af='volume=0')
    dubchunk(line, 2, p, C[0], C[1], t / F + 0.2, span2); add(f, n, 'Denise (dub v07, sentence 3)', talk=True)
def dubwhole(src, line, label, at=0.25, span=None, fx=''):
    """a whole cut 10 piece, muted, with the line laid over it"""
    d = dur(src); f, n = cut(src, 0.0, d, f's-{len(pieces):03d}-' + os.path.basename(src)[:-4], af='volume=0')
    dubline(line, t / F + at, span or d - at - 0.3, fx); add(f, n, f'{label} (dub {line})', talk=True)

# ---- made piece: the archive opening (Kai: real WW2 footage, more weight before the modern scenes)
# cut 4 (Jack: 'too long and has too much dead air'): four shots, each cut to its action, 5.9 s instead of 12.2
ARCH = [('wa-01-dunkirk-stuka-bombs-beach', 0.3, 1.5), ('wa-03-desert-tank-through-shellburst', 0.5, 1.4), ('wa-04-alamein-crusader-tank-charge', 0.6, 1.4), ('wa-05-alamein-bayonet-charge', 0.3, 1.6)]
BATTLE = P + '/vids/short/d01-dunkirk.mp4'   # the archive is silent: the old Flow Dunkirk clip's own sound (surf, gunfire, a dive bomber)
def archive():
    o = f'{OUT}/s-archive.mov'
    if not (os.path.exists(o) and os.path.getsize(o) > 0):
        ins, fc = [], ''
        for k, (c, a, d) in enumerate(ARCH): ins += ['-ss', str(a), '-t', str(d), '-i', f'{ARC}/{c}.mp4']; fc += f'[{k}:v]{FIT},format=yuv420p,setpts=PTS-STARTPTS[v{k}];'
        T = sum(x[2] for x in ARCH)
        fc += ''.join(f'[v{k}]' for k in range(len(ARCH))) + f'concat=n={len(ARCH)}:v=1,noise=alls=10:allf=t,fade=t=in:d=0.5[v];'
        fc += f'[{len(ARCH)}:a]atrim=0:{T},asetpts=PTS-STARTPTS,aresample=48000,aformat=channel_layouts=stereo,volume=3dB,afade=t=in:d=0.15[a]'
        run(ins + ['-i', BATTLE, '-filter_complex', fc, '-map', '[v]', '-map', '[a]', '-t', str(T)] + ENC + [o])
    return 's-archive.mov', fr(sum(x[2] for x in ARCH))

# ---- made piece: the deposit reveal, lingering on the press still (no new pictures: Jack, "dont change the videos")
def stillpush3(img, d, name, z1=1.3, cx=0.62, cy=0.62):
    return stillpush(img, d, name, z1, cx, cy, base=I3)
def stillpush(img, d, name, z1=1.3, cx=0.5, cy=0.55, base=None, flick=False):
    o = f'{OUT}/{name}.mov'
    if not (os.path.exists(o) and os.path.getsize(o) > 0):
        run(['-loop', '1', '-i', f'{base or IMG}/{img}.jpg', '-f', 'lavfi', '-i', f'anullsrc=r=48000:cl=stereo', '-filter_complex',
             f'[0:v]scale=1280:720,setsar=1,fps=24,trim=0:{d:.3f},setpts=PTS-STARTPTS,{zoomcrop(1.0, z1, d, cx, cy)},noise=alls=6:allf=t' + (',' + flicker(t / F) if flick else '') + '[v]', '-map', '[v]', '-map', '1:a', '-t', f'{d:.3f}'] + ENC + [o])
    return name + '.mov', fr(d)

# ---- made piece: the estate agent's window as a fruit machine (the meeting: "slot machine" prices doubling)
PRICES = ['£180,000', '£210,000', '£195,000', '£240,000', '£165,000', '£225,000']
STRIPS = [(348, 348), (643, 348), (938, 348), (348, 533), (643, 533), (938, 533)]   # centres of the white margins under each card, read off e01-estate at 1280x720
def slot(d=3.8):
    """cut 4: the new window plate (e01n-estate), three cards whose prices roll like fruit-machine reels in perspective
    (slot4.py, OpenCV); the clicks, a ding as each reel lands and the jackpot bell, as in cut 3"""
    o = f'{OUT}/s-slot4.mov'
    if not (os.path.exists(o) and os.path.getsize(o) > 0):
        plate = f'{V4}/e01n-estate.mp4' if os.path.exists(f'{V4}/e01n-estate.mp4') else f'{I4}/e01n-estate.jpg'
        subprocess.run([os.path.expanduser('~/.cache/badcode-recut/venv/bin/python'), H + '/slot4.py', plate, f'{OUT}/s-slot4', str(d)], check=True)
        R0, TK, stops = 0.5, 1 / 12, [1.5, 1.95, 2.4]; J = stops[-1] + 0.1
        clicks = '+'.join(f"0.35*between(t,{R0},{s})*sin(2*PI*2400*t)*exp(-mod(t,{TK:.5f})*260)" for s in stops)
        dings = '+'.join(f"0.25*gte(t,{s})*sin(2*PI*1760*t)*exp(-(t-{s})*14)" for s in stops)
        bell = f"gte(t,{J})*0.3*(sin(2*PI*1318.5*t)+sin(2*PI*1568*t)+sin(2*PI*2093*t))*exp(-(t-{J})*3)"
        run(['-i', f'{OUT}/s-slot4.v.mp4', '-f', 'lavfi', '-i', f"aevalsrc=exprs='({clicks}+{dings}+{bell})/3':s=48000:d={d}", '-t', f'{d:.3f}',
             '-filter_complex', '[0:v]setsar=1,fps=24[v];[1:a]aformat=channel_layouts=stereo,volume=-4dB[a]', '-map', '[v]', '-map', '[a]'] + ENC + [o])
    return 's-slot4.mov', fr(d)

# ---- cut 4: real banknote printing (Jack: "find real footage of that happening"). The ECB's own film of the 2015 EUR20
# being printed (Wikimedia Commons, CC BY 3.0, credit "ECB euro"); only shots with no readable currency: the purple ink
# going into the duct, the magenta roller. Graded down toward the brick room, grain, the credit small in the corner.
ECB = P + '/clips/short4/archive-print/ecb-euro20-printing-production.webm'
ECB_CUTS = [(89.0, 1.9, 'real: purple ink into the press duct (ECB)'), (281.0, 1.6, 'real: the magenta ink roller turning (ECB)')]
CREDIT = "drawtext=fontfile=/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf:text='Footage\\: ECB euro, CC BY 3.0':fontsize=15:fontcolor=white@0.7:x=24:y=h-36"
def ecb_inserts():
    out = []
    for k, (a, d, label) in enumerate(ECB_CUTS):
        f, n = cut(ECB, a, d, f's-ecb{k + 1}', vf='eq=brightness=-0.06:contrast=1.08:saturation=1.15:gamma_r=1.04:gamma_b=0.94,vignette=PI/5,noise=alls=7:allf=t,' + CREDIT, af='volume=0')
        out.append((f, n, label))
    return out

# ---- cut 6: the press as light and sound
PRESS_HZ = 1 / 0.49            # the ECB press's own beat, 0.49 s (autocorrelation of its sound at 67-87 s); light and bed share it
ECB_BED = 67.0                 # the ECB film's real press sound, clean of music and voice from 1:07 (listened)
FLICK = set(); STOP = [0.0]; QUIET = []; BED0 = [0.0]
def flicker(t0):
    return 'null'   # cut 7b (Jack: 'remove the flashing black screen thing, it is strange for the whole scenes when they print the money')
def flicker_cut6(t0):
    """the work lamp is cut by the press's moving arms once a beat: a short dip in exposure, in phase with the bed"""
    ph = f'((t+{t0:.4f}-{BED0[0] + 0.02:.4f})*{PRESS_HZ:.5f}+0.25)'   # the dip peaks on each thump of the bed (the first at +0.02 s)
    return f"eq=brightness='-0.09*pow(max(0,sin(2*PI*{ph})),6)':contrast='1-0.06*pow(max(0,sin(2*PI*{ph})),6)':eval=frame"
ECBGRADE = 'eq=brightness=-0.06:contrast=1.08:saturation=1.15:gamma_r=1.04:gamma_b=0.94,vignette=PI/5,noise=alls=7:allf=t'
KEY_IN, KEY_LEN, KEY_CLICK = 1.3, 0.7, 1.85     # m5-enter-key: the click is at 1.85 s in the clip (its loudest moment); the finger is already down
NR6_CLICK, NR6_PAY = 5.15, 5.9                 # nr6-print-pay: inside the 4.88-5.56 s pause after 'print the money'; 'pay' (silencedetect)
def press_bed(a, b):
    """the ECB's real press (its own sound, from ECB_BED), with a low synthetic thump under each of its beats for weight
    (cut 6's first bed was all synthetic and was heard as 'a tight, unvarying loop ... artificial'). Cut dead at b, the key's click."""
    d = b - a; o = 'press-bed.wav'
    thump = f"0.9*sin(2*PI*52*t)*exp(-mod(t+{1 / PRESS_HZ - 0.02:.4f},{1 / PRESS_HZ:.4f})*20)"
    run(['-f', 'lavfi', '-i', f"aevalsrc=exprs='{thump}':s=48000:d={d:.3f}", '-ss', f'{ECB_BED}', '-t', f'{d + 0.1:.3f}', '-i', ECB,
         '-filter_complex',
         f'[0:a]aformat=channel_layouts=stereo,lowpass=f=200,volume=-10dB[x];[1:a]aresample=48000,aformat=channel_layouts=stereo,atrim=0:{d:.3f},volume=3dB[y];'
         f'[x][y]amix=inputs=2:normalize=0,atrim=0:{d:.3f},afade=t=in:d=0.2,afade=t=out:st={d - 0.02:.3f}:d=0.02,apad=pad_dur=0.7,aecho=0.8:0.55:45|110|190:0.35|0.22|0.12,alimiter=limit=0.8:level=disabled[o]',   # the room rings on for a moment after the dead stop
         '-map', '[o]', '-c:a', 'pcm_s16le', '-t', f'{d + 0.7:.3f}', f'{OUT}/{o}'])
    dub.append([o, round(a, 4), round(d + 0.7, 3), 'press-bed', 1.0])
def screen(d, r0, r1):
    o = f'{OUT}/s-screen6.mov'
    if not (os.path.exists(o) and os.path.getsize(o) > 0):
        subprocess.run([os.path.expanduser('~/.cache/badcode-recut/venv/bin/python'), H + '/screen6.py', o, f'{d:.3f}', f'{r0:.3f}', f'{r1:.3f}'], check=True)
    return 's-screen6.mov', fr(d)

CHANT_IN, REPLY_IN = 3.0, 3.4   # cut 7b: the chant clip's police officer punches the air at 1.5-2.6 s, so in after it
def megaphone(clip, a, d, line, take, label, gain=0):
    """cut 7b (Jack: "the protesters shouting at each other ... sounds terrible, maybe they use megaphones and only hear
    the rest of the crowds background noise, so either side has one megaphone"). One voice a side, through the megaphone
    filter; the clip's own sound is muted (Omni sang its own chants into both, "We will not be moved!"); the crowd is the
    wordless roar under it (crowd_bed)."""
    f, n = cut(clip, a, d, f's-{len(pieces):03d}-' + os.path.basename(clip)[:-4], af='volume=0')
    p = f'{VOX}/take{take}/{line}.wav'; o = f'mega-{line}.wav'
    # loudnorm: the megaphone chain's compressor had left it at -34 LUFS, unheard under the roar
    run(['-i', p, '-af', f'{take_gain(p)},volume={gain}dB,{MEGA},apad=pad_dur=0.6,aecho=0.8:0.5:90|180:0.3|0.15,loudnorm=I=-14:TP=-1.5:LRA=7,aresample=48000', '-ac', '2', '-c:a', 'pcm_s16le', f'{OUT}/{o}'])
    at = t / F + 0.35; dd = dur(f'{OUT}/{o}'); dub.append([o, round(at, 4), round(dd, 3), label, 1.0]); speech.append((at, at + dd)); add(f, n, label, talk=True)
def crowd_bed(start, length):
    """the wide's own roar (no words in it: faster-whisper hears only its usual 'Thanks for watching!' on noise), run on
    past its 8 s by playing it backwards, which a roar survives; ducked under the megaphones, dying away under Denise"""
    w = f'{V3}/pr-w-wide.mp4'; o = 'crowd-bed.wav'
    run(['-ss', '2.9', '-i', w, '-i', w, '-filter_complex',
         f'[0:a]aresample=48000,aformat=channel_layouts=stereo[x];[1:a]aresample=48000,aformat=channel_layouts=stereo,areverse[y];[x][y]acrossfade=d=0.8[z];[z]atrim=0:{length:.3f},volume=-2dB,afade=t=in:d=0.3,afade=t=out:st={length - 3.0:.3f}:d=3.0[o]',
         '-map', '[o]', '-c:a', 'pcm_s16le', f'{OUT}/{o}'])
    dub.append([o, round(start, 4), round(dur(f'{OUT}/{o}'), 3), 'the crowd', 1.0])
# ---- the protest crowds: several TTS takes shouted together, laid over a muted crowd clip
def crowd(clip, a, d, lines, label, at=0.3, clipgain='volume=-14dB'):
    """lines: [(line_id, take, delay_s, gain_db)]. The clip keeps a little of its own crowd roar under the voices."""
    f, n = cut(clip, a, d, f's-{len(pieces):03d}-' + os.path.basename(clip)[:-4], af=clipgain)
    o = f'crowd-{len(pieces):03d}.wav'; ins, fc = [], ''
    for k, (ln, tk, dl, g) in enumerate(lines):
        ins += ['-i', f'{VOX}/take{tk}/{ln}.wav']; fc += f'[{k}:a]aresample=48000,aformat=channel_layouts=stereo,volume={g}dB,adelay={int(dl * 1000)}:all=1[c{k}];'
    fc += ''.join(f'[c{k}]' for k in range(len(lines))) + f'amix=inputs={len(lines)}:normalize=0,apad=pad_dur=1.8,aecho=0.8:0.6:70|140|260:0.45|0.3|0.18,afade=t=out:st={{END}}:d=1.8,alimiter=limit=0.9:level=disabled[o]'   # cut 5: the shout rings off the buildings instead of stopping mid-syllable
    end = max(dur(f'{VOX}/take{tk}/{ln}.wav') + dl for ln, tk, dl, g in lines)
    run(ins + ['-filter_complex', fc.replace('{END}', f'{end:.3f}'), '-map', '[o]', '-c:a', 'pcm_s16le', f'{OUT}/{o}'])
    cd = dur(f'{OUT}/{o}'); dub.append([o, round(t / F + at, 4), round(cd, 3), label, 1.0]); speech.append((t / F + at, t / F + at + cd)); add(f, n, label, talk=True)

# ---- the plan, in script order (short.md, "Cut 2")
def build():
    scenes.append(['cafe', t])
    f, n = archive(); A = n / F; add(f, n, 'A1: the action archive (Dunkirk Stuka, Alamein advance, tanks, bayonets)')
    narr.append(['na1-grandparents.wav', 0.6, round(dur(nwav('na1-grandparents')), 3)]); speech.append((0.6, 0.6 + narr[-1][2]))
    f, n = reveal(); add(f, n, 'the last archive shot, its last frame repainted, the painting on the cafe wall, pull back (no shake)')
    n3 = A + 3.0; narr.append(['ns03-one-bed.wav', round(n3, 3), round(dur(f'{NAR}/ns03-one-bed.wav'), 3)]); speech.append((n3, n3 + narr[-1][2]))
    # cut 4: Barry and Denise re-shot in the cafe of the wide (Jack: 'the painting changes into the old one')
    # cut 7b: every talking clip timed to its measured lips (lipsync); the rest of a line rides a cutaway
    # the cutaways are the listener with a shut mouth (spans read off lips-short.json), each stretch used once:
    # under Barry, Denise at her counter; under Denise, Barry with the mug (his own clip, half speed where it must stretch)
    DEN_A, DEN_C, DEN_D = (f'{V4}/c03a-denise4.mp4', 3.7), (f'{V4}/c03c-denise4.mp4', 3.4), (f'{V4}/c03d-denise4.mp4', 4.3)
    BAR_TAIL, BAR_MID, WIDE = (f'{V7}/c02p-barry7.mp4', 6.95, 'setpts=2.0*PTS'), (f'{V7}/c02p-barry7.mp4', 3.35, 'setpts=2.0*PTS'), (f'{V3}/c01b-cafe-wide.mp4', 4.0)
    # (Barry's three lags carry +0.2 s more after the sync check asked for it on all three; late is the safe side)
    # cut 7b: a face only where its clip passes (own speech = the dub's words, on the moving lips); lags measured
    ownsync(f'{V7}/c02f-barry-boxroom.mp4', 'v04-barry', 'Barry', 0.29); ownsync(f'{V7}/c03f-denise-gone-up.mp4', 'v05-denise', 'Denise', 0.08)
    ownsync(f'{V7}/c02p-barry7.mp4', 'v06-barry', 'Barry, the mug already in his hands', 0.0); cafepans('v07-denise', 'Denise (her clips fail the test)')
    ownsync(f'{V4}/c02c-barry4.mp4', 'v08-barry', 'Barry', 0.2); ownsync(f'{V7}/c03f-denise-daughter.mp4', 'v09-denise', 'Denise', 0.0, mode='warp')   # the warp scores better on her lips (0.61 vs 0.44)
    ownsync(f'{V7}/c04f-barry-freddo10.mp4', 'v10-barry', 'Barry, a real Freddo at 10p', 0.38)
    over('ns11-both-right', [(f'{V4}/b01n-bank.mp4', 0.3, 1)], label='ns11: the bank across the road, through the cafe window')
    scenes.append(['plan', t])
    # cut 6 (Jack: "fix it looking like ai ... flow clearly cant do this"): no AI press at all. The machine is only ever
    # the ECB's real film; the planners are only ever lit by it, never beside it; two stills of hands and glass; the
    # press is heard, and its rhythm is in the light. Then one key is pressed, the press stops dead, and the screen does it.
    p0 = t / F; BED0[0] = p0; nd = dur(nwav('ns12-masks')); need = 0.15 + nd + 0.45
    narr.append(['ns12-masks.wav', round(p0 + 0.15, 4), round(nd, 3)]); speech.append((p0 + 0.15, p0 + 0.15 + nd))
    MONT = [('ecb', 89.0, 1.0, 'real: purple ink into the press duct (ECB)'), ('ecb', 376.0, 0.8, 'real: the numbering heads turning (ECB)'),
            ('still', 'm1-glass-press', 0.9, 'still: whisky on the press feed board, ink, the work lamp'), ('ecb', 176.8, 0.7, 'real: printed sheets flying into the delivery (ECB)'),
            ('still', 'm2-band-brick', 0.9, 'still: a paper band pulled round a brick of new twenties')]
    for k, (kind, a, d, label) in enumerate(MONT):
        if k == len(MONT) - 1: d = max(d, need - sum(m[2] for m in MONT[:-1]))   # the last still holds to the end of the line
        if kind == 'ecb': f, n = cut(ECB, a, d, f's-{len(pieces):03d}-ecb', vf=ECBGRADE + ',' + CREDIT, af='volume=0')
        else: f, n = stillpush(a, d, f's-{len(pieces):03d}-{a}', z1=1.12, cx=0.5, cy=0.5, base=I4, flick=True)
        add(f, n, label)
    FLICK.update({f'{V4}/m3-ex-lamp.mp4', f'{V4}/m4-red-blue-toast.mp4'})
    # the press room keeps cut 7b's lip-run timing: both own-speech searches hit their stretch limit on these two clips
    lipsync(f'{V4}/m3-ex-lamp.mp4', 'v13-ex', 'The Ex, lit by the press lamp', (ECB, 376.0), cvf=ECBGRADE + ',' + CREDIT)
    lipsync(f'{V4}/m4-red-blue-toast.mp4', 'v14-red', 'Mr Red and Mr Blue from above, the toast', (ECB, 330.0), cvf=ECBGRADE + ',' + CREDIT)
    # Jack on cut 6: 'the narrator should say "this lot print the money then pay it in"' and 'there is not enough of the
    # money being printed'. So R1 is one new line, placed whole (nr6-print-pay, take c, +2.3 dB to sit with the others),
    # over a second montage of sheer volume (the ECB's pallets and trolleys of printed sheets, a table buried in bricks);
    # the key's click lands in its pause after "print the money", the press stops dead, and the screen lands PAID IN on "pay".
    nd = dur(nwav('nr6-print-pay')); n0 = t / F + 0.2
    narr.append(['nr6-print-pay.wav', round(n0, 4), round(nd, 3)]); speech.append((n0, n0 + nd))
    L2 = 0.2 + NR6_CLICK - (KEY_CLICK - KEY_IN)
    MONT2 = [('ecb', 128.5, 0.8, 'real: printed sheets streaming through (ECB), shifted to the twenty\'s purple', 'hue=h=45:s=1.4,'), ('ecb', 142.0, 0.9, 'real: a pallet of printed sheets pushed off the press (ECB)', ''),
             ('still', 'm7-table-bricks', 1.0, 'still: a table buried in banded bricks of twenties', ''), ('ecb', 330.0, 0.9, 'real: a trolley tower of printed stacks (ECB)', ''),
             ('ecb', 515.0, 0.7, 'real: bundles shrink-wrapped (ECB)', '')]
    for k, (kind, a, d, label, pre) in enumerate(MONT2):
        if k == len(MONT2) - 1: d = max(d, L2 - sum(m[2] for m in MONT2[:-1]))
        if kind == 'ecb': f, n = cut(ECB, a, d, f's-{len(pieces):03d}-ecb', vf=pre + ECBGRADE + ',' + CREDIT, af='volume=0')
        else: f, n = stillpush(a, d, f's-{len(pieces):03d}-{a}', z1=1.15, cx=0.5, cy=0.5, base=I4, flick=True)
        add(f, n, label)
    k0 = t / F
    f, n = cut(f'{V4}/m5-enter-key.mp4', KEY_IN, KEY_LEN, f's-{len(pieces):03d}-m5-enter-key', af='volume=6dB'); add(f, n, 'the key pressed in the pause: the press stops dead')
    STOP[0] = k0 + (KEY_CLICK - KEY_IN)
    s0 = t / F; d = max(3.0, n0 + nd + 1.6 - s0)
    f, n = screen(d, 0.05, n0 + NR6_PAY - s0); add(f, n, 'R1: the terminal, the credit rolls to £200,000,000,000, PAID IN on "then pay it in"')
    QUIET[:] = [STOP[0], t / F]
    press_bed(p0, STOP[0])
    scenes.append(['march', t])
    over('np1-shout', [(f'{C9}/c9-paper-blue.mov', 0.0, 1), (f'{C9}/c9-paper-red.mov', 0.0, 1)], tail=2.4, label='P1: the newspaper drops (cut 9 front pages)')
    # cut 7b (Jack: 'the whole crowd are white people please diversify the crowd, but keep the camera shot and vibe'): the
    # re-made wide (pr-w7b), with the old wide's wordless roar under it (the new clip's own sound is not trusted)
    run(['-ss', '0.3', '-t', '2.6', '-i', f'{V3}/pr-w-wide.mp4', '-af', 'aresample=48000,volume=-3dB,afade=t=in:d=0.05', '-ac', '2', '-c:a', 'pcm_s16le', f'{OUT}/wide-roar.wav'])
    dub.append(['wide-roar.wav', round(t / F, 4), 2.6, 'the crowd', 1.0])
    f, n = cut(f'{V7}/pr-w7b-wide.mp4', 0.3, 2.6, f's-{len(pieces):03d}-pr-w7b-wide', af='volume=0'); add(f, n, 'the protest from the bank: two mixed crowds, nobody looking up')
    c0 = t / F
    megaphone(f'{V7}/pr-a7m-chant.mp4', CHANT_IN, 4.4, 'v17c-a1', 1, 'the chant: one megaphone, the woman at the front')
    megaphone(f'{V7}/pr-b7m-reply.mp4', REPLY_IN, 4.6, 'v17r-b1', 1, 'the reply: one megaphone, Barry')
    crowd_bed(c0, t / F - c0 + 3.6)
    # cut 4: the crowd used to stop dead on the cut to Denise; its roar now dies away under her
    over('ns19-first-line', [('r04-denise-window', 0.5, 1)])
    over('ns1-side-door', [(f'{V4}/s01n-side-door.mp4', 3.4, 1)], tail=0.6, af='afade=t=out:st={st:.2f}:d=1.2',   # its first 3 s open the door wider with a figure in it: the still half only
         label='S1: the side door ajar, light in the gap (re-made)')
    scenes.append(['bank', t])
    # cut 4 (Jack: 'we need to show them putting the printed money in the bank'): the key and the pallet out, the deposit in
    # cut 7b (Jack: 'when they put the money in, it looks unrealistic ... make quick cuts of them doing it to avoid
    # artifacts'): five stills, no faces, each a short exact push (no AI motion to go wrong), over the old vault clips' room
    v0 = t / F
    for img, d_, z, cx, cy, lab in [('vq1-door-trolley', 1.1, 1.08, 0.55, 0.6, 'the trolley of bricks through the vault door'),
                                    ('vq3-trolley-above', 0.85, 1.1, 0.6, 0.45, 'from above, a gloved hand lifts a brick off the trolley'),
                                    ('vq2-hands-shelf', 1.0, 1.1, 0.4, 0.45, 'gloved hands press the last brick onto the shelf'),
                                    ('vq4-shelves', 1.0, 1.06, 0.5, 0.5, 'the aisle, shelves packed to the ceiling'),
                                    ('vq5-door-shut', 1.6, 1.08, 0.7, 0.55, 'the vault door almost shut, a gloved hand on the wheel')]:
        f, n = stillpush(img, d_, f's-{len(pieces):03d}-{img}', z1=z, cx=cx, cy=cy, base=P + '/images/short7'); add(f, n, 'the vault, quick cuts: ' + lab)
    vd = t / F - v0
    run(['-ss', '0.4', '-i', f'{V4}/v1-deposit-wide.mp4', '-ss', '0.4', '-i', f'{V8}/s11g-full.mp4', '-filter_complex',
         f'[0:a]atrim=0:2.5,asetpts=PTS-STARTPTS[a];[1:a]atrim=0:3.4,asetpts=PTS-STARTPTS[b];[a][b]acrossfade=d=0.5,atrim=0:{vd:.3f},aresample=48000,volume=-6dB,afade=t=out:st={vd - 0.6:.3f}:d=0.6[o]',
         '-map', '[o]', '-ac', '2', '-c:a', 'pcm_s16le', f'{OUT}/vault-room.wav'])
    dub.append(['vault-room.wav', round(v0, 4), round(vd, 3), 'the vault room', 1.0])
    over('ns23-just-early', [('e02-donor-keys', 0.4, 1)], label='the Donor and the keys')
    f, n = slot(); add(f, n, 'the window as a fruit machine, prices double')
    ownsync(f'{V7}/f02f-barry-freddo20.mp4', 'v24-barry', 'Barry, the Freddo at 20p', 0.34); cafepans('v25-denise', 'Denise (her clip fails the test)', shot_len=1.8)
    over('ns26-no-law', [(f'{V3}/c01b-cafe-wide.mp4', 0.0, 1)], off=0.2, tail=0.5)
    scenes.append(['ending', t])
    silent('s01-sink', 1.0, 3.5, 'Denise at the sink, the letter')
    silent('c10-081-08349', 0.5, 4.0, 'the badcode kebab shop (cut 10)')
build()
TOTAL = t

# ---- cut 5: transitions (Jack: "put transitions that fit and make it look cinematic, so it is not only hard cuts").
# Dissolves where the film changes place or time, dips to black where it goes inside or to the end; hard cuts kept inside
# the cafe conversation, the protest and the vault, and on the jokes (the slot to the 20p Freddo). Each transition is a
# segment centred on the cut: the outgoing piece runs on past the cut and the incoming one starts before it, from the
# source clip's own frames where it has them (a frozen frame where it does not), so nothing moves in time.
TRANS = [('c04f-barry-freddo10', 'fade', 0.5),      # the Freddo, to the bank through the window
         ('b01n-bank', 'fadeblack', 0.75),    # the cafe, to the printing room
         ('s-screen6', 'fadeblack', 0.5),     # PAID IN, to the front pages
         ('c9-paper-red', 'fade', 0.42),      # the front pages, to the crowd
         ('pr-b7m-reply', 'fade', 0.67),      # the crowd, to Denise watching it
         ('r04-denise-window', 'fade', 0.67), # Denise, to the side door at night
         ('s01n-side-door', 'fadeblack', 0.5),# in through the door, to the vault
         ('vq5-door-shut', 'fade', 0.75),     # the vault shut, to the man who spends it
         ('e02-donor-keys', 'fade', 0.42),    # the keys, to the window
         ('c01b-cafe-wide', 'fade', 0.83),    # the cafe, to Denise at the sink
         ('s01-sink', 'fadeblack', 0.83)]     # the sink, to the kebab shop
def hframes(D): return max(2, int(round(D * F / 2)))
def window(f, start, length, edge):
    """input args, vf and af for `length` s of piece f starting `start` s from the piece's own start (may be < 0 or run past its end)"""
    m = META.get(f)
    if m:
        src, a, d, vf, af = m; t0 = a + start
        if t0 >= 0 and t0 + length <= dur(src) - 0.05:
            return ['-ss', f'{t0:.4f}', '-t', f'{length + 0.1:.4f}', '-i', src], FIT + (',' + vf if vf and 'tpad' not in vf else ''), (af or 'anull')
    n = dur(f'{OUT}/{f}')
    if edge == 'out':   # run past the end on the last frame
        return ['-ss', f'{max(0, start):.4f}', '-i', f'{OUT}/{f}'], f'{FIT},tpad=stop_mode=clone:stop_duration={length:.3f}', 'apad'
    return ['-i', f'{OUT}/{f}'], f'{FIT},tpad=start_mode=clone:start_duration={-start:.3f}', f'adelay={int(-start * 1000)}:all=1'
def segment(i, kind, D):
    (f0, s0, n0), (f1, s1, n1) = pieces[i], pieces[i + 1]; h = hframes(D) / F; L = 2 * h
    o = f'x-{i:03d}-{kind}.mov'
    if not (os.path.exists(f'{OUT}/{o}') and os.path.getsize(f'{OUT}/{o}') > 0):
        i0, v0, a0 = window(f0, n0 / F - h, L, 'out'); i1, v1, a1 = window(f1, -h, L, 'in')
        print('segment', i, f0, '->', f1, i0[-1:], i1[-1:])
        fc = (f'[0:v]{v0},trim=0:{L:.4f},setpts=PTS-STARTPTS,fps=24,settb=1/24[a];[1:v]{v1},trim=0:{L:.4f},setpts=PTS-STARTPTS,fps=24,settb=1/24[b];'
              f'[a][b]xfade=transition={kind}:duration={L:.4f}:offset=0,tpad=stop_mode=clone:stop_duration=0.125[v];'
              f'[0:a]aresample=48000,aformat=channel_layouts=stereo,{a0},apad,atrim=0:{L:.4f},asetpts=PTS-STARTPTS,afade=t=out:d={L:.4f}[x];'
              f'[1:a]aresample=48000,aformat=channel_layouts=stereo,{a1},apad,atrim=0:{L:.4f},asetpts=PTS-STARTPTS,afade=t=in:d={L:.4f}[y];'
              f'[x][y]amix=inputs=2:normalize=0[au]')
        run(i0 + i1 + ['-filter_complex', fc, '-map', '[v]', '-map', '[au]', '-t', f'{L + 0.125:.4f}'] + ENC + [f'{OUT}/{o}'])   # cut 7: a spare frame, or Premiere reads one frame short (x-010, x-027 left 1-frame gaps)
    return o, hframes(D)
def trimmed(f, cut_in, cut_out, n):
    """piece f without its first cut_in and last cut_out frames"""
    if not (cut_in or cut_out): return f, n
    o = f't-{cut_in}-{cut_out}-{f}'
    if not (os.path.exists(f'{OUT}/{o}') and os.path.getsize(f'{OUT}/{o}') > 0):
        run(['-i', f'{OUT}/{f}', '-vf', f'trim=start_frame={cut_in}:end_frame={n - cut_out},setpts=PTS-STARTPTS', '-af', f'atrim=start={cut_in / F:.5f}:end={(n - cut_out) / F:.5f},asetpts=PTS-STARTPTS'] + ENC + [f'{OUT}/{o}'])
    return o, n - cut_in - cut_out
RAW = pieces[:]
at = {}
for key, kind, D in TRANS:
    i = max(k for k, (f, _, _) in enumerate(pieces) if key in f); at[i] = (kind, D)   # cut 7b: a line can be several pieces now; the transition follows the last
final, cin = [], 0
for i, (f, s0, n) in enumerate(pieces):
    cout = 0
    if i in at: seg, hh = segment(i, *at[i]); cout = hh
    g, m = trimmed(f, cin, cout, n); final.append([g, s0 + cin, m])
    if i in at: final.append([seg, s0 + n - hh, 2 * hh]); cin = hh
    else: cin = 0
assert sum(x[2] for x in final) == TOTAL, (sum(x[2] for x in final), TOTAL)
pieces = final

DUBGAIN = {'the vault room': 0, 'the crowd': -5,  'the crowd dying away': 0, 'press-bed': -2}   # cut 4: dubs +2 dB on cut 3, the last two +4 (heard thin)

# ---- music: one lofi cue per scene, ducked under every line (same recipe as cut 10)
CUES = {'cafe': ('01-cafe-holiznacc0-busking-in-the-sunlight.mp3', 10.2), 'plan': ('02-plan-holiznacc0-busted-jazz.mp3', 10.0),
        'march': ('04-march-holiznacc0-never-sleeping.mp3', 11.0), 'bank': ('05-bank-holiznacc0-cellar-door.mp3', 11.0),
        'ending': ('06-ending-holiznacc0-all-the-way-sad.mp3', 0.0)}
CAFE_IN = sum(x[2] for x in ARCH) + 2.2   # music starts as the cafe arrives
scenes.append(['end', TOTAL]); music = []
for i, (name, s0) in enumerate(scenes[:-1]):
    s1 = scenes[i + 1][1]; fn, inn = CUES[name]; a = max(0.0, s0 / F - (0.0 if i == 0 else 1.0)); b = s1 / F + (1.5 if i < len(scenes) - 2 else 0.0); d = b - a
    if name == 'cafe': a, d = a + CAFE_IN, d - CAFE_IN   # no music under the archive or the battle
    env = '+'.join(f'between(t,{max(0, x - a - 0.25):.2f},{y - a + 0.35:.2f})' for x, y in speech if y > a and x < b) or '0'
    q = f'between(t,{QUIET[0] - a:.3f},{QUIET[1] - a:.3f})' if QUIET and QUIET[1] > a and QUIET[0] < b else '0'   # cut 6: nothing but the key and the screen
    o = f'ms-{i + 1:02d}-{name}.wav'; fo = 1.5 if i < len(scenes) - 2 else 2.5
    run(['-ss', f'{inn}', '-i', f'{MUS}/{fn}', '-t', f'{d:.3f}', '-af', f"loudnorm=I=-14.5:TP=-2:LRA=11,aresample=48000,volume='if(gt({q},0),0,if(gt({env},0),0.24,0.52))':eval=frame,asetnsamples=480,afade=t=in:d={1.0},afade=t=out:st={d - fo:.3f}:d={fo}", '-ac', '2', '-c:a', 'pcm_s16le', f'{OUT}/{o}'])
    music.append([o, round(a, 4), round(d, 3), 2 + i % 2])
json.dump({'pieces': [[f, s / F, n / F] for f, s, n in pieces], 'narr': narr, 'dub': dub, 'music': music, 'total': TOTAL / F, 'scenes': [[n, s / F] for n, s in scenes]}, open(H + '/edl-short7.json', 'w'), indent=1)
open(H + '/edl-short7.txt', 'w').write('The Bank Robbery short, cut 7. start, length, file, what.\n\n' + ''.join(f'{s:8.3f}  {d:6.3f}  {f:34s} {n}\n' for s, d, f, n in notes) + '\nNarrator:\n' + ''.join(f'{s:8.3f}  {d:6.3f}  {f}\n' for f, s, d in narr) + '\nCharacter voices (dub):\n' + ''.join(f'{s:8.3f}  {d:6.3f}  {f}  x{tp}\n' for f, s, d, l, tp in dub) + '\nMusic:\n' + ''.join(f'{s:8.3f}  {d:6.3f}  {f}  A{tr + 1}\n' for f, s, d, tr in music))
print(len(pieces), 'pieces', len(narr), 'narrator lines', len(dub), 'voice lines', len(music), 'cues; total', round(TOTAL / F, 2), 's')
if '--preview' in sys.argv:
    lst = OUT + '/preview.txt'; open(lst, 'w').write(''.join(f"file '{OUT}/{f}'\noutpoint {n / F:.5f}\n" for f, s, n in pieces))
    ins = ['-f', 'concat', '-safe', '0', '-i', lst]; fc = '[0:a]volume=1.0[a0];'; mix = '[a0]'
    for k, (f, s, d) in enumerate(narr): ins += ['-i', nwav(f[:-4])]; fc += f'[{k + 1}:a]volume=2dB,adelay={int(s * 1000)}:all=1[n{k}];'; mix += f'[n{k}]'
    for k, (f, s, d, l, tp) in enumerate(dub): ins += ['-i', f'{OUT}/{f}']; fc += f'[{len(narr) + 1 + k}:a]volume={DUBGAIN.get(l, 4)}dB,adelay={int(s * 1000)}:all=1[d{k}];'; mix += f'[d{k}]'
    for k, (f, s, d, tr) in enumerate(music): ins += ['-i', f'{OUT}/{f}']; fc += f'[{len(narr) + len(dub) + 1 + k}:a]adelay={int(s * 1000)}:all=1[m{k}];'; mix += f'[m{k}]'
    fc += f'{mix}amix=inputs={1 + len(narr) + len(dub) + len(music)}:normalize=0:duration=first,loudnorm=I=-14:TP=-1.5:LRA=11,aresample=48000[a]'   # cut 4: to the delivery target
    run(ins + ['-filter_complex', fc, '-map', '0:v', '-map', '[a]', '-vf', f'fade=t=out:st={TOTAL / F - 1.2:.3f}:d=1.2,scale=in_range=full:out_range=limited', '-c:v', 'libx264', '-crf', '20', '-preset', 'veryfast', '-pix_fmt', 'yuv420p', '-r', '24', '-c:a', 'aac', '-b:a', '192k', ] + TAG + [OUT + '/preview-short7.mp4'])
    print('preview', dur(OUT + '/preview-short7.mp4'))
