#!/usr/bin/env python3
"""Fire Sale: lip-sync pass (2026-11-22: "do the lip syncing"), the lip-sync-dub skill's method.

Three on-camera lines: Jim's two (voice jim-r2-d, Kai's pick) and Phineas's (phineas-a). BadCode is masked: no mouth.
For every clip of a line, the voice is laid WHOLE at one onset and one tempo (0.97-1.15); the fit is the one that puts
the most of the voice's words inside -45..+125 ms of the clip's own words (its own audio shifted by the lag to its
tracked mouth; ITU-R BT.1359), never more than 45 ms before the clip's first word. Takes = the picked take plus any
re-voices in audio/lines-sync/<line>--<voice>-*.wav (same voice, pause tags only).

The hospital clips speak a stand-in ("Here you go, love. Forty quid.": Flow refuses the real line as speech), so the
voice's "hospitals" is anchored on the clip's "here"; the other words match by name.

    python3 scripts/shorts/fire_lipsync.py check   # transcribe + mouth-track every clip -> sync/clips.json
    python3 scripts/shorts/fire_lipsync.py fit     # every take x clip -> sync/fits.json (best first)
"""
# style-lint: story=short-fire-sale
import importlib.util, json, pathlib, re, subprocess, sys
import numpy as np

REPO = pathlib.Path(__file__).resolve().parents[2]
SCENE = REPO / 'docs/stories/short-fire-sale/scenes/fire-sale'
sys.path.insert(0, str(REPO / 'scripts/drive'))
from localmap import localize  # noqa: E402

spec = importlib.util.spec_from_file_location('vrf', REPO / 'scripts/gpom/second-half-video/voice-row-fit.py')
vrf = importlib.util.module_from_spec(spec); spec.loader.exec_module(vrf)

cfg = localize(json.loads((SCENE / 'scene.json').read_text()))
MEDIA = pathlib.Path(cfg['media'])
VID, STRIPS, CAST, SYNC = MEDIA / 'video', MEDIA / 'strips', MEDIA / 'audio/casting', MEDIA / 'audio/lines-sync'
OUT = SCENE / 'sync'
FPS = 24
EARLY, LATE = -0.045, 0.125
# line -> (voice, clip glob, face)
LINES = {
    '01-hospitals': ('jim-r2-d', 'fire-sale-S02h[f-j]-S02h.mp4', 'big'),
    '02-courts': ('jim-r2-d', 'fire-sale-S03?-S03.mp4', 'big'),
    '03-allofit': ('phineas-a', 'fire-sale-S06?-S06.mp4', 'left'),
}
ALIAS = {'01-hospitals': {'hospitals': 'lots'}}  # voice word -> the stand-in's word at the same spot (S02hf-j say 'Lots of pals, love. Forty quid.'; S02hd said 'Here you go')
_W = {}


def norm(w):
    w = w.lower().replace('£', '').replace(',', '')
    w = re.sub(r"[^a-z0-9']", '', w)
    return {'40': 'forty', '50': 'fifty'}.get(w, w)


def words(path):
    path = str(path)
    if path not in _W:
        code = ("import json,sys;from faster_whisper import WhisperModel;m=WhisperModel('small',device='cpu',compute_type='int8');"
                "s,_=m.transcribe(sys.argv[1],word_timestamps=True,language='en');"
                "print(json.dumps([[w.word,w.start,w.end] for x in s for w in x.words]))")
        out = subprocess.run([vrf.WPY, '-c', code, path], capture_output=True, text=True, check=True).stdout
        _W[path] = [(norm(w), s, e) for w, s, e in json.loads(out) if norm(w)]  # vrf.words_of drops digits ("40")
    return _W[path]


def clips_of(line):
    return sorted(p for p in VID.glob(LINES[line][1]) if '-muted' not in p.name)


def takes_of(line):
    v = LINES[line][0]
    return [CAST / f'{line}--{v}.wav'] + sorted(SYNC.glob(f'{line}--{v}-*.wav'))


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
    """The clip's own words, moved by the lag between its own audio and its tracked mouth (Omni's audio drifts)."""
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
    for line, (v, _, face) in LINES.items():
        want = [ALIAS.get(line, {}).get(w, w) for w, _, _ in words(takes_of(line)[0])]
        for c in clips_of(line):
            got = [w for w, _, _ in words(c)]
            miss = [x for x in want if x not in got]
            cw, lag, tracked = anchors(c, face)
            rep[c.name] = dict(line=line, miss=miss, heard=' '.join(got), lag=round(lag, 3), tracked=round(tracked, 2))
            print(line, c.name, 'tracked', round(tracked, 2), 'lag', round(lag, 3), 'MISS' if miss else 'ok', miss, '|', ' '.join(got))
        for t in takes_of(line):
            print('  take', t.name, '|', ' '.join(w for w, _, _ in words(t)))
    (OUT / 'clips.json').write_text(json.dumps(rep, indent=1))


def fit_one(line, clip, take, tempos=np.arange(0.97, 1.151, 0.01)):
    face = LINES[line][2]
    al = ALIAS.get(line, {})
    tw = [(al.get(w, w), s, e) for w, s, e in words(take)]
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
    return dict(line=line, clip=clip.name, take=pathlib.Path(take).name, on=best[2], tempo=best[3], vs=round(vs / best[3], 3),
                words=best[0], of=len(tw), matched=len(pairs), err=round(best[1], 3), lag=round(lag, 3),
                tracked=round(tracked, 2), untracked=tracked < 0.5, table=best[4])


def cmd_fit():
    res = {}
    for line in LINES:
        rows = [f for t in takes_of(line) for c in clips_of(line) if (f := fit_one(line, c, t))]
        rows.sort(key=lambda r: (-r['words'], r['err']))
        res[line] = rows
        for r in rows[:6]:
            print(line, f"{r['take']} on {r['clip']} x{r['tempo']} at {r['on']}: {r['words']}/{r['of']} in time "
                  f"(err {r['err']}, lag {r['lag']}, tracked {r['tracked']})", r['table'])
    (OUT / 'fits.json').write_text(json.dumps(res, indent=1))



# ---- events fit (2026-11-22, cut 5): Whisper's word starts were 0.3-0.6 s off on these clips and on the takes, so the
# hospital line is fitted on EVENTS read from the picture and the sound: phrase 1 start, its lip closure (the p of
# "Hos-pitals" / the stand-in's p), phrase 1 end, phrase 2 start ("Forty"), phrase 2 end.
def _phrases(on, t, gap):
    segs, a, last = [], None, None
    for i, s in enumerate(on):
        if s:
            if a is None: a = t[i]
            elif t[i] - last > gap: segs.append((a, last)); a = t[i]
            last = t[i]
    if a is not None: segs.append((a, last))
    return segs


def mouth_events(clip, face='big', t0=0.3):
    r = mouth(clip, face); t = np.arange(len(r)) / FPS
    rr = np.nan_to_num(r); on = (rr > 0.3) & (t >= t0)  # t0: skip an opening held grin (read it off the strip)
    segs = _phrases(on, t, 0.2)
    if len(segs) < 2: return None
    gaps = [segs[i + 1][0] - segs[i][1] for i in range(len(segs) - 1)]; k = int(np.argmax(gaps))
    p1, p2 = (segs[0][0], segs[k][1]), (segs[k + 1][0], segs[-1][1])
    w = np.where((t > p1[0] + 0.15) & (t < p1[1] - 0.1))[0]
    pc = float(t[w[np.argmin(rr[w])]]) if len(w) else (p1[0] + p1[1]) / 2
    return {'on1': p1[0], 'p': pc, 'end1': p1[1] + 1 / FPS, 'on2': p2[0], 'end2': p2[1] + 1 / FPS}


def voice_events(take):
    import librosa
    y, sr = librosa.load(str(take), sr=24000); h = 240
    db = 20 * np.log10(librosa.feature.rms(y=y, frame_length=480, hop_length=h)[0] + 1e-9); t = np.arange(len(db)) * h / sr
    segs = _phrases(db > db.max() - 30, t, 0.15)
    if len(segs) < 2: return None
    gaps = [segs[i + 1][0] - segs[i][1] for i in range(len(segs) - 1)]; k = int(np.argmax(gaps))
    p1, p2 = (segs[0][0], segs[k][1]), (segs[k + 1][0], segs[-1][1])
    w = np.where((t > p1[0] + 0.12) & (t < p1[0] + 0.45))[0]
    return {'on1': p1[0], 'p': float(t[w[np.argmin(db[w])]]), 'end1': p1[1], 'on2': p2[0], 'end2': p2[1]}


def fit_events(T, ev):
    best = None
    for tp in np.arange(0.97, 1.151, 0.01):
        for anc in ('on1', 'p', 'on2'):
            fs = T[anc] + 0.04 - ev[anc] / tp
            d = {k: fs + ev[k] / tp - T[k] for k in T}
            if min(d['on1'], d['p'], d['on2']) < -0.045: continue
            n = sum(-0.045 <= d[k] <= 0.125 for k in ('on1', 'p', 'on2')) + sum(abs(d[k]) <= 0.15 for k in ('end1', 'end2'))
            err = sum(abs(d[k] - 0.04) for k in T)
            if best is None or (n, -err) > (best['n'], -best['err']):
                best = dict(n=int(n), err=round(err, 3), tempo=round(float(tp), 2), file_at=round(float(fs), 3), d={k: round(float(v), 2) for k, v in d.items()})
    return best


def cmd_events():
    line = '01-hospitals'; rows = []
    for c in clips_of(line):
        T = mouth_events(c)
        if not T: print(c.name, 'no two phrases'); continue
        print(c.name, 'mouth', {k: round(v, 2) for k, v in T.items()})
        for tk in takes_of(line):
            ev = voice_events(tk)
            if ev and (b := fit_events(T, ev)): rows.append(dict(clip=c.name, take=tk.name, **b))
    rows.sort(key=lambda r: (-r['n'], r['err']))
    for r in rows[:10]: print(r)
    (OUT / 'events-hospitals.json').write_text(json.dumps(rows, indent=1, default=float))


if __name__ == '__main__':
    {'check': cmd_check, 'fit': cmd_fit, 'events': cmd_events}[sys.argv[1]]()
