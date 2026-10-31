"""Round 6 cut: `Colour Noir 2`. Each row: hint time, clip, source in-point, speed. Starts snap to the nearest tracked beat (lines to the beat just before their first word), and a row ends where the next starts.
Singing rows (LIP) get LatentSync on the vocal stem for exactly that slot. Writes cut-r6.json and ls-jobs.json.
Word times are Whisper's on the stem, loose by 0.1-0.3 s; that only moves a cut, never the sync, because the mouth is drawn to the audio of its own slot."""
import json, os, pathlib, subprocess, sys
HERE = pathlib.Path(__file__).parent
CACHE = pathlib.Path.home() / ".cache/badcode-scenes/mv-colour-noir"
N = "/mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/songs/bank robbery/noir"
FPS = 24
beats = json.load(open(CACHE / "beats.json"))["beats"]
def snap(t):
    b = min(beats, key=lambda x: abs(x - t))
    return b if abs(b - t) < 0.3 else t
# (time, clip, source in, speed). Time None = previous end handled by order. L = sing.
R = [
 (0, "city1-b", 0, 1), (3.7, "den3", 0.3, 1), (7.4, "rods2-b", 1, 1), (11.1, "mask4", 0, .96),
 (15.02, "L:n01", .3, 1), (19.23, "pov3-r3-a", 2, 1), (20.62, "a13", .5, 1.3), (21.55, "safe1", 1.2, 1),
 (22.95, "L:n02", .3, 1), (26.68, "L:n03", .3, 1), (30.4, "L:n04", .3, 1), (34.1, "chase1-a", 1, 1), (35.95, "a3", .5, 1),
 (37.7, "L:n05", .3, 1), (41.4, "L:n06", .3, 1), (44.65, "pov2-a", 1, 1), (46.5, "a2", .4, 1),
 (48.6, "L:n07", .3, 1), (52.3, "L:n08", .3, 1), (56.0, "safe2-c", 0, 1), (59.3, "L:n09", .3, 1),
 (64.9, "rods3-b", 1, 1), (66.05, "L:l01", .3, 1), (70.0, "L:l02", .3, 1), (74.4, "a6", .4, 1),
 # chorus 1, the den
 (76.3, "L:d1", .3, 1), (78.15, "L:d2", .3, 1), (81.9, "L:d3", .3, 1), (84.35, "L:d4", .3, 1), (86.3, "L:d5", .3, 1), (88.1, "a12", .5, 1),
 # chorus 2, the bridge
 (90.8, "L:b1", .3, 1), (92.65, "L:b2", .3, 1), (94.5, "a9", .4, 1), (96.35, "L:b3", .3, 1), (98.9, "L:b4", .3, 1), (100.85, "L:b5", .3, 1), (102.7, "a1", .4, 1.5),
 # verse 3
 (104.0, "L:n10", .3, 1), (107.65, "safe4-b", 2, 1), (109.5, "a5", .5, 1.5), (111.3, "L:n11", .3, 1), (115.0, "chase4-b", 1.5, 1), (116.85, "a14", .5, 1.6),
 (118.7, "L:n12", .3, 1), (122.25, "rods1-r3-a", 1, 1), (124.05, "a4", .2, 1), (125.8, "L:n13", .3, 1), (129.4, "pov4-b", 1, 1), (131.3, "a10", .4, 1.6),
 (133.2, "L:n14", .3, 1), (136.6, "rods4", .8, 1.6), (138.45, "a13", 1.5, 1.3), (140.1, "L:l03", .3, 1), (144.2, "L:l04", .3, 1),
 (147.7, "L:n15", .3, 1), (151.4, "safe3-r3-a", 1, 1), (153.0, "a11", .3, 1), (154.6, "L:l05", .3, 1), (158.8, "L:l06", .3, 1), (162.0, "a9", 2.0, 1),
 # chorus 3
 (163.6, "L:b6", .3, 1), (165.4, "L:b1", 1.8, 1), (167.25, "a8", .4, 1), (169.5, "L:d1", 1.8, 1), (171.65, "L:b3", 2.3, 1), (173.6, "L:d3", 2.3, 1), (175.4, "a13", .2, 1.3),
 # chorus 4, the gang
 (178.25, "L:c1", .3, 1), (180.05, "L:c2", .3, 1), (182.3, "a11", 1.8, 1), (184.05, "L:c3", .3, 1), (186.15, "L:c4", .3, 1), (188.2, "L:c5", .3, 1),
 # break
 (191.1, "pov1-r3-b", 1, 1), (194.4, "L:n16", .3, 1), (198.6, "a12", 1.5, 1),
 # verse 5
 (199.55, "L:e1", .3, 1), (202.2, "L:e2", .3, 1), (206.0, "L:e3", .3, 1), (209.3, "L:e4", .3, 1), (213.0, "mask3-a", 1, 1), (214.9, "a8", 1.5, 1), (216.4, "L:n17", .3, 1),
 (220.25, "L:f1", .3, 1), (222.75, "L:f2", .3, 1), (225.4, "L:f3", .3, 1), (227.55, "L:f4", .3, 1), (230.0, "L:f5", .3, 1), (231.8, "L:f6", .3, 1), (235.0, "L:f7", .3, 1), (238.2, "L:f8", .3, 1),
 (241.8, "L:n18", .3, 1), (245.6, "mask1-b", 2, 1),
]
OUTRO = [(250, "o1-b", 8), (258, "o2-a", 4), (262, "o3-b", 4), (266, "o4-b", 4), (270, "o5-b", 4), (274, "o6-b", 4), (278, "o7-a", 8)]
def path(c):
    if c in ("l05", "l06", "f5", "f6"): return None
    return None
OLD_LIP = dict(l05="l05-b", l06="l06-a", f5="f5-a", f6="f6-a")
ACT_TAKE = dict(safe1="safe1-a", rods4="rods4-a", a1="a1-a", a2="a2-a", a3="a3-a", a4="a4-a", a5="a5-a", a6="a6-a", a8="a8-a", a9="a9-a", a10="a10-a", a11="a11-a", a12="a12-a", a13="a13-a", a14="a14-a", den3="den3-push", mask4="mask4-a")
over = HERE / "takes-r6.json"
if over.exists(): ACT_TAKE.update(json.load(open(over)))
def src(c):
    if c in OLD_LIP: return f"{N}/lipsync/video/{OLD_LIP[c]}.mp4"
    if c in ACT_TAKE: return f"{N}/r6/video/{ACT_TAKE[c]}.mp4"
    if os.path.exists(f"{N}/r6/video/{c}.mp4"): return f"{N}/r6/video/{c}.mp4"
    return f"{N}/video/{c}.mp4"
MISSING = []
def probe(p):
    if not os.path.exists(p): MISSING.append(p); return 6.0
    return float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", p], capture_output=True, text=True).stdout)
rows, jobs = [], []
WORK = CACHE / "r6-ls"; (WORK / "in").mkdir(parents=True, exist_ok=True)
SYNC = f"{N}/r6/synced"
times = [round(snap(r[0]) * FPS) / FPS for r in R] + [250.0]
for i, (t, c, sin, sp) in enumerate(R):
    a, b = times[i], times[i + 1]
    lip = c.startswith("L:"); c = c[2:] if lip else c
    s = src(c); dur = b - a; have = probe(s)
    need = sin + dur * sp
    if need > have:
        sin = max(0, have - dur * sp)
        if dur * sp > have: print("SHORT", c, a, b, round(have, 2))
    row = dict(n=i, start=round(a, 4), end=round(b, 4), clip=c, lip=lip, src=s, inPoint=round(sin, 3), speed=sp)
    if lip:
        name = f"{i:03d}-{c}"
        out = f"{SYNC}/{name}.mp4"; row["file"] = out; row["inPoint"] = 0
        jobs.append(dict(id=name, video=str(WORK / "in" / f"{name}.mp4"), audio=str(WORK / "in" / f"{name}.wav"), out=out, src=s, src_in=round(sin, 3), start=round(a, 4), dur=round(dur, 4)))
    rows.append(row)
for t, c, d in OUTRO:
    rows.append(dict(n=len(rows), start=t, end=t + d, clip=c, lip=False, src=f"{N}/outro/video/{c}.mp4", inPoint=0, speed=1))
json.dump(rows, open(HERE / "cut-r6.json", "w"), indent=0)
json.dump(jobs, open(HERE / "ls-jobs-r6.json", "w"), indent=0)
d = [r["end"] - r["start"] for r in rows if r["start"] < 250]
print("missing sources:", len(MISSING))
print(len(rows), "rows,", len(jobs), "sung; shot length median", sorted(d)[len(d)//2], "max", max(d), "; sung seconds", sum(j["dur"] for j in jobs))
