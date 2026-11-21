#!/usr/bin/env python3
"""The Forecast: rough cut from the picked clips and the presenter's voice (presenter-b).

    python3 scripts/shorts/forecast_cut.py [--round N]

The presenter is masked (no mouth), so every line is placed by ear. Flow refused every clip of the masked presenter on
the lit news set with a crew around him (the reveal, F02), so the reveal is a slow pull-back on the still F02y.
The clips' own sound runs low. Ends on a plain logo card (placeholder). Writes <media>/cut/r<N>/ in the timeline format.
"""
# style-lint: story=short-the-forecast
import argparse, json, pathlib, subprocess, sys

REPO = pathlib.Path(__file__).resolve().parents[2]
SCENE = REPO / 'docs/stories/short-the-forecast/scenes/the-forecast'
sys.path.insert(0, str(REPO / 'scripts/drive'))
from localmap import localize  # noqa: E402

cfg = localize(json.loads((SCENE / 'scene.json').read_text()))
MEDIA = pathlib.Path(cfg['media'])
VID, CAST, MB = MEDIA / 'video', MEDIA / 'audio/casting', MEDIA / 'moodboard'
TXT = {l['key']: l for l in json.loads((REPO / 'docs/stories/short-the-forecast/voices/lines/lines.json').read_text())}
VOICE = 'presenter-b'
LOGO = REPO / 'docs/brand/logo/badcode-stacked-reversed-2400.png'
W, H, FPS = 1080, 1920, 24
CLAMP = 'scale=in_range=full:out_range=limited,format=yuv420p,lutyuv=y=clip(val\\,20\\,235)'
ENC = ['-c:v', 'libx264', '-preset', 'veryfast', '-crf', '18', '-pix_fmt', 'yuv420p', '-color_range', 'tv',
       '-colorspace', 'bt709', '-color_primaries', 'bt709', '-color_trc', 'bt709']
VF = f'scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},fps={FPS},{CLAMP}'
# (beat, title, source, kind, in, min dur, [(line key, at)], own sound?, what we see)
SHOTS = [
    ('forecast', 'The forecast', 'the-forecast-F01y-F01y.mp4', 'clip', 0.2, 2.6, [('01-forecast', 0.25)], True, 'The presenter at the map'),
    ('reveal', 'The reveal', 'F02y.jpg', 'pullback', 0.0, 3.0, [('02-front', 0.2)], False, 'Pull back: the man with the fan off-set'),
    ('caught', 'Caught', 'the-forecast-F03a-F03.mp4', 'clip', 0.3, 2.4, [('03-continue', 0.5)], True, 'He grins at the camera and keeps blowing'),
    ('tags', 'The way out', 'the-forecast-F04ya-F04y.mp4', 'clip', 0.2, 2.6, [('04-fan', 0.3)], True, 'Every cloud has a name tag'),
    ('turn', 'The button', 'the-forecast-F05yb-F05y.mp4', 'clip', 0.2, 2.8, [], True, 'The fan turned on him'),
    ('logo', 'The logo', None, 'logo', 0.0, 2.4, [], False, 'Logo card (placeholder)'),
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
        for k, at in lines:
            w = cut / f'line-{k}.wav'
            ff('-i', CAST / f'{k}--{VOICE}.wav', '-af', 'silenceremove=start_periods=1:start_threshold=-55dB,areverse,'
               'silenceremove=start_periods=1:start_threshold=-55dB,areverse', w)
            d = round(dur(w), 3); lt = round(st + at, 3)
            vox.append((lt, w))
            ls.append({'i': len(ls), 'who': 'presenter', 'name': 'The presenter (BadCode)', 't': lt, 'dur': d, 'text': TXT[k]['text'], 'by': TXT[k]['by']})
            events.append({'stem': 'vox-presenter', 't': lt, 'dur': d, 'what': f'{title}: the presenter', 'src': str(w)})
            sd = max(sd, round(at + d + 0.35, 3))
        pf = cut / f'v{n:02d}-{bid}.mp4'
        if kind == 'clip':
            s = VID / src
            ff('-ss', cin, '-i', s, '-t', sd, '-vf', VF + ',tpad=stop_mode=clone:stop_duration=4', '-t', sd, '-an', *ENC, pf)
            if own:
                room.append((round(st, 3), s, cin, sd))
                events.append({'stem': 'amb-room', 't': round(st, 3), 'dur': sd, 'what': f"{title}: the clip's own sound", 'src': str(s)})
        elif kind == 'pullback':
            s = MB / src; fr = int(sd * FPS)
            # start tight on the presenter at the map (left third), ease out to the whole frame
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
    ins, fl = [], []
    for k, (at, w) in enumerate(vox):
        ins += ['-i', w]; fl.append(f'[{k}]aresample=48000,aformat=channel_layouts=stereo,adelay={int(at * 1000)}|{int(at * 1000)}[s{k}]')
    fl.append(f"{''.join(f'[s{k}]' for k in range(len(vox)))}amix=inputs={len(vox)}:normalize=0,apad=whole_dur={total},atrim=end={total}[o]")
    sp = cut / 'vox-presenter.wav'; ff(*ins, '-filter_complex', ';'.join(fl), '-map', '[o]', '-ar', 48000, sp)
    audio.append({'track': 'A1', 'name': 'vox-presenter', 'file': str(sp)})
    ins, fl = [], []
    for k, (at, s, iin, ilen) in enumerate(room):
        ins += ['-ss', iin, '-t', ilen, '-i', s]
        fl.append(f'[{k}:a]asetpts=PTS-STARTPTS,aresample=48000,aformat=channel_layouts=stereo,highpass=f=100,'
                  f'afade=t=in:d=0.1,afade=t=out:st={max(0, ilen - 0.15)}:d=0.15,volume=-16dB,adelay={int(at * 1000)}|{int(at * 1000)}[f{k}]')
    fl.append(f"{''.join(f'[f{k}]' for k in range(len(room)))}amix=inputs={len(room)}:normalize=0,apad=whole_dur={total},atrim=end={total}[o]")
    sp = cut / 'amb-room.wav'; ff(*ins, '-filter_complex', ';'.join(fl), '-map', '[o]', '-ar', 48000, sp)
    audio.append({'track': 'A2', 'name': 'amb-room', 'file': str(sp)})
    ins = sum([['-i', x['file']] for x in audio], [])
    ff(*ins, '-filter_complex', f"{''.join(f'[{k}]' for k in range(len(audio)))}amix=inputs={len(audio)}:normalize=0,loudnorm=I=-14:TP=-1.5,alimiter=limit=0.84:level=0[o]",
       '-map', '[o]', '-ar', 48000, '-ac', 2, cut / 'mix.wav')
    ff('-i', cut / 'picture.mp4', '-i', cut / 'mix.wav', '-map', '0:v', '-map', '1:a', '-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k', '-t', total, cut / 'preview.mp4')
    edl = {'sequence': f'short-the-forecast-1-the-forecast-r{a.round}', 'title': 'Forecast Timeline',
           'heading': f'BadCode Shorts ▲ The Forecast, rough cut {a.round}',
           'intro': 'The economy forecast as weather; the camera pulls back to a man blowing the clouds with a desk fan; every cloud gets a name tag; the fan is turned on him.',
           'fps': FPS, 'total': total, 'beats': beats, 'video': vids, 'audio': audio, 'events': events,
           'flags': ['No music yet. Room sound is the clips\' own, low.',
                     'The presenter\'s mask is yellow now: Flow refused every clip of the navy-masked presenter on the news set.',
                     'The reveal is a pull-back on a still: Flow refused every clip of that shot, in either mask.',
                     'The logo is a plain card, a placeholder until we pick a creative logo end.']}
    (cut / 'edl.json').write_text(json.dumps(edl, indent=1, ensure_ascii=False))
    print(json.dumps({'total': total, 'preview': str(cut / 'preview.mp4')}))


if __name__ == '__main__':
    main()
