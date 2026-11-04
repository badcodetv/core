#!/usr/bin/env python3
"""Sandra's "If there's a way to fix this, I'd love to take it." re-voiced to the timing of her clip (br18), so it
goes in as ONE take, not pieces (Kai 4 Nov, timeline r7 at1788: "it's very much cutting the audio up to try and
lip-sync... regenerate the audio to the specific time"). Six takes with a beat after "fix this,"; each is scored
against br18's word anchors (relative to "If"): fix +1.22, I'd +2.60, take +3.50. -> <voice3>/sandra-fit/
"""
import importlib.util, json, os, sys
from concurrent.futures import ThreadPoolExecutor
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, 'ending'))
import voice3 as V3  # noqa: E402
import voices as E  # noqa: E402
spec = importlib.util.spec_from_file_location('vb', os.path.join(HERE, 'voice-bridge.py'))
sys.argv = [sys.argv[0], '--round', '4']
VB = importlib.util.module_from_spec(spec); spec.loader.exec_module(VB)
V = VB.V
TEXT, RND = "If there's a way to fix this, I'd love to take it.", 'sandra-fit'
EMO = ("wry and tired, deadpan; an even, unhurried pace; after 'fix this,' she stops for a real beat, almost a second, "
       "as if weighing it, then 'I'd love to take it.' quietly and flatly")
ANCHOR = {'fix': 1.22, "i'd": 2.60, 'take': 3.50}


def main():
    V3.load_key()
    for d in (V3.OUT3 / RND, V3.WORK3 / RND):
        d.mkdir(parents=True, exist_ok=True)
    cast = json.loads(V3.CAST_FILE.read_text())['cast']
    base = cast['woman']['prompt'].replace("Pace: quick and clipped, a pause before 'Again.'", 'Pace: even, unhurried.')
    prompt = V3.with_emotion(base, EMO)
    V.profiles[f'{RND}-woman'] = prompt
    jobs = [{'key': f'16a-woman-{t}', 'stem': '16a-woman', 'dir': RND, 'who': f'{RND}-woman', 'voice': cast['woman']['voice'],
             'text': TEXT, 'target': TEXT, 'how': None, 'work': V3.WORK3 / RND} for t in 'abcdef']
    with ThreadPoolExecutor(3) as ex:
        res = list(ex.map(V3.run, jobs))
    import subprocess
    wpy = os.path.expanduser('~/.cache/badcode-whisper/venv/bin/python')  # faster-whisper lives in its own venv

    def words_of(f):
        code = ("import json,sys;from faster_whisper import WhisperModel;m=WhisperModel('small',device='cpu',compute_type='int8');"
                "s,_=m.transcribe(sys.argv[1],word_timestamps=True);print(json.dumps([[w.word,w.start] for x in s for w in x.words]))")
        return json.loads(subprocess.run([wpy, '-c', code, str(f)], capture_output=True, text=True, check=True).stdout)
    takes = []
    for r in res:
        f = V3.OUT3 / RND / f"{r['key']}.wav"
        if not r['duration']:
            continue
        words = [(w.strip().strip(',.').lower(), s) for w, s in words_of(f)]
        t0 = words[0][1] if words else 0
        rel = {k: next((t - t0 for w, t in words if w == k), None) for k in ANCHOR}
        err = sum(abs(rel[k] - v) for k, v in ANCHOR.items()) if all(v is not None for v in rel.values()) else 99
        VB.card(f, prompt, cast['woman']['voice'], f'bridge line 16 first half, fitted to br18: {TEXT}')
        takes.append({'take': r['key'][-1], 'file': f'{RND}/{f.name}', 'duration': round(r['duration'], 2),
                      'heard': ' '.join(w for w, _ in words), 'first_word': round(t0, 2),
                      'rel': {k: (round(v, 2) if v is not None else None) for k, v in rel.items()}, 'err': round(err, 2)})
        print(takes[-1])
    best = min(takes, key=lambda t: t['err'])
    out = V.S.SCENES / VB.FOLDER / 'voices-sandra-fit.json'
    out.write_text(json.dumps({'media': str(V3.OUT3), 'text': TEXT, 'anchor': ANCHOR, 'prompt': prompt, 'pick': best['take'],
                               'takes': takes}, indent=1, ensure_ascii=False) + '\n')
    print('pick', best)


if __name__ == '__main__':
    main()
