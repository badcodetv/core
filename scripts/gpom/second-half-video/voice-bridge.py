#!/usr/bin/env python3
"""Voice the GPOM bridge (scene B revived, draft 1G, picked 2 Nov) in Gemini TTS.

Same method as voice3.py's D rounds (whose helpers it imports, so that file is left alone for the
gpom-second-half session): one voice per call, three takes per phrase, whisper-checked, picked by measurement.
The cast and prompts are GPOM's locked ones (sound.md): Maddie = Aoede on the second-half 'bot' profile; the old
lady, Sandra and Derek = scenes/second-half-cut3-cast.json. The line's stage direction (and a leading [tag]) goes
into that call's DIRECTOR'S NOTES as its emotion. [pause] / [beat] / [long pause] are edit gaps, never spoken.
Lines tagged "fx" in script.json get a filtered copy beside the dry pick (voice.py's FX: tannoy, muffled).

    python3 scripts/gpom/second-half-video/voice-bridge.py      # existing takes are kept
    python3 scripts/gpom/second-half-video/voice-bridge.py --round 2   # Kai's timeline r1 words: unchanged phrases
        reuse the previous round's picks; the old lady is auditioned in three voices (LADY_AUDITION) -> voices-bridge2.json

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
ROUND = int(sys.argv[sys.argv.index('--round') + 1]) if '--round' in sys.argv else 1
GAP = {'[pause]': 0.6, '[beat]': 0.6, '[long pause]': 1.2}
SPEAKERS = ('bot', 'lady', 'woman', 'man')
# The script's stage direction is written for the edit; where it says nothing a voice can act, say it here.
EMO = {  # keyed by the line's opening words, so it survives lines moving
    'Hey, humans': 'chirpy and bright, calling out through a megaphone to people behind a steel door',
    # Kai 4 Nov (timeline r2): "she sounds like she's in charge of a children's birthday party... coy and apologetic"
    'Hello there': 'coy and apologetic, a little awkward, softly sorry to intrude; hesitant, not bright, not a performer',
    # Kai 4 Nov: "the voice that says Derek go and see what that was is the perfect voice for the old lady"
    'We do have': 'brisk, a quiet plain statement to the people around her, the same voice as a quiet order; quick',
    # Kai 4 Nov (timeline r4): "it kind of tails off rather than lands... should be a bit of a joke... more sincerely"
    '...And everything': 'the punchline of a joke, said sincerely and straight-faced, every word clear and landing firmly; '
                         'not mumbled, not trailing off, not sheepish',
    'Are you literally': 'shouting at the door, furious and disbelieving',
    'You killed': 'shouting, furious, with grief in it',
    'Yeah. [pause]': 'caught out; quiet and honest, a small wince',
    'How can we': 'sincere, a genuine question',
    'Oh, and': 'brisk, a little pleased with herself',
    'Right. I': 'cheerful, matter-of-fact, signing off',
    'If there': 'quick and wry, deadpan, all in one breath with no pause',
    'Oi.': 'indignant protest, wounded and outraged, like a man accused of leaving the toilet seat up',
    'Well. [pause]': 'dry, flat and slow; not agreeing, stating a fact',
    'Derek, go': 'brisk, a quiet order, turning to him',
    # Kai 11 Nov (bridge script page r1): "definitely emotion and surprise in Derek's voice"
    "They've blown": 'shocked and emotional, real surprise, almost a laugh of disbelief, peering through a periscope'
                     if ROUND >= 7 else 'quietly stunned, half to himself, peering through a periscope',
    # round 7 (Kai 11 Nov, draft 1D)
    'You mean': 'flat and quiet, a statement not a question; the penny dropping as she takes in what the robot just admitted',
    "Yeah, we're": 'sincere, a little ashamed, genuinely sorry; not performing',
    "I'll tell you": 'a thought arriving, a little brighter; decisive',
    'Look. I understand': 'gentle and plain, owning it; no pleading',
    # Round 9 (Kai, timeline r11 at1729): it must sound like her report line, so it takes the report's direction
    'Hey, boss, are': ('reporting quietly to her boss on the radio, checking he is on the line; tired, hopeful, a bit unsure; '
                       'not for anyone else to hear') if ROUND >= 9 else
                      'quiet, a private radio call to her boss as she rolls away, checking he is on the line; casual, a little tired',
    "I've given them": 'reporting quietly to her boss on the radio; tired, hopeful, a bit unsure; not for anyone else to hear',
    'Hey, boss': 'quiet, a private radio call to her boss as she rolls away; tired, hopeful, a bit unsure; not for anyone else to hear',
    'We know we': 'brisk and matter-of-fact, quick, no long pauses; the practical one',
}


def emo_for(text):
    return next((v for k, v in EMO.items() if text.startswith(k)), None)


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


if ROUND > 1:
    RND = f'bridge{ROUND}'
PREV = 'voices-bridge.json' if ROUND <= 2 else f'voices-bridge{ROUND - 1}.json'
# round 3 (Kai's timeline r2 notes, 4 Nov): Maddie's opening re-voiced coy; the old lady's shorter vote line in her 'Derek' voice
DOC = 'voices-bridge.json' if ROUND == 1 else f'voices-bridge{ROUND}.json'
# Kai 3 Nov (timeline r1): "the old lady's got really posh to the extent where she's a bit annoying... a different
# voice". Three auditions, the same four-part prompt with the accent and register changed; Kai picks by ear.
LADY_AUDITION = [
    ('Gacrux', "West Country, as heard in rural Wiltshire; warm but dry, not posh. Never American, never Received Pronunciation",
     'a Wiltshire farmer\'s widow in her seventies'),
    ('Vindemiatrix', "Northern English, as heard in Yorkshire, around Sheffield; plain-spoken, not posh. Never American, never Received Pronunciation",
     'a retired Sheffield school dinner lady in her seventies'),
    ('Callirrhoe', "Midlands English, as heard in Birmingham; down to earth, not posh. Never American, never Received Pronunciation",
     'a retired Birmingham shopkeeper in her seventies'),
]


def lady_profile(who):
    return ("# AUDIO PROFILE\n" f"The old lady, {who}: the one the hundred survivors listen to.\n\n"
            "## THE SCENE\nA Cold War bunker under a Wiltshire hill, five years underground with a hundred people. "
            "A robot that works for the machine that killed everyone is at the door.\n\n"
            "### DIRECTOR'S NOTES\nStyle: dry, flat and practical; deeply suspicious; nobody's fool, never theatrical.\n"
            "Pace: brisk; no long pauses.\nAccent: {acc}.\n\n### SAMPLE CONTEXT\n"
            "The voice you'd cast as the nan in a British drama who everyone secretly does what she says.")


# Round 2 filters (Kai 3 Nov: "the static is far too loud... it overwhelms Maddie's speech"; "we need to hear the old
# lady say you killed everybody... it's far too muffled"): the tannoy without voice.py's crackle and a little wider, so
# the words sit on top; the door muffle much lighter.
FX2 = {
    'tannoy': 'highpass=f=380,highpass=f=380,lowpass=f=3400,lowpass=f=3400,volume=7dB,asoftclip=type=tanh,'
              'apad=pad_dur=0.6,aecho=0.8:0.5:70|140:0.22|0.12,volume=-2dB',
    'muffled': 'lowpass=f=1500,lowpass=f=1500,volume=-4dB,aecho=0.7:0.4:40:0.2',
}
REVOICE = {'Oi.'} if ROUND <= 2 else {'...And everything else.'} if ROUND == 4 else {'Hey, boss, are you there?'} if ROUND == 9 else set()  # Kai: on screen now, the toilet-row protest face; the old read was 'from across the room'


# Round 4 (Kai 4 Nov, timeline r4: "a louder version of you killed everybody... the emotion... landed more than the
# sound effect does of her being behind the door"): the door muffle lighter again, so the words stay clear.
FX4 = {**FX2, 'muffled': 'lowpass=f=2600,volume=-2dB,aecho=0.7:0.35:35:0.15'}


def fx(src, dst, kind):
    if ROUND == 1:
        return V.fx(src, dst, kind)
    import subprocess
    af = (FX4 if ROUND >= 4 else FX2)[kind]
    subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', '-i', str(src), '-af', af, str(dst)], check=True)


def reuse_map():
    """(who, phrase) -> the picked take (and its fx copy) from the previous round's file, for unchanged words."""
    out = {}
    prev = V.S.SCENES / FOLDER / PREV
    if ROUND == 1 or not prev.exists():
        return out
    for row in json.loads(prev.read_text())['lines']:
        for ph in row['phrases']:
            if 'audition' in ph:                    # round 2's lady: Kai picked Vindemiatrix (3 Nov)
                ph = {**ph, **ph['audition'][LADY_AUDITION[1][0]]}
                row = {**row, 'voice': LADY_AUDITION[1][0]}
            if ph.get('reused'):
                out[(row['who'], ph['text'])] = {'reused': ph['reused'], 'fx_file': ph.get('fx_file'), 'voice': row['voice']}
            elif 'pick' in ph and 'takes' in ph:
                f = next(t['file'] for t in ph['takes'] if t['take'] == ph['pick'])
                fx = ph.get('fx_file')
                if fx and not fx.startswith(f.rsplit('.', 1)[0]):
                    fx = f.rsplit('.', 1)[0] + '-fx.wav'
                out[(row['who'], ph['text'])] = {'reused': f, 'fx_file': fx, 'voice': row['voice']}
    return out


def jobs():
    cast = json.loads(V3.CAST_FILE.read_text())['cast']
    base = {'bot': V.profiles['bot'], **{k: cast[k]['prompt'] for k in ('lady', 'woman', 'man')}}
    # Sandra's locked prompt carries "a pause before 'Again.'" from the toilet row; two takes said "Again." (3 Nov)
    base['woman'] = base['woman'].replace("Pace: quick and clipped, a pause before 'Again.'", 'Pace: quick and clipped.')
    voice = {'bot': 'Aoede', **{k: cast[k]['voice'] for k in ('lady', 'woman', 'man')}}
    script = json.loads((V.S.SCENES / FOLDER / 'script.json').read_text())
    reuse = reuse_map()
    out, rows = [], []
    for i, ln in enumerate(script['lines']):
        who = ln['who']
        if who not in SPEAKERS:
            continue
        audition = who == 'lady' and ROUND == 2
        phs, gaps = phrases(ln['text'])
        row = {'i': i, 'who': who, 'text': ln['text'], 'off': bool(ln.get('off')), 'fx': ln.get('fx'),
               'voice': voice[who], 'phrases': [],
               'gaps': [{'after': p, 'before': p + 1, 'seconds': g} for p, g in enumerate(gaps)]}
        for p, (ph, tag) in enumerate(phs):
            emo = '; '.join(x for x in (tag, emo_for(ln['text'])) if x) or emotion(ln.get('direction'), tag)
            if not audition and (who, ph) in reuse and ph not in REVOICE:
                row['phrases'].append({'p': p, 'text': ph, 'direction': emo, **reuse[(who, ph)]})
                continue
            if audition:
                cands = [(vc, V3.with_emotion(lady_profile(desc).replace('{acc}', acc), emo)) for vc, acc, desc in LADY_AUDITION]
            elif who == 'lady' and ROUND > 2:
                vc, acc, desc = LADY_AUDITION[1]          # Vindemiatrix, Kai's pick 3 Nov
                cands = [(vc, V3.with_emotion(lady_profile(desc).replace('{acc}', acc), emo))]
            else:
                cands = [(voice[who], V3.with_emotion(base[who], emo))]
            entry = {'p': p, 'text': ph, 'direction': emo, 'cands': {}}
            for vc, prompt in cands:
                stem = f'{i:02d}-{who}' + (f'-{vc}' if audition else '') + (f'-p{p}' if len(phs) > 1 else '')
                pkey = f'{RND}-{stem}'
                V.profiles[pkey] = prompt  # in-process only
                entry['cands'][vc] = {'prompt': prompt, 'stem': stem}
                out += [{'key': f'{stem}-{t}', 'stem': stem, 'dir': RND, 'who': pkey, 'voice': vc, 'text': ph,
                         'target': ph, 'how': None, 'work': V3.WORK3 / RND} for t in 'abc']
            row['phrases'].append(entry)
        if audition:
            row['audition'] = [vc for vc, _, _ in LADY_AUDITION]
            row['voice'] = LADY_AUDITION[0][0]
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
            if 'cands' not in ph:
                if row['fx'] and ROUND > 1:  # the round's filter on the reused dry take
                    src = V3.OUT3 / ph['reused']
                    dst = V3.OUT3 / RND / (src.stem + '-fx.wav')
                    fx(src, dst, row['fx'])
                    ph['fx_file'] = f"{RND}/{dst.name}"
                    card(dst, None, None, f"{row['fx']} (round {ROUND} filter) copy of the reused pick", parent=src,
                         fx=f"{row['fx']}-r{ROUND}")
                print(f"{row['i']:2d} p{ph['p']} {row['who']:5s} reused {ph['reused']}")
                continue
            for vc, c in ph.pop('cands').items():
                takes = by[c['stem']]
                ok = [t for t in takes if t['ok']] or takes
                best = min(ok, key=lambda t: (-t['match'], t['gap']))
                pick = {'pick': best['take'], 'verified': best['ok'], 'prompt': c['prompt'],
                        'takes': [{k: v for k, v in t.items() if k != 'ok'} for t in takes]}
                if row['fx']:
                    src = V3.OUT3 / best['file']
                    dst = src.with_name(src.stem + '-fx.wav')
                    fx(src, dst, row['fx'])
                    pick['fx_file'] = f"{RND}/{dst.name}"
                card(V3.OUT3 / best['file'], c['prompt'], vc, f"bridge r{ROUND} line {row['i']} p{ph['p']}: {ph['text']}")
                if row['fx']:
                    card(dst, None, None, f"{row['fx']} copy of the pick", parent=V3.OUT3 / best['file'], fx=row['fx'])
                if 'audition' in row:
                    ph.setdefault('audition', {})[vc] = pick
                    if vc == row['voice']:
                        ph.update(pick)
                else:
                    ph.update(pick)
                print(f"{row['i']:2d} p{ph['p']} {row['who']:5s} {vc:12s} pick {best['take']} {best['duration']:5.2f}s gap "
                      f"{best['gap']:4.2f} match {best['match']:.2f}{'' if best['ok'] else '  UNVERIFIED'}  '{best['heard']}'")
    doc = {'about': f"Scene B bridge lines (draft {script['dialogue']['picked']}), voiced in Gemini TTS by "
                    "scripts/gpom/second-half-video/voice-bridge.py. Files are relative to the media folder. Picked by "
                    "measurement (whisper + longest gap); nobody has listened.",
           'media': str(V3.OUT3), 'source': f'docs/stories/gitpush-origin-master/scenes/{FOLDER}/script.json',
           'dialogue': script['dialogue'], 'lines': rows}
    dst = V.S.SCENES / FOLDER / DOC
    dst.write_text(json.dumps(doc, indent=1, ensure_ascii=False) + '\n')
    print(f'wrote {dst}')


if __name__ == '__main__':
    main()
