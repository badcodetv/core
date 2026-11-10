#!/usr/bin/env python3
"""Round 24 (Kai r23 at3998/at4169/at4248/at4325, 10 Nov): measure every talking clip of the row for free.
Per clip: its own audio's words (faster-whisper), the tracked mouth (mouth-track.py, cached), the lag between its own
audio and its mouth, and word anchors = own word starts + lag. Writes clips.json in the work dir.
    python3 measure_clips.py <workdir> <clip.mp4> ...
"""
import json, os, re, subprocess, sys
import numpy as np
REPO = '/home/kai/projects/badcode/badcode'
WPY = os.path.expanduser('~/.cache/badcode-whisper/venv/bin/python')
LPY = os.path.expanduser('~/.cache/badcode-lips/venv/bin/python')
FPS = 24
norm = lambda w: re.sub(r"[^a-z']", '', w.lower())


def words_of(path):
    code = ("import json,sys;from faster_whisper import WhisperModel;m=WhisperModel('small',device='cpu',compute_type='int8');"
            "r=[]\nfor p in sys.argv[1:]:\n s,_=m.transcribe(p,word_timestamps=True,language='en');r.append([[w.word,w.start,w.end] for x in s for w in x.words])\n"
            "print(json.dumps(r))")
    return code


def env(path, sr=24000):
    raw = subprocess.run(['ffmpeg', '-loglevel', 'error', '-i', path, '-ac', '1', '-ar', str(sr), '-f', 's16le', '-'],
                         capture_output=True, check=True).stdout
    x = np.frombuffer(raw, np.int16).astype(float) / 32768
    hop = sr // FPS; n = len(x) // hop
    return 20 * np.log10(np.sqrt((x[:n * hop].reshape(n, hop) ** 2).mean(1)) + 1e-9)


def main():
    work, clips = sys.argv[1], sys.argv[2:]
    os.makedirs(work, exist_ok=True)
    out_p = f'{work}/clips.json'
    out = json.load(open(out_p)) if os.path.exists(out_p) else {}
    todo = [c for c in clips if os.path.basename(c) not in out]
    if not todo:
        return
    wavs = []
    for c in todo:
        w = f'{work}/{os.path.basename(c)}.16k.wav'
        subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', '-i', c, '-ac', '1', '-ar', '16000', w], check=True)
        wavs.append(w)
    allw = json.loads(subprocess.run([WPY, '-c', words_of(None), *wavs], capture_output=True, text=True, check=True).stdout)
    for c, w in zip(todo, allw):
        strip = f'{work}/{os.path.basename(c)}-strip.jpg'
        if not os.path.exists(strip + '.json'):
            subprocess.run([LPY, f'{REPO}/scripts/lipsync/mouth-track.py', c, strip], capture_output=True)
        r = np.array([np.nan if x is None else x for x in json.load(open(strip + '.json'))['scaled']], float)
        e = env(c); n = min(len(e), len(r))
        ee = np.clip((e[:n] - (e[:n].max() - 30)) / 30, 0, 1); rr = np.nan_to_num(r[:n])
        lags = list(range(-10, 11))
        cc = [np.corrcoef(np.roll(ee, L)[12:-12], rr[12:-12])[0, 1] for L in lags]
        lag = lags[int(np.nanargmax(cc))] / FPS
        words = [[norm(a), round(s, 3), round(z, 3)] for a, s, z in w]
        out[os.path.basename(c)] = dict(path=c, heard=' '.join(x[0] for x in words), lag=round(lag, 3),
                                        corr=round(float(np.nanmax(cc)), 2), missing=int(np.isnan(r).sum()),
                                        words=words, anchors=[[x, round(s + lag, 3)] for x, s, _ in words],
                                        mouth=[None if np.isnan(v) else round(float(v), 3) for v in r])
        print(os.path.basename(c), 'lag', round(lag, 3), 'corr', out[os.path.basename(c)]['corr'], 'miss', out[os.path.basename(c)]['missing'],
              '|', ' '.join(f'{x}@{s:.2f}' for x, s, _ in words))
        json.dump(out, open(out_p, 'w'))


main()
