#!/usr/bin/env python3
"""Word timings for a voice take, for captions: prints JSON [[start, end, word], ...] (seconds).

    python3 scripts/word_times.py <audio>

faster-whisper (base.en) on the CPU, audio decoded by ffmpeg into memory (as scripts/transcribe.py, and for the same
reasons). Re-execs itself under ~/.venvs/whisper if faster_whisper is not importable here.
"""
import json, os, subprocess, sys

VENV = os.path.expanduser('~/.venvs/whisper/bin/python')
try:
    from faster_whisper import WhisperModel
except ImportError:
    if os.path.exists(VENV) and sys.executable != VENV:
        os.execv(VENV, [VENV, *sys.argv])
    sys.exit('faster_whisper not found (see scripts/transcribe.py)')
import numpy as np

pcm = subprocess.run(['ffmpeg', '-v', 'error', '-i', sys.argv[1], '-ac', '1', '-ar', '16000', '-f', 'f32le', '-'],
                     capture_output=True, check=True).stdout
segs, _ = WhisperModel('base.en', device='cpu', compute_type='int8').transcribe(np.frombuffer(pcm, np.float32), word_timestamps=True)
print(json.dumps([[round(w.start, 3), round(w.end, 3), w.word.strip()] for s in segs for w in s.words]))
