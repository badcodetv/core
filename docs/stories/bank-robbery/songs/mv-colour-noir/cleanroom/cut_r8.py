"""Round 8 cut: `Colour Noir 4`. Colour Noir 2 kept shot for shot, except 8 sung shots become action on the beats. Every remaining sung shot plays from a render with spare frames, slipped so the mouth meets the voice.
Slip: 2 frames by default (voice just behind the mouth), moved only when that shot's own window measures clearly better. Run with the lips venv. Writes build-r8.json."""
import json, os, pathlib, subprocess, sys, tempfile, wave
import numpy as np
HERE = pathlib.Path(__file__).parent
CACHE = pathlib.Path.home() / ".cache/badcode-scenes/mv-colour-noir"
TRACK = HERE.parents[5] / "scripts/lipsync/mouth-track.py"
N = "/mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/songs/bank robbery/noir"
FPS = 24; fr = lambda t: round(t * FPS) / FPS
beats = json.load(open(CACHE / "beats.json"))["beats"]
old = json.load(open(HERE / "build-r6.json"))
jobs = {j["id"]: j for j in json.load(open(HERE / "ls-run-r8.json"))}
w = wave.open(str(CACHE / "stems/vocals16.wav")); a = np.frombuffer(w.readframes(w.getnframes()), dtype=np.int16).astype(float)
vox = lambda t: np.sqrt((a[int(t * 16000):int(t * 16000) + 640] ** 2).mean())
R6, F = f"{N}/r6/video", f"{N}/r7/fast"; V = f"{N}/video"
POOL = [  # family, file, window start and end in that file's own seconds
 ("a2", f"{F}/a2-b-x1.3.mp4", .25, 2.9), ("chase3", f"{F}/chase3-a-x1.3.mp4", .25, 4.3), ("a3", f"{R6}/a3-b.mp4", .3, 3.8), ("a8", f"{R6}/a8-a.mp4", .3, 3.8),
 ("pov3", f"{F}/pov3-a-x1.3.mp4", .25, 4.7), ("a5", f"{F}/a5-a-x1.5.mp4", .2, 2.5), ("a11", f"{F}/a11-b-x1.2.mp4", .25, 3.1), ("rods1", f"{F}/rods1-a-x1.3.mp4", .2, 2.7),
 ("a9", f"{R6}/a9-a.mp4", .3, 3.8), ("a13", f"{F}/a13-b-x1.3.mp4", .25, 2.9), ("pov1", f"{F}/pov1-b-x1.3.mp4", .25, 4.3), ("a10", f"{F}/a10-b-x1.6.mp4", .2, 2.3),
 ("a12", f"{R6}/a12-b.mp4", .3, 5.7), ("chase1", f"{F}/chase1-a-x1.2.mp4", .25, 4.3), ("a14", f"{F}/a14-b-x1.6.mp4", .2, 2.3), ("rods4", f"{F}/rods4-a-x1.6.mp4", .2, 2.3),
 ("pov4", f"{F}/pov4-b-x1.3.mp4", .25, 4.6), ("safe1", f"{R6}/safe1-b.mp4", .5, 3.6),
]
cursor = {p[1]: p[2] for p in POOL}; recent = []; pick = [0]
def bi(t): return min(range(len(beats)), key=lambda i: abs(beats[i] - t))
def fill(rows, s0, e0):
    i, j = bi(s0), bi(e0); pattern = [4, 2, 2, 4, 2, 2]; p = 0; t = i
    while t < j:
        step = pattern[p % 6]; p += 1
        if j - (t + step) < 2: step = j - t
        s, e = (s0 if t == i else beats[t]), (e0 if t + step >= j else beats[t + step])
        d = fr(e) - fr(s)
        for _ in range(len(POOL)):
            fam, path, w0, w1 = POOL[pick[0] % len(POOL)]; pick[0] += 1
            if fam not in recent and d <= w1 - w0: break
        c = cursor[path]
        if c + d > w1: c = w0 + .4
        cursor[path] = c + d; recent.append(fam); del recent[:-10]
        rows.append(dict(start=fr(s), end=fr(e), clip=os.path.basename(path)[:-4], lip=False, path=path, inPoint=fr(c)))
        t += step
tmp = tempfile.mkdtemp(); rows = []; report = []
for r in old:
    name = f"{r['n']:03d}-{r['clip']}"
    if r["lip"] and name not in jobs:
        fill(rows, r["start"], r["end"]); continue
    if not r["lip"]:
        recent.append(r["clip"].split("-")[0]); del recent[:-10]
        rows.append(dict(start=r["start"], end=r["end"], clip=r["clip"], lip=False, path=r["path"], inPoint=r["inPoint"])); continue
    j = jobs[name]
    local = f"{tmp}/x.mp4"; subprocess.run(["cp", j["out"], local])
    subprocess.run([sys.executable, str(TRACK), local, local + ".png"], capture_output=True)
    g = np.array([x or 0 for x in json.load(open(local + ".png.json"))["gap"]], float)
    ts = np.arange(r["start"], r["end"], .04); e = np.array([vox(t) for t in ts])
    def corr(slip):
        idx = ((j["head"] + slip + (ts - r["start"])) * 25).astype(int)
        if idx.min() < 0 or idx.max() >= len(g) or g[idx].std() == 0 or e.std() == 0: return None
        return float(np.corrcoef(g[idx], e)[0, 1])
    cand = {f: corr(f / FPS) for f in range(-8, 13)}; cand = {f: c for f, c in cand.items() if c is not None}
    # 2 frames unless the shot clearly says otherwise; a big move has to earn more.
    f = 2 if 2 in cand else min(cand, key=lambda x: abs(x - 2)); base = cand[f]
    for x, c in cand.items():
        need = .12 if abs(x - 2) <= 4 else .22
        if c - base >= need and c > cand[f]: f = x
    in_point = fr(j["head"] + f / FPS)
    report.append((name, round(r["start"], 2), round(r["end"] - r["start"], 2), f, round(cand[f], 2), round(cand.get(0, 0), 2)))
    rows.append(dict(start=r["start"], end=r["end"], clip=r["clip"], name=name, lip=True, path=j["out"], inPoint=in_point, slipFrames=f, corr=round(cand[f], 2)))
for n, r in enumerate(rows): r["n"] = n
json.dump(rows, open(HERE / "build-r8.json", "w"), indent=0)
pre = [r for r in rows if r["start"] < 250]; d = [r["end"] - r["start"] for r in pre]
print(len(rows), "rows; sung", sum(r["lip"] for r in pre), round(sum(r["end"] - r["start"] for r in pre if r["lip"]), 1), "s; median", round(sorted(d)[len(d) // 2], 2), "shortest", round(min(d), 2))
print("gaps", [(x["n"], round(y["start"] - x["end"], 3)) for x, y in zip(rows, rows[1:]) if abs(y["start"] - x["end"]) > .001])
print("frames slipped:", sorted((x[3] for x in report)))
print("mean corr at slip", round(np.mean([x[4] for x in report]), 3), "at 0", round(np.mean([x[5] for x in report]), 3))
for x in sorted(report, key=lambda x: x[4])[:12]: print(x)
print("big slips", [x for x in report if abs(x[3]) > 6])
print(json.dumps([[q["path"].split("/noir/")[1], round(q["start"], 4), round(q["end"], 4), round(q["inPoint"], 4)] for q in rows], separators=(",", ":")))
print("distinct new r8 files", len({q["path"] for q in rows if "/r8/" in q["path"]}))
