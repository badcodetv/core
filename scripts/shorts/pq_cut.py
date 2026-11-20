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


if __name__ == '__main__':
    main()
