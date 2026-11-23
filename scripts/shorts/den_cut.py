#!/usr/bin/env python3
"""The Den: rough cut from Jack's picked clips and the locked voices.

    python3 scripts/shorts/den_cut.py [--round N]

Writes <media>/cut/rN/: one piece per shot (whole frames), the voice stem (each take laid WHOLE at its fitted onset and
tempo: scenes sync/phrasefits.json), a room stem (the silent clips' own sound), the end card, the mix, preview.mp4 and
edl.json in the timeline format (scripts/scene/timeline.py).
"""
# style-lint: story=short-the-den
import argparse, json, pathlib, subprocess, sys
from PIL import Image, ImageDraw, ImageFont

REPO = pathlib.Path(__file__).resolve().parents[2]
SCENE = REPO / 'docs/stories/short-the-den/scenes/the-den'
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
# Jack, 2026-11-23: "the quote is wrong, it should be about government investing going wrong, you showed me the original
# quote please use that" (the pitch's NAO fact). Read at source 2026-11-23 (report PDF, para 8): "only nine out of 108 major
# projects – representing £35 billion (8%) of £432 billion in expenditure – had plans for robust impact evaluation in place".
CARD = ["The National Audit Office looked at £432 billion of the government's biggest projects.",
        "Only 8% had a robust plan to find out if they worked."]
SOURCE = "National Audit Office, Evaluating government spending (HC 860), December 2021"
# line -> (who, take under audio/, tempo, text)
LINES = {
    '01': ('narrator', 'casting/narrator--en-gb-podcaster-2.wav', 1.0, "Next into the den: a government minister, asking for two billion pounds."),
    '02': ('minister', 'lines/02-minister-pitch--b.wav', 1.07, "Two billion pounds. Every teenager in the country, taken round a prison. Scare them straight."),
    '03': ('badcode', 'lines/03-badcode-ask--a.wav', 1.0, "And how will you know it works?"),
    '04': ('minister', 'lines/04-minister-feeling--b.wav', 0.97, "...I've got a good feeling."),
    '05a': ('inv-a', 'casting/inv-a--en-gb-tutor-5.wav', 0.97, "I'm out."),
    '05c': ('inv-c', 'casting/inv-c--en-gb-assistant-5.wav', 0.97, "I'm out."),
    '05d': ('inv-d', 'casting/inv-d--en-gb-assistant-6.wav', 0.97, "I'm out."),
    '06': ('nurse', 'lines-sync/06-nurse--N5-2.wav', 1.02, "One ward. Six months. If readmissions don't fall by a tenth, you stop paying me."),
    '07': ('badcode', 'lines/07-badcode-in--e.wav', 1.0, "I'm in."),
}
NAMES = {'narrator': 'Narrator', 'minister': 'The minister', 'badcode': 'BadCode', 'nurse': 'The nurse',
         'inv-a': 'Investor A', 'inv-c': 'Investor C', 'inv-d': 'Investor D'}
PITCH_IN = 0.69  # r5: 1.042 minus the 0.352 s mix shift; MIN1a, refit 2026-11-23 on the tracked mouth (den_refit.py; r2's 1.68 measured off on the assembled cut)
GLASS = dict(cx=540, cy=820, w=560, fade=0.5)  # the logo's place on the GLASSa window (1080x1920 px)
# Jack, 2026-11-22: "an outro where it goes onto the factory glass and the condensation spells out badcode with the logo"
# Round 5 (2026-11-23): every talking in-point minus 0.352 s, the mix shift they had been fitted against (the nurse's 0.8
# was fitted in planned time and stays). Round 4: the feeling's in-point 2.8 -> 2.9 (a larger in-point shows the mouth EARLIER, so the voice lands later:
# r3 measured it 0.125 s early; the I'm-outs measured +0.083 s late in r3 and stay), and the music bed: Jack's pick piano-a (music r1 picks page), recorded from the player.
MUSIC = AUD / 'music/den-music-r1-lone-piano-clock-v6-w20-ef69e318.wav'
MUS_GAIN, MUS_FADE = -9, 1.5  # dB under the voices before ducking; fade-out at the end (s)
TALK = {'MIN1a', 'MIN2a', 'INVAb', 'INVCa', 'INVDa', 'NURSEc'}  # their own audio is Omni's voice: muted, room laid under
# (beat, title, clip key, still, in, dur, hold-first-frame, [(line, the take FILE's start, s into the shot)], what we see)
# The pitch: the take runs whole from the panel shot; the cut to MIN1a falls in the pause before "Every teenager" (voice
# 2.30 s in, x1.07) and PITCH_IN puts his mouth's "Every" 0.04 s before it; the panel again for "Scare them straight".
# Round 3 (2026-11-23): voices unchanged; talking in-points moved so each mouth opens 0.05 s before its voice (den_refit.py,
# strips by eye: INVAb opens 2.17, INVCa 3.91, INVDa 3.54). The nurse re-voiced plain, no pause tags ("One ward, six
# months.", take N5-2): its phrase gaps match her mouth's ("One" purses at clip 0.97, "Six" 2.46, the p/m of "paying me" 6.5/6.8). Round 1-2 fitted file starts: MIN2a 3.408; INVAb 2.007; INVCa 2.439; INVDa 3.315; NURSEc L-1 0.842 x1.05.
SHOTS = [
    ('stairs', '1. Next into the den', 'STAIRSb', 'STAIRS', 0.0, 6.2, 0, [('01', 0.35)], 'The minister comes down the iron stairs'),
    ('listen', '2. The pitch', 'WIDEa', 'WIDE', 3.0, 2.35, 0, [('02', 0.2)], 'The panel listens: "Two billion pounds."'),
    ('pitch', '2. The pitch', 'MIN1a', 'MIN', PITCH_IN, 2.9, 0, [], 'On the mark, all teeth'),
    ('react', '2. The pitch', 'WIDEa', 'WIDE', 0.5, 1.5, 0, [], 'The panel, over "Scare them straight"'),
    ('ask', '3. How will you know?', 'BCASKa', 'BC', 0.6, 2.6, 0, [('03', 0.15)], 'BadCode leans in'),
    ('feeling', '4. A good feeling', 'MIN2a', 'MIN', 2.548, 2.6, 0, [('04', 0.608)], 'The grin holds'),
    ('outa', '5. I\'m out', 'INVAb', 'INVA', 1.544, 1.5, 0, [('05a', 0.407)], 'Investor A'),
    ('outc', '5. I\'m out', 'INVCa', 'INVC', 3.211, 1.5, 0, [('05c', 0.439)], 'Investor C'),
    ('outd', '5. I\'m out', 'INVDa', 'INVD', 2.92, 1.5, 0, [('05d', 0.415)], 'Investor D'),
    ('nurse', '6. The nurse', 'NURSEc', 'NURSE', 0.8, 7.0, 0, [('06', 0.03)], 'One ward, six months'),
    ('in', '7. I\'m in', 'BCINa', 'BC', 4.0, 3.2, 0, [('07', 1.6)], 'BadCode leans right in'),
    ('card', '8. The evidence', None, None, 0, 5.0, 0, [], 'The National Audit Office finding'),
    ('glass', '9. The logo on the glass', 'GLASSa', 'GLASS', 0.5, 5.0, 0, [], 'The window steams up; the condensation clears in the shape of the BadCode logo'),
]


def ff(*a):
    subprocess.run(['ffmpeg', '-nostdin', '-loglevel', 'error', '-y', *map(str, a)], check=True)


def dur(p):
    return float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', str(p)],
                                capture_output=True, text=True, check=True).stdout)


def card_png(out):
    im = Image.new('RGB', (W, H), 'black'); d = ImageDraw.Draw(im)
    big = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 58)
    small = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 30)

    def wrap(text, font, width):
        out, line = [], ''
        for w in text.split():
            t = (line + ' ' + w).strip()
            if d.textlength(t, font=font) > width and line:
                out.append(line); line = w
            else:
                line = t
        return out + [line]
    y = 620
    for para in CARD:
        for ln in wrap(para, big, 840):
            d.text((W / 2, y), ln, font=big, fill='white', anchor='ma'); y += 76
        y += 50
    for ln in wrap(SOURCE, small, 840):
        d.text((W / 2, y + 30), ln, font=small, fill=(170, 170, 170), anchor='ma'); y += 42
    im.save(out)


def main():
    ap = argparse.ArgumentParser(); ap.add_argument('--round', type=int, default=1); a = ap.parse_args()
    cut = MEDIA / 'cut' / f'r{a.round}'; cut.mkdir(parents=True, exist_ok=True)
    t, parts, vids, beats, vox, room, events = 0.0, [], [], [], [], [], []
    for n, (bid, title, key, still, cin, sd, hold, lines, see) in enumerate(SHOTS):
        st = round(t, 3); fr = round(sd * FPS); sd = fr / FPS
        pf = cut / f'v{n:02d}-{bid}.mp4'
        if key:
            src = VID / f'the-den-{key}-{still}.mp4'
            vf = VF + (f',tpad=start_mode=clone:start_duration={hold}' if hold else '') + f',tpad=stop_mode=clone:stop_duration=4,{CLAMP}'
            if bid == 'glass':
                subprocess.run([str(pathlib.Path.home() / '.cache/badcode-lips/venv/bin/python'), str(REPO / 'scripts/shorts/den_glass_logo.py'),
                                str(src), str(pf), '--in', str(cin), '--dur', str(sd), *[x for k, v in GLASS.items() for x in (f'--{k}', str(v))]], check=True)
            else:
                ff('-ss', cin, '-i', src, '-vf', vf, '-frames:v', fr, '-an', *ENC, pf)
            # room: a silent clip's own sound; under a talking clip, the panel wide's room tone instead
            rs = VID / 'the-den-WIDEa-WIDE.mp4' if key in TALK else src
            rin = 0.3 if key in TALK else cin
            room.append((st, rs, rin, sd))
            events.append({'stem': 'amb-room', 't': st, 'dur': sd, 'what': f"{title}: room ({rs.name})", 'src': rs.name})
        elif bid == 'card':
            png = cut / 'card.png'; card_png(png)
            ff('-loop', 1, '-i', png, '-vf', f'fps={FPS},fade=t=in:st=0:d=0.3,{CLAMP}', '-frames:v', fr, *ENC, pf)
        else:
            ff('-f', 'lavfi', '-i', f'color=black:s={W}x{H}:r={FPS}:d={sd}', '-loop', 1, '-i', LOGO, '-filter_complex',
               f"[1]scale=640:-1,format=rgba,fade=t=in:st=0.15:d=0.4:alpha=1[l];[0][l]overlay=(W-w)/2:(H-h)/2:shortest=1,{CLAMP}",
               '-frames:v', fr, *ENC, pf)
        ls = []
        for k, at in lines:
            who, take, tempo, text = LINES[k]
            w = AUD / take; d = round(dur(w) / tempo, 3); lt = round(st + at, 3)
            vox.append((lt, w, tempo))
            ls.append({'i': len(ls), 'who': who, 'name': NAMES[who], 't': lt, 'dur': d, 'text': text, 'by': 'claude (script agreed by Jack)'})
            events.append({'stem': 'vox', 't': lt, 'dur': d, 'what': f'{title}: {NAMES[who]}', 'src': take})
        parts.append(pf)
        vids.append({'file': str(pf), 'in': cin, 'start': st, 'dur': sd, 'beat': bid, 'source': key or bid, 'looped': False})
        beats.append({'id': bid, 'title': title, 'start': st, 'dur': sd, 'see': see, 'lines': ls})
        t = st + sd
    total = round(t, 3)
    (cut / 'list.txt').write_text(''.join(f"file '{p.name}'\n" for p in parts))
    ff('-f', 'concat', '-safe', '0', '-i', cut / 'list.txt', '-c', 'copy', cut / 'picture.mp4')
    ins, fl = [], []
    for k, (at, w, tempo) in enumerate(vox):
        ins += ['-i', w]; ms = int(at * 1000)
        fl.append(f'[{k}]aresample=48000,aformat=channel_layouts=stereo,atempo={tempo},adelay={ms}|{ms}[s{k}]')
    # 🔴 A silent bed from 0 as the mix's first input (2026-11-23, Jack: "see why the lip syncing is not working"): without it amix
    # started at the earliest line (the narrator, 0.35 s) and the WAV dropped that gap, so EVERY voice in rough cuts 1-3 played
    # 0.35 s early against the picture and the planned times. Measured by cross-correlating each take against vox.wav.
    k0 = len(vox); ins += ['-f', 'lavfi', '-t', total, '-i', 'anullsrc=r=48000:cl=stereo']
    fl.append(f"[{k0}][{']['.join(f's{k}' for k in range(len(vox)))}]amix=inputs={len(vox) + 1}:normalize=0,apad=whole_dur={total},atrim=end={total}[o]")
    ff(*ins, '-filter_complex', ';'.join(fl), '-map', '[o]', '-ar', 48000, cut / 'vox.wav')
    ins, fl = [], []
    for k, (at, s, iin, ilen) in enumerate(room):
        ins += ['-ss', iin, '-t', ilen, '-i', s]; ms = int(at * 1000)
        fl.append(f'[{k}:a]asetpts=PTS-STARTPTS,aresample=48000,aformat=channel_layouts=stereo,afade=t=in:d=0.08,'
                  f'afade=t=out:st={max(0, ilen - 0.12)}:d=0.12,volume=-14dB,adelay={ms}|{ms}[f{k}]')
    fl.append(f"{''.join(f'[f{k}]' for k in range(len(room)))}amix=inputs={len(room)}:normalize=0,apad=whole_dur={total},atrim=end={total}[o]")
    ff(*ins, '-filter_complex', ';'.join(fl), '-map', '[o]', '-ar', 48000, cut / 'amb-room.wav')
    audio = [{'track': 'A1', 'name': 'vox', 'file': str(cut / 'vox.wav')},
             {'track': 'A2', 'name': 'amb-room', 'file': str(cut / 'amb-room.wav')}]
    if MUSIC.exists():  # the bed, ducked under the voices (sidechain on the vox stem), faded out at the end
        ff('-i', MUSIC, '-i', cut / 'vox.wav', '-filter_complex',
           f'[0]aresample=48000,aformat=channel_layouts=stereo,volume={MUS_GAIN}dB,atrim=end={total},'
           f'afade=t=out:st={total - MUS_FADE}:d={MUS_FADE}[m];[1]aformat=channel_layouts=stereo[k];'
           '[m][k]sidechaincompress=threshold=0.03:ratio=5:attack=25:release=350:makeup=1[o]',
           '-map', '[o]', '-ar', 48000, cut / 'mus-bed.wav')
        audio.append({'track': 'A3', 'name': 'mus-bed', 'file': str(cut / 'mus-bed.wav')})
        events.append({'stem': 'mus-bed', 't': 0.0, 'dur': total, 'what': "Music: Jack's pick (piano and clock, take 1)", 'src': MUSIC.name})
    n = len(audio)
    ff(*[x for a in audio for x in ('-i', a['file'])], '-filter_complex',
       f"{''.join(f'[{k}]' for k in range(n))}amix=inputs={n}:normalize=0,loudnorm=I=-14:TP=-1.5,alimiter=limit=0.84:level=0[o]", '-map', '[o]', '-ar', 48000, '-ac', 2, cut / 'mix.wav')
    ff('-i', cut / 'picture.mp4', '-i', cut / 'mix.wav', '-map', '0:v', '-map', '1:a', '-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k', '-t', total, cut / 'preview.mp4')
    edl = {'sequence': f'short-the-den-1-the-den-r{a.round}', 'title': 'The Den Timeline',
           'heading': f'BadCode Shorts ▲ The Den, rough cut {a.round}',
           'intro': 'A TV pitch-show parody: a minister wants £2bn to scare teenagers straight on a good feeling; everyone is out. A nurse offers one ward and the number that proves her wrong; BadCode is in. The evidence closes it.',
           'fps': FPS, 'total': total, 'beats': beats, 'video': vids, 'audio': audio, 'events': events,
           'flags': ["Music: Jack's pick (piano and clock, take 1), ducked under the voices.",
                     'Lip-sync round 3: voices unchanged, each talking clip\'s in-point moved so the mouth opens just before its voice (scripts/shorts/den_refit.py; measured on the assembled cut with row-measure.py).',
                     'End card: the NAO finding (Evaluating government spending, HC 860, Dec 2021), read at source.']}
    (cut / 'edl.json').write_text(json.dumps(edl, indent=1, ensure_ascii=False))
    print(json.dumps({'total': total, 'preview': str(cut / 'preview.mp4')}))


if __name__ == '__main__':
    main()
