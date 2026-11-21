#!/usr/bin/env python3
"""Fire Sale: rough cut from the picked clips and the voices.

    python3 scripts/shorts/fire_cut.py [--round N]

Jim and Phineas speak on camera: the clip was made saying the line (Omni's own audio, dropped), and the AI Studio voice
is laid where the clip's own speech starts, stretched (0.88-1.15) to the clip's speech length (from its sound level,
silencedetect). The auctioneer is masked: his line is placed by ear. Fiona's phone notification is drawn over the home
shot. The clips' own room sound runs low. Ends on a plain logo card. Writes <media>/cut/r<N>/ in the timeline format.
"""
# style-lint: story=short-fire-sale
import argparse, json, pathlib, re, subprocess, sys

REPO = pathlib.Path(__file__).resolve().parents[2]
SCENE = REPO / 'docs/stories/short-fire-sale/scenes/fire-sale'
sys.path.insert(0, str(REPO / 'scripts/drive'))
from localmap import localize  # noqa: E402

cfg = localize(json.loads((SCENE / 'scene.json').read_text()))
MEDIA = pathlib.Path(cfg['media'])
VID, CAST, MB = MEDIA / 'video', MEDIA / 'audio/casting', MEDIA / 'moodboard'
TXT = {l['key']: l for l in json.loads((REPO / 'docs/stories/short-fire-sale/voices/lines/lines.json').read_text())}
VOICE = {'jim': 'jim-a', 'phineas': 'phineas-a', 'badcode': 'badcode-c'}  # Claude's guesses while Jack is away
TEMPO = {}
HOSPITAL = 'fire-sale-S02hd-S02h.mp4'  # speaks a stand-in line (the hospital line is refused as speech); dubbed here
NAMES = {'jim': 'Jim', 'phineas': 'Phineas', 'badcode': 'BadCode (auctioneer)'}
FONT = '/mnt/c/Windows/Fonts/segoeui.ttf'
NOTE = ['Phineas narrowly defeats', 'Brian in the polls']
LOGO = REPO / 'docs/brand/logo/badcode-stacked-reversed-2400.png'
W, H, FPS = 1080, 1920, 24
CLAMP = 'scale=in_range=full:out_range=limited,format=yuv420p,lutyuv=y=clip(val\\,20\\,235)'
ENC = ['-c:v', 'libx264', '-preset', 'veryfast', '-crf', '18', '-pix_fmt', 'yuv420p', '-color_range', 'tv',
       '-colorspace', 'bt709', '-color_primaries', 'bt709', '-color_trc', 'bt709']
VF = f'scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},fps={FPS},{CLAMP}'
# (beat, title, source, kind, in, min dur, [(line key, at)], own sound?, what we see)
SHOTS = [
    ('carboot', 'The car boot', 'fire-sale-S01a-S01.mp4', 'clip', 0.3, 2.6, [], True, 'Fiona trudges through the drizzle'),
    ('hospital', 'Hospitals', 'HOSPITAL_CLIP', 'clip', 0.0, 2.4, [('01-hospitals', 'sync')], True, 'NHS £40'),
    ('courts', 'The courts', 'fire-sale-S03b-S03.mp4', 'clip', 1.1, 2.4, [('02-courts', 'sync')], True, 'THE COURTS – SLIGHTLY USED'),
    ('car', 'The car', 'fire-sale-S04a-S04.mp4', 'clip', 0.3, 2.6, [], True, 'A long black car rolls across the mud'),
    ('arrival', 'Phineas arrives', 'fire-sale-S05b-S05.mp4', 'clip', 0.2, 2.8, [], True, 'Under the chauffeur\'s umbrella, Larry behind'),
    ('allofit', 'All of it', 'fire-sale-S06b-S06.mp4', 'clip', 1.2, 2.2, [('03-allofit', 'sync')], True, 'The ring on Larry\'s shoulder'),
    ('home', 'Home', 'fire-sale-S07a-S07.mp4', 'note', 0.3, 3.4, [], True, 'Her phone: Phineas narrowly defeats Brian in the polls'),
    ('paddle', 'The auction', 'fire-sale-S08a-S08.mp4', 'clip', 0.2, 2.4, [], True, 'Paddle 29: £150,000'),
    ('limit', 'The limit', 'fire-sale-S09a-S09.mp4', 'clip', 0.2, 2.0, [('04-limit', 0.3)], True, 'Fifty quid, same as everyone'),
    ('everyone', 'Same as everyone', 'fire-sale-S10a-S10.mp4', 'clip', 0.3, 3.0, [], True, 'Every paddle in the tent says £50'),
    ('logo', 'The logo', None, 'logo', 0.0, 2.4, [], False, 'Logo card'),
]


def ff(*a):
    subprocess.run(['ffmpeg', '-nostdin', '-loglevel', 'error', '-y', *map(str, a)], check=True)


def dur(p):
    return float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', str(p)],
                                capture_output=True, text=True, check=True).stdout)


def src_path(src):
    return VID / src


def speech_span(src, cin, sd):
    """Start and end (seconds into the shot) of the clip's own speech, from its sound level."""
    r = subprocess.run(['ffmpeg', '-nostdin', '-ss', str(cin), '-t', str(sd + 3), '-i', str(src), '-af',
                        'highpass=f=200,lowpass=f=3500,silencedetect=n=-32dB:d=0.25', '-f', 'null', '-'],
                       capture_output=True, text=True).stderr
    ends = [float(x) for x in re.findall(r'silence_end: ([0-9.]+)', r)]
    starts = [float(x) for x in re.findall(r'silence_start: ([0-9.]+)', r)]
    on = ends[0] if ends and (not starts or starts[0] < 0.05) else 0.0
    off = next((x for x in starts if x > on + 0.3), sd)
    return on, off


import importlib.util as _iu
_spec = _iu.spec_from_file_location('vrf', REPO / 'scripts/gpom/second-half-video/voice-row-fit.py')
vrf = _iu.module_from_spec(_spec); _spec.loader.exec_module(vrf)
norm = lambda w: re.sub(r'[^a-z]', '', w.lower())


def phrases(wav):
    """(start, end) of each spoken phrase in a voice take, split at pauses of 0.12 s or more."""
    r = subprocess.run(['ffmpeg', '-nostdin', '-i', str(wav), '-af', 'silencedetect=n=-40dB:d=0.12', '-f', 'null', '-'],
                       capture_output=True, text=True).stderr
    st = [float(x) for x in re.findall(r'silence_start: ([0-9.]+)', r)]
    en = [float(x) for x in re.findall(r'silence_end: ([0-9.]+)', r)]
    total = dur(wav); segs, t = [], 0.0
    for a, b in zip(st, en + [total]):
        if a - t > 0.08: segs.append((t, a))
        t = b
    if total - t > 0.08: segs.append((t, total))
    return segs or [(0.0, total)]


def main():
    ap = argparse.ArgumentParser(); ap.add_argument('--round', type=int, default=1); a = ap.parse_args()
    cut = MEDIA / 'cut' / f'r{a.round}'; cut.mkdir(parents=True, exist_ok=True)
    t, beats, vids, parts, vox, events, room = 0.0, [], [], [], [], [], []
    for n, (bid, title, src, kind, cin, sd, lines, own, see) in enumerate(SHOTS):
        src = HOSPITAL if src == 'HOSPITAL_CLIP' else src
        title = f'{n + 1}. {title}'; st = t; ls = []
        prev_end = None
        for k, at in lines:
            role = TXT[k]['role']; w = cut / f'line-{k}.wav'
            raw = cut / f'raw-{k}.wav'
            ff('-i', CAST / f'{k}--{VOICE[role]}.wav', '-af', 'silenceremove=start_periods=1:start_threshold=-55dB,areverse,'
               'silenceremove=start_periods=1:start_threshold=-55dB,areverse', raw)
            if at == 'sync':
                # each sentence of our line goes where the clip says its first word (or, if the clip's words differ, its
                # first spoken word for sentence 1); Whisper word times from the clip's own audio stand in for the mouth
                cw = [(norm(x), a0 - cin, b0 - cin) for x, a0, b0 in vrf.words_of(str(src_path(src))) if cin - 0.2 <= a0 <= cin + sd + 2]
                NUM = {'forty', 'fifty', 'twenty', 'thirty', 'hundred'}
                cw = [(x[0] or '#num', x[1] if x[2] - x[1] < 0.6 else x[2] - 0.3, x[2]) for x in cw]  # '' = a number Whisper wrote as digits
                sents = [x.split() for x in re.split(r'(?<=[.!?])\s+', TXT[k]['text']) if x.strip()]
                segs = phrases(raw)
                if len(segs) != len(sents):
                    segs = [(segs[0][0], segs[-1][1])]; sents = [sum(sents, [])]
                starts, used = [], 0
                for i, sent in enumerate(sents):
                    key = '#num' if norm(sent[0]) in NUM else norm(sent[0])
                    hit = next((a0 for wd, a0, b0 in cw[used:] if wd == key), None)
                    if hit is None:
                        hit = cw[0][1] if (i == 0 and cw) else (starts[-1] + (segs[i][0] - segs[i - 1][0]) if starts else 0.0)
                    starts.append(max(0.0, hit))
                ins, fl = ['-i', raw], []
                for i, ((a0, b0), t0) in enumerate(zip(segs, starts)):
                    fl.append(f'[0]atrim={a0}:{b0},asetpts=PTS-STARTPTS,adelay={int((t0 - starts[0]) * 1000)}|{int((t0 - starts[0]) * 1000)}[p{i}]')
                fl.append(f"{''.join(f'[p{i}]' for i in range(len(segs)))}amix=inputs={len(segs)}:normalize=0[o]")
                ff(*ins, '-filter_complex', ';'.join(fl), '-map', '[o]', w)
                at = round(starts[0], 3)
            else:
                ff('-i', raw, w)
            d = round(dur(w), 3); lt = round(prev_end + 0.15 if at is None else st + at, 3); prev_end = lt + d
            vox.append((lt, w, role))
            ls.append({'i': len(ls), 'who': role, 'name': NAMES[role], 't': lt, 'dur': d, 'text': TXT[k]['text'], 'by': TXT[k]['by']})
            events.append({'stem': f'vox-{role}', 't': lt, 'dur': d, 'what': f'{title}: {NAMES[role]}', 'src': str(w)})
            sd = max(sd, round(lt - st + d + 0.35, 3))
        pf = cut / f'v{n:02d}-{bid}.mp4'
        if kind in ('clip', 'note'):
            s = VID / src
            vf = VF + ',tpad=stop_mode=clone:stop_duration=4'
            if kind == 'note':  # a phone notification card, top of frame, fades in
                box = "drawbox=x=90:y=260:w=900:h=190:color=white@0.92:t=fill:enable='gte(t,0.5)',"
                txt = box + ''.join(f"drawtext=fontfile='{FONT}':text='{q}':fontsize=50:fontcolor=black:x=140:y={300 + i * 66}:enable='gte(t,0.5)',"
                                    for i, q in enumerate(NOTE))
                txt += f"drawtext=fontfile='{FONT}':text='NEWS':fontsize=28:fontcolor=gray:x=140:y=272:enable='gte(t,0.5)'"
                vf = vf.replace(CLAMP, txt + ',' + CLAMP)
            ff('-ss', cin, '-i', s, '-t', sd, '-vf', vf, '-t', sd, '-an', *ENC, pf)
            if own:
                room.append((round(st, 3), s, cin, sd))
                events.append({'stem': 'amb-room', 't': round(st, 3), 'dur': sd, 'what': f"{title}: the clip's own sound", 'src': str(s)})
        elif kind == 'pullback':
            s = MB / src; fr = int(sd * FPS)
            ff('-loop', 1, '-i', s, '-vf', f"scale=3240:-2,zoompan=z='1.9-0.9*(1-pow(1-on/{fr},2))':x='(iw-iw/zoom)*0.12*(1-on/{fr})+(iw-iw/zoom)/2*(on/{fr})':"
               f"y='(ih-ih/zoom)*0.45':d={fr}:s={W}x{H}:fps={FPS},{CLAMP}", '-frames:v', fr, *ENC, pf)
        else:
            ff('-f', 'lavfi', '-i', f'color=black:s={W}x{H}:r={FPS}:d={sd}', '-loop', 1, '-i', LOGO, '-filter_complex',
               f"[1]scale=640:-1,format=rgba,fade=t=in:st=0.2:d=0.5:alpha=1[l];[0][l]overlay=(W-w)/2:(H-h)/2:shortest=1,{CLAMP}",
               '-t', sd, *ENC, pf)
        parts.append(pf); vids.append({'file': str(pf), 'in': cin, 'start': round(st, 3), 'dur': sd, 'beat': bid, 'source': str(src), 'looped': False})
        beats.append({'id': bid, 'title': title, 'start': round(st, 3), 'dur': sd, 'see': see, 'lines': ls})
        t = st + sd
    total = round(t, 3)
    (cut / 'list.txt').write_text(''.join(f"file '{p.name}'\n" for p in parts))
    ff('-f', 'concat', '-safe', '0', '-i', cut / 'list.txt', '-c', 'copy', cut / 'picture.mp4')
    audio = []
    for role in NAMES:
        items = [(at, w) for at, w, r in vox if r == role]
        if not items:
            continue
        ins, fl = [], []
        for k, (at, w) in enumerate(items):
            ins += ['-i', w]; fl.append(f'[{k}]aresample=48000,aformat=channel_layouts=stereo,adelay={int(at * 1000)}|{int(at * 1000)}[s{k}]')
        fl.append(f"{''.join(f'[s{k}]' for k in range(len(items)))}amix=inputs={len(items)}:normalize=0,apad=whole_dur={total},atrim=end={total}[o]")
        sp = cut / f'vox-{role}.wav'; ff(*ins, '-filter_complex', ';'.join(fl), '-map', '[o]', '-ar', 48000, sp)
        audio.append({'track': f'A{len(audio) + 1}', 'name': f'vox-{role}', 'file': str(sp)})
    ins, fl = [], []
    for k, (at, s, iin, ilen) in enumerate(room):
        ins += ['-ss', iin, '-t', ilen, '-i', s]
        fl.append(f'[{k}:a]asetpts=PTS-STARTPTS,aresample=48000,aformat=channel_layouts=stereo,highpass=f=100,'
                  f'afade=t=in:d=0.1,afade=t=out:st={max(0, ilen - 0.15)}:d=0.15,volume=-16dB,adelay={int(at * 1000)}|{int(at * 1000)}[f{k}]')
    fl.append(f"{''.join(f'[f{k}]' for k in range(len(room)))}amix=inputs={len(room)}:normalize=0,apad=whole_dur={total},atrim=end={total}[o]")
    sp = cut / 'amb-room.wav'; ff(*ins, '-filter_complex', ';'.join(fl), '-map', '[o]', '-ar', 48000, sp)
    audio.append({'track': f'A{len(audio) + 1}', 'name': 'amb-room', 'file': str(sp)})
    ins = sum([['-i', x['file']] for x in audio], [])
    ff(*ins, '-filter_complex', f"{''.join(f'[{k}]' for k in range(len(audio)))}amix=inputs={len(audio)}:normalize=0,loudnorm=I=-14:TP=-1.5,alimiter=limit=0.84:level=0[o]",
       '-map', '[o]', '-ar', 48000, '-ac', 2, cut / 'mix.wav')
    ff('-i', cut / 'picture.mp4', '-i', cut / 'mix.wav', '-map', '0:v', '-map', '1:a', '-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k', '-t', total, cut / 'preview.mp4')
    edl = {'sequence': f'short-fire-sale-1-fire-sale-r{a.round}', 'title': 'Fire Sale Timeline',
           'heading': f'BadCode Shorts ▲ Fire Sale, rough cut {a.round}',
           'intro': 'A rainy car boot: Jim flogs the country; Phineas arrives in a long black car and buys the lot; he wins the election; at the auction, fifty quid is the limit, same as everyone.',
           'fps': FPS, 'total': total, 'beats': beats, 'video': vids, 'audio': audio, 'events': events,
           'flags': ['No music yet. Room sound is the clips\' own, low.', 'Voices are Claude\'s guesses (Jim a, Phineas a, BadCode c) until Jack picks.', 'The way out (a fifty-pound cap on donations) is Claude\'s: no government policy on record.', 'Logo: a plain card for now.']}
    (cut / 'edl.json').write_text(json.dumps(edl, indent=1, ensure_ascii=False))
    print(json.dumps({'total': total, 'preview': str(cut / 'preview.mp4')}))


if __name__ == '__main__':
    main()
