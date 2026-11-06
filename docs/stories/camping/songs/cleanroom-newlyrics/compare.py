"""Compare each recorded Add-Vocals take with the original Camping instrumental.

    ~/.cache/badcode-venvs/demucs/bin/python compare.py <original_instrumental.wav> <take.wav> [...]

Per take: split it (htdemucs_ft, two stems), then
- beat: cross-correlate the take's instrumental with the original in 10 s windows (onset envelopes) → offset per window
  (0 = the same beat in the same place; drift shows as a moving offset) and the correlation (≈1 = same music);
- vocals: where the take's vocal stem is active, against the map (intro 0–24.6, A 24.6–72, drop 72–90.5, B 90.5–137.5,
  drop 137.5–155.5, C 155.5–202, outro 202–215.3).
Prints one JSON line per take.
"""
import json, pathlib, subprocess, sys
import numpy as np
import soundfile as sf

ORIG = pathlib.Path(sys.argv[1])
SR = 22050
MAP = [('intro', 0, 24.6), ('A', 24.6, 72), ('drop1', 72, 90.5), ('B', 90.5, 137.5), ('drop2', 137.5, 155.5), ('C', 155.5, 202), ('outro', 202, 215.3)]


def load(p):
    out = subprocess.run(['ffmpeg', '-v', 'error', '-i', str(p), '-ac', '1', '-ar', str(SR), '-f', 'f32le', '-'], capture_output=True, check=True).stdout
    return np.frombuffer(out, dtype=np.float32)


def onset_env(x, hop=256):
    n = len(x) // hop
    frames = x[:n * hop].reshape(n, hop)
    e = np.log1p(100 * np.sqrt((frames ** 2).mean(1)))
    d = np.maximum(0, np.diff(e, prepend=e[0]))
    return (d - d.mean()) / (d.std() + 1e-9), SR / hop


def windows(a, b, rate, win=10.0, maxlag=0.5):
    res = []
    L, M = int(win * rate), int(maxlag * rate)
    for s in range(0, min(len(a), len(b)) - L - M, L):
        x = a[s:s + L]
        # Pearson per window (2026-11-06: the raw dot product ran past 1 and could not be read against a baseline)
        best = max(((float(np.corrcoef(x, b[s + k:s + k + L])[0, 1]), k) for k in range(-min(M, s), M)), key=lambda t: t[0])
        res.append({'t': round(s / rate), 'lag_ms': round(best[1] / rate * 1000), 'corr': round(best[0], 2)})
    return res


def activity(v, thresh_db=-35):
    hop = int(0.25 * SR); n = len(v) // hop
    rms = 20 * np.log10(np.sqrt((v[:n * hop].reshape(n, hop) ** 2).mean(1)) + 1e-9)
    on = rms > thresh_db
    return {name: round(float(on[int(a / 0.25):int(b / 0.25)].mean()), 2) for name, a, b in MAP}


orig = load(ORIG)
oe, rate = onset_env(orig)
for take in sys.argv[2:]:
    take = pathlib.Path(take)
    sep = take.parent / 'sep'
    stem_dir = sep / 'htdemucs_ft' / take.stem
    if not (stem_dir / 'no_vocals.wav').exists():
        subprocess.run([sys.executable, '-m', 'demucs', '-n', 'htdemucs_ft', '--two-stems', 'vocals', '-d', 'cuda', '-o', str(sep), str(take)], check=True, capture_output=True)
    inst, voc = load(stem_dir / 'no_vocals.wav'), load(stem_dir / 'vocals.wav')
    te, _ = onset_env(inst)
    # The player recording starts late (w1: 1.88 s, 2026-11-06), past the ±0.5 s window search — find the global
    # offset first over ±5 s, then shift the take so the windows only measure drift.
    n = min(len(oe), len(te)); M = int(5 * rate)
    g = max(range(-M, M + 1), key=lambda k: float(np.dot(oe[max(0, -k):n - max(0, k)], te[max(0, k):n - max(0, -k)])))
    off = g / rate
    o_env = oe
    if g > 0:
        te, inst, voc = te[g:], inst[int(off * SR):], voc[int(off * SR):]
    elif g < 0:  # the take starts EARLY (Suno trimmed the lead-in): pad it so it lines up with the original
        pad = int(-off * SR)
        te = np.concatenate([np.zeros(-g, dtype=te.dtype), te])
        inst = np.concatenate([np.zeros(pad, dtype=inst.dtype), inst]); voc = np.concatenate([np.zeros(pad, dtype=voc.dtype), voc])
    w = windows(o_env, te, rate)
    lags = [x['lag_ms'] for x in w]; corrs = [x['corr'] for x in w]
    print(json.dumps({'take': take.name, 'offset_s': round(off, 2), 'dur': round(len(load(take)) / SR, 2),
                      'beat_corr_median': round(float(np.median(corrs)), 2), 'beat_corr_min': min(corrs),
                      'lag_ms_range': [min(lags), max(lags)], 'windows': w,
                      'vocal_share_by_section': activity(voc)}))
