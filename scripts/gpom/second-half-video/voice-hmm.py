#!/usr/bin/env python3
"""The old lady's thinking "Hmm..." before "Perhaps we should vote." (GPOM bridge, Kai timeline r5 at1960:
"put a hmm, like a HMMMM pause, perhaps we should vote"). Her locked voice (Vindemiatrix, voice-bridge.py's
lady_profile); three takes, whisper-checked loosely (a hum has no words). -> <voice3>/hmm/ + voices-hmm.json
"""
import importlib.util, json, os, sys
from concurrent.futures import ThreadPoolExecutor
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, 'ending'))
import voice3 as V3  # noqa: E402
spec = importlib.util.spec_from_file_location('vb', os.path.join(HERE, 'voice-bridge.py'))
sys.argv = [sys.argv[0], '--round', '4']
VB = importlib.util.module_from_spec(spec); spec.loader.exec_module(VB)
V = VB.V
TEXT, RND = 'Hmmmm...', 'hmm'
EMO = ('a long, low, closed-mouth thinking hum through the nose, considering the room before she suggests something; '
       'unhurried, about a second and a half, then stops')


def main():
    V3.load_key()
    for d in (V3.OUT3 / RND, V3.WORK3 / RND):
        d.mkdir(parents=True, exist_ok=True)
    vc, acc, desc = VB.LADY_AUDITION[1]
    prompt = V3.with_emotion(VB.lady_profile(desc).replace('{acc}', acc), EMO)
    V.profiles[f'{RND}-lady'] = prompt
    jobs = [{'key': f'17-lady-hmm-{t}', 'stem': '17-lady-hmm', 'dir': RND, 'who': f'{RND}-lady', 'voice': vc, 'text': TEXT,
             'target': TEXT, 'how': None, 'work': V3.WORK3 / RND} for t in 'abc']
    with ThreadPoolExecutor(3) as ex:
        res = list(ex.map(V3.run, jobs))
    takes = []
    for r in res:
        f = V3.OUT3 / RND / f"{r['key']}.wav"
        if r['duration']:
            VB.card(f, prompt, vc, f'bridge line 17 hum before the vote: {TEXT}')
        takes.append({'take': r['key'][-1], 'file': f'{RND}/{f.name}', 'duration': round(r['duration'] or 0, 2),
                      'status': r['status']})
        print(takes[-1])
    out = V.S.SCENES / VB.FOLDER / 'voices-hmm.json'
    out.write_text(json.dumps({'media': str(V3.OUT3), 'text': TEXT, 'voice': vc, 'prompt': prompt, 'takes': takes},
                              indent=1, ensure_ascii=False) + '\n')


if __name__ == '__main__':
    main()
