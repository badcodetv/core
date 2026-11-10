#!/usr/bin/env python3
"""rowwarp.py: fit a cast-voice TTS take to an Omni talking clip, sound by sound (GPOM scene A round 24, 10 Nov 2026).

Why: round 19 fitted each take WHOLE (one onset, one tempo) and single phrases still landed 0.2-0.25 s early, because
Omni draws mouths at its own rhythm. Here the clip's OWN audio (the same words, Omni's timing) is the timing map:
  1. DTW on MFCCs, take -> clip's own audio (speech to speech: much tighter than whisper's 0.1-0.3 s word times);
  2. the take is cut only at its own quiet minima (>= MIN_SEG apart), each piece stretched with rubberband (pitch kept)
     to its mapped length, clamped to x0.87-1.18 (Tarquin warbled past ~1.2), seams cross-faded 12 ms, laid unbroken;
  3. Omni's audio drifts from its own picture, so the whole result is shifted by delta, searched -0.25..+0.15 s on the
     tracked mouth (mouth-track.py 'scaled'): loudness vs mouth-gap correlation, minus voice on a shut mouth, minus a
     heavy penalty per voice onset before the mouth opens (early is not forgiven).
Output time 0 = clip time 0. Also prints the same score for the unwarped take at its best onset/tempo (for comparison).

usage (badcode-lips venv):
  rowwarp.py fit <take.wav> <clip.mp4> <mouth.json> <c0> <c1> <out.wav> [--deltas a,b] [--json res.json]
     c0..c1 = the clip's speech span (s) to map onto.
"""
import json, os, subprocess, sys, tempfile
import numpy as np, librosa, soundfile as sf

SR, HOP = 16000, 160
LO, HI = 0.87, 1.18
MIN_SEG = 0.14
FPS = 24


def load(path, a=None, b=None, sr=SR):
    cmd = ['ffmpeg', '-v', 'error']
    if a is not None:
        cmd += ['-ss', f'{a:.3f}']
    if b is not None:
        cmd += ['-t', f'{b - (a or 0):.3f}']
    cmd += ['-i', path, '-ac', '1', '-ar', str(sr), '-f', 'f32le', '-']
    return np.frombuffer(subprocess.run(cmd, capture_output=True, check=True).stdout, np.float32).copy()


def feats(y):
    m = librosa.feature.mfcc(y=y, sr=SR, n_mfcc=20, hop_length=HOP, n_fft=512)
    m = np.vstack([m[1:], librosa.feature.delta(m[1:])])
    return (m - m.mean(1, keepdims=True)) / (m.std(1, keepdims=True) + 1e-6)


def speech_span(y, sr=SR, floor=35):
    e = 20 * np.log10(librosa.feature.rms(y=y, frame_length=400, hop_length=HOP)[0] + 1e-9)
    on = np.where(e > e.max() - floor)[0]
    return on[0] * HOP / sr, (on[-1] + 1) * HOP / sr


def dtw_map(a, b):
    _, wp = librosa.sequence.dtw(feats(a), feats(b), metric='cosine', global_constraints=True, band_rad=0.25)
    wp = wp[::-1]
    na = int(np.ceil(len(a) / HOP)) + 1
    f = np.zeros(na)
    for i in range(na):
        js = wp[wp[:, 0] == min(i, wp[-1, 0]), 1]
        f[i] = js.mean() if len(js) else f[i - 1]
    f = np.maximum.accumulate(f)
    k = 15  # smooth the step-like DTW path over ~150 ms (the pieces are >= 140 ms), keep it monotone
    fp = np.pad(f, (k, k), mode='edge')
    f = np.convolve(fp, np.ones(2 * k + 1) / (2 * k + 1), mode='same')[k:-k]
    return np.maximum.accumulate(f)


def warp(take, t0, t1, clip_audio, c0, c1):
    """The take's speech t0..t1 warped onto the clip audio's speech c0..c1. Returns (48k mono, at clip time c0), report.
    Speech RUNS (separated by >= 60 ms of quiet) keep their pieces end to end (no gaps cut into words); the silences
    between runs are free (padded or trimmed), so a pause in a different place costs nothing. A run never starts before
    its mapped start (early is not forgiven); inside a run every piece is stretched toward its mapped length, clamped."""
    a, b = load(take, t0, t1), load(clip_audio, c0, c1)
    f = dtw_map(a, b)
    rms = librosa.feature.rms(y=a, frame_length=400, hop_length=HOP)[0]
    db = 20 * np.log10(rms + 1e-9); quiet = db < db.max() - 32
    na = min(len(f), len(rms)); gap = int(MIN_SEG * 100)
    runs, i = [], 0
    while i < na:
        if quiet[i]:
            i += 1; continue
        j = i
        while j < na and not (quiet[j:j + 6].all() and j + 6 <= na):
            j += 1
        runs.append((i, min(j, na - 1))); i = j + 6
    hi = load(take, t0, t1 + 0.05, 48000)
    buf = np.zeros(int((c1 - c0 + 1.5) * 48000), np.float32)
    xf = int(0.012 * 48000)
    ratios, raw_ratios, starts = [], [], []
    pos = 0.0
    with tempfile.TemporaryDirectory() as td:
        for (r0, r1) in runs:
            cuts = [r0]
            for k in range(r0 + 1, r1):
                if k - cuts[-1] >= gap and r1 - k >= gap // 2 and rms[k] <= rms[max(r0, k - 5):k + 6].min() + 1e-9:
                    cuts.append(k)
            cuts.append(r1)
            pos = max(pos + 0.02 * 100 if starts else 0.0, f[r0])  # the run starts on its mapped start, or late
            starts.append(round(pos / 100, 3))
            for k in range(len(cuts) - 1):
                i0, i1 = cuts[k], cuts[k + 1]
                src = hi[int(i0 * HOP * 3):int(i1 * HOP * 3) + xf]
                if len(src) < 64:
                    continue
                want = max(1.0, f[i1] - pos)
                r_raw = (i1 - i0) / want
                ratio = float(np.clip(r_raw, LO, HI))
                raw_ratios.append(round(float(r_raw), 3)); ratios.append(round(ratio, 3))
                sf.write(f'{td}/s.wav', src, 48000)
                subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', f'{td}/s.wav', '-af', f'rubberband=tempo={ratio:.4f}:pitchq=quality',
                                f'{td}/o.wav'], check=True)
                seg, _ = sf.read(f'{td}/o.wav', dtype='float32')
                if seg.ndim > 1:
                    seg = seg.mean(1)
                n = min(len(seg) // 2, xf)
                if n:
                    seg[:n] *= np.linspace(0, 1, n); seg[-n:] *= np.linspace(1, 0, n)
                at = int(pos * HOP * 3)
                buf[at:at + len(seg)] += seg[:max(0, len(buf) - at)]
                pos += (len(seg) - xf) / (HOP * 3)
    buf = buf[:int((pos + 5) * HOP * 3)]
    drift = (pos - f[na - 1]) / 100
    lr = np.abs(np.log(np.array(raw_ratios))) if raw_ratios else np.array([9.0])
    return buf, dict(pieces=len(ratios), runs=len(runs), run_starts=starts, ratios=ratios, raw=raw_ratios,
                     end_drift=round(float(drift), 3), warp_cost=round(float(np.mean(lr)), 3),
                     clamped=int(sum(1 for r in raw_ratios if not LO <= r <= HI)))


def residual(voice48, at, clip_audio, c0, c1):
    """Timing error left after fitting: DTW of the fitted voice (its t=0 at clip time `at`) against the clip's own audio
    c0..c1. Returns per-10ms error (voice time - clip time, + = voice late) over the voice's speech frames."""
    v = librosa.resample(voice48, orig_sr=48000, target_sr=SR)
    lead = at - c0
    if lead >= 0:
        v = np.concatenate([np.zeros(int(lead * SR), np.float32), v])
    else:
        v = v[int(-lead * SR):]
    b = load(clip_audio, c0, c1)
    v = v[:len(b) + int(0.5 * SR)]
    _, wp = librosa.sequence.dtw(feats(v), feats(b), metric='cosine')
    wp = wp[::-1]
    rms = librosa.feature.rms(y=v, frame_length=400, hop_length=HOP)[0]
    db = 20 * np.log10(rms + 1e-9); loud = db > db.max() - 25
    err = {}
    for i, j in wp:
        if i < len(loud) and loud[i]:
            err.setdefault(i, []).append(i - j)
    e = np.array([np.mean(x) for _, x in sorted(err.items())]) / 100
    return e


def env24(y48):
    h = 2000
    n = len(y48) // h
    return 20 * np.log10(np.sqrt((y48[:n * h].reshape(n, h) ** 2).mean(1)) + 1e-9)


def score(voice48, at, r, deltas):
    """Lay voice (48k, its t=0 at clip time `at`) on mouth r (24 fps, scaled 0..1); best delta. Returns list."""
    e = env24(voice48)
    vmax = e.max(); act = e > vmax - 25
    n = len(r); ok = ~np.isnan(r); rr = np.nan_to_num(r)
    out = []
    for d in deltas:
        off = int(round((at + d) * FPS))
        v = np.zeros(n); va = np.zeros(n, bool)
        for i, x in enumerate(e):
            j = off + i
            if 0 <= j < n:
                v[j] = np.clip((x - (vmax - 30)) / 30, 0, 1); va[j] = act[i]
        if va.sum() == 0:
            continue
        corr = np.corrcoef(v[ok], rr[ok])[0, 1]
        shut = float(np.mean(rr[va & ok] < 0.08))
        # onsets: voice switches on after >= 2 quiet frames; early if the mouth is shut there and opens within 0.3 s
        early = []
        for j in range(2, n):
            if va[j] and not va[j - 1] and not va[j - 2]:
                if rr[j] < 0.25:
                    k = next((k for k in range(j, min(n, j + 8)) if rr[k] >= 0.25), None)
                    if k is not None:
                        early.append(round((k - j) / FPS, 3))
        sc = corr - 2.0 * shut - 0.5 * sum(early) * 10
        out.append(dict(delta=round(d, 3), score=round(float(sc), 3), corr=round(float(corr), 3), shut=round(shut, 3), early=early))
    return sorted(out, key=lambda x: -x['score'])


def main():
    if sys.argv[1] != 'fit':
        sys.exit(__doc__)
    take, clip, mouthj, c0, c1, out = sys.argv[2:8]
    c0, c1 = float(c0), float(c1)
    deltas = [float(x) for x in sys.argv[sys.argv.index('--deltas') + 1].split(',')] if '--deltas' in sys.argv else \
        list(np.round(np.arange(-0.45, 0.151, 1 / 48), 4))
    r = np.array([np.nan if x is None else x for x in json.load(open(mouthj))['scaled']], float)
    y = load(take)
    t0, t1 = speech_span(y)
    t0, t1 = max(0, t0 - 0.03), t1 + 0.03
    w, rep = warp(take, t0, t1, clip, c0, c1)
    sc = score(w, c0, r, deltas)
    best = sc[0]
    full = np.zeros(int((c0 + best['delta']) * 48000) + len(w) + 4800, np.float32) if c0 + best['delta'] >= 0 else None
    if full is None:
        cut = int(-(c0 + best['delta']) * 48000); w2 = w[cut:]; full = np.zeros(len(w2) + 4800, np.float32); full[:len(w2)] = w2
    else:
        s = int((c0 + best['delta']) * 48000); full[s:s + len(w)] = w
    sf.write(out, np.stack([full, full], 1), 48000, subtype='PCM_24')
    e = residual(w, c0, clip, c0, c1)  # against the clip's AUDIO (delta 0); the mouth offset is delta on top
    rep['resid'] = dict(p50=round(float(np.median(np.abs(e))), 3), p90=round(float(np.percentile(np.abs(e), 90)), 3),
                        early90=round(float(-np.percentile(e, 10)), 3), late90=round(float(np.percentile(e, 90)), 3))
    res = dict(take=take, clip=clip, take_span=[round(t0, 3), round(t1, 3)], clip_span=[c0, c1], **rep, best=best, top=sc[:4],
               out=out)
    print(json.dumps(res))
    if '--json' in sys.argv:
        json.dump(res, open(sys.argv[sys.argv.index('--json') + 1], 'w'), indent=1)


if __name__ == '__main__':
    main()
