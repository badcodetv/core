#!/usr/bin/env python3
"""Pub Quiz: Housing: rough cut from the picked clips and the recorded voice lines.

    python3 scripts/shorts/pq_cut.py [--round N]

Picture is timed to the real voice lengths (scene-timeline): lead-in 0.4 s, 0.35 s between lines, tail 0.6 s; a shot
with no line holds HOLD seconds; a shot longer than its 8 s clip plays forward then back (looped). The clips' own sound
is dropped (Omni's whispers are placeholders for the recorded voices). One stem per speaker. Logo card on the tail.
Writes <media>/cut/r<N>/edl.json (timeline format), picture.mp4, the stems, mix.wav and preview.mp4.
"""
# style-lint: story=short-pub-quiz-housing (this cut script belongs to one short)
import argparse, json, pathlib, subprocess, sys

REPO = pathlib.Path(__file__).resolve().parents[2]
SCENE = REPO / 'docs/stories/short-pub-quiz-housing/scenes/pub-quiz-housing'
sys.path.insert(0, str(REPO / 'scripts/drive'))
from localmap import localize  # noqa: E402

cfg = localize(json.loads((SCENE / 'scene.json').read_text()))
MEDIA = pathlib.Path(cfg['media'])
VID, LINES = MEDIA / 'video', MEDIA / 'audio/lines'
LINE_TXT = {l['key']: l for l in json.loads((REPO / 'docs/stories/short-pub-quiz-housing/voices/lines/lines.json').read_text())}
LOGO = REPO / 'docs/brand/logo/badcode-stacked-reversed-2400.png'
W, H, FPS = 1080, 1920, 24
LEAD, GAP, TAIL, HOLD, LOGO_D = 0.4, 0.35, 0.6, 1.6, 2.5
JACKS = {'04-student-sum', '06-plasterer-fuckoff', '08-banker-billions', '10-bob-noone'}  # Jack's own lines (2026-11-20); the rest are drafts he agreed
NAMES = {'quizmaster': 'Quizmaster (BadCode)', 'student': 'The student', 'plasterer': 'The plasterer', 'banker': 'The banker', 'bob': 'Bob'}
# (beat id, title, clip key from scene.json clip_picks, in-point, [line keys], what we see)
SHOTS = [
    ('q', '1. The question', '01', 0.2, ['01-quizmaster-question'], 'The quizmaster at the bar, the room looks up'),
    ('huddle', '2. The huddle', '02', 0.2, ['02-student-hundred'], 'The four pull in over the sheet'),
    ('pen', '3. The pen', '03', 0.3, [], 'A hand writes a number'),
    ('more', '4. Crossed out', '04', 0.2, ['03-plasterer-more'], 'The plasterer crosses it out'),
    ('sum', '5. The beer mat', '05', 0.2, ['04-student-sum', '05-student-billions'], 'The student does sums on a beer mat'),
    ('eaves', '6. Eavesdroppers', '06', 0.2, ['06-plasterer-fuckoff'], 'The plasterer and the ginger man, face to face'),
    ('banker', '7. The banker', '07', 0.2, ['07-quizmaster-twenty', '08-banker-billions'], 'The banker, eyes on his pint'),
    ('bob', '8. Bob takes the pen', '08', 0.2, ['09-banker-bob', '10-bob-noone'], 'Bob takes the sheet'),
    ('nod', '9. The nod', '09', 0.3, [], 'The banker reads it and nods'),
    ('answer', '10. Pens down', '10', 0.2, ['11-quizmaster-pens', '12-quizmaster-answer'], 'The quizmaster reads the answer'),
    ('lands', '11. The answer lands', '11', 0.3, [], 'The table frozen at Bob\'s sheet'),
    ('wayout', '12. The way out', '12', 0.2, ['13-student-own', '14-banker-gets', '15-plasterer-brick', '16-banker-bricks'], 'The student asks; the banker turns'),
]
# Rough cut 2 (Jack, 2026-11-20: "cut what you think should go"): shots 3 (the pen) and 9 (the nod) out; lines 05, 07, 09
# and 14 out (marked "cut" in lines.json); the drunk regular's three cutaways in (clip keys D01-D03 in scene.json clip_picks).
CUT_SHOTS = {'pen', 'nod'}
CUTAWAYS = [  # (after beat id, beat, title, clip key, in, length, what we see); in/length set from the contact sheet
    ('q', 'drunk1', 'The drunk: leaning', 'D01', 0.7, 1.6, 'The drunk regular at the bar, leaning; he lurches and catches himself'),
    ('sum', 'drunk2', 'The drunk: sliding', 'D02', 0.3, 1.2, 'The drunk regular, slid most of the way off his stool'),
    ('answer', 'drunk3', 'The drunk: going over', 'D03', 0.1, 2.2, 'The drunk regular goes over; the pint lands upright in his hand'),
]
CUT_LEN = {c[1]: c[5] for c in CUTAWAYS}
# The bar filter (Jack, 2026-11-20: "lets add a bar appropriate filter"; read as the voices in a small pub room, a guess):
# a short early-reflection echo, band-limited; whispers get less room (they are close to the mic).
ROOM = {'talk': 'highpass=f=90,lowpass=f=9000,aecho=0.85:0.55:23|37|58:0.22|0.15|0.09',
        'whisper': 'highpass=f=110,lowpass=f=8500,aecho=0.9:0.6:19|31:0.12|0.07'}
CLAMP = 'scale=in_range=full:out_range=limited,format=yuv420p,lutyuv=y=clip(val\\,20\\,235)'
ENC = ['-c:v', 'libx264', '-preset', 'veryfast', '-crf', '18', '-pix_fmt', 'yuv420p', '-color_range', 'tv',
       '-colorspace', 'bt709', '-color_primaries', 'bt709', '-color_trc', 'bt709']


def ff(*a):
    subprocess.run(['ffmpeg', '-nostdin', '-loglevel', 'error', '-y', *map(str, a)], check=True)


def dur(p):
    return float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', str(p)],
                                capture_output=True, text=True, check=True).stdout)


def main():
    ap = argparse.ArgumentParser(); ap.add_argument('--round', type=int, default=1)
    ap.add_argument('--lines', default='audio/lines', help='voice-line folder under <media> (round 2: audio/lines-fast-pick)')
    ap.add_argument('--tight', action='store_true', help='round 2 on (Jack: "make the whole thing fast"): lead 0.15, gap 0.1, tail 0.25, hold 1.0')
    ap.add_argument('--room', action='store_true', help='the bar filter on the voices (ROOM)')
    a = ap.parse_args()
    global LINES, LEAD, GAP, TAIL, HOLD
    LINES = MEDIA / a.lines
    if a.tight:
        LEAD, GAP, TAIL, HOLD = 0.15, 0.1, 0.25, 1.0
    if a.round >= 3:
        return main3(a)
    cut = MEDIA / 'cut' / f'r{a.round}'; cut.mkdir(parents=True, exist_ok=True)
    picks = cfg['clip_picks']
    t, beats, vids, events, parts, flags = 0.0, [], [], [], [], []
    stems = {}  # role -> [(t, wav)]
    shots = SHOTS
    if a.round >= 2:
        shots = []
        for bid, title, ck, tin, keys, see in SHOTS:
            if bid in CUT_SHOTS:
                continue
            shots.append((bid, title, ck, tin, [k for k in keys if not LINE_TXT[k].get('cut')], see))
            for after, cb, ct, cck, cin, _, csee in CUTAWAYS:
                if after == bid and cck in picks:
                    shots.append((cb, ct, cck, cin, [], csee))
        shots = [(b, f'{n + 1}. ' + t.split('. ', 1)[-1], c, i_, k, s_) for n, (b, t, c, i_, k, s_) in enumerate(shots)]
    for i, (bid, title, ck, tin, keys, see) in enumerate(shots):
        st = t; lt = t + (LEAD if keys else 0); lines = []
        for j, k in enumerate(keys):
            w = LINES / f'{k}.wav'; d = round(dur(w), 3); role = LINE_TXT[k]['role']
            stems.setdefault(role, []).append((round(lt, 3), w))
            lines.append({'i': j, 'who': role, 'name': NAMES[role], 't': round(lt, 3), 'dur': d, 'text': LINE_TXT[k]['text'], 'by': 'jack' if k in JACKS else 'claude'})
            events.append({'stem': f'vox-{role}', 't': round(lt, 3), 'dur': d, 'what': f'{title}: {NAMES[role]}', 'src': str(w)})
            lt += d + (GAP if j < len(keys) - 1 else 0)
        sd = round((lt + TAIL - st) if keys else CUT_LEN.get(bid, HOLD), 3)
        src = VID / f"{picks[ck]}.mp4"; cd = dur(src) - tin; looped = sd > cd - 0.05
        out = cut / f'v{i:02d}-{bid}.mp4'
        vf = f'scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},fps={FPS},{CLAMP}'
        if looped:
            n = int(sd // cd) + 1  # forward, back, forward... as many passes as the words need
            labels = ''.join(f'[p{k}]' for k in range(n))
            chain = f'[0:v]{vf},split={n}{labels};' + ';'.join(f'[p{k}]{"reverse" if k % 2 else "null"}[q{k}]' for k in range(n))
            ff('-ss', tin, '-i', src, '-filter_complex', chain + ';' + ''.join(f'[q{k}]' for k in range(n)) + f'concat=n={n}:v=1[v]',
               '-map', '[v]', '-t', sd, '-an', *ENC, out)
            flags.append(f'{title}: {sd:.1f}s of words on an {cd:.1f}s clip, so it plays forward and back {n} times.')
        else:
            ff('-ss', tin, '-i', src, '-t', sd, '-vf', vf, '-an', *ENC, out)
        parts.append(out)
        vids.append({'file': str(out), 'in': tin, 'start': round(st, 3), 'dur': sd, 'beat': bid, 'source': str(src), 'looped': looped})
        beats.append({'id': bid, 'title': title, 'start': round(st, 3), 'dur': sd, 'see': see, 'lines': lines})
        t = st + sd
    ls = round(t, 3)
    ff('-f', 'lavfi', '-i', f'color=black:s={W}x{H}:r={FPS}:d={LOGO_D}', '-loop', '1', '-i', LOGO, '-filter_complex',
       f"[1]scale={int(W * 0.62)}:-1,format=rgba,fade=t=in:st=0.1:d=0.4:alpha=1[l];[0][l]overlay=(W-w)/2:(H-h)/2:shortest=1,{CLAMP}",
       '-t', LOGO_D, *ENC, cut / 'v99-logo.mp4')
    parts.append(cut / 'v99-logo.mp4')
    vids.append({'file': str(cut / 'v99-logo.mp4'), 'in': 0, 'start': ls, 'dur': LOGO_D, 'beat': 'logo', 'source': 'logo card', 'looped': False})
    beats.append({'id': 'logo', 'title': f'{len(shots) + 1}. Logo', 'start': ls, 'dur': LOGO_D, 'see': 'The BadCode logo on black', 'lines': []})
    total = round(ls + LOGO_D, 3)
    (cut / 'list.txt').write_text(''.join(f"file '{p.name}'\n" for p in parts))
    ff('-f', 'concat', '-safe', '0', '-i', cut / 'list.txt', '-c', 'copy', cut / 'picture.mp4')
    audio = []
    for role, items in stems.items():
        ins, fl = [], []
        for n, (at, w) in enumerate(items):
            ins += ['-i', w]
            room = (ROOM['whisper' if LINE_TXT[w.stem.rsplit('-', 1)[0] if w.stem not in LINE_TXT else w.stem]['whisper'] else 'talk'] + ',') if a.room else ''
            fl.append(f'[{n}]aresample=48000,aformat=channel_layouts=stereo,{room}adelay={int(at * 1000)}|{int(at * 1000)}[s{n}]')
        mixin = ''.join(f'[s{n}]' for n in range(len(items)))
        fl.append(f'{mixin}amix=inputs={len(items)}:normalize=0,apad=whole_dur={total},atrim=end={total}[o]')
        st = cut / f'vox-{role}.wav'
        ff(*ins, '-filter_complex', ';'.join(fl), '-map', '[o]', '-ar', 48000, st)
        audio.append({'track': f'A{len(audio) + 1}', 'name': f'vox-{role}', 'file': str(st)})
    ins = sum([['-i', x['file']] for x in audio], [])
    ff(*ins, '-filter_complex', f"{''.join(f'[{n}]' for n in range(len(audio)))}amix=inputs={len(audio)}:normalize=0,loudnorm=I=-14:TP=-1.5[o]",
       '-map', '[o]', '-ar', 48000, '-ac', 2, cut / 'mix.wav')
    ff('-i', cut / 'picture.mp4', '-i', cut / 'mix.wav', '-map', '0:v', '-map', '1:a', '-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k',
       '-t', total, cut / 'preview.mp4')
    flags = ['No music or pub atmosphere yet: voices only (the clips\' own sound is dropped, it holds Omni\'s placeholder whispers).',
             'Lips: the voices are placed by line length, not yet synced to the mouths (lip-sync pass owed on the talking shots).'] + flags
    edl = {'sequence': f'short-pub-quiz-housing-1-pub-quiz-r{a.round}', 'title': 'Pub Quiz Timeline',
           'heading': f'BadCode Shorts ▲ Pub Quiz: Housing, rough cut {a.round}',
           'intro': 'Your twelve picked clips with the recorded voices, timed to the words. Note anything: a beat, a line, a shot, or a frame.',
           'fps': FPS, 'total': total, 'beats': beats, 'video': vids, 'audio': audio, 'events': events, 'flags': flags}
    (cut / 'edl.json').write_text(json.dumps(edl, indent=1, ensure_ascii=False))
    print(json.dumps({'total': total, 'preview': str(cut / 'preview.mp4'), 'looped': sum(v['looped'] for v in vids)}))


# ---------------------------------------------------------------------------------------------------------------------
# Rough cut 3 (Jack, 2026-11-20: "do the edit fixes and use the beer outro i asked for"). Edit only, nothing generated:
#  1. the drunk's cutaways play OVER the lines (inserted into a talking shot), never in a silent gap;
#  2. long shots are broken up with inserts from clips we already have, so nothing plays forward-and-back if avoidable;
#  3. the whispers overlap (a negative gap between lines; short lead and tail);
#  4. a pub-room bed built from the no-dialogue clips' own sound (Flow's murmur and glasses), and the drunk's own sound
#     (thud, clatter, laugh) on his cutaways;
#  5. the outro is the end of the logo-bank clip `4/bottled it.mp4` (the spilt beer spells BADCODE on the cobbles),
#     cropped to 9:16 (a guess at "the beer outro i asked for": no record of the ask was found).
# Inserts: shot id -> [(offset from shot start | 'L<n>' = that line's start, clip key, in, length, label, own sound?)]
INSERTS = {
    'more': [(2.4, 'D01', 0.7, 1.6, 'The drunk: leaning, then a lurch', True)],
    'sum': [(2.4, 'D02', 0.3, 1.3, 'The drunk: slid off his stool', True), (5.6, '02', 2.0, 1.2, 'The table leans in', False)],
    'banker': [(3.0, '05', 4.0, 1.4, 'The student, stung', False)],
    'answer': [(0.0, 'D03', 0.1, 2.2, 'The drunk goes over on "Pens down"', True)],
    'wayout': [('L1', '11', 0.5, 1.6, 'The table from above', False)],
}
FX_GAIN = {'pq-13a-P13': 0, 'pq-14a-P14': 12, 'pq-15b-P15': -6}  # dB, from each clip's measured loudness (-29, -44, -21 LUFS)
BED = ['pq-03a-P03', 'pq-03b-P03', 'pq-11a-P11', 'pq-09b-P09', 'pq-11b-P11', 'pq-14a-P14']  # whisper-checked: no speech
OUTRO = (pathlib.Path(cfg['media']).parent.parent / 'badcode logo designs/Badcode-logo-vid/4/bottled it.mp4', 21.0, 3.0,
         'crop=420:580:38:60')  # the whole width (the word fills it), the black bars and the bottom-corner watermark cut off
L3 = dict(first_lead=0.15, lead=0.05, gap=-0.15, tail=0.12)


def seg(src, sin, d, out, vf):
    """d seconds of src from sin, forward then back as often as needed; returns True if it had to loop."""
    cd = dur(src) - sin
    if d <= cd - 0.05:
        ff('-ss', sin, '-i', src, '-t', d, '-vf', vf, '-an', *ENC, out); return False
    n = int(d // cd) + 1
    labels = ''.join(f'[p{k}]' for k in range(n))
    chain = f'[0:v]{vf},split={n}{labels};' + ';'.join(f'[p{k}]{"reverse" if k % 2 else "null"}[q{k}]' for k in range(n))
    ff('-ss', sin, '-i', src, '-filter_complex', chain + ';' + ''.join(f'[q{k}]' for k in range(n)) + f'concat=n={n}:v=1[v]',
       '-map', '[v]', '-t', d, '-an', *ENC, out)
    return True


def main3(a):
    cut = MEDIA / 'cut' / f'r{a.round}'; cut.mkdir(parents=True, exist_ok=True)
    picks = cfg['clip_picks']
    vf = f'scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},fps={FPS},{CLAMP}'
    shots = [(b, t, c, i_, [k for k in ks if not LINE_TXT[k].get('cut')], s_) for b, t, c, i_, ks, s_ in SHOTS if b not in CUT_SHOTS]
    t, beats, vids, events, parts, flags, fx = 0.0, [], [], [], [], [], []
    stems = {}
    for n, (bid, title, ck, tin, keys, see) in enumerate(shots):
        title = f'{n + 1}. ' + title.split('. ', 1)[-1]
        st = t; lt = t + (L3['first_lead'] if n == 0 else L3['lead']); lines, starts = [], []
        for j, k in enumerate(keys):
            w = LINES / f'{k}.wav'; d = round(dur(w), 3); role = LINE_TXT[k]['role']
            stems.setdefault(role, []).append((round(lt, 3), w)); starts.append(lt - st)
            lines.append({'i': j, 'who': role, 'name': NAMES[role], 't': round(lt, 3), 'dur': d, 'text': LINE_TXT[k]['text'], 'by': 'jack' if k in JACKS else 'claude'})
            events.append({'stem': f'vox-{role}', 't': round(lt, 3), 'dur': d, 'what': f'{title}: {NAMES[role]}', 'src': str(w)})
            lt += d + (L3['gap'] if j < len(keys) - 1 else 0)
        sd = round(lt + L3['tail'] - st, 3) if keys else 1.0  # a reaction shot with no words holds 1 s
        ins = []
        for off, ik, iin, ilen, lab, own in INSERTS.get(bid, []):
            o = starts[int(off[1:])] if isinstance(off, str) else off
            ins.append((round(o, 3), ik, iin, min(ilen, sd - o), lab, own))
        ins.sort()
        main_src = VID / f'{picks[ck]}.mp4'
        need = sd - sum(i[3] for i in ins)
        mfile = cut / f'm{n:02d}-{bid}.mp4'; looped = seg(main_src, tin, need, mfile, vf)
        if looped:
            flags.append(f'{title}: {need:.1f}s of its own clip needed on a {dur(main_src) - tin:.1f}s clip, so it plays forward and back.')
        cur, used = 0.0, 0.0
        pieces = []
        for o, ik, iin, ilen, lab, own in ins + [(sd, None, 0, 0, '', False)]:
            if o > cur + 0.01:  # a stretch of the shot's own clip
                pf = cut / f'v{n:02d}-{len(pieces)}-{bid}.mp4'
                ff('-ss', used, '-i', mfile, '-t', o - cur, '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '18', '-pix_fmt', 'yuv420p',
                   '-color_range', 'tv', '-colorspace', 'bt709', '-color_primaries', 'bt709', '-color_trc', 'bt709', pf)
                pieces.append(pf)
                vids.append({'file': str(pf), 'in': round(tin + used, 3), 'start': round(st + cur, 3), 'dur': round(o - cur, 3), 'beat': bid, 'source': str(main_src), 'looped': looped})
                used += o - cur; cur = o
            if ik is None:
                break
            isrc = VID / f'{picks[ik]}.mp4'; pf = cut / f'v{n:02d}-{len(pieces)}-{bid}-ins.mp4'
            seg(isrc, iin, ilen, pf, vf); pieces.append(pf)
            vids.append({'file': str(pf), 'in': iin, 'start': round(st + cur, 3), 'dur': round(ilen, 3), 'beat': bid, 'source': str(isrc), 'looped': False, 'note': lab})
            if own:
                fx.append((round(st + cur, 3), isrc, iin, ilen, lab))
                events.append({'stem': 'fx-drunk', 't': round(st + cur, 3), 'dur': round(ilen, 3), 'what': f'{title}: {lab} (its own sound)', 'src': str(isrc)})
            cur += ilen
        parts += pieces
        beats.append({'id': bid, 'title': title, 'start': round(st, 3), 'dur': sd, 'see': see + ''.join(f'; insert: {i[4]}' for i in ins), 'lines': lines})
        t = st + sd
    # the outro: the logo bank's beer clip
    ls = round(t, 3); osrc, oin, od, ocrop = OUTRO
    ff('-ss', oin, '-i', osrc, '-t', od, '-filter_complex',
       f'[0:v]{ocrop},split[a][b];[b]scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},boxblur=30:2,eq=brightness=-0.15[bg];'
       f'[a]scale={W}:-2:flags=lanczos[fg];[bg][fg]overlay=0:(H-h)/2,fps={FPS},{CLAMP}[v]', '-map', '[v]', '-an', *ENC, cut / 'v99-outro.mp4')
    parts.append(cut / 'v99-outro.mp4')
    vids.append({'file': str(cut / 'v99-outro.mp4'), 'in': oin, 'start': ls, 'dur': od, 'beat': 'logo', 'source': str(osrc), 'looped': False})
    beats.append({'id': 'logo', 'title': f'{len(shots) + 1}. Outro', 'start': ls, 'dur': od, 'see': 'The spilt beer spells BADCODE on the cobbles (logo bank: 4/bottled it.mp4, from 21 s)', 'lines': []})
    total = round(ls + od, 3)
    (cut / 'list.txt').write_text(''.join(f"file '{p.name}'\n" for p in parts))
    ff('-f', 'concat', '-safe', '0', '-i', cut / 'list.txt', '-c', 'copy', cut / 'picture.mp4')
    audio = []
    for role, items in stems.items():
        ins_, fl = [], []
        for k, (at, w) in enumerate(items):
            ins_ += ['-i', w]
            room = (ROOM['whisper' if LINE_TXT[w.stem]['whisper'] else 'talk'] + ',') if a.room else ''
            fl.append(f'[{k}]aresample=48000,aformat=channel_layouts=stereo,{room}adelay={int(at * 1000)}|{int(at * 1000)}[s{k}]')
        fl.append(f"{''.join(f'[s{k}]' for k in range(len(items)))}amix=inputs={len(items)}:normalize=0,apad=whole_dur={total},atrim=end={total}[o]")
        stp = cut / f'vox-{role}.wav'; ff(*ins_, '-filter_complex', ';'.join(fl), '-map', '[o]', '-ar', 48000, stp)
        audio.append({'track': f'A{len(audio) + 1}', 'name': f'vox-{role}', 'file': str(stp)})
    # the drunk's own sound on his cutaways
    ins_, fl = [], []
    for k, (at, src, iin, ilen, _) in enumerate(fx):
        ins_ += ['-ss', iin, '-t', ilen, '-i', src]
        fl.append(f'[{k}:a]asetpts=PTS-STARTPTS,aresample=48000,aformat=channel_layouts=stereo,afade=t=in:d=0.05,afade=t=out:st={max(0, ilen - 0.15)}:d=0.15,volume={FX_GAIN.get(src.stem, 0)}dB,adelay={int(at * 1000)}|{int(at * 1000)},asetpts=N/SR/TB[f{k}]')  # reset pts: -ss inputs + atrim shifted every sound by the first delay (2026-11-20)
    fl.append(f"{''.join(f'[f{k}]' for k in range(len(fx)))}amix=inputs={len(fx)}:normalize=0,apad=whole_dur={total},atrim=end={total}[o]")
    stp = cut / 'fx-drunk.wav'; ff(*ins_, '-filter_complex', ';'.join(fl), '-map', '[o]', '-ar', 48000, stp)
    audio.append({'track': f'A{len(audio) + 1}', 'name': 'fx-drunk', 'file': str(stp)})
    # the pub-room bed: the no-dialogue clips' own sound, crossfaded and looped under the whole cut, out under the outro
    ins_ = sum([['-i', VID / f'{b}.mp4'] for b in BED], [])
    chain = '[0:a]aresample=48000,aformat=channel_layouts=stereo[b0];'
    for k in range(1, len(BED)):
        chain += f'[{k}:a]aresample=48000,aformat=channel_layouts=stereo[r{k}];[b{k - 1}][r{k}]acrossfade=d=1.5[b{k}];'
    chain += f'[b{len(BED) - 1}]aloop=loop=-1:size=2e9,atrim=end={total},loudnorm=I=-30,volume=-14dB,afade=t=out:st={ls}:d={od}[o]'
    stp = cut / 'amb-pub.wav'; ff(*ins_, '-filter_complex', chain, '-map', '[o]', '-ar', 48000, '-ac', 2, stp)
    audio.append({'track': f'A{len(audio) + 1}', 'name': 'amb-pub', 'file': str(stp)})
    events.append({'stem': 'amb-pub', 't': 0, 'dur': total, 'what': 'Pub room: murmur and glasses (from the clips\' own sound)', 'src': str(VID / f'{BED[0]}.mp4')})  # the bed's first clip; all of them are in BED
    ins_ = sum([['-i', x['file']] for x in audio], [])
    ff(*ins_, '-filter_complex', f"{''.join(f'[{k}]' for k in range(len(audio)))}amix=inputs={len(audio)}:normalize=0,loudnorm=I=-14:TP=-1.5,alimiter=limit=0.85:level=0[o]",
       '-map', '[o]', '-ar', 48000, '-ac', 2, cut / 'mix.wav')
    ff('-i', cut / 'picture.mp4', '-i', cut / 'mix.wav', '-map', '0:v', '-map', '1:a', '-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k', '-t', total, cut / 'preview.mp4')
    flags = ['No music yet. Pub room sound is built from the clips\' own murmur (no library sound).',
             'Lips: not yet synced (step 2, after this pacing is agreed).',
             'Outro: the end of the logo bank\'s "bottled it" clip (spilt beer spells BADCODE), my guess at "the beer outro"; it is a 496x744 source, so it is soft at 1080x1920.'] + flags
    edl = {'sequence': f'short-pub-quiz-housing-1-pub-quiz-r{a.round}', 'title': 'Pub Quiz Timeline',
           'heading': f'BadCode Shorts ▲ Pub Quiz: Housing, rough cut {a.round}',
           'intro': 'Edit fixes: the drunk plays over the lines, long shots broken up, whispers overlapping, pub room sound, the beer outro.',
           'fps': FPS, 'total': total, 'beats': beats, 'video': vids, 'audio': audio, 'events': events, 'flags': flags}
    (cut / 'edl.json').write_text(json.dumps(edl, indent=1, ensure_ascii=False))
    print(json.dumps({'total': total, 'preview': str(cut / 'preview.mp4'), 'looped': sum(v['looped'] for v in vids)}))


if __name__ == '__main__':
    main()
