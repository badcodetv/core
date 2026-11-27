#!/usr/bin/env python3
"""Camping Story, cut r1: Kai's 42 notes on Jack's '0 synced' cut (2026-11-27), assembled outside Premiere.

    python3 scripts/camping/story-cut-r1.py [--out /mnt/d/badcode-videos/camping-story/timeline/cut-r1]

Words: docs/stories/camping/scenes/story/script-r1.md. New lines are the takes in <timeline>/r1/voices/ (AI Studio,
the locked voices); kept lines are cut at word boundaries out of Jack's voice files (camping jack/narration/), found by
transcribing them (never by the Premiere in-points, which no longer match the files). Picture is Jack's source clips
(new clips/) with a light grade towards his render; every shot still to be made is a dark card saying what goes there.
Timing: a group of shots is as long as its lines need (0.4 s lead, 0.35 s between lines, 0.6 s tail), never shorter
than the shots it replaces; a shot too short for its words plays forward then back (looped). Writes edl.json (the
timeline format, scripts/scene/timeline.py), the stems, mix.wav and preview.mp4.
"""
import argparse, json, os, pathlib, re, subprocess, sys, difflib

ROOT = pathlib.Path('/mnt/d/badcode-videos/camping-story')
JACK = ROOT / 'Camping Video NEW!'
CLIPS, NARR, MUSIC = JACK / 'new clips', JACK / 'camping jack' / 'narration', JACK / 'background music'
NEW = ROOT / 'timeline' / 'r1' / 'voices'
SCENE = pathlib.Path(__file__).resolve().parents[2] / 'docs/stories/camping/scenes/story'
GRADE = 'eq=contrast=1.07:brightness=-0.025:saturation=0.96'
ap = argparse.ArgumentParser(); ap.add_argument('--out', default=str(ROOT / 'timeline' / 'cut-r1'))
a = ap.parse_args(); OUT = pathlib.Path(a.out); (OUT / 'seg').mkdir(parents=True, exist_ok=True)
FPS, W, H = 24, 1920, 1080


def ff(*args):
    subprocess.run(['ffmpeg', '-v', 'error', '-y', *map(str, args)], check=True)


def dur(f):
    return float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', str(f)],
                                capture_output=True, text=True).stdout)


# ---------- words: where each line sits inside its file ----------
WORDS_CACHE = OUT / 'words.json'
words = json.loads(WORDS_CACHE.read_text()) if WORDS_CACHE.exists() else {}


def word_times(f):
    k = str(f)
    if k not in words:
        r = subprocess.run([os.path.expanduser('~/.venvs/whisper/bin/python'), str(pathlib.Path(__file__).parents[1] / 'word_times.py'), k],
                           capture_output=True, text=True, check=True)
        words[k] = json.loads(r.stdout)
        WORDS_CACHE.write_text(json.dumps(words))
    return words[k]


norm = lambda s: re.sub(r'[^a-z0-9 ]', '', s.lower().replace('-', ' ').replace('–', ' ')).split()


def locate(f, phrase):
    """(start, end) seconds of `phrase` inside file f, by the best-matching run of transcribed words."""
    ws = word_times(f)
    toks = [norm(w[2]) for w in ws]
    want = norm(phrase)
    best = (0, None)
    for i in range(len(ws)):
        got = []
        for j in range(i, len(ws)):
            got += toks[j]
            if len(got) >= len(want):
                r = difflib.SequenceMatcher(None, ' '.join(want), ' '.join(got)).ratio()
                if r > best[0]:
                    best = (r, (i, j))
                break
    if not best[1] or best[0] < 0.8:
        sys.exit(f'could not find "{phrase}" in {f} (best {best[0]:.2f})')
    i, j = best[1]
    t0 = max(0.0, ws[i][0] - 0.08) if i == 0 or ws[i][0] - ws[i - 1][1] > 0.16 else (ws[i - 1][1] + ws[i][0]) / 2
    t1 = (min(ws[j][1] + 0.45, dur(f)) if j == len(ws) - 1 else min(ws[j][1] + 0.45, ws[j + 1][0] - 0.05)) if j == len(ws) - 1 or ws[j + 1][0] - ws[j][1] > 0.3 else (ws[j][1] + ws[j + 1][0]) / 2
    return round(t0, 3), round(t1, 3)


SCRIPT_NEW = {i: t for i, _, t, _ in json.loads((NEW / 'lines.json').read_text())}
WHO = {'n': ('narrator', 'Narrator'), 't': ('tarquin', 'Tarquin'), 'b': ('bob', 'Bob')}


def new(lid, at=None):
    f = NEW / f'{lid}.wav'
    ws = word_times(f)
    t0, t1 = max(0, ws[0][0] - 0.06), min(dur(f), ws[-1][1] + 0.45)  # Whisper ends a last word early
    who = WHO[lid.split('-')[1][0]]
    return {'src': f, 'in': t0, 'dur': t1 - t0, 'who': who[0], 'name': who[1], 'text': SCRIPT_NEW[lid], 'by': 'kai', 'at': at, 'new': True}


def kept(rel, phrase, name, at=None):
    f = NARR / rel
    t0, t1 = locate(f, phrase)
    return {'src': f, 'in': t0, 'dur': t1 - t0, 'who': name.lower(), 'name': name, 'text': phrase, 'at': at}


PAUSE = lambda s: {'pause': s}

# ---------- the cut ----------
clip = lambda n, i, d: {'clip': n, 'in': i, 'min': d}
card = lambda text, d=3.0: {'card': text, 'min': d}
black = lambda d: {'black': True, 'min': d}
BEATS = [
    ('0', '🎵 Cue 1 · 2008', '1.wav'), ('1', '🎵 Cue 2 · The last good day', '2.wav'), ('2', '🔇 Silence · the crash', None),
    ('3', '🎵 Cue 3 · The top floor', '3.wav'), ('4', '🎵 Cue 4 · The tent', '4.wav'), ('5', '🎵 Cue 5 · The couch', '5.wav'),
    ('6', '🎵 Cue 6 · Two bays', '6.wav'), ('7', '🎵 Cue 7 · The trip', '7.wav'), ('8', '🎵 Cue 8 · Five years later', '8.wav'),
    ('9', '🎵 Cue 9 · BAD C0DE', '9.wav')]
G = [  # (beat, shots, lines, options)
    ('0', [clip('0', 0, 2.667), card('NEW SHOT · the City of London, pushing in to the NatWest Tower', 3.5)], [new('b0-n1')], {}),
    ('0', [clip('36', 0, 2.417), card('NEW SHOT · trading-floor mania (replaces the lift)')], [new('b0-n2')], {}),
    ('0', [clip('39', 0, 2.333), card('NEW SHOT · trading-floor mania 2 (replaces the empty office)')], [new('b0-n3'), new('b0-n4')], {}),
    ('0', [clip('2', 4.083, 3.917)], [new('b0-n5'), new('b0-n6')], {}),
    ('0', [clip('37', 0, 3.5)], [new('b0-n7')], {}),
    ('1', [clip('4', 0, 1.125), clip('49', 0, 1.792), clip('47', 5.333, 1.958), clip('4', 1.042, 2.292), clip('46', 1.667, 1.542),
           clip('4', 3.333, 2.208), clip('50', 0, 2.083), clip('4', 6.583, 1.417), clip('48', 0, 6.417), clip('47', 3.458, 1.875),
           clip('5', 0, 4.667)],
     [kept('nell-kore-narrator/2.5.wav', 'Bob, a struggling middle manager, decides that driving away from the stress of the economic crash with his wife is a better idea than watching politicians squirm on TV.', 'Narrator', at=0.13),
      kept('bob.wav', 'We had four days booked in Wales, and the tent was already in the boot. She wanted to leave early to miss the traffic. I said there was no rush. A young fool I was.', 'Bob', at=14.25)], {}),
    ('2', [black(0.75), clip('5.5', 0, 4.042)], [], {}),
    ('3', [clip('6.5', 0, 2.708), clip('6.6', 0, 5.0), clip('7', 0, 8.0), clip('8', 2.292, 1.708)],
     [kept('tarquin/2.wav', '2026. I run the largest private equity firm in the country. We buy mouldy old, empty social housing. Easy money, really.', 'Tarquin', at=0.3),
      kept('nell-kore-narrator/3.wav', "He's ditched the tie at least.", 'Narrator', at=13.0)], {}),
    ('3', [clip('9', 0, 5.0)], [kept('tarquin/3.wav', 'You lot are going to have a few more mates out here soon.', 'Tarquin'), new('b3-t1')], {}),
    ('3', [clip('10', 2.417, 2.583), card('NEW SHOT · Tarquin in the car from a second angle, the smile gone')],
     [kept('tarquin/4.wav', 'It is a tad chilly though.', 'Tarquin', at=2.9)], {}),
    ('3', [card('NEW SHOT · the car from outside, at night')], [new('b3-n1')], {}),
    ('4', [clip('12', 0, 6.0)], [new('b4-n1'), PAUSE(1.0), new('b4-b1')], {}),
    ('4', [card('NEW SHOT · the whole Waitrose car park, wide and full of cars (the twin of the ending wide)')], [new('b4-b2')], {}),
    ('4', [clip('14', 1.5, 5.292)], [new('b4-b3')], {}),
    ('5', [clip('15.1', 0, 6.0), clip('15.2', 0, 8.0), clip('15.3', 0, 6.0)], [new('b5-t1'), new('b5-t2'), new('b5-t3')], {}),
    ('6', [clip('17', 0, 6.583)], [new('b6-n1')], {}),
    ('6', [card('NEW SHOT · Bob inside the tent looking out, the wank tank parked in front')], [new('b6-b1'), PAUSE(0.8), new('b6-b2')], {}),
    ('6', [clip('17.1', 0, 8.0)], [new('b6-n2'), PAUSE(0.8), new('b6-n3'), kept('tarquin/8.wav', 'Get a job, you fuckwit.', 'Tarquin')], {}),
    ('6', [clip('20', 0, 1.75)], [kept('tarquin/8.wav', "Even if I give you money, you'll shoot it up your arm.", 'Tarquin')], {}),
    ('6', [clip('19', 0, 4.0)], [kept('bob 2.wav', 'We should have left early. I should have.', 'Bob')], {}),
    ('6', [clip('55', 0.042, 3.5), clip('17', 0, 7.042)], [kept('nell-kore-narrator/4.wav', "Bob's mind is thrown into a tailspin every time he sees those wank tanks, as he calls them.", 'Narrator')], {}),
    ('6', [card('NEW SHOT · Bob just inside the tent, Tarquin by his car looking down at him (the aerial, recut)')], [], {}),
    ('7', [clip('57', 0, 6.333), clip('22', 0, 8.0), clip('23', 3.0, 5.0), clip('24', 0, 4.0), clip('25', 0, 4.167)],
     [kept('nell-kore-narrator/5.wav', 'Tarquin, off to do some spiritual work. With drugs, of course.', 'Narrator', at=0.7),
      kept('tarquin/9.wav', "I cannot bloody meditate and I have never sat on a floor before, what am I, a dog? Oh, that's kicked in alright.", 'Tarquin', at=6.5),
      kept('tarquin/9.wav', "I can't fucking handle this. I would like to go to bed now, please.", 'Tarquin', at=21.1)], {}),
    ('7', [clip('58', 0, 4.125), clip('59', 0, 5.5), clip('64', 0, 5.5), clip('62', 0, 5.5)],
     [kept('nell-kore-narrator/8.wav', "Tarquin thinks he's pleading his innocence before God. It isn't God. I'd know. It's his conscience. First time they've met.", 'Narrator'),
      kept('tarquin/12.wav', 'Please.', 'Tarquin'),
      kept('tarquin/12.wav', "That's not a crime. That's the economy. I did everything right. Good school, good university, good job. And everyone clapped. I didn't crash the bloody market. I just saw it coming. That's not greed. That's foresight.", 'Tarquin')],
     {'xfade': 0.6}),
    ('8', [clip('26', 0, 5.0)], [kept('nell-kore-narrator/5.wav', 'Surprise, surprise, he did not experience an ego death.', 'Narrator')], {}),
    ('8', [clip('27', 0, 3.042)], [new('b8-n1')], {}),
    ('8', [card('NEW SHOT · Tarquin wakes in the tent, very shocked, no beer (re-make of 28)')], [new('b8-t1')], {}),
    ('8', [card('NEW SHOT · re-make of 67 without the beer', 3.125), clip('29', 0, 3.625)], [], {}),
    ('9', [clip('33', 1.292, 6.708), clip('68', 0, 8.0)], [], {}),
]

# ---------- timing ----------
LEAD, GAP, TAIL = 0.4, 0.35, 0.6
t, video, vox, cuts = 0.0, [], [], []
for beat, shots, lines, opt in G:
    pos, end = LEAD, 0.0
    for ln in lines:
        if 'pause' in ln:
            pos += ln['pause'] - GAP
            continue
        ln['rel'] = (max(ln['at'], pos) if end else ln['at']) if ln.get('at') is not None else pos  # never over the line before
        pos = ln['rel'] + ln['dur'] + GAP
        end = ln['rel'] + ln['dur']
    xf = opt.get('xfade', 0)
    need = (end + TAIL) if lines else 0
    have = sum(s['min'] for s in shots) - xf * (len(shots) - 1)
    extra = max(0.0, need - have)
    for s in shots:  # spread the extra time over the shots by their length
        s['dur'] = s['min'] + extra * s['min'] / sum(x['min'] for x in shots)
    gdur = sum(s['dur'] for s in shots) - xf * (len(shots) - 1)
    cuts.append({'beat': beat, 'start': t, 'dur': gdur, 'shots': shots, 'xfade': xf})
    st = t
    for s in shots:
        video.append({'beat': beat, 'start': round(st, 3), 'dur': round(s['dur'], 3), 'shot': s})
        st += s['dur'] - xf
    for ln in lines:
        if 'pause' not in ln:
            vox.append({**ln, 't': round(t + ln['rel'], 3), 'beat': beat})
    t += gdur
TOTAL = round(t, 3)

# ---------- picture ----------
seg_files = []
for k, c in enumerate(cuts):
    parts = []
    for j, s in enumerate(c['shots']):
        f = OUT / 'seg' / f'{k:02d}-{j}.mp4'
        d = s['dur']
        base = f'scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},fps={FPS},setsar=1'
        if 'clip' in s:
            src = CLIPS / f"{s['clip']}.mp4"
            avail = dur(src) - s['in']
            s['looped'] = d > avail + 0.02
            if s['looped']:  # forward then back, as often as needed
                ff('-i', src, '-filter_complex', f"[0:v]trim=start={s['in']},setpts=PTS-STARTPTS,{base},{GRADE},split[a][b];[b]reverse[r];"
                   f"[a][r]concat=n=2:v=1,loop=loop=-1:size=32767,trim=duration={d},setpts=PTS-STARTPTS,format=yuv420p[v]",
                   '-map', '[v]', '-an', '-c:v', 'libx264', '-preset', 'fast', '-crf', '18', f)
            else:
                ff('-ss', s['in'], '-t', d, '-i', src, '-vf', f'{base},{GRADE},format=yuv420p', '-an', '-c:v', 'libx264', '-preset', 'fast', '-crf', '18', f)
        else:
            text = s.get('card', '')
            lines_txt = re.sub(r'(.{1,46})(\s|$)', r'\1\n', text).strip().replace("'", '’').replace(':', '\\:')
            ff('-f', 'lavfi', '-i', f'color=c=0x1b1d22:s={W}x{H}:r={FPS}:d={d}', '-vf',
               (f"drawtext=fontfile=/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf:text='{lines_txt}':fontcolor=0xe9c46a:fontsize=54:"
                f"line_spacing=18:x=(w-text_w)/2:y=(h-text_h)/2,format=yuv420p") if text else 'format=yuv420p',
               '-c:v', 'libx264', '-preset', 'fast', '-crf', '18', f)
        parts.append(f)
    out = OUT / 'seg' / f'{k:02d}.mp4'
    if len(parts) == 1:
        os.replace(parts[0], out)
    elif c['xfade']:
        xf, chain, off, last = c['xfade'], [], 0.0, '0:v'
        for j in range(1, len(parts)):
            off += c['shots'][j - 1]['dur'] - xf
            chain.append(f"[{last}][{j}:v]xfade=transition=fade:duration={xf}:offset={off:.3f}[x{j}]")
            last = f'x{j}'
        ff(*sum([['-i', p] for p in parts], []), '-filter_complex', ';'.join(chain), '-map', f'[{last}]',
           '-c:v', 'libx264', '-preset', 'fast', '-crf', '18', '-pix_fmt', 'yuv420p', out)
    else:
        lst = OUT / 'seg' / f'{k:02d}.txt'
        lst.write_text(''.join(f"file '{p}'\n" for p in parts))
        ff('-f', 'concat', '-safe', '0', '-i', lst, '-c', 'copy', out)
    seg_files.append(out)
(OUT / 'seg' / 'all.txt').write_text(''.join(f"file '{p}'\n" for p in seg_files))
ff('-f', 'concat', '-safe', '0', '-i', OUT / 'seg' / 'all.txt', '-c', 'copy', OUT / 'picture.mp4')

# ---------- sound: one stem per track, all from t=0 ----------
def stem(name, items, loud):
    """items: [(file, in, dur, at, fade_out)]; writes <name>.wav, loudness-matched to `loud` LUFS (None = as is)."""
    path = OUT / f'{name}.wav'
    if not items:
        ff('-f', 'lavfi', '-i', f'anullsrc=r=48000:cl=stereo', '-t', TOTAL, path); return path
    ins, fl = [], []
    for k, (f, i, d, at, fo) in enumerate(items):
        ins += ['-i', f]
        fade = f',afade=t=out:st={max(0, d - fo):.3f}:d={fo}' if fo else ''
        fl.append(f"[{k}:a]atrim=start={i}:duration={d},asetpts=PTS-STARTPTS,aresample=48000,aformat=channel_layouts=stereo{fade},"
                  f"adelay={int(at * 1000)}|{int(at * 1000)}[a{k}]")
    fl.append(''.join(f'[a{k}]' for k in range(len(items))) + f'amix=inputs={len(items)}:normalize=0,apad,atrim=duration={TOTAL}'
              + (f',loudnorm=I={loud}:TP=-2' if loud else '') + '[o]')
    ff(*ins, '-filter_complex', ';'.join(fl), '-map', '[o]', '-ar', '48000', path)
    return path


v_items = [(ln['src'], ln['in'], ln['dur'], ln['t'], 0) for ln in vox]
s_items = [(CLIPS / f"{v['shot']['clip']}.mp4", v['shot']['in'], min(v['dur'], dur(CLIPS / f"{v['shot']['clip']}.mp4") - v['shot']['in']), v['start'], 0.3)
           for v in video if 'clip' in v['shot']]
beat_span = {}
for c in cuts:
    b = beat_span.setdefault(c['beat'], [c['start'], c['start'] + c['dur']])
    b[1] = c['start'] + c['dur']
m_items = []
for bid, title, cue in BEATS:
    if cue and bid in beat_span:
        s0, s1 = beat_span[bid]
        f = MUSIC / cue
        reps = int((s1 - s0) // dur(f)) + 1
        if reps > 1:  # a cue shorter than its beat now: loop it
            lf = OUT / f'loop-{cue}'
            ff('-stream_loop', reps - 1, '-i', f, '-c', 'copy', lf); f = lf
        m_items.append((f, 0, s1 - s0, s0, 1.5))
stems = {'sfx-clip-sound': stem('sfx-clip-sound', s_items, -36), 'vox-voices': stem('vox-voices', v_items, None),
         'mus-score': stem('mus-score', m_items, -29)}
ff('-i', stems['vox-voices'], '-i', stems['mus-score'], '-i', stems['sfx-clip-sound'], '-filter_complex',
   '[0:a][1:a][2:a]amix=inputs=3:normalize=0,loudnorm=I=-16:TP=-1.5[o]', '-map', '[o]', '-ar', '48000', OUT / 'mix.wav')
ff('-i', OUT / 'picture.mp4', '-i', OUT / 'mix.wav', '-map', '0:v', '-map', '1:a',  # limited range, tagged BT.709 (delivery-qc.sh)
   '-vf', "lutyuv=y='16+val*219/255':u='16+val*224/255':v='16+val*224/255'",  # scale's range options were a no-op here '-c:v', 'libx264', '-preset', 'medium', '-crf', '18', '-pix_fmt', 'yuv420p',
   '-color_range', 'tv', '-colorspace', 'bt709', '-color_primaries', 'bt709', '-color_trc', 'bt709', '-c:a', 'aac', '-b:a', '192k',
   '-shortest', '-movflags', '+faststart', OUT / 'preview.mp4')

# ---------- edl ----------
beats = []
for bid, title, cue in BEATS:
    if bid not in beat_span: continue
    s0, s1 = beat_span[bid]
    ls = [x for x in vox if x['beat'] == bid]
    beats.append({'id': bid, 'title': title, 'start': round(s0, 3), 'dur': round(s1 - s0, 3),
                  'see': {'0': 'Kai r1: the 2008 words (CDOs), the treadmill gone, the locksmith moved here.',
                          '3': 'Kai r1: the bonus line, a real cut to the worried face, the narrator bridges to Bob.',
                          '4': "Kai r1: the narrator brings Bob in, Bob answers her; his old speech is gone.",
                          '5': 'Kai r1: the therapy speech shortened.', '6': 'Kai r1: no drive, Bob first from the tent, the insults trimmed.',
                          '7': 'Kai r1: the vortex out, fades between the trip shots.', '8': 'Kai r1: sweet dreams; where the fuck am I.'}.get(bid, ''),
                  'lines': [{'i': k, 't': x['t'], 'dur': round(x['dur'], 3), 'who': x['who'], 'name': x['name'], 'text': x['text'],
                             **({'by': 'kai'} if x.get('new') else {})} for k, x in enumerate(ls)]})
edl = {'sequence': 'camping-story-r1', 'title': 'Camping Story Timeline · r1', 'fps': FPS, 'total': TOTAL, 'beats': beats,
       'video': [{'file': str(CLIPS / f"{v['shot']['clip']}.mp4") if 'clip' in v['shot'] else 'card', 'start': v['start'], 'dur': v['dur'],
                  'beat': v['beat'], 'source': (str(CLIPS / f"{v['shot']['clip']}.mp4") if 'clip' in v['shot'] else
                                                (v['shot'].get('card') or 'black')), 'looped': bool(v['shot'].get('looped'))} for v in video],
       'audio': [{'track': 'A1', 'name': 'sfx-clip-sound'}, {'track': 'A2', 'name': 'vox-voices'}, {'track': 'A3', 'name': 'mus-score'}],
       'events': [{'stem': 'vox-voices', 't': x['t'], 'dur': round(x['dur'], 3), 'what': x['text'][:40], 'src': str(x['src'])} for x in vox]
               + [{'stem': 'sfx-clip-sound', 't': i[3], 'dur': round(i[2], 3), 'what': pathlib.Path(i[0]).name, 'src': str(i[0])} for i in s_items]
               + [{'stem': 'mus-score', 't': round(i[3], 3), 'dur': round(i[2], 3), 'what': pathlib.Path(i[0]).name, 'src': str(i[0])} for i in m_items],
       'flags': ["Cut r1 from Kai's 42 notes, assembled outside Premiere from Jack's source clips with a light grade towards his render "
                 "(Jack's own grade and effects are not in it). Dark cards with yellow words are the new shots still to be made.",
                 'Lines tagged "your words" are new takes in the locked voices; the rest are Jack\'s takes, cut at word boundaries.',
                 'The trip is not yet half as long: the plea still runs nearly whole (only "I only wanted to make money" is out). '
                 'Halving it means cutting its words, which Kai left for next round.']}
(OUT / 'edl.json').write_text(json.dumps(edl, indent=1, ensure_ascii=False))
print(json.dumps({'total': TOTAL, 'groups': len(cuts), 'shots': len(video), 'lines': len(vox), 'out': str(OUT)}))
