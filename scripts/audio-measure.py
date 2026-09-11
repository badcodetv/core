#!/usr/bin/env python3
"""Measure an audio segment and print one JSON object — the listen server's local ears.

    python3 scripts/audio-measure.py SEG.wav

Gemini hears a 16 kbps mono copy of whatever we upload (ai.google.dev/gemini-api/docs/audio), so
it cannot judge stereo width and misses fine top-end detail. These numbers are the things it
cannot hear, measured here instead. Loudness and a trustworthy tempo are handed to Gemini as facts
it must not contradict; the stereo numbers are recorded in the ledger and never sent.

Keys are exactly the TypeScript `Measurements` interface in packages/listen-mcp/src/types.ts —
camelCase, not snake_case. Output always goes through json.dumps(allow_nan=False), so NaN or
Infinity can never reach the TypeScript side: every non-finite value becomes null or is clamped.

Needs: ffmpeg (loudness), librosa (centroid, and tempo via scripts/beat-grid.py).
Exit 1 with a message on stderr on any failure.
"""
from __future__ import annotations

import importlib.util
import json
import math
import os
import re
import subprocess
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))

# ffmpeg's ebur128 summary prints this for digital silence. Anything at or below it is "no signal".
SILENT_LUFS = -70.0
SIDE_TO_MID_CLAMP = 120.0


def loudness(path: str) -> tuple[float | None, float | None, float | None]:
    """(integrated LUFS, loudness range LU, true peak) from ffmpeg's ebur128 Summary block.

    In ffmpeg 4.4 the block reads `Integrated loudness:` → `I: … LUFS`, `Loudness range:` →
    `LRA: … LU`, and `True peak:` → `Peak: … dBFS` (the unit says dBFS although the filter was asked
    for true peak). `Threshold:` appears twice and is ignored. Keyed on each header, then the next
    value line, so a reordering inside the block cannot mismatch values.
    """
    out = subprocess.run(
        ['ffmpeg', '-nostats', '-hide_banner', '-i', path, '-af', 'ebur128=peak=true', '-f', 'null', '-'],
        capture_output=True, text=True, timeout=600,
    )
    if out.returncode != 0:
        raise RuntimeError(f'ffmpeg ebur128 failed: {out.stderr[-500:]}')
    text = out.stderr
    at = text.rfind('Summary:')
    if at < 0:
        raise RuntimeError('ffmpeg ebur128 printed no Summary block')
    lines = text[at:].splitlines()

    def after(header: str, key: str) -> float | None:
        for i, line in enumerate(lines):
            if line.strip() == header:
                for nxt in lines[i + 1:]:
                    m = re.match(rf'\s*{key}:\s*(-?inf|-?\d+(?:\.\d+)?)', nxt)
                    if m:
                        v = float(m.group(1))
                        return v if math.isfinite(v) else None
                return None
        return None

    i = after('Integrated loudness:', 'I')
    lra = after('Loudness range:', 'LRA')
    peak = after('True peak:', 'Peak')
    if i is None or i <= SILENT_LUFS:
        i, lra = None, None
    return i, lra, peak


def stereo(y: np.ndarray) -> tuple[float | None, float | None]:
    """(Pearson correlation of L and R, side-to-mid ratio in dB). Both None for mono."""
    if y.ndim == 1 or y.shape[0] < 2:
        return None, None
    left, right = y[0].astype(np.float64), y[1].astype(np.float64)

    corr = None
    if np.std(left) > 0 and np.std(right) > 0:
        c = float(np.corrcoef(left, right)[0, 1])
        corr = max(-1.0, min(1.0, c)) if math.isfinite(c) else None

    mid, side = (left + right) / 2, (left - right) / 2
    rms_m, rms_s = float(np.sqrt(np.mean(mid ** 2))), float(np.sqrt(np.mean(side ** 2)))
    if rms_m == 0 and rms_s == 0:
        s2m = None
    elif rms_s == 0:
        s2m = -SIDE_TO_MID_CLAMP
    elif rms_m == 0:
        s2m = SIDE_TO_MID_CLAMP
    else:
        s2m = max(-SIDE_TO_MID_CLAMP, min(SIDE_TO_MID_CLAMP, 20 * math.log10(rms_s / rms_m)))
    return corr, s2m


def centroid(mono: np.ndarray, sr: int) -> float:
    import librosa

    if not np.any(mono):
        return 0.0
    c = librosa.feature.spectral_centroid(y=mono, sr=sr)
    v = float(np.nanmean(c))
    return round(v, 1) if math.isfinite(v) else 0.0


def tempo(path: str) -> dict:
    """Reuse scripts/beat-grid.py's analyse() — the hyphenated file name can't be imported normally."""
    # Loading it this way would drop scripts/__pycache__/ into a shared checkout on every listen.
    sys.dont_write_bytecode = True
    spec = importlib.util.spec_from_file_location('beat_grid', os.path.join(HERE, 'beat-grid.py'))
    if spec is None or spec.loader is None:
        raise RuntimeError('cannot load scripts/beat-grid.py')
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    try:
        r = mod.analyse(path, 4, 8, None)
    except Exception:  # noqa: BLE001 — any detector failure is "no tempo", not a failed measurement
        return {'bpm': None, 'confidence': 'none'}
    bpm = r.get('bpm')
    if bpm is not None and not math.isfinite(bpm):
        bpm = None
    return {'bpm': bpm, 'confidence': r.get('confidence', 'none')}


def measure(path: str) -> dict:
    import librosa

    y, sr = librosa.load(path, sr=None, mono=False)
    channels = 1 if y.ndim == 1 else int(y.shape[0])
    samples = y.shape[-1]
    mono = y if y.ndim == 1 else np.mean(y, axis=0)

    i, lra, peak = loudness(path)
    corr, s2m = stereo(y)
    return {
        'durationSec': round(samples / sr, 3),
        'integratedLufs': i,
        'truePeakDbtp': peak,
        'loudnessRangeLu': lra,
        'channels': channels,
        'stereoCorrelation': None if corr is None else round(corr, 4),
        'sideToMidDb': None if s2m is None else round(s2m, 2),
        'spectralCentroidHz': centroid(mono, sr),
        'tempo': tempo(path),
    }


def main() -> int:
    if len(sys.argv) != 2:
        print('usage: audio-measure.py SEG.wav', file=sys.stderr)
        return 1
    path = sys.argv[1]
    if not os.path.isfile(path):
        print(f'no such file: {path}', file=sys.stderr)
        return 1
    try:
        result = measure(path)
        print(json.dumps(result, allow_nan=False))
    except Exception as e:  # noqa: BLE001
        print(f'audio-measure failed: {e}', file=sys.stderr)
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
