#!/usr/bin/env python3
"""The Den: lip-sync pass on the picked clips (the lip-sync-dub skill's method).

On-camera talkers: the minister (MIN1a pitch, MIN2a "good feeling"), the nurse (NURSEc) and three investors' "I'm out"
(INVAb, INVCa, INVDa). BadCode is masked: no mouth, his lines are laid over.
For each line, every take of the locked voice is laid WHOLE at one onset and one tempo (0.97-1.15); the fit is the one
that puts the most of the voice's words inside -45..+125 ms of the clip's own words (its own audio shifted by the lag
to its tracked mouth), never more than 45 ms before the clip's first word.

    ~/.cache/badcode-lips/venv/bin/python scripts/shorts/den_lipsync.py check   # transcribe + track -> sync/clips.json
    ~/.cache/badcode-lips/venv/bin/python scripts/shorts/den_lipsync.py fit     # takes x clip -> sync/fits.json
"""
# style-lint: story=short-the-den
import importlib.util, json, pathlib, re, subprocess, sys
import numpy as np

REPO = pathlib.Path(__file__).resolve().parents[2]
SCENE = REPO / 'docs/stories/short-the-den/scenes/the-den'
sys.path.insert(0, str(REPO / 'scripts/drive'))
from localmap import localize  # noqa: E402

spec = importlib.util.spec_from_file_location('vrf', REPO / 'scripts/gpom/second-half-video/voice-row-fit.py')
vrf = importlib.util.module_from_spec(spec); spec.loader.exec_module(vrf)

cfg = localize(json.loads((SCENE / 'scene.json').read_text()))
MEDIA = pathlib.Path(cfg['media'])
VID, STRIPS, AUD = MEDIA / 'video', MEDIA / 'strips', MEDIA / 'audio'
OUT = SCENE / 'sync'
FPS = 24
EARLY, LATE = -0.045, 0.125
# line -> (picked clip, [takes, picked first], face)
LINES = {
    '02-minister-pitch': ('the-den-MIN1a-MIN.mp4', ['lines/02-minister-pitch--b.wav', 'lines/02-minister-pitch--a.wav'], 'big'),
    '04-minister-feeling': ('the-den-MIN2a-MIN.mp4', ['lines/04-minister-feeling--b.wav', 'lines/04-minister-feeling--a.wav'], 'big'),
    '05a-inv-a-out': ('the-den-INVAb-INVA.mp4', ['casting/inv-a--en-gb-tutor-5.wav'], 'big'),
    '05c-inv-c-out': ('the-den-INVCa-INVC.mp4', ['casting/inv-c--en-gb-assistant-5.wav'], 'big'),
    '05d-inv-d-out': ('the-den-INVDa-INVD.mp4', ['casting/inv-d--en-gb-assistant-6.wav'], 'big'),
    '06-nurse': ('the-den-NURSEc-NURSE.mp4', ['casting/nurse--en-gb-advisor-7.wav'], 'big'),
}
_W = {}


def norm(w):
    w = w.lower().replace('£', '').replace(',', '')
    w = re.sub(r"[^a-z0-9']", '', w)
    return {'2': 'two', 'around': 'round'}.get(w, w)


def words(path):
    path = str(path)
    if path not in _W:
        code = ("import json,sys;from faster_whisper import WhisperModel;m=WhisperModel('small',device='cpu',compute_type='int8');"
                "s,_=m.transcribe(sys.argv[1],word_timestamps=True,language='en');"
                "print(json.dumps([[w.word,w.start,w.end] for x in s for w in x.words]))")
        out = subprocess.run([vrf.WPY, '-c', code, path], capture_output=True, text=True, check=True).stdout
        _W[path] = [(norm(w), s, e) for w, s, e in json.loads(out) if norm(w)]
    return _W[path]


def mouth(clip, face):
    STRIPS.mkdir(exist_ok=True)
    strip = STRIPS / f'{clip.name}-strip.jpg'
    jp = pathlib.Path(str(strip) + '.json')
    if not jp.exists():
        subprocess.run([vrf.LPY, str(REPO / 'scripts/lipsync/mouth-track.py'), str(clip), str(strip), '--face', face], capture_output=True)
    if not jp.exists():
        return np.full(int(round(vrf.env(str(clip)).shape[0])), np.nan)
    js = json.load(open(jp))
    return np.array([np.nan if x is None else x for x in js['scaled']], float)


def anchors(clip, face):
    """The clip's own words, moved by the lag between its own audio and its tracked mouth."""
    w = words(clip); e = vrf.env(str(clip)); r = mouth(clip, face)
    n = min(len(e), len(r))
    ee = np.clip((e[:n] - (e[:n].max() - 30)) / 30, 0, 1); rr = np.nan_to_num(r[:n])
    tracked = float(np.mean(~np.isnan(r)))
    lag = 0.0
    if tracked >= 0.5:
        lags = list(range(-12, 13))
        cc = [np.corrcoef(np.roll(ee, L)[12:-12], rr[12:-12])[0, 1] for L in lags]
        lag = lags[int(np.nanargmax(cc))] / FPS
    return [(x, s + lag) for x, s, _ in w], lag, tracked


def cmd_check():
    OUT.mkdir(exist_ok=True)
    rep = {}
    for line, (clip, takes, face) in LINES.items():
        c = VID / clip
        cw, lag, tracked = anchors(c, face)
        rep[line] = dict(clip=clip, heard=' '.join(w for w, _ in cw), lag=round(lag, 3), tracked=round(tracked, 2),
                         takes={t: ' '.join(w for w, _, _ in words(AUD / t)) for t in takes})
        print(line, clip, 'tracked', round(tracked, 2), 'lag', round(lag, 3), '|', rep[line]['heard'])
    (OUT / 'clips.json').write_text(json.dumps(rep, indent=1))


def fit_one(line, clip, take, tempos=np.arange(0.97, 1.151, 0.01)):
    face = LINES[line][2]
    tw = words(take)
    cw, lag, tracked = anchors(clip, face)
    pairs, j = [], 0
    for w, s_, _ in tw:
        k = next((i for i in range(j, len(cw)) if cw[i][0] == w), None)
        if k is not None:
            pairs.append((w, s_, cw[k][1])); j = k + 1
    if not pairs:
        return None
    vs = tw[0][1]
    ts0 = np.array([p[1] for p in pairs]) - vs; cs = np.array([p[2] for p in pairs])
    best = None
    for tempo in (tempos if len(pairs) > 1 else [1.0]):
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
    # on = where the take's FIRST WORD lands in clip time; file_at = where the file starts (its lead-in silence before it)
    return dict(line=line, clip=clip.name, take=take.name, on=best[2], tempo=best[3], file_at=round(best[2] - vs / best[3], 3),
                words=best[0], of=len(tw), matched=len(pairs), err=round(best[1], 3), lag=round(lag, 3),
                tracked=round(tracked, 2), table=best[4])


def cmd_fit():
    res = {}
    for line, (clip, takes, face) in LINES.items():
        rows = [f for t in takes if (f := fit_one(line, VID / clip, AUD / t))]
        rows.sort(key=lambda r: (-r['words'], r['err']))
        res[line] = rows
        for r in rows:
            print(line, f"{r['take']} on {r['clip']} x{r['tempo']} file at {r['file_at']}: {r['words']}/{r['of']} in time "
                  f"(err {r['err']}, lag {r['lag']}, tracked {r['tracked']})", r['table'])
    (OUT / 'fits.json').write_text(json.dumps(res, indent=1))


if __name__ == '__main__':
    {'check': cmd_check, 'fit': cmd_fit}[sys.argv[1]]()
