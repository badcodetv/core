#!/usr/bin/env python3
"""Voice every line of the second half's sound script in Gemini TTS, one take per line.

Reads scenes/second-half-audio-plan.json (the single source of the words) and writes
clips/second-half/audio/voice/<frame>-<i>-<who>.wav plus voice/takes.json (durations).
One voice per call: the multi-speaker mode drops and swaps lines (docs/ai-studio/README.md).
A take much shorter than its words should be is re-run (one take in five comes back truncated).

Rough-cut casting, Kai to re-cast: the casting tests in the plan are not run yet.

    python3 scripts/gpom/second-half-video/voice.py [frame ...]     # existing takes are kept

CUT 2 (beats 0-18, the `cut2` block) writes to voice2/ and leaves voice/ alone:

    python3 scripts/gpom/second-half-video/voice.py --cut2 --cast   # casting tests -> voice2/casting/
    python3 scripts/gpom/second-half-video/voice.py --cut2 [beat ...]  # every line + the -fx versions

voice2/<beat>-<i>-<who>.wav (beat ids zero-padded: 00, 11b, 14a) plus voice2/takes.json, a list of
{beat, i, who, text, file, duration[, fx][, short]}. Filtered copies keep the dry take beside them:
  * the AI through Maddie's small speaker (beats 11, 11b, 18)      -> <key>-fx.wav
  * Maddie on the bunker's old wall tannoy (beat 14b)               -> <key>-fx.wav
  * the row muffled through the bunker wall: beat 4 is the beat 6 take, and the beat 7 lines are
    reused under beat 8                                             -> 04-0-woman-fx.wav, 08-<i>-<who>-fx.wav
Beat 4's line is not voiced: its note says it is the row's own takes, low-passed.
"""
import json
import os
import re
import pathlib
import shutil
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import shots as S  # noqa: E402

REPO = S.REPO
OUT = S.CLIPS / 'audio' / 'voice'
WORK = pathlib.Path(os.environ['HOME']) / '.cache/badcode-gpom-second-half/voice'
CAST = {'narrator': 'Algenib', 'ai': 'Algenib', 'bot': 'Aoede', 'woman': 'Kore', 'man': 'Fenrir', 'lady': 'Gacrux'}
# The hundred: one voice per take, stacked in the edit.
CROWD = [('Puck', 'Whoa.'), ('Leda', 'Hang on a minute.'), ('Orus', "What's that?"), ('Zephyr', 'Oh my God.')]
WPS = 2.6  # spoken words per second, for the truncation check

plan = json.loads((S.SCENES / 'second-half-audio-plan.json').read_text())
profiles = {v['id']: v['prompt'] for v in plan['voices']}

# ---- cut 2 -------------------------------------------------------------------------------------
OUT2 = S.CLIPS / 'audio' / 'voice2'
# Casting tests run 2026-10-19 (voice2/casting/, casting.json). Nobody listened: picked on length
# sanity (total vs words/WPS, speech-active time, longest silent gap) and on Google's descriptor for
# each voice against the profile. Kai to re-cast by ear.
#   woman: Autonoe. Kore ("firm") fits the brief best on paper, but both its takes put a long unscripted
#          pause mid-line (3.1s, 1.2s; 9.1s / 7.3s for a ~4.6s line). Autonoe came in at 6.5s, no gap
#          over 0.7s, the lowest-pitched of the three. Leda is "youthful", two decades off.
#   man:   Fenrir ("excitable"): 4.6s for a ~4.6s line, an angry burst as the brief asks.
#   lady:  Gacrux ("mature"): 6.8s for ~6.2s, slow and deliberate as the brief asks.
CAST2 = {'ai': 'Algenib', 'bot': 'Aoede', 'woman': 'Autonoe', 'man': 'Fenrir', 'lady': 'Gacrux'}
CASTING = {
    'woman': (['Kore', 'Leda', 'Autonoe'], "Yeah, the world ended. Doesn't mean you get to stop having manners."),
    'man': (['Fenrir', 'Puck', 'Algieba'], "Fuck that. I'm not dying for the thing that killed us all."),
    'lady': (['Gacrux', 'Sulafat', 'Vindemiatrix'],
             "You don't expect us to leave this bunker so you can finish the job, do you?"),
}
# The hundred, one voice per take, stacked in the edit: each phrase of a crowd line gets these voices.
CROWD2 = ['Puck', 'Leda', 'Orus', 'Zephyr', 'Charon', 'Kore']
PAUSE = {'[pause]': 0.6, '[short pause]': 0.4, '[long pause]': 1.2}  # as build-cut-plan.py
SPEAKER_BEATS = {'11', '11b', '18'}  # the AI heard through Maddie's speaker
TANNOY_BEATS = {'14b'}               # Maddie on the wall tannoy
SKIP_BEATS = {'4'}                   # the row's own takes, muffled (made from beat 6, not voiced)


def bkey(beat):
    m = re.match(r'(\d+)(.*)', beat)
    return f'{int(m.group(1)):02d}{m.group(2)}'


def expect(text):
    """Seconds a line should take: words at WPS plus its marked pauses (build-cut-plan.py's rule)."""
    words = len(re.sub(r'\[[^\]]*\]', '', text).split())
    return words, words / WPS + sum(v * text.count(k) for k, v in PAUSE.items())


def phrases(text):
    parts = [p.strip() for p in text.split(' / ')] if ' / ' in text else re.findall(r'[^.?!]+[.?!]', text)
    return [p.strip() for p in parts if p.strip()]


def jobs2(only):
    out = []
    for b in plan['cut2']['beats']:
        if (only and b['id'] not in only) or b['id'] in SKIP_BEATS:
            continue
        for i, ln in enumerate(b['lines']):
            base = dict(beat=b['id'], i=i, who=ln['who'], text=ln['text'])
            if ln['who'] == 'crowd':
                n = 0
                for p in phrases(ln['text']):
                    for _ in range(2):
                        out.append({**base, 'key': f"{bkey(b['id'])}-{i}-crowd{n}", 'text': p,
                                    'voice': CROWD2[n % len(CROWD2)], 'how': None})
                        n += 1
            else:
                out.append({**base, 'key': f"{bkey(b['id'])}-{i}-{ln['who']}", 'voice': CAST2[ln['who']],
                            'how': ln.get('how')})
    return out


def longest_gap(p):
    """Longest run of near-silence inside a take, in seconds (35 dB under its loudest 25 ms)."""
    import numpy as np
    raw = subprocess.run(['ffmpeg', '-loglevel', 'error', '-i', str(p), '-ac', '1', '-ar', '16000', '-f', 's16le', '-'],
                         capture_output=True).stdout
    x = np.frombuffer(raw, np.int16).astype(float) / 32768
    n = len(x) // 400
    if not n:
        return 0.0
    db = 20 * np.log10(np.sqrt((x[:n * 400].reshape(n, 400) ** 2).mean(1)) + 1e-9)
    act = np.where(db > db.max() - 35)[0]
    return float(np.diff(act).max() - 1) * 0.025 if len(act) > 1 else 0.0


def tts(job, wav_out, work):
    """One take with up to three tries. Re-run: a take much shorter than words/WPS + pauses (truncated),
    or one with a silent gap well past its marked pauses (dead air). Returns (duration, status); if all
    three fail, the best try is kept (not short, then least dead air, then longest) and flagged."""
    key, who, text = job['key'], job['who'], job['text']
    words, exp = expect(text)
    (work / f'{key}.txt').write_text(text)
    prof = work / f'{key}.md'
    body = profiles['crowd'] if who == 'crowd' else profiles[who]
    if job.get('how'):
        body += f"\n\n### THIS LINE\n{job['how']}"
    prof.write_text(body)
    tries, last = [], ''
    allow = max(2.0, 2.5 * max([v for k, v in PAUSE.items() if k in text] or [0]))
    for attempt in range(1, 4):
        tmp = work / f'{key}.try{attempt}.wav'
        tmp.unlink(missing_ok=True)
        r = subprocess.run(['uv', 'run', '-q', '--with', 'google-genai', 'python3', str(REPO / 'scripts/aistudio-tts.py'),
                            str(work / f'{key}.txt'), str(tmp), '--profile', str(prof), '--voice', job['voice']],
                           capture_output=True, text=True, env=os.environ)
        if r.returncode or not tmp.exists():
            last = (r.stderr or r.stdout).strip()[-200:]
            continue
        d, gap = duration(tmp), longest_gap(tmp)
        # Short lines ("Whoa.") run long relative to their words; only judge lines of 4+ words.
        short = words >= 4 and d < 0.5 * exp
        tries.append((short, gap, -d, tmp))
        if short:
            last = f'short take {d:.1f}s, expected ~{exp:.1f}s'
        elif gap > allow:
            # The other way round: a [pause] rendered as seconds of dead air (06-0 came back with 6.2s).
            last = f'{gap:.1f}s of dead air (allowed {allow:.1f}s)'
        else:
            shutil.move(str(tmp), wav_out)
            return d, f'ok (attempt {attempt})'
    if tries:
        short, gap, negd, tmp = min(tries)  # not short first, then least dead air, then longest
        shutil.move(str(tmp), wav_out)
        return -negd, ('SHORT' if short else 'DEAD AIR') + f' after 3 tries ({last})'
    return 0, 'FAILED ' + last


FX = {
    # small speaker: telephone band, driven a little into a soft clipper
    'speaker': 'highpass=f=300,highpass=f=300,lowpass=f=3400,lowpass=f=3400,volume=6dB,'
               'asoftclip=type=atan,acrusher=bits=12:mix=0.15,volume=-3dB',
    # old wall tannoy: narrower band, driven, a corridor slap, light crackle mixed in below
    'tannoy': 'highpass=f=500,highpass=f=500,lowpass=f=2800,lowpass=f=2800,volume=8dB,asoftclip=type=tanh,'
              'apad=pad_dur=0.8,aecho=0.8:0.55:70|140:0.3|0.18,volume=-2dB',
    # through the bunker wall: everything above ~600 Hz gone, quieter
    'muffled': 'lowpass=f=600,lowpass=f=600,lowpass=f=600,volume=-12dB',
}


def fx(src, dst, kind):
    if kind == 'tannoy':
        graph = (f"[0:a]{FX['tannoy']}[v];anoisesrc=color=velvet:amplitude=0.05:sample_rate=24000,"
                 f"highpass=f=1500,aformat=channel_layouts=stereo[n];[v][n]amix=inputs=2:duration=first:"
                 f"weights=1 0.35:normalize=0[o]")
        cmd = ['ffmpeg', '-loglevel', 'error', '-y', '-i', str(src), '-filter_complex', graph, '-map', '[o]', str(dst)]
    else:
        cmd = ['ffmpeg', '-loglevel', 'error', '-y', '-i', str(src), '-af', FX[kind], str(dst)]
    subprocess.run(cmd, check=True)


def run2(job):
    wav = OUT2 / f"{job['key']}.wav"
    if wav.exists():
        return {**job, 'duration': duration(wav), 'status': 'kept'}
    d, how = tts(job, wav, WORK / 'cut2')
    return {**job, 'duration': d, 'status': how}


def casting():
    out = OUT2 / 'casting'
    out.mkdir(parents=True, exist_ok=True)
    (WORK / 'casting').mkdir(parents=True, exist_ok=True)
    todo = [{'key': f'{who}-{v}', 'who': who, 'voice': v, 'text': line, 'how': None}
            for who, (voices, line) in CASTING.items() for v in voices]

    def one(job):
        wav = out / f"{job['key']}.wav"
        if wav.exists():
            return job, duration(wav), 'kept'
        d, how = tts(job, wav, WORK / 'casting')
        return job, d, how
    with ThreadPoolExecutor(3) as ex:
        res = list(ex.map(one, todo))
    rows = []
    for job, d, how in res:
        _, exp = expect(job['text'])
        print(f"{job['key']:22s} {d:5.2f}s (expected ~{exp:.1f}s)  {how}")
        rows.append({'who': job['who'], 'voice': job['voice'], 'text': job['text'], 'file': f"casting/{job['key']}.wav",
                     'duration': round(d, 2), 'expected': round(exp, 2), 'status': how})
    (out / 'casting.json').write_text(json.dumps(rows, indent=1, ensure_ascii=False))


def main2(only):
    (WORK / 'cut2').mkdir(parents=True, exist_ok=True)
    OUT2.mkdir(parents=True, exist_ok=True)
    with ThreadPoolExecutor(3) as ex:
        results = list(ex.map(run2, jobs2(only)))
    index = OUT2 / 'takes.json'
    old = {t['file'] or t['fx']: t for t in json.loads(index.read_text())} if index.exists() else {}
    for r in results:
        print(f"{r['key']:24s} {r['duration']:5.2f}s  {r['status']}")
        if not r['duration']:
            continue
        row = {k: r[k] for k in ('beat', 'i', 'who', 'text')} | {
            'file': f"{r['key']}.wav", 'duration': round(r['duration'], 2), 'voice': r['voice']}
        if r['status'].startswith('SHORT'):
            row['short'] = True
        if r['status'].startswith('DEAD AIR'):
            row['deadAir'] = True
        kind = 'speaker' if (r['beat'] in SPEAKER_BEATS and r['who'] == 'ai') else \
               'tannoy' if (r['beat'] in TANNOY_BEATS and r['who'] == 'bot') else None
        if kind:
            fx(OUT2 / row['file'], OUT2 / f"{r['key']}-fx.wav", kind)
            row['fx'] = f"{r['key']}-fx.wav"
            row['fxKind'] = kind
        old[row['file']] = row
    # The row through the wall, made from the dry takes (no new voicing).
    beats = {b['id']: b for b in plan['cut2']['beats']}
    reuse = [('4', 0, '06-0-woman.wav')] + [('8', i, f'07-{i}-{ln["who"]}.wav') for i, ln in enumerate(beats['7']['lines'])]
    for beat, i, src in reuse:
        if not (OUT2 / src).exists():
            continue
        srow = old.get(src, {})
        dst = f'{bkey(beat)}-{i}-{srow.get("who", "woman")}-fx.wav'
        fx(OUT2 / src, OUT2 / dst, 'muffled')
        text = beats[beat]['lines'][0]['text'] if beat == '4' else srow.get('text', '')
        old[dst] = {'beat': beat, 'i': i, 'who': srow.get('who'), 'text': text, 'file': None, 'source': src,
                    'duration': round(duration(OUT2 / dst), 2), 'fx': dst, 'fxKind': 'muffled'}
    order = {b['id']: n for n, b in enumerate(plan['cut2']['beats'])} | {'8': 6.5}
    rows = sorted(old.values(), key=lambda t: (order.get(t['beat'], 99), t['i'], t.get('file') or t['fx']))
    index.write_text(json.dumps(rows, indent=1, ensure_ascii=False))
    print(f'{len(rows)} rows in {index}')


def jobs(only):
    out = []
    for n, shot in plan['shots'].items():
        if only and n not in only:
            continue
        for i, (who, said) in enumerate(shot.get('lines', [])):
            if who == 'crowd':
                for j, (voice, text) in enumerate(CROWD):
                    out.append((f'{int(n):02d}-{i}-crowd{j}', 'crowd', voice, text))
            else:
                out.append((f'{int(n):02d}-{i}-{who}', who, CAST[who], said))
    return out


def duration(p):
    r = subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', str(p)],
                       capture_output=True, text=True)
    return float(r.stdout.strip() or 0)


def run(job):
    key, who, voice, text = job
    wav = OUT / f'{key}.wav'
    words = len(text.split())
    if wav.exists():
        return key, duration(wav), 'kept'
    (WORK / f'{key}.txt').write_text(text)
    prof = WORK / f'{who}.md'
    prof.write_text(profiles['crowd'] if who == 'crowd' else profiles[who])
    last = ''
    for attempt in range(1, 4):
        tmp = WORK / f'{key}.wav'
        r = subprocess.run(['uv', 'run', '-q', '--with', 'google-genai', 'python3', str(REPO / 'scripts/aistudio-tts.py'),
                            str(WORK / f'{key}.txt'), str(tmp), '--profile', str(prof), '--voice', voice],
                           capture_output=True, text=True, env=os.environ)
        if r.returncode or not tmp.exists():
            last = (r.stderr or r.stdout)[-200:]
            continue
        d = duration(tmp)
        # Short lines ("Hello.") run long relative to their words; only judge lines of 4+ words.
        if words >= 4 and d < 0.5 * words / WPS:
            last = f'short take {d:.1f}s for {words} words'
            continue
        shutil.move(str(tmp), wav)
        return key, d, f'ok (attempt {attempt})'
    return key, 0, 'FAILED ' + last


if __name__ == '__main__' and '--cut2' in sys.argv:
    if 'GEMINI_API_KEY' not in os.environ:
        for line in (REPO / '.env').read_text().splitlines():
            if '=' in line and not line.lstrip().startswith('#'):
                k, v = line.split('=', 1)
                os.environ.setdefault(k.strip().removeprefix('export ').strip(), v.strip().strip('"\''))
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    casting() if '--cast' in sys.argv else main2(set(args))
elif __name__ == '__main__':
    OUT.mkdir(parents=True, exist_ok=True)
    WORK.mkdir(parents=True, exist_ok=True)
    todo = jobs(set(sys.argv[1:]))
    with ThreadPoolExecutor(3) as ex:
        results = list(ex.map(run, todo))
    for key, d, how in results:
        print(f'{key:24s} {d:5.2f}s  {how}')
    takes = {k: d for k, d, h in results if d}
    index = OUT / 'takes.json'
    old = json.loads(index.read_text()) if index.exists() else {}
    index.write_text(json.dumps({**old, **takes}, indent=1, sort_keys=True))
