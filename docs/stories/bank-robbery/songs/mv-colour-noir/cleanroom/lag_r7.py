"""Measure the mouth against the vocal on every sung shot of Colour Noir 2, at lags of -0.48 to +0.48 s. Positive lag = the mouth moves later than the voice. Writes mouth-r7.json. Lips venv."""
import json, os, pathlib, subprocess, sys, tempfile, wave
import numpy as np
HERE = pathlib.Path(__file__).parent
TRACK = HERE.parents[5] / "scripts/lipsync/mouth-track.py"
choice = json.load(open(HERE / "ls-choice-r6.json")); tmp = tempfile.mkdtemp(); res = {}
for j in json.load(open(HERE / "ls-run-r6.json")):
    f = j["out"]; 
    if choice.get(j["id"]) == "v2": f = f"{os.path.dirname(f)}/v2/{j['id']}.mp4"
    local = f"{tmp}/x.mp4"; subprocess.run(["cp", f, local]); strip = f"{tmp}/x.png"
    subprocess.run([sys.executable, str(TRACK), local, strip], capture_output=True)
    g = np.array([x or 0 for x in json.load(open(strip + ".json"))["gap"]], float)
    w = wave.open(j["audio"]); a = np.frombuffer(w.readframes(w.getnframes()), dtype=np.int16).astype(float)
    e = np.array([np.sqrt((a[i:i + 640] ** 2).mean()) for i in range(0, len(a) - 640, 640)])
    n = min(len(g), len(e)); g = g[:n]; e = e[:n]; curve = {}
    for lag in range(-12, 13):
        x, y = (g[lag:], e[:n - lag]) if lag >= 0 else (g[:n + lag], e[-lag:])
        curve[lag] = float(np.corrcoef(x, y)[0, 1]) if len(x) > 12 and x.std() > 0 and y.std() > 0 else 0
    best = max(curve, key=curve.get)
    res[j["id"]] = dict(file=f, start=j["start"], dur=j["dur"], best=best * .04, peak=round(curve[best], 2), at0=round(curve[0], 2), curve=curve, gap=g.round(4).tolist(), vox=(e / max(e.max(), 1)).round(3).tolist())
json.dump(res, open(HERE / "mouth-r7.json", "w"))
avg = {l: round(np.mean([r["curve"][l] for r in res.values()]), 3) for l in range(-12, 13)}
print("mean corr by lag:", {l * 40: v for l, v in avg.items()})
print("per shot:", sorted((k, r["best"], r["peak"], r["at0"]) for k, r in res.items()))
