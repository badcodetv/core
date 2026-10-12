#!/usr/bin/env python3
"""The Bank Robbery, cut 9 (2026-10-12): every narrator line in the new voice (Sadaltager, a Walthamstow note, deadpan).
usage: GEMINI_API_KEY=... python3 br-narration-v9.py <outdir> [voice]. Raw takes; the pause-closing and levelling pass is in docs/stories/bank-robbery/review-cut8.md."""
import base64, json, os, struct, sys, time, urllib.request
URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-flash-tts-preview:generateContent"
def render(voice, note, text):
    prompt = f"Read the following transcript based on the director's note.\n\n# Director's note\n{note}\n\n## Transcript:\n{text}"
    body = {"contents": [{"role": "user", "parts": [{"text": prompt}]}], "generationConfig": {"temperature": 1, "responseModalities": ["AUDIO"], "speechConfig": {"voiceConfig": {"prebuiltVoiceConfig": {"voiceName": voice}}}}}
    req = urllib.request.Request(URL, data=json.dumps(body).encode(), headers={"Content-Type": "application/json", "x-goog-api-key": os.environ["GEMINI_API_KEY"]})
    try: r = json.load(urllib.request.urlopen(req, timeout=180))
    except urllib.error.HTTPError as e: raise RuntimeError(f"HTTP {e.code} {e.read()[:160]!r}")
    return b"".join(base64.b64decode(p["inlineData"]["data"]) for p in r["candidates"][0]["content"]["parts"] if "inlineData" in p)
def save(path, voice, note, text):
    if os.path.exists(path): print("skip", path); return
    for attempt in range(1, 6):
        try:
            pcm = render(voice, note, text)
            if not pcm: raise RuntimeError("no audio")
            st = b"".join(pcm[i:i + 2] * 2 for i in range(0, len(pcm) - 1, 2))
            open(path, "wb").write(struct.pack("<4sI4s4sIHHIIHH4sI", b"RIFF", 36 + len(st), b"WAVE", b"fmt ", 16, 1, 2, 24000, 24000 * 4, 4, 16, b"data", len(st)) + st)
            print(f"OK {os.path.basename(path)} {len(pcm) / 48000:.1f}s", flush=True); return
        except Exception as e: print(f"retry {attempt} {str(e)[:120]}", flush=True); time.sleep(15 * attempt)
from concurrent.futures import ThreadPoolExecutor
VOICE = sys.argv[2] if len(sys.argv) > 2 else "Sadaltager"
NOTE = "Accent: British (London, working class, an ordinary bloke from Walthamstow in east London; everyday, not posh, not stagey cockney).\nStyle: deadpan and completely straight. A middle-aged man stating plain facts. Flat, dry, matter-of-fact, never amused, never performs or signals a joke, no smile in the voice.\nPace: brisk and even, clear articulation, short pauses."
LINES = json.load(open(os.path.join(os.path.dirname(__file__), "br-narration-v9.json")))
out = sys.argv[1]
with ThreadPoolExecutor(6) as ex:
    for n, t in LINES: ex.submit(save, f"{out}/{n}.wav", VOICE, NOTE, t)
