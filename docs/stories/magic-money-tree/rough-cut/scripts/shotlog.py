#!/usr/bin/env python3
"""Index a film into shots, and draw a labelled contact sheet of them.

    shotlog.py <id> [<id> ...]      ids as in the conform status (e.g. gov.fdr.25.4, DiaryForTimothy)

Reads the film's DOWNLOADED master from a local copy (~/.cache/badcode/mmt-masters/, made by
run-shotlogs.sh), not the ProRes picture-only file on D:. The masters are a tenth of the size and
local, and the drvfs link to D: made the ProRes scan take hours. Every time written out is converted
to the picture-only file's clock (master time minus the master's start_time), because that file is
what Premiere will see. The masters are only read here; they are never imported (they carry sound).

For each film:
  rough-cut/shotlogs/<id>.tsv          one row per shot: n, in_s, out_s, dur_s, desc (desc blank until
                                       someone looks). A header comment records the source and offset
  <clips>/_shotlogs/<id>/sheet-NN.jpg  5x4 grids; each cell one frame, labelled "#n  in-out".
                                       Shots longer than 12 s get a frame every 8 s, labelled #n.a, #n.b…

Cuts come from ffmpeg's scene score on a 160 px proxy, deinterlaced first when the conform was.
The threshold starts at 0.30 and drops (0.18, then 0.10) for soft prints that leave shots averaging
over 20 s. Any shot under 0.6 s is folded into its neighbour: old film flickers, and a flash is not a cut.
"""
import csv, os, re, subprocess, sys, tempfile, shutil

HERE = os.path.dirname(os.path.abspath(__file__))
LOGS = os.path.normpath(os.path.join(HERE, "..", "shotlogs"))
CONFORM = os.path.normpath(os.path.join(HERE, "..", "..", "research", "footage-pass-2026-09-29", "scripts",
                                        "conform-status.tsv"))
LOCAL = os.path.expanduser("~/.cache/badcode/mmt-masters")
CLIPS = "/mnt/d/badcode-videos/magic-money-tree/clips"
FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"
MIN_SHOT, LONG, STEP = 0.6, 12.0, 8.0


def status():
    return {r["id"]: r for r in csv.DictReader(open(CONFORM), delimiter="\t")}


def probe(p, what):
    return subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", f"format={what}",
                                    "-of", "csv=p=0", p]).decode().strip()


def cuts(src, deint, d):
    fd, tmp = tempfile.mkstemp(suffix=".txt")
    os.close(fd)
    vf = ("yadif=1," if deint else "") + \
        f"scale=160:-2,select='gt(scene,0.04)',metadata=print:key=lavfi.scene_score:file={tmp}"
    subprocess.run(["ffmpeg", "-nostdin", "-hide_banner", "-v", "error", "-i", src, "-an", "-vf", vf,
                    "-f", "null", "-"], check=True)
    txt = open(tmp).read()
    os.remove(tmp)
    scored = [(float(t), float(v)) for t, v in
              re.findall(r"pts_time:([0-9.]+)\s*\n?lavfi.scene_score=([0-9.]+)", txt)]
    for th in (0.30, 0.18, 0.10):
        c = [t for t, v in scored if v > th]
        if d / (len(c) + 1) <= 20:
            break
    return c, th


def fmt(t):
    return f"{int(t // 60):02d}:{t % 60:05.2f}"


def frame(src, t_master, deint, label, dst):
    txt = label.replace(":", r"\:")
    vf = ("yadif=0," if deint else "") + \
        "scale=iw*sar:ih,setsar=1,scale=384:288:force_original_aspect_ratio=decrease,pad=384:300:(ow-iw)/2:0:black," \
        f"drawtext=fontfile={FONT}:text='{txt}':x=6:y=h-24:fontsize=15:fontcolor=white:box=1:boxcolor=black@0.7"
    subprocess.run(["ffmpeg", "-nostdin", "-v", "error", "-y", "-ss", f"{max(0, t_master - 0.2):.3f}", "-i", src,
                    "-ss", "0.2", "-frames:v", "1", "-vf", vf, dst], check=True)


def index(fid, row):
    src = os.path.join(LOCAL, row["master"])
    start = float(probe(src, "start_time") or 0)
    d = float(probe(src, "duration"))
    deint = row["filter"].startswith("yadif")
    raw, th = cuts(src, deint, d)
    edges = [0.0] + [c - start for c in raw if 0 < c - start < d] + [d]
    sh = []
    for a, b in zip(edges, edges[1:]):
        if sh and ((b - a) < MIN_SHOT or (sh[-1][1] - sh[-1][0]) < MIN_SHOT):
            sh[-1][1] = b
        else:
            sh.append([a, b])
    with open(os.path.join(LOGS, f"{fid}.tsv"), "w") as f:
        f.write(f"# source {row['master']} · offset -{start:.3f}s · threshold {th} · "
                f"deinterlaced {deint} · times are the picture-only file's clock\n")
        f.write("n\tin_s\tout_s\tdur_s\tdesc\n")
        for i, (a, b) in enumerate(sh, 1):
            f.write(f"{i}\t{a:.2f}\t{b:.2f}\t{b - a:.2f}\t\n")
    outdir = os.path.join(CLIPS, "_shotlogs", fid)
    shutil.rmtree(outdir, ignore_errors=True)
    os.makedirs(outdir)
    tmp = tempfile.mkdtemp()
    k = 0
    for i, (a, b) in enumerate(sh, 1):
        pts = [(a + b) / 2] if b - a <= LONG else [a + 1 + STEP * j for j in range(int((b - a - 2) // STEP) + 1)]
        for j, t in enumerate(pts):
            lab = f"#{i} {fmt(a)}-{fmt(b)}" if len(pts) == 1 else f"#{i}.{'abcdefghijklmnopqrstuvwxyz'[min(j, 25)]} @{fmt(t)}"
            frame(src, t + start, deint, lab, os.path.join(tmp, f"{k:05d}.png"))
            k += 1
    subprocess.run(["ffmpeg", "-nostdin", "-v", "error", "-y", "-i", os.path.join(tmp, "%05d.png"),
                    "-vf", "tile=5x4:padding=4:color=gray", "-q:v", "3",
                    os.path.join(outdir, "sheet-%02d.jpg")], check=True)
    shutil.rmtree(tmp)
    print(f"{fid}\t{len(sh)} shots\tthreshold {th}\t{len(os.listdir(outdir))} sheets", flush=True)


def main(ids):
    os.makedirs(LOGS, exist_ok=True)
    st = status()
    for fid in ids:
        if fid not in st:
            print(f"{fid}\tnot in conform status", flush=True)
            continue
        index(fid, st[fid])


if __name__ == "__main__":
    main(sys.argv[1:])
