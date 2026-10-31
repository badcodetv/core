"""Round 7 cut: `Colour Noir 3`. Jack: too much lip sync, more action, people only occasionally singing, lips lined up by editing.
Starts from Colour Noir 2 (build-r6.json): every non-sung row stays where it was, 20 sung shots stay, and the other sung slots fill with action cut on the beats.
Sung shots are slipped in the edit: the source in-point moves so the mouth meets the voice (mouth-r7.json, from lag_r7.py). Writes build-r7.json and report lines."""
import json, os, pathlib, subprocess
HERE = pathlib.Path(__file__).parent
CACHE = pathlib.Path.home() / ".cache/badcode-scenes/mv-colour-noir"
N = "/mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/songs/bank robbery/noir"
FPS = 24
beats = json.load(open(CACHE / "beats.json"))["beats"]
fr = lambda t: round(t * FPS) / FPS
old = json.load(open(HERE / "build-r6.json"))
mouth = json.load(open(HERE / "mouth-r7.json"))
# The sung shots that stay: row number in Colour Noir 2, and the most beats it may hold.
KEEP = {4: 8, 10: 8, 17: 8, 27: 6, 29: 4, 32: 4, 35: 4, 47: 8, 50: 8, 55: 8, 58: 8, 62: 4, 66: 4, 69: 4, 72: 4, 77: 6, 83: 8, 85: 4, 90: 6, 92: 8}
# Clean windows in seconds of source (the older 8 s clips swerve into a swipe near the end), and the speed to play them at.
R6, V = f"{N}/r6/video", f"{N}/video"
POOL = [  # family, path, window start, window end, speed
 ("a1", f"{R6}/a1-a.mp4", .3, 3.8, 1.5), ("a2", f"{R6}/a2-b.mp4", .3, 3.8, 1.3), ("chase3", f"{V}/chase3-a.mp4", .3, 5.6, 1.3), ("a3", f"{R6}/a3-b.mp4", .3, 3.8, 1),
 ("a8", f"{R6}/a8-a.mp4", .3, 3.8, 1), ("pov3", f"{V}/pov3-a.mp4", .3, 6.2, 1.3), ("a5", f"{R6}/a5-a.mp4", .3, 3.8, 1.5), ("a11", f"{R6}/a11-b.mp4", .3, 3.8, 1.2),
 ("rods1", f"{V}/rods1-a.mp4", .2, 3.6, 1.3), ("a9", f"{R6}/a9-a.mp4", .3, 3.8, 1), ("a13", f"{R6}/a13-b.mp4", .3, 3.8, 1.3), ("pov1", f"{V}/pov1-b.mp4", .3, 5.6, 1.3),
 ("a10", f"{R6}/a10-b.mp4", .3, 3.8, 1.6), ("a12", f"{R6}/a12-b.mp4", .3, 5.7, 1), ("chase1", f"{V}/chase1-a.mp4", .3, 5.2, 1.2), ("a4", f"{R6}/a4-a.mp4", .1, 1.3, 1),
 ("a14", f"{R6}/a14-b.mp4", .3, 3.8, 1.6), ("rods3", f"{V}/rods3-b.mp4", .3, 5.0, 1.3), ("mask3", f"{V}/mask3-a.mp4", .3, 6.0, 1), ("rods4", f"{R6}/rods4-a.mp4", .3, 3.8, 1.6),
 ("pov4", f"{V}/pov4-b.mp4", .3, 6.0, 1.3), ("a6", f"{R6}/a6-a.mp4", 2.3, 5.6, 1), ("safe1", f"{R6}/safe1-b.mp4", .5, 3.6, 1), ("rods2", f"{V}/rods2-b.mp4", 1, 5.5, 1.3),
 ("safe3", f"{V}/safe3-r3-a.mp4", .3, 6.2, 1.5), ("chase4", f"{V}/chase4-b.mp4", .3, 6.3, 1), ("safe4", f"{V}/safe4-b.mp4", .3, 5.4, 1), ("pov2", f"{V}/pov2-a.mp4", .3, 5.6, 1),
 ("mask1", f"{V}/mask1-b.mp4", .3, 6.0, 1),
]
cursor = {p[1]: p[2] for p in POOL}; wraps = {}
def nearest(t): return min(beats, key=lambda b: abs(b - t))
def beat_index(t): return beats.index(nearest(t))
def slip_for(name, nominal=.083):
    """Positive lag = mouth later than the voice, so the picture must start later in its file. Aim the voice a touch behind the mouth: late is forgiven, early is not."""
    m = mouth[name]
    if m["peak"] >= .3 and m["peak"] - m["at0"] >= .1 and .08 <= abs(m["best"]) <= .44:
        return m["best"] + .04, "shot"
    return nominal, "nominal"
rows, recent, pick_i, report = [], [], 0, []
def fill(a, b):
    """Action from a to b, on the beats: 4, 2, 2 beats and so on, never a sliver at the end."""
    global pick_i
    i, j = beat_index(a), beat_index(b); pattern = [4, 2, 2, 4, 2, 4, 2, 2]; p = 0; t = i
    while t < j:
        step = pattern[p % len(pattern)]; p += 1
        if j - (t + step) < 2: step = j - t
        s, e = (a if t == i else beats[t]), (b if t + step >= j else beats[t + step])
        for _ in range(len(POOL)):
            fam, path, w0, w1, sp = POOL[pick_i % len(POOL)]; pick_i += 1
            if fam in recent: continue
            need = (fr(e) - fr(s)) * sp
            if need > w1 - w0: continue
            break
        c = cursor[path]
        if c + need > w1:
            wraps[path] = wraps.get(path, 0) + 1; c = w0 + (wraps[path] * .37) % max(.01, min(.9, w1 - w0 - need))   # a repeat starts somewhere new
        cursor[path] = c + need
        recent.append(fam); del recent[:-10]
        rows.append(dict(start=fr(s), end=fr(e), clip=os.path.basename(path)[:-4], lip=False, src=path, srcIn=round(c, 3), speed=sp))
        t += step
pending = None
for k, r in enumerate(old):
    if r["start"] >= 250:
        if pending is not None: fill(pending, r["start"]); pending = None
        rows.append(dict(start=r["start"], end=r["end"], clip=r["clip"], lip=False, path=r["path"], inPoint=r["inPoint"])); continue
    if r["lip"] and r["n"] not in KEEP:
        pending = r["start"] if pending is None else pending
        continue
    if pending is not None: fill(pending, r["start"]); pending = None
    if not r["lip"]:
        recent.append(r["clip"].split("-")[0]); del recent[:-10]
        rows.append(dict(start=r["start"], end=r["end"], clip=r["clip"], lip=False, path=r["path"], inPoint=r["inPoint"])); continue
    name = f"{r['n']:03d}-{r['clip']}"; slip, how = slip_for(name)
    file_len = float(subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v", "-show_entries", "stream=duration", "-of", "csv=p=0", r["path"]], capture_output=True, text=True).stdout)
    s = r["start"]; bi = beat_index(s)
    if slip < 0: s = beats[bi + 1]; bi += 1   # no picture before the file starts, so come in a beat later
    cap = beats[min(bi + KEEP[r["n"]], len(beats) - 1)]
    e = min(cap, r["end"])
    if fr(s) - r["start"] + slip < 0: slip = r["start"] - fr(s)
    if fr(s) - r["start"] + slip + (fr(e) - fr(s)) > file_len:
        room = file_len - (fr(s) - r["start"]) - (fr(e) - fr(s));
        if room < slip:   # end the shot earlier rather than lose the slip
            for b in reversed([x for x in beats if s + 1 < x < e]):
                if fr(s) - r["start"] + slip + (fr(b) - fr(s)) <= file_len: e = b; break
            else: slip = max(0, room); how += " clamped"
    in_point = fr(fr(s) - r["start"] + slip)
    report.append((name, fr(s), fr(e), round(in_point - (fr(s) - r["start"]), 3), how, mouth[name]["peak"], mouth[name]["at0"]))
    rows.append(dict(start=fr(s), end=fr(e), clip=r["clip"], name=name, lip=True, path=r["path"], inPoint=in_point, songStart=r["start"], slip=round(in_point - (fr(s) - r["start"]), 3)))
    if fr(s) > r["start"] + .01: fill(r["start"], s) if False else None
    if fr(e) < r["end"] - .01: pending = e
# A sung shot that came in a beat late leaves its first beat to the shot before: extend that shot.
for a, b in zip(rows, rows[1:]):
    if abs(b["start"] - a["end"]) > .001: a["end"] = b["start"]
FAST = f"{N}/r7/fast"; os.makedirs(FAST, exist_ok=True)
for r in rows:
    if "src" not in r: continue
    if r["speed"] == 1:
        r["path"], r["inPoint"] = r["src"], fr(r["srcIn"])
    else:
        out = f"{FAST}/{os.path.basename(r['src'])[:-4]}-x{r['speed']}.mp4"
        if not os.path.exists(out):
            subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", r["src"], "-an", "-vf", f"setpts=PTS/{r['speed']},fps=24", "-c:v", "libx264", "-crf", "14", "-preset", "fast", "-pix_fmt", "yuv420p", out], check=True)
        r["path"], r["inPoint"] = out, fr(r["srcIn"] / r["speed"])
for n, r in enumerate(rows): r["n"] = n
json.dump(rows, open(HERE / "build-r7.json", "w"), indent=0)
pre = [r for r in rows if r["start"] < 250]; d = [r["end"] - r["start"] for r in pre]
sung = sum(r["end"] - r["start"] for r in pre if r["lip"])
off = [min(abs(b - r["start"]) for b in beats) for r in pre[1:]]
print(len(rows), "rows;", len(pre), "before outro; sung", sum(r["lip"] for r in pre), "shots", round(sung, 1), "s =", round(100 * sung / 250), "% ; median shot", round(sorted(d)[len(d) // 2], 2), "shortest", round(min(d), 2), "longest", round(max(d), 2))
print("cuts more than one frame off a beat:", sum(o > .043 for o in off), "of", len(off))
print("gaps", [(a["n"], round(b["start"] - a["end"], 3)) for a, b in zip(rows, rows[1:]) if abs(b["start"] - a["end"]) > .001])
from collections import Counter
print("uses", Counter(r["clip"].split("-")[0] for r in pre if not r["lip"]).most_common(40))
for x in report: print(x)
print("new files:", len({r["path"] for r in rows}))
