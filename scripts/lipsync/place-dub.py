#!/usr/bin/env python3
"""Build one dub track for a talking clip from a phrase table (2026-10-19, Karen 10b2).

Each phrase is a slice of a TTS take, evenly retimed (ffmpeg atempo, pitch kept) and laid at a time in the clip. Keep tempo
within ~0.85-1.30: past ~1.3 the voice warbles (heard on Karen review 4 and a 1.40x test). Phrases start on the mouth
openings from mouth-map.py, 0-0.1 s late, never early. Writes a 48 kHz stereo WAV the length of the clip, levelled to
--lufs (default -20.5, which sits with -18 LUFS narration once the clip's bed is under it), and prints each phrase's voice
onset so it can be checked against the mouth.
phrases.json: {"duration": 15.958, "phrases": [{"src": "take.wav", "from": 0.27, "to": 2.12, "at": 11.40, "tempo": 1.0,
                "text": "We do not take action!"}, ...]}
usage: place-dub.py <phrases.json> <out.wav> [--lufs -20.5]
"""
import json, subprocess, sys
import numpy as np
SR = 48000
spec = json.load(open(sys.argv[1])); out = sys.argv[2]
lufs = float(sys.argv[sys.argv.index('--lufs') + 1]) if '--lufs' in sys.argv else -20.5
mix = np.zeros((int(spec['duration'] * SR), 2), np.float32)
for p in spec['phrases']:
    t = p.get('tempo', 1.0); d = p['to'] - p['from']
    af = f"atrim={p['from']}:{p['to']},asetpts=PTS-STARTPTS,afade=t=in:d=0.015,afade=t=out:st={max(0, d - 0.05)}:d=0.05" + (f',atempo={t}' if t != 1 else '')
    y = np.frombuffer(subprocess.run(['ffmpeg', '-v', 'error', '-i', p['src'], '-af', af, '-ac', '2', '-ar', str(SR), '-f', 'f32le', '-'],
                                     capture_output=True, check=True).stdout, np.float32).reshape(-1, 2)
    i = int(p['at'] * SR); n = min(len(y), len(mix) - i); mix[i:i + n] += y[:n]
    rms = np.sqrt(np.convolve(y[:, 0] ** 2, np.ones(600) / 600, 'same')); on = np.argmax(rms > 10 ** (-35 / 20)) / SR
    print(f"{p.get('text', ''):34} {d:.2f}s x{t:.2f} -> {len(y) / SR:.2f}s at {p['at']:.2f}, voice on {p['at'] + on:.2f}, ends {p['at'] + len(y) / SR:.2f}")
tmp = out + '.raw.wav'
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-f', 'f32le', '-ar', str(SR), '-ac', '2', '-i', '-', tmp], input=mix.tobytes(), check=True)
m = subprocess.run(['ffmpeg', '-i', tmp, '-af', 'ebur128', '-f', 'null', '-'], capture_output=True, text=True).stderr
I = float([l for l in m.splitlines() if l.strip().startswith('I:')][-1].split()[1])
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', tmp, '-af', f'volume={lufs - I:.2f}dB,alimiter=limit=0.89:level=false', out], check=True)
subprocess.run(['rm', '-f', tmp]); print(f'wrote {out} ({I:.1f} -> {lufs} LUFS)')
