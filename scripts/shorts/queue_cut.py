#!/usr/bin/env python3
"""The Queue: rough cut from the picked clips, the picked voices and the phone-charging logo (queue_logo.py).

    python3 scripts/shorts/queue_logo.py ... && python3 scripts/shorts/queue_cut.py [--round N]

The pensioner's line sits where her clip's own mouth says it; the cashier has no mouth (balaclava) and the tannoy has
no face, so their lines are placed by ear. A two-tone chime (ffmpeg sine) plays before each tannoy call. The clips'
own room sound runs low under everything except the talking clip. Writes <media>/cut/r<N>/ in the timeline format.
"""
# style-lint: story=short-the-queue
import argparse, json, pathlib, subprocess, sys

REPO = pathlib.Path(__file__).resolve().parents[2]
SCENE = REPO / 'docs/stories/short-the-queue/scenes/the-queue'
sys.path.insert(0, str(REPO / 'scripts/drive'))
from localmap import localize  # noqa: E402

cfg = localize(json.loads((SCENE / 'scene.json').read_text()))
MEDIA = pathlib.Path(cfg['media'])
VID, CAST = MEDIA / 'video', MEDIA / 'audio/casting'
TXT = {l['key']: l for l in json.loads((REPO / 'docs/stories/short-the-queue/voices/lines/lines.json').read_text())}
PICK = {'tannoy': 'tannoy-a', 'pensioner': 'pensioner-b', 'cashier': 'cashier-a'}
NAMES = {'tannoy': 'Tannoy', 'pensioner': 'The pensioner', 'cashier': 'The cashier (BadCode)'}
W, H, FPS = 1080, 1920, 24
CLAMP = 'scale=in_range=full:out_range=limited,format=yuv420p,lutyuv=y=clip(val\\,20\\,235)'
ENC = ['-c:v', 'libx264', '-preset', 'veryfast', '-crf', '18', '-pix_fmt', 'yuv420p', '-color_range', 'tv',
       '-colorspace', 'bt709', '-color_primaries', 'bt709', '-color_trc', 'bt709']
VF = f'scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},fps={FPS},{CLAMP}'
# (beat, title, clip file (in video/ or cut dir), in, dur, [(line key, at seconds into the shot)], room sound?, what we see)
SHOTS = [
    ('queue', 'The queue', 'the-queue-Q01b-Q01.mp4', 0.3, 3.3, [('01-tannoy-three', 0.55)], True, 'A slow queue at the POWER windows'),
    ('barge', 'The push-in', 'the-queue-Q02b-Q02.mp4', 0.6, 3.0, [('02-pensioner-queue', None)], False, 'The machine rolls past the queue'),
    ('cashier', 'Wrong queue', 'the-queue-Q03b-Q03.mp4', 0.4, 2.6, [('03-cashier-wrong', 0.35)], True, 'The cashier looks it up and down'),
    ('closed', 'Position closed', 'the-queue-Q04a-Q04.mp4', 0.2, 2.4, [], True, 'POSITION CLOSED; the machine backs off'),
    ('kettle', 'Households first', 'the-queue-Q05a-Q05.mp4', 0.3, 3.6, [('04-tannoy-households', 0.45)], True, 'The kettle plugs in and boils'),
    ('phone', 'The lad plugs in', 'the-queue-Q06a-Q06.mp4', 0.4, 2.6, [], True, 'The lad on 1% plugs his phone into the machine'),
    ('logo', 'The logo', 'logo-phone.mp4', 0.0, 3.4, [], False, 'The charging ring fills and becomes the BadCode logo'),
]
OWN = {'02-pensioner-queue': 1.9}  # where Q02b's own mouth says the line (transcribed)


def ff(*a):
    subprocess.run(['ffmpeg', '-nostdin', '-loglevel', 'error', '-y', *map(str, a)], check=True)


def dur(p):
    return float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', str(p)],
                                capture_output=True, text=True, check=True).stdout)


def main():
    ap = argparse.ArgumentParser(); ap.add_argument('--round', type=int, default=1); a = ap.parse_args()
    cut = MEDIA / 'cut' / f'r{a.round}'; cut.mkdir(parents=True, exist_ok=True)
    chime = cut / 'chime.wav'
    ff('-f', 'lavfi', '-i', 'sine=f=784:d=0.35', '-f', 'lavfi', '-i', 'sine=f=587:d=0.5', '-filter_complex',
       '[0]afade=t=out:st=0.2:d=0.15,volume=0.35[a];[1]afade=t=out:st=0.3:d=0.2,volume=0.35[b];[a][b]concat=n=2:v=0:a=1[o]', '-map', '[o]', chime)
    t, beats, vids, parts, stems, events, room = 0.0, [], [], [], {}, [], []
    for n, (bid, title, clip, cin, sd, lines, own_sound, see) in enumerate(SHOTS):
        title = f'{n + 1}. {title}'; st = t; ls = []
        src = (cut / clip) if (cut / clip).exists() else VID / clip
        for k, at in lines:
            role = TXT[k]['role']; w = cut / f'line-{k}.wav'
            ff('-i', CAST / f'{k}--{PICK[role]}.wav', '-af', 'silenceremove=start_periods=1:start_threshold=-55dB,areverse,silenceremove=start_periods=1:start_threshold=-55dB,areverse', w)
            lt = st + (OWN[k] - cin if at is None else at)
            if role == 'tannoy':
                stems.setdefault('chime', []).append((round(lt - 0.15, 3), chime)); lt += 0.75
                events.append({'stem': 'fx-chime', 't': round(lt - 0.9, 3), 'dur': 0.85, 'what': f'{title}: the chime', 'src': str(chime)})
            d = round(dur(w), 3)
            stems.setdefault(role, []).append((round(lt, 3), w))
            ls.append({'i': len(ls), 'who': role, 'name': NAMES[role], 't': round(lt, 3), 'dur': d, 'text': TXT[k]['text'], 'by': 'claude'})
            events.append({'stem': f'vox-{role}', 't': round(lt, 3), 'dur': d, 'what': f'{title}: {NAMES[role]}', 'src': str(w)})
            sd = max(sd, round(lt + d + 0.2 - st, 3))
        pf = cut / f'v{n:02d}-{bid}.mp4'
        ff('-ss', cin, '-i', src, '-t', sd, '-vf', VF + ',tpad=stop_mode=clone:stop_duration=4', '-t', sd, '-an', *ENC, pf)
        parts.append(pf); vids.append({'file': str(pf), 'in': cin, 'start': round(st, 3), 'dur': sd, 'beat': bid, 'source': str(src), 'looped': False})
        if own_sound and bid != 'logo':
            room.append((round(st, 3), src, cin, sd))
            events.append({'stem': 'amb-room', 't': round(st, 3), 'dur': sd, 'what': f"{title}: the clip's own room sound", 'src': str(src)})
        beats.append({'id': bid, 'title': title, 'start': round(st, 3), 'dur': sd, 'see': see, 'lines': ls})
        t = st + sd
    total = round(t, 3)
    (cut / 'list.txt').write_text(''.join(f"file '{p.name}'\n" for p in parts))
    ff('-f', 'concat', '-safe', '0', '-i', cut / 'list.txt', '-c', 'copy', cut / 'picture.mp4')
    audio = []
    for role, items in stems.items():
        ins, fl = [], []
        for k, (at, w) in enumerate(items):
            ins += ['-i', w]
            fl.append(f'[{k}]aresample=48000,aformat=channel_layouts=stereo,adelay={int(at * 1000)}|{int(at * 1000)},asetpts=N/SR/TB[s{k}]')
        fl.append(f"{''.join(f'[s{k}]' for k in range(len(items)))}amix=inputs={len(items)}:normalize=0,apad=whole_dur={total},atrim=end={total}[o]")
        name = 'fx-chime' if role == 'chime' else f'vox-{role}'
        sp = cut / f'{name}.wav'; ff(*ins, '-filter_complex', ';'.join(fl), '-map', '[o]', '-ar', 48000, sp)
        audio.append({'track': f'A{len(audio) + 1}', 'name': name, 'file': str(sp)})
    ins, fl = [], []
    for k, (at, src, iin, ilen) in enumerate(room):
        ins += ['-ss', iin, '-t', ilen, '-i', src]
        fl.append(f'[{k}:a]asetpts=PTS-STARTPTS,aresample=48000,aformat=channel_layouts=stereo,highpass=f=120,lowpass=f=6000,'
                  f'afade=t=in:d=0.1,afade=t=out:st={max(0, ilen - 0.15)}:d=0.15,volume=-16dB,adelay={int(at * 1000)}|{int(at * 1000)},asetpts=N/SR/TB[f{k}]')
    fl.append(f"{''.join(f'[f{k}]' for k in range(len(room)))}amix=inputs={len(room)}:normalize=0,apad=whole_dur={total},atrim=end={total}[o]")
    sp = cut / 'amb-room.wav'; ff(*ins, '-filter_complex', ';'.join(fl), '-map', '[o]', '-ar', 48000, sp)
    audio.append({'track': f'A{len(audio) + 1}', 'name': 'amb-room', 'file': str(sp)})
    ins = sum([['-i', x['file']] for x in audio], [])
    ff(*ins, '-filter_complex', f"{''.join(f'[{k}]' for k in range(len(audio)))}amix=inputs={len(audio)}:normalize=0,loudnorm=I=-14:TP=-1.5,alimiter=limit=0.84:level=0[o]",
       '-map', '[o]', '-ar', 48000, '-ac', 2, cut / 'mix.wav')
    ff('-i', cut / 'picture.mp4', '-i', cut / 'mix.wav', '-map', '0:v', '-map', '1:a', '-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k', '-t', total, cut / 'preview.mp4')
    edl = {'sequence': f'short-the-queue-1-the-queue-r{a.round}', 'title': 'The Queue Timeline',
           'heading': f'BadCode Shorts ▲ The Queue, rough cut {a.round}',
           'intro': 'Cashier number three, please: the machine pushes in, the cashier sends it back, households first, and the logo charges up on the lad\'s phone.',
           'fps': FPS, 'total': total, 'beats': beats, 'video': vids, 'audio': audio, 'events': events,
           'flags': ['No music yet. Room sound is the clips\' own, low.', 'Only the pensioner\'s line needs lip-sync; it sits where her clip says it.']}
    (cut / 'edl.json').write_text(json.dumps(edl, indent=1, ensure_ascii=False))
    print(json.dumps({'total': total, 'preview': str(cut / 'preview.mp4')}))


if __name__ == '__main__':
    main()
