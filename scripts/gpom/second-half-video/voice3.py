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


def run(job):
    wav = OUT3 / job['dir'] / f"{job['key']}.wav"
    if wav.exists():
        return {**job, 'duration': V.duration(wav), 'status': 'kept'}
    d, how = V.tts(job, wav, WORK3)
    return {**job, 'duration': d, 'status': how}


def main():
    if 'GEMINI_API_KEY' not in os.environ:
        for line in (V.REPO / '.env').read_text().splitlines():
            if '=' in line and not line.lstrip().startswith('#'):
                k, v = line.split('=', 1)
                os.environ.setdefault(k.strip().removeprefix('export ').strip(), v.strip().strip('"\''))
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
    main()
