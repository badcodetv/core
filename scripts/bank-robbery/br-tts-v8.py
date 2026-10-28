#!/usr/bin/env python3
"""The Bank Robbery, cut 8 (2026-10-09): three spoken lines made in AI Studio speech, not in Flow.

- n29b: the narrator's line 29 with Jack's wording ("every pound she has, worth less"), same voice and note as br-narration.py.
- panel-q, guard-q: two lines by people who are not Flow Characters and are seen only from behind. Flow gave them
  American voices (Frames mode has no saved voice), so they are spoken here and laid over the picture.
usage: GEMINI_API_KEY=... python3 br-tts-v8.py <outdir> [id ...]
"""
import base64, json, os, struct, sys, time, urllib.request
out, only = sys.argv[1], sys.argv[2:]
URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-flash-tts-preview:generateContent"
LINES = [
 ("n29b-s11-crime-number", "Zubenelgenubi", "Accent: British (Brixton).", "And it was. Take a pound off someone and they call the police. Make every pound she has, worth less, and there isn't a crime number for that."),
 ("v8-panel-q", "Gacrux", "Accent: British (received pronunciation, southern England). An elderly committee chairwoman, slow, dry and unimpressed, speaking across a quiet room.", "If we let you go, what would you do?"),
 ("v8-guard-q", "Algieba", "Accent: British (London, working class). A middle-aged bank security guard, puzzled, calling across a cellar.", "You're putting it in?"),
]
def render(voice, note, text):
    prompt = f"Read the following transcript based on the director's note.\n\n# Director's note\n{note}\n\n## Transcript:\n{text}"
    body = {"contents": [{"role": "user", "parts": [{"text": prompt}]}], "generationConfig": {"temperature": 1, "responseModalities": ["AUDIO"], "speechConfig": {"voiceConfig": {"prebuiltVoiceConfig": {"voiceName": voice}}}}}
    req = urllib.request.Request(URL, data=json.dumps(body).encode(), headers={"Content-Type": "application/json", "x-goog-api-key": os.environ["GEMINI_API_KEY"]})
    try: r = json.load(urllib.request.urlopen(req, timeout=180))
    except urllib.error.HTTPError as e: raise RuntimeError(f"HTTP {e.code} {e.read()[:160]!r}")
    return b"".join(base64.b64decode(p["inlineData"]["data"]) for p in r["candidates"][0]["content"]["parts"] if "inlineData" in p)
for name, voice, note, text in LINES:
    if only and name not in only: continue
    path = os.path.join(out, name + ".wav")
    if os.path.exists(path): print("skip", name); continue
    for attempt in range(1, 6):
        try:
            pcm = render(voice, note, text)
            if not pcm: raise RuntimeError("no audio")
            st = b"".join(pcm[i:i + 2] * 2 for i in range(0, len(pcm) - 1, 2))
            open(path, "wb").write(struct.pack("<4sI4s4sIHHIIHH4sI", b"RIFF", 36 + len(st), b"WAVE", b"fmt ", 16, 1, 2, 24000, 24000 * 4, 4, 16, b"data", len(st)) + st)
            print(f"OK {name} {len(pcm) / 48000:.1f}s", flush=True); break
        except Exception as e: print(f"retry {name} {attempt} {str(e)[:120]}", flush=True); time.sleep(20 * attempt)
print("DONE")
