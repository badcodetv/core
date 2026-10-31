"""Second pass on shots the screen flagged: re-pick each shot's source in-point so the mouth is shut where the vocal is silent. New takes go to synced/v2. Run with the lips venv."""
import json, os, pathlib, subprocess, sys, tempfile, wave
import numpy as np
HERE = pathlib.Path(__file__).parent
TRACK = HERE.parents[5] / "scripts/lipsync/mouth-track.py"
W = pathlib.Path.home() / ".cache/badcode-scenes/mv-colour-noir/r6-ls/in2"; W.mkdir(exist_ok=True)
qc = json.load(open(HERE / "ls-qc-r6.json"))
jobs = json.load(open(HERE / "ls-run-r6.json"))
tmp = tempfile.mkdtemp(); out = []
gaps = {}
for j in jobs:
    q = qc[j["id"]]
    if not (q.get("silent_open", 0) >= .4 or q.get("corr", 1) <= 0): continue
    if j["src"] not in gaps:
        local = f"{tmp}/s{len(gaps)}.mp4"
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", j["src"], "-an", "-r", "25", "-c:v", "libx264", "-crf", "20", "-preset", "ultrafast", local], check=True)
        subprocess.run([sys.executable, str(TRACK), local, local + ".png"], capture_output=True)
        gaps[j["src"]] = np.array([x or 0 for x in json.load(open(local + ".png.json"))["gap"]], float)
    g = gaps[j["src"]]
    w = wave.open(j["audio"]); a = np.frombuffer(w.readframes(w.getnframes()), dtype=np.int16).astype(float)
    e = np.array([np.sqrt((a[i:i + 640] ** 2).mean()) for i in range(0, len(a) - 640, 640)])
    silent = e < e.max() * .12; n = len(e)
    best = None
    for k in range(0, max(1, len(g) - n)):
        win = g[k:k + n]
        if len(win) < n: break
        score = win[silent].mean() if silent.any() else 0
        score = score + max(0, win[:3].mean() - .03) * .5 + abs(k * .04 - j["src_in"]) * .002
        if best is None or score < best[0]: best = (score, k)
    k = best[1]; src_in = round(k * .04, 3)
    print(j["id"], "in", j["src_in"], "->", src_in, "silent frames", int(silent.sum()), "of", n)
    v = str(W / f"{j['id']}.mp4")
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", str(src_in), "-t", str(j["dur"] + .2), "-i", j["src"], "-an", "-r", "25", "-c:v", "libx264", "-crf", "12", "-preset", "fast", "-pix_fmt", "yuv420p", v], check=True)
    d = os.path.dirname(j["out"]) + "/v2"; os.makedirs(d, exist_ok=True)
    out.append(dict(id=j["id"], video=v, audio=j["audio"], out=f"{d}/{j['id']}.mp4", src=j["src"], src_in=src_in, start=j["start"], dur=j["dur"]))
json.dump(out, open(HERE / "ls-run2-r6.json", "w"), indent=0)
print(len(out))
