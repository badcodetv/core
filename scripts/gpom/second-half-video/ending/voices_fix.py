#!/usr/bin/env python3
"""Re-voice chosen human lines of ONE scene (review fix passes), on voices.py's engine, without touching other lines.

    python3 scripts/gpom/second-half-video/ending/voices_fix.py D r1 d5-2-derek d7-0-sandra d7-1-derek
    python3 scripts/gpom/second-half-video/ending/voices_fix.py --takes 3 --supersede "<why>" C r1 c1-0-maddie ...

Reads the lines' CURRENT words from scene.json, voices takes named <id>-<tag><a|b...>.wav (so the old takes of a
line whose words changed are never "kept" by mistake), checks each with faster-whisper as voices.py does
(retaking in pairs while none passes), and rewrites only those lines' rows in that scene's voices.json, keeping
the previous row under `previous`.

--takes N: N takes in the first pass (default 2), then pairs. --supersede WHY: every row of that voices.json whose
words are no longer in scene.json (a retired line, or the old words of a re-voiced id) is moved, whole, to the
file's `superseded` map (key '<id>@<tag>') with WHY, instead of being dropped.
"""
import json
import sys

import voices as VO

args = sys.argv[1:]
TAKES, WHY = 2, None
while args[0].startswith('--'):
    if args[0] == '--takes':
        TAKES, args = int(args[1]), args[2:]
    elif args[0] == '--supersede':
        WHY, args = args[1], args[2:]
    else:
        sys.exit(f'unknown flag {args[0]}')
scene, tag, ids = args[0], args[1], args[2:]
LETTERS = 'abcdefghij'
FIRST = LETTERS[:TAKES]
RETAKES = [LETTERS[i:i + 2] for i in range(TAKES, TAKES + 4, 2)]  # up to two more pairs


def main():
    VO.V3.load_key()
    lines = [ln for ln in VO.collect() if ln['scene'] == scene and ln['id'] in ids]
    assert len(lines) == len(ids), [ln['id'] for ln in lines]

    def job(ln, t):
        j = VO.take_job(ln, t)
        j['key'] = f"{ln['id']}-{tag}{t}"
        return j

    res = [VO.run(job(ln, t)) for ln in lines for t in FIRST]
    heard = VO.whisper([r['wav'] for r in res if r['wav']])
    scored = {}
    for r in res:
        scored.setdefault(r['line']['id'], []).append(VO.score(r, heard.get(str(r['wav']))))
    for pair in RETAKES:
        redo = [ln for ln in lines if not any(t['ok'] for t in scored[ln['id']])]
        if not redo:
            break
        res2 = [VO.run(job(ln, t)) for ln in redo for t in pair]
        heard2 = VO.whisper([r['wav'] for r in res2 if r['wav']])
        for r in res2:
            scored[r['line']['id']].append(VO.score(r, heard2.get(str(r['wav']))))
    path = VO.SCENES / VO.SCENE_DIRS[scene] / 'voices.json'
    doc = json.loads(path.read_text())
    if WHY:
        now = {ln['id']: ln['text'] for ln in VO.collect() if ln['scene'] == scene}
        sup = doc.setdefault('superseded', {})
        for lid, row in list(doc['lines'].items()):
            if now.get(lid) != row['text']:
                sup[f'{lid}@{tag}'] = {**row, 'superseded': WHY}
                del doc['lines'][lid]
    for ln in lines:
        takes = scored[ln['id']]
        best, why = VO.pick(takes)
        prev = doc['lines'].get(ln['id'])
        doc['lines'][ln['id']] = {
            'speaker': ln['speaker'], 'frame': ln['frame'], 'text': ln['text'], 'voice': ln['voice'],
            'file': f"voices/{best['file']}", 'duration': best['duration'], 'speech': best['speech'],
            'lead': ln['lead'], 'heard': best['heard'], 'verified': best['ok'], 'why': f'[{tag}] ' + why,
            'takes': [{k: t[k] for k in ('take', 'file', 'duration', 'expected', 'heard', 'match', 'gap', 'status')}
                      for t in takes],
            'prompt': VO.V.profiles[f"end-{ln['scene']}-{ln['id']}"],
            'previous': {k: prev[k] for k in ('text', 'file', 'heard')} if prev else None}
        if WHY and ln['id'] + '@' + tag in doc.get('superseded', {}):
            doc['lines'][ln['id']]['previous'] = {'superseded': f"{ln['id']}@{tag}"}
        print(f"{ln['id']:16s} {best['file']:26s} {best['duration']:5.2f}s match {best['match']:.2f} "
              f"{'OK ' if best['ok'] else 'BAD'} | {why}")
        for t in takes:
            print(f"    {t['take']} {t['file']} {t['heard']!r} {t['match']}")
    path.write_text(json.dumps(doc, indent=1, ensure_ascii=False) + '\n')


if __name__ == '__main__':
    main()
