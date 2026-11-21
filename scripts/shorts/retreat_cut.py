#!/usr/bin/env python3
"""The Retreat: rough cut from the picked clips and the voices.

    python3 scripts/shorts/retreat_cut.py [--round N]

No line needs lip-sync: the guru is soft in the background, the bro whispers behind his hand, BadCode is masked.
The Ram Dass quote is drawn over the sunset. The clips' own sound runs low. Ends on a plain logo card.
Writes <media>/cut/r<N>/ in the timeline format.
"""
# style-lint: story=short-the-retreat
import argparse, json, pathlib, subprocess, sys

REPO = pathlib.Path(__file__).resolve().parents[2]
SCENE = REPO / 'docs/stories/short-the-retreat/scenes/the-retreat'
sys.path.insert(0, str(REPO / 'scripts/drive'))
from localmap import localize  # noqa: E402

cfg = localize(json.loads((SCENE / 'scene.json').read_text()))
MEDIA = pathlib.Path(cfg['media'])
VID, CAST, MB = MEDIA / 'video', MEDIA / 'audio/casting', MEDIA / 'moodboard'
TXT = {l['key']: l for l in json.loads((REPO / 'docs/stories/short-the-retreat/voices/lines/lines.json').read_text())}
VOICE = {'guru': 'guru-a', 'bro': 'bro-a', 'badcode': 'badcode-a'}  # Claude's guesses until Jack picks
TEMPO = {'guru': 1.3}  # the guru's meditation voice is slow; 30% faster, same pitch
NAMES = {'guru': 'The guru', 'bro': 'The bro', 'badcode': 'BadCode (card machine)'}
FONT = '/mnt/c/Windows/Fonts/georgiai.ttf'
QUOTE = ["If you think you're enlightened,", 'go and spend a week', 'with your family.']
CREDIT = 'attributed to Ram Dass'
LOGO = REPO / 'docs/brand/logo/badcode-stacked-reversed-2400.png'
W, H, FPS = 1080, 1920, 24
CLAMP = 'scale=in_range=full:out_range=limited,format=yuv420p,lutyuv=y=clip(val\\,20\\,235)'
ENC = ['-c:v', 'libx264', '-preset', 'veryfast', '-crf', '18', '-pix_fmt', 'yuv420p', '-color_range', 'tv',
       '-colorspace', 'bt709', '-color_primaries', 'bt709', '-color_trc', 'bt709']
VF = f'scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},fps={FPS},{CLAMP}'
# (beat, title, source, kind, in, min dur, [(line key, at)], own sound?, what we see)
SHOTS = [
    ('quote', 'The quote', 'the-retreat-R01b-R01.mp4', 'quote', 0.2, 4.2, [], True, 'The Ram Dass line over a golden sunset'),
    ('sign', 'The sign', 'the-retreat-R02a-R02.mp4', 'clip', 0.6, 2.2, [], True, 'DETOX FROM MATERIALISM, £3,000'),
    ('circle', 'The circle', 'the-retreat-R03a-R03.mp4', 'clip', 0.2, 4.0, [('01-attachment', 0.2), ('02-sell', None)], True, 'Let go of every attachment; the bro trades into his sleeve'),
    ('gong', 'The gong', 'the-retreat-R04a-R04.mp4', 'clip', 0.1, 3.0, [('03-gong', 0.6)], True, 'The gong; BadCode holds out the card machine'),
    ('shop', 'The gift shop', 'the-retreat-R05a-R05.mp4', 'clip', 0.3, 2.6, [], True, '£80 rocks'),
    ('keeper', 'The groundskeeper', 'the-retreat-R06a-R06.mp4', 'clip', 0.2, 3.0, [], True, 'On his break, the wind in the trees'),
    ('dog', 'The dog', 'the-retreat-R07a-R07.mp4', 'clip', 0.2, 3.6, [], True, 'The dog runs up; he pets it'),
    ('logo', 'The logo', None, 'logo', 0.0, 2.4, [], False, 'Logo card'),
]


def ff(*a):
    subprocess.run(['ffmpeg', '-nostdin', '-loglevel', 'error', '-y', *map(str, a)], check=True)


def dur(p):
    return float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', str(p)],
                                capture_output=True, text=True, check=True).stdout)


def main():
    ap = argparse.ArgumentParser(); ap.add_argument('--round', type=int, default=1); a = ap.parse_args()
    cut = MEDIA / 'cut' / f'r{a.round}'; cut.mkdir(parents=True, exist_ok=True)
    t, beats, vids, parts, vox, events, room = 0.0, [], [], [], [], [], []
    for n, (bid, title, src, kind, cin, sd, lines, own, see) in enumerate(SHOTS):
        title = f'{n + 1}. {title}'; st = t; ls = []
        prev_end = None
        for k, at in lines:
            role = TXT[k]['role']; w = cut / f'line-{k}.wav'
            ff('-i', CAST / f'{k}--{VOICE[role]}.wav', '-af', 'silenceremove=start_periods=1:start_threshold=-55dB,areverse,'
               f'silenceremove=start_periods=1:start_threshold=-55dB,areverse,atempo={TEMPO.get(role, 1.0)}', w)
            d = round(dur(w), 3); lt = round(prev_end + 0.15 if at is None else st + at, 3); prev_end = lt + d
            vox.append((lt, w, role))
            ls.append({'i': len(ls), 'who': role, 'name': NAMES[role], 't': lt, 'dur': d, 'text': TXT[k]['text'], 'by': TXT[k]['by']})
            events.append({'stem': f'vox-{role}', 't': lt, 'dur': d, 'what': f'{title}: {NAMES[role]}', 'src': str(w)})
            sd = max(sd, round(lt - st + d + 0.35, 3))
        pf = cut / f'v{n:02d}-{bid}.mp4'
        if kind in ('clip', 'quote'):
            s = VID / src
            vf = VF + ',tpad=stop_mode=clone:stop_duration=4'
            if kind == 'quote':
                txt = ''.join(f"drawtext=fontfile='{FONT}':text='{q.replace(chr(39), chr(8217))}':fontsize=62:fontcolor=white:x=(w-tw)/2:y={300 + i * 84}:"
                              f"shadowcolor=black@0.35:shadowx=2:shadowy=2:alpha='min(1,max(0,(t-0.3)/0.6))'," for i, q in enumerate(QUOTE))
                txt += f"drawtext=fontfile='{FONT}':text='{CREDIT}':fontsize=40:fontcolor=white@0.9:x=(w-tw)/2:y={300 + len(QUOTE) * 84 + 30}:shadowcolor=black@0.35:shadowx=2:shadowy=2:alpha='min(1,max(0,(t-0.9)/0.6))'"
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
    edl = {'sequence': f'short-the-retreat-1-the-retreat-r{a.round}', 'title': 'Retreat Timeline',
           'heading': f'BadCode Shorts ▲ The Retreat, rough cut {a.round}',
           'intro': 'The Ram Dass line over a sunset; a £3,000 detox from materialism where nobody detoxes; behind it, the groundskeeper and his dog.',
           'fps': FPS, 'total': total, 'beats': beats, 'video': vids, 'audio': audio, 'events': events,
           'flags': ['No music yet. Room sound is the clips\' own, low.', 'Voices are Claude\'s guesses (a for each role) until Jack picks on the voices page.', 'The quote is credited "attributed to Ram Dass" until we find its source.']}
    (cut / 'edl.json').write_text(json.dumps(edl, indent=1, ensure_ascii=False))
    print(json.dumps({'total': total, 'preview': str(cut / 'preview.mp4')}))


if __name__ == '__main__':
    main()
