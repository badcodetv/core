#!/usr/bin/env python3
"""Pub Quiz: Democracy: rough cut from the picked clips, the fitted voices (sync/fits.json) and the series' outro.

    python3 scripts/shorts/pqd_sync.py && python3 scripts/shorts/pqd_cut.py [--round N]

Each talking shot starts LEAD s before its voice (cut in at the in-point the fit chose, voice at the fitted tempo).
The quizmaster has no mouth (balaclava), so his lines sit on his clips without fitting. The clips' own audio is
dropped except the whole pub's "Why?!" (the crowd, no line of ours) and the pour. Writes <media>/cut/r<N>/: edl.json
(timeline format), the stems, mix.wav and preview.mp4.
"""
# style-lint: story=short-pub-quiz-democracy
import argparse, json, pathlib, subprocess, sys

REPO = pathlib.Path(__file__).resolve().parents[2]
SCENE = REPO / 'docs/stories/short-pub-quiz-democracy/scenes/pub-quiz-democracy'
sys.path.insert(0, str(REPO / 'scripts/drive'))
from localmap import localize  # noqa: E402

cfg = localize(json.loads((SCENE / 'scene.json').read_text()))
MEDIA = pathlib.Path(cfg['media'])
VID, CAST, SYNC = MEDIA / 'video', MEDIA / 'audio/casting', MEDIA / 'audio/sync'
TXT = {l['key']: l for l in json.loads((REPO / 'docs/stories/short-pub-quiz-democracy/voices/lines/lines.json').read_text())}
PICK = {'quizmaster': 'quizmaster-b', 'tourist': 'tourist-a', 'voter': 'voter-a', 'swiss': 'swiss-a', 'bob': 'bob-1'}
NAMES = {'quizmaster': 'Quizmaster (BadCode)', 'tourist': 'The Florida tourist', 'voter': 'The one-party voter', 'swiss': 'The Swiss bloke', 'bob': 'Bob'}
# The outro: the series' pint pour with the logo printed on the glass, copied from the first Pub Quiz's rough cut 5
# into this short's own folder (Drive syncs projects, so every file a project uses lives inside it).
OUTRO = MEDIA / 'video/outro-pint-logo.mp4'
OUTRO_SOUND = (MEDIA / 'video/outro-pour-sound.mp4', 2.0)  # the pour clip the outro was cut from, at the same in-point
W, H, FPS = 1080, 1920, 24
LEAD, TAIL = 0.30, 0.20
QM_TEMPO = 1.12  # the quizmaster's lines: no mouth to fit, so quicker (rough cut 1, made fast)
OUTRO_D = 3.2
CLAMP = 'scale=in_range=full:out_range=limited,format=yuv420p,lutyuv=y=clip(val\\,20\\,235)'
ENC = ['-c:v', 'libx264', '-preset', 'veryfast', '-crf', '18', '-pix_fmt', 'yuv420p', '-color_range', 'tv',
       '-colorspace', 'bt709', '-color_primaries', 'bt709', '-color_trc', 'bt709']
VF = f'scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},fps={FPS},{CLAMP}'
# (beat, title, clip, clip in-point or None (= from the fit), [line keys], what we see, hold)
SHOTS = [
    ('out', 'The pub', 'pub-quiz-democracy-P00a-P00.mp4', 1.0, [], 'A countryside pub at dusk', 0.8),
    ('q', 'The question', 'pub-quiz-democracy-P01b-P01.mp4', 0.0, ['01-qm-question'], 'The quizmaster asks', 0),
    ('fifth', 'Everyone looks at her', None, None, ['02-tourist-fifth'], 'The table turns to the tourist', 0),
    ('answer', 'The answer', 'pub-quiz-democracy-P01a-P01.mp4', 2.0, ['03-qm-answer'], 'The quizmaster reads the answer', 0),
    ('both', 'So they wanted both?', None, None, ['04-voter-both'], 'The voter, puzzled', 0),
    ('liked', 'I liked both things', None, None, ['05-tourist-liked'], 'The tourist, sincere', 0),
    ('party', 'The whole party', None, None, ['06-voter-like'], 'The voter, firm', 0),
    ('cows', 'Cow horns', None, None, ['07-swiss-cows'], 'The Swiss bloke, calm', 0),
    ('why-we', 'So why can\'t we?', None, None, ['08-bob-why'], 'Bob, deadpan', 0),
    ('bar', 'Comes as a set', None, None, ['09-tourist-crisps', '10-qm-set'], 'The tourist orders; the quizmaster answers', 0),
    ('why', 'Why?!', 'pub-quiz-democracy-P08a-P08.mp4', 0.0, [], 'The whole pub shouts at the quizmaster', 1.3),
]


def ff(*a):
    subprocess.run(['ffmpeg', '-nostdin', '-loglevel', 'error', '-y', *map(str, a)], check=True)


def dur(p):
    return float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', str(p)],
                                capture_output=True, text=True, check=True).stdout)


def take_for(key, fits):
    role = TXT[key]['role']
    if key in fits and fits[key]:
        b = fits[key][0]
        src = CAST / b['take'] if (CAST / b['take']).exists() else SYNC / b['take']
        return src, b
    return CAST / f'{key}--{PICK[role]}.wav', None


def main():
    ap = argparse.ArgumentParser(); ap.add_argument('--round', type=int, default=1); a = ap.parse_args()
    cut = MEDIA / 'cut' / f'r{a.round}'; cut.mkdir(parents=True, exist_ok=True)
    fits = json.loads((SCENE / 'sync/fits.json').read_text())
    t, beats, vids, parts, stems, events, flags, fx = 0.0, [], [], [], {}, [], [], []
    for n, (bid, title, clip, cin, keys, see, hold) in enumerate(SHOTS):
        title = f'{n + 1}. {title}'; st = t; lines = []
        first = None
        lt = st + (LEAD if keys else 0)
        for j, k in enumerate(keys):
            src, b = take_for(k, fits)
            w = cut / f'line-{k}.wav'
            tempo = b['tempo'] if b else (QM_TEMPO if TXT[k]['role'] == 'quizmaster' else 1.0)
            ff('-i', src, '-af', f"silenceremove=start_periods=1:start_threshold=-55dB:start_silence=0.05,atempo={tempo}", w)
            if j == 0 and b:
                first = b
                clip = b['clip']; cin = max(0.0, b['on'] - LEAD)
                lt = st + (b['on'] - cin)
            if k == '10-qm-set':  # no mouth to match: straight in after her line (the clip's own reply comes 2 s later)
                lt += 0.1
            d = round(dur(w), 3); role = TXT[k]['role']
            stems.setdefault(role, []).append((round(lt, 3), w))
            lines.append({'i': j, 'who': role, 'name': NAMES[role], 't': round(lt, 3), 'dur': d, 'text': TXT[k]['text'], 'by': 'claude'})
            events.append({'stem': f'vox-{role}', 't': round(lt, 3), 'dur': d, 'what': f'{title}: {NAMES[role]}', 'src': str(w)})
            lt += d + 0.05
        sd = round((lt - st + TAIL) if keys else hold, 3)
        src = VID / clip
        avail = dur(src) - cin
        if sd > avail:
            flags.append(f'{title}: {clip} runs out ({avail:.1f}s of {sd:.1f}s); held on its last frame')
        pf = cut / f'v{n:02d}-{bid}.mp4'
        ff('-ss', cin, '-i', src, '-t', sd, '-vf', VF + ',tpad=stop_mode=clone:stop_duration=3', '-t', sd, '-an', *ENC, pf)
        parts.append(pf)
        vids.append({'file': str(pf), 'in': round(cin, 3), 'start': round(st, 3), 'dur': sd, 'beat': bid, 'source': str(src), 'looped': False})
        if first:
            flags.append(f"{title}: lip-sync {first['words']} of {first['of']} words in time ({first['clip']}, x{first['tempo']})")
        if bid == 'why':
            fx.append((round(st, 3), src, cin, sd, "The whole pub: \"Why?!\" (the clip's own crowd)"))
            events.append({'stem': 'fx', 't': round(st, 3), 'dur': sd, 'what': 'The whole pub shouts "Why?!" (the clip\'s own sound)', 'src': str(src)})
        beats.append({'id': bid, 'title': title, 'start': round(st, 3), 'dur': sd, 'see': see, 'lines': lines})
        t = st + sd
    # the outro
    od = min(OUTRO_D, dur(OUTRO)); ls = round(t, 3)
    ff('-i', OUTRO, '-t', od, '-vf', VF, '-an', *ENC, cut / 'v99-outro.mp4'); parts.append(cut / 'v99-outro.mp4')
    vids.append({'file': str(cut / 'v99-outro.mp4'), 'in': 0, 'start': ls, 'dur': od, 'beat': 'logo', 'source': str(OUTRO), 'looped': False})
    beats.append({'id': 'logo', 'title': f'{len(SHOTS) + 1}. Outro', 'start': ls, 'dur': od, 'see': 'The pint pour with the logo on the glass (the series outro)', 'lines': []})
    fx.append((ls, OUTRO_SOUND[0], OUTRO_SOUND[1], od, 'The pour'))
    events.append({'stem': 'fx', 't': ls, 'dur': od, 'what': 'Outro: the pour (its own sound)', 'src': str(OUTRO)})
    total = round(ls + od, 3)
    (cut / 'list.txt').write_text(''.join(f"file '{p.name}'\n" for p in parts))
    ff('-f', 'concat', '-safe', '0', '-i', cut / 'list.txt', '-c', 'copy', cut / 'picture.mp4')
    audio = []
    for role, items in stems.items():
        ins, fl = [], []
        for k, (at, w) in enumerate(items):
            ins += ['-i', w]
            fl.append(f'[{k}]aresample=48000,aformat=channel_layouts=stereo,adelay={int(at * 1000)}|{int(at * 1000)},asetpts=N/SR/TB[s{k}]')
        fl.append(f"{''.join(f'[s{k}]' for k in range(len(items)))}amix=inputs={len(items)}:normalize=0,apad=whole_dur={total},atrim=end={total}[o]")
        sp = cut / f'vox-{role}.wav'; ff(*ins, '-filter_complex', ';'.join(fl), '-map', '[o]', '-ar', 48000, sp)
        audio.append({'track': f'A{len(audio) + 1}', 'name': f'vox-{role}', 'file': str(sp)})
    ins, fl = [], []
    for k, (at, src, iin, ilen, _) in enumerate(fx):
        ins += ['-ss', iin, '-t', ilen, '-i', src]
        fl.append(f'[{k}:a]asetpts=PTS-STARTPTS,aresample=48000,aformat=channel_layouts=stereo,afade=t=out:st={max(0, ilen - 0.2)}:d=0.2,'
                  f'adelay={int(at * 1000)}|{int(at * 1000)},asetpts=N/SR/TB[f{k}]')
    fl.append(f"{''.join(f'[f{k}]' for k in range(len(fx)))}amix=inputs={len(fx)}:normalize=0,apad=whole_dur={total},atrim=end={total}[o]")
    sp = cut / 'fx.wav'; ff(*ins, '-filter_complex', ';'.join(fl), '-map', '[o]', '-ar', 48000, sp)
    audio.append({'track': f'A{len(audio) + 1}', 'name': 'fx', 'file': str(sp)})
    ins = sum([['-i', x['file']] for x in audio], [])
    ff(*ins, '-filter_complex', f"{''.join(f'[{k}]' for k in range(len(audio)))}amix=inputs={len(audio)}:normalize=0,loudnorm=I=-14:TP=-1.5,alimiter=limit=0.84:level=0[o]",
       '-map', '[o]', '-ar', 48000, '-ac', 2, cut / 'mix.wav')
    ff('-i', cut / 'picture.mp4', '-i', cut / 'mix.wav', '-map', '0:v', '-map', '1:a', '-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k', '-t', total, cut / 'preview.mp4')
    flags = flags + ['No music or pub room sound yet.']
    edl = {'sequence': f'short-pub-quiz-democracy-1-pub-quiz-democracy-r{a.round}', 'title': 'Pub Quiz Democracy Timeline',
           'heading': f'BadCode Shorts ▲ Pub Quiz: Democracy, rough cut {a.round}',
           'intro': 'The countryside pub, the denim cowboy quizmaster, the new table. Voices fitted to the mouths; no music yet.',
           'fps': FPS, 'total': total, 'beats': beats, 'video': vids, 'audio': audio, 'events': events, 'flags': flags}
    (cut / 'edl.json').write_text(json.dumps(edl, indent=1, ensure_ascii=False))
    print(json.dumps({'total': total, 'preview': str(cut / 'preview.mp4')}))


if __name__ == '__main__':
    main()
