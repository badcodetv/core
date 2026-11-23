#!/usr/bin/env python3
"""By the Balls (short #18): rough cut from Jack's picked clips, BadCode's line, the picked music and the post labels.

Writes <media>/cut/rN/: one piece per shot (whole frames), vox / music / room stems, the mix, preview.mp4 and edl.json in
the timeline format (scripts/scene/timeline.py), then runs scripts/lipsync/check-cut.py (every voice on its plan, picture
and sound from 0). The voice mix starts with a silent bed from 0 (the 2026-11-23 early-voice bug, docs/rules/voices.md).

    ~/.cache/badcode-lips/venv/bin/python scripts/shorts/btb_cut.py --round 1
"""
# style-lint: story=short-by-the-balls
import argparse, json, pathlib, subprocess, sys
from PIL import Image, ImageDraw, ImageFont

REPO = pathlib.Path(__file__).resolve().parents[2]
SCENE = REPO / 'docs/stories/short-by-the-balls/scenes/by-the-balls'
sys.path.insert(0, str(REPO / 'scripts/drive'))
from localmap import localize  # noqa: E402

cfg = localize(json.loads((SCENE / 'scene.json').read_text()))
MEDIA = pathlib.Path(cfg['media'])
VID, AUD = MEDIA / 'video', MEDIA / 'audio'
LOGO = REPO / 'docs/brand/logo/badcode-stacked-reversed-2400.png'
W, H, FPS = 1080, 1920, 24
CLAMP = 'scale=in_range=full:out_range=limited,format=yuv420p,lutyuv=y=clip(val\\,20\\,235)'
ENC = ['-c:v', 'libx264', '-preset', 'veryfast', '-crf', '18', '-pix_fmt', 'yuv420p', '-color_range', 'tv',
       '-colorspace', 'bt709', '-color_primaries', 'bt709', '-color_trc', 'bt709']
VF = f'scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},fps={FPS}'
BOLD = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
# Jack's picks (clips page, 2026-11-23); music: fm-a; voice: en-gb-csagent-11
MUSIC = AUD / 'music/btb-music-r1-fm-cabinet-attract-loop-v6-w30-ae605d80.wav'
MUS_GAIN, MUS_FADE = -6, 1.2
LINE = ('badcode', 'casting/badcode--en-gb-csagent-11.wav', 1.0, "It was never broken. It was set.")
# Post labels (Flow can't write text). The claw: the owners' names (brief.md); the dial: the land-price rule (Jack, "land price").
CLAW_TAGS = ['BANK', 'LANDLORD', 'ENERGY CO.']
DIAL_TOP, DIAL_LEFT, DIAL_RIGHT = 'LAND PRICE', 'WHAT IT MIGHT\nBE WORTH', "WHAT IT'S\nWORTH"
# (beat, title, clip key, still, in, frames, line at (s into the shot) or None, label, what we see)
SHOTS = [
    ('play', '1. The game', 'PLAYb', 'PLAY', 0.4, 48, None, None, 'The couple at the claw machine'),
    ('grab', '1. The game', 'GRABb', 'GRAB', 0.0, 44, None, 'claw', 'The claw grabs the house (the owners\' names on it)'),
    ('limp', '1. The game', 'LIMPWIDEa', 'LIMPWIDE', 0.0, 44, None, None, 'The claw goes limp; the house drops'),
    ('faces', '1. The game', 'FACESb', 'FACES', 0.0, 44, None, None, 'They deflate'),
    ('badcode', '2. The reveal', 'BADCODEb', 'BADCODE', 0.2, 84, 0.45, None, 'BadCode: "It was never broken. It was set."'),
    ('unlock', '3. The way out', 'UNLOCKc', 'UNLOCK', 0.0, 52, None, None, 'He unlocks the hidden dial'),
    ('dial', '3. The way out', 'DIALb', 'DIAL', 0.3, 66, None, 'dial', 'Everyone turns the land-price dial'),
    ('win', '3. The way out', 'WINc', 'WIN', 0.0, 60, None, None, 'They win the house'),
    ('logo', '4. Logo', None, None, 0, 36, None, None, 'The BadCode logo'),
]


def ff(*a):
    subprocess.run(['ffmpeg', '-nostdin', '-loglevel', 'error', '-y', *map(str, a)], check=True)


def dur(p):
    return float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', str(p)],
                                capture_output=True, text=True, check=True).stdout)


def tag(d, xy, text, size, anchor='mm'):
    f = ImageFont.truetype(BOLD, size)
    box = d.multiline_textbbox(xy, text, font=f, anchor=anchor, align='center')
    d.rounded_rectangle((box[0] - 18, box[1] - 12, box[2] + 18, box[3] + 12), 12, fill=(0, 0, 0, 170))
    d.multiline_text(xy, text, font=f, fill='white', anchor=anchor, align='center')


def label_png(kind, out):
    im = Image.new('RGBA', (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    if kind == 'claw':  # inside the safe box (x 65-930, y 270-1250)
        for i, t in enumerate(CLAW_TAGS):
            tag(d, (W / 2, 330 + i * 78), t, 44)
    else:
        tag(d, (W / 2, 320), DIAL_TOP, 64)
        tag(d, (250, 1160), DIAL_LEFT, 38)
        tag(d, (830, 1160), DIAL_RIGHT, 38)
    im.save(out)


def main():
    ap = argparse.ArgumentParser(); ap.add_argument('--round', type=int, default=1); a = ap.parse_args()
    cut = MEDIA / 'cut' / f'r{a.round}'; cut.mkdir(parents=True, exist_ok=True)
    t, parts, vids, beats, events, room, vox = 0.0, [], [], [], [], [], []
    for n, (bid, title, key, still, cin, fr, line_at, label, see) in enumerate(SHOTS):
        st = round(t, 3); sd = fr / FPS
        pf = cut / f'v{n:02d}-{bid}.mp4'
        if key:
            src = VID / f'by-the-balls-{key}-{still}.mp4'
            if label:
                lp = cut / f'label-{label}.png'; label_png(label, lp)
                ff('-ss', cin, '-i', src, '-loop', 1, '-i', lp, '-filter_complex',
                   f'[0:v]{VF},tpad=stop_mode=clone:stop_duration=4[v];[1]format=rgba,fade=t=in:st=0.25:d=0.3:alpha=1[l];[v][l]overlay=0:0:shortest=1,{CLAMP}',
                   '-frames:v', fr, '-an', *ENC, pf)
            else:
                ff('-ss', cin, '-i', src, '-vf', f'{VF},tpad=stop_mode=clone:stop_duration=4,{CLAMP}', '-frames:v', fr, '-an', *ENC, pf)
            room.append((st, src, cin, sd))
            events.append({'stem': 'amb-room', 't': st, 'dur': sd, 'what': f'{title}: room ({src.name})', 'src': src.name})
        else:
            ff('-f', 'lavfi', '-i', f'color=black:s={W}x{H}:r={FPS}:d={sd}', '-loop', 1, '-i', LOGO, '-filter_complex',
               f"[1]scale=640:-1,format=rgba,fade=t=in:st=0.1:d=0.4:alpha=1[l];[0][l]overlay=(W-w)/2:(H-h)/2:shortest=1,{CLAMP}",
               '-frames:v', fr, *ENC, pf)
        ls = []
        if line_at is not None:
            who, take, tempo, text = LINE
            w = AUD / take; d = round(dur(w) / tempo, 3); lt = round(st + line_at, 3)
            vox.append((lt, w, tempo))
            ls.append({'i': 0, 'who': who, 'name': 'BadCode', 't': lt, 'dur': d, 'text': text, 'by': 'jack'})
            events.append({'stem': 'vox-badcode', 't': lt, 'dur': d, 'what': f'{title}: BadCode', 'src': take})
        parts.append(pf)
        vids.append({'file': str(pf), 'in': cin, 'start': st, 'dur': sd, 'beat': bid, 'source': key or bid, 'looped': False})
        beats.append({'id': bid, 'title': title, 'start': st, 'dur': sd, 'see': see, 'lines': ls})
        t = st + sd
    total = round(t, 3)
    (cut / 'list.txt').write_text(''.join(f"file '{p.name}'\n" for p in parts))
    ff('-f', 'concat', '-safe', '0', '-i', cut / 'list.txt', '-c', 'copy', cut / 'picture.mp4')
    # voice: a silent bed from 0 first, so the stem keeps its lead-in (never drop it: every line would play early)
    ins, fl = [], []
    for k, (at, w, tempo) in enumerate(vox):
        ins += ['-i', w]; ms = int(at * 1000)
        fl.append(f'[{k}]aresample=48000,aformat=channel_layouts=stereo,atempo={tempo},adelay={ms}|{ms}[s{k}]')
    k0 = len(vox); ins += ['-f', 'lavfi', '-t', total, '-i', 'anullsrc=r=48000:cl=stereo']
    fl.append(f"[{k0}][{']['.join(f's{k}' for k in range(len(vox)))}]amix=inputs={len(vox) + 1}:normalize=0,apad=whole_dur={total},atrim=end={total}[o]")
    ff(*ins, '-filter_complex', ';'.join(fl), '-map', '[o]', '-ar', 48000, cut / 'vox-badcode.wav')
    ins, fl = [], []
    for k, (at, s, iin, ilen) in enumerate(room):
        ins += ['-ss', iin, '-t', ilen, '-i', s]; ms = int(at * 1000)
        fl.append(f'[{k}:a]asetpts=PTS-STARTPTS,aresample=48000,aformat=channel_layouts=stereo,afade=t=in:d=0.06,'
                  f'afade=t=out:st={max(0, ilen - 0.08)}:d=0.08,volume=-12dB,adelay={ms}|{ms}[f{k}]')
    k0 = len(room); ins += ['-f', 'lavfi', '-t', total, '-i', 'anullsrc=r=48000:cl=stereo']
    fl.append(f"[{k0}]{''.join(f'[f{k}]' for k in range(len(room)))}amix=inputs={len(room) + 1}:normalize=0,apad=whole_dur={total},atrim=end={total}[o]")
    ff(*ins, '-filter_complex', ';'.join(fl), '-map', '[o]', '-ar', 48000, cut / 'amb-room.wav')
    ff('-i', MUSIC, '-i', cut / 'vox-badcode.wav', '-filter_complex',
       f'[0]aresample=48000,aformat=channel_layouts=stereo,volume={MUS_GAIN}dB,apad=whole_dur={total},atrim=end={total},'
       f'afade=t=out:st={total - MUS_FADE}:d={MUS_FADE}[m];[1]aformat=channel_layouts=stereo[k];'
       '[m][k]sidechaincompress=threshold=0.03:ratio=5:attack=25:release=350:makeup=1[o]', '-map', '[o]', '-ar', 48000, cut / 'mus-arcade.wav')
    events.append({'stem': 'mus-arcade', 't': 0.0, 'dur': total, 'what': "Music: Jack's pick (cabinet attract loop, take 1)", 'src': MUSIC.name})
    audio = [{'track': 'A1', 'name': 'vox-badcode', 'file': str(cut / 'vox-badcode.wav')},
             {'track': 'A2', 'name': 'mus-arcade', 'file': str(cut / 'mus-arcade.wav')},
             {'track': 'A3', 'name': 'amb-room', 'file': str(cut / 'amb-room.wav')}]
    ff(*[x for s in audio for x in ('-i', s['file'])], '-filter_complex',
       '[0][1][2]amix=inputs=3:normalize=0,loudnorm=I=-14:TP=-1.5,alimiter=limit=0.84:level=0[o]', '-map', '[o]', '-ar', 48000, '-ac', 2, cut / 'mix.wav')
    ff('-i', cut / 'picture.mp4', '-i', cut / 'mix.wav', '-map', '0:v', '-map', '1:a', '-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k', '-t', total, cut / 'preview.mp4')
    edl = {'sequence': f'short-by-the-balls-1-by-the-balls-r{a.round}', 'title': 'By the Balls Timeline',
           'heading': f'BadCode Shorts ▲ By the Balls, rough cut {a.round}',
           'intro': 'A young couple can\'t win the house in the claw machine. BadCode: "It was never broken. It was set." He unlocks the hidden dial, and everyone turns the land price down together; the claw holds.',
           'fps': FPS, 'total': total, 'beats': beats, 'video': vids, 'audio': audio, 'events': events,
           'flags': ["Music: Jack's pick (cabinet attract loop, take 1), ducked under BadCode's line.",
                     'Labels added in post (Flow cannot write): the owners on the claw (BANK, LANDLORD, ENERGY CO.) and the dial (LAND PRICE: WHAT IT MIGHT BE WORTH / WHAT IT\'S WORTH). Wording is a draft for Jack.',
                     "The claw's-view fall (LIMPPOV) is being redone (Jack: 'make it fall realistically'); this cut uses the couple's LIMP only.",
                     'Plain logo card at the end; a creative logo outro can follow.']}
    (cut / 'edl.json').write_text(json.dumps(edl, indent=1, ensure_ascii=False))
    chk = subprocess.run([sys.executable, str(REPO / 'scripts/lipsync/check-cut.py'), str(cut / 'edl.json'), str(AUD)])
    print(json.dumps({'total': total, 'preview': str(cut / 'preview.mp4'), 'check': 'ok' if chk.returncode == 0 else 'FAILED'}))


if __name__ == '__main__':
    main()
