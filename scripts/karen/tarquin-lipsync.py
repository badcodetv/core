#!/usr/bin/env python3
"""Karen 10b2: place Tarquin's TTS line on the lips measured from the picture (2026-10-19).

The repo's rule (docs/video-fx/2026-10-19-lip-sync-for-dubbed-ai-clips.md, bank-robbery short-shots.md "Cut 7c"): Omni's
own audio does not follow its picture, so align to the mouth, not to the clip's speech; late audio is forgiven, early is not.
Each phrase of the take (word times from faster-whisper) is cut out, evenly stretched (ffmpeg atempo, kept within ~0.8-1.3x)
and laid at the start of its lip run (lips.py on the final clip), plus a small late bias. Then the dub's loudness envelope is
cross-correlated with the lip-motion curve to report the best shift (want ~0 to +0.1 s, audio late).
usage: tarquin-lipsync.py <take.wav> <lips.json> <out.wav> [bias_s]
"""
import json, subprocess, sys
import numpy as np

take, lipsj, out = sys.argv[1:4]; bias = float(sys.argv[4]) if len(sys.argv) > 4 else 0.04
OWN = sys.argv[5] if len(sys.argv) > 5 else None   # the clip's own speech (mono wav, clip time): each phrase is slid
# within +/-0.4 s to best match its loudness envelope (per-phrase "global" alignment, as dtwsync.py does per half)
def envl(y, sr, hop=0.01):
    h = int(sr * hop); return np.array([np.sqrt((y[j:j + h] ** 2).mean()) for j in range(0, len(y) - h, h)])
own = None
if OWN:
    own = np.frombuffer(subprocess.run(['ffmpeg', '-v', 'error', '-i', OWN, '-ac', '1', '-ar', '48000', '-f', 'f32le', '-'], capture_output=True).stdout, np.float32)
    oenv = envl(own, 48000)
SR = 48000; DUR = 15.958
# phrase: (take start, take end, target start, target end) — targets are the lip runs from lips.py
# targets = Tarquin's OWN on-screen speech (faster-whisper on the clip audio, which scores 0.58 against his lip motion at
# zero shift, i.e. it sits on the lips); the last line uses the lip run's end because his own read is too fast to match
PH = [(0.00, 0.62, 1.12, 1.66, 'Karen!'),
      (1.22, 1.92, 1.78, 2.34, 'Is that you?'),
      (2.56, 4.62, 3.26, 5.10, 'I have an urgent message for you.'),
      (5.30, 6.62, 5.38, 6.60, "For fuck's sake, listen!"),
      (7.22, 8.74, 8.60, 10.40, 'I have seen what happens if'),
      (8.78, 10.40, 11.36, 12.60, 'we do not take action!'),
      (11.34, 13.15, 13.54, 14.96, 'Christ, are you even there?!')]
# final placements fixed by hand against lips.py's runs (mouth opens 1.04, 3.38, 8.50, 11.79, 13.50): a phrase may start up
# to ~0.1 s after the mouth opens, never before (2026-10-19)
FIX = {'I have an urgent message for you.': 3.42, 'I have seen what happens if': 8.56}
mix = np.zeros((int(DUR * SR), 2), np.float32)
for t0, t1, a0, a1, txt in PH:
    tempo = min(1.32, max(0.8, (t1 - t0) / (a1 - a0)))
    raw = subprocess.run(['ffmpeg', '-v', 'error', '-ss', f'{t0}', '-t', f'{t1 - t0}', '-i', take, '-af',
                          f'silenceremove=start_periods=1:start_threshold=-38dB:start_silence=0.02,afade=t=in:d=0.015,atempo={tempo:.4f}',
                          '-ac', '2', '-ar', str(SR), '-f', 'f32le', '-'], capture_output=True).stdout
    y = np.frombuffer(raw, np.float32).reshape(-1, 2); sh = 0.0
    if own is not None:
        pe = envl(y[:, 0], SR); best = -2
        for k in range(-2, 31):          # never more than 20 ms early: early audio is the visible error
            j = int(a0 * 100) + k
            if j < 0 or j + len(pe) > len(oenv): continue
            c = np.corrcoef(pe, oenv[j:j + len(pe)])[0, 1]
            if c > best: best, sh = c, k / 100
    if txt in FIX: sh, bias_ = FIX[txt] - a0, 0.0     # checked against the lip-run onsets measured from the picture
    else: bias_ = bias
    i = int((a0 + sh + bias_) * SR)
    mix[i:i + len(y)] += y[:max(0, len(mix) - i)]
    print(f'{txt:32} take {t1 - t0:.2f}s -> {len(y) / SR:.2f}s at {a0 + sh + bias_:.2f} (x{tempo:.2f}, slid {sh:+.2f})')
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-f', 'f32le', '-ar', str(SR), '-ac', '2', '-i', '-', out], input=mix.tobytes(), check=True)
# score: dub loudness envelope against lip motion, over shifts of -0.5..+0.5 s
L = json.load(open(lipsj)); fps = L['fps']; g = np.array([x if x is not None else np.nan for x in L['gap']], float)
g = np.nan_to_num(g, nan=np.nanmean(g)); mot = np.abs(np.diff(g, prepend=g[0])); k = max(1, int(fps / 5))
mot = np.convolve(mot, np.ones(k) / k, 'same')
hop = int(SR / fps); env = np.array([np.sqrt((mix[j:j + hop, 0] ** 2).mean()) for j in range(0, len(mix) - hop, hop)])
n = min(len(env), len(mot)); env, mot = env[:n], mot[:n]
def corr(s):
    a, b = (env[s:], mot[:n - s]) if s >= 0 else (env[:n + s], mot[-s:])
    return float(np.corrcoef(a, b)[0, 1])
best = max(range(-int(fps / 2), int(fps / 2) + 1), key=corr)
print(f'sync: corr at 0 = {corr(0):.2f}; best shift {best / fps:+.3f} s (audio later than lips if +) corr {corr(best):.2f}')
