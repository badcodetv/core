#!/usr/bin/env python3
"""Word timings for a list of wav files (faster-whisper small.en, CPU int8). Prints one JSON object:
{path: {"text": heard, "words": [[word, start, end], ...]}}. Run with the whisper venv:
    ~/.cache/badcode-whisper/venv/bin/python -I whisper_words.py a.wav b.wav ..."""
import json
import subprocess
import sys

import numpy as np
from faster_whisper import WhisperModel

m = WhisperModel('small.en', device='cpu', compute_type='int8')
out = {}
for p in sys.argv[1:]:
    raw = subprocess.check_output(['ffmpeg', '-v', 'error', '-i', p, '-ac', '1', '-ar', '16000', '-f', 's16le', '-'])
    w = np.frombuffer(raw, dtype=np.int16).astype(np.float32) / 32768.0
    segs, _ = m.transcribe(w, word_timestamps=True, vad_filter=False, condition_on_previous_text=False, beam_size=5)
    ws = [x for s in segs for x in s.words]
    out[p] = {'text': ' '.join(x.word.strip() for x in ws),
              'words': [[x.word.strip(), round(x.start, 2), round(x.end, 2)] for x in ws]}
print(json.dumps(out))
