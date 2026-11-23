#!/usr/bin/env python3
"""The Fredo Job (short #27): rough cut from Jack's locked clips, the crew's four lines, the picked funk take and post labels.

Writes <media>/cut/rN/: one piece per shot (whole frames), vox / music stems, the mix, preview.mp4 and edl.json in the
timeline format (scripts/scene/timeline.py), then runs scripts/lipsync/check-cut.py. The voice stem starts with a silent
bed from 0 (the 2026-11-23 early-voice bug, docs/rules/voices.md).

The music stops dead on the 39p snap zoom (a short wind-down cut from the take itself, made here) and comes back from a
later point of the take when the jar appears, so its own ending lands on the last frame. The take has no stop of its own
at that moment (measured 2026-11-23: no silent gap before its end at 19.5 s).

    python3 scripts/shorts/fj_cut.py --round 1
"""
# style-lint: story=short-fredo-job
import argparse, json, pathlib, subprocess, sys

REPO = pathlib.Path(__file__).resolve().parents[2]
SCENE = REPO / 'docs/stories/short-fredo-job/scenes/fredo-job'
sys.path.insert(0, str(REPO / 'scripts/drive'))
from localmap import localize  # noqa: E402

cfg = localize(json.loads((SCENE / 'scene.json').read_text()))
MEDIA = pathlib.Path(cfg['media'])
VID, AUD = MEDIA / 'video', MEDIA / 'audio'
WORDMARK = REPO / 'docs/brand/logo/badcode-wordmark-2400.png'
W, H, FPS = 1080, 1920, 24
CLAMP = 'scale=in_range=full:out_range=limited,format=yuv420p,lutyuv=y=clip(val\\,30\\,226)'
ENC = ['-c:v', 'libx264', '-preset', 'veryfast', '-crf', '18', '-pix_fmt', 'yuv420p', '-color_range', 'tv',
       '-colorspace', 'bt709', '-color_primaries', 'bt709', '-color_trc', 'bt709']
VF = f'scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},fps={FPS}'
BOLD = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
# Music: Jack's pick (2026-11-23, "this one thanks")
MUSIC = AUD / 'music-r1/fj-sound-r1-hard-funk-v6-w45-311a082b.wav'
MUS_GAIN = -5
STOP_AT, RESUME_FROM = None, 13.35   # STOP_AT = the snap zoom (set from the shots); RESUME_FROM = where the take picks up
# Lines (Claude, Jack 2026-11-23: "you make the lines and do the cut"); takes picked by transcript (a/b), voice en-gb-concierge-10
LINES = {
    'board': ('lines-r1/L1-pitch-b.wav', 0.15, 'Job of the century, lads. Ten p.'),
    'laser': ('lines-r1/L3-butter-a.wav', 0.75, 'Like butter.'),
    'tag': ('lines-r1/L5-twist-a.wav', 1.6, 'It was ten p when we started planning.'),
    'jar': ('lines-r1/L6-wayout-b.wav', 0.2, 'New plan, lads. Savings that keep up with prices.'),
}
# (beat id, title, clip file, in (s), frames, freeze frames at the end, what we see)
SHOTS = [
    ('board', '1. The plan', 'fredo-job-01-r2a-r2-BOARD-b.mp4', 0.3, 78, 0, 'The plan on the wall; the target gets a 10p in red'),
    ('crew', '2. The crew', 'fredo-job-02-r2-CREW-b.mp4', 1.0, 66, 0, 'The four walk out of the smoke'),
    ('laser', '3. The job', 'fredo-job-03-r2-LASER-b.mp4', 4.0, 60, 0, 'Through the lasers to the jar: "Like butter."'),
    ('grab', '4. The prize', 'fredo-job-04-r3-GRAB-b.mp4', 0.4, 48, 12, 'The Freddoo lifted to the light; freeze'),
    ('tag', '5. The twist', 'fredo-job-05-r2b-r3-TAG-a.mp4', 0.5, 98, 0, 'At the counter; snap zoom on the tag: 39p. The music stops dead'),
    ('jar', '6. The way out', 'fredo-job-06-b-r4-WAY-C-b.mp4', 0.3, 94, 0, 'The savings jar beside the price: both count up together'),
    ('snow', '7. Logo', 'fredo-job-07-a-SNOW-street-a.mp4', 0.3, 54, 0, 'The BadCode mark in the snow; the wordmark fades on'),
]
ZOOM_AT = 34   # frames into the tag shot: the snap zoom
TAG_X, TAG_Y = 540, 1458   # the blank label on the jar in the tag shot (1080x1920)


def ff(*a):
    subprocess.run(['ffmpeg', '-nostdin', '-loglevel', 'error', '-y', *map(str, a)], check=True)


def dur(p):
    return float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', str(p)],
                                capture_output=True, text=True, check=True).stdout)


def dt(text, x, y, size, color='white', box='black@0.65', extra=''):
    return (f"drawtext=fontfile={BOLD}:text='{text}':x={x}:y={y}:fontsize={size}:fontcolor={color}"
            f":box=1:boxcolor={box}:boxborderw=18{extra}")


def shot_filter(bid, fr, freeze):
    base = f'{VF},tpad=stop_mode=clone:stop_duration=4'
    if freeze:
        base += f",trim=end_frame={fr - freeze},tpad=stop_mode=clone:stop_duration={freeze / FPS + 0.1}"
    if bid == 'board':   # the target on the plan, marked in red marker, as Ten p is said
        return base + ',' + dt('10p', 850, 700, 104, color='0xd81e1e', box='white@0.0', extra=":enable='gte(t,1.9)'")
    if bid == 'tag':     # the price on the blank label, then the snap zoom onto it (2.6x)
        z, zt = 2.6, ZOOM_AT / FPS
        cw, ch = int(W / z) // 2 * 2, int(H / z) // 2 * 2
        cx, cy = min(max(TAG_X - cw // 2, 0), W - cw), min(max(TAG_Y - ch // 2, 0), H - ch)
        lab = dt('39p', TAG_X - 62, TAG_Y - 40, 64, color='black', box='white@0.0')
        return (f'{base},{lab},split[a][b];[b]crop={cw}:{ch}:{cx}:{cy},scale={W}:{H}[z];'
                f"[a][z]overlay=0:0:enable='gte(t,{zt:.3f})'")
    if bid == 'jar':     # price and savings tick up together, 10p to 39p
        n = "%{eif\\:min(39\\,10+floor(max(0\\,t-0.4)*16))\\:d}p"
        return (base + ',' + dt(f'SAVINGS {n}', 120, 760, 54, color='0xe6e6e6') + ',' + dt(f'PRICE {n}', 600, 760, 54, color='0xe6e6e6'))
    if bid == 'snow':
        return None
    return base


def main():
    ap = argparse.ArgumentParser(); ap.add_argument('--round', type=int, default=1); a = ap.parse_args()
    cut = MEDIA / 'cut' / f'r{a.round}'; cut.mkdir(parents=True, exist_ok=True)
    t, parts, vids, beats, events, vox = 0.0, [], [], [], [], []
    stop_at = resume_at = None
    for n, (bid, title, clip, cin, fr, freeze, see) in enumerate(SHOTS):
        st = round(t, 3); sd = fr / FPS
        pf = cut / f'v{n:02d}-{bid}.mp4'; src = VID / clip
        f = shot_filter(bid, fr, freeze)
        if bid == 'snow':   # the brand wordmark under the mark in the snow (never Flow's letters)
            ff('-ss', cin, '-i', src, '-loop', 1, '-i', WORDMARK, '-filter_complex',
               f'[0:v]{VF},tpad=stop_mode=clone:stop_duration=4[v];[1]scale=640:-1,format=rgba,fade=t=in:st=0.5:d=0.5:alpha=1[l];'
               f'[v][l]overlay=(W-w)/2:1380:shortest=1,{CLAMP}', '-frames:v', fr, '-an', *ENC, pf)
        elif bid == 'jar':  # the counting labels' expression stops the clamp in the same graph applying (YMAX 239): clamp in a second pass
            tmp = cut / f'v{n:02d}-{bid}-labels.mp4'
            ff('-ss', cin, '-i', src, '-filter_complex', f'[0:v]{f}', '-frames:v', fr, '-an', '-c:v', 'libx264', '-crf', '12', '-pix_fmt', 'yuv444p', tmp)
            ff('-i', tmp, '-vf', CLAMP.replace('226', '220'), '-frames:v', fr, '-an', *ENC, pf); tmp.unlink()
        else:
            ff('-ss', cin, '-i', src, '-filter_complex', f'[0:v]{f},{CLAMP}', '-frames:v', fr, '-an', *ENC, pf)
        if bid == 'tag':
            stop_at = round(st + ZOOM_AT / FPS, 3)
        if bid == 'jar':
            resume_at = st
        ls = []
        if bid in LINES:
            take, at, text = LINES[bid]
            w = AUD / take; d = round(dur(w), 3); lt = round(st + at, 3)
            vox.append((lt, w))
            ls.append({'i': 0, 'who': 'crew', 'name': 'The crew', 't': lt, 'dur': d, 'text': text, 'by': 'claude'})
            events.append({'stem': 'vox-crew', 't': lt, 'dur': d, 'what': f'{title}: the crew', 'src': take})
        parts.append(pf)
        vids.append({'file': str(pf), 'in': cin, 'start': st, 'dur': sd, 'beat': bid, 'source': clip, 'looped': False})
        beats.append({'id': bid, 'title': title, 'start': st, 'dur': sd, 'see': see, 'lines': ls})
        t = st + sd
    total = round(t, 3)
    (cut / 'list.txt').write_text(''.join(f"file '{p.name}'\n" for p in parts))
    ff('-f', 'concat', '-safe', '0', '-i', cut / 'list.txt', '-c', 'copy', cut / 'picture.mp4')
    # voice: a silent bed from 0 first, so the stem keeps its lead-in
    ins, fl = [], []
    for k, (at, w) in enumerate(vox):
        ins += ['-i', w]; ms = int(at * 1000)
        fl.append(f'[{k}]aresample=48000,aformat=channel_layouts=stereo,adelay={ms}|{ms}[s{k}]')
    k0 = len(vox); ins += ['-f', 'lavfi', '-t', total, '-i', 'anullsrc=r=48000:cl=stereo']
    fl.append(f"[{k0}][{']['.join(f's{k}' for k in range(len(vox)))}]amix=inputs={len(vox) + 1}:normalize=0,apad=whole_dur={total},atrim=end={total}[o]")
    ff(*ins, '-filter_complex', ';'.join(fl), '-map', '[o]', '-ar', 48000, cut / 'vox-crew.wav')
    # music: the take to the snap zoom, a 0.25 s wind-down (pitched down to a stop), silence under the twist line,
    # then the take again from RESUME_FROM on the jar, its own ending on the last frame
    back = total - resume_at
    ms_r = int(resume_at * 1000); ms_s = int(stop_at * 1000)
    ff('-i', MUSIC, '-i', cut / 'vox-crew.wav', '-filter_complex',
       f'[0]aresample=48000,aformat=channel_layouts=stereo,asplit=3[m0][m1][m2];'
       f'[m0]atrim=0:{stop_at},afade=t=out:st={stop_at - 0.04}:d=0.04[a];'
       f'[m1]atrim={stop_at}:{stop_at + 0.25},asetpts=PTS-STARTPTS,asetrate=48000*0.55,aresample=48000,'
       f'afade=t=out:st=0.2:d=0.25,adelay={ms_s}|{ms_s}[w];'
       f'[m2]atrim={RESUME_FROM}:{RESUME_FROM + back},asetpts=PTS-STARTPTS,afade=t=in:d=0.02,afade=t=out:st={back - 0.3}:d=0.3,'
       f'adelay={ms_r}|{ms_r}[b];'
       f'[a][w][b]amix=inputs=3:normalize=0,volume={MUS_GAIN}dB,apad=whole_dur={total},atrim=end={total}[m];'
       '[1]aformat=channel_layouts=stereo[k];[m][k]sidechaincompress=threshold=0.03:ratio=5:attack=25:release=350:makeup=1[o]',
       '-map', '[o]', '-ar', 48000, cut / 'mus-funk.wav')
    events.append({'stem': 'mus-funk', 't': 0.0, 'dur': stop_at, 'what': "Music: Jack's pick (hard funk, take 2), to the snap zoom", 'src': MUSIC.name})
    events.append({'stem': 'mus-funk', 't': stop_at, 'dur': 0.45, 'what': 'Wind-down: the music stops dead on 39p', 'src': MUSIC.name})
    events.append({'stem': 'mus-funk', 't': resume_at, 'dur': back, 'what': f'Music back on the jar (from {RESUME_FROM}s of the take)', 'src': MUSIC.name})
    audio = [{'track': 'A1', 'name': 'vox-crew', 'file': str(cut / 'vox-crew.wav')},
             {'track': 'A2', 'name': 'mus-funk', 'file': str(cut / 'mus-funk.wav')}]
    ff(*[x for s in audio for x in ('-i', s['file'])], '-filter_complex',
       '[0][1]amix=inputs=2:normalize=0,loudnorm=I=-14:TP=-1.5,alimiter=limit=0.84:level=0[o]', '-map', '[o]', '-ar', 48000, '-ac', 2, cut / 'mix.wav')
    ff('-i', cut / 'picture.mp4', '-i', cut / 'mix.wav', '-map', '0:v', '-map', '1:a', '-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k', '-t', total, cut / 'preview.mp4')
    edl = {'sequence': f'short-fredo-job-1-fredo-job-r{a.round}', 'title': 'The Fredo Job Timeline',
           'heading': f'BadCode Shorts ▲ The Fredo Job, rough cut {a.round}',
           'intro': 'A crew in BadCode balaclavas pulls the job of the century on a 10p Freddoo. At the counter it is 39p. The way out: savings that keep up with prices.',
           'fps': FPS, 'total': total, 'beats': beats, 'video': vids, 'audio': audio, 'events': events,
           'flags': ['Lines by Claude (Jack: "you make the lines and do the cut"), one voice for the crew (en-gb-concierge-10). Takes picked by transcript: L1 b, L3 a, L5 a, L6 b.',
                     "Music: Jack's pick (hard funk, take 2). The take has no stop of its own at the twist, so the cut makes one: a short pitched-down wind-down on the snap zoom, silence under the twist line, then the take again from 13.35 s on the jar.",
                     'Labels added in post (Flow cannot write): 10p in red on the plan, 39p on the jar label, SAVINGS and PRICE counting 10p to 39p together on the jars. Placement is by eye from contact sheets; wording is a draft.',
                     'Snow: the brand wordmark (docs/brand/logo/badcode-wordmark-2400.png) laid under the mark in the snow.',
                     'Not covered yet: faint maker script at the top of some wrappers (clip 4), from the clips round.']}
    (cut / 'edl.json').write_text(json.dumps(edl, indent=1, ensure_ascii=False))
    chk = subprocess.run([sys.executable, str(REPO / 'scripts/lipsync/check-cut.py'), str(cut / 'edl.json'), str(AUD)])
    print(json.dumps({'total': total, 'preview': str(cut / 'preview.mp4'), 'check': 'ok' if chk.returncode == 0 else 'FAILED'}))


if __name__ == '__main__':
    main()
