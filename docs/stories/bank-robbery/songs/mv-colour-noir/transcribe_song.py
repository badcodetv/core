"""Word-level transcript of the stand-in song, for planning who sings or talks each line. Whisper's times are loose by 0.1-0.3 s: planning only, never lip placement."""
import json, sys, wave
import numpy as np
from faster_whisper import WhisperModel
wav, out = sys.argv[1], sys.argv[2]
model = WhisperModel("medium.en", device="cpu", compute_type="int8")
w = wave.open(wav); audio = np.frombuffer(w.readframes(w.getnframes()), dtype=np.int16).astype(np.float32) / 32768.0  # passed as an array: this venv's PyAV rejects a path
segs, info = model.transcribe(audio, word_timestamps=True, vad_filter=False, language="en", beam_size=5)
rows = []
for s in segs:
    rows.append({"start": round(s.start, 2), "end": round(s.end, 2), "text": s.text.strip(),
                 "words": [{"w": w.word.strip(), "s": round(w.start, 2), "e": round(w.end, 2)} for w in s.words]})
    print(f"{s.start:7.2f} {s.end:7.2f}  {s.text.strip()}", flush=True)
json.dump({"duration": info.duration, "segments": rows}, open(out, "w"), indent=1, ensure_ascii=False)
