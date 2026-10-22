#!/usr/bin/env python3
"""Re-voice chosen human lines of ONE scene (review fix passes), on voices.py's engine, without touching other lines.

    python3 scripts/gpom/second-half-video/ending/voices_fix.py D r1 d5-2-derek d7-0-sandra d7-1-derek

Reads the lines' CURRENT words from scene.json, voices takes named <id>-<tag><a|b...>.wav (so the old takes of a
line whose words changed are never "kept" by mistake), checks each with faster-whisper as voices.py does
(retaking in pairs while none passes), and rewrites only those lines' rows in that scene's voices.json, keeping
the previous row under `previous`.
"""
import json
import sys

import voices as VO

scene, tag, ids = sys.argv[1], sys.argv[2], sys.argv[3:]


def main():
    VO.V3.load_key()
    lines = [ln for ln in VO.collect() if ln['scene'] == scene and ln['id'] in ids]
    assert len(lines) == len(ids), [ln['id'] for ln in lines]

    def job(ln, t):
        j = VO.take_job(ln, t)
        j['key'] = f"{ln['id']}-{tag}{t}"
        return j

    res = [VO.run(job(ln, t)) for ln in lines for t in 'ab']
    heard = VO.whisper([r['wav'] for r in res if r['wav']])
    scored = {}
    for r in res:
        scored.setdefault(r['line']['id'], []).append(VO.score(r, heard.get(str(r['wav']))))
    for pair in VO.RETAKES[1:]:
        redo = [ln for ln in lines if not any(t['ok'] for t in scored[ln['id']])]
        if not redo:
            break
        res2 = [VO.run(job(ln, t)) for ln in redo for t in pair]
        heard2 = VO.whisper([r['wav'] for r in res2 if r['wav']])
        for r in res2:
            scored[r['line']['id']].append(VO.score(r, heard2.get(str(r['wav']))))
    path = VO.SCENES / VO.SCENE_DIRS[scene] / 'voices.json'
    doc = json.loads(path.read_text())
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
        print(f"{ln['id']:16s} {best['file']:26s} {best['duration']:5.2f}s match {best['match']:.2f} "
              f"{'OK ' if best['ok'] else 'BAD'} | {why}")
        for t in takes:
            print(f"    {t['take']} {t['file']} {t['heard']!r} {t['match']}")
    path.write_text(json.dumps(doc, indent=1, ensure_ascii=False) + '\n')


if __name__ == '__main__':
    main()
