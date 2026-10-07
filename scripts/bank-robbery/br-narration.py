#!/usr/bin/env python3
"""The Bank Robbery narrator lines (2026-10-07), in the Money For Something narrator voice.

One WAV per line from br-narration.json. The prompt is word for word what the AI Studio speech page
sent when Jack chose the voice on 2026-10-03 (docs/stories/magic-money-tree/money-for-something.md,
"The narrator's voice"): model gemini-3.1-flash-tts-preview, voice Zubenelgenubi, Accent British
(Brixton), nothing else. Stereo, as scripts/aistudio-tts.py writes it. Skips files already on disk.

usage (needs only the standard library): GEMINI_API_KEY=... python3 br-narration.py <outdir> [id ...]
"""
import base64, json, os, struct, sys, time, urllib.request
here = os.path.dirname(os.path.abspath(__file__))
out, only = sys.argv[1], sys.argv[2:]
os.makedirs(out, exist_ok=True)
lines = json.load(open(os.path.join(here, "br-narration.json")))
URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-flash-tts-preview:generateContent"
def render(text):
    # Plain HTTPS, no SDK: the google-genai package is not installed on Jack's machine.
    prompt = f"Read the following transcript based on the director's note.\n\n# Director's note\nAccent: British (Brixton).\n\n## Transcript:\n{text}"
    body = {"contents": [{"role": "user", "parts": [{"text": prompt}]}],
            "generationConfig": {"temperature": 1, "responseModalities": ["AUDIO"],
                                 "speechConfig": {"voiceConfig": {"prebuiltVoiceConfig": {"voiceName": "Zubenelgenubi"}}}}}
    req = urllib.request.Request(URL, data=json.dumps(body).encode(), headers={"Content-Type": "application/json", "x-goog-api-key": os.environ["GEMINI_API_KEY"]})
    try:
        r = json.load(urllib.request.urlopen(req, timeout=180))
    except urllib.error.HTTPError as e:
        raise RuntimeError(f"HTTP {e.code} {e.read()[:160]!r}")
    parts = r["candidates"][0]["content"]["parts"]
    return b"".join(base64.b64decode(p["inlineData"]["data"]) for p in parts if "inlineData" in p)
for name, text in lines:
    if only and name not in only: continue
    path = os.path.join(out, name + ".wav")
    if os.path.exists(path): print("skip", name); continue
    for attempt in range(1, 6):
        try:
            pcm = render(text)
            if not pcm: raise RuntimeError("no audio")
            st = b"".join(pcm[i:i + 2] * 2 for i in range(0, len(pcm) - 1, 2))  # mono 16-bit 24 kHz -> stereo
            hdr = struct.pack("<4sI4s4sIHHIIHH4sI", b"RIFF", 36 + len(st), b"WAVE", b"fmt ", 16, 1, 2, 24000, 24000 * 4, 4, 16, b"data", len(st))
            open(path, "wb").write(hdr + st)
            print(f"OK {name} {len(pcm) / 48000:.1f}s", flush=True); break
        except Exception as e:
            print(f"retry {name} {attempt} {str(e)[:120]}", flush=True); time.sleep(20 * attempt)
print("DONE")
