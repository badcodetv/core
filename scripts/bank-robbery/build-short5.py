#!/usr/bin/env python3
"""The Bank Robbery SHORT, cut 5 (2026-10-18, later): cut 4 with Jack's two notes: "some of the audio cuts off early,
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
OUT, V, IMG, NAR, MUS, C10 = P + '/clips/short5', P + '/vids/short', P + '/images/short', P + '/narrator/short', P + '/music/lofi', P + '/clips/cut10'
V3, I3, ARC, V7, V8 = P + '/vids/short3', P + '/images/short3', P + '/clips/short3/archive', P + '/vids/v7', P + '/vids/v8'
V4, I4 = P + '/vids/short4', P + '/images/short4'
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
def nwav(line): return f'{NAR2}/{line}.wav' if os.path.exists(f'{NAR2}/{line}.wav') else f'{NAR}/{line}.wav'
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
def reveal():
    """cut 3: the last archive shot (a soldier striding through smoke) plays out, holds on its last frame, dissolves into
    the same frame repainted (a01-painting), and that dissolves into the new cafe wide cropped to the painting on the
    wall, which pulls back to the whole room. Eased zooms only: no shake anywhere."""
    o = f'{OUT}/s-reveal4.mov'
    if not (os.path.exists(o) and os.path.getsize(o) > 0):
        we, pa, cf = f'{ARC}/wa-end-alamein-soldier-through-smoke.mp4', f'{I3}/a01-painting.jpg', f'{V3}/c01b-cafe-wide.mp4'
        pcx, pcy, pw = (CANVAS[0] + CANVAS[2]) / 2, (CANVAS[1] + CANVAS[3]) / 2, CANVAS[2] - CANVAS[0]
        T0 = sum(x[2] for x in ARCH)
        fc = (f"[0:v]{FIT},noise=alls=10:allf=t,tpad=stop_mode=clone:stop_duration=0.4,trim=0:1.9,setpts=PTS-STARTPTS,fps=24,settb=1/24[w];"
              f"[1:v]scale=1280:720,setsar=1,loop=loop=-1:size=1:start=0,fps=24,trim=0:1.8,setpts=PTS-STARTPTS,{zoomcrop(1.0, 1.03, 1.8, 0.5, 0.5)},fps=24,settb=1/24[pt];"
              f"[2:v]{FIT},trim=0:3.8,setpts=PTS-STARTPTS,{zoomcrop(round(1 / pw, 3), 1.0, 2.4, pcx, pcy)},fps=24,settb=1/24[cafe];"
              f"[w][pt]xfade=transition=fade:duration=0.5:offset=1.4[a1];[a1][cafe]xfade=transition=fade:duration=0.4:offset=2.8[v];"
              f"[3:a]atrim=4.0:8.0,asetpts=PTS-STARTPTS,aresample=48000,aformat=channel_layouts=stereo,volume=3dB,afade=t=out:st=1.6:d=2.2[ba];"
              f"[2:a]atrim=0:5.5,asetpts=PTS-STARTPTS,volume=-3dB,afade=t=in:d=1.0,adelay=1100:all=1[ca];"
              f"[ba][ca]amix=inputs=2:normalize=0:duration=longest,apad,atrim=0:6.6[a]")
        run(['-i', we, '-i', pa, '-i', cf, '-i', BATTLE, '-filter_complex', fc, '-map', '[v]', '-map', '[a]', '-t', '6.6'] + ENC + [o])
    return 's-reveal4.mov', fr(6.6)

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
def tts(line):
    p = f'{VOX}/take{PICK[line]}/{line}.wav'; w = TTSW[p]; a, b = sound_span(p)
    return p, a, max(w[-1][1], b)   # the sound's own start: a word time of 0.00 over half a second of silence put the voice in late
def dubline(line, at, span, fx=''):
    """write the line stretched toward span seconds (0.8-1.25x) and lay it at `at` seconds on the dub track"""
    p, t0, t1 = tts(line); d = t1 - t0; tempo = max(0.8, min(1.25, d / span)); nd = d / tempo
    o = f'dub-{line}.wav'
    run(['-ss', f'{max(0, t0 - 0.06):.3f}', '-t', f'{min(dur(p) - max(0, t0 - 0.06), d + 0.3):.3f}', '-i', p, '-af', f'atempo={tempo:.4f}' + (',' + fx if fx else '') + ',areverse,silenceremove=start_periods=1:start_threshold=-45dB,areverse,aresample=48000', '-ac', '2', '-c:a', 'pcm_s16le', f'{OUT}/{o}'])
    dub.append([o, round(at, 4), round(dur(f'{OUT}/{o}'), 3), line, round(tempo, 3)]); speech.append((at, at + nd)); return nd   # cut 5: placed at the file's whole length
def dubtalk(clip, line, label, lead=0.15, tail=0.35, upto=None, fx=''):
    """cut 1's picture of a talk clip, muted, one continuous range round the mouth's words; the TTS line laid where
    the mouth moves. If the stretched line runs past the words the range is lengthened, holding the last frame if
    the clip runs out."""
    w = [list(x) for x in words(clip)]
    if upto: w = w[:next(i for i, x in enumerate(w) if x[2].lower().startswith(upto)) + 1]
    if w[0][1] - w[0][0] > 0.8: w[0][0] = w[0][1] - 0.8
    s0, s1 = w[0][0], w[-1][1]; end = dur(src(clip))
    p, t0, t1 = tts(line); nd = (t1 - t0) / max(0.8, min(1.25, (t1 - t0) / (s1 - s0)))
    a = max(0.0, s0 - lead); b = max(s1, s0 + nd) + tail; hold = max(0.0, b - end)
    f, n = cut(src(clip), a, b - a, f's-{len(pieces):03d}-{os.path.basename(clip)[:-4] if clip.startswith("/") else clip}', vf=f'tpad=stop_mode=clone:stop_duration={hold + 0.1:.2f}' if hold > 0 else '', af='volume=0')
    dubline(line, t / F + (s0 - a), s1 - s0, fx); add(f, n, f'{label} (dub {line})', talk=True)
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
def stillpush(img, d, name, z1=1.3, cx=0.5, cy=0.55, base=None):
    o = f'{OUT}/{name}.mov'
    if not (os.path.exists(o) and os.path.getsize(o) > 0):
        run(['-loop', '1', '-i', f'{base or IMG}/{img}.jpg', '-f', 'lavfi', '-i', f'anullsrc=r=48000:cl=stereo', '-filter_complex',
             f'[0:v]scale=1280:720,setsar=1,fps=24,trim=0:{d:.3f},setpts=PTS-STARTPTS,{zoomcrop(1.0, z1, d, cx, cy)},noise=alls=6:allf=t[v]', '-map', '[v]', '-map', '1:a', '-t', f'{d:.3f}'] + ENC + [o])
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
    dubtalk(f'{V4}/c02a-barry4.mp4', 'v04-barry', 'Barry'); dubtalk(f'{V4}/c03a-denise4.mp4', 'v05-denise', 'Denise'); dubtalk(f'{V4}/c02b-barry4f.mp4', 'v06-barry', 'Barry')
    dubtalk(f'{V4}/c03b-denise4.mp4', 'v07-denise', 'Denise'); dubtalk(f'{V4}/c02c-barry4.mp4', 'v08-barry', 'Barry'); dubtalk(f'{V4}/c03c-denise4.mp4', 'v09-denise', 'Denise')
    dubtalk(f'{V4}/c04n-freddo10.mp4', 'v10-barry', 'Barry, a real Freddo at 10p')
    over('ns11-both-right', [(f'{V4}/b01n-bank.mp4', 0.3, 1)], label='ns11: the bank across the road, through the cafe window')
    scenes.append(['plan', t])
    # cut 4 (Jack: 'printing money part looks unrealistic'): two real inserts, then the room re-made around a real press
    ins = ecb_inserts(); nd = dur(nwav('ns12-masks')); ti = sum(n for _, n, _ in ins) / F
    narr.append(['ns12-masks.wav', round(t / F + 0.15, 4), round(nd, 3)]); speech.append((t / F + 0.15, t / F + 0.15 + nd))
    for f, n, label in ins: add(f, n, label)
    silent(f'{V4}/p05-press-wide.mp4', 0.3, max(1.8, 0.15 + nd + 0.3 - ti), 'ns12: the brick room, a real modern press, the men drinking', gain='volume=-6dB')
    dubtalk(f'{V4}/p06-ex.mp4', 'v13-ex', 'The Ex'); dubtalk(f'{V4}/p07-red.mp4', 'v14-red', 'Mr Red')
    nd = dur(nwav('nr1-paying-in')); d = 0.3 + nd + 1.8
    narr.append(['nr1-paying-in.wav', round(t / F + 0.3, 4), round(nd, 3)]); speech.append((t / F + 0.3, t / F + 0.3 + nd))
    f, n = stillpush('p05-press-wide', d, 's-r1-press4', z1=1.3, cx=0.66, cy=0.62, base=I4); add(f, n, 'R1: the deposit reveal, a slow push on the delivery stack')
    scenes.append(['march', t])
    over('np1-shout', [(f'{C9}/c9-paper-blue.mov', 0.0, 1), (f'{C9}/c9-paper-red.mov', 0.0, 1)], tail=2.4, label='P1: the newspaper drops (cut 9 front pages)')
    silent(f'{V3}/pr-w-wide.mp4', 0.3, 2.6, 'the protest from the bank: two crowds, nobody looking up', gain='volume=-3dB')
    crowd(f'{V3}/pr-a-chant.mp4', 3.6, 4.4, [('v17c-a1', 1, 0.0, 0), ('v17c-a2', 2, 0.06, -1), ('v17c-a3', 2, 0.12, -2), ('v17c-a4', 2, 0.03, -2)], 'the chant (four voices)')
    crowd(f'{V3}/pr-b-reply.mp4', 3.4, 4.6, [('v17r-b1', 1, 0.0, 1), ('v17r-b4', 1, 0.08, -3), ('v17r-b2', 1, 0.15, -4), ('v17r-b3', 1, 0.05, -4)], 'the reply, Barry leading (four voices)')
    # cut 4: the crowd used to stop dead on the cut to Denise; its roar now dies away under her
    run(['-i', f'{V3}/pr-a-chant.mp4', '-t', '3.6', '-af', 'aresample=48000,volume=2dB,afade=t=in:d=0.05,afade=t=out:st=0.3:d=3.3', '-ac', '2', '-c:a', 'pcm_s16le', f'{OUT}/crowd-tail.wav'])
    dub.append(['crowd-tail.wav', round(t / F - 0.05, 4), 3.6, 'the crowd dying away', 1.0])
    over('ns19-first-line', [('r04-denise-window', 0.5, 1)])
    over('ns1-side-door', [(f'{V4}/s01n-side-door.mp4', 3.4, 1)], tail=0.6, af='afade=t=out:st={st:.2f}:d=1.2',   # its first 3 s open the door wider with a figure in it: the still half only
         label='S1: the side door ajar, light in the gap (re-made)')
    scenes.append(['bank', t])
    # cut 4 (Jack: 'we need to show them putting the printed money in the bank'): the key and the pallet out, the deposit in
    silent(f'{V4}/v1-deposit-wide.mp4', 0.4, 3.0, 'the vault: a brick of new notes slid onto the shelf, ticked off', gain='volume=-6dB')
    silent(f'{V4}/v2-deposit-close.mp4', 0.3, 2.2, 'the vault: the last brick pressed home', gain='volume=-6dB')
    silent(f'{V8}/s11g-full.mp4', 0.4, 3.4, 'the vault full, the door shut (v8)', gain='volume=-10dB')
    over('ns23-just-early', [('e02-donor-keys', 0.4, 1)], label='the Donor and the keys')
    f, n = slot(); add(f, n, 'the window as a fruit machine, prices double')
    dubtalk(f'{V4}/f02n-freddo20f.mp4', 'v24-barry', 'Barry, the Freddo at 20p'); dubtalk(f'{V4}/c03d-denise4.mp4', 'v25-denise', 'Denise', upto='landlord')
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
TRANS = [('c04n-freddo10', 'fade', 0.5),      # the Freddo, to the bank through the window
         ('b01n-bank', 'fadeblack', 0.75),    # the cafe, to the printing room
         ('s-ecb2', 'fade', 0.5),             # the real press, into the made room
         ('s-r1-press4', 'fadeblack', 0.5),   # the reveal, to the front pages
         ('c9-paper-red', 'fade', 0.42),      # the front pages, to the crowd
         ('pr-b-reply', 'fade', 0.67),        # the crowd, to Denise watching it
         ('r04-denise-window', 'fade', 0.67), # Denise, to the side door at night
         ('s01n-side-door', 'fadeblack', 0.5),# in through the door, to the vault
         ('s11g-full', 'fade', 0.75),         # the vault shut, to the man who spends it
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
        fc = (f'[0:v]{v0},trim=0:{L:.4f},setpts=PTS-STARTPTS,fps=24,settb=1/24[a];[1:v]{v1},trim=0:{L:.4f},setpts=PTS-STARTPTS,fps=24,settb=1/24[b];'
              f'[a][b]xfade=transition={kind}:duration={L:.4f}:offset=0[v];'
              f'[0:a]aresample=48000,aformat=channel_layouts=stereo,{a0},apad,atrim=0:{L:.4f},asetpts=PTS-STARTPTS,afade=t=out:d={L:.4f}[x];'
              f'[1:a]aresample=48000,aformat=channel_layouts=stereo,{a1},apad,atrim=0:{L:.4f},asetpts=PTS-STARTPTS,afade=t=in:d={L:.4f}[y];'
              f'[x][y]amix=inputs=2:normalize=0[au]')
        run(i0 + i1 + ['-filter_complex', fc, '-map', '[v]', '-map', '[au]', '-t', f'{L:.4f}'] + ENC + [f'{OUT}/{o}'])
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
    i = next(k for k, (f, _, _) in enumerate(pieces) if key in f); at[i] = (kind, D)
final, cin = [], 0
for i, (f, s0, n) in enumerate(pieces):
    cout = 0
    if i in at: seg, hh = segment(i, *at[i]); cout = hh
    g, m = trimmed(f, cin, cout, n); final.append([g, s0 + cin, m])
    if i in at: final.append([seg, s0 + n - hh, 2 * hh]); cin = hh
    else: cin = 0
assert sum(x[2] for x in final) == TOTAL, (sum(x[2] for x in final), TOTAL)
pieces = final

DUBGAIN = {'v24-barry': 6, 'v25-denise': 6, 'the crowd dying away': 0}   # cut 4: dubs +2 dB on cut 3, the last two +4 (heard thin)

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
    o = f'ms-{i + 1:02d}-{name}.wav'; fo = 1.5 if i < len(scenes) - 2 else 2.5
    run(['-ss', f'{inn}', '-i', f'{MUS}/{fn}', '-t', f'{d:.3f}', '-af', f"loudnorm=I=-14.5:TP=-2:LRA=11,aresample=48000,volume='if(gt({env},0),0.24,0.52)':eval=frame,asetnsamples=480,afade=t=in:d={1.0},afade=t=out:st={d - fo:.3f}:d={fo}", '-ac', '2', '-c:a', 'pcm_s16le', f'{OUT}/{o}'])
    music.append([o, round(a, 4), round(d, 3), 2 + i % 2])
json.dump({'pieces': [[f, s / F, n / F] for f, s, n in pieces], 'narr': narr, 'dub': dub, 'music': music, 'total': TOTAL / F, 'scenes': [[n, s / F] for n, s in scenes]}, open(H + '/edl-short5.json', 'w'), indent=1)
open(H + '/edl-short5.txt', 'w').write('The Bank Robbery short, cut 5. start, length, file, what.\n\n' + ''.join(f'{s:8.3f}  {d:6.3f}  {f:34s} {n}\n' for s, d, f, n in notes) + '\nNarrator:\n' + ''.join(f'{s:8.3f}  {d:6.3f}  {f}\n' for f, s, d in narr) + '\nCharacter voices (dub):\n' + ''.join(f'{s:8.3f}  {d:6.3f}  {f}  x{tp}\n' for f, s, d, l, tp in dub) + '\nMusic:\n' + ''.join(f'{s:8.3f}  {d:6.3f}  {f}  A{tr + 1}\n' for f, s, d, tr in music))
print(len(pieces), 'pieces', len(narr), 'narrator lines', len(dub), 'voice lines', len(music), 'cues; total', round(TOTAL / F, 2), 's')
if '--preview' in sys.argv:
    lst = OUT + '/preview.txt'; open(lst, 'w').write(''.join(f"file '{OUT}/{f}'\noutpoint {n / F:.5f}\n" for f, s, n in pieces))
    ins = ['-f', 'concat', '-safe', '0', '-i', lst]; fc = '[0:a]volume=1.0[a0];'; mix = '[a0]'
    for k, (f, s, d) in enumerate(narr): ins += ['-i', nwav(f[:-4])]; fc += f'[{k + 1}:a]volume=2dB,adelay={int(s * 1000)}:all=1[n{k}];'; mix += f'[n{k}]'
    for k, (f, s, d, l, tp) in enumerate(dub): ins += ['-i', f'{OUT}/{f}']; fc += f'[{len(narr) + 1 + k}:a]volume={DUBGAIN.get(l, 4)}dB,adelay={int(s * 1000)}:all=1[d{k}];'; mix += f'[d{k}]'
    for k, (f, s, d, tr) in enumerate(music): ins += ['-i', f'{OUT}/{f}']; fc += f'[{len(narr) + len(dub) + 1 + k}:a]adelay={int(s * 1000)}:all=1[m{k}];'; mix += f'[m{k}]'
    fc += f'{mix}amix=inputs={1 + len(narr) + len(dub) + len(music)}:normalize=0:duration=first,loudnorm=I=-14:TP=-1.5:LRA=11,aresample=48000[a]'   # cut 4: to the delivery target
    run(ins + ['-filter_complex', fc, '-map', '0:v', '-map', '[a]', '-vf', f'fade=t=out:st={TOTAL / F - 1.2:.3f}:d=1.2,scale=in_range=full:out_range=limited', '-c:v', 'libx264', '-crf', '20', '-preset', 'veryfast', '-pix_fmt', 'yuv420p', '-r', '24', '-c:a', 'aac', '-b:a', '192k', ] + TAG + [OUT + '/preview-short5.mp4'])
    print('preview', dur(OUT + '/preview-short5.mp4'))
