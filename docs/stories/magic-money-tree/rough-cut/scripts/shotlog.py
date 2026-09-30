#!/usr/bin/env python3
"""Index a picture-only film into shots, and draw a labelled contact sheet of them.

    shotlog.py <clip.mov> [<clip.mov> ...]

For each film:
  rough-cut/shotlogs/<id>.tsv          one row per shot: n, in_s, out_s, dur_s, desc (desc left blank
                                       for a human or an agent to fill)
  <clips>/_shotlogs/<id>/sheet-NN.jpg  5x4 grids; each cell is one frame, labelled "#n  in-out".
                                       Shots longer than 12 s get a frame every 8 s, labelled #n.a, #n.b…

Cuts come from ffmpeg's scene score (threshold 0.30) on a 160 px proxy, then any shot shorter
than 0.6 s is merged into its neighbour: old film flickers, and a flash is not a cut.
Times are seconds in the picture-only file, which is what Premiere will see.
"""
import os, re, subprocess, sys, tempfile, shutil

HERE = os.path.dirname(os.path.abspath(__file__))
LOGS = os.path.normpath(os.path.join(HERE, "..", "shotlogs"))
CLIPS = "/mnt/d/badcode-videos/magic-money-tree/clips"
FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"
THRESH, MIN_SHOT, LONG, STEP = 0.30, 0.6, 12.0, 8.0


def duration(p):
    return float(subprocess.check_output(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", p]).strip())


def cuts(p):
    r = subprocess.run(
        ["ffmpeg", "-nostdin", "-hide_banner", "-i", p, "-an", "-vf",
         f"scale=160:-2,select='gt(scene,{THRESH})',showinfo", "-f", "null", "-"],
        capture_output=True, text=True)
    return [float(m) for m in re.findall(r"pts_time:([0-9.]+)", r.stderr)]


def shots(p):
    d = duration(p)
    edges = [0.0] + [c for c in cuts(p) if 0 < c < d] + [d]
    out = []
    for a, b in zip(edges, edges[1:]):
        if out and (b - a) < MIN_SHOT:
            out[-1][1] = b          # flash: fold into the previous shot
        elif out and (out[-1][1] - out[-1][0]) < MIN_SHOT:
            out[-1][1] = b
        else:
            out.append([a, b])
    return out


def fmt(t):
    return f"{int(t // 60):02d}:{t % 60:05.2f}"


def frame(p, t, label, dst):
    txt = label.replace(":", r"\:")
    subprocess.run(
        ["ffmpeg", "-nostdin", "-v", "error", "-y", "-ss", f"{t:.3f}", "-i", p, "-frames:v", "1",
         "-vf", f"scale=iw*sar:ih,setsar=1,scale=384:288:force_original_aspect_ratio=decrease,pad=384:300:(ow-iw)/2:0:black,"
                f"drawtext=fontfile={FONT}:text='{txt}':x=6:y=h-24:fontsize=15:fontcolor=white:"
                f"box=1:boxcolor=black@0.7", dst], check=True)


def main(paths):
    os.makedirs(LOGS, exist_ok=True)
    for p in paths:
        fid = os.path.basename(p).replace(".picture-only.mov", "")
        sh = shots(p)
        with open(os.path.join(LOGS, f"{fid}.tsv"), "w") as f:
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
                suffix = "" if len(pts) == 1 else "." + "abcdefghijklmnopqrstuvwxyz"[min(j, 25)]
                frame(p, t, f"#{i}{suffix} {fmt(a)}-{fmt(b)}" if not suffix else f"#{i}{suffix} @{fmt(t)}",
                      os.path.join(tmp, f"{k:05d}.png"))
                k += 1
        subprocess.run(["ffmpeg", "-nostdin", "-v", "error", "-y", "-i", os.path.join(tmp, "%05d.png"),
                        "-vf", "tile=5x4:padding=4:color=gray", "-q:v", "3",
                        os.path.join(outdir, "sheet-%02d.jpg")], check=True)
        shutil.rmtree(tmp)
        print(f"{fid}\t{len(sh)} shots\t{len(os.listdir(outdir))} sheets", flush=True)


if __name__ == "__main__":
    main(sys.argv[1:])
