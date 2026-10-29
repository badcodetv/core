"""Clean-room round 3 (2026-10-29): the whole ALT film's stills on one picks page.
Copies media into <out>/img and writes picks-r3.json; then run scripts/scene/build-picks.py on it."""
import json, pathlib, shutil, subprocess, sys
HERE = pathlib.Path(__file__).parent
M = pathlib.Path("/mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/songs/bank robbery/alt/moodboard/cleanroom")
OUT = pathlib.Path(sys.argv[1]); (OUT / "img").mkdir(parents=True, exist_ok=True)
FOLDERS = {  # folder: scene per batch index (Flow projects hang after ~8 prompts, so the runs were split)
    "cr3-02-11": list(range(2, 12)), "cr3-12-21": [12, 13, 14, 15],
    "cr3-17-25-16": list(range(17, 25)), "cr3-25-16-26-31": [25, 16, 26, 27, 28],
    "cr3-29-33": [29, 30], "cr3-31-33": [31, 32, 33]}
P = json.load(open(HERE / "cr3-prompts.json"))
beats = {l.split("|")[1].strip(): l for l in open(HERE / "beats-alt.md") if l.startswith("| ") and l.split("|")[1].strip().isdigit()}
src = {}
for f, scenes in FOLDERS.items():
    for i, n in enumerate(scenes):
        for x in "ab":
            p = M / f / f"{i:02d}-{x}.jpg"
            if p.exists():
                dst = OUT / "img" / f"s{n:02d}-{x}.jpg"
                subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-i", str(p), "-q:v", "3", str(dst)], check=True)
                src.setdefault(n, []).append(x)
for n in (1,):
    for w in "1234":
        for x in "ab":
            shutil.copy(M / f"cr2-w{w}-{x}.jpg", OUT / "img" / f"s01-w{w}{x}.jpg")
groups = [{"slot": "s01", "title": "1. (Intro) Robbery! The getaway car", "line": "Round 2's eight stills (the ones you loved): back seat, from the El, police windscreen, dusk alley.", "kind": "image",
           "opts": [{"id": f"w{w}{x}", "src": f"img/s01-w{w}{x}.jpg", "label": f"{w}{x}"} for w in "1234" for x in "ab"]}]
for n in range(2, 34):
    cells = [c.strip() for c in beats[str(n)].split("|")[1:-1]]
    opts = [{"id": x, "src": f"img/s{n:02d}-{x}.jpg", "label": x} for x in src.get(n, [])]
    if not opts:
        opts = []
    groups.append({"slot": f"s{n:02d}", "title": f"{n}. {cells[1]}", "line": f"{cells[2]}: {cells[3]}  ·  Layer: {P[str(n)]['why']}", "kind": "image", "opts": opts,
                   **({} if opts else {"line": f"{cells[2]}: {cells[3]}  ·  ⬜ not generated yet"})})
spec = {"title": "Speakeasy Mint Stills", "eyebrow": "Bank Robbery MV · ALT · clean room round 3 · the whole film",
        "heading": "The Speakeasy Mint ALT: every scene, new stills",
        "intro": "The clean room you liked on scene 1, run on the whole film: the same web research on Nano Banana 2.1, eight sealed writers (four scenes each) who never saw the repo's prompts, run verbatim, two takes per scene. Each scene has its own physical psychedelic layer (frost on glass, a goldfish bowl, a whiskey decanter, a mirror ball, ink in the river...). People are described the same way in every scene, but no Flow Characters were used, so faces will drift between scenes. Click any image to see it large. Pick one per scene and leave a note where it needs another go.",
        "sections": [{"h": "All 33 scenes", "lede": "Pick a or b (or note what to change).", "groups": groups}]}
json.dump(spec, open(HERE / "picks-r3.json", "w"), indent=1, ensure_ascii=False)
print(json.dumps({n: src.get(n, []) for n in range(2, 34)}))
