"""Cut each sung slot's picture (25 fps, no audio) and its vocal stem slice for LatentSync. usage: prep_ls_r6.py [--have] writes ls-jobs-ready-r6.json with the jobs whose source exists."""
import json, os, pathlib, subprocess
HERE = pathlib.Path(__file__).parent
STEM = pathlib.Path.home() / ".cache/badcode-scenes/mv-colour-noir/stems/vocals16.wav"
ready = []
for j in json.load(open(HERE / "ls-jobs-r6.json")):
    if not os.path.exists(j["src"]) or os.path.exists(j["out"]): continue
    if not os.path.exists(j["video"]):
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", str(j["src_in"]), "-t", str(j["dur"] + .2), "-i", j["src"], "-an", "-r", "25", "-c:v", "libx264", "-crf", "12", "-preset", "fast", "-pix_fmt", "yuv420p", j["video"]], check=True)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", str(j["start"]), "-t", str(j["dur"]), "-i", str(STEM), "-ar", "16000", "-ac", "1", j["audio"]], check=True)
    ready.append(j)
json.dump(ready, open(HERE / "ls-jobs-ready-r6.json", "w"), indent=0)
print(len(ready), "ready", [j["id"] for j in ready][:40])
