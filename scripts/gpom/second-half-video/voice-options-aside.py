#!/usr/bin/env python3
"""Ten readings of Maddie's "...And everything else." (GPOM bridge, line 1) for Kai to pick by ear.

Kai 4 Nov (timeline r5, at126): "The emotion in this particular moment is very important... subdued, apologetic,
serious, regretful... 10 different approaches... in a prompt for Maddy's voice. And then we can pick one."
Same voice and profile as every other Maddie line (Aoede on the second-half 'bot' profile); only the Emotion line
changes. Two takes each, whisper-checked, the best kept; each gets the round's tannoy filter, as in the cut.

    python3 scripts/gpom/second-half-video/voice-options-aside.py
    -> <voice3>/aside-opts/<n>-<a|b>.wav (+ -fx.wav) and scenes/second-half-b-the-door/voices-aside-options.json
"""
import difflib
import importlib.util
import json
import os
import sys
from concurrent.futures import ThreadPoolExecutor

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, 'ending'))
import voice3 as V3  # noqa: E402
import voices as E  # noqa: E402

spec = importlib.util.spec_from_file_location('vb', os.path.join(HERE, 'voice-bridge.py'))
sys.argv = [sys.argv[0], '--round', '4']
VB = importlib.util.module_from_spec(spec)
spec.loader.exec_module(VB)
V = VB.V

TEXT = '...And everything else.'
RND = 'aside-opts'
OPTIONS = [
    ('confession', 'a quiet confession, barely above a murmur, as the full weight of what she means finally lands on her'),
    ('catch', 'she stops, a catch in the throat, then says it: owning the enormous thing behind the small words'),
    ('verdict', 'flat and plain, no performance at all, like reading out a verdict against herself'),
    ('owning-up', 'small and ashamed, like a child owning up to something far too big to fix'),
    ('careful', 'slow and heavy, each word set down carefully, as if it might break'),
    ('understatement', 'rueful, knowing the words are absurdly too small for what happened, saying them softly anyway'),
    ('mourner', 'grief in it: a mourner speaking at a funeral she herself caused'),
    ('formal', 'a formal, dignified apology she truly means; measured and grave, nothing cute about it'),
    ('exhale', 'a long breath out first, then the words carried almost on that breath, sad and tired'),
    ('tender', 'gentle and sincere, warm with regret, as if to someone she hurt and still cares about'),
]


def main():
    V3.load_key()
    (V3.OUT3 / RND).mkdir(parents=True, exist_ok=True)
    (V3.WORK3 / RND).mkdir(parents=True, exist_ok=True)
    base = V.profiles['bot']
    jobs, prompts = [], {}
    for n, (slug, emo) in enumerate(OPTIONS, 1):
        stem = f'{n:02d}-{slug}'
        prompt = V3.with_emotion(base, emo)
        prompts[stem] = prompt
        V.profiles[f'{RND}-{stem}'] = prompt
        jobs += [{'key': f'{stem}-{t}', 'stem': stem, 'dir': RND, 'who': f'{RND}-{stem}', 'voice': 'Aoede', 'text': TEXT,
                  'target': TEXT, 'how': None, 'work': V3.WORK3 / RND} for t in 'ab']
    with ThreadPoolExecutor(3) as ex:
        res = list(ex.map(V3.run, jobs))
    heard = E.whisper([V3.OUT3 / RND / f"{r['key']}.wav" for r in res if r['duration']])
    rows = []
    for n, (slug, emo) in enumerate(OPTIONS, 1):
        stem = f'{n:02d}-{slug}'
        takes = []
        for r in (r for r in res if r['stem'] == stem):
            f = V3.OUT3 / RND / f"{r['key']}.wav"
            h = heard.get(str(f)) if r['duration'] else None
            ratio = difflib.SequenceMatcher(None, E.norm(TEXT), E.norm(h['text'])).ratio() if h else 0.0
            takes.append({'take': r['key'][-1], 'file': f'{RND}/{f.name}', 'duration': round(r['duration'], 2),
                          'heard': h['text'] if h else '', 'match': round(ratio, 3), 'status': r['status']})
        best = max(takes, key=lambda t: (t['match'] >= E.MATCH, t['heard'].rstrip().endswith('.'), t['match']))
        src = V3.OUT3 / best['file']
        dst = src.with_name(src.stem + '-fx.wav')
        VB.fx(src, dst, 'tannoy')
        VB.card(src, prompts[stem], 'Aoede', f'bridge aside option {n} ({slug}): {TEXT}')
        VB.card(dst, None, None, 'tannoy copy of the option', parent=src, fx='tannoy-r2')
        rows.append({'n': n, 'slug': slug, 'emotion': emo, 'pick': best['take'], 'file': best['file'],
                     'fx_file': f'{RND}/{dst.name}', 'prompt': prompts[stem], 'takes': takes})
        print(f"{n:2d} {slug:15s} {best['take']} {best['duration']:4.2f}s  '{best['heard']}'")
    doc = {'about': "Ten readings of Maddie's aside for Kai to pick (timeline r5 at126). Files relative to media.",
           'media': str(V3.OUT3), 'text': TEXT, 'options': rows}
    out = V.S.SCENES / VB.FOLDER / 'voices-aside-options.json'
    out.write_text(json.dumps(doc, indent=1, ensure_ascii=False) + '\n')
    print(f'wrote {out}')


if __name__ == '__main__':
    main()
