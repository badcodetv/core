"""Measure every synced shot: does the mouth follow the vocal? Run with ~/.cache/badcode-lips/venv/bin/python.
corr = mouth gap against vocal loudness, best of lag 0-80 ms. silent_open = share of silent frames with the mouth well open.
A blunt screen for shots to look at, not a verdict: the skill warns correlation alone is too blunt, so read a mouth strip for anything flagged."""
import json, os, pathlib, subprocess, sys, tempfile, wave
import numpy as np
HERE = pathlib.Path(__file__).parent
TRACK = HERE.parents[5] / "scripts/lipsync/mouth-track.py"
name = sys.argv[1] if len(sys.argv) > 1 else "ls-run-r6.json"
jobs = json.load(open(HERE / name))
tmp = tempfile.mkdtemp()
OUT = HERE / ("ls-qc-r6.json" if len(sys.argv) < 2 else "ls-qc2-r6.json")
res = json.load(open(OUT)) if OUT.exists() else {}
for j in jobs:
    if not os.path.exists(j["out"]): res[j["id"]] = dict(missing=True); continue
    if j["id"] in res and res[j["id"]].get("mtime") == os.path.getmtime(j["out"]): continue
    strip = f"{tmp}/{j['id']}.png"
    local = f"{tmp}/{j['id']}.mp4"; subprocess.run(["cp", j["out"], local])
    subprocess.run([sys.executable, str(TRACK), local, strip], capture_output=True)
    if not os.path.exists(strip + ".json"): res[j["id"]] = dict(noface=True, mtime=os.path.getmtime(j["out"])); os.remove(local); continue
    d = json.load(open(strip + ".json")); g = np.array([x or 0 for x in d["gap"]], float)
    w = wave.open(j["audio"]); a = np.frombuffer(w.readframes(w.getnframes()), dtype=np.int16).astype(float)
    hop = 640; e = np.array([np.sqrt((a[i:i + hop] ** 2).mean()) for i in range(0, len(a) - hop, hop)])
    n = min(len(g), len(e)); g, e = g[:n], e[:n]
    best = -1
    for lag in (0, 1, 2):
        if n - lag > 10 and g[lag:].std() > 0 and e[:n - lag].std() > 0:
            best = max(best, float(np.corrcoef(g[lag:], e[:n - lag])[0, 1]))
    silent = e < e.max() * .12
    res[j["id"]] = dict(corr=round(best, 2), silent_open=round(float((g[silent] > .06).mean()), 2) if silent.any() else 0, moves=round(float(g.std()), 3), mtime=os.path.getmtime(j["out"]))
    os.remove(local); os.remove(strip)
json.dump(res, open(OUT, "w"), indent=0)
for k, v in sorted(res.items(), key=lambda x: x[1].get("corr", 9)):
    print(k, {a: b for a, b in v.items() if a != "mtime"})
