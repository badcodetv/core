#!/usr/bin/env python3
"""wordwarp.py: lay a cast-voice TTS take on an Omni talking clip WORD BY WORD (GPOM scene A round 24, 10 Nov 2026).

Round 19 fitted each take whole (one onset, one tempo): single phrases landed 0.2-0.25 s early. Rhythm differs inside
the line, so here every word start of the take is anchored on the same word in the clip:
  target(word) = the word's start in the clip's OWN audio (forced alignment, align.py)  -  lag  +  LATE
  lag  = how late Omni's own audio runs against its own mouth (row-measure on the clip with its own audio, per clip)
  LATE = 0.03 s (late is forgiven, early is not).
Between anchors the take is cut only at word starts. Silence in the take (a pause >= 50 ms) is trimmed or padded
freely; speech is stretched with rubberband (pitch kept) by at most x0.87-1.18; any shortfall carries to the next word
(the next piece starts late, never early). Small words (< 70 ms, 'a', 'to') ride with the word before them.
Output: wav in CLIP time (t=0 = clip frame 0) + a json with each word's target, placed start, error and tempo.

  wordwarp.py <take.wav> <take_words.json-key> <clip_words> <lag> <out.wav>   (called from fitline.py)
"""
import json, subprocess, sys, tempfile
import numpy as np, soundfile as sf

LO, HI, LATE, SR = 0.87, 1.18, 0.04, 48000
FREE_GAP = 0.10  # the pause before a free word (no anchor) is capped: 'up... Again.' plays as one sentence (Kai at3201)
XF = int(0.010 * SR)


def load(path):
    raw = subprocess.run(['ffmpeg', '-v', 'error', '-i', path, '-ac', '1', '-ar', str(SR), '-f', 'f32le', '-'],
                         capture_output=True, check=True).stdout
    return np.frombuffer(raw, np.float32).copy()


def stretch(x, ratio, td):
    if abs(ratio - 1) < 0.004:
        return x.copy()
    sf.write(f'{td}/s.wav', x, SR)
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', f'{td}/s.wav', '-af', f'rubberband=tempo={ratio:.4f}:pitchq=quality',
                    f'{td}/o.wav'], check=True)
    y, _ = sf.read(f'{td}/o.wav', dtype='float32')
    return y.mean(1) if y.ndim > 1 else y


def merge_small(words, min_len=0.07):
    out = []
    for w in words:
        if out and w[1] is not None and out[-1][1] is not None and (w[2] - w[1]) < min_len:
            out[-1] = [out[-1][0] + ' ' + w[0], out[-1][1], w[2]]
        else:
            out.append([w[0], w[1], w[2]])
    return out


def plan(take_w, clip_w, lag, late=LATE, lo=LO, hi=HI):
    """Pure timing plan (no audio). Per word: the piece = the word (+30 ms) and its silent tail up to the next word.
    start = max(where we are, the word's target): we never start early; a late start carries.
    A tail that is a real pause (>= 50 ms) is free: speech keeps tempo 1.0 and the pause takes up the difference (or the
    word is squeezed up to x1.18 if there is no room). Words run together: one tempo x0.87-1.18 to reach the next target,
    and only past x0.87 a short silence is added (counted as 'pads')."""
    tw, cw = merge_small(take_w), merge_small(clip_w)
    if [w[0] for w in tw] != [w[0] for w in cw]:
        tw, cw = take_w, clip_w
    assert [w[0] for w in tw] == [w[0] for w in cw], (tw, cw)
    tgt = [None if c[1] is None else c[1] - lag + late for c in cw]  # None = free: follows at the take's own pace
    rows, pos = [], -9.0
    for k, (w, s, e) in enumerate(tw):
        last = k + 1 == len(tw)
        nxt = e + 0.03 if last else tw[k + 1][1]
        start = pos if tgt[k] is None else max(pos, tgt[k])
        tail = 0.0 if last else max(0.0, nxt - (e + 0.03))
        pause = tail >= 0.05
        body = (nxt - s) - (tail if pause else 0.0)
        if last:
            tempo, out_gap = (rows[-1]['tempo'] if rows else 1.0), 0.0
        else:
            room = min(nxt - s, body + FREE_GAP) if tgt[k + 1] is None else tgt[k + 1] - start
            if pause:
                tempo = 1.0 if room >= body else float(min(hi, body / max(room, 1e-3)))
            else:
                tempo = float(np.clip(body / max(room, 1e-3), lo, hi))
            out_gap = max(0.0, room - body / tempo)
            if not pause and out_gap < 0.02:
                out_gap = 0.0
        gap_in = tail if pause else 0.0
        rows.append(dict(word=w, gap_in=round(gap_in, 3), take=[round(s, 3), round(s + body, 3)], target=None if tgt[k] is None else round(tgt[k], 3), placed=round(start, 3),
                         err=0.0 if tgt[k] is None else round(start - tgt[k], 3), free=tgt[k] is None, tempo=round(tempo, 3), pause=pause, gap_out=round(out_gap, 3)))
        pos = start + body / tempo + out_gap
    return rows


def render(take, rows, out):
    """Returns origin: the CLIP time of the wav's t=0 (negative when the first word must lead the picture)."""
    x = load(take)
    origin = min(0.0, rows[0]['placed'] - 0.03)
    buf = np.zeros(int((rows[-1]['placed'] - origin + 3) * SR), np.float32)
    with tempfile.TemporaryDirectory() as td:
        for r in rows:
            a, b = int(r['take'][0] * SR), int(r['take'][1] * SR)
            seg = stretch(x[max(0, a - XF // 2):b + XF // 2], r['tempo'], td)
            n = min(len(seg) // 2, XF)
            seg[:n] *= np.linspace(0, 1, n); seg[-n:] *= np.linspace(1, 0, n)
            at = int((r['placed'] - origin) * SR) - XF // 2
            if at < 0:
                seg, at = seg[-at:], 0
            buf[at:at + len(seg)] += seg[:len(buf) - at]
    nz = np.nonzero(np.abs(buf) > 1e-5)[0]
    buf = buf[:nz[-1] + SR // 4] if len(nz) else buf
    sf.write(out, np.stack([buf, buf], 1), SR, subtype='PCM_24')
    return round(origin, 4)


def summary(rows):
    e = np.array([r['err'] for r in rows]); t = np.array([r['tempo'] for r in rows])
    pads = sum(1 for r in rows if not r['pause'] and r['gap_out'] > 0)
    added = sum(max(0.0, r['gap_out'] - r.get('gap_in', 0)) for r in rows[:-1])
    worst_add = max([max(0.0, r['gap_out'] - r.get('gap_in', 0)) for r in rows[:-1]] or [0])
    return dict(pads=pads, max_late=round(float(e.max()), 3), mean_late=round(float(e.mean()), 3), max_early=round(float(-min(0, e.min())), 3),
                tempo_lo=round(float(t.min()), 3), tempo_hi=round(float(t.max()), 3),
                added=round(added, 3), worst_add=round(worst_add, 3),
                cost=round(float(e.mean() + 0.5 * e.max() + np.mean(np.abs(np.log(t))) + 0.15 * added + 0.3 * max(0, worst_add - 0.15)), 3))
