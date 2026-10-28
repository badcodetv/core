#!/usr/bin/env python3
"""Warp a TTS take onto the timing of a clip's own speech of the SAME words (2026-10-19, short cut 7b).

Jack: "for some clips you have matched the lip syncing perfectly and some are completly messed around". The clips that
sync are the ones whose own generated speech says the dub's words and sits on the moving lips (Frames mode, the exact
line in the prompt). Their own speech is then a sound-by-sound timing map for the dub. Phrase-level matching was not
enough (the take and the clip pause in different places), so this does what dialogue editors do: dynamic time warping
on MFCCs between the two utterances, then the take is cut at its own quiet moments, each piece stretched by ffmpeg's
rubberband (pitch kept) toward its mapped length (0.75-1.33x) and laid at its mapped start, seams cross-faded.

usage: dtwsync.py <tts.wav> <t0> <t1> <clip.mp4> <c0> <c1> <out.wav> [auto|warp|global]
  t0..t1: the take's speech; c0..c1: the clip's speech (seconds). Writes out.wav (48 kHz stereo) whose time 0 is c0.
run with ~/.cache/badcode-lips/venv/bin/python
"""
import subprocess, sys, tempfile, os
import numpy as np, librosa, soundfile as sf

def load(path, a, b, sr):
    raw = subprocess.run(['ffmpeg', '-v', 'error', '-ss', f'{a:.3f}', '-t', f'{b - a:.3f}', '-i', path, '-ac', '1', '-ar', str(sr), '-f', 'f32le', '-'], capture_output=True).stdout
    return np.frombuffer(raw, np.float32).copy()

def feats(y, sr, hop):
    m = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=20, hop_length=hop, n_fft=512)
    m = np.vstack([m[1:], librosa.feature.delta(m[1:])])
    return (m - m.mean(1, keepdims=True)) / (m.std(1, keepdims=True) + 1e-6)

def main(tts, t0, t1, clip, c0, c1, out):
    SR, HOP = 16000, 160                                        # 10 ms frames
    a, b = load(tts, t0, t1, SR), load(clip, c0, c1, SR)
    _, wp = librosa.sequence.dtw(feats(a, SR, HOP), feats(b, SR, HOP), metric='cosine')
    wp = wp[::-1]; na = int(np.ceil(len(a) / HOP)) + 1
    f = np.zeros(na)                                            # take frame -> clip frame
    for i in range(na):
        js = wp[wp[:, 0] == min(i, wp[-1, 0]), 1]; f[i] = js.mean() if len(js) else f[i - 1]
    f = np.maximum.accumulate(f)
    # cut points: quiet moments of the take, at least 0.22 s apart
    rms = librosa.feature.rms(y=a, frame_length=400, hop_length=HOP)[0]
    cuts = [0]
    for i in range(1, len(rms) - 1):
        if i - cuts[-1] >= 22 and rms[i] <= rms[max(0, i - 6):i + 7].min() + 1e-9: cuts.append(i)
    if na - 1 - cuts[-1] < 12: cuts[-1] = na - 1
    else: cuts.append(na - 1)
    hi = load(tts, t0, t1 + 0.05, 48000); outlen = int((c1 - c0 + 0.6) * 48000); buf = np.zeros(outlen + 48000, np.float32)
    xf = int(0.012 * 48000)
    with tempfile.TemporaryDirectory() as td:
        for k in range(len(cuts) - 1):
            i0, i1 = cuts[k], cuts[k + 1]
            src = hi[int(i0 * HOP * 3):int(i1 * HOP * 3) + xf]       # 16 kHz frame -> 48 kHz samples
            if len(src) < 64: continue
            want = max(1, f[i1] - f[i0]); ratio = float(np.clip((i1 - i0) / want, 0.75, 1.33))
            sf.write(f'{td}/s.wav', src, 48000)
            subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', f'{td}/s.wav', '-af', f'rubberband=tempo={ratio:.4f}', f'{td}/o.wav'], check=True)
            seg, _ = sf.read(f'{td}/o.wav', dtype='float32')
            if seg.ndim > 1: seg = seg.mean(1)
            n = min(len(seg), xf)
            if n: seg[:n] *= np.linspace(0, 1, n); seg[-n:] *= np.linspace(1, 0, n)
            at = int(f[i0] * HOP * 3); buf[at:at + len(seg)] += seg[:len(buf) - at]
    buf = buf[:outlen]
    # the second candidate: one shift and one even stretch, searched on the speech envelopes (no warping at all)
    env = lambda y, sr: np.log1p(50 * librosa.feature.rms(y=librosa.effects.preemphasis(y), frame_length=int(sr * 0.025), hop_length=int(sr * 0.01))[0])
    eb = env(load(clip, c0 - 0.5, c1 + 0.5, SR), SR); ea = env(a, SR)
    def score(e):                                              # best normalised correlation of an envelope against the clip's, and where
        best = (-1, 0)
        for off in range(0, max(1, len(eb) - len(e) + 1)):
            seg = eb[off:off + len(e)]
            if len(seg) < len(e): break
            c = np.corrcoef(seg, e)[0, 1]
            if c > best[0]: best = (c, off)
        return best
    gbest = (-1, 0, 1.0)
    for st in np.arange(0.82, 1.24, 0.02):
        e = np.interp(np.arange(0, len(ea) * st) / st, np.arange(len(ea)), ea)
        c, off = score(e)
        if c > gbest[0]: gbest = (c, off, st)
    eo = env(buf[::3].copy(), SR); dtw_c = np.corrcoef(eb[50:50 + len(eo)], eo[:len(eb) - 50])[0, 1] if len(eb) > 60 else -1
    if MODE == 'global' or (MODE == 'auto' and gbest[0] > dtw_c):
        c, off, st = gbest
        with tempfile.TemporaryDirectory() as td:
            sf.write(f'{td}/s.wav', hi, 48000)
            subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', f'{td}/s.wav', '-af', f'rubberband=tempo={1 / st:.4f}', f'{td}/o.wav'], check=True)
            seg, _ = sf.read(f'{td}/o.wav', dtype='float32')
        if seg.ndim > 1: seg = seg.mean(1)
        buf = np.zeros(outlen + 48000, np.float32); at = int((off * 0.01 - 0.5) * 48000)
        if at < 0: seg, at = seg[-at:], 0
        buf[at:at + len(seg)] = seg[:len(buf) - at]; buf = buf[:outlen]
        print(f'CHOSE global shift {off * 0.01 - 0.5:+.2f}s stretch {st:.2f} corr {c:.2f} (warp {dtw_c:.2f})')
    else: print(f'CHOSE warp corr {dtw_c:.2f} (global {gbest[0]:.2f})')
    sf.write(out, np.stack([buf, buf], 1), 48000, subtype='PCM_16')

MODE = 'auto'
if __name__ == '__main__':
    tts, t0, t1, clip, c0, c1, out = sys.argv[1:8]
    if len(sys.argv) > 8: MODE = sys.argv[8]   # auto | warp | global
    main(tts, float(t0), float(t1), clip, float(c0), float(c1), out)
