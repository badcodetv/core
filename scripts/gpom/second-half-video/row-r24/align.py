#!/usr/bin/env python3
"""align.py <out.json> <text> <audio>... : word start/end (s) by forced alignment of a KNOWN transcript (torchaudio
MMS_FA, ~20 ms, far tighter than whisper's 0.1-0.3 s word times, which clamp the first word to 0.00).
Cached per (audio, text). Env: ~/.cache/badcode-align/venv (torch 2.5.1 + torchaudio, CUDA). GPOM scene A round 24."""
import json, os, re, subprocess, sys
import numpy as np, torch, torchaudio
out_p, text, files = sys.argv[1], sys.argv[2], sys.argv[3:]
cache = json.load(open(out_p)) if os.path.exists(out_p) else {}
words = [re.sub(r"[^a-z]", '', w.lower()) for w in text.split()]
words = [w for w in words if w]
todo = [f for f in files if f'{f}|{text}' not in cache]
if todo:
    dev = 'cuda' if torch.cuda.is_available() else 'cpu'
    B = torchaudio.pipelines.MMS_FA
    model, tok, aligner = B.get_model(with_star=False).to(dev), B.get_tokenizer(), B.get_aligner()
    for f in todo:
        raw = subprocess.run(['ffmpeg', '-v', 'error', '-i', f, '-ac', '1', '-ar', str(B.sample_rate), '-f', 'f32le', '-'],
                             capture_output=True, check=True).stdout
        wav = torch.from_numpy(np.frombuffer(raw, np.float32).copy())[None].to(dev)
        with torch.inference_mode():
            em, _ = model(wav)
            spans = aligner(em[0], tok(words))
        ratio = wav.shape[1] / em.shape[1] / B.sample_rate
        cache[f'{f}|{text}'] = [[w, round(s[0].start * ratio, 3), round(s[-1].end * ratio, 3),
                                 round(float(np.mean([x.score for x in s])), 2)] for w, s in zip(words, spans)]
    json.dump(cache, open(out_p, 'w'))
for f in files:
    w = cache[f'{f}|{text}']
    print(os.path.basename(f), ' '.join(f'{a}@{s:.2f}-{e:.2f}' for a, s, e, _ in w))
