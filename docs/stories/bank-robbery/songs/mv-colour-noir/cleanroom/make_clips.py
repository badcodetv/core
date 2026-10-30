"""The clips picks page. Shrinks each clip into <out>/vid and writes picks-clips.json; then run scripts/scene/build-picks.py on it."""
import json, pathlib, subprocess, sys
HERE = pathlib.Path(__file__).parent
V = pathlib.Path("/mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/songs/bank robbery/noir/video")
OUT = pathlib.Path(sys.argv[1]); (OUT / "vid").mkdir(parents=True, exist_ok=True)
C = json.load(open(HERE / "clips.json"))
BEATS = [("Car chases", ["chase1", "chase2", "chase3", "chase4"]), ("The first-person driver", ["pov1", "pov2", "pov3", "pov4"]),
         ("Hot rod racing", ["rods1", "rods2", "rods3", "rods4"]), ("Prohibition cities", ["city1"]), ("The dragged safe", ["safe2", "safe3"])]
sections, files = [], {}
for name, keys in BEATS:
    groups = []
    for k in keys:
        opts = []
        for x in "abc":
            src = V / f"{k}-{x}.mp4"
            if src.exists():
                dst = OUT / "vid" / f"{k}-{x}.mp4"
                if not dst.exists():
                    subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-i", str(src), "-vf", "scale=960:-2", "-c:v", "libx264", "-crf", "26", "-preset", "veryfast", "-an", "-movflags", "+faststart", str(dst)], check=True)
                opts.append({"id": x, "src": f"vid/{k}-{x}.mp4", "label": x})
        groups.append({"slot": f"clip-{k}", "title": k, "line": "Ends on: " + C[k]["ends_on"], "kind": "video", "opts": opts})
    sections.append({"h": name, "lede": "Pick a take, or leave a note on what to change.", "groups": groups})
# Round 2: Jack's approved stills, and chase2 redone. Slots are new so round 1's picks stay.
C2 = json.load(open(HERE / "clips-r2.json"))
g2 = []
for k in ["mask1", "mask3", "safe4", "den1", "den4", "bridge1", "bridge2", "bridge3", "bridge4", "chase2"]:
    opts = []
    stem = "chase2-r2" if k == "chase2" else k
    for x in "ab":
        src = V / f"{stem}-{x}.mp4"
        if src.exists():
            dst = OUT / "vid" / f"{stem}-{x}.mp4"
            if not dst.exists():
                subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-i", str(src), "-vf", "scale=960:-2", "-c:v", "libx264", "-crf", "26", "-preset", "veryfast", "-an", "-movflags", "+faststart", str(dst)], check=True)
            opts.append({"id": x, "src": f"vid/{stem}-{x}.mp4", "label": x})
    g2.append({"slot": f"r2-clip-{k}", "title": k, "line": "Ends on: " + C2[k]["ends_on"], "kind": "video", "opts": opts})
sections.insert(0, {"h": "Round 2: your approved stills", "lede": "One plain action per clip, as your notes asked. The singer isn't singing yet: lip sync comes later. The riverboat (mask4) was refused by Flow.", "groups": g2})
# Round 3: Jack's picks of the new start frames, and chase2 a third time.
C3 = json.load(open(HERE / "clips-r3.json"))
g3 = []
for k, stem in [("pov1", "pov1-r3"), ("pov3", "pov3-r3"), ("rods1", "rods1-r3"), ("rods4", "rods4-r3"), ("safe1", "safe1"), ("safe3", "safe3-r3"), ("chase2", "chase2-r3")]:
    opts = []
    for x in "ab":
        src = V / f"{stem}-{x}.mp4"
        if src.exists():
            dst = OUT / "vid" / f"{stem}-{x}.mp4"
            if not dst.exists():
                subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-i", str(src), "-vf", "scale=960:-2", "-c:v", "libx264", "-crf", "26", "-preset", "veryfast", "-an", "-movflags", "+faststart", str(dst)], check=True)
            opts.append({"id": x, "src": f"vid/{stem}-{x}.mp4", "label": x})
    g3.append({"slot": f"r3-clip-{k}", "title": k, "line": "Ends on: " + C3[k]["ends_on"], "kind": "video", "opts": opts})
sections.insert(0, {"h": "Round 3: your new start frames", "lede": "Simple and plain, from your notes. Pick a take, or leave a note.", "groups": g3})
spec = {"title": "Colour Noir Clips", "eyebrow": "Bank Robbery MV · colourful noir · clips",
        "heading": "Colourful noir: the first clips",
        "intro": "Your picked stills with no fixes needed, animated on Omni Flash, 8 seconds each, with the sound off because the song replaces it. Each clip ends on something the editor can cut on: a pillar crossing the lens, a whip pan, a headlamp flare. The poker table (den3) and riverboat (mask4) were refused by Flow, so they aren't here.",
        "sections": sections}
json.dump(spec, open(HERE / "picks-clips.json", "w"), indent=1, ensure_ascii=False)
print(sum(len(g["opts"]) for s in sections for g in s["groups"]), "clips")
