#!/usr/bin/env python3
"""qa.py: scan a generated still or clip for defects BEFORE a person sees it (Jack, 2026-11-25: "when you show me an
image you've made with an obvious problem, why can't you see it and fix it … is there a way for you to scan the
image/video for problems and then fix it").

A vision model (Gemini, the key in .env) answers one yes/no question per checklist item, with evidence and where in
the frame. A still is sent whole plus four zoomed quarters (small faults such as shirt numbers, extra hands, levitating
feet show up only when zoomed). Optional reference images (the stadium) go in for the consistency question. A clip is
sent whole (inline, under 15 MB) and judged on the clip checklist.

    python3 qa.py <checklist.json> <image-or-clip> [more files…] [--ref ref.jpg …] [--prompt "…"] [--json out.json]

Exit 0 = every file passes, 1 = at least one fails. Prints one line per file and each failed item with its fix hint.
Recipe and sources: RESEARCH.md beside this file. The checklist is per project (start from
checklists/generic.json): {"still": [{"id","q","fail_if","fix"}…], "clip": [...]}.
"""
import argparse, base64, io, json, os, sys, time, urllib.request, urllib.error
from pathlib import Path

MODELS = ["gemini-3.5-flash", "gemini-3-flash-preview", "gemini-2.5-flash"]
ENDPOINT = "https://generativelanguage.googleapis.com/v1beta/models/{m}:generateContent"


def key():
    """GEMINI_API_KEY from the environment, else from a .env in the current folder or any folder above it."""
    if os.environ.get("GEMINI_API_KEY"):
        return os.environ["GEMINI_API_KEY"]
    for d in [Path.cwd(), *Path.cwd().parents, Path(__file__).resolve().parent]:
        env = d / ".env"
        if env.exists():
            for line in env.read_text().splitlines():
                line = line.strip().removeprefix("export ")
                if line.startswith("GEMINI_API_KEY="):
                    return line.split("=", 1)[1].strip().strip('"\'')
    sys.exit("GEMINI_API_KEY not found (set it, or put GEMINI_API_KEY=... in a .env)")


def jpeg_part(img, maxside=1600):
    from PIL import Image
    im = img.convert("RGB"); im.thumbnail((maxside, maxside))
    b = io.BytesIO(); im.save(b, "JPEG", quality=88)
    return {"inline_data": {"mime_type": "image/jpeg", "data": base64.b64encode(b.getvalue()).decode()}}


def still_parts(path):
    from PIL import Image
    im = Image.open(path); w, h = im.size
    parts = [{"text": "IMAGE UNDER TEST, whole frame:"}, jpeg_part(im)]
    for name, box in (("top-left", (0, 0, w // 2 + w // 10, h // 2 + h // 10)), ("top-right", (w // 2 - w // 10, 0, w, h // 2 + h // 10)),
                      ("bottom-left", (0, h // 2 - h // 10, w // 2 + w // 10, h)), ("bottom-right", (w // 2 - w // 10, h // 2 - h // 10, w, h))):
        parts += [{"text": f"IMAGE UNDER TEST, zoomed {name} quarter:"}, jpeg_part(im.crop(box), 1400)]
    return parts


def clip_parts(path):
    data = Path(path).read_bytes()
    if len(data) > 15 * 1024 * 1024:
        sys.exit(f"{path}: over 15 MB; trim or downscale first")
    return [{"text": "CLIP UNDER TEST:"}, {"inline_data": {"mime_type": "video/mp4", "data": base64.b64encode(data).decode()}}]


def ask(parts, items, prompt_text):
    qs = "\n".join(f'{i["id"]}: {i["q"]} (FAIL if: {i["fail_if"]})' for i in items)
    instr = ("You are a strict quality inspector for AI-generated film stills and clips. Inspect the media above. Look at the "
             "zoomed quarters closely. Answer EVERY item below independently. Be strict: if you can see the fault anywhere, "
             "even small, it fails. Do not assume; look.\n"
             + (f"\nWhat the image was meant to show (the prompt): {prompt_text}\n" if prompt_text else "")
             + f"\nItems:\n{qs}\n\nReply with JSON only: {{\"items\": [{{\"id\": \"…\", \"fail\": true|false, \"evidence\": \"what you see\", "
               "\"where\": \"part of the frame\"}}]}}")
    body = {"contents": [{"role": "user", "parts": parts + [{"text": instr}]}],
            "generationConfig": {"responseMimeType": "application/json", "temperature": 0}}
    last = None
    for m in MODELS:
        for attempt in range(3):
            req = urllib.request.Request(ENDPOINT.format(m=m), data=json.dumps(body).encode(),
                                         headers={"x-goog-api-key": key(), "Content-Type": "application/json"})
            try:
                res = json.load(urllib.request.urlopen(req, timeout=240))
                txt = res["candidates"][0]["content"]["parts"][0]["text"]
                return m, json.loads(txt)["items"]
            except urllib.error.HTTPError as e:
                last = f"{m}: HTTP {e.code} {e.read()[:200]!r}"
                if e.code in (429, 404, 400):
                    break
                time.sleep(4 * (attempt + 1))
            except Exception as e:  # bad JSON or network
                last = f"{m}: {e}"; time.sleep(3)
    sys.exit(f"QA call failed: {last}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("checklist"); ap.add_argument("files", nargs="+")
    ap.add_argument("--ref", action="append", default=[]); ap.add_argument("--prompt", default="")
    ap.add_argument("--json")
    a = ap.parse_args()
    from PIL import Image
    cl = json.loads(Path(a.checklist).read_text())
    report, bad = {}, False
    for f in a.files:
        is_clip = f.lower().endswith((".mp4", ".mov", ".webm"))
        items = cl["clip" if is_clip else "still"]
        parts = clip_parts(f) if is_clip else still_parts(f)
        for r in a.ref:
            parts = [{"text": "REFERENCE (what the subject must match: a set, a character, a mask, the start still):"}, jpeg_part(Image.open(r), 1200)] + parts
        model, answers = ask(parts, items, a.prompt)
        byid = {i["id"]: i for i in items}
        fails = [x for x in answers if x.get("fail")]
        report[f] = {"model": model, "pass": not fails, "fails": [dict(x, fix=byid.get(x["id"], {}).get("fix", "")) for x in fails]}
        bad |= bool(fails)
        print(f"{'PASS' if not fails else 'FAIL'}  {Path(f).name}  ({model})")
        for x in fails:
            print(f"   ✗ {x['id']}: {x.get('evidence','')} [{x.get('where','')}] → fix: {byid.get(x['id'],{}).get('fix','')}")
    if a.json:
        Path(a.json).write_text(json.dumps(report, indent=1, ensure_ascii=False))
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
