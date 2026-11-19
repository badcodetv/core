#!/usr/bin/env python3
"""Karen story film, cut r3 (2026-11-18): Kai's notes up to 2:08 put into one attempted cut, to be noted on the page.

    python3 scripts/karen/story-cut-r3.py            # writes <OUT>/edl.json, <OUT>/preview.mp4

Kai, 2026-11-18: "absorb everything we've said and get it incorporated into a timeline, however wrong that might be".
The head (office -> calling everyone -> the seasons) is re-assembled here from the clips; the tail (Viral onward) is
Jack's Karen v4 render from 176.917 s, unchanged, so his effects stay. Picture is timed to the voice (lead 0.35 s,
gaps 0.35 s). New lines: scripts/karen/narration-r3.tsv (render-narration-r3.sh), levelled to -18 LUFS like v2.
Shots that don't exist yet are placeholder cards over a dimmed nearby frame.
"""
import json
import pathlib
import subprocess
import sys

from PIL import Image, ImageDraw, ImageFont

K = pathlib.Path('/mnt/d/badcode-videos/karen-story')
NC, OC = K / 'new clips', K / 'old clips'
N2 = K / '_outside/Karen/narration-v2/final'
N3 = K / '_outside/Karen/narration-r3'
# r3b (Kai, 19 Nov): "we're hearing the audio track from the videos ... We should only be hearing the music and the
# narration and sound effects we've explicitly put in the timeline." So: no clip sound anywhere, and the tail (Viral on)
# gets its sound rebuilt from v4's own events (narration, score, hold music) instead of the render's mix, which has
# Jack's A1 clip sound baked in. Same picture as r3, so notes pinned to r3's frames still line up.
NO_CLIP = '--no-clip-sound' in sys.argv
TAIL_DB = -4.0  # measured: the rebuilt tail ran -14.0 LUFS against the v4 render's -18.0 (Jack's mix sat lower)
OUT = K / ('timeline/cut-r3b' if NO_CLIP else 'timeline/cut-r3')
SEG = OUT / 'seg'
V4 = json.loads((K / 'timeline/cut-v4/edl.json').read_text())
RENDER = K / 'renders/karen-v4-r0.mp4'
TAIL_FROM = 176.917   # v4 beat 7 "Viral" starts here
FPS = 24
BOLD = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
MUS = K / 'background music'
MUS_DB = -18.0        # measured: v4's score sits ~18 dB under the files
CLIP_DB = -24.0

SEG.mkdir(parents=True, exist_ok=True)


def ff(*a):
    subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', *map(str, a)], check=True)


def probe(p):
    return float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', str(p)],
                                capture_output=True, text=True, check=True).stdout)


def q(t):
    return round(t * FPS) / FPS


# ---------- generated stills ----------
def card(bg_clip, at, text, name):
    """A placeholder for a shot not made yet: a nearby frame, dimmed, with what the shot should be."""
    raw, out = SEG / f'{name}-bg.png', SEG / f'{name}.png'
    ff('-ss', at, '-i', bg_clip, '-frames:v', 1, '-vf', 'scale=1920:1080', raw)
    im = Image.open(raw).convert('RGB').point(lambda v: int(v * 0.35))
    d = ImageDraw.Draw(im)
    d.text((960, 430), 'NEW SHOT TO MAKE', font=ImageFont.truetype(BOLD, 44), fill=(255, 200, 60), anchor='mm')
    y = 520
    for ln in text:
        d.text((960, y), ln, font=ImageFont.truetype(BOLD, 56), fill='white', anchor='mm')
        y += 74
    im.save(out)
    return out


def sean_boss():
    """Sean's screen from new clip 6, with the boss's words instead of Karen's (UI text goes on in post)."""
    raw, out = SEG / 'sean-raw.png', SEG / 'sean-boss.png'
    ff('-ss', 7.6, '-i', NC / '6.mp4', '-frames:v', 1, '-vf', 'scale=1920:1080', raw)
    im = Image.open(raw).convert('RGB')
    bg = im.getpixel((300, 560))
    d = ImageDraw.Draw(im)
    d.rectangle((380, 430, 1560, 680), fill=bg)
    f = ImageFont.truetype(BOLD, 88)
    d.text((960, 495), 'Your role has also', font=f, fill=(20, 20, 20), anchor='mm')
    d.text((960, 610), 'been made redundant.', font=f, fill=(20, 20, 20), anchor='mm')
    im.save(out)
    return out


# ---------- the map: pins on the aerial, zooming pin to pin ----------
AERIAL = SEG / 'aerial.png'
PINS = {'A': (700, 640), 'B': (1180, 430), 'C': (1430, 760)}   # Martha, Clive, Harriet (spots on the aerial, not real addresses)


def pin_move(name, frm, to, dur):
    """frm/to = None (whole map) or a pin key; zoom out of one pin and into the next, pins drawn as they're reached."""
    if not AERIAL.exists():
        ff('-ss', 1.0, '-i', NC / '15.mp4', '-frames:v', 1, '-vf', 'scale=1920:1080', AERIAL)
    base = Image.open(AERIAL).convert('RGB')
    out = SEG / f'{name}.mp4'
    n = round(dur * FPS)
    p = subprocess.Popen(['ffmpeg', '-loglevel', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', '1920x1080',
                          '-r', str(FPS), '-i', '-', '-c:v', 'libx264', '-crf', '18', '-preset', 'veryfast', '-pix_fmt',
                          'yuv420p', str(out)], stdin=subprocess.PIPE)
    full = (960.0, 540.0, 1.0)
    a = full if frm is None else (*PINS[frm], 3.2)
    b = full if to is None else (*PINS[to], 3.2)
    shown = {k for k in PINS if k == frm or (frm and list(PINS).index(k) < list(PINS).index(frm))}
    for i in range(n):
        u = i / max(n - 1, 1)
        if frm is not None and to is not None:      # out to the whole map, then in
            if u < 0.45:
                s = u / 0.45; s = s * s * (3 - 2 * s); c = tuple(a[j] + (full[j] - a[j]) * s for j in range(3))
            else:
                s = (u - 0.45) / 0.55; s = s * s * (3 - 2 * s); c = tuple(full[j] + (b[j] - full[j]) * s for j in range(3))
        else:
            s = u * u * (3 - 2 * u); c = tuple(a[j] + (b[j] - a[j]) * s for j in range(3))
        cx, cy, z = c
        w, h = 1920 / z, 1080 / z
        x0 = min(max(cx - w / 2, 0), 1920 - w); y0 = min(max(cy - h / 2, 0), 1080 - h)
        fr = base.crop((int(x0), int(y0), int(x0 + w), int(y0 + h))).resize((1920, 1080), Image.LANCZOS)
        d = ImageDraw.Draw(fr)
        on = set(shown)
        if to and u > (0.55 if frm else 0.15):
            on.add(to)
        for k in on:
            px, py = PINS[k]
            sx, sy = (px - x0) * z, (py - y0) * z
            drop = 0
            if k == to:
                t0 = 0.55 if frm else 0.15
                drop = max(0.0, 1 - (u - t0) / 0.2) * 60
            r = 26
            sy -= drop
            d.polygon([(sx, sy), (sx - r * 0.8, sy - r * 1.6), (sx + r * 0.8, sy - r * 1.6)], fill=(220, 30, 40))
            d.ellipse((sx - r, sy - r * 2.6, sx + r, sy - r * 0.6), fill=(220, 30, 40), outline='white', width=4)
            d.ellipse((sx - 8, sy - r * 1.6 - 8, sx + 8, sy - r * 1.6 + 8), fill='white')
        p.stdin.write(fr.tobytes())
    p.stdin.close(); p.wait()
    return out


# ---------- the head, block by block ----------
video, events, beats = [], [], []
t = 0.0
cur_beat = None


def beat(bid, title):
    global cur_beat
    cur_beat = {'id': bid, 'title': title, 'start': q(t), 'lines': []}
    beats.append(cur_beat)


def add_shot(src, inp, dur, fx=None, lt=None, still=False, looped=False, what=None):
    """One V1 shot at the cursor. fx = extra ffmpeg filter; lt = lower third text; still = an image."""
    global t
    dur = q(dur)
    k = len(video)
    seg = SEG / f'v{k:03d}.mp4'
    vf = ['scale=1920:1080:force_original_aspect_ratio=decrease', 'pad=1920:1080:(ow-iw)/2:(oh-ih)/2', f'fps={FPS}', 'setsar=1']
    hold = 0.0
    if not still and str(src).endswith('.mp4'):
        avail = probe(src) - inp
        if avail < dur:
            hold = dur - avail + 0.05
            vf.append(f'tpad=stop_mode=clone:stop_duration={hold:.3f}')
    if fx:
        vf.append(fx)
    if lt:
        tf = SEG / f'v{k:03d}-lt.txt'; tf.write_text(lt)
        vf.append(f"drawtext=fontfile={BOLD}:textfile={tf}:fontsize=44:fontcolor=white:box=1:boxcolor=black@0.6:"
                  f"boxborderw=18:x=90:y=h-170:enable='gte(t,0.25)'")
    inp_args = ['-loop', 1, '-i', src] if still else ['-ss', inp, '-i', src]
    key = SEG / f'v{k:03d}.key'
    sig = repr((str(src), inp, dur, vf, lt, pathlib.Path(src).stat().st_mtime))
    if seg.exists() and key.exists() and key.read_text() == sig:
        inp_args = None
    if inp_args: ff(*inp_args, '-t', dur, '-vf', ','.join(vf), '-an', '-c:v', 'libx264', '-crf', 18, '-preset', 'veryfast',
       '-pix_fmt', 'yuv420p', '-r', FPS, '-frames:v', round(dur * FPS), seg)
    key.write_text(sig)
    video.append({'file': str(seg), 'source': str(src), 'start': q(t), 'dur': dur, 'beat': cur_beat['id'],
                  'track': 'V1', 'in': inp, 'looped': bool(looped or hold > 0.2), 'what': what or pathlib.Path(src).name})
    if not NO_CLIP and not still and str(src).endswith('.mp4') and not str(src).startswith(str(SEG)):
        events.append({'stem': 'sfx-clip-sound', 't': q(t), 'dur': dur, 'what': pathlib.Path(src).name, 'src': str(src),
                           'in': inp, 'gain': CLIP_DB})
    t += dur


def line(src, who, name, text, by, at=None, stem='vox-narration', fx=None):
    d = probe(src)
    tt = q(t if at is None else at)
    events.append({'stem': stem, 't': tt, 'dur': d, 'what': pathlib.Path(src).name, 'src': str(src), 'fx': fx})
    cur_beat['lines'].append({'i': len(cur_beat['lines']), 'who': who, 'name': name, 't': tt, 'dur': d, 'text': text, 'by': by})
    return d


def block(lines, shots, lead=0.35, tail=0.0, min_dur=0.0):
    """lines = [(src, who, name, text, by[, stem, fx])], played one after another; shots fill the block.
    shots = [(src, in, fixed_dur or None, kw)]; the None ones share what's left."""
    t0 = t
    c = t0 + lead
    for ln in lines:
        src, who, name, text, by, *rest = ln
        c += line(src, who, name, text, by, at=c, stem=rest[0] if rest else 'vox-narration', fx=rest[1] if len(rest) > 1 else None) + 0.35
    total = max(c - 0.35 - t0 + tail if lines else 0, min_dur)
    fixed = sum(s[2] for s in shots if s[2])
    free = [s for s in shots if not s[2]]
    each = max((total - fixed) / len(free), 0.5) if free else 0
    for src, inp, dur, kw in shots:
        add_shot(src, inp, dur or each, **kw)


NARR = ('narrator', 'Narrator (Algenib)')
def nv2(f, text): return (N2 / f, *NARR, text, 'jack')
def nv3(f, text): return (N3 / f, *NARR, text, 'claude')


# beat 0: v4 as it was to 33.96 s, with the coffee-shop card in place of old clip 2 (Kai: plant the archetype)
barista = card(OC / '2.mp4', 1.0, ['Karen in a coffee shop, finger pointed', 'at the barista: "Can I speak to your manager?"'], 'card-barista')
beat('0', 'The office')
v4_words = {}
for b in V4['beats']:
    for ln in b['lines']:
        v4_words[round(ln['t'], 3)] = ln['text']
for v in V4['video']:
    if v['track'] != 'V1' or v['start'] >= 33.95:
        continue
    if abs(v['start'] - 21.917) < 0.01:
        beat('1', 'Fired by A.I. Sean')
    if 'old clips/2.mp4' in v['file']:
        add_shot(barista, 0, v['dur'], still=True, what='NEW SHOT: Karen at a coffee shop, pointing at the barista')
    else:
        add_shot(pathlib.Path(v['file']), v['in'], v['dur'])
for e in V4['events']:
    if e['stem'] == 'vox-narration' and e['t'] < 24.8:
        b = beats[0] if e['t'] < 21.9 else beats[1]
        b['lines'].append({'i': len(b['lines']), 'who': 'narrator', 'name': NARR[1], 't': e['t'], 'dur': e['dur'],
                           'text': v4_words.get(round(e['t'], 3), ''), 'by': 'jack'})
        events.append({'stem': 'vox-narration', 't': e['t'], 'dur': e['dur'], 'what': pathlib.Path(e['src']).name, 'src': e['src']})
t = q(33.958)
n04_end = 24.708 + 13.167

# beat 1 continued: Karen stunned -> hands the laptop back -> Sean fires the boss -> the boss reacts -> defenestrate
block([], [(NC / '43.mp4', 0, None, {})], min_dur=n04_end + 0.35 - t)
block([nv3('lvl_r3a1.wav', 'Stunned, Karen hands the laptop back to her boss.')], [(NC / '5.mp4', 5.2, None, {})], lead=0.0)
block([nv3('lvl_r3a2.wav', 'Ay-Eye Sean fires him too.')], [(sean_boss(), 0, None, {'still': True, 'what': "Sean's screen (the boss's words, made in post)"})], tail=0.5)
block([], [(NC / '42.mp4', 1.0, 2.6, {'what': '42.mp4 (the boss reacts)'})], min_dur=2.6)
block([nv2('lvl_n06-a.wav', 'Karen struggles to find empathy for someone she wants to defenestrate at the best of times...')],
      [(NC / '43.mp4', 4.0, None, {})], lead=0.2, tail=0.4)

# beat 2: night out; the phone thrown in protest (Kai)
beat('2', 'Night out with Susan')
block([nv2('lvl3_n38x-b.wav', 'Next stop: getting fucked up with Susan. A.I. Sean sacked her this morning too.'),
       nv2('lvl_n39-a.wav', 'Stand clear of the closing doors, please.')], [(NC / '7.mp4', 0.958, None, {})], lead=0.2)
block([nv2('lvl_n40-a.wav', 'They steal wine glasses, and head out to look over the river.')], [(OC / '28.mp4', 0, None, {})], tail=0.3)
shout = card(K / 'vids/seagull/seagull vid.mp4', 0.0, ['Karen at the railing, phone held high,', 'shouting at it'], 'card-shout')
block([(N3 / 'lvl_k01.wav', 'karen', 'Karen (Gacrux)', "Tomorrow, I'm making the complaint of the century! You hear that, Sean? Fuck you, Sean! Fuck this technology!", 'kai', 'vox-karen')],
      [(shout, 0, None, {'still': True, 'what': 'NEW SHOT: Karen at the railing, phone held high, shouting at it'})], lead=0.3, tail=0.0)
block([], [(NC / '8.mp4', 0.17, 1.7, {'what': '8.mp4 (the throw; flicker trimmed)'})], min_dur=1.7)
block([(N3 / 'lvl_s01.wav', 'susan', 'Susan (Kore)', 'Karen, you mad lad.', 'kai', 'vox-susan')],
      [(K / 'vids/seagull/seagull vid.mp4', 7.167, None, {})], lead=0.0, tail=0.2)

# beat 3: the morning after (Susan-asleep shot cut, round 1)
beat('3', 'The morning after')
block([nv2('lvl_n41-b.wav', 'Lesson learned. Know your limit... and eat something. Get fucked up responsibly, folks.'),
       nv2('lvl_n07-a.wav', 'In these moments, even atheists pray to Christ.')],
      [(NC / '8.mp4', 2.0, 2.0, {'what': '8.mp4 (the river, after)'}), (NC / '44.mp4', 0, None, {})], lead=0.3, tail=0.3)

# beat 4: the phone box, Susan's reminder, the flashback, sleeves up (Kai)
beat('4', 'The phone box')
block([nv2('lvl_n08-a.wav', "Karen, without a phone, has no idea what's happening. She heads out to find an ancient relic."),
       nv2('lvl_n09-a.wav', '[serious] A phone booth.')], [(NC / '45.mp4', 0, None, {})])
block([nv3('lvl_r3b.wav', 'Susan reminds her. Last night, Karen threw her phone in the river... and swore to make the biggest complaint the world has ever seen.')],
      [(NC / '10.mp4', 0, None, {})], tail=0.2)
FB = 'hue=s=0.3,eq=brightness=0.05:contrast=0.9,gblur=sigma=1.5,vignette=PI/4,fade=t=in:st=0:d=0.2:color=white'
block([(N3 / 'lvl_k01fb.wav', 'karen', 'Karen (Gacrux), remembered', "Tomorrow, I'm making the complaint of the century!", 'kai', 'vox-karen', 'echo')],
      [(OC / '28.mp4', 3.0, 3.0, {'fx': FB, 'what': '28.mp4 (flashback)'}), (NC / '8.mp4', 0.17, None, {'fx': FB, 'what': '8.mp4 (flashback)'})],
      lead=0.1, tail=0.2)
block([(N3 / 'n13-sleeves.wav', *NARR, 'Karen, well... she rolls her sleeves up and actually does something about it.', 'jack')],
      [(NC / '46.mp4', 0, None, {})], tail=0.3)

# beat 5: calling everyone (Kai: pins on the map, three named people, fast)
beat('5', 'Calling everyone')
block([nv3('lvl_r3c.wav', 'New York is about to experience a level of complaining it never thought possible. Every borough had better prepare.')],
      [(NC / '12.mp4', 0, None, {})], tail=0.2)
block([], [(pin_move('pin-A', None, 'A', 1.5), 0, 1.5, {'what': 'map: pin 1 (Martha)'})], min_dur=1.5)
block([nv3('lvl_r3d.wav', "First: Martha. She's just a receptionist.")], [(NC / '13.mp4', 0, None, {'lt': 'MARTHA  ·  RECEPTIONIST'})], lead=0.15)
block([nv2('lvl_n19-a.wav', '"A.I. is taking our jobs. And you just sit there. Appalling."')], [(NC / '23.mp4', 0, None, {}), (NC / '13.mp4', 4.5, 1.6, {})], tail=0.1)
block([], [(pin_move('pin-AB', 'A', 'B', 1.8), 0, 1.8, {'what': 'map: pin 1 -> pin 2 (Clive)'})], min_dur=1.8)
block([nv3('lvl_r3e.wav', 'Then Clive, from the council.')], [(NC / '16.mp4', 0, None, {'lt': 'CLIVE  ·  LOCAL COUNCIL'})], lead=0.15)
block([nv2('lvl_n20-a.wav', 'She savours each syllable, inflicting psychological damage, exactly as she did at her old H.R. job.')],
      [(NC / '23.mp4', 3.0, 3.0, {}), (NC / '16.mp4', 3.0, None, {})], tail=0.1)
block([], [(pin_move('pin-BC', 'B', 'C', 1.8), 0, 1.8, {'what': 'map: pin 2 -> pin 3 (Harriet)'})], min_dur=1.8)
block([nv3('lvl_r3f.wav', 'Then Harriet, the borough representative.')], [(NC / '20.mp4', 0, None, {'lt': 'HARRIET  ·  BOROUGH REPRESENTATIVE'})], lead=0.15)
block([nv2('lvl_n18-a.wav', 'She claims the souls of her victims. The vitriolic decay of their empty eyes fuels her bloodlust.'),
       nv2('lvl_n15-a.wav', 'Poor bastards.')],
      [(NC / '20.mp4', 3.2, 3.0, {}), (NC / '18.mp4', 0, None, {})], tail=0.2)

# beat 6: all day to complain, the seasons (Kai)
beat('6', 'All day to complain')
block([nv3('lvl_r3g.wav', "Karen's conquest will take patience.")], [(NC / '22.mp4', 0, None, {})], tail=0.1)
block([nv2('lvl_n16-b.wav', '"I have ALL DAY to complain." Karen ain\'t fucking around.')], [(NC / '14.mp4', 3.917, None, {})], tail=0.2)
block([nv3('lvl_r3h1.wav', 'All night...')], [(NC / '21.mp4', 0, None, {})], lead=0.2, min_dur=1.6)
block([nv3('lvl_r3h2.wav', 'All month...')], [(NC / '17.mp4', 0, None, {})], lead=0.2, min_dur=1.6)
block([nv3('lvl_r3h3.wav', 'All year.')], [(NC / '19.mp4', 0, None, {})], lead=0.2, min_dur=1.6)
block([nv2('lvl_n17-a.wav', "[sarcastic] No one has stayed on hold this long. Guinness World Records weep at the sight of it.")],
      [(NC / '19.mp4', 1.8, 3.2, {}), (NC / '46.mp4', 2.0, None, {})], lead=0.2)
block([nv2('lvl_n21-b.wav', 'A new day, a new dawn. Karen clutches the phone like a sniper... picking her shots.')],
      [(NC / '22.mp4', 3.5, 3.0, {}), (NC / '23.mp4', 4.0, None, {})], tail=0.6)

HEAD = q(t)
DELTA = HEAD - TAIL_FROM
for i, b in enumerate(beats):
    b['dur'] = q((beats[i + 1]['start'] if i + 1 < len(beats) else HEAD) - b['start'])
    b['see'] = f"{sum(1 for v in video if v['beat'] == b['id'])} shots, {len(b['lines'])} lines."

# ---------- the tail: Jack's v4 from "Viral" on ----------
tail_mov = SEG / 'tail.mov'
if not tail_mov.exists():
    ff('-threads', 4, '-ss', TAIL_FROM, '-i', RENDER, '-vf', f'scale=1920:1080,fps={FPS},setsar=1', '-threads', 4, '-c:v', 'libx264', '-crf', 18,
       '-preset', 'veryfast', '-pix_fmt', 'yuv420p', '-c:a', 'pcm_s16le', '-ar', 48000, '-ac', 2, tail_mov)
for b in V4['beats']:
    if b['start'] >= TAIL_FROM - 0.01:
        beats.append({**b, 'start': q(b['start'] + DELTA),
                      'lines': [{**ln, 't': ln['t'] + DELTA, 'by': 'jack'} for ln in b['lines']]})
for v in V4['video']:
    if v['start'] >= TAIL_FROM - 0.01:
        video.append({**v, 'start': v['start'] + DELTA})
for e in V4['events']:
    if e['t'] >= TAIL_FROM - 0.05 and not (NO_CLIP and e['stem'] == 'sfx-clip-sound'):
        events.append({**e, 't': e['t'] + DELTA, 'in_render': True})
TOTAL = HEAD + (V4['total'] - TAIL_FROM)

# ---------- picture: head segments + tail ----------
lst = SEG / 'head.txt'
lst.write_text(''.join(f"file '{v['file']}'\n" for v in video if v['file'].startswith(str(SEG))))
head_v = SEG / 'head-v.mp4'
ff('-f', 'concat', '-safe', 0, '-i', lst, '-c', 'copy', head_v)

# ---------- sound for the head: lines, clip sound, score ----------
ins, fl = [], []
nin = 0
for e in events:
    if e.get('in_render') or e['t'] >= HEAD:
        continue
    k = nin; nin += 1
    if e['stem'] == 'sfx-clip-sound':
        ins += ['-ss', str(e['in']), '-t', f"{e['dur']:.3f}", '-i', e['src']]
        fl.append(f"[{k}:a]aresample=48000,aformat=channel_layouts=stereo,volume={e['gain']}dB,afade=t=in:d=0.05,"
                  f"afade=t=out:st={max(e['dur'] - 0.08, 0):.3f}:d=0.08,adelay={int(e['t'] * 1000)}:all=1[a{k}]")
    else:
        ins += ['-i', e['src']]
        fx = ',aecho=0.8:0.6:120|240:0.35|0.2' if e.get('fx') == 'echo' else ''
        fl.append(f"[{k}:a]aresample=48000,aformat=channel_layouts=stereo{fx},adelay={int(e['t'] * 1000)}:all=1[a{k}]")
# score: v4's cues 1-3 laid under the new beats (1 under the office, 2 from the night out, 3 from calling everyone)
b2 = next(b['start'] for b in beats if b['id'] == '2')
b5 = next(b['start'] for b in beats if b['id'] == '5')
for f, a, z in (('1.mp3', 0.0, b2), ('2.mp3', b2, b5), ('3.mp3', b5, HEAD)):
    k = nin; nin += 1
    ins += ['-stream_loop', '-1', '-i', str(MUS / f)]
    ln = z - a
    fl.append(f"[{k}:a]atrim=0:{ln + 0.6:.3f},aresample=48000,aformat=channel_layouts=stereo,volume={MUS_DB}dB,"
              f"afade=t=in:d=0.3,afade=t=out:st={max(ln - 0.4, 0):.3f}:d=1.0,adelay={int(a * 1000)}:all=1[a{k}]")
    events.append({'stem': 'mus-score', 't': a, 'dur': ln, 'what': f, 'src': str(MUS / f)})
n = len(fl)
mix = ';'.join(fl) + ';' + ''.join(f'[a{i}]' for i in range(n)) + f'amix=inputs={n}:normalize=0:dropout_transition=0,atrim=0:{HEAD:.3f},apad=whole_dur={HEAD:.3f}[m]'
head_a = SEG / 'head-a.wav'
ff(*ins, '-filter_complex', mix, '-map', '[m]', '-ar', 48000, '-ac', 2, head_a)

if NO_CLIP:  # the tail's sound rebuilt from v4's events, the same way as the head (narration and hold music as recorded,
    # the score at MUS_DB with short fades), over the render's picture only
    tins, tfl = [], []
    for e in [e for e in events if e.get('in_render')]:
        k = len(tfl); a = e['t'] - HEAD
        if e['stem'] == 'mus-score':
            tins += ['-stream_loop', '-1', '-i', e['src']]
            tfl.append(f"[{k}:a]atrim=0:{e['dur'] + 0.6:.3f},aresample=48000,aformat=channel_layouts=stereo,volume={MUS_DB}dB,"
                       f"afade=t=in:d=0.3,afade=t=out:st={max(e['dur'] - 0.4, 0):.3f}:d=1.0,adelay={int(a * 1000)}:all=1[t{k}]")
        else:
            tins += ['-i', e['src']]
            tfl.append(f"[{k}:a]aresample=48000,aformat=channel_layouts=stereo,adelay={int(a * 1000)}:all=1[t{k}]")
    TL = TOTAL - HEAD
    tail_a = SEG / 'tail-a-noclip.wav'
    ff(*tins, '-filter_complex', ';'.join(tfl) + ';' + ''.join(f'[t{i}]' for i in range(len(tfl))) +
       f'amix=inputs={len(tfl)}:normalize=0:dropout_transition=0,volume={TAIL_DB}dB,atrim=0:{TL:.3f},apad=whole_dur={TL:.3f}[m]',
       '-map', '[m]', '-ar', 48000, '-ac', 2, tail_a)
    tail_nc = SEG / 'tail-noclip.mov'
    ff('-i', tail_mov, '-i', tail_a, '-map', '0:v', '-map', '1:a', '-c:v', 'copy', '-c:a', 'pcm_s16le', '-shortest', tail_nc)
    tail_mov = tail_nc

head_av = SEG / 'head-av.mov'
ff('-i', head_v, '-i', head_a, '-c:v', 'copy', '-c:a', 'pcm_s16le', '-shortest', head_av)
preview = OUT / 'preview.mp4'
ff('-i', head_av, '-i', tail_mov, '-filter_complex', '[0:v][0:a][1:v][1:a]concat=n=2:v=1:a=1[v][a]', '-map', '[v]', '-map', '[a]',
   '-c:v', 'libx264', '-crf', 18, '-preset', 'medium', '-pix_fmt', 'yuv420p', '-c:a', 'aac', '-b:a', '192k', '-movflags', '+faststart', preview)

# ---------- the edl ----------
stems = []
for s in ('sfx-clip-sound', 'vox-narration', 'vox-karen', 'vox-susan', 'mus-score', 'sfx-hold-music'):
    if any(e['stem'] == s for e in events):
        stems.append(s)
edl = {
    'sequence': 'karen-story-r3', 'title': 'Karen Story Timeline', 'fps': FPS, 'total': round(TOTAL, 3),
    'heading': 'Karen Story: the narrated film (cut r3, attempted from Kai\'s notes)',
    'intro': ("Cut r3 (2026-11-18): Kai's notes up to 2:08 put into one attempted cut, to note again. Office to the seasons is "
              "re-assembled from the clips; Viral onward is still Jack's Karen v4 render, unchanged. Grey cards = shots not made yet."),
    'beats': beats, 'video': video,
    'audio': [{'track': f'A{i + 1}', 'name': s} for i, s in enumerate(stems)],
    'events': [{k: v for k, v in e.items() if k in ('stem', 't', 'dur', 'what', 'src')} for e in events],
    'flags': (["r3b (Kai, 19 Nov): no clip sound anywhere. Only narration, score and the hold music play; Viral onward keeps "
               "the v4 render's picture with its sound rebuilt from v4's narration, score and hold-music events (Jack's A1 clip "
               "sound left out). Same picture as r3."] if NO_CLIP else
              ['Viral onward is the Karen v4 render (Premiere effects baked in); its sound is that render\'s mix.']) + [
              'New lines are drafts unless marked by Kai or Jack; jokes stay theirs.',
              'Grey "NEW SHOT TO MAKE" cards stand in for the coffee shop and the shouting-at-the-phone shots.'],
    'render': str(preview),
}
(OUT / 'edl.json').write_text(json.dumps(edl, indent=1))
print(json.dumps({'head': HEAD, 'total': TOTAL, 'shots': len(video), 'beats': [(b['id'], b['title'], round(b['start'], 2)) for b in beats]}))
