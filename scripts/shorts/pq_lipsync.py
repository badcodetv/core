#!/usr/bin/env python3
"""Pub Quiz: Housing: lip-sync pass (Jack, 2026-11-20: "fix the lip synccing"), the lip-sync-dub skill's method.

The voice takes are fixed (the fast picks, audio/lines-fast-pick/); new Omni talking clips were made per line with the
exact words (cleanroom/prompts-r4-sync.json, keys L02..L16, three tries each, on the tab pool). For each line SEGMENT
(a long line is split across two clips) this finds, on every clip of it, the in-point that puts the most of the voice's
words inside -45..+125 ms of the clip's own words (its own audio, shifted by the lag to its tracked mouth; ITU-R BT.1359),
the voice laid whole at tempo 1.00, never more than 45 ms before the clip's first word. The best clip per segment wins.

    python3 scripts/shorts/pq_lipsync.py check   # transcribe + mouth-track every new clip -> sync/clips.json
    python3 scripts/shorts/pq_lipsync.py fit     # every clip of every segment -> sync/fits.json (best first)
"""
# style-lint: story=short-pub-quiz-housing
import importlib.util, json, os, pathlib, re, subprocess, sys
import numpy as np

REPO = pathlib.Path(__file__).resolve().parents[2]
SCENE = REPO / 'docs/stories/short-pub-quiz-housing/scenes/pub-quiz-housing'
sys.path.insert(0, str(REPO / 'scripts/drive'))
from localmap import localize  # noqa: E402

spec = importlib.util.spec_from_file_location('vrf', REPO / 'scripts/gpom/second-half-video/voice-row-fit.py')
vrf = importlib.util.module_from_spec(spec); spec.loader.exec_module(vrf)

cfg = localize(json.loads((SCENE / 'scene.json').read_text()))
MEDIA = pathlib.Path(cfg['media'])
VID, VOX, STRIPS = MEDIA / 'video', MEDIA / 'audio/lines-fast-pick', MEDIA / 'strips'
OUT = SCENE / 'sync'
FPS = 24
LINE_TXT = {l['key']: l for l in json.loads((REPO / 'docs/stories/short-pub-quiz-housing/voices/lines/lines.json').read_text())}
# segment -> (line key, clip key prefix, first word index, last word index (exclusive, None = to the end), speaker's face)
SEGS = {
    'L02': ('02-student-hundred', 'L02', 0, None, 'big'),
    'L03': ('03-plasterer-more', 'L03', 0, None, 'big'),
    'L04a': ('04-student-sum', 'L04a', 0, 12, 'big'),   # "Say fifty quid a night. I don't know how much things are,"
    'L04b': ('04-student-sum', 'L04b', 12, None, 'big'),
    'L06': ('06-plasterer-fuckoff', 'L06', 0, None, 'big'),
    'L08a': ('08-banker-billions', 'L08a', 0, 11, 'big'),  # "Paying by the night is the dearest way to buy anything."
    'L08b': ('08-banker-billions', 'L08b', 11, None, 'big'),
    'L10': ('10-bob-noone', 'L10', 0, None, 'big'),
    'L13': ('13-student-own', 'L13', 0, None, 'big'),
    'L15': ('15-plasterer-brick', 'L15', 0, None, 'big'),
    'L16': ('16-banker-bricks', 'L16', 0, None, 'big'),
}
FACE = json.loads((OUT / 'faces.json').read_text()) if (OUT / 'faces.json').exists() else {}  # clip key -> face override
EARLY, LATE = -0.045, 0.125
PRE_TEMPO = {'04-student-sum.wav': 1.15, '08-banker-billions.wav': 1.15}  # the picks already carry atempo 1.15 (rough cut 2)
PRESPED = {'04-student-sum.wav', '08-banker-billions.wav'}
_W = {}


def norm(w):
    w = w.lower().replace('£', '').replace(',', '')
    return {'50': 'fifty', '100': 'hundred', '000': 'thousand'}.get(re.sub(r"[^a-z0-9']", '', w), re.sub(r"[^a-z0-9']", '', w))


def words(path):
    if path not in _W:
        _W[path] = [(norm(w), s, e) for w, s, e in vrf.words_of(str(path)) if norm(w)]
    return _W[path]


def clips_of(prefix):
    return sorted(p for p in VID.glob(f'pq-{prefix}?-*.mp4') if '-muted' not in p.name)


def mouth(clip, face):
    STRIPS.mkdir(exist_ok=True)
    strip = STRIPS / f'{clip.name}-strip.jpg'
    if not pathlib.Path(str(strip) + '.json').exists():
        subprocess.run([vrf.LPY, str(REPO / 'scripts/lipsync/mouth-track.py'), str(clip), str(strip), '--face', face], capture_output=True)
    jp = pathlib.Path(str(strip) + '.json')
    if not jp.exists():  # no face found at all (a bowed head in a wide shot): an empty track
        return np.full(int(round(vrf.env(str(clip)).shape[0])), np.nan)
    js = json.load(open(jp))
    return np.array([np.nan if x is None else x for x in js['scaled']], float)


def anchors(clip, face):
    """The clip's own words, moved by the lag between its own audio and its tracked mouth (Omni's audio drifts)."""
    w = words(clip); e = vrf.env(str(clip)); r = mouth(clip, face)
    n = min(len(e), len(r))
    ee = np.clip((e[:n] - (e[:n].max() - 30)) / 30, 0, 1); rr = np.nan_to_num(r[:n])
    tracked = float(np.mean(~np.isnan(r)))
    lag = 0.0  # untracked (or barely tracked) mouth: trust the clip's own audio (flagged as 'untracked' in the fit)
    if tracked >= 0.5:
        lags = list(range(-12, 13))
        cc = [np.corrcoef(np.roll(ee, L)[12:-12], rr[12:-12])[0, 1] for L in lags]
        lag = lags[int(np.nanargmax(cc))] / FPS
    return [(x, s + lag) for x, s, _ in w], lag, tracked


def seg_words(seg):
    key, _, a, b, _ = SEGS[seg]
    tw = words(VOX / f'{key}.wav')
    return tw[a:b]


def cmd_check():
    OUT.mkdir(exist_ok=True)
    rep = {}
    for seg, (key, prefix, a, b, face) in SEGS.items():
        want = [w for w, _, _ in seg_words(seg)]
        for c in clips_of(prefix):
            got = [w for w, _, _ in words(c)]
            miss = [x for x in want if x not in got]
            cw, lag, tracked = anchors(c, FACE.get(c.name, face))
            rep[c.name] = dict(seg=seg, miss=miss, heard=' '.join(got), lag=round(lag, 3), tracked=round(tracked, 2))
            print(seg, c.name, 'tracked', round(tracked, 2), 'MISS' if miss else 'ok', miss, '|', ' '.join(got))
    (OUT / 'clips.json').write_text(json.dumps(rep, indent=1))


def fit_one(seg, clip, face, take=None, tempos=np.arange(0.97, 1.151, 0.01)):
    """Best in-point (and voice tempo) for one take on one clip: most of the take's words inside -45..+125 ms."""
    key = SEGS[seg][0]; a, b = SEGS[seg][2], SEGS[seg][3]
    take = take or VOX / f'{key}.wav'
    tw = words(take)[a:b]
    cw, lag, tracked = anchors(clip, face)
    pairs, j = [], 0
    for w, s_, _ in tw:
        k = next((i for i in range(j, len(cw)) if cw[i][0] == w), None)
        if k is not None:
            pairs.append((w, s_, cw[k][1])); j = k + 1
    if len(pairs) < 2:
        return None
    vs = tw[0][1]
    ts0 = np.array([p[1] for p in pairs]) - vs; cs = np.array([p[2] for p in pairs])
    best = None
    for tempo in tempos:
        ts = ts0 / tempo
        for i in range(len(pairs)):
            on = cs[i] + 0.04 - ts[i]
            d = on + ts - cs
            if d[0] < EARLY or on < 0:
                continue
            n = int(np.sum((d >= EARLY) & (d <= LATE))); err = float(np.mean(np.abs(d - 0.04)))
            if best is None or (n, -err) > (best[0], -best[1]):
                best = (n, err, round(float(on), 3), round(float(tempo), 2), [(p[0], round(float(x), 3)) for p, x in zip(pairs, d)])
    if not best:
        return None
    return dict(seg=seg, clip=clip.name, take=pathlib.Path(take).name, on=best[2], tempo=best[3], vs=round(vs / best[3], 3),
                vs_raw=round(vs, 3), words=best[0], of=len(tw), matched=len(pairs), err=round(best[1], 3), lag=round(lag, 3),
                tracked=round(tracked, 2), untracked=tracked < 0.5, table=best[4])


def takes_of(key):
    """The picked fast take plus any re-voices in audio/lines-sync/<key>-*.wav."""
    return [VOX / f'{key}.wav'] + sorted((MEDIA / 'audio/lines-sync').glob(f'{key}-*.wav'))


def cmd_fit():
    chk = json.loads((OUT / 'clips.json').read_text())
    res = {}
    by_line = {}
    for seg, (key, *_r) in SEGS.items():
        by_line.setdefault(key, []).append(seg)
    for key, segs in by_line.items():
        rows = []  # one row per (take, tempo): the best clip for every segment of the line at that take and tempo
        for take in takes_of(key):
            # the picks for 04 and 08 were already sped x1.15 (rough cut 2): cap the total near x1.25, past it a whisper warbles
            top = 1.081 if take.name in PRESPED else 1.151
            for tempo in np.arange(0.97, top, 0.01):
                pick, total, of = {}, 0, 0
                for seg in segs:
                    face = SEGS[seg][4]
                    cand = [fit_one(seg, c, FACE.get(c.name, face), take, [tempo]) for c in clips_of(SEGS[seg][1])
                            if len(chk.get(c.name, {}).get('miss', [])) <= 3]
                    cand = [x for x in cand if x]
                    if not cand:
                        break
                    b = max(cand, key=lambda x: (x['words'], -x['err']))
                    pick[seg] = b; total += b['words']; of += b['of']
                else:
                    rows.append(dict(take=take.name, tempo=round(float(tempo), 2), words=total, of=of,
                                     err=round(float(np.mean([p['err'] for p in pick.values()])), 3), segs=pick))
        rows.sort(key=lambda r: (-r['words'], r['err']))
        for seg in segs:
            res[seg] = [r['segs'][seg] for r in rows[:5]]
        r = rows[0] if rows else None
        print(key, f"{r['take']} x{r['tempo']}: {r['words']} of {r['of']} words in time (err {r['err']}s) " +
              ' '.join(f"{s_}={r['segs'][s_]['clip']}" for s_ in segs) if r else 'NO FIT')
    (OUT / 'fits.json').write_text(json.dumps(res, indent=1))


if __name__ == '__main__':
    {'check': cmd_check, 'fit': cmd_fit}[sys.argv[1]]()
