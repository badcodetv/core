#!/usr/bin/env python3
"""
Turn a music track into a beat/bar/phrase grid, and say whether to trust it.

Written for BadCode's drum & bass: the tempo is never a mystery (we wrote the Suno prompt),
so this is about placing a cut *precisely*, not discovering the tempo.

    scripts/beat-grid.py TRACK.wav                     # report the grid and the confidence
    scripts/beat-grid.py TRACK.wav --emit phrase       # marker times, one per 8-bar phrase
    scripts/beat-grid.py TRACK.wav --emit bar --json   # JSON ready for premiere_add_marker

🔴 Read the confidence line before using the numbers. Beat trackers return a confident answer
for material that has no beat at all — narration over a held note produces a plausible BPM and
a grid that means nothing. `confidence: none` means there is no beat, not that detection failed.

Needs: librosa (pip) and aubiotrack (apt install aubio-tools). aubio is the second opinion; if
it is missing the script still runs, but the cross-check is skipped and confidence is capped.
"""
from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
import warnings

warnings.filterwarnings('ignore')

import numpy as np

# Detected tempo is trusted when the two detectors agree to within this, after octave-folding.
AGREEMENT_TOLERANCE = 0.05
# How far each beat sits from the constant-tempo grid, after folding every gap onto the nearest
# multiple of the median (so a dropped or doubled beat does not count against regularity).
#
# 🔴 Measured on aubio's times, NEVER librosa's: librosa quantises every beat to the analysis
# hop (512 samples = 21.33ms at 48kHz), so its spread reads the same for a locked D&B track and
# for spoken narration, and tells you nothing at all.
#
# Measured across six real BadCode tracks, 2026-08-22. The one properly beat-locked track scores
# 0.45ms; every other piece of material on the drive lands between 11.8ms and 22.8ms. That 26x
# gap is what these thresholds sit in — they are not tuned, they are the empty space.
TIGHT_RESIDUAL = 0.005
LOOSE_RESIDUAL = 0.015


def octave_fold(a: float, b: float) -> tuple[float, float]:
    """Bring b within a factor of sqrt(2) of a by doubling/halving. Returns (folded, error)."""
    if a <= 0 or b <= 0:
        return b, 1.0
    best, best_err = b, abs(b - a) / a
    for mult in (0.25, 0.5, 1.0, 2.0, 4.0):
        cand = b * mult
        err = abs(cand - a) / a
        if err < best_err:
            best, best_err = cand, err
    return best, best_err


def aubio_beats(path: str) -> np.ndarray | None:
    if not shutil.which('aubiotrack'):
        return None
    try:
        out = subprocess.run(
            ['aubiotrack', '-i', path], capture_output=True, text=True, timeout=300
        ).stdout
    except (subprocess.SubprocessError, OSError):
        return None
    times = [float(line) for line in out.split() if line.strip()]
    return np.array(times) if len(times) > 4 else None


def pick_downbeat(onset_env: np.ndarray, beat_frames: np.ndarray, meter: int) -> int:
    """Which of the `meter` phases is beat one? The one carrying the most onset energy."""
    if len(beat_frames) < meter * 2:
        return 0
    strength = np.asarray([onset_env[f] if f < len(onset_env) else 0.0 for f in beat_frames])
    sums = [float(strength[phase::meter].sum()) for phase in range(meter)]
    return int(np.argmax(sums))


def analyse(path: str, meter: int, bars_per_phrase: int, start_bpm: float | None) -> dict:
    import librosa

    y, sr = librosa.load(path, sr=None, mono=True)
    duration = len(y) / sr

    # 🔴 aggregate=np.median is load-bearing, not a tuning choice. With the default mean this
    # octave-errors on real drum & bass — measured 87.89 BPM against a true 175.78 on the same
    # file. It is what beat_track uses internally when handed audio rather than an envelope.
    onset_env = librosa.onset.onset_strength(y=y, sr=sr, aggregate=np.median)
    kwargs = {'start_bpm': start_bpm} if start_bpm else {}
    tempo, beat_frames = librosa.beat.beat_track(onset_envelope=onset_env, sr=sr, **kwargs)
    tempo = float(np.atleast_1d(tempo)[0])
    beats = librosa.frames_to_time(beat_frames, sr=sr)

    if len(beats) < 4:
        return {'path': path, 'duration': duration, 'confidence': 'none',
                'why': 'fewer than four beats were found — there is nothing to build a grid on'}

    gaps = np.diff(beats)
    median_gap = float(np.median(gaps))
    detected_bpm = 60.0 / median_gap

    # Second opinion — and the only usable regularity measurement, see TIGHT_RESIDUAL.
    ab = aubio_beats(path)
    cross, iqr = None, None
    if ab is not None and len(ab) > 4:
        ab_gaps = np.diff(ab)
        ab_gap = float(np.median(ab_gaps))
        ab_bpm = 60.0 / ab_gap if ab_gap else 0.0
        iqr = float(np.percentile(ab_gaps, 75) - np.percentile(ab_gaps, 25))
        multiples = np.maximum(np.round(ab_gaps / ab_gap), 1)
        residual = float(np.median(np.abs(ab_gaps - multiples * ab_gap)))
        folded, err = octave_fold(detected_bpm, ab_bpm)
        cross = {'aubio_bpm': round(ab_bpm, 2), 'folded_to': round(folded, 2),
                 'error': round(err, 4), 'agrees': err <= AGREEMENT_TOLERANCE,
                 'aubio_iqr': round(iqr, 5), 'residual': round(residual, 5)}

    # Two independent signals, and the two ways they fail want opposite advice.
    if cross is None:
        confidence = 'unverified'
        why = 'aubiotrack is not installed, so the tempo has only one opinion behind it'
    elif not cross['agrees']:
        confidence = 'none'
        why = (f"the two detectors do not agree at any octave "
               f"({detected_bpm:.1f} against {cross['aubio_bpm']:.1f}) — this is material with no "
               f"beat to find. Narration, ambience and free time all land here. Do not cut to it")
    elif cross['residual'] <= TIGHT_RESIDUAL:
        confidence = 'high'
        why = (f"both detectors agree to {cross['error'] * 100:.1f}% after octave-folding, and "
               f"every beat sits within {cross['residual'] * 1000:.1f}ms of a constant grid")
    elif cross['residual'] <= LOOSE_RESIDUAL:
        confidence = 'fair'
        why = (f"the tempo is solid (detectors agree to {cross['error'] * 100:.1f}%) but beats "
               f"sit {cross['residual'] * 1000:.1f}ms off a constant grid — played, not "
               f"programmed. Trust the BPM; check the downbeat by ear before cutting")
    else:
        confidence = 'tempo-only'
        why = (f"the tempo is agreed to {cross['error'] * 100:.1f}% ({detected_bpm:.1f} BPM) but "
               f"the beat POSITIONS are unusable — {cross['residual'] * 1000:.1f}ms off a constant "
               f"grid. Build the grid from the BPM and a downbeat you set by hand; do not use the "
               f"emitted times")

    # A regular grid anchored on the first downbeat cuts better than the wobbly detected one.
    phase = pick_downbeat(onset_env, beat_frames, meter)
    anchor = float(beats[phase])
    bar_len = median_gap * meter
    phrase_len = bar_len * bars_per_phrase

    def grid(step: float) -> list[float]:
        n = int((duration - anchor) / step) + 1
        return [round(anchor + i * step, 4) for i in range(max(n, 0)) if anchor + i * step < duration]

    return {
        'path': path,
        'duration': round(duration, 3),
        'bpm': round(detected_bpm, 2),
        'librosa_reported_bpm': round(tempo, 2),
        'meter': meter,
        'bars_per_phrase': bars_per_phrase,
        'beat_seconds': round(median_gap, 5),
        'bar_seconds': round(bar_len, 5),
        'phrase_seconds': round(phrase_len, 5),
        'downbeat_offset': round(anchor, 4),
        'iqr': round(iqr, 5) if iqr is not None else None,
        'cross_check': cross,
        'confidence': confidence,
        'why': why,
        'grids': {'beat': grid(median_gap), 'bar': grid(bar_len), 'phrase': grid(phrase_len)},
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('track')
    ap.add_argument('--emit', choices=['beat', 'bar', 'phrase'], help='print the grid times')
    ap.add_argument('--json', action='store_true', help='machine-readable output')
    ap.add_argument('--meter', type=int, default=4, help='beats per bar (default 4)')
    ap.add_argument('--bars-per-phrase', type=int, default=8, help='D&B phrases in 8s and 16s')
    ap.add_argument('--start-bpm', type=float, help='tempo prior — the BPM you asked Suno for')
    ap.add_argument('--limit', type=int, help='cap how many grid times are emitted')
    args = ap.parse_args()

    r = analyse(args.track, args.meter, args.bars_per_phrase, args.start_bpm)

    if args.emit and 'grids' in r:
        times = r['grids'][args.emit]
        if args.limit:
            times = times[:args.limit]
        if args.json:
            print(json.dumps({'confidence': r['confidence'], 'bpm': r['bpm'],
                              'unit': args.emit, 'times': times}, indent=2))
        else:
            for t in times:
                print(f'{t:.4f}')
        return 0

    if args.json:
        print(json.dumps(r, indent=2))
        return 0

    print(f"{r['path']}  ({r['duration']}s)")
    if 'bpm' not in r:
        print(f"  confidence: {r['confidence']} — {r['why']}")
        return 1
    print(f"  {r['bpm']} BPM   beat {r['beat_seconds']}s   bar {r['bar_seconds']}s   "
          f"phrase {r['phrase_seconds']}s ({r['bars_per_phrase']} bars)")
    print(f"  first downbeat at {r['downbeat_offset']}s")
    if r['cross_check']:
        c = r['cross_check']
        print(f"  aubio says {c['aubio_bpm']} → folds to {c['folded_to']} "
              f"({c['error'] * 100:.1f}% off)")
    print(f"  confidence: {r['confidence']} — {r['why']}")
    print(f"  grid sizes: {len(r['grids']['beat'])} beats, "
          f"{len(r['grids']['bar'])} bars, {len(r['grids']['phrase'])} phrases")
    return 0


if __name__ == '__main__':
    sys.exit(main())
