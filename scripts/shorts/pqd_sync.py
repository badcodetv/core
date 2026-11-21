#!/usr/bin/env python3
"""Pub Quiz: Democracy: fit each voice line to its talking clip (the lip-sync-dub method, quick form).

Every clip was made saying its exact line (Omni's own audio, dropped in the cut). For each line, each candidate clip
and each voice take, this finds the clip in-point and voice tempo (0.90-1.15) that put the most voice words inside
-45..+125 ms of the clip's own words, words matched in order. The clip's own audio stands in for its mouth (no mouth
tracker pass: Jack, 2026-11-21, "the quickest way possible"). Best first, to sync/fits.json.

    python3 scripts/shorts/pqd_sync.py
"""
# style-lint: story=short-pub-quiz-democracy
import importlib.util, json, pathlib, re, sys
import numpy as np

REPO = pathlib.Path(__file__).resolve().parents[2]
SCENE = REPO / 'docs/stories/short-pub-quiz-democracy/scenes/pub-quiz-democracy'
sys.path.insert(0, str(REPO / 'scripts/drive'))
from localmap import localize  # noqa: E402

spec = importlib.util.spec_from_file_location('vrf', REPO / 'scripts/gpom/second-half-video/voice-row-fit.py')
vrf = importlib.util.module_from_spec(spec); spec.loader.exec_module(vrf)
cfg = localize(json.loads((SCENE / 'scene.json').read_text()))
MEDIA = pathlib.Path(cfg['media'])
VID, VOX = MEDIA / 'video', MEDIA / 'audio/casting'
EARLY, LATE = -0.045, 0.125
# line -> clip prefix (clips are video/pub-quiz-democracy-<prefix><a|b>-<still>.mp4)
LINES = {'02-tourist-fifth': 'P02', '05-tourist-liked': 'P03', '04-voter-both': 'P04', '06-voter-like': 'P04B',
         '07-swiss-cows': 'P05', '08-bob-why': 'P06', '09-tourist-crisps': 'P07'}
PICK = {r: v for r, v in (('quizmaster', 'quizmaster-b'), ('tourist', 'tourist-a'), ('voter', 'voter-a'), ('swiss', 'swiss-a'), ('bob', 'bob-1'))}


def norm(w):
    return re.sub(r"[^a-z']", '', w.lower())


def words(p):
    return [(norm(w), s, e) for w, s, e in vrf.words_of(str(p)) if norm(w)]


def fit(cw, vw):
    """Best (in-point, tempo, words in time) laying voice words vw over clip words cw."""
    best = (0, 0.0, 1.0, 0)
    pairs, j = [], 0
    for w, s, _ in vw:  # match voice words to clip words in order
        for k in range(j, len(cw)):
            if cw[k][0] == w:
                pairs.append((s, cw[k][1])); j = k + 1; break
    if not pairs:
        return None
    for tempo in np.arange(0.90, 1.151, 0.01):
        for vs, cs in pairs:  # anchor each matched pair in turn
            on = cs - vs / tempo  # clip time where the voice starts
            if on < -0.05:
                continue
            n = sum(EARLY <= (on + v / tempo) - c <= LATE for v, c in pairs)
            if n > best[0] or (n == best[0] and abs(tempo - 1) < abs(best[2] - 1)):
                best = (int(n), round(float(max(on, 0.0)), 3), round(float(tempo), 2), len(vw))
    return best


def main():
    out = {}
    for key, pre in LINES.items():
        role = key.split('-')[1]
        takes = [VOX / f'{key}--{PICK[role]}.wav'] + sorted((MEDIA / 'audio/sync').glob(f'{key}--p*.wav'))  # re-voices with pause tags
        rows = []
        for take in takes:
            vw = words(take)
            for clip in sorted(VID.glob(f'pub-quiz-democracy-{pre}[ab]-*.mp4')):
                r = fit(words(clip), vw)
                if r:
                    rows.append({'clip': clip.name, 'take': take.name, 'on': r[1], 'tempo': r[2], 'words': r[0], 'of': r[3]})
        rows.sort(key=lambda x: (-x['words'], abs(x['tempo'] - 1)))
        out[key] = rows
        b = rows[0] if rows else None
        print(key, b and f"{b['clip']} on {b['on']}s x{b['tempo']}: {b['words']}/{b['of']} words in time")
    (SCENE / 'sync').mkdir(exist_ok=True)
    (SCENE / 'sync/fits.json').write_text(json.dumps(out, indent=1))


if __name__ == '__main__':
    main()
