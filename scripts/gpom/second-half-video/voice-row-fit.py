#!/usr/bin/env python3
"""Round 19 (Kai, 5 Nov, at3777): the row's lip sync at NATURAL picture speed. The lip-sync-dub skill's newest fix:
re-voice to the clip. For each talking clip: its own audio's word starts (faster-whisper), corrected by the lag between
its own audio and its tracked mouth (Omni's audio drifts from its picture); then TTS takes of the line in the
character's cast voice, directed to the clip's rhythm; each take scored by its word starts against the anchors; the
best laid UNBROKEN (one global tempo, 0.97-1.08) at its first word's anchor + 0.03 s. Writes phrase tables in
cut3.py's format (cut3-lip-<name>-r19-phrases.json) and dubs (cut3-lip-<name>-r19-dub.wav, clip time).

    python3 scripts/gpom/second-half-video/voice-row-fit.py anchors          # measure the clips (no TTS)
    python3 scripts/gpom/second-half-video/voice-row-fit.py voice [line...]  # 6 takes per line (billed key), score, fit
"""
import json, os, re, subprocess, sys
from concurrent.futures import ThreadPoolExecutor
import numpy as np

REPO = '/home/kai/projects/badcode/badcode'
CL = '/mnt/d/badcode-videos/gitpush-origin-master/clips/second-half'
RAW = f'{CL}/video/cut3-lip-raw'
LIP = f'{CL}/audio/cut3-lip'
OUT = f'{CL}/audio/voice3/r19-row'
WORK = f'{REPO}/docs/stories/gitpush-origin-master/scenes/second-half-a-killbots/voice-r19'
CAST = f'{REPO}/docs/stories/gitpush-origin-master/scenes/second-half-cut3-cast.json'
WPY = os.path.expanduser('~/.cache/badcode-whisper/venv/bin/python')
LPY = os.path.expanduser('~/.cache/badcode-lips/venv/bin/python')
FPS = 24

# name: (clip, who, text spoken, phrase splits (texts, in order), words that anchor the fit, direction)
LINES = {
    '6-0': ('cut3-lip-6-0-v3-t1', 'woman', "Derek. You've left the seat up. Again.",
            ['Derek.', "You've left the seat up.", 'Again.'], ['derek', "you've", 'left', 'seat', 'up'],
            "sharp, sarcastic; 'Derek.' clipped on its own, then a short beat, then 'You've left the seat up.' quick "
            "and pointed; a long pause, glaring; then one flat word, 'Again.'"),
    '7d-0c': ('cut3-lip-7d-0-v3-t6', 'man', "I'm really sorry, love.", ["I'm really sorry, love."],
              ["i'm", 'really', 'sorry', 'love'],
              "sheepish and quick, a placating mumble, the words run together; a long, drawn-out 'I'm' at the start"),
    '7-0': ('L07-0-a', 'woman', "Five years underground, and you still can't put a seat down.",
            ['Five years underground,', "and you still can't put a seat down."],
            ['five', 'years', 'underground', 'and', 'you', 'still', "can't", 'put', 'seat', 'down'],
            "brisk and cutting, the words tumbling out, building; 'Five years underground,' fast, straight into the rest"),
    '7d-1c': ('L07d-1-a', 'man', 'But the world ended, Sandra!', ['But the world ended, Sandra!'],
              ['but', 'world', 'ended', 'sandra'],
              "indignant, arms up, a burst; 'But the world ended,' then 'Sandra!' louder"),
    '7-2': ('cut3-lip-7-2-v3-t1', 'woman', "Yeah, the world ended. Doesn't mean you get to stop having manners.",
            ["Yeah, the world ended. Doesn't mean you get to stop having manners."],
            ['yeah', 'world', 'ended', "doesn't", 'mean', 'get', 'stop', 'having', 'manners'],
            "snaps straight back, quick and cutting, the words tumbling out fast, no pause after 'ended.'"),
}


def norm(w):
    return re.sub(r"[^a-z']", '', w.lower())


def words_of(path):
    code = ("import json,sys;from faster_whisper import WhisperModel;m=WhisperModel('small',device='cpu',compute_type='int8');"
            "s,_=m.transcribe(sys.argv[1],word_timestamps=True,language='en');"
            "print(json.dumps([[w.word,w.start,w.end] for x in s for w in x.words]))")
    out = subprocess.run([WPY, '-c', code, path], capture_output=True, text=True, check=True).stdout
    return [(norm(w), s, e) for w, s, e in json.loads(out)]


def env(path, hop_s=1 / FPS, sr=24000):
    raw = subprocess.run(['ffmpeg', '-loglevel', 'error', '-i', path, '-ac', '1', '-ar', str(sr), '-f', 's16le', '-'],
                         capture_output=True, check=True).stdout
    x = np.frombuffer(raw, np.int16).astype(float) / 32768
    hop = int(sr * hop_s); n = len(x) // hop
    return 20 * np.log10(np.sqrt((x[:n * hop].reshape(n, hop) ** 2).mean(1)) + 1e-9)


def mouth(clip):
    strip = f'{WORK}/{os.path.basename(clip)}-strip.jpg'
    if not os.path.exists(strip + '.json'):
        subprocess.run([LPY, f'{REPO}/scripts/lipsync/mouth-track.py', clip, strip], capture_output=True)
    return np.array([np.nan if x is None else x for x in json.load(open(strip + '.json'))['scaled']], float)


def anchors(name):
    clip, who, text, splits, keys, _ = LINES[name]
    path = f'{RAW}/{clip}.mp4'
    w = words_of(path)
    e = env(path); r = mouth(path)
    n = min(len(e), len(r))
    ee = np.clip((e[:n] - (e[:n].max() - 30)) / 30, 0, 1); rr = np.nan_to_num(r[:n])
    lags = list(range(-12, 13))
    cc = [np.corrcoef(np.roll(ee, L)[12:-12], rr[12:-12])[0, 1] for L in lags]  # audio shifted later by L frames
    lag = lags[int(np.nanargmax(cc))] / FPS
    # anchors: own-audio word starts moved by the audio->mouth lag (positive lag = the mouth is later than its audio)
    a = {}
    for k in keys:
        hit = next(((s, e_) for ww, s, e_ in w if ww == k and ww not in a), None)
        if hit:
            a[k] = round(hit[0] + lag, 3)
    op = [i / FPS for i in range(1, n) if not np.isnan(r[i]) and r[i] > .4 and (np.isnan(r[i - 1]) or r[i - 1] <= .4)]
    res = dict(clip=clip, heard=' '.join(x for x, _, _ in w), lag=round(lag, 3), corr=round(float(np.nanmax(cc)), 2),
               anchors=a, mouth_opens=[round(x, 2) for x in op], words=[[x, round(s, 2), round(e_, 2)] for x, s, e_ in w])
    return res


def main_anchors(names):
    os.makedirs(WORK, exist_ok=True)
    out = {}
    for nm in names:
        out[nm] = anchors(nm)
        print(nm, json.dumps(out[nm])[:900])
    json.dump(out, open(f'{WORK}/anchors.json', 'w'), indent=1)


# ---------------------------------------------------------------- the mouth fit
def fine_env(path, a=0.0, b=None, hop=0.01, sr=16000):
    cmd = ['ffmpeg', '-loglevel', 'error', '-i', path] + (['-af', f'atrim={a}:{b}'] if b else ['-af', f'atrim={a}']) + \
          ['-ac', '1', '-ar', str(sr), '-f', 's16le', '-']
    x = np.frombuffer(subprocess.run(cmd, capture_output=True, check=True).stdout, np.int16).astype(float) / 32768
    h = int(sr * hop); n = len(x) // h
    return 20 * np.log10(np.sqrt((x[:n * h].reshape(n, h) ** 2).mean(1)) + 1e-9)


def fit(r, e, until=None, tempos=np.arange(0.97, 1.081, 0.01), window=None):
    """Best (score, onset, tempo, detail) laying voice envelope e (10 ms hops, t=0 = the piece start) on mouth r (24 fps):
    correlation of voice energy with mouth gap, minus voiced frames on a shut mouth; the onset frame must have the mouth
    opening (no voice before the mouth opens)."""
    n = len(r) if until is None else min(len(r), int(until * FPS))
    rr = np.nan_to_num(r[:n]); ok = ~np.isnan(r[:n])
    vmax = e.max(); act = e > vmax - 25
    best = (-9, None, None, None)
    for t in tempos:
        tt = np.arange(len(e)) * 0.01 / t  # clip seconds from the onset
        dur = tt[-1]
        for k in range(-12, int((n / FPS - dur) * 48) + 1):
            on = k / 48
            if window and not (window[0] <= on <= window[1]):
                continue
            idx = np.floor((on + tt) * FPS).astype(int)
            m = (idx >= 0) & (idx < n)
            if m.sum() < len(idx) * 0.95:
                continue
            v = np.zeros(n); c = np.zeros(n)
            np.add.at(v, idx[m], np.clip((e[m] - (vmax - 30)) / 30, 0, 1)); np.add.at(c, idx[m], 1)
            v = np.where(c > 0, v / np.maximum(c, 1), 0)
            va = np.zeros(n, bool); np.logical_or.at(va, idx[m & act], True)
            f0 = int(np.floor((on + tt[np.argmax(act)]) * FPS))  # the voice onset frame
            if f0 < 0 or f0 + 1 >= n or rr[min(n - 1, f0 + 1)] < 0.3:
                continue
            if va.sum() == 0 or np.std(v[ok]) == 0:
                continue
            corr = np.corrcoef(v[ok], rr[ok])[0, 1]
            shut = np.mean(rr[va & ok] < 0.08)
            sc = corr - 2.0 * shut
            if sc > best[0]:
                best = (sc, round(on, 4), round(float(t), 3), dict(corr=round(float(corr), 3), shut=round(float(shut), 3)))
    return best


def check_v3():
    """Sanity: does the fit find the approved v3 placements of the master voices?"""
    for nm in LINES:
        clip = f"{RAW}/{LINES[nm][0]}.mp4"
        r = mouth(clip)
        ph = json.load(open(f'{LIP}/cut3-lip-{nm}-v3-phrases.json'))['phrases']
        p = ph[0] if nm != '7-0' else ph[1]
        e = fine_env(p['src'], p['from'], p['to'])
        b = fit(r, e, tempos=[p['tempo']])
        print(nm, 'v3 at', p['at'], 'tempo', p['tempo'], '-> fit', b)


WINDOW = {'6-0': (0.0, 0.6), '7d-0c': (1.5, 2.7), '7-0': (1.7, 2.7), '7d-1c': (0.2, 0.9), '7-2': (-0.2, 0.5)}
UNTIL = {'6-0': 4.2}  # 6-0: fit "Derek. You've left the seat up." before the long pause; "Again." goes over Derek


def tts(name, take):
    clip, who, text, splits, keys, direction = LINES[name]
    cast = json.load(open(CAST))['cast'][who]
    prof = re.sub(r'^Pace: .*$', 'Pace: ' + direction + '.', cast['prompt'], count=1, flags=re.M)
    os.makedirs(WORK, exist_ok=True); os.makedirs(OUT, exist_ok=True)
    pf, tf = f'{WORK}/{name}.profile.md', f'{WORK}/{name}.txt'
    open(pf, 'w').write(prof); open(tf, 'w').write(text + '\n')
    out = f'{OUT}/{name}-{take}.wav'
    if not os.path.exists(out):
        subprocess.run(f'set -a; . ./.env; set +a; uv run -q --with "google-genai<2" python3 scripts/aistudio-tts.py {tf} {out} '
                       f'--profile {pf} --voice {cast["voice"]}', shell=True, cwd=REPO, capture_output=True, check=True)
        subprocess.run([sys.executable, f'{REPO}/scripts/provenance/prov.py', 'card', out, '--kind', 'voice', '--engine',
                        'Gemini TTS', '--model', f'gemini-3.1-flash-tts-preview / {cast["voice"]}', '--tool',
                        'scripts/aistudio-tts.py (billed key) via voice-row-fit.py', '--prompt-file', pf,
                        '--setting', f'text={text}', '--why', f'round 19: re-voiced to the clip {clip} (lip sync at natural speed)'],
                       check=True, capture_output=True)
    return out


def pieces_of(name, w):
    """Split points (take seconds) between the line's phrases, from whisper word times."""
    clip, who, text, splits, keys, _ = LINES[name]
    firsts = [norm(sp.split()[0]) for sp in splits]
    starts, i = [], 0
    for f in firsts:
        while i < len(w) and w[i][0] != f:
            i += 1
        if i >= len(w):
            return None
        starts.append(i); i += 1
    bounds = []
    for k, si in enumerate(starts):
        a = w[si][1]
        b = w[starts[k + 1] - 1][2] if k + 1 < len(starts) else w[-1][2]
        bounds.append([a, b])
    for k in range(1, len(bounds)):  # split at the middle of the gap between phrases
        mid = (bounds[k - 1][1] + bounds[k][0]) / 2
        bounds[k - 1][1] = bounds[k][0] = mid
    return bounds


def score_take(name, path):
    clip = f"{RAW}/{LINES[name][0]}.mp4"
    r = mouth(clip)
    w = words_of(path)
    want = [norm(x) for x in LINES[name][2].split()]
    got = [x for x, _, _ in w]
    miss = [x for x in want if x not in got]
    b = pieces_of(name, w)
    if b is None:
        return dict(take=path, heard=' '.join(got), miss=miss, score=-9)
    # speech bounds from loudness inside the whisper span (whisper starts are loose)
    e_all = fine_env(path)
    act = np.where(e_all > e_all.max() - 40)[0]
    s0, s1 = act[0] * 0.01 - 0.03, (act[-1] + 1) * 0.01 + 0.05
    b[0][0] = max(0.0, s0); b[-1][1] = s1
    fit_to = b[1][1] if name == '6-0' else b[-1][1]  # 6-0: the first two phrases
    fit_from = b[1][0] if name == '7-0' else b[0][0]  # 7-0: only "and you still..." is on her face
    e = fine_env(path, fit_from, fit_to)
    sc, on, tempo, det = fit(r, e, until=UNTIL.get(name), window=WINDOW[name])
    if on is not None and name == '7-0':
        on = round(on - (fit_from - b[0][0]) / tempo, 4)  # back to the take's first phrase
    gaps = np.diff(np.where(e_all > e_all.max() - 40)[0]) * 0.01
    return dict(take=path, heard=' '.join(got), miss=miss, score=round(float(sc), 3), at=on, tempo=tempo, detail=det,
                bounds=[[round(x, 3), round(y, 3)] for x, y in b], speech=round(fit_to - b[0][0], 2),
                maxgap=round(float(gaps.max() - 0.01) if len(gaps) else 0, 2))


def write_fit(name, best):
    clip, who, text, splits, keys, _ = LINES[name]
    ph = []
    for (a, b), sp in zip(best['bounds'], splits):
        at = best['at'] + (a - best['bounds'][0][0]) / best['tempo']
        ph.append(dict(src=best['take'], **{'from': a, 'to': b}, at=round(at, 4), tempo=best['tempo'], text=sp))
    dur = float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0',
                                f'{RAW}/{clip}.mp4'], capture_output=True, text=True).stdout)
    spec = dict(clip=f'cut3-lip-raw/{clip}.mp4', duration=round(dur, 3), note=(
        'r19 2026-11-05 (Kai at3777: natural picture speed, lips that genuinely match): the line re-voiced to this clip '
        '(voice-row-fit.py), the best of the takes by a joint fit of its loudness on the tracked mouth, laid unbroken at '
        'one tempo; pieces split only at the take\'s own pauses.'), score=best['score'], detail=best['detail'], phrases=ph)
    pj = f'{LIP}/cut3-lip-{name}-r19-phrases.json'
    json.dump(spec, open(pj, 'w'), indent=1)
    on_face = [q for q in (ph[:2] if name == '6-0' else ph) if q['at'] >= 0]
    dj = f'{WORK}/{name}-dub.json'
    json.dump(dict(duration=spec['duration'], phrases=on_face), open(dj, 'w'), indent=1)
    dub = f'{LIP}/cut3-lip-{name}-r19-dub.wav'
    subprocess.run([sys.executable, f'{REPO}/scripts/lipsync/place-dub.py', dj, dub], check=True, capture_output=True)
    subprocess.run([sys.executable, f'{REPO}/scripts/provenance/prov.py', 'card', dub, '--kind', 'voice', '--engine', 'ffmpeg',
                    '--tool', 'scripts/lipsync/place-dub.py (voice-row-fit.py r19)', '--parent', best['take'],
                    '--why', f'round 19 dub for {clip}: one take, unbroken, x{best["tempo"]}'], check=True, capture_output=True)
    return pj


def main_voice(names, n=6):
    res = {}
    for nm in names:
        with ThreadPoolExecutor(3) as ex:
            takes = list(ex.map(lambda t: tts(nm, t), 'abcdef'[:n]))
        scored = [score_take(nm, t) for t in takes]
        # the v3 master as a baseline (tempos up to 1.15, as fitted then)
        ph = json.load(open(f'{LIP}/cut3-lip-{nm}-v3-phrases.json'))['phrases']
        base = None
        good = [x for x in scored if not x['miss'] and x['score'] > -9 and x['maxgap'] <= 1.8]
        best = max(good or scored, key=lambda x: x['score'])
        for x in scored:
            print(nm, os.path.basename(x['take']), x.get('score'), x.get('at'), x.get('tempo'), x.get('detail'), 'miss', x['miss'],
                  'speech', x.get('speech'), '|', x['heard'])
        print(nm, 'PICK', os.path.basename(best['take']), best['score'], best['at'], best['tempo'])
        if best['score'] > -9:
            write_fit(nm, best)
        res[nm] = dict(takes=scored, pick=best['take'])
    prev = json.load(open(f'{WORK}/fits.json')) if os.path.exists(f'{WORK}/fits.json') else {}
    prev.update(res)
    json.dump(prev, open(f'{WORK}/fits.json', 'w'), indent=1)


def eval_dub(name, dub, until=None):
    """corr / shut-mouth score of a dub already laid in clip time (the same measure as fit())."""
    r = mouth(f"{RAW}/{LINES[name][0]}.mp4")
    e = fine_env(dub)
    n = min(len(r), int((until or 99) * FPS))
    idx = np.floor(np.arange(len(e)) * 0.01 * FPS).astype(int); m = idx < n
    v = np.zeros(n); c = np.zeros(n); vmax = e.max()
    np.add.at(v, idx[m], np.clip((e[m] - (vmax - 30)) / 30, 0, 1)); np.add.at(c, idx[m], 1)
    v = np.where(c > 0, v / np.maximum(c, 1), 0)
    act = np.zeros(n, bool); np.logical_or.at(act, idx[m & (e > vmax - 25)], True)
    rr = np.nan_to_num(r[:n]); ok = ~np.isnan(r[:n])
    corr = np.corrcoef(v[ok], rr[ok])[0, 1]; shut = np.mean(rr[act & ok] < 0.08)
    return dict(score=round(float(corr - 2 * shut), 3), corr=round(float(corr), 3), shut=round(float(shut), 3))


def compare(names):
    for nm in names:
        u = {'6-0': 4.2}.get(nm)
        v3 = eval_dub(nm, f'{LIP}/cut3-lip-{nm}-v3-dub.wav', u)
        p19 = f'{LIP}/cut3-lip-{nm}-r19-dub.wav'
        r19 = eval_dub(nm, p19, u) if os.path.exists(p19) else None
        print(nm, 'v3', v3, 'r19', r19)


if __name__ == '__main__':
    cmd = sys.argv[1]
    names = sys.argv[2:] or list(LINES)
    if cmd == 'anchors':
        main_anchors(names)
    elif cmd == 'check':
        check_v3()
    elif cmd == 'voice':
        main_voice(names)
    elif cmd == 'compare':
        compare(names)


def cross(name, clips, voices):
    """Every (clip, voice) pair for a line: the best fit of each voice on each existing clip (no credits)."""
    global RAW
    out = []
    for cl in clips:
        r = mouth(f'{RAW}/{cl}.mp4')
        for v, a, b in voices:
            e = fine_env(v, a, b)
            sc, on, t, det = fit(r, e, window=(0.0, 4.5))
            out.append((sc, cl, os.path.basename(v), on, t, det))
    out.sort(key=lambda x: -x[0])
    for o in out[:12]:
        print(name, o)
    return out
