#!/usr/bin/env python3
"""The Bank Robbery SHORT (2026-10-15): the narrator lines in the cut 9 voice (Sadaltager, a Walthamstow note, deadpan).
usage: GEMINI_API_KEY=... python3 brs-narration.py <outdir> [voice]. Raw takes; the pause-closing and levelling pass is in docs/stories/bank-robbery/review-cut8.md."""
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
