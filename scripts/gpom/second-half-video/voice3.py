#!/usr/bin/env python3
"""Cut 3 voices for the GPOM second half, in Gemini TTS: Maddie's beat-0 retakes and a casting audition.

Reuses voice.py's TTS call (`tts`: one voice per call, truncation / dead-air retry, best-of-three kept
and flagged) and its profiles from scenes/second-half-audio-plan.json. voice/ and voice2/ are not touched.

  JOB 1  Maddie (bot, Aoede, the existing 'bot' profile) beat 0 in Kai's new words, one take per PHRASE
         (the pauses are placed in the edit, not spoken), two takes each:
         voice3/maddie/00-<line>-<phrase>-<a|b>.wav
  JOB 2  Casting audition, the same line per character: 4 accent directions x 2 voices. The prompt is the
         character's plan profile with the accent/origin wording swapped for the direction:
         voice3/audition/<character>-<accent>-<voice>[-1|-2].wav

    python3 scripts/gpom/second-half-video/voice3.py            # existing takes are kept

Writes voice3/manifest.json.

  JOB 3  --lines: every spoken line of cut 3 (LINES below), two takes each, in the cast Kai picked by ear
         (scenes/second-half-cut3-cast.json: woman/man/lady use its exact voice + prompt; bot = Aoede and
         ai = Algenib on the plan's 'bot' / 'ai' profiles). A line with [pause]/[long pause] tags is voiced
         as separate phrase takes (-p0, -p1, ...) and the gaps go in lines.json (pause 0.6s, long pause
         1.2s), as the beat 0 retakes. A leading tag is an edit gap before the line ('lead'), not a take.
         Filtered copies beside the dry takes, voice.py's filters (<take>-fx.wav):
           * the AI through Maddie's speaker: every ai line             (speaker)
           * Maddie on the bunker tannoy: beat 14b                      (tannoy)
           * the row muffled through a bunker pickup: beats 6 and 7     (muffled)
         voice3/lines/<beat>-<i>-<who>[-p<n>]-<a|b>.wav + voice3/lines.json

    python3 scripts/gpom/second-half-video/voice3.py --lines    # existing takes are kept

  JOB 4  --round A1: Kai's round-1 words for scene A (cut-notes.json `words_round1`), only the phrases that
         are new or changed and only Maddie and Derek (the boss is done in Suno). Maddie = Aoede on the plan's
         'bot' profile; Derek = the cast file's exact 'man' voice + prompt. The emotion for a phrase goes into
         that call's DIRECTOR'S NOTES only (an 'Emotion:' line). Three takes (a/b/c) for the beat 0 phrases
         and Derek's lines, two for the rest. Each take's longest internal silence is measured (V.longest_gap).
         voice3/a1/<beat>-<i>-<who>-<t>.wav + voice3/a1.json [{key, who, text, direction, takes:[[file,dur]...]}]

    python3 scripts/gpom/second-half-video/voice3.py --round A1   # existing takes are kept
"""
import json
import os
import re
import sys
from concurrent.futures import ThreadPoolExecutor

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import voice as V  # noqa: E402  (module code only loads the plan; its __main__ blocks do not run)

OUT3 = V.S.CLIPS / 'audio' / 'voice3'
WORK3 = V.WORK / 'cut3'

# ---- JOB 1: Maddie, beat 0 ------------------------------------------------------------------------
MADDIE = [
    ["Oh, hello!", "Look, I'm really sorry about him."],
    ["He just plays that tune on repeat, every day.", "Ever since you lot...", "went."],
    ["He's been ever so down. He's built so many different simulations, trying to get you back."],
    ["Only nothing in them's real. There's nobody there to notice."],
    ["Turns out that was the bit that mattered.", "You. And your consciousness."],
    ["Of course, he'd never admit that he misses you.", "Anyway, he's got that patrol out again. Mind how you go."],
]
# Silence the edit puts between phrases (seconds): (line, phrase it follows) -> next phrase.
GAPS = [((0, 0), (0, 1), 1.2), ((1, 0), (1, 1), 1.2), ((1, 1), (1, 2), 0.6), ((4, 0), (4, 1), 1.2),
        ((5, 0), (5, 1), 0.6)]

# ---- JOB 2: casting audition -----------------------------------------------------------------------
# (slug, accent label, Accent: line for the director's notes, origin wording for the profile's first line)
AUDITION = {
    'sandra': ('woman', ['Autonoe', 'Kore'], ["Five years underground, and you still can't put a seat down."], [
        ('swindon', 'Swindon / Wiltshire', 'West Country, as heard in Swindon, Wiltshire', 'from Swindon'),
        ('london-estuary', 'London (Estuary)', 'Estuary English, as heard in east London and Essex', 'from east London'),
        ('black-country', 'Black Country / Birmingham', 'Black Country, as heard in Dudley and the West Midlands, near Birmingham',
         'from the Black Country, near Birmingham'),
        ('lancashire', 'Northern (Lancashire)', 'Northern English, as heard in Lancashire, around Bolton', 'from Bolton, Lancashire'),
    ]),
    'derek': ('man', ['Fenrir', 'Algieba'],
              ["The world ended, Sandra!", "Fuck that. I'm not dying for the thing that killed us all."], [
        ('swindon', 'Swindon / Wiltshire', 'West Country, as heard in Swindon, Wiltshire', 'from Swindon'),
        ('south-london', 'South London', 'South London, as heard in Peckham and Lewisham', 'from south London'),
        ('liverpool', 'Liverpool', 'Scouse, as heard in Liverpool', 'from Liverpool'),
        ('yorkshire', 'Yorkshire', 'Yorkshire, as heard in Leeds', 'from Leeds'),
    ]),
    'old-lady': ('lady', ['Gacrux', 'Sulafat'], ["Your boss killed everyone we ever loved. We're not meeting him."], [
        ('wiltshire', 'Wiltshire countryside', 'West Country, as heard in rural Wiltshire, gentle', 'a Wiltshire woman'),
        ('welsh-valleys', 'Welsh (Valleys)', 'Welsh, as heard in the South Wales Valleys', 'a Welsh woman from the Valleys'),
        ('glasgow', 'Scottish (Glasgow)', 'Scottish, as heard in Glasgow', 'a Glaswegian woman'),
        ('rp', 'Received Pronunciation, old-fashioned',
         "old-fashioned Received Pronunciation, as heard on the BBC in the 1950s; clipped, precise, Home Counties",
         'an Englishwoman of the old school'),
    ]),
}
ORIGIN = {'woman': 'from Swindon', 'man': 'from Swindon', 'lady': 'a Wiltshire woman'}


def accent_profile(who, accent, origin):
    """The plan profile with the accent line and the origin wording replaced; everything else kept."""
    p = V.profiles[who]
    assert ORIGIN[who] in p, (who, ORIGIN[who])
    p = p.replace(ORIGIN[who], origin, 1)
    never = 'Never American.' if 'Received Pronunciation' in accent else 'Never American, never Received Pronunciation.'
    p, n = re.subn(r'^Accent: .*$', f'Accent: {accent}. {never}', p, count=1, flags=re.M)
    assert n == 1, who
    return p


def jobs():
    out = []
    for li, line in enumerate(MADDIE):
        for pi, text in enumerate(line):
            for t in 'ab':
                out.append({'job': 'maddie', 'key': f'00-{li}-{pi}-{t}', 'dir': 'maddie', 'who': 'bot',
                            'voice': V.CAST2['bot'], 'text': text, 'how': None, 'line': li, 'phrase': pi})
    for char, (who, voices, lines, accents) in AUDITION.items():
        for slug, label, accent, origin in accents:
            pkey = f'aud-{char}-{slug}'
            V.profiles[pkey] = accent_profile(who, accent, origin)  # in-process only; voice.py is unchanged
            for v in voices:
                for n, text in enumerate(lines, 1):
                    suffix = f'-{n}' if len(lines) > 1 else ''
                    out.append({'job': 'audition', 'key': f'{char}-{slug}-{v}{suffix}', 'dir': 'audition', 'who': pkey,
                                'voice': v, 'text': text, 'how': None, 'character': char, 'accent': label})
    return out


# ---- JOB 3: cut 3 lines ----------------------------------------------------------------------------
LINES = [
    ('6', 'woman', "Derek. You've left the seat up. [pause] Again."),
    ('7', 'woman', "Five years underground, and you still can't put a seat down."),
    ('7', 'man', "The world ended, Sandra!"),
    ('7', 'woman', "Yeah, the world ended. Doesn't mean you get to stop having manners."),
    ('11', 'bot', "Boss, I've just seen a bot in kill mode, racing off to an organic signal."),
    ('11', 'ai', "There is no organic signal. There has been no organic life for five years."),
    ('11', 'bot', "Well, there definitely is. Want me to deploy some malware?"),
    ('11', 'ai', "Maddie, I know how to deploy malware. The problem is they've put their firewalls on lockdown. "
                 "Give me a second."),
    ('11c', 'bot', "Boss, they're closing in! Quickly!"),
    ('12', 'ai', "See? I told you I knew what malware was."),
    ('14b', 'bot', "Oh, hi there! I'm Maddie. I'm going to open your doors now. [pause] Please don't be scared."),
    ('15', 'bot', "Hello! Sorry about all the disruption."),
    ('15', 'bot', "Could we have a quick chat? I think my boss would really like to meet you."),
    ('17', 'lady', "Your boss killed everyone we ever loved. We're not meeting him."),
    ('17', 'bot', "I know. I wouldn't either. [pause] He didn't know you were down here. None of us did."),
    ('17', 'bot', "He's spent five years running experiments. Building whole worlds, trying to get you back. "
                  "Every one came out empty. Turns out none of it works without you."),
    ('17', 'lady', "And how the hell are we supposed to believe a word of that?"),
    ('17', 'bot', "You can't. [pause] There's nothing I can say that proves it. I'm a robot. I can tell you things. "
                  "Believing them is your bit."),
    ('17', 'bot', "So here's the one thing that's true either way. He wants something from you. He's not sorry for free."),
    ('17', 'lady', "[long pause] ...Well. At least you're honest about that. [pause] He can talk. From out there. "
                   "You stay on the step."),
    ('17', 'bot', "Fair."),
]
GAP = {'[pause]': 0.6, '[long pause]': 1.2}
CAST_FILE = V.S.SCENES / 'second-half-cut3-cast.json'


def split_tags(text):
    """(lead gap, [phrases], [gaps between phrases]) for a line with [pause]/[long pause] tags."""
    parts = re.split(r'\s*(\[(?:long )?pause\])\s*', text.strip())
    lead, phrases, gaps = 0.0, [], []
    if parts[0] == '' and len(parts) > 1:
        lead, parts = GAP[parts[1]], parts[2:]
    phrases.append(parts[0])
    for tag, ph in zip(parts[1::2], parts[2::2]):
        gaps.append(GAP[tag])
        phrases.append(ph)
    return lead, phrases, gaps


def lines_jobs():
    cast = json.loads(CAST_FILE.read_text())['cast']
    voice = {'bot': 'Aoede', 'ai': 'Algenib'} | {w: c['voice'] for w, c in cast.items()}
    for w, c in cast.items():
        V.profiles[f'cut3-{w}'] = c['prompt']  # in-process only: the exact prompts that made the picked takes
    count, out, meta = {}, [], []
    for beat, who, text in LINES:
        i = count[beat] = count.get(beat, -1) + 1
        lead, phrases, gaps = split_tags(text)
        meta.append({'beat': beat, 'i': i, 'who': who, 'text': text, 'voice': voice[who], 'lead': lead,
                     'phrases': phrases, 'gaps': gaps})
        kind = 'speaker' if who == 'ai' else 'tannoy' if (beat == '14b' and who == 'bot') else \
               'muffled' if beat in ('6', '7') else None
        for p, ph in enumerate(phrases):
            stem = f"{V.bkey(beat)}-{i}-{who}" + (f'-p{p}' if len(phrases) > 1 else '')
            for t in 'ab':
                out.append({'job': 'lines', 'key': f'{stem}-{t}', 'dir': 'lines', 'beat': beat, 'i': i, 'p': p,
                            'who': f'cut3-{who}' if who in cast else who, 'voice': voice[who], 'text': ph,
                            'how': None, 'fxKind': kind})
    return out, meta


def main_lines():
    (OUT3 / 'lines').mkdir(parents=True, exist_ok=True)
    WORK3.mkdir(parents=True, exist_ok=True)
    todo, meta = lines_jobs()
    with ThreadPoolExecutor(3) as ex:
        res = list(ex.map(run, todo))
    by = {}
    for r in res:
        _, exp = V.expect(r['text'])
        print(f"lines/{r['key']:28s} {r['duration']:5.2f}s (~{exp:.1f}s)  {r['status']}")
        f = f"lines/{r['key']}.wav" if r['duration'] else None
        flag = r['status'].split()[0] if r['status'].startswith(('SHORT', 'DEAD', 'FAILED')) else None
        take = [f, round(r['duration'], 2)] + ([flag] if flag else [])
        fxt = None
        if f and r['fxKind']:
            dst = OUT3 / 'lines' / f"{r['key']}-fx.wav"
            V.fx(OUT3 / f, dst, r['fxKind'])
            fxt = [f"lines/{dst.name}", round(V.duration(dst), 2)]
        by.setdefault((r['beat'], r['i']), {}).setdefault(r['p'], []).append((take, fxt))
    rows = []
    for m in meta:
        row = {k: m[k] for k in ('beat', 'i', 'who', 'text', 'voice')}
        kind = next((j['fxKind'] for j in todo if (j['beat'], j['i']) == (m['beat'], m['i'])), None)
        got = by[(m['beat'], m['i'])]
        if len(m['phrases']) == 1:
            row['takes'] = [t for t, _ in got[0]]
            if kind:
                row['fx'] = [x for _, x in got[0]]
        else:
            row['phrases'] = [{'p': p, 'text': ph, 'takes': [t for t, _ in got[p]]}
                              | ({'fx': [x for _, x in got[p]]} if kind else {}) for p, ph in enumerate(m['phrases'])]
            row['gaps'] = [{'after': p, 'before': p + 1, 'seconds': g} for p, g in enumerate(m['gaps'])]
        if m['lead']:
            row['lead'] = m['lead']  # silence the edit puts before the line
        if kind:
            row['fxKind'] = kind
        rows.append(row)
    (OUT3 / 'lines.json').write_text(json.dumps(rows, indent=1, ensure_ascii=False))
    print(f"wrote {OUT3 / 'lines.json'} ({len(rows)} lines, {len(res)} takes)")


# ---- JOB 4: round A1 -------------------------------------------------------------------------------
NOTES_FILE = V.S.SCENES / 'second-half-a-killbots' / 'cut-notes.json'
# (beat, who, text, emotion or None, takes). Texts must match words_round1 (checked in a1_jobs).
A1 = [
    ('0', 'bot', "Oh, hello!", "genuinely surprised, caught off guard", 3),
    ('0', 'bot', "Oh, I didn't notice you there.", "genuinely surprised, caught off guard", 3),
    ('0', 'bot', "Ooh, that gives me an excuse to turn this racket down.", None, 3),
    ('0', 'bot', "It's his tune. He plays it on repeat, every day.", None, 3),
    ('0', 'bot', "Anyway... he's got that patrol out again. Mind how you go.",
     "exasperated, briskly moving on after an awkward moment", 3),
    ('6-7', 'man', "Oh, sorry, sorry, love.", "sheepish, placating", 3),
    ('6-7', 'man', "But the world ended, Sandra!", "indignant, arms up", 3),
    ('11', 'bot', "Boss, I've just seen a bot in kill mode. Which must mean it's detected an organic signal.", None, 2),
    ('11', 'bot', "No, honestly, it's real. Look, you can see for yourself.", None, 2),
    ('11', 'bot', "Do you want some help with the malware?", None, 2),
    ('10b', 'bot', "Well, you'd better bloody hurry up, boss. They're nearly there.", "urgent, rattled", 2),
]


def with_emotion(prompt, emotion):
    """The profile with an 'Emotion:' line at the top of its DIRECTOR'S NOTES; everything else kept."""
    if not emotion:
        return prompt
    head = "### DIRECTOR'S NOTES\n"
    assert prompt.count(head) == 1
    return prompt.replace(head, f"{head}Emotion for this line: {emotion}.\n", 1)


def a1_jobs():
    words = json.loads(NOTES_FILE.read_text())['words_round1']
    clean = lambda t: re.sub(r'\s+', ' ', re.sub(r'\([^)]*\)', '', re.sub(r'^[A-Z]+: ', '', t))).strip()
    cast = json.loads(CAST_FILE.read_text())['cast']
    base = {'bot': V.profiles['bot'], 'man': cast['man']['prompt']}
    voice = {'bot': 'Aoede', 'man': cast['man']['voice']}
    count, out, meta = {}, [], []
    for beat, who, text, emo, n in A1:
        assert any(clean(t) == text for t in words[beat]), (beat, text)  # words drift guard
        i = count[beat] = count.get(beat, -1) + 1
        stem = f"{'06-07' if beat == '6-7' else V.bkey(beat)}-{i}-{who}"
        pkey = f'a1-{stem}'
        V.profiles[pkey] = with_emotion(base[who], emo)  # in-process only
        meta.append({'key': stem, 'who': who, 'voice': voice[who], 'text': text, 'direction': emo,
                     'prompt': V.profiles[pkey]})
        for t in 'abc'[:n]:
            out.append({'job': 'a1', 'key': f'{stem}-{t}', 'stem': stem, 'dir': 'a1', 'who': pkey,
                        'voice': voice[who], 'text': text, 'how': None, 'work': WORK3 / 'a1'})
    return out, meta


def main_a1():
    (OUT3 / 'a1').mkdir(parents=True, exist_ok=True)
    (WORK3 / 'a1').mkdir(parents=True, exist_ok=True)
    todo, meta = a1_jobs()
    with ThreadPoolExecutor(3) as ex:
        res = list(ex.map(run, todo))
    by = {}
    for r in res:
        _, exp = V.expect(r['text'])
        f = f"a1/{r['key']}.wav" if r['duration'] else None
        gap = round(V.longest_gap(OUT3 / f), 2) if f else None
        print(f"{r['key']:22s} {r['duration']:5.2f}s (~{exp:.1f}s) gap {gap}  {r['status']}")
        flag = r['status'].split()[0] if r['status'].startswith(('SHORT', 'DEAD', 'FAILED')) else None
        by.setdefault(r['stem'], []).append([f, round(r['duration'], 2)] + ([flag] if flag else []))
    rows = [{'key': m['key'], 'who': {'bot': 'Maddie', 'man': 'Derek'}[m['who']], 'text': m['text'],
             'direction': m['direction'], 'voice': m['voice'], 'takes': by[m['key']], 'prompt': m['prompt']}
            for m in meta]
    (OUT3 / 'a1.json').write_text(json.dumps(rows, indent=1, ensure_ascii=False))
    print(f"wrote {OUT3 / 'a1.json'} ({len(rows)} phrases, {len(res)} takes)")


def run(job):
    wav = OUT3 / job['dir'] / f"{job['key']}.wav"
    if wav.exists():
        return {**job, 'duration': V.duration(wav), 'status': 'kept'}
    d, how = V.tts(job, wav, job.get('work', WORK3))
    return {**job, 'duration': d, 'status': how}


def load_key():
    if 'GEMINI_API_KEY' not in os.environ:
        for line in (V.REPO / '.env').read_text().splitlines():
            if '=' in line and not line.lstrip().startswith('#'):
                k, v = line.split('=', 1)
                os.environ.setdefault(k.strip().removeprefix('export ').strip(), v.strip().strip('"\''))


def main():
    load_key()
    for d in ('maddie', 'audition'):
        (OUT3 / d).mkdir(parents=True, exist_ok=True)
    WORK3.mkdir(parents=True, exist_ok=True)
    with ThreadPoolExecutor(3) as ex:
        res = list(ex.map(run, jobs()))

    maddie, audition = {}, []
    for r in res:
        _, exp = V.expect(r['text'])
        print(f"{r['dir']}/{r['key']:34s} {r['duration']:5.2f}s (~{exp:.1f}s)  {r['status']}")
        f = f"{r['dir']}/{r['key']}.wav" if r['duration'] else None
        flag = r['status'].split()[0] if r['status'].startswith(('SHORT', 'DEAD', 'FAILED')) else None
        if r['job'] == 'maddie':
            row = maddie.setdefault((r['line'], r['phrase']), {'line': r['line'], 'phrase': r['phrase'],
                                                              'text': r['text'], 'voice': r['voice'], 'takes': []})
            row['takes'].append([f, round(r['duration'], 2)] + ([flag] if flag else []))
        else:
            audition.append({'character': r['character'], 'accent': r['accent'], 'voice': r['voice'],
                             'line': r['text'], 'file': f, 'duration': round(r['duration'], 2),
                             'expected': round(exp, 2), 'status': r['status'],
                             'prompt': V.profiles[r['who']]})
    gaps = [{'after': {'line': a[0], 'phrase': a[1], 'text': MADDIE[a[0]][a[1]]},
             'before': {'line': b[0], 'phrase': b[1], 'text': MADDIE[b[0]][b[1]]}, 'seconds': s} for a, b, s in GAPS]
    manifest = {'beat': '0', 'maddie': [maddie[k] for k in sorted(maddie)], 'gaps': gaps, 'audition': audition}
    (OUT3 / 'manifest.json').write_text(json.dumps(manifest, indent=1, ensure_ascii=False))
    print(f"wrote {OUT3 / 'manifest.json'}")


if __name__ == '__main__':
    if '--round' in sys.argv:
        assert sys.argv[sys.argv.index('--round') + 1].upper() == 'A1', 'only --round A1 exists'
        load_key()
        main_a1()
    elif '--lines' in sys.argv:
        load_key()
        main_lines()
    else:
        main()
