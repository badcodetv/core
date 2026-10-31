"""Round 8: Colour Noir 2 with a few sung shots swapped for action, and every remaining sung shot re-rendered with spare frames at both ends, so its lips can be slipped in Premiere without moving a cut. Writes ls-run-r8.json."""
import json, os, pathlib, subprocess
HERE = pathlib.Path(__file__).parent
N = "/mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/songs/bank robbery/noir"
W = pathlib.Path.home() / ".cache/badcode-scenes/mv-colour-noir/r8-ls"; W.mkdir(exist_ok=True)
STEM = pathlib.Path.home() / ".cache/badcode-scenes/mv-colour-noir/stems/vocals16.wav"
REMOVE = ["014-n06", "023-l02", "031-b1", "034-b3", "038-n10", "061-b6", "078-e2", "087-f4"]  # weakest mouth tracking, spread across the film
HEAD, TAIL = .5, .6
os.makedirs(f"{N}/r8/synced", exist_ok=True)
choice = json.load(open(HERE / "ls-choice-r6.json"))
v2 = {j["id"]: j for j in json.load(open(HERE / "ls-run2-r6.json"))}
out = []
for j in json.load(open(HERE / "ls-run-r6.json")):
    if j["id"] in REMOVE: continue
    if choice.get(j["id"]) == "v2": j = v2[j["id"]]
    head = min(HEAD, j["src_in"])
    v, a = str(W / f"{j['id']}.mp4"), str(W / f"{j['id']}.wav")
    length = head + j["dur"] + TAIL
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", str(j["src_in"] - head), "-t", str(length + .1), "-i", j["src"], "-an", "-r", "25", "-c:v", "libx264", "-crf", "12", "-preset", "fast", "-pix_fmt", "yuv420p", v], check=True)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", str(j["start"] - head), "-t", str(length), "-i", str(STEM), "-ar", "16000", "-ac", "1", a], check=True)
    out.append(dict(id=j["id"], video=v, audio=a, out=f"{N}/r8/synced/{j['id']}.mp4", src=j["src"], src_in=round(j["src_in"] - head, 3), start=j["start"], dur=j["dur"], head=round(head, 3)))
json.dump(out, open(HERE / "ls-run-r8.json", "w"), indent=0)
print(len(out), "shots; shots with less than full head:", [(o["id"], o["head"]) for o in out if o["head"] < HEAD][:20])
