"""Word timings for the 26 Oct shorts' voice takes (local faster-whisper), plus a diff against each transcript.
usage: ~/.cache/badcode-whisper/venv/bin/python words.py <voicedir>   → writes words.json beside this file"""
import os, sys, json, glob, re, difflib, subprocess
import numpy as np
from faster_whisper import WhisperModel
here = os.path.dirname(os.path.abspath(__file__)); vd = sys.argv[1]
m = WhisperModel("small.en", device="cpu", compute_type="int8"); out = {}
norm = lambda s: re.findall(r"[a-z0-9']+", s.lower())
for f in sorted(glob.glob(os.path.join(here, "*.txt"))):
    n = os.path.basename(f)[:-4]; pcm = subprocess.run(["ffmpeg", "-v", "error", "-i", os.path.join(vd, n + ".wav"), "-ac", "1", "-ar", "16000", "-f", "f32le", "-"], capture_output=True, check=True).stdout  # this venv's PyAV is too old for decode_audio
    segs, _ = m.transcribe(np.frombuffer(pcm, np.float32), word_timestamps=True, language="en")
    ws = [(w.word.strip(), round(w.start, 2), round(w.end, 2)) for s in segs for w in s.words]; out[n] = ws
    a, b = norm(open(f).read()), norm(" ".join(w[0] for w in ws))
    bad = [(t, a[i1:i2], b[j1:j2]) for t, i1, i2, j1, j2 in difflib.SequenceMatcher(None, a, b).get_opcodes() if t != "equal"]
    print(n, f"{ws[0][1]:.2f}-{ws[-1][2]:.2f}s", "MATCH" if not bad else bad)
json.dump(out, open(os.path.join(here, "words.json"), "w"), indent=0)
