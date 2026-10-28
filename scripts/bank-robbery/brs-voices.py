#!/usr/bin/env python3
"""The Bank Robbery SHORT, cut 2 (2026-10-15): each character's lines as voice-over (Jack: mute the clips, a TTS voice
for each character as they talk). Same engine as aistudio.google.com/generate-speech (gemini-3.1-flash-tts-preview),
the same preset as each Flow Character. Two takes a line into <outdir>/take1, take2.
usage: GEMINI_API_KEY=... python3 brs-voices.py <outdir> [ids...]"""
import json, os, sys
sys.path.insert(0, os.path.dirname(__file__))
from concurrent.futures import ThreadPoolExecutor
import importlib.util
spec = importlib.util.spec_from_file_location('nar', os.path.join(os.path.dirname(__file__), 'brs-tts-lib.py')); nar = importlib.util.module_from_spec(spec); spec.loader.exec_module(nar)
J = json.load(open(os.path.join(os.path.dirname(__file__), 'brs-voices.json')))
out = sys.argv[1]; only = set(sys.argv[2:])
with ThreadPoolExecutor(6) as ex:
    for take in (1, 2):
        os.makedirs(f'{out}/take{take}', exist_ok=True)
        for i, who, text in J['lines']:
            if only and i not in only: continue
            v = J['voices'][who]; ex.submit(nar.save, f'{out}/take{take}/{i}.wav', v['voice'], v['note'], text)
