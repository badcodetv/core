#!/usr/bin/env python3
"""Money For Something 26 Oct shorts: the narrator voice, one WAV per transcript in voice/*.txt.

The narrator recipe Jack chose on 2026-10-03 (docs/stories/magic-money-tree/money-for-something.md, "The narrator's
voice"), copied from scripts/bank-robbery/br-narration.py: gemini-3.1-flash-tts-preview, Zubenelgenubi, Accent British
(Brixton), nothing else. Non-streaming (streaming truncates past ~60 s). Stereo. Skips files already on disk.
Free tier: 3 calls a minute, 10 a day, so it waits 21 s between calls.

usage (standard library only): GEMINI_API_KEY=... python3 mfs-voice.py <outdir> [name ...]
"""
import base64, glob, json, os, struct, sys, time, urllib.request
here = os.path.dirname(os.path.abspath(__file__))
out, only = sys.argv[1], sys.argv[2:]
os.makedirs(out, exist_ok=True)
URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-flash-tts-preview:generateContent"
def render(text):
    prompt = f"Read the following transcript based on the director's note.\n\n# Director's note\nAccent: British (Brixton).\n\n## Transcript:\n{text}"
    body = {"contents": [{"role": "user", "parts": [{"text": prompt}]}],
            "generationConfig": {"temperature": 1, "responseModalities": ["AUDIO"],
                                 "speechConfig": {"voiceConfig": {"prebuiltVoiceConfig": {"voiceName": "Zubenelgenubi"}}}}}
    req = urllib.request.Request(URL, data=json.dumps(body).encode(), headers={"Content-Type": "application/json", "x-goog-api-key": os.environ["GEMINI_API_KEY"]})
    try:
        r = json.load(urllib.request.urlopen(req, timeout=180))
    except urllib.error.HTTPError as e:
        raise RuntimeError(f"HTTP {e.code} {e.read()[:200]!r}")
    parts = r["candidates"][0]["content"]["parts"]
    return b"".join(base64.b64decode(p["inlineData"]["data"]) for p in parts if "inlineData" in p)
for f in sorted(glob.glob(os.path.join(here, "*.txt"))):
    name = os.path.basename(f)[:-4]
    if only and name not in only: continue
    path = os.path.join(out, name + ".wav")
    if os.path.exists(path): print("skip", name); continue
    text = open(f).read().strip()
    for attempt in range(1, 4):
        try:
            pcm = render(text)
            if not pcm: raise RuntimeError("no audio")
            st = b"".join(pcm[i:i + 2] * 2 for i in range(0, len(pcm) - 1, 2))
            hdr = struct.pack("<4sI4s4sIHHIIHH4sI", b"RIFF", 36 + len(st), b"WAVE", b"fmt ", 16, 1, 2, 24000, 24000 * 4, 4, 16, b"data", len(st))
            open(path, "wb").write(hdr + st)
            print(f"OK {name} {len(pcm) / 48000:.1f}s ({len(text.split())} words)", flush=True); break
        except Exception as e:
            print(f"retry {name} {attempt} {str(e)[:200]}", flush=True)
            if "PerDay" in str(e): sys.exit("daily quota spent")
            time.sleep(30 * attempt)
    time.sleep(21)
print("DONE")
