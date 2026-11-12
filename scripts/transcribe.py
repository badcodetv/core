#!/usr/bin/env python3
"""Transcribe audio/video files to check every word is there (voice takes, cuts).

    scripts/transcribe.py <file> [<file> ...]          # prints "file | text" (add --times for segments)

Runs faster-whisper (base.en) on the CPU with the audio decoded by ffmpeg into memory, which side-steps
the two failures hit on Jack's machine on 2026-11-12: av.open's metadata_errors TypeError and the missing
libcublas for the GPU. Re-execs itself under ~/.venvs/whisper if faster_whisper is not importable here.
"""
import os, subprocess, sys

VENV = os.path.expanduser('~/.venvs/whisper/bin/python')
try:
    from faster_whisper import WhisperModel
except ImportError:
    if os.path.exists(VENV) and sys.executable != VENV:
        os.execv(VENV, [VENV, *sys.argv])
    sys.exit('faster_whisper not found; make ~/.venvs/whisper with: python3 -m venv ~/.venvs/whisper && ~/.venvs/whisper/bin/pip install faster-whisper numpy')
import numpy as np

args = [a for a in sys.argv[1:] if a != '--times']
times = '--times' in sys.argv
if not args:
    sys.exit(__doc__)
model = WhisperModel('base.en', device='cpu', compute_type='int8')
for f in args:
    pcm = subprocess.run(['ffmpeg', '-v', 'error', '-i', f, '-ac', '1', '-ar', '16000', '-f', 'f32le', '-'],
                         capture_output=True, check=True).stdout
    segs, _ = model.transcribe(np.frombuffer(pcm, np.float32))
    segs = list(segs)
    if times:
        for s in segs:
            print(f'{f} | {s.start:6.2f}-{s.end:6.2f} | {s.text.strip()}')
    else:
        print(f'{f} | ' + ' '.join(s.text.strip() for s in segs))
