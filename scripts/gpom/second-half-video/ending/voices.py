#!/usr/bin/env python3
"""GPOM second half, the ending (scenes C, D, E): every HUMAN line voiced in Gemini TTS.

Modelled on ../voice3.py and reusing voice.py's TTS call (`V.tts`: truncation / dead-air retry). The AI's
lines are NOT voiced here (Suno, "badcode newsreader"). Reads each scene's scene.json (the single source of
the words) and, per line:

  * the cast's exact voice + prompt (scenes/second-half-cut3-cast.json: lady/woman/man; Maddie = Aoede on
    the audio plan's 'bot' profile), with two changes made in-process only:
      - THE SCENE section is swapped for where this scene happens (the cast prompts say "a tiled lavatory,
        echo off the tiles", which would put bathroom reverb on the downs);
      - the line's `how` goes into DIRECTOR'S NOTES as an 'Emotion for this line:' (voice3 --round A1's rule);
  * a leading "..." is an edit gap (`lead`, 1.2 s), not spoken: the take is voiced without it;
  * two takes (a, b). Each is transcribed by faster-whisper (small.en) and compared with the text.
    If neither take is heard correctly, two more (c, d) are made. The pick is: heard correctly, then not
    flagged by V.tts (short / dead air), then closest transcript, then no long internal silence, then
    duration closest to the words' expected length. The reason is written beside the pick.

E01's "...you go." is not voiced: it is the tail of D16's picked take, filtered to a phone speaker; D16 plays
the head. D16 is voiced as "Mind how... you go." (a hesitation before "you", since a straight read runs "how
you" together) and must have >= SPLIT_MIN s of silence inside; the cut is at that silence's centre (by level:
whisper's word times run words together and always start at 0.0).

Media:   /mnt/d/badcode-videos/gitpush-origin-master/clips/second-half/ending/<C|D|E>/voices/<id>-<t>.wav
Map:     docs/stories/gitpush-origin-master/scenes/<scene>/voices.json  (line id -> chosen file, duration)

    python3 scripts/gpom/second-half-video/ending/voices.py        # existing takes are kept
"""
import difflib
import json
import os
import pathlib
import re
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
import voice as V  # noqa: E402
import voice3 as V3  # noqa: E402

SCENES = V.S.SCENES
CLIPS = pathlib.Path('/mnt/d/badcode-videos/gitpush-origin-master/clips/second-half/ending')
WORK = V.WORK / 'ending'
WHISPER_PY = pathlib.Path(os.environ['HOME']) / '.cache/badcode-whisper/venv/bin/python'
LEAD = 1.2  # a leading "..." = the long pause, as voice3's [long pause]
MATCH = 0.85  # char-level similarity of normalised text vs transcript that counts as "heard correctly"

SCENE_DIRS = {'C': 'second-half-c-walk-out', 'D': 'second-half-d-crossing', 'E': 'second-half-e-ending'}
# Where the line is spoken; replaces the cast prompt's THE SCENE paragraph.
WHERE = {
    'C': "Outside, in the open air. The hundred survivors walk out of the bunker's blast doors into grey "
         "daylight after five years underground, then across wet green chalk downs in Wiltshire towards a long, "
         "low, black glass building. Wind, open sky, no echo; voices close and private amid a crowd walking.",
    'D': "Inside the machine's building: a vast, silent, spotless clean room, white and futuristic, a hundred "
         "people in white suits settling into chairs they know they will not get up from. A soft, dead, hushed "
         "acoustic, no echo; voices close and quiet.",
}
CAST_KEY = {'lady': 'lady', 'sandra': 'woman', 'derek': 'man'}
# Cast-prompt wording that quotes a cut-3 line. Gemini speaks it: Sandra's "a pause before 'Again.'" put an
# unscripted "Again." on the end of both "Five years, one toilet" takes. Removed in-process.
SCRUB = [(", a pause before 'Again.'", '.'), (" ('Kettle's on')", '')]
# A word the takes kept saying as another word (whisper heard "Sit down!" for "Seat down?" on 6 of 8 takes).
# (word, only for this speaker or None, note)
PRON = [('seat', None, "the word is 'seat', as in the toilet seat: a long, clear 'ee'; never 'sit'"),
        # Bristol drops the h: whisper heard "Mind out" (= "watch out") on 3 of 4 takes of "Mind how you go".
        ('how', 'maddie', "say 'how' with a clear, soft h, so it can never be heard as 'out'")]
RETAKES = ['ab', 'cd', 'ef']
SPLIT_WORD = 'you'  # scene.json D16 `split`: cut at the gap before "you"
SPLIT_MIN = 0.2  # seconds of silence a split take must have between its halves  # first pair, then up to two more pairs while no take is heard correctly


def profile(speaker, scene, how, text):
    cast = json.loads(V3.CAST_FILE.read_text())['cast']
    base = V.profiles['bot'] if speaker == 'maddie' else cast[CAST_KEY[speaker]]['prompt']
    voice = 'Aoede' if speaker == 'maddie' else cast[CAST_KEY[speaker]]['voice']
    for a, b in SCRUB:
        base = base.replace(a, b)
    notes = [v for k, who, v in PRON if (who in (None, speaker)) and re.search(rf'\b{k}\b', text.lower())]
    how = '; '.join([how] + notes) if how else '; '.join(notes) or None
    p, n = re.subn(r'(## THE SCENE\n).*?(\n\n###)', lambda m: m.group(1) + WHERE[scene] + m.group(2), base,
                   count=1, flags=re.S)
    assert n == 1, speaker
    return V3.with_emotion(p, how), voice


def norm(s):
    return ' '.join(re.findall(r"[a-z0-9']+", s.lower()))


def collect():
    lines = []
    for sc, d in SCENE_DIRS.items():
        data = json.loads((SCENES / d / 'scene.json').read_text())
        for b in data['beats']:
            for i, ln in enumerate(b.get('lines', [])):
                if ln['speaker'] == 'ai':
                    continue
                lid = f"{b['key']}-{i}-{ln['speaker']}"
                text = ln['text']
                lead = 0.0
                if text.startswith('...'):
                    text, lead = text[3:].lstrip(), LEAD
                if 'split' in ln:
                    # "Mind how you go" runs "how you" together (no gap to cut in: the first cut leaked the
                    # end of "how" into E01, heard as "There you go"). Voiced with a hesitation before the
                    # split word so there is silence to cut in; it plays as her faltering to the empty chairs.
                    text = re.sub(rf'\s+({SPLIT_WORD})\b', r'... \1', text, count=1)
                lines.append({'scene': sc, 'id': lid, 'speaker': ln['speaker'], 'frame': ln.get('frame'),
                              'text': ln['text'], 'spoken': text, 'lead': lead, 'how': ln.get('how'),
                              'derived': 'from' in ln, 'split': 'split' in ln})
    return lines


def take_job(ln, t):
    pkey = f"end-{ln['scene']}-{ln['id']}"
    if pkey not in V.profiles:
        V.profiles[pkey], ln['voice'] = profile(ln['speaker'], ln['scene'], ln['how'], ln['spoken'])
    return {'key': f"{ln['id']}-{t}", 'who': pkey, 'voice': ln['voice'], 'text': ln['spoken'], 'how': None,
            'dir': CLIPS / ln['scene'] / 'voices', 'line': ln}


def run(job):
    wav = job['dir'] / f"{job['key']}.wav"
    if wav.exists():
        return {**job, 'wav': wav, 'duration': V.duration(wav), 'status': 'kept'}
    work = WORK / job['line']['scene']
    work.mkdir(parents=True, exist_ok=True)
    d, how = V.tts(job, wav, work)
    return {**job, 'wav': wav if d else None, 'duration': d, 'status': how}


def whisper(paths):
    if not paths:
        return {}
    r = subprocess.run([str(WHISPER_PY), '-I', str(HERE / 'whisper_words.py'), *map(str, paths)],
                       capture_output=True, text=True, check=True, timeout=900,
                       env={**os.environ, 'HF_HUB_OFFLINE': '1'})  # offline: a hub check once hung 20 min
    return json.loads(r.stdout.strip().splitlines()[-1])


def score(r, heard):
    ln = r['line']
    ratio = difflib.SequenceMatcher(None, norm(ln['spoken']), norm(heard['text'])).ratio() if heard else 0.0
    flagged = r['status'].split()[0] in ('SHORT', 'DEAD', 'FAILED')
    # Word level: an extra or a missing word fails outright; a same-length substitution passes only on the
    # character ratio (accent spellings: 'Oh, ta' for 'Ooh. Ta', 'Mind out you go' for Bristol 'mind 'ow').
    a, b = norm(ln['spoken']).split(), norm(heard['text']).split() if heard else []
    extra = [op for op in difflib.SequenceMatcher(None, a, b).get_opcodes()
             if op[0] in ('insert', 'delete') or (op[0] == 'replace' and op[2] - op[1] != op[4] - op[3])]
    gap = round(V.longest_gap(r['wav']), 2) if r['wav'] else 9.0
    _, exp = V.expect(ln['spoken'])
    words = heard['words'] if heard else []
    sil = silence(r['wav']) if (r['wav'] and ln['split']) else None
    if ln['split'] and (not sil or sil[1] - sil[0] < SPLIT_MIN):
        extra = extra + [('nosplit',)]
    return {'take': r['key'][-1], 'silence': sil, 'file': r['wav'].name if r['wav'] else None, 'duration': round(r['duration'], 2),
            'expected': round(exp, 2), 'status': r['status'], 'heard': heard['text'] if heard else '',
            'match': round(ratio, 3), 'ok': ratio >= MATCH and not flagged and not extra, 'extra': bool(extra), 'flagged': flagged, 'gap': gap,
            'speech': [words[0][1], words[-1][2]] if words else None, 'words': words}


def silence(wav):
    """(start, end) of the longest near-silent run INSIDE the speech (40 dB under the loudest 10 ms)."""
    import numpy as np
    raw = subprocess.run(['ffmpeg', '-loglevel', 'error', '-i', str(wav), '-ac', '1', '-ar', '16000', '-f', 's16le',
                          '-'], capture_output=True).stdout
    x = np.frombuffer(raw, np.int16).astype(float) / 32768
    n = len(x) // 160
    db = 20 * np.log10(np.sqrt((x[:n * 160].reshape(n, 160) ** 2).mean(1)) + 1e-9)
    act = np.where(db > db.max() - 40)[0]
    if len(act) < 2:
        return None
    d = np.diff(act)
    i = int(d.argmax())
    return (round((act[i] + 1) * 0.01, 2), round(act[i + 1] * 0.01, 2)) if d[i] > 1 else None


def pick(takes):
    def key(t):
        return (not t['ok'], t['flagged'], -t['match'], t['gap'] > 0.8, abs(t['duration'] - t['expected']))
    best = min(takes, key=key)
    others = [t for t in takes if t is not best]
    why = []
    if not best['ok']:
        why.append(f"NO take passed the check; best transcript {best['match']:.2f} ('{best['heard']}')")
    for o in others:
        if not o['ok'] and best['ok']:
            why.append(f"{o['take']} failed{' (extra/missing word, or no silence to split in)' if o['extra'] else ''} ('{o['heard']}', {o['match']:.2f}{', ' + o['status'] if o['flagged'] else ''})")
        elif o['match'] < best['match']:
            why.append(f"{o['take']} transcript less exact ({o['match']:.2f} vs {best['match']:.2f}: '{o['heard']}')")
        elif o['gap'] > 0.8 and best['gap'] <= 0.8:
            why.append(f"{o['take']} has a {o['gap']}s silence inside the line")
        else:
            why.append(f"both heard as written; {best['take']} {best['duration']}s is closer to the ~{best['expected']}s "
                       f"the words take than {o['take']} {o['duration']}s")
    return best, f"{best['take']}: " + '; '.join(why)


PHONE = ('highpass=f=380,highpass=f=380,lowpass=f=3000,lowpass=f=3000,volume=6dB,asoftclip=type=atan,'
         'acrusher=bits=10:mix=0.1,volume=-10dB')


def split_d16(ln_d, ln_e, chosen):
    """D16 head ('Mind how') and E01's phone tail ('you go.') from the D16 pick, cut at the gap before 'you'."""
    a, b = chosen['silence']  # whisper's word times start at 0.0 and run words together: cut in the silence
    cut = round((a + b) / 2, 3)
    src = CLIPS / 'D' / 'voices' / chosen['file']
    head = CLIPS / 'D' / 'voices' / f"{ln_d['id']}-head.wav"
    tail_dry = CLIPS / 'E' / 'voices' / f"{ln_e['id']}-dry.wav"
    tail = CLIPS / 'E' / 'voices' / f"{ln_e['id']}-phone.wav"
    tail.parent.mkdir(parents=True, exist_ok=True)
    ff = ['ffmpeg', '-loglevel', 'error', '-y', '-i', str(src)]
    subprocess.run(ff + ['-t', str(cut), '-af', 'afade=t=out:st=%.3f:d=0.03' % (cut - 0.03), str(head)], check=True)
    subprocess.run(ff + ['-ss', str(cut), '-af', 'afade=t=in:d=0.02', str(tail_dry)], check=True)
    subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', '-i', str(tail_dry), '-af', PHONE, str(tail)], check=True)
    return cut, head, tail_dry, tail


def main():
    V3.load_key()
    lines = collect()
    for sc in SCENE_DIRS:
        (CLIPS / sc / 'voices').mkdir(parents=True, exist_ok=True)
    voiced = [ln for ln in lines if not ln['derived']]
    jobs = [take_job(ln, t) for ln in voiced for t in 'ab']
    with ThreadPoolExecutor(3) as ex:
        res = list(ex.map(run, jobs))
    heard = whisper([r['wav'] for r in res if r['wav']])
    scored = {}
    for r in res:
        scored.setdefault(r['line']['id'] + r['line']['scene'], []).append(score(r, heard.get(str(r['wav']))))
    for pair in RETAKES[1:]:  # retake while no take of a line is heard correctly
        redo = [ln for ln in voiced if not any(t['ok'] for t in scored[ln['id'] + ln['scene']])]
        if not redo:
            break
        with ThreadPoolExecutor(3) as ex:
            res2 = list(ex.map(run, [take_job(ln, t) for ln in redo for t in pair]))
        heard2 = whisper([r['wav'] for r in res2 if r['wav']])
        for r in res2:
            scored[r['line']['id'] + r['line']['scene']].append(score(r, heard2.get(str(r['wav']))))

    out = {sc: {} for sc in SCENE_DIRS}
    d16 = None
    for ln in voiced:
        takes = scored[ln['id'] + ln['scene']]
        best, why = pick(takes)
        row = {'speaker': ln['speaker'], 'frame': ln['frame'], 'text': ln['text'], 'voice': ln['voice'],
               'file': f"voices/{best['file']}", 'duration': best['duration'], 'speech': best['speech'],
               'lead': ln['lead'], 'heard': best['heard'], 'verified': best['ok'], 'why': why,
               'takes': [{k: t[k] for k in ('take', 'file', 'duration', 'expected', 'heard', 'match', 'gap', 'status')}
                         for t in takes],
               'prompt': V.profiles[f"end-{ln['scene']}-{ln['id']}"]}
        out[ln['scene']][ln['id']] = row
        if ln['split']:
            d16 = (ln, best)
        print(f"{ln['scene']} {ln['id']:18s} {best['file']:24s} {best['duration']:5.2f}s match {best['match']:.2f} "
              f"{'OK ' if best['ok'] else 'BAD'} | {why}")
    for ln in lines:
        if not ln['derived']:
            continue
        assert d16, 'E01 needs the D16 split take'
        cut, head, tail_dry, tail = split_d16(d16[0], ln, d16[1])
        dd = out['D'][d16[0]['id']]
        dd['split'] = {'cut_at': cut, 'head': f"voices/{head.name}", 'head_duration': round(V.duration(head), 2),
                       'note': "D16 plays the head ('...Mind how'); E01 plays the tail on the phone"}
        out['E'][ln['id']] = {'speaker': ln['speaker'], 'frame': ln['frame'], 'text': ln['text'],
                              'voice': d16[0]['voice'], 'file': f"voices/{tail.name}",
                              'duration': round(V.duration(tail), 2), 'dry': f"voices/{tail_dry.name}",
                              'lead': 0.0, 'fx': 'phone', 'filter': PHONE,
                              'from': f"D {d16[0]['id']} take {d16[1]['take']}, cut at {cut}s (gap before 'you')",
                              'verified': d16[1]['ok'], 'why': 'derived: not voiced separately (scene.json `from`)'}
        print(f"E {ln['id']:18s} {tail.name:24s} {V.duration(tail):5.2f}s  (D16 tail from {cut}s)")
    for sc, d in SCENE_DIRS.items():
        doc = {'about': 'Human lines voiced in Gemini TTS (scripts/gpom/second-half-video/ending/voices.py). '
                        'Files are relative to the media folder; the AI lines are Suno and are not here.',
               'media': str(CLIPS / sc), 'lines': out[sc]}
        (SCENES / d / 'voices.json').write_text(json.dumps(doc, indent=1, ensure_ascii=False) + '\n')
        print(f"wrote {SCENES / d / 'voices.json'} ({len(out[sc])} lines)")


if __name__ == '__main__':
    main()
