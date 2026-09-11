"""Tests for scripts/audio-measure.py — synthetic signals only, written with numpy + wave.

Run: python3 -m unittest scripts/test_audio_measure.py -v
"""
import json
import os
import subprocess
import sys
import tempfile
import unittest
import wave

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
SCRIPT = os.path.join(HERE, 'audio-measure.py')
KEYS = {
    'durationSec', 'integratedLufs', 'truePeakDbtp', 'loudnessRangeLu', 'channels',
    'stereoCorrelation', 'sideToMidDb', 'spectralCentroidHz', 'tempo',
}


def write_wav(path: str, left: np.ndarray, right: np.ndarray | None, sr: int = 44100) -> None:
    chans = [left] if right is None else [left, right]
    data = np.stack(chans, axis=1)
    pcm = np.clip(np.round(data * 32767), -32768, 32767).astype('<i2')
    with wave.open(path, 'wb') as w:
        w.setnchannels(len(chans))
        w.setsampwidth(2)
        w.setframerate(sr)
        w.writeframes(pcm.tobytes())


def run(path: str) -> tuple[dict, str]:
    out = subprocess.run([sys.executable, SCRIPT, path], capture_output=True, text=True, timeout=300)
    if out.returncode != 0:
        raise AssertionError(f'exit {out.returncode}: {out.stderr}')
    return json.loads(out.stdout), out.stdout


def sine(freq: float, seconds: float, amp: float, sr: int = 44100) -> np.ndarray:
    t = np.arange(int(seconds * sr)) / sr
    return amp * np.sin(2 * np.pi * freq * t)


class AudioMeasureTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.TemporaryDirectory()

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()

    def path(self, name: str) -> str:
        return os.path.join(self.tmp.name, name)

    def test_identical_channels(self):
        rng = np.random.default_rng(1)
        x = 0.3 * rng.standard_normal(44100 * 3)
        p = self.path('same.wav')
        write_wav(p, x, x)
        m, _ = run(p)
        self.assertEqual(set(m), KEYS)
        self.assertEqual(m['channels'], 2)
        self.assertGreaterEqual(m['stereoCorrelation'], 0.999)
        self.assertLessEqual(m['sideToMidDb'], -100)

    def test_inverted_channels(self):
        rng = np.random.default_rng(2)
        x = 0.3 * rng.standard_normal(44100 * 3)
        p = self.path('inverted.wav')
        write_wav(p, x, -x)
        m, raw = run(p)
        self.assertLessEqual(m['stereoCorrelation'], -0.999)
        json.loads(raw)  # no NaN / Infinity may reach the TypeScript side

    def test_sine_loudness(self):
        amp = 10 ** (-20 / 20)
        x = sine(1000, 5, amp)
        p = self.path('sine.wav')
        write_wav(p, x, x)
        m, _ = run(p)
        # BS.1770: -3 dB for a sine's RMS, +3 dB for summing two channels → ≈ -20 LUFS.
        self.assertAlmostEqual(m['integratedLufs'], -20, delta=1.5)
        self.assertGreater(m['spectralCentroidHz'], 500)

    def test_mono(self):
        p = self.path('mono.wav')
        write_wav(p, sine(440, 3, 0.3), None)
        m, _ = run(p)
        self.assertEqual(m['channels'], 1)
        self.assertIsNone(m['stereoCorrelation'])
        self.assertIsNone(m['sideToMidDb'])

    def test_click_tempo(self):
        sr = 48000
        bpm = 174
        x = np.zeros(sr * 10)
        step = 60 / bpm
        # A 20 ms decaying noise burst. A 10 ms windowed sine blip is too faint for librosa's
        # median-aggregated onset envelope: it found fewer than four beats (measured 2026-09-11).
        n = int(0.02 * sr)
        click = 0.5 * np.random.default_rng(3).standard_normal(n) * np.exp(-np.linspace(0, 8, n))
        t = 0.0
        while t < 10 - 0.1:
            i = int(t * sr)
            x[i:i + len(click)] += click
            t += step
        p = self.path('clicks.wav')
        write_wav(p, x, x, sr)
        m, _ = run(p)
        got = m['tempo']['bpm']
        self.assertIsNotNone(got)
        self.assertTrue(any(abs(got - b) <= 3 for b in (bpm, bpm / 2, bpm * 2)), got)
        self.assertNotEqual(m['tempo']['confidence'], 'none')

    def test_silence(self):
        x = np.zeros(44100 * 3)
        p = self.path('silence.wav')
        write_wav(p, x, x)
        m, raw = run(p)
        self.assertIsNone(m['integratedLufs'])
        self.assertIsNone(m['loudnessRangeLu'])
        self.assertIsNone(m['truePeakDbtp'])
        self.assertIsNone(m['stereoCorrelation'])
        self.assertEqual(m['tempo']['confidence'], 'none')
        json.loads(raw)


if __name__ == '__main__':
    unittest.main()
