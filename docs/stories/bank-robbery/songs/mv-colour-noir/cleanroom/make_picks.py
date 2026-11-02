"""The stills picks page. Copies whatever exists into <out>/img and writes picks.json; then run scripts/scene/build-picks.py on it."""
import json, pathlib, subprocess, sys
HERE = pathlib.Path(__file__).parent
M = pathlib.Path("/mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/songs/bank robbery/noir/moodboard")
OUT = pathlib.Path(sys.argv[1]); (OUT / "img").mkdir(parents=True, exist_ok=True)
# Flow hangs after about two prompts in a project, so each folder holds two shots at most.
FOLDERS = {"den": ["den1", "den2"], "den-2": ["den3", "den4"], "bridge": ["bridge1", "bridge2"], "bridge-2": ["bridge3", "bridge4"],
           "chase": ["chase1", "chase2"], "chase-2": ["chase3"], "chase4-pov1": ["chase4", "pov1"], "pov-23": ["pov2", "pov3"],
           "pov4-safe1": ["pov4", "safe1"], "safe-23": ["safe2", "safe3"], "safe4-mask1": ["safe4", "mask1"], "mask-23": ["mask2", "mask3"],
           "mask4-city1": ["mask4", "city1"], "city-23": ["city2", "city3"], "city4-rods1": ["city4", "rods1"], "rods-23": ["rods2", "rods3"], "rods4": ["rods4"]}
BEATS = [("den", "The den and its band"), ("bridge", "The band under the bridge"), ("chase", "Car chases"), ("pov", "The first-person driver"),
         ("safe", "The dragged safe"), ("mask", "Balaclava robberies"), ("city", "Prohibition cities"), ("rods", "Hot rod racing")]
P = json.load(open(HERE / "prompts.json"))
got = {}
for folder, shots in FOLDERS.items():
    for i, shot in enumerate(shots):
        for x in "ab":
            src = M / folder / f"{i:02d}-{x}.jpg"
            if src.exists():
                dst = OUT / "img" / f"{shot}-{x}.jpg"
                if not dst.exists():
                    subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-i", str(src), "-q:v", "3", str(dst)], check=True)
                got.setdefault(shot, []).append(x)
sections = []
for key, name in BEATS:
    groups = [{"slot": shot, "title": shot, "line": P[shot]["why"] + "  ·  Way out: " + P[shot]["way_out"], "kind": "image",
               "opts": [{"id": x, "src": f"img/{shot}-{x}.jpg", "label": x} for x in got[shot]]}
              for shot in P if P[shot]["beat"] == key and shot in got]
    if groups:
        sections.append({"h": name, "lede": "Pick the ones you like. Leave a note on anything that needs another go.", "groups": groups})
# Round 2 (Jack's notes): a male singer throughout, the real balaclavas in period wool. Slots are new so round 1's picks stay.
R2 = {"r2-mask1-3": ["mask1", "mask3"], "r2-mask4-safe1": ["mask4", "safe1"], "r2-safe4-den1": ["safe4", "den1"],
      "r2-den4-bridge1": ["den4", "bridge1"], "r2-bridge23": ["bridge2", "bridge3"], "r2-bridge4": ["bridge4"]}
PR2 = json.load(open(HERE / "prompts-r2.json"))
got2 = {}
for folder, shots in R2.items():
    for i, shot in enumerate(shots):
        for x in "ab":
            src = M / folder / f"{i:02d}-{x}.jpg"
            if src.exists():
                dst = OUT / "img" / f"r2-{shot}-{x}.jpg"
                if not dst.exists():
                    subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-i", str(src), "-q:v", "3", str(dst)], check=True)
                got2.setdefault(shot, []).append(x)
ORDER = ["mask1", "mask3", "mask4", "safe1", "safe4", "den1", "den4", "bridge1", "bridge2", "bridge3", "bridge4"]
sections.insert(0, {"h": "Round 2: your notes", "lede": "The real balaclavas with the logo over the eye, in different 1920s wool colours, and a male singer throughout. Pick the ones you want animated.",
    "groups": [{"slot": f"r2-{k}", "title": k, "line": PR2[k]["why"], "kind": "image",
                "opts": [{"id": x, "src": f"img/r2-{k}-{x}.jpg", "label": x} for x in got2[k]]} for k in ORDER if k in got2]})
# Round 3 (Jack's notes on the clips): new start frames, simple enough to move. Slots are new again.
R3 = {"r3-pov13": ["pov1", "pov3"], "r3-rods14": ["rods1", "rods4"], "r3-safe31": ["safe3", "safe1"]}
PR3 = json.load(open(HERE / "prompts-r3.json"))
groups3 = []
for folder, shots in R3.items():
    for i, shot in enumerate(shots):
        opts = []
        for x in "ab":
            src = M / folder / f"{i:02d}-{x}.jpg"
            if src.exists():
                dst = OUT / "img" / f"r3-{shot}-{x}.jpg"
                if not dst.exists():
                    subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-i", str(src), "-q:v", "3", str(dst)], check=True)
                opts.append({"id": x, "src": f"img/r3-{shot}-{x}.jpg", "label": x})
        groups3.append({"slot": f"r3-{shot}", "title": shot, "line": PR3[shot]["why"], "kind": "image", "opts": opts})
sections.insert(0, {"h": "Round 3: new start frames from your clip notes", "lede": "Simple frames that can move plainly, and safe1 with the logo moved. Pick the ones you want animated.", "groups": groups3})
# Round 4: replacements for the two shots Flow refused to animate.
PR4 = {}
import re as _re
for k, b in _re.findall(r"=== SHOT (\w+) ===\n(.*?)(?==== SHOT|\Z)", (HERE / "n4.md").read_text(), _re.S):
    PR4[k] = _re.search(r"WHY:\s*(.*)", b).group(1).strip()
g4 = []
for i, shot in enumerate(["den3", "mask4"]):
    opts = []
    for x in "ab":
        src = M / "r4-den3-mask4" / f"{i:02d}-{x}.jpg"
        if src.exists():
            dst = OUT / "img" / f"r4-{shot}-{x}.jpg"
            if not dst.exists():
                subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-i", str(src), "-q:v", "3", str(dst)], check=True)
            opts.append({"id": x, "src": f"img/r4-{shot}-{x}.jpg", "label": x})
    g4.append({"slot": f"r4-{shot}", "title": shot, "line": PR4[shot], "kind": "image", "opts": opts})
sections.insert(0, {"h": "Round 4: replacements for the refused shots", "lede": "The poker table and the riverboat, plainer so Flow should animate them. Skip them if you'd rather drop these.", "groups": g4})
spec = {"title": "Colour Noir Stills", "eyebrow": "Bank Robbery MV · colourful noir · clean room",
        "heading": "Colourful noir: a bank of cool shots",
        "intro": "Internet research and separate writers, run exactly as written on Nano Banana 2.1, two takes per shot. Round 2 writers saw only their own scene from round 1, plus the mask facts from Money For Something. No story yet and no lip sync. Click any image to see it large. Pick per shot and leave notes; skip anything you don't like.",
        "sections": sections}
json.dump(spec, open(HERE / "picks.json", "w"), indent=1, ensure_ascii=False)
print(sum(len(v) for v in got.values()), "stills,", len(got), "shots")
