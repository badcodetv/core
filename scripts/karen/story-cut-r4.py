#!/usr/bin/env python3
"""Karen story film, cut r4 (2026-11-24, overnight): the whole film rebuilt from beats-r4.md.

    python3 scripts/karen/story-cut-r4.py          # writes <OUT>/edl.json, <OUT>/preview.mp4

Kai, 2026-11-24: "an exciting version of Karen ... producing this like you get the story". Every stretch is built here
from clips (no v4 render tail any more, except the "To be continued" + spray-logo ending, lifted from Jack's render).
Picture is timed to the voice (block(): lines played back to back, shots share the block). The escalation is the
centrepiece: map + org-chart ladder + day counter + weather move together, each rung faster than the last.
No clip sound anywhere (Kai, 19 Nov): only narration, voices, score and the sound effects placed here on purpose.
New lines: scripts/karen/narration-r4.tsv (render-narration-r4.py, finish-voice-r4.py). New shots: scenes/story-r4-shots.
"""
import json
import pathlib
import subprocess
import sys

import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont

K = pathlib.Path('/mnt/d/badcode-videos/karen-story')
NC, OC, VIDS = K / 'new clips', K / 'old clips', K / 'vids'
N2 = K / '_outside/Karen/narration-v2/final'
N3 = K / '_outside/Karen/narration-r3'
N4 = K / '_outside/Karen/narration-r4'
R4 = K / 'clips/r4'                       # the r4 shots scene's media (stills in moodboard/, clips in video/)
END = K / 'clips/ending/final'
GPOM_LONDON = pathlib.Path('/mnt/d/badcode-videos/gitpush-origin-master/clips/bulletin-v2/cut/05-london.mp4')
SONG = K / '_outside/songs/Karen/song.wav'
RENDER = K / 'renders/karen-v4-r0.mp4'
MUS = K / 'background music'
OUT = K / 'timeline/cut-r4'
SEG = OUT / 'seg'
FPS = 24
BOLD = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
MONO = '/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf'
MUS_DB = -19.0        # score under the voice (v4's score sat ~18 dB under the files)
SEG.mkdir(parents=True, exist_ok=True)
GAP = 0.25            # between lines in a block (r3: 0.35; Kai: snappier)


def ff(*a):
    subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', *map(str, a)], check=True)


def probe(p):
    return float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', str(p)],
                                capture_output=True, text=True, check=True).stdout)


def q(t):
    return round(t * FPS) / FPS


def clip(name):
    """A new r4 shot: the clip if it has landed, else None (the cut then uses the still with a slow push)."""
    p = R4 / 'video' / name
    return p if p.exists() else None


def font(sz, mono=False):
    return ImageFont.truetype(MONO if mono else BOLD, sz)


# ---------- graphics made here ----------
RUNGS = ['CITY HALL RECEPTION', 'BOROUGH OF MANHATTAN', 'STATE OF NEW YORK', 'CONGRESS', '? ? ?']
GOLD = (255, 196, 60)


def ladder_png(level, when, name):
    """The escalation overlay: the org-chart ladder (right) with the current rung lit, and the day counter (top left)."""
    out = SEG / f'{name}.png'
    im = Image.new('RGBA', (1920, 1080), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    x0, w, h, gap, yb = 1380, 480, 74, 16, 940
    d.rounded_rectangle((x0 - 24, yb - 5 * (h + gap) - 54, x0 + w + 24, yb + h + 20), 18, fill=(10, 10, 14, 150))
    d.text((x0 + w / 2, yb - 5 * (h + gap) - 30), 'CHAIN OF COMMAND', font=font(28), fill=(230, 230, 230, 220), anchor='mm')
    for i, r in enumerate(RUNGS):
        y = yb - i * (h + gap)
        if i < level:
            fill, txt, edge = (90, 70, 30, 230), (255, 230, 170, 255), GOLD
        elif i == level:
            fill, txt, edge = (*GOLD, 255), (20, 16, 10, 255), (255, 255, 255)
        else:
            fill, txt, edge = (40, 40, 46, 200), (130, 130, 140, 255), (80, 80, 90)
        d.rounded_rectangle((x0, y, x0 + w, y + h), 10, fill=fill, outline=edge, width=3)
        d.text((x0 + w / 2, y + h / 2), r, font=font(31 if len(r) < 20 else 28), fill=txt, anchor='mm')
        if i < 4:
            d.line((x0 + w / 2, y - gap, x0 + w / 2, y), fill=(200, 200, 200, 160), width=3)
    d.text((84, 70), when, font=font(92), fill=(255, 255, 255, 255), stroke_width=6, stroke_fill=(0, 0, 0, 255))
    im.save(out)
    return out


def lower_third(text, name):
    out = SEG / f'{name}.png'
    im = Image.new('RGBA', (1920, 1080), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    f = font(46)
    tw = d.textlength(text, font=f)
    d.rectangle((70, 860, 70 + tw + 60, 940), fill=(0, 0, 0, 170))
    d.rectangle((70, 860, 82, 940), fill=(*GOLD, 255))
    d.text((112, 900), text, font=f, fill='white', anchor='lm')
    im.save(out)
    return out


def sean_boss():
    """Sean's screen from new clip 6, with the boss's words (made in r3)."""
    raw, out = SEG / 'sean-raw.png', SEG / 'sean-boss.png'
    ff('-ss', 7.6, '-i', NC / '6.mp4', '-frames:v', 1, '-vf', 'scale=1920:1080', raw)
    im = Image.open(raw).convert('RGB')
    bg = im.getpixel((300, 560))
    d = ImageDraw.Draw(im)
    d.rectangle((380, 430, 1560, 680), fill=bg)
    d.text((960, 495), 'Your role has also', font=font(88), fill=(20, 20, 20), anchor='mm')
    d.text((960, 610), 'been made redundant.', font=font(88), fill=(20, 20, 20), anchor='mm')
    im.save(out)
    return out


def sean_president(dur):
    """Sean, gold, on the studio screen (new clip 40, before its static), with the sacking typed on: a callback to
    Karen's own firing card. Text goes on in post (no legible text in a generated frame)."""
    out = SEG / 'sean-president.mp4'
    pngs = []
    for i, lines in enumerate((['MR PRESIDENT,', 'YOUR ROLE HAS BEEN', 'MADE REDUNDANT.'], ['I NOW RUN', 'THE GOVERNMENT.'])):
        im = Image.new('RGBA', (1920, 1080), (0, 0, 0, 0))
        d = ImageDraw.Draw(im)
        y = 770 if i == 0 else 905
        if i == 0:
            d.rectangle((660, 740, 1270, 1020), fill=(8, 8, 12, 235))
        for ln in lines:
            d.text((965, y), ln, font=font(46, mono=True), fill=(*GOLD, 255), anchor='mm')
            y += 54
        p = SEG / f'sean-pres-{i}.png'
        im.save(p)
        pngs.append(p)
    ff('-ss', 0, '-t', 2.7, '-i', NC / '40.mp4', '-i', pngs[0], '-i', pngs[1], '-filter_complex',
       f"[0:v]scale=1920:1080,fps={FPS},setpts=PTS*1.15,tpad=stop_mode=clone:stop_duration={dur}[b];"
       f"[b][1:v]overlay=enable='gte(t,0.5)'[c];[c][2:v]overlay=enable='gte(t,{dur * 0.55:.2f})',trim=0:{dur},setpts=PTS-STARTPTS[v]",
       '-map', '[v]', '-an', '-c:v', 'libx264', '-crf', 18, '-preset', 'veryfast', '-pix_fmt', 'yuv420p', out)
    return out


def london_sacked():
    """GitPush Origin Master's London screen shot (bulletin 05), its headline swapped (Kai: 'a little nod')."""
    out = SEG / 'london-sacked.mp4'
    if out.exists():
        return out

    def band(x):
        t = np.polyfit([650, 1000, 1337], [373, 433, 416], 2)
        b = np.polyfit([650, 1000, 1337], [418, 491, 465], 2)
        return np.polyval(t, x), np.polyval(b, x)
    text = 'PRESIDENT SACKED ON LIVE TV BY SEAN AI'
    W0, H0 = 2000, 200
    flat = Image.new('RGBA', (W0, H0), (168, 28, 48, 255))
    d = ImageDraw.Draw(flat)
    f = font(150)
    tw = d.textlength(text, font=f)
    if tw > W0 - 80:
        f = font(int(150 * (W0 - 80) / tw))
    d.text((W0 / 2, H0 / 2 + 4), text, font=f, fill=(250, 236, 232, 255), anchor='mm')
    fa = np.array(flat)
    o = np.zeros((1080, 1920, 4), np.uint8)
    for x in range(648, 1340):
        t, b = band(x)
        sx = int((x - 648) / (1340 - 648) * (W0 - 1))
        y0, y1 = int(round(t)), int(round(b))
        o[y0:y1, x, :] = fa[np.linspace(0, H0 - 1, y1 - y0).astype(int), sx, :]
    png = SEG / 'london-band.png'
    Image.fromarray(o).filter(ImageFilter.GaussianBlur(0.8)).save(png)
    ff('-i', GPOM_LONDON, '-i', png, '-filter_complex', f'[0:v]fps={FPS},setpts=PTS*1.2[b];[b][1:v]overlay[v]', '-map', '[v]',
       '-an', '-c:v', 'libx264', '-crf', 18, '-preset', 'veryfast', '-pix_fmt', 'yuv420p', out)
    return out


def meme_phone(dur):
    """The coffee girl's phone: the Karen meme (crowd at the phone box, new clip 30) over the writers' room, blurred."""
    out = SEG / 'meme-phone.mp4'
    bg = SEG / 'meme-bg.png'
    ff('-ss', 3.0, '-i', NC / '33.mp4', '-frames:v', 1, '-vf', 'scale=1920:1080,gblur=sigma=18,eq=brightness=-0.12', bg)
    sw, sh, sx, sy = 520, 920, 700, 80                 # the phone's screen
    frame = Image.new('RGBA', (1920, 1080), (0, 0, 0, 0))
    d = ImageDraw.Draw(frame)
    d.rounded_rectangle((sx - 26, sy - 40, sx + sw + 26, sy + sh + 60), 60, fill=(18, 18, 20, 255))
    d.rounded_rectangle((sx, sy, sx + sw, sy + sh), 34, fill=(0, 0, 0, 0))
    hole = Image.new('L', (1920, 1080), 0)
    ImageDraw.Draw(hole).rounded_rectangle((sx, sy, sx + sw, sy + sh), 34, fill=255)
    a = np.array(frame)
    a[..., 3] = np.where(np.array(hole) > 0, 0, a[..., 3])
    frame = Image.fromarray(a)
    d = ImageDraw.Draw(frame)
    # the app chrome and the meme's top text, drawn over the video
    d.rectangle((sx, sy, sx + sw, sy + 96), fill=(255, 255, 255, 255))
    d.ellipse((sx + 18, sy + 22, sx + 70, sy + 74), fill=(230, 60, 90, 255))
    d.text((sx + 86, sy + 34), '@nyc.unhinged', font=font(28), fill=(20, 20, 20, 255), anchor='lm')
    d.text((sx + 86, sy + 66), 'Lexington & 3rd', font=font(20), fill=(110, 110, 110, 255), anchor='lm')
    for i, ln in enumerate(["I'VE GOT ALL DAY", 'TO COMPLAIN']):
        d.text((sx + sw / 2, sy + 160 + i * 66), ln, font=font(54), fill='white', stroke_width=5, stroke_fill='black', anchor='mm')
    d.rectangle((sx, sy + sh - 120, sx + sw, sy + sh), fill=(255, 255, 255, 255))
    d.text((sx + 24, sy + sh - 84), '♥ 2.4M   ↻ 611K', font=font(32), fill=(220, 40, 70, 255), anchor='lm')
    d.text((sx + 24, sy + sh - 40), 'day 41 and she is STILL in there', font=font(22), fill=(60, 60, 60, 255), anchor='lm')
    fp = SEG / 'meme-frame.png'
    frame.save(fp)
    ff('-loop', 1, '-t', dur, '-i', bg, '-ss', 0.5, '-t', dur, '-i', NC / '30.mp4', '-i', fp, '-filter_complex',
       f"[1:v]fps={FPS},crop=ih*{sw}/{sh}:ih,scale={sw}:{sh},tpad=stop_mode=clone:stop_duration={dur}[m];"
       f"[0:v]fps={FPS},scale=1920:1080[b];[b][m]overlay={sx}:{sy}[c];[c][2:v]overlay,"
       f"zoompan=z='1+0.0009*on':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=1:s=1920x1080:fps={FPS},trim=0:{dur}[v]",
       '-map', '[v]', '-an', '-c:v', 'libx264', '-crf', 18, '-preset', 'veryfast', '-pix_fmt', 'yuv420p', out)
    return out


def still_push(png, dur, name, zoom=0.06):
    """A new shot's still (when its clip isn't made yet): a slow push in, so it plays as a shot."""
    out = SEG / f'{name}.mp4'
    n = round(dur * FPS)
    ff('-loop', 1, '-i', png, '-vf', f"scale=3840:2160,zoompan=z='1+{zoom}*on/{n}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)'"
       f":d=1:s=1920x1080:fps={FPS}", '-frames:v', n, '-c:v', 'libx264', '-crf', 18, '-preset', 'veryfast', '-pix_fmt', 'yuv420p', out)
    return out


def sfx():
    """Sound effects made here: a US phone ring, Sean's takeover drone, a static burst."""
    s = {}
    s['ring'] = SEG / 'sfx-ring.wav'
    ff('-f', 'lavfi', '-i', "aevalsrc='0.25*(sin(2*PI*440*t)+sin(2*PI*480*t))*lt(mod(t\\,3)\\,1.2)*(0.6+0.4*sin(2*PI*20*t))':s=48000:d=4.2",
       '-af', 'highpass=f=300,lowpass=f=3400,afade=t=out:st=3.9:d=0.3', '-ac', 2, s['ring'])
    s['drone'] = SEG / 'sfx-drone.wav'
    ff('-f', 'lavfi', '-i', "aevalsrc='0.35*sin(2*PI*55*t)+0.2*sin(2*PI*110.5*t)+0.12*sin(2*PI*164*t)':s=48000:d=6",
       '-f', 'lavfi', '-i', 'anoisesrc=c=brown:a=0.08:d=6:r=48000', '-filter_complex',
       '[0:a][1:a]amix=inputs=2:normalize=0,afade=t=in:d=0.4,afade=t=out:st=5.2:d=0.8[a]', '-map', '[a]', '-ac', 2, s['drone'])
    s['static'] = SEG / 'sfx-static.wav'
    ff('-f', 'lavfi', '-i', 'anoisesrc=c=white:a=0.25:d=1.2:r=48000', '-af', 'highpass=f=800,afade=t=out:st=0.9:d=0.3', '-ac', 2,
       s['static'])
    s['tick'] = SEG / 'sfx-tick.wav'       # the touch-tone blip that marks each new rung
    ff('-f', 'lavfi', '-i', "aevalsrc='0.3*(sin(2*PI*1336*t)+sin(2*PI*697*t))':s=48000:d=0.16", '-af', 'afade=t=out:st=0.12:d=0.04',
       '-ac', 2, s['tick'])
    # r4 review (listen pass: "the takeover sounds flat"): a riser into an impact, a studio-audience gasp, a siren, a splash
    s['riser'] = SEG / 'sfx-riser.wav'
    ff('-f', 'lavfi', '-i', "aevalsrc='0.35*sin(2*PI*(70*t+70*t*t))*t/2.6':s=48000:d=2.6", '-f', 'lavfi', '-i',
       'anoisesrc=c=pink:a=0.25:d=2.6:r=48000', '-filter_complex',
       "[1:a]highpass=f=1500,volume='t/2.6':eval=frame[n];[0:a][n]amix=inputs=2:normalize=0[a]", '-map', '[a]', '-ac', 2, s['riser'])
    s['impact'] = SEG / 'sfx-impact.wav'
    ff('-f', 'lavfi', '-i', "aevalsrc='0.9*sin(2*PI*42*t)*exp(-2.2*t)+0.45*sin(2*PI*84*t)*exp(-4*t)':s=48000:d=3",
       '-f', 'lavfi', '-i', 'anoisesrc=c=brown:a=0.6:d=3:r=48000', '-filter_complex',
       "[1:a]lowpass=f=900,volume='exp(-10*t)':eval=frame[n];[0:a][n]amix=inputs=2:normalize=0[a]", '-map', '[a]', '-ac', 2, s['impact'])
    s['siren'] = SEG / 'sfx-siren.wav'
    ff('-f', 'lavfi', '-i', "aevalsrc='0.3*sin(2*PI*750*t-2*PI*119.4*cos(2*PI*t/3))':s=48000:d=8", '-af',
       'lowpass=f=1800,aecho=0.8:0.6:180|340:0.4|0.25,afade=t=in:d=1.5,afade=t=out:st=5.5:d=2.5', '-ac', 2, s['siren'])
    s['splash'] = SEG / 'sfx-splash.wav'
    ff('-f', 'lavfi', '-i', 'anoisesrc=c=white:a=0.7:d=1.6:r=48000', '-af',
       "lowpass=f=2200,highpass=f=120,volume='min(1,t*40)*exp(-4.5*t)':eval=frame", '-ac', 2, s['splash'])
    s['gasp'] = SEG / 'sfx-gasp.wav'
    gs = sorted((K / '_outside/Karen/sfx-r4').glob('g-*.wav'))
    if gs:
        offs = [0.0, 0.12, 0.25, 0.07, 0.33, 0.18]
        pans = ['c0=0.9*c0|c1=0.4*c0', 'c0=0.4*c0|c1=0.9*c0', 'c0=0.7*c0|c1=0.7*c0']
        ins_, fl_ = [], []
        for i, g in enumerate(gs):
            ins_ += ['-i', g]
            fl_.append(f'[{i}:a]aresample=48000,pan=stereo|{pans[i % 3]},adelay={int(offs[i % 6] * 1000)}:all=1[g{i}]')
        ff(*ins_, '-filter_complex', ';'.join(fl_) + ';' + ''.join(f'[g{i}]' for i in range(len(gs))) +
           f'amix=inputs={len(gs)}:normalize=0,aecho=0.8:0.7:60|110:0.3|0.2,lowpass=f=6000,volume=-6dB[a]', '-map', '[a]', s['gasp'])
    return s


# ---------- the timeline ----------
video, events, beats = [], [], []
t = 0.0
cur_beat = None


def beat(bid, title):
    global cur_beat
    cur_beat = {'id': bid, 'title': title, 'start': q(t), 'lines': []}
    beats.append(cur_beat)


def add_shot(src, inp, dur, fx=None, lt=None, ov=None, still=False, speed=1.0, what=None):
    """One V1 shot at the cursor. fx = extra filter; lt = lower-third text; ov = an RGBA png laid over it;
    speed > 1 plays the source faster."""
    global t
    dur = q(dur)
    k = len(video)
    seg = SEG / f'v{k:03d}.mp4'
    vf = ['scale=1920:1080:force_original_aspect_ratio=decrease', 'pad=1920:1080:(ow-iw)/2:(oh-ih)/2', 'setsar=1']
    if speed != 1.0:
        vf.insert(0, f'setpts=PTS/{speed}')
    vf.append(f'fps={FPS}')
    hold = 0.0
    if not still and str(src).endswith('.mp4'):
        avail = (probe(src) - inp) / speed
        if avail < dur:
            hold = dur - avail + 0.05
            vf.append(f'tpad=stop_mode=clone:stop_duration={hold:.3f}')
    if fx:
        vf.append(fx)
    if lt:
        ov = lower_third(lt, f'v{k:03d}-lt')
    graph = ','.join(vf)
    if ov:
        graph = f'{graph}[b];movie={ov}[o];[b][o]overlay=0:0'
    inp_args = ['-loop', 1, '-i', src] if still else ['-ss', inp, '-t', dur * speed + 0.2, '-i', src]
    key = SEG / f'v{k:03d}.key'
    sig = repr((str(src), inp, dur, graph, speed, pathlib.Path(src).stat().st_mtime,
                pathlib.Path(ov).stat().st_mtime if ov else 0))
    if not (seg.exists() and key.exists() and key.read_text() == sig):
        ff('-threads', 4, *inp_args, '-vf', graph, '-an', '-c:v', 'libx264', '-crf', 18, '-preset', 'veryfast',
           '-threads', 4, '-pix_fmt', 'yuv420p', '-r', FPS, '-frames:v', round(dur * FPS), seg)
        # 4K sources decoded with many threads ran out of memory and truncated silently (r3, again in r4 v1): check
        got = probe(seg)
        if abs(got - dur) > 0.06:
            seg.unlink()
            sys.exit(f'{seg.name}: {got:.2f}s, wanted {dur:.2f}s ({src})')
        key.write_text(sig)
    video.append({'file': str(seg), 'source': str(src), 'start': q(t), 'dur': dur, 'beat': cur_beat['id'],
                  'track': 'V1', 'in': inp, 'looped': hold > 0.2, 'what': what or pathlib.Path(src).name})
    t += dur


def ev(src, at, stem, what=None, inp=0.0, dur=None, gain=0.0, fx=None):
    d = (probe(src) - inp) if dur is None else dur
    events.append({'stem': stem, 't': q(at), 'dur': d, 'what': what or pathlib.Path(src).name, 'src': str(src),
                   'in': inp, 'gain': gain, 'fx': fx})
    return d


def line(src, who, name, text, by, at, stem='vox-narration', fx=None, inp=0.0, dur=None):
    d = ev(src, at, stem, inp=inp, dur=dur, fx=fx)
    cur_beat['lines'].append({'i': len(cur_beat['lines']), 'who': who, 'name': name, 't': q(at), 'dur': d, 'text': text, 'by': by})
    return d


def block(lines, shots, lead=0.25, tail=0.0, min_dur=0.0, gap=GAP):
    """lines = [dict(src, who, name, text, by, stem?, fx?, inp?, dur?, pre?)] back to back; shots fill the block.
    shots = [(src, in, fixed_dur or None, kw)]; the None ones share what's left. Returns the block's start."""
    t0 = t
    c = t0 + lead
    for ln in lines:
        c += ln.pop('pre', 0.0)
        c += line(at=c, **ln) + gap
    total = max(c - gap - t0 + tail if lines else 0, min_dur)
    fixed = sum(s[2] for s in shots if s[2])
    free = [s for s in shots if not s[2]]
    each = max((total - fixed) / len(free), 0.5) if free else 0
    for src, inp, dur, kw in shots:
        add_shot(src, inp, dur or each, **kw)
    return t0


NARR = ('narrator', 'Narrator (Algenib)')


def nar(f, text, by='jack', **kw):
    base = next(b for b in (N4, N3, N2) if (b / f).exists())
    return {'src': base / f, 'who': NARR[0], 'name': NARR[1], 'text': text, 'by': by, **kw}


def vox(f, who, name, text, by='kai', **kw):
    return {'src': N4 / f, 'who': who, 'name': name, 'text': text, 'by': by, 'stem': f'vox-{who}', **kw}


S = sfx()
FB = 'hue=s=0.25,eq=brightness=0.04:contrast=0.9,gblur=sigma=1.4,vignette=PI/4'

# ===== 1. Setup: who Karen is, and the firing =====
beat('1', 'Who Karen is')
wag = clip('r4-wag-office-wag-b.mp4') or still_push(R4 / 'moodboard/office-wag-b.jpg', 5, 'wag-still')
block([nar('lvl_n01-b.wav', 'Karens have been known to plague the world with their unrelenting, entitled bullshit. This Karen is no different.')],
      [(VIDS / 'opening shot/opening shot_1.mp4', 0, 4.4, {}), (wag, 0.3, None, {'what': 'NEW r4: Karen wags her finger over a colleague'})],
      lead=1.2, tail=0.3)
block([nar('lvl_n02-b.wav', 'Starting her morning routine of polite pep talks... followed by active listening.')],
      [(OC / '1.mp4', 0.3, 3.2, {}), (OC / '2.mp4', 1.0, None, {})], lead=0.15, tail=0.45)
# the fish joke stays (Jack's), minus "Who knew", and ends before the cut (Kai)
block([nar('lvl_n03-b.wav', "[sarcastic] Turns out putting fish in the microwave is the cleaner's fault.", dur=4.6)],
      [(VIDS / 'cleaner/Cleaner.mp4', 0.0, 2.6, {}), (VIDS / 'cleaner/Cleaner.mp4', 4.3, None, {})], lead=0.6, tail=0.55)

beat('2', 'Fired by A.I. Sean')
# "Karen is told to see her boss" starts on the cut, as they're sat (Kai)
block([nar('lvl3_n04y-a.wav', 'Karen is told to see her boss. She reluctantly opens the laptop, and is immediately fired by A.I. Sean, who deems Karen and her H.R. department completely useless.')],
      [(NC / '5.mp4', 0, 2.9, {}), (NC / '6.mp4', 2.04, 5.0, {}), (NC / '6.mp4', 6.0, None, {})], lead=0.12, tail=0.3)
block([], [(NC / '43.mp4', 0.5, 2.2, {'what': '43.mp4 (stunned)'})], min_dur=2.2)
block([nar('lvl_r3a1.wav', 'Stunned, Karen hands the laptop back to her boss.', by='claude')], [(NC / '5.mp4', 5.2, None, {})], lead=0.0, tail=0.1)
block([nar('lvl_r3a2.wav', 'Ay-Eye Sean fires him too.', by='claude')],
      [(sean_boss(), 0, None, {'still': True, 'what': "Sean's screen: 'Your role has also been made redundant' (post)"})], lead=0.1, tail=0.6)
block([], [(NC / '42.mp4', 1.0, 2.4, {'what': '42.mp4 (the boss, shocked)'})], min_dur=2.4)   # silence -> straight to the bar

# ===== 2. The turn: the night =====
beat('3', 'The night: "Fuck you, Sean!"')
block([nar('lvl3_n38x-b.wav', 'Next stop: getting fucked up with Susan. A.I. Sean sacked her this morning too.'),
       nar('lvl_n39-a.wav', 'Stand clear of the closing doors, please.')], [(NC / '7.mp4', 0.958, None, {})], lead=0.1, tail=0.1)
block([nar('lvl_n40-a.wav', 'They steal wine glasses, and head out to look over the river.')], [(OC / '28.mp4', 0, None, {})], lead=0.1, tail=0.2)
shout = clip('r4-shout-river-shout-b.mp4')
shout_src = shout or still_push(R4 / 'moodboard/river-shout-b.jpg', 4, 'shout-still')
# Karen's only words in the scene, one move with the throw (Kai); take D of six (the laugh in it), picked by ear
block([vox('lvl_k401d.wav', 'karen', 'Karen (Gacrux)', 'You hear that, Sean? Fuck you, Sean!')],
      [(shout_src, 0.0, None, {'speed': 0.8, 'what': 'NEW r4: Karen at the railing, phone held high, shouting, then the throw'})], lead=0.2, tail=0.3)
block([], [(NC / '8.mp4', 0.17, 1.6, {'what': '8.mp4 (the phone falls; flicker trimmed)'}),
           (VIDS / 'seagull/seagull vid.mp4', 7.0, 1.9, {'what': 'seagull vid (the phone sinks)'})], min_dur=3.5)
ev(S['splash'], t - 2.0, 'sfx', what='splash (made here)', gain=-6)

beat('4', 'The morning, the phone box')
# phone sinking -> straight to the punchline on Karen's hangover (Kai); "Lesson learned..." is cut
block([nar('lvl_n07-a.wav', 'In these moments, even atheists pray to Christ.')], [(NC / '44.mp4', 0, None, {})], lead=0.15, tail=0.35)
block([nar('lvl_n08-a.wav', "Karen, without a phone, has no idea what's happening. She heads out to find an ancient relic."),
       nar('lvl_n09-a.wav', '[serious] A phone booth.')], [(NC / '22.mp4', 0.5, 4.2, {}), (NC / '45.mp4', 0, None, {})], lead=0.1)
block([nar('lvl_r3b.wav', 'Susan reminds her. Last night, Karen threw her phone in the river... and swore to make the biggest complaint the world has ever seen.', by='claude')],
      [(NC / '10.mp4', 0, None, {})], tail=0.1)
fb2 = (shout_src, 0.6, None, {'fx': FB, 'what': 'flashback: the railing'}) if shout else (NC / '8.mp4', 0.17, None, {'fx': FB, 'what': '8.mp4 (flashback)'})
block([{'src': N3 / 'lvl_k01fb.wav', 'who': 'karen', 'name': 'Karen (Gacrux), remembered', 'by': 'kai', 'stem': 'vox-karen',
        'text': "Tomorrow, I'm making the complaint of the century!", 'fx': 'echo'}],
      [(OC / '28.mp4', 3.0, 1.4, {'fx': FB, 'what': '28.mp4 (flashback)'}), fb2], lead=0.1, tail=0.25)
b0 = block([nar('lvl_n401.wav', 'Karen rolls her sleeves up. Somewhere in City Hall, a phone starts ringing.', by='kai')],
           [(NC / '46.mp4', 0, 3.4, {}), (VIDS / 'still on hold/still on hold.mp4', 4.6, None, {'what': 'still on hold (City Hall)'})],
           lead=0.1, tail=1.1)
ev(S['ring'], t - 2.4, 'sfx', what='phone ring (made here)', gain=-8)

# ===== 3. The escalation: map + ladder + weather, each rung faster =====
beat('5', 'The escalation: Martha')
esc0 = t
ev(S['tick'], t, 'sfx', what='touch-tone (rung 1)', gain=-10)
block([nar('lvl_n408.wav', 'Day one.', by='claude')],
      [(VIDS / 'red pin map/part 1.mp4', 2.0, None, {'speed': 1.7, 'ov': ladder_png(0, 'DAY 1', 'lad0'), 'what': "Jack's map: pin 1"})],
      lead=0.3, min_dur=3.2)
block([nar('lvl_r3d.wav', "First: Martha. She's just a receptionist.", by='claude')],
      [(NC / '13.mp4', 1.2, None, {'lt': 'MARTHA  ·  CITY HALL RECEPTION'})], lead=0.05, tail=0.05)
block([vox('lvl_k402a.wav', 'karen', 'Karen (Gacrux)', "I don't want a form. I want a human. A senior human.", by='claude')],
      [(NC / '11.mp4', 0.3, None, {})], lead=0.1, tail=0.1)
dl = clip('r4-delivery-delivery-b.mp4') or still_push(R4 / 'moodboard/delivery-b.jpg', 4, 'delivery-still')
block([nar('lvl_n402.wav', "By hour three, she's ordered lunch. Delivery address: the phone box.", by='claude')],
      [(VIDS / 'time/time.mp4', 0.0, 2.4, {'speed': 2.4, 'ov': ladder_png(0, 'HOUR 3', 'lad0b'), 'what': 'time.mp4 (the hours pass)'}),
       (dl, 0.2, None, {'what': 'NEW r4: lunch delivered to the phone box'})], lead=0.1, tail=0.3)
block([vox('lvl_m401a.wav', 'martha', 'Martha (en-us-csagent-5)', "I can escalate you, Karen... but you're going to have to wait.", fx='phone')],
      [(NC / '13.mp4', 4.0, 1.6, {}), (NC / '23.mp4', 0.5, None, {})], lead=0.1, tail=0.1)
block([vox('lvl_k403b.wav', 'karen', 'Karen (Gacrux)', "I've got all day to complain.")], [(NC / '23.mp4', 4.0, None, {})], lead=0.15, tail=0.7)

beat('6', 'The escalation: Clive, Harriet, the weather')
ev(S['tick'], t, 'sfx', what='touch-tone (rung 2)', gain=-10)
block([nar('lvl_n403.wav', 'Next day: Clive. Borough of Manhattan.', by='claude')],
      [(VIDS / 'yellow pin map/part 1.mp4', 1.0, 1.8, {'speed': 2.4, 'ov': ladder_png(1, 'DAY 2', 'lad1'), 'what': "Jack's map: pin 2"}),
       (NC / '16.mp4', 0.5, None, {'lt': 'CLIVE  ·  BOROUGH OF MANHATTAN'})], lead=0.15, tail=0.05)
nd = clip('r4-noodles-noodles-a.mp4') or still_push(R4 / 'moodboard/noodles-a.jpg', 4, 'noodles-still')
block([nar('lvl_n20-a.wav', 'She savours each syllable, inflicting psychological damage, exactly as she did at her old H.R. job.')],
      [(nd, 0.5, 3.6, {'what': 'NEW r4: night, noodles, still on the phone'}), (NC / '16.mp4', 3.5, None, {})], lead=0.05, tail=0.1)
ev(S['tick'], t, 'sfx', what='touch-tone (rung 3)', gain=-10)
block([nar('lvl_n404.wav', 'Next week: Harriet. State of New York.', by='claude')],
      [(VIDS / 'red pin map/red pin zoom map.mp4', 5.0, 1.5, {'speed': 2.4, 'ov': ladder_png(2, 'WEEK 2', 'lad2'), 'what': "Jack's map: pin 3"}),
       (OC / '21.mp4', 1.0, 1.4, {'what': 'old 21 (rain)'}),
       (NC / '20.mp4', 0.5, None, {'lt': 'HARRIET  ·  STATE OF NEW YORK'})], lead=0.1, tail=0.05)
block([nar('lvl_n405.wav', 'Next month.', by='claude'),
       nar('lvl_n17-a.wav', "[sarcastic] No one has stayed on hold this long. Guinness World Records weep at the sight of it.")],
      [(NC / '19.mp4', 0.5, 2.2, {'ov': ladder_png(2, 'MONTH 2', 'lad2b')}), (R4 / 'moodboard/asleep-a.jpg', 0, 2.4, {'still': True, 'fx': 'zoompan=z=1.08:d=1:s=1920x1080', 'what': 'NEW r4 still: snow, she is still there'}),
       (VIDS / 'still on hold/still on hold.mp4', 0.0, None, {'what': 'still on hold (rain, the box, the crowd)'})], lead=0.1, tail=0.1)
block([vox('lvl_h401c.wav', 'harriet', 'Harriet (en-us-sami)', "Karen, you can't just keep ringing like this.")],
      [(NC / '20.mp4', 4.0, None, {})], lead=0.05, tail=0.1)
# the repeat: what Aaron hears and samples (Kai)
block([vox('lvl_k404b.wav', 'karen', 'Karen (Gacrux)', "I've got ALL DAY to complain!")], [(NC / '26.mp4', 1.0, None, {})], lead=0.1, tail=0.6)
esc1 = t

# ===== 4. Viral: a ruthless edit =====
beat('7', 'Viral')
block([nar('lvl_n406.wav', 'This is Aaron. He makes music on the streets of New York. He hears it... and it has a ring to it.', by='claude')],
      [(NC / '25.mp4', 1.0, 3.6, {}), (NC / '26.mp4', 3.6, None, {})], lead=0.05, tail=0.0)
v0 = t
ev(SONG, v0, 'mus-song', what='song.wav: "Take your time, I got all day to complain. All day to complain..."', inp=74.9, dur=4.6, gain=-4)
ev(SONG, v0 + 4.6, 'mus-song', what='song.wav (under the narration)', inp=79.5, dur=7.5, gain=-17)
block([nar('lvl_n23-a.wav', "[sarcastic] It shouldn't, but it goes viral. Terrible... bloody... A.I. slop song.", pre=4.5)],
      [(OC / '12.mp4', 0, None, {'what': 'old 12 (the song online)'})], lead=0.0, tail=0.2)
block([nar('lvl_n24-a.wav', 'Now internet famous, people catch wind of her location.'), nar('lvl_n25-a.wav', 'Creepy.'),
       nar('lvl_n26-a.wav', 'Crowds start to form.', dur=1.6)],
      [(NC / '28.mp4', 0.5, 3.0, {}), (NC / '29.mp4', 0.5, 2.0, {}), (NC / '30.mp4', 0.5, None, {})], lead=0.1, gap=0.15)
block([nar('lvl_n29-a.wav', "She's made the news. Her anti-A.I. message is being repeated throughout the masses.")],
      [(NC / '38.mp4', 1.0, 2.4, {}), (NC / '31.mp4', 0.5, None, {'what': '31.mp4 (ends on the TV camera)'})], lead=0.1, tail=0.3)

# ===== 5. The writers' room =====
beat('8', "The writers' room")
block([nar('lvl_n407.wav', "These are the writers of a late-night talk show. Tonight's guest: the President. Tonight's material... nothing. Their jobs are on the line.", by='kai')],
      [(NC / '32.mp4', 0, 6.0, {}), (NC / '33.mp4', 0.5, None, {})], lead=0.05, tail=0.1)
block([vox('lvl_c401c.wav', 'coffee', 'Coffee girl (en-us-podcaster-2)', "Have you seen the Karen at the phone box? She's been complaining for weeks.")],
      [(NC / '35.mp4', 0.5, 1.4, {}), (meme_phone(5.0), 0, None, {'what': "the meme on her phone (post)"})], lead=0.05, tail=0.3)
block([vox('lvl_w401c.wav', 'writer', 'Writer (en-us-knox)', 'She wants to speak to the manager?'),
       vox('lvl_c402c.wav', 'coffee', 'Coffee girl (en-us-podcaster-2)', "There's only one manager left.", pre=0.15)],
      [(NC / '35.mp4', 2.5, None, {})], lead=0.05, tail=0.7)

# ===== 6. The call and the coup =====
beat('9', 'The call and the coup')
coup0 = t
block([nar('lvl_n33-b.wav', "The interview with the President is going well. The host asks if he'd give Karen a call... and so he continues with the puppet show.")],
      [(NC / '36.mp4', 0.5, 3.5, {}), (NC / '37.mp4', 0, 3.6, {}), (NC / '38.mp4', 0.3, None, {'what': '38.mp4 (Karen on the line)'})], lead=0.1)
block([nar('lvl2_n34-a.wav', 'They talk about the rise of A.I. He patronises her on live television, to show dominance.'),
       nar('lvl_n35-b.wav', 'Karen, completely unfazed.')], [(NC / '37.mp4', 3.6, 4.4, {}), (NC / '38.mp4', 4.0, None, {})], tail=0.2)
music_off = t
block([nar('lvl_n36-a.wav', 'The screen in the studio suddenly flashes on.'), nar('lvl3_n37y-a.wav', '[serious] It\'s A.I. Sean.')],
      [(NC / '39.mp4', 2.6, None, {})], lead=0.1, tail=0.4)
ev(S['riser'], t - 2.6, 'sfx', what='riser (made here)', gain=-8)
ev(S['impact'], t, 'sfx', what='impact (made here)', gain=-3)
ev(S['drone'], t - 0.1, 'sfx', what="Sean's takeover drone (made here)", gain=-6)
block([], [(sean_president(4.6), 0, 4.6, {'what': "Sean's screen: 'Mr President, your role has been made redundant. I now run the government.' (post)"})],
      min_dur=4.6)
ev(S['static'], t, 'sfx', what='static burst', gain=-12)
add_shot(NC / '40.mp4', 3.2, 0.6, what='40.mp4 (the screen breaks up)')
ev_ = clip('r4-evacuate-evacuate-b.mp4') or still_push(R4 / 'moodboard/evacuate-b.jpg', 6, 'evacuate-still', zoom=0.1)
ev(S['gasp'], t + 0.1, 'sfx', what='studio audience gasp (six AI Studio voices, layered here)', gain=5)
ev(S['drone'], t, 'sfx', what='drone, under the evacuation', gain=-12)
block([nar('lvl_n42-b-tight.wav', 'She complained so much, she reached the final boss. [deadpan] And the final boss just got sacked.')],
      [(ev_, 0.0, None, {'speed': 0.6, 'what': 'NEW r4: security rush him off the set'})], lead=1.3, tail=0.4)
ev(S['siren'], t, 'sfx', what='siren, far off (made here)', gain=-10)
block([], [(london_sacked(), 0, 3.4, {'what': "GitPush Origin Master's London screen, headline swapped (post)"})], min_dur=3.4)

beat('10', 'The President calls Karen')
car = clip('r4-car-car-phone2-a.mp4')
cars = sorted((R4 / 'moodboard').glob('car-phone2-*.jpg'))
car_src = car or still_push(cars[0] if cars else R4 / 'moodboard/car-phone-b.jpg', 9, 'car-still', zoom=0.08)
pres = N4 / 'lvl_p401a.wav'
block([{'src': pres, 'who': 'president', 'name': 'The President (Charon)', 'by': 'kai', 'stem': 'vox-president',
        'text': "Karen? It's the President. ...Former President. Listen. You don't give up. Right now, that's exactly what this country needs. We need to work together to beat this thing. Meet me in the Situation Room. And I'm bringing in my guy in England. He can pull a few strings."}],
      [(car_src, 0, 8.0, {'what': 'NEW r4: the man in the dark suit, in the car, on the phone'}),
       (NC / '38.mp4', 2.0, 5.2, {'what': '38.mp4 (Karen listens)'}),
       (clip('r4-car2-car-phone2-b.mp4') or car_src, 0.5, None, {'what': 'NEW r4: the car, the other side'})], lead=0.4, tail=0.5)
tq = t
add_shot(END / '10g-tarquin.mp4', 0, 13.1, what='10g-tarquin.mp4 (lip-synced; held half a second for the hang-up)')
cur_beat['lines'].append({'i': len(cur_beat['lines']), 'who': 'tarquin', 'name': 'Tarquin (Zubenelgenubi)', 't': q(tq + 0.25), 'dur': 12.625,
                          'text': "Karen! Is that you? I have an urgent message for you. For fuck's sake, listen! I have seen what happens if we do not take action! Christ, are you even there?", 'by': 'jack'})
ev(N2 / 'lvl13_t01-dub.wav', tq + 0.25, 'vox-tarquin', dur=12.35)

# the ending, lifted from Jack's v4 render: To be continued + the spray logo, with its sting
end_mov = SEG / 'end.mp4'
if not end_mov.exists():
    ff('-threads', 4, '-ss', 300.5, '-t', 10.54, '-i', RENDER, '-vf', f'scale=1920:1080,fps={FPS},setsar=1', '-threads', 4, '-an',
       '-c:v', 'libx264', '-crf', 18, '-preset', 'veryfast', '-pix_fmt', 'yuv420p', end_mov)
te = t
add_shot(end_mov, 0, probe(end_mov) - 0.05, what='To be continued + spray logo (Jack, v4 render)')
ev(NC / 'ending/sting-hold-please.wav', te + 0.75, 'sfx-hold-music', what='sting-hold-please.wav (v4)')
TOTAL = q(t)

for i, b in enumerate(beats):
    b['dur'] = q((beats[i + 1]['start'] if i + 1 < len(beats) else TOTAL) - b['start'])
    b['see'] = f"{sum(1 for v in video if v['beat'] == b['id'])} shots, {len(b['lines'])} lines."

# ---------- score: v4's cues, music out for the coup ----------
SCORE = [('1.mp3', 0.0, beats[2]['start'], 0), ('2.mp3', beats[2]['start'], esc0, 0), ('3.mp3', esc0, v0, 0),
         ('5.mp3', v0 + 7.0, music_off, 0), ('1.mp3', tq - 0.5, TOTAL - 9.0, 20.0)]
for f, a, z, inp in SCORE:
    events.append({'stem': 'mus-score', 't': q(a), 'dur': z - a, 'what': f, 'src': str(MUS / f), 'in': inp, 'gain': MUS_DB, 'fx': 'score'})

# ---------- picture ----------
lst = SEG / 'list.txt'
lst.write_text(''.join(f"file '{v['file']}'\n" for v in video))
pic = SEG / 'picture.mp4'
# re-encoded, not stream-copied: segments made by different paths (stills, post pieces) don't join cleanly by copy
# (r4 v1 played with broken NAL units)
ff('-threads', 4, '-f', 'concat', '-safe', 0, '-i', lst, '-c:v', 'libx264', '-crf', 17, '-preset', 'veryfast', '-bf', 0,
   '-pix_fmt', 'yuv420p', '-r', FPS, pic)

# ---------- sound: a silent bed first (so amix never drops the lead-in), then every event ----------
def mixdown(evs, out):
    ins, fl = ['-f', 'lavfi', '-t', f'{TOTAL:.3f}', '-i', 'anullsrc=r=48000:cl=stereo'], []
    for k, e in enumerate(evs, start=1):
        if e.get('fx') == 'score':
            ins += ['-stream_loop', '-1', '-ss', str(e['in']), '-i', e['src']]
            ln = e['dur']
            chain = (f"atrim=0:{ln + 0.6:.3f},aresample=48000,aformat=channel_layouts=stereo,volume={e['gain']}dB,"
                     f"afade=t=in:d=0.4,afade=t=out:st={max(ln - 0.5, 0):.3f}:d=1.1")
        else:
            ins += ['-ss', str(e['in']), '-t', f"{e['dur']:.3f}", '-i', e['src']]
            extra = {'echo': ',aecho=0.8:0.6:120|240:0.35|0.2', 'phone': ',highpass=f=320,lowpass=f=3300,volume=1.5dB'}.get(e.get('fx') or '', '')
            fade = f",afade=t=in:d=0.4,afade=t=out:st={max(e['dur'] - 0.8, 0):.3f}:d=0.8" if e['stem'] == 'mus-song' else ''
            chain = f"aresample=48000,aformat=channel_layouts=stereo{extra},volume={e.get('gain', 0)}dB{fade}"
        fl.append(f"[{k}:a]{chain},adelay={int(e['t'] * 1000)}:all=1[a{k}]")
    n = len(fl)
    mix = ';'.join(fl) + ';[0:a]' + ''.join(f'[a{i}]' for i in range(1, n + 1)) + \
        f'amix=inputs={n + 1}:normalize=0:dropout_transition=0,atrim=0:{TOTAL:.3f}[m]'
    ff(*ins, '-filter_complex', mix, '-map', '[m]', '-ar', 48000, '-ac', 2, out)


snd = SEG / 'sound.wav'
mixdown(events, snd)
# one file per stem (gain and filters baked in), for the Premiere build (scripts/scene/premiere-plan.py)
STEM_FILES = {}
for st in sorted({e['stem'] for e in events}):
    STEM_FILES[st] = OUT / 'stems' / f'{st}.wav'
    STEM_FILES[st].parent.mkdir(exist_ok=True)
    mixdown([e for e in events if e['stem'] == st], STEM_FILES[st])

preview = OUT / 'preview.mp4'
ff('-i', pic, '-i', snd, '-map', '0:v', '-map', '1:a', '-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k', '-movflags', '+faststart', '-shortest', preview)

# ---------- the edl ----------
order = ['vox-narration', 'vox-karen', 'vox-martha', 'vox-harriet', 'vox-coffee', 'vox-writer', 'vox-president', 'vox-tarquin',
         'mus-score', 'mus-song', 'sfx', 'sfx-hold-music']
stems = [s for s in order if any(e['stem'] == s for e in events)]
edl = {
    'sequence': 'karen-1-story-r4', 'title': 'Karen Story Timeline', 'fps': FPS, 'total': round(TOTAL, 3),
    'heading': 'Karen Story: the narrated film (cut r4, from beats-r4)',
    'intro': ("Cut r4 (2026-11-24, made overnight): the whole film rebuilt from the r4 beat sheet. New Flow shots, new voices, "
              "the escalation as map + chain-of-command ladder + day counter + weather, a ruthless viral edit, the writers' room, "
              "the coup, and the President calling Karen."),
    'beats': beats, 'video': video,
    'audio': [{'track': f'A{i + 1}', 'name': s, 'file': str(STEM_FILES[s])} for i, s in enumerate(stems)],
    'events': [{k: v for k, v in e.items() if k in ('stem', 't', 'dur', 'what', 'src', 'in')} for e in events],
    'flags': ['No clip sound anywhere: narration, voices, score, the song and the sound effects placed here.',
              'Lines marked by=claude are drafts (Kai and Jack overrule freely); joke picks are Kai\'s first-suggestion picks.'],
    'render': str(preview),
}
(OUT / 'edl.json').write_text(json.dumps(edl, indent=1))
print(json.dumps({'total': TOTAL, 'shots': len(video), 'escalation': [round(esc0, 2), round(esc1, 2)],
                  'beats': [(b['id'], b['title'], round(b['start'], 2)) for b in beats]}))
