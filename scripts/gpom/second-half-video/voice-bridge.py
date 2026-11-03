#!/usr/bin/env python3
"""Voice the GPOM bridge (scene B revived, draft 1G, picked 2 Nov) in Gemini TTS.

Same method as voice3.py's D rounds (whose helpers it imports, so that file is left alone for the
gpom-second-half session): one voice per call, three takes per phrase, whisper-checked, picked by measurement.
The cast and prompts are GPOM's locked ones (sound.md): Maddie = Aoede on the second-half 'bot' profile; the old
lady, Sandra and Derek = scenes/second-half-cut3-cast.json. The line's stage direction (and a leading [tag]) goes
into that call's DIRECTOR'S NOTES as its emotion. [pause] / [beat] / [long pause] are edit gaps, never spoken.
Lines tagged "fx" in script.json get a filtered copy beside the dry pick (voice.py's FX: tannoy, muffled).

    python3 scripts/gpom/second-half-video/voice-bridge.py      # existing takes are kept

    voice3/bridge/<i>-<who>[-p<n>]-<a|b|c>.wav (+ -fx.wav)  +  scenes/second-half-b-the-door/voices-bridge.json
"""
import difflib
import json
import os
import re
import sys
from concurrent.futures import ThreadPoolExecutor

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, 'ending'))
import voice3 as V3  # noqa: E402
import voices as E  # noqa: E402  (whisper + norm)

V = V3.V
RND = 'bridge'
FOLDER = 'second-half-b-the-door'
GAP = {'[pause]': 0.6, '[beat]': 0.6, '[long pause]': 1.2}
SPEAKERS = ('bot', 'lady', 'woman', 'man')
# The script's stage direction is written for the edit; where it says nothing a voice can act, say it here.
EMO = {
    0: 'chirpy and bright, calling out through a megaphone to people behind a steel door',
    3: 'shouting at the door, furious and disbelieving',
    4: 'shouting, furious, with grief in it',
    5: 'caught out; quiet and honest, a small wince',
    6: 'sincere, a genuine question',
    9: 'brisk, a little pleased with herself',
    12: 'cheerful, matter-of-fact, signing off',
    14: 'tired and wry, deadpan; the swear is heartfelt',
    15: 'indignant, from across the room',
    16: 'dry, flat and slow; not agreeing, stating a fact',
}


def phrases(text):
    parts = re.split(r'\s*(\[(?:pause|beat|long pause)\])\s*', text.strip())
    out, gaps = [], [GAP[t] for t in parts[1::2]]
    for ph in parts[0::2]:
        m = re.match(r'\[([^\]]+)\]\s*', ph)
        emo = m.group(1) if m else None
        out.append(((ph[m.end():] if m else ph).strip(), emo))
    return out, gaps


def emotion(direction, tag):
    d = re.sub(r'^[A-Z][a-z]+( lady)?\s*', '', direction or '').strip('() ')
    return '; '.join(x for x in (tag, d) if x) or None


def jobs():
    cast = json.loads(V3.CAST_FILE.read_text())['cast']
    base = {'bot': V.profiles['bot'], **{k: cast[k]['prompt'] for k in ('lady', 'woman', 'man')}}
    voice = {'bot': 'Aoede', **{k: cast[k]['voice'] for k in ('lady', 'woman', 'man')}}
    script = json.loads((V.S.SCENES / FOLDER / 'script.json').read_text())
    out, rows = [], []
    for i, ln in enumerate(script['lines']):
        who = ln['who']
        if who not in SPEAKERS:
            continue
        phs, gaps = phrases(ln['text'])
        row = {'i': i, 'who': who, 'text': ln['text'], 'off': bool(ln.get('off')), 'fx': ln.get('fx'),
               'voice': voice[who], 'phrases': [],
               'gaps': [{'after': p, 'before': p + 1, 'seconds': g} for p, g in enumerate(gaps)]}
        for p, (ph, tag) in enumerate(phs):
            stem = f'{i:02d}-{who}' + (f'-p{p}' if len(phs) > 1 else '')
            pkey = f'{RND}-{stem}'
            emo = '; '.join(x for x in (tag, EMO.get(i)) if x) or emotion(ln.get('direction'), tag)
            V.profiles[pkey] = V3.with_emotion(base[who], emo)  # in-process only
            row['phrases'].append({'p': p, 'text': ph, 'direction': emo, 'prompt': V.profiles[pkey], 'stem': stem})
            out += [{'key': f'{stem}-{t}', 'stem': stem, 'dir': RND, 'who': pkey, 'voice': voice[who], 'text': ph,
                     'target': ph, 'how': None, 'work': V3.WORK3 / RND} for t in 'abc']
        rows.append(row)
    return out, script, rows


def card(f, prompt, voice, why, parent=None, fx=None):
    import subprocess
    cmd = [sys.executable, str(V.S.REPO / 'scripts/provenance/prov.py'), 'card', str(f), '--kind', 'voice',
           '--tool', 'scripts/gpom/second-half-video/voice-bridge.py', '--why', why]
    cmd += ['--engine', 'ffmpeg', '--parent', str(parent), '--setting', f'fx={fx}'] if parent else \
           ['--engine', 'gemini-tts', '--model', 'Gemini TTS', '--prompt', prompt, '--setting', f'voice={voice}']
    subprocess.run(cmd, check=True, capture_output=True)


def main():
    V3.load_key()
    (V3.OUT3 / RND).mkdir(parents=True, exist_ok=True)
    (V3.WORK3 / RND).mkdir(parents=True, exist_ok=True)
    todo, script, rows = jobs()
    with ThreadPoolExecutor(3) as ex:
        res = list(ex.map(V3.run, todo))
    heard = E.whisper([V3.OUT3 / RND / f"{r['key']}.wav" for r in res if r['duration']])
    by = {}
    for r in res:
        f = V3.OUT3 / RND / f"{r['key']}.wav"
        h = heard.get(str(f)) if r['duration'] else None
        ratio = difflib.SequenceMatcher(None, E.norm(r['target']), E.norm(h['text'])).ratio() if h else 0.0
        gap = round(V.longest_gap(f), 2) if r['duration'] else 0.0
        flagged = r['status'].split()[0] in ('SHORT', 'DEAD', 'FAILED')
        t = {'take': r['key'][-1], 'file': f"{RND}/{f.name}", 'spoken': r['text'], 'duration': round(r['duration'], 2),
             'heard': h['text'] if h else '', 'match': round(ratio, 3), 'gap': gap, 'status': r['status'],
             'ok': ratio >= E.MATCH and gap <= 2.0 and not flagged}
        by.setdefault(r['stem'], []).append(t)
    for row in rows:
        for ph in row['phrases']:
            takes = by[ph.pop('stem')]
            ok = [t for t in takes if t['ok']] or takes
            best = min(ok, key=lambda t: (-t['match'], t['gap']))
            ph['pick'], ph['verified'] = best['take'], best['ok']
            ph['takes'] = [{k: v for k, v in t.items() if k != 'ok'} for t in takes]
            if row['fx']:
                src = V3.OUT3 / best['file']
                dst = src.with_name(src.stem + '-fx.wav')
                V.fx(src, dst, row['fx'])
                ph['fx_file'] = f"{RND}/{dst.name}"
            card(V3.OUT3 / best['file'], ph['prompt'], row['voice'], f"bridge line {row['i']} p{ph['p']}: {ph['text']}")
            if row['fx']:
                card(dst, None, None, f"{row['fx']} copy of the pick", parent=V3.OUT3 / best['file'], fx=row['fx'])
            print(f"{row['i']:2d} p{ph['p']} {row['who']:5s} pick {ph['pick']} {best['duration']:5.2f}s gap "
                  f"{best['gap']:4.2f} match {best['match']:.2f}{'' if ph['verified'] else '  UNVERIFIED'}  "
                  f"'{best['heard']}'")
    doc = {'about': f"Scene B bridge lines (draft {script['dialogue']['picked']}), voiced in Gemini TTS by "
                    "scripts/gpom/second-half-video/voice-bridge.py. Files are relative to the media folder. Picked by "
                    "measurement (whisper + longest gap); nobody has listened.",
           'media': str(V3.OUT3), 'source': f'docs/stories/gitpush-origin-master/scenes/{FOLDER}/script.json',
           'dialogue': script['dialogue'], 'lines': rows}
    dst = V.S.SCENES / FOLDER / 'voices-bridge.json'
    dst.write_text(json.dumps(doc, indent=1, ensure_ascii=False) + '\n')
    print(f'wrote {dst}')


if __name__ == '__main__':
    main()
