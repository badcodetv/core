"""Clean-room video round (2026-10-29): every scene's Omni clips on one picks page.
Makes small web copies in <out>/vid (the full clips stay in alt/video-cr) and writes picks-vid.json;
then run scripts/scene/build-picks.py on it."""
import json, pathlib, subprocess, sys
HERE = pathlib.Path(__file__).parent
V = pathlib.Path("/mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/songs/bank robbery/alt/video-cr")
OUT = pathlib.Path(sys.argv[1]); (OUT / "vid").mkdir(parents=True, exist_ok=True)
P = json.load(open(HERE / "vid-prompts.json"))
beats = {l.split("|")[1].strip(): l for l in open(HERE / "beats-alt.md") if l.startswith("| ") and l.split("|")[1].strip().isdigit()}
NOTES = {  # what changed on the way through Flow, per scene
    1: "Flow blocked the gun lines twice; this runs without them (the gun in the still still points at the sky).",
    5: "'gangster' swapped for 'man' after a policy block; the cigarette kept.",
    8: "One take: Flow's second take came back as a copy of scene 7's.",
    9: "'red-haired lad' with a toothpick became 'a man in his twenties' after two blocks.",
    11: "One take: Flow's second take came back as a copy of scene 10's.",
    13: "'the slumped stoker stays still' was blocked; now he rests and breathes.",
    14: "Flow refused to upload your picked still (every try, three projects), so these start from your other still.",
    15: "Flow refused to upload your picked still, so these start from your other still.",
    23: "Start frame is my pick from the redo (23A-b); your other three redo stills are in alt/moodboard/cleanroom/cr4-s23.",
    31: "Flow refused to upload your picked still, so these start from your other still.",
}
groups = []
for n in range(1, 34):
    opts = []
    for clip in sorted(V.glob(f"s{n:02d}*-[ab].mp4")):
        dst = OUT / "vid" / clip.name
        if not dst.exists():
            subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-i", str(clip), "-vf", "scale=854:-2", "-c:v", "libx264",
                            "-preset", "veryfast", "-b:v", "700k", "-c:a", "aac", "-b:a", "64k", "-movflags", "+faststart", str(dst)], check=True)
        alt = "-alt" in clip.stem
        opts.append({"id": clip.stem.split("-", 1)[1], "src": f"vid/{clip.name}", "label": clip.stem.split("-", 1)[1] + (" (from your 2nd-choice still)" if alt else "")})
    if n == 1:
        title, where = "1. (Intro) Robbery! The getaway car", "Through the police windscreen"
    else:
        cells = [c.strip() for c in beats[str(n)].split("|")[1:-1]]
        title, where = f"{n}. {cells[1]}", f"{cells[2]}: {cells[3]}"
    line = f"{where}  ·  Layer: {P[str(n)]['why']}  ·  Ends on: {P[str(n)]['handoff']}"
    if n in NOTES:
        line += f"  ·  ⚠ {NOTES[n]}"
    if not opts:
        line += "  ·  ⬜ no clip yet"
    groups.append({"slot": f"v{n:02d}", "title": title, "line": line, "kind": "video", "opts": opts})
spec = {"title": "Speakeasy Mint Clips", "eyebrow": "Bank Robbery MV · ALT · clean room · the clips",
        "heading": "The Speakeasy Mint ALT: every scene in motion",
        "intro": "Your picked stills, animated in Omni Flash (8 s, two takes each). Fresh web research on psychedelic-but-filmed video, then eight sealed writers who never saw the repo's prompts, each animating a run of scenes so every clip ends on something that cuts into the next one. Run verbatim apart from the policy fixes noted on a row. The clips' own sound is a guide only; the song goes over the top. Pick one per scene and note anything to redo.",
        "sections": [{"h": "All 33 scenes", "lede": "Pick a or b (or note what to change).", "groups": groups}]}
json.dump(spec, open(HERE / "picks-vid.json", "w"), indent=1, ensure_ascii=False)
print(json.dumps({n: len(g["opts"]) for n, g in enumerate(groups, 1)}))
