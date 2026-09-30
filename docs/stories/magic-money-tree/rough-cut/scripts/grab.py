#!/usr/bin/env python3
"""Grab frames from a film at picture-only-file times, fast, from the local master copy.

    grab.py <id> <sec> [<sec> …]        -> /tmp/mmt-grab/<id>@<sec>.jpg (960 px wide, aspect-correct)
    grab.py <id> <from>-<to>            -> a 5x2 strip of 10 frames across that range

Use it to confirm a shot before writing it into the cut list: the shot logs find cuts, a human (or
an agent) still has to look. Times are the picture-only file's clock, as in the shot logs.
"""
import csv, os, subprocess, sys, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from shotlog import CONFORM, LOCAL, CLIPS, probe  # noqa: E402

OUT = "/tmp/mmt-grab"


def source(fid):
    st = {r["id"]: r for r in csv.DictReader(open(CONFORM), delimiter="\t")}
    r = st[fid]
    p = os.path.join(LOCAL, r["master"])
    if not os.path.exists(p):
        for c in (os.path.join(CLIPS, "_masters", r["master"]), os.path.join(CLIPS, r["scene"], r["master"])):
            if os.path.exists(c):
                p = c
                break
    return p, float(probe(p, "start_time") or 0), r["filter"].startswith("yadif")


def grab(p, t, deint, dst, w=960):
    vf = ("yadif=0," if deint else "") + f"scale=iw*sar:ih,setsar=1,scale={w}:-2"
    subprocess.run(["ffmpeg", "-nostdin", "-v", "error", "-y", "-ss", f"{max(0, t - 0.2):.3f}", "-i", p,
                    "-ss", "0.2", "-frames:v", "1", "-vf", vf, dst], check=True)


def main(a):
    fid = a[0]
    p, off, deint = source(fid)
    os.makedirs(OUT, exist_ok=True)
    for spec in a[1:]:
        if "-" in spec:
            t0, t1 = map(float, spec.split("-"))
            tmp = tempfile.mkdtemp()
            for i in range(10):
                grab(p, off + t0 + (t1 - t0) * i / 9, deint, os.path.join(tmp, f"{i:02d}.png"), 384)
            dst = os.path.join(OUT, f"{fid}@{t0:.2f}-{t1:.2f}.jpg")
            subprocess.run(["ffmpeg", "-nostdin", "-v", "error", "-y", "-i", os.path.join(tmp, "%02d.png"),
                            "-vf", "tile=5x2:padding=4:color=gray", dst], check=True)
        else:
            dst = os.path.join(OUT, f"{fid}@{float(spec):.2f}.jpg")
            grab(p, off + float(spec), deint, dst)
        print(dst)


if __name__ == "__main__":
    main(sys.argv[1:])
