#!/usr/bin/env python3
"""The Bank Robbery SHORT, cut 2 (2026-10-15 evening): cut 1 with the 15 October meeting's changes (short.md, "Cut 2").

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
OUT, V, IMG, NAR, MUS, C10 = P + '/clips/short2', P + '/vids/short', P + '/images/short', P + '/narrator/short', P + '/music/lofi', P + '/clips/cut10'
NAR2, VOX, C9, C5 = P + '/narrator/short2', P + '/voices/short2', P + '/clips/cut9', P + '/clips/cut5'
F = 24
fr = lambda t: int(round(t * F))
os.makedirs(OUT, exist_ok=True)
def run(a):
    r = subprocess.run(['ffmpeg', '-v', 'error', '-y'] + a, capture_output=True, text=True)
    if r.returncode: sys.exit('ffmpeg failed: ' + r.stderr[-1200:])
def dur(p): return float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', p], capture_output=True, text=True).stdout)
ENC = ['-c:v', 'libx264', '-crf', '14', '-preset', 'medium', '-pix_fmt', 'yuv420p', '-r', '24', '-c:a', 'pcm_s16le', '-ar', '48000', '-ac', '2']
FIT = 'scale=1280:720:force_original_aspect_ratio=increase,crop=1280:720,setsar=1,fps=24'

# ---- word times of every talk clip, cached (the whisper venv is the one the cut 8 transcript used)
WCACHE = H + '/words-short.json'
WORDS = json.load(open(WCACHE)) if os.path.exists(WCACHE) else {}
def words(clip):
    if clip not in WORDS:
        code = ("import sys,json,subprocess,numpy as np\nfrom faster_whisper import WhisperModel\n"
                "a=np.frombuffer(subprocess.run(['ffmpeg','-loglevel','error','-i',sys.argv[1],'-ac','1','-ar','16000','-f','f32le','-'],capture_output=True).stdout,np.float32)\n"
                "m=WhisperModel('small.en',device='cpu',compute_type='int8')\nsegs,_=m.transcribe(a,word_timestamps=True)\n"
                "print(json.dumps([[w.start,w.end,w.word.strip()] for s in segs for w in s.words]))")
        r = subprocess.run([os.path.expanduser('~/.cache/badcode-whisper/venv/bin/python'), '-c', code, f'{V}/{clip}.mp4'], capture_output=True, text=True)
        WORDS[clip] = json.loads(r.stdout.strip().splitlines()[-1]); json.dump(WORDS, open(WCACHE, 'w'), indent=1)
    return WORDS[clip]

pieces, narr, notes, speech, scenes, dub = [], [], [], [], [], []
t = 0  # frames
def add(f, n, label, talk=False):
    global t
    pieces.append([f, t, n]); notes.append((t / F, n / F, f, label))
    if talk: speech.append((t / F, (t + n) / F))
    t += n
def cut(src, a, d, name, vf='', af=''):
    """a range of a source file as its own piece, d seconds long"""
    o = f'{OUT}/{name}.mov'
    if not (os.path.exists(o) and os.path.getsize(o) > 0):
        v = FIT + (',' + vf if vf else '')
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
def over(line, shots, off=0.15, tail=0.3, label=''):
    """narrator line over one or more silent shots: [(clip, start_in_clip, weight)], shared out by weight"""
    nd = dur(nwav(line)); need = off + nd + tail; tw = sum(s[2] for s in shots)
    narr.append([line + '.wav', round(t / F + off, 4), round(nd, 3)]); speech.append((t / F + off, t / F + off + nd))
    for clip, a, wgt in shots:
        d = need * wgt / tw
        if clip.startswith('c10-'): f, n = cut(f'{C10}/{clip}.mov', a, d, f's-{len(pieces):03d}-{clip}', af='volume=-6dB')
        elif clip.startswith('/'): f, n = cut(clip, a, d, f's-{len(pieces):03d}-' + os.path.basename(clip)[:-4], af='volume=-6dB')
        elif clip.endswith('.mov'): f, n = clip, fr(d)
        else: f, n = cut(f'{V}/{clip}.mp4', a, d, f's-{len(pieces):03d}-{clip}', af='volume=-8dB')
        add(f, n, label or line)
def silent(clip, a, d, label, vf='', gain='volume=-4dB'):
    src = f'{C10}/{clip}.mov' if clip.startswith('c10-') else f'{V}/{clip}.mp4'
    f, n = cut(src, a, d, f's-{len(pieces):03d}-{clip}', vf=vf, af=gain); add(f, n, label)

# ---- made piece 1: Dunkirk with grain (cut 2: the hand-held jolt is gone, Kai's 'camera jitter'), pushing in on the soldier's face in its last second
FACE = (0.468, 0.31)          # the shouting soldier, as a fraction of the frame (d01 and d02 share the composition)
PAINT = (0.127, 0.0, 0.507, 0.48)  # the painting's box in c01-cafe-wide (x0, y0, x1, y1), read off the still
def zoomcrop(z0, z1, T, cx, cy):
    """scale up per frame from zoom z0 to z1 over T seconds (eased), then a fixed 1280x720 crop centred on (cx, cy), clamped"""
    z = f'({z0}+({z1}-{z0})*(1-cos(PI*min(t/{T},1)))/2)'
    return (f"scale=w='trunc(1280*{z}/2)*2':h='trunc(720*{z}/2)*2':eval=frame,"
            f"crop=1280:720:x='max(0,min(iw-1280,{cx}*iw-640))':y='max(0,min(ih-720,{cy}*ih-360))',setsar=1")
def reveal():
    o = f'{OUT}/s-reveal.mov'
    if not (os.path.exists(o) and os.path.getsize(o) > 0):
        d01, c01 = f'{V}/d01-dunkirk.mp4', f'{V}/c01-cafe-wide.mp4'
        war = "eq=saturation=0.75:contrast=1.08,noise=alls=16:allf=t,crop=iw*0.94:ih*0.94,scale=1280:720,setsar=1"
        pcx, pcy, pw = (PAINT[0] + PAINT[2]) / 2, (PAINT[1] + PAINT[3]) / 2, PAINT[2] - PAINT[0]
        # 0-3.6 battle, 3.6-4.6 push in on the face; dissolve 0.35 into the painting at the same zoom; painting pulls back 1.4 s;
        # dissolve 0.35 into the cafe clip cropped to the painting, which pulls back to the full room over 2.2 s
        fc = (f"[0:v]{FIT},trim=0.3:4.9,setpts=PTS-STARTPTS,{war}[w0];"
              f"[w0]split[wa][wb];[wa]trim=0:3.6,setpts=PTS-STARTPTS[w1];[wb]trim=3.6:4.6,setpts=PTS-STARTPTS,{zoomcrop(1, 1.9, 1.0, *FACE)}[w2];"
              f"[w1][w2]concat=n=2:v=1,fps=24,settb=1/24[war];"
              f"[1:v]scale=1280:720,setsar=1,loop=loop=-1:size=1:start=0,fps=24,trim=0:2.0,setpts=PTS-STARTPTS,{zoomcrop(1.9, 1.0, 1.4, *FACE)},fps=24,settb=1/24[pt];"
              f"[2:v]{FIT},trim=0:4.5,setpts=PTS-STARTPTS,{zoomcrop(round(1 / pw, 3), 1.0, 2.2, pcx, pcy)},fps=24,settb=1/24[cafe];"
              f"[war][pt]xfade=transition=fade:duration=0.35:offset=4.25[a1];[a1][cafe]xfade=transition=fade:duration=0.35:offset=5.9[v];"
              # sound: the battle, cut dead to cafe clatter on the painting
              f"[0:a]atrim=0.3:4.6,asetpts=PTS-STARTPTS,volume=2dB,afade=t=out:st=4.0:d=0.3[ba];[2:a]atrim=0:6.1,asetpts=PTS-STARTPTS,volume=-6dB,adelay=4300:all=1[ca];"
              f"[ba][ca]amix=inputs=2:normalize=0:duration=longest,apad,atrim=0:10.4[a]")
        run(['-i', d01, '-i', f'{IMG}/d02-painting.jpg', '-i', c01, '-filter_complex', fc, '-map', '[v]', '-map', '[a]', '-t', '10.4'] + ENC + [o])
    return 's-reveal.mov', fr(10.4)

# ---- cut 2: the character voices (brs-voices.json), the take per line picked on a faster-whisper check
# (words-short2-tts.json): word-perfect first, then the take whose length is nearest the clip's own speech
PICK = {'v04-barry': 2, 'v05-denise': 2, 'v06-barry': 2, 'v07-denise': 2, 'v08-barry': 2, 'v09-denise': 1, 'v10-barry': 1,
        'v13-ex': 1, 'v14-red': 2, 'v17-red-chant': 1, 'v18-blue': 2, 'v24-barry': 2, 'v25-denise': 1}
TTSW = json.load(open(H + '/words-short2-tts.json'))
MEGA = 'highpass=f=450,lowpass=f=3400,acompressor=threshold=0.1:ratio=6:attack=2:release=60,volume=4dB,aecho=0.8:0.5:45:0.18'
def tts(line):
    p = f'{VOX}/take{PICK[line]}/{line}.wav'; w = TTSW[p]; return p, w[0][0], w[-1][1]
def dubline(line, at, span, fx=''):
    """write the line stretched toward span seconds (0.8-1.25x) and lay it at `at` seconds on the dub track"""
    p, t0, t1 = tts(line); d = t1 - t0; tempo = max(0.8, min(1.25, d / span)); nd = d / tempo
    o = f'dub-{line}.wav'
    run(['-ss', f'{max(0, t0 - 0.03):.3f}', '-t', f'{min(dur(p) - max(0, t0 - 0.03), d + 0.4):.3f}', '-i', p, '-af', f'atempo={tempo:.4f}' + (',' + fx if fx else '') + ',areverse,silenceremove=start_periods=1:start_threshold=-45dB,areverse,aresample=48000', '-ac', '2', '-c:a', 'pcm_s16le', f'{OUT}/{o}'])
    dub.append([o, round(at, 4), round(nd, 3), line, round(tempo, 3)]); speech.append((at, at + nd)); return nd
def dubtalk(clip, line, label, lead=0.15, tail=0.35, upto=None, fx=''):
    """cut 1's picture of a talk clip, muted, one continuous range round the mouth's words; the TTS line laid where
    the mouth moves. If the stretched line runs past the words the range is lengthened, holding the last frame if
    the clip runs out."""
    w = [list(x) for x in words(clip)]
    if upto: w = w[:next(i for i, x in enumerate(w) if x[2].lower().startswith(upto)) + 1]
    if w[0][1] - w[0][0] > 0.8: w[0][0] = w[0][1] - 0.8
    s0, s1 = w[0][0], w[-1][1]; end = dur(f'{V}/{clip}.mp4')
    p, t0, t1 = tts(line); nd = (t1 - t0) / max(0.8, min(1.25, (t1 - t0) / (s1 - s0)))
    a = max(0.0, s0 - lead); b = max(s1, s0 + nd) + tail; hold = max(0.0, b - end)
    f, n = cut(f'{V}/{clip}.mp4', a, b - a, f's-{len(pieces):03d}-{clip}', vf=f'tpad=stop_mode=clone:stop_duration={hold + 0.1:.2f}' if hold > 0 else '', af='volume=0')
    dubline(line, t / F + (s0 - a), s1 - s0, fx); add(f, n, f'{label} (dub {line})', talk=True)
def dubwhole(src, line, label, at=0.25, span=None, fx=''):
    """a whole cut 10 piece, muted, with the line laid over it"""
    d = dur(src); f, n = cut(src, 0.0, d, f's-{len(pieces):03d}-' + os.path.basename(src)[:-4], af='volume=0')
    dubline(line, t / F + at, span or d - at - 0.3, fx); add(f, n, f'{label} (dub {line})', talk=True)

# ---- made piece: the archive opening (Kai: real WW2 footage, more weight before the modern scenes)
ARCH = [('ww2-04-dunkirk-tommies-grinning', 0.0, 2.5), ('ww2-02-pilots-scramble', 0.0, 2.5), ('ww2-03-home-guard-marching', 0.0, 2.5), ('ww2-06-st-pauls-floodlit-ve-night', 0.0, 2.5)]
def archive():
    o = f'{OUT}/s-archive.mov'
    if not (os.path.exists(o) and os.path.getsize(o) > 0):
        ins, fc = [], ''
        for k, (c, a, d) in enumerate(ARCH): ins += ['-ss', str(a), '-t', str(d), '-i', f'{C5}/{c}.mp4']; fc += f'[{k}:v]{FIT},format=yuv420p,setpts=PTS-STARTPTS[v{k}];'
        T = sum(x[2] for x in ARCH)
        fc += ''.join(f'[v{k}]' for k in range(len(ARCH))) + f'concat=n={len(ARCH)}:v=1,noise=alls=10:allf=t,fade=t=in:d=0.5[v];'
        fc += f'anoisesrc=color=brown:amplitude=0.02:d={T},highpass=f=60,lowpass=f=1800,afade=t=in:d=0.6,afade=t=out:st={T - 0.4}:d=0.4,aformat=channel_layouts=stereo[a]'
        run(ins + ['-filter_complex', fc, '-map', '[v]', '-map', '[a]', '-t', str(T)] + ENC + [o])
    return 's-archive.mov', fr(sum(x[2] for x in ARCH))

# ---- made piece: the deposit reveal, lingering on the press still (no new pictures: Jack, "dont change the videos")
def stillpush(img, d, name, z1=1.3, cx=0.5, cy=0.55):
    o = f'{OUT}/{name}.mov'
    if not (os.path.exists(o) and os.path.getsize(o) > 0):
        run(['-loop', '1', '-i', f'{IMG}/{img}.jpg', '-f', 'lavfi', '-i', f'anullsrc=r=48000:cl=stereo', '-filter_complex',
             f'[0:v]scale=1280:720,setsar=1,fps=24,trim=0:{d:.3f},setpts=PTS-STARTPTS,{zoomcrop(1.0, z1, d, cx, cy)},noise=alls=6:allf=t[v]', '-map', '[v]', '-map', '1:a', '-t', f'{d:.3f}'] + ENC + [o])
    return name + '.mov', fr(d)

# ---- made piece: the estate agent's window as a fruit machine (the meeting: "slot machine" prices doubling)
PRICES = ['£180,000', '£210,000', '£195,000', '£240,000', '£165,000', '£225,000']
STRIPS = [(348, 348), (643, 348), (938, 348), (348, 533), (643, 533), (938, 533)]   # centres of the white margins under each card, read off e01-estate at 1280x720
def slot(d=3.8):
    """0-0.5 s the old prices; then every card rolls (a new random price every 1/12 s, scrolling down), the reels stop
    one after another from 1.3 s, each on double its old price, a tick and a ding as each lands, a jackpot bell at the end"""
    o = f'{OUT}/s-slot.mov'
    if not (os.path.exists(o) and os.path.getsize(o) > 0):
        import random; random.seed(7)
        font = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'; dt = []; R0, TK = 0.5, 1 / 12
        stops = [1.3 + 0.3 * k for k in range(6)]
        for k, ((x, y), p) in enumerate(zip(STRIPS, PRICES)):
            dbl = '£{:,}'.format(2 * int(p[1:].replace(',', '')))
            dt.append(f"drawtext=fontfile={font}:text='{p.replace(',', chr(92) + ',')}':fontsize=28:fontcolor=0x111111:x={x}-tw/2:y={y}-th/2:enable='lt(t,{R0})'")
            tk = R0
            while tk < stops[k] - 1e-6:
                r = '£{:,}'.format(random.randrange(120, 499) * 1000).replace(',', chr(92) + ',')
                dt.append(f"drawtext=fontfile={font}:text='{r}':fontsize=28:fontcolor=0x333333:x={x}-tw/2:y={y}-th/2+(t-{tk:.4f})*288-12:enable='between(t,{tk:.4f},{tk + TK:.4f})'")
                tk += TK
            dt.append(f"drawtext=fontfile={font}:text='{dbl.replace(',', chr(92) + ',')}':fontsize=28:fontcolor=0x111111:x={x}-tw/2:y={y}-th/2:enable='gte(t,{stops[k]})'")
        J = stops[-1] + 0.12
        vf = ','.join(dt) + f",eq=brightness='if(between(t,{J},{J + 0.1}),0.3,0)':eval=frame"
        clicks = '+'.join(f"0.35*between(t,{R0},{s})*sin(2*PI*2400*t)*exp(-mod(t,{TK:.5f})*260)" for s in stops)
        dings = '+'.join(f"0.25*gte(t,{s})*sin(2*PI*1760*t)*exp(-(t-{s})*14)" for s in stops)
        bell = f"gte(t,{J})*0.3*(sin(2*PI*1318.5*t)+sin(2*PI*1568*t)+sin(2*PI*2093*t))*exp(-(t-{J})*3)"
        run(['-ss', '0.5', '-i', f'{V}/e01-estate.mp4', '-f', 'lavfi', '-i', f"aevalsrc=exprs='({clicks}+{dings}+{bell})/3':s=48000:d={d}", '-t', f'{d:.3f}',
             '-filter_complex', f'[0:v]{FIT},{vf}[v];[1:a]aformat=channel_layouts=stereo,volume=-4dB[a]', '-map', '[v]', '-map', '[a]'] + ENC + [o])
    return 's-slot.mov', fr(d)

# ---- the plan, in script order (short.md, "Cut 2")
def build():
    scenes.append(['cafe', t])
    f, n = archive(); A = n / F; add(f, n, 'A1: the archive (Dunkirk deck, the scramble, the Home Guard, St Paul\'s)')
    narr.append(['na1-grandparents.wav', 1.0, round(dur(nwav('na1-grandparents')), 3)]); speech.append((1.0, 1.0 + narr[-1][2]))
    f, n = reveal(); add(f, n, 'Dunkirk, push in, the painting, pull out to the cafe (no jolt)')
    n2 = A + 3.45; narr.append(['ns02-beach.wav', n2, round(dur(f'{NAR}/ns02-beach.wav'), 3)]); speech.append((n2, n2 + dur(f'{NAR}/ns02-beach.wav')))
    narr.append(['ns03-one-bed.wav', round(n2 + dur(f'{NAR}/ns02-beach.wav') + 0.2, 3), round(dur(f'{NAR}/ns03-one-bed.wav'), 3)])
    speech.append((narr[-1][1], narr[-1][1] + narr[-1][2]))
    dubtalk('c02a-barry', 'v04-barry', 'Barry'); dubtalk('c03a-denise', 'v05-denise', 'Denise'); dubtalk('c02b-barry', 'v06-barry', 'Barry')
    dubtalk('c03b-denise', 'v07-denise', 'Denise'); dubtalk('c02c-barry', 'v08-barry', 'Barry'); dubtalk('c03c-denise', 'v09-denise', 'Denise')
    dubtalk('c04-fredo10', 'v10-barry', 'Barry, the Fredo at 10p')
    over('ns11-both-right', [('c05-window-bank', 0.5, 1)])
    scenes.append(['plan', t])
    over('ns12-masks', [('p01-press', 0.5, 1)])
    dubtalk('p02a-ex', 'v13-ex', 'The Ex'); dubtalk('p03-red', 'v14-red', 'Mr Red')
    nd = dur(nwav('nr1-paying-in')); d = 0.3 + nd + 1.8   # Kai: let the reveal land and breathe before the protest
    narr.append(['nr1-paying-in.wav', round(t / F + 0.3, 4), round(nd, 3)]); speech.append((t / F + 0.3, t / F + 0.3 + nd))
    f, n = stillpush('p01-press', d, 's-r1-press'); add(f, n, 'R1: the deposit reveal, held on the press')
    scenes.append(['march', t])
    over('np1-shout', [(f'{C9}/c9-paper-blue.mov', 0.0, 1), (f'{C9}/c9-paper-red.mov', 0.0, 1)], tail=2.4, label='P1: the newspaper drops (cut 9 front pages)')
    silent('r01-barry-sign', 0.4, 1.4, 'Barry with the sign', gain='volume=-12dB'); silent('r01b-woman-sign', 0.4, 1.0, 'the woman with the same sign', gain='volume=-12dB')
    dubtalk('r02-red-megaphone', 'v17-red-chant', 'Mr Red, the chant', lead=0.1, tail=0.25, fx=MEGA)
    dubwhole(f'{C10}/c10-049-04784.mov', 'v18-blue', 'whose fault it is (cut 10)', fx=MEGA)
    over('ns19-first-line', [('r04-denise-window', 0.5, 1)])
    over('ns1-side-door', [('c05-window-bank', 3.0, 1)], tail=0.5, label='S1: the side door, over the bank across the road')
    scenes.append(['bank', t])
    over('ns23-just-early', [('e02-donor-keys', 0.4, 1)], label='the Donor and the keys')
    f, n = slot(); add(f, n, 'the window as a fruit machine, prices double')
    dubtalk('f02-fredo20', 'v24-barry', 'Barry, the Fredo at 20p'); dubtalk('c03d-denise', 'v25-denise', 'Denise', upto='landlord')
    over('ns26-no-law', [('c01-cafe-wide', 3.0, 1)], off=0.2, tail=0.5)
    scenes.append(['ending', t])
    silent('s01-sink', 1.0, 3.5, 'Denise at the sink, the letter')
    silent('c10-081-08349', 0.5, 4.0, 'the badcode kebab shop (cut 10)')
build()
TOTAL = t

# ---- music: one lofi cue per scene, ducked under every line (same recipe as cut 10)
CUES = {'cafe': ('01-cafe-holiznacc0-busking-in-the-sunlight.mp3', 10.2), 'plan': ('02-plan-holiznacc0-busted-jazz.mp3', 10.0),
        'march': ('04-march-holiznacc0-never-sleeping.mp3', 11.0), 'bank': ('05-bank-holiznacc0-cellar-door.mp3', 11.0),
        'ending': ('06-ending-holiznacc0-all-the-way-sad.mp3', 0.0)}
ARCHT = sum(x[2] for x in ARCH)
scenes.append(['end', TOTAL]); music = []
for i, (name, s0) in enumerate(scenes[:-1]):
    s1 = scenes[i + 1][1]; fn, inn = CUES[name]; a = max(0.0, s0 / F - (0.0 if i == 0 else 0.6)); b = s1 / F + (0.8 if i < len(scenes) - 2 else 0.0); d = b - a
    if name == 'cafe': a, d = a + ARCHT + 4.3, d - ARCHT - 4.3   # no music under the archive or the battle
    env = '+'.join(f'between(t,{max(0, x - a - 0.25):.2f},{y - a + 0.35:.2f})' for x, y in speech if y > a and x < b) or '0'
    o = f'ms-{i + 1:02d}-{name}.wav'; fo = 0.8 if i < len(scenes) - 2 else 2.5
    run(['-ss', f'{inn}', '-i', f'{MUS}/{fn}', '-t', f'{d:.3f}', '-af', f"loudnorm=I=-14.5:TP=-2:LRA=11,aresample=48000,volume='if(gt({env},0),0.24,0.52)':eval=frame,asetnsamples=480,afade=t=in:d={0.6},afade=t=out:st={d - fo:.3f}:d={fo}", '-ac', '2', '-c:a', 'pcm_s16le', f'{OUT}/{o}'])
    music.append([o, round(a, 4), round(d, 3), 2 + i % 2])
json.dump({'pieces': [[f, s / F, n / F] for f, s, n in pieces], 'narr': narr, 'dub': dub, 'music': music, 'total': TOTAL / F, 'scenes': [[n, s / F] for n, s in scenes]}, open(H + '/edl-short2.json', 'w'), indent=1)
open(H + '/edl-short2.txt', 'w').write('The Bank Robbery short, cut 2. start, length, file, what.\n\n' + ''.join(f'{s:8.3f}  {d:6.3f}  {f:34s} {n}\n' for s, d, f, n in notes) + '\nNarrator:\n' + ''.join(f'{s:8.3f}  {d:6.3f}  {f}\n' for f, s, d in narr) + '\nCharacter voices (dub):\n' + ''.join(f'{s:8.3f}  {d:6.3f}  {f}  x{tp}\n' for f, s, d, l, tp in dub) + '\nMusic:\n' + ''.join(f'{s:8.3f}  {d:6.3f}  {f}  A{tr + 1}\n' for f, s, d, tr in music))
print(len(pieces), 'pieces', len(narr), 'narrator lines', len(dub), 'voice lines', len(music), 'cues; total', round(TOTAL / F, 2), 's')
if '--preview' in sys.argv:
    lst = OUT + '/preview.txt'; open(lst, 'w').write(''.join(f"file '{OUT}/{f}'\noutpoint {n / F:.5f}\n" for f, s, n in pieces))
    ins = ['-f', 'concat', '-safe', '0', '-i', lst]; fc = '[0:a]volume=1.0[a0];'; mix = '[a0]'
    for k, (f, s, d) in enumerate(narr): ins += ['-i', nwav(f[:-4])]; fc += f'[{k + 1}:a]volume=2dB,adelay={int(s * 1000)}:all=1[n{k}];'; mix += f'[n{k}]'
    for k, (f, s, d, l, tp) in enumerate(dub): ins += ['-i', f'{OUT}/{f}']; fc += f'[{len(narr) + 1 + k}:a]volume=2dB,adelay={int(s * 1000)}:all=1[d{k}];'; mix += f'[d{k}]'
    for k, (f, s, d, tr) in enumerate(music): ins += ['-i', f'{OUT}/{f}']; fc += f'[{len(narr) + len(dub) + 1 + k}:a]adelay={int(s * 1000)}:all=1[m{k}];'; mix += f'[m{k}]'
    fc += f'{mix}amix=inputs={1 + len(narr) + len(dub) + len(music)}:normalize=0:duration=first,alimiter=limit=0.9:level=disabled[a]'
    run(ins + ['-filter_complex', fc, '-map', '0:v', '-map', '[a]', '-c:v', 'libx264', '-crf', '20', '-preset', 'veryfast', '-pix_fmt', 'yuv420p', '-r', '24', '-c:a', 'aac', '-b:a', '192k', OUT + '/preview-short2.mp4'])
    print('preview', dur(OUT + '/preview-short2.mp4'))
