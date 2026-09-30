#!/usr/bin/env python3
"""Render a low-resolution PREVIEW of the cut list with ffmpeg. Viewing only: the edit is the
Premiere timeline (house ruling 2026-08-24), this is so the film can be watched before Premiere.

    preview.py                         whole film  -> <media>/previews/rough-cut-preview.mp4
    preview.py 01 02                   some scenes -> <media>/previews/preview-01-02.mp4
    preview.py --audio narration.wav   lay one audio file under the whole film (phase 2)

How: split time at every clip edge; in each slice the top track wins (V3 over V2 over V1), except
that V4 labels are laid over whatever is below. Each slice is rendered to its own 960x540 25 fps
file, the slices are joined, then labels and the narration text (as subtitles, from lines.json)
go on top. Transitions are hard cuts here; Premiere does the dissolves.
"""
import glob, json, os, subprocess, sys, tempfile, shutil

HERE = os.path.dirname(os.path.abspath(__file__))
RC = os.path.normpath(os.path.join(HERE, ".."))
MEDIA = "/mnt/d/badcode-videos/magic-money-tree"
CLIPS = os.path.join(MEDIA, "clips")
W, H, FPS = 960, 540, 25
sys.path.insert(0, HERE)
import validate  # noqa: E402

ORDER = {"V3": 3, "V2": 2, "V1": 1}
FIT = f"scale=iw*sar:ih,setsar=1,scale={W}:{H}:force_original_aspect_ratio=decrease,pad={W}:{H}:(ow-iw)/2:(oh-ih)/2"


def ff(args):
    subprocess.run(["ffmpeg", "-nostdin", "-v", "error", "-y"] + args, check=True)


def enc(dst):
    return ["-r", str(FPS), "-pix_fmt", "yuv420p", "-c:v", "libx264", "-preset", "veryfast", "-crf", "24", "-an", dst]


def render_slice(c, a, b, dst):
    d = round(b - a, 3)
    if d <= 0.01:
        return False
    tr = c.get("treatment") or ""
    if c["kind"] == "black" or not c.get("file"):
        ff(["-f", "lavfi", "-t", str(d), "-i", f"color=black:s={W}x{H}:r={FPS}"] + enc(dst))
        return True
    p = os.path.join(CLIPS, c["file"])
    if not os.path.exists(p):
        ff(["-f", "lavfi", "-t", str(d), "-i", f"color=0x302020:s={W}x{H}:r={FPS}", "-vf",
            f"drawtext=fontfile=/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf:text='MISSING {os.path.basename(c['file'])[:40]}':"
            f"x=(w-tw)/2:y=(h-th)/2:fontsize=22:fontcolor=white"] + enc(dst))
        return True
    if c["kind"] == "film":
        src = c["src_in"] + (a - c["start"])
        vf = FIT + (",hue=s=0" if "GRADE-BW" in tr else "")
        ff(["-ss", f"{src:.3f}", "-t", str(d), "-i", p, "-vf", vf] + enc(dst))
        return True
    # still-like: stills, cards, docs, charts, illustrations
    n = max(1, int(round(d * FPS)))
    f0 = (a - c["start"]) / c["dur"]
    f1 = (b - c["start"]) / c["dur"]
    pre = "scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2,setsar=1"
    if "INSET" in tr or c["kind"] == "doc":
        k = 0.62 if "INSET" in tr else 0.9
        pre = (f"scale={int(1920 * k)}:{int(1080 * k)}:force_original_aspect_ratio=decrease,"
               f"pad=iw+8:ih+8:4:4:0xd8d8d0,pad=1920:1080:(ow-iw)/2:(oh-ih)/2:0x050607,setsar=1")
    mv = c.get("move")
    if mv:
        (x0, y0, z0), (x1, y1, z1) = mv["from"], mv["to"]
    elif "PUSH" in tr:
        x0 = y0 = x1 = y1 = 0.5
        z0, z1 = 1.0, (1.06 if c["kind"] in ("doc",) or "INSET" in tr else 1.12)
    elif "DRIFT" in tr:
        x0, x1, y0, y1, z0, z1 = 0.46, 0.54, 0.5, 0.5, 1.1, 1.1
    else:
        x0 = y0 = x1 = y1 = 0.5
        z0 = z1 = 1.0
    za, zb = z0 + (z1 - z0) * f0, z0 + (z1 - z0) * f1
    xa, xb = x0 + (x1 - x0) * f0, x0 + (x1 - x0) * f1
    ya, yb = y0 + (y1 - y0) * f0, y0 + (y1 - y0) * f1
    z = f"{za}+({zb}-{za})*on/{n}"
    x = f"({xa}+({xb}-{xa})*on/{n})*iw-iw/zoom/2"
    y = f"({ya}+({yb}-{ya})*on/{n})*ih-ih/zoom/2"
    ff(["-loop", "1", "-framerate", str(FPS), "-t", str(d), "-i", p, "-vf",
        f"{pre},zoompan=z='{z}':x='{x}':y='{y}':d=1:s={W}x{H}:fps={FPS}", "-frames:v", str(n)] + enc(dst))
    return True


def srt_time(t):
    ms = int(round(t * 1000))
    return f"{ms // 3600000:02d}:{ms // 60000 % 60:02d}:{ms // 1000 % 60:02d},{ms % 1000:03d}"


def main(args):
    audio = None
    if "--audio" in args:
        audio = args[args.index("--audio") + 1]
        args = [a for a in args if a not in ("--audio", audio)]
    lines, scenes = validate.load(args)
    tl = validate.timeline(lines, scenes)
    if not tl:
        sys.exit("empty cut list")
    t0, t1 = min(c["start"] for c in tl), max(c["end"] for c in tl)
    edges = sorted({round(t, 3) for c in tl for t in (c["start"], c["end"])})
    tmp = tempfile.mkdtemp(prefix="mmt-preview-")
    parts = []
    for i, (a, b) in enumerate(zip(edges, edges[1:])):
        live = [c for c in tl if c["track"] in ORDER and c["start"] <= a + 1e-3 and c["end"] >= b - 1e-3]
        top = max(live, key=lambda c: ORDER[c["track"]]) if live else {"kind": "black", "start": a, "dur": b - a}
        dst = os.path.join(tmp, f"{i:05d}.mp4")
        if render_slice(top, a, b, dst):
            parts.append(dst)
        print(f"\r{i + 1}/{len(edges) - 1} slices", end="", flush=True)
    print()
    with open(os.path.join(tmp, "list.txt"), "w") as f:
        f.writelines(f"file '{p}'\n" for p in parts)
    joined = os.path.join(tmp, "joined.mp4")
    ff(["-f", "concat", "-safe", "0", "-i", os.path.join(tmp, "list.txt"), "-c", "copy", joined])
    # subtitles: the narration text at its (planned or real) time
    srt = os.path.join(tmp, "lines.srt")
    ls = sorted((l for l in lines.values() if l.get("start") is not None and t0 - 0.01 <= l["start"] < t1),
                key=lambda l: l["start"])
    with open(srt, "w") as f:
        for k, l in enumerate(ls, 1):
            f.write(f"{k}\n{srt_time(l['start'] - t0)} --> {srt_time(l['end'] - t0)}\n{l['text']}\n\n")
    labels = [c for c in tl if c["track"] == "V4" and c.get("file") and os.path.exists(os.path.join(CLIPS, c["file"]))]
    inputs, chain, last = ["-i", joined], [], "0:v"
    for j, c in enumerate(labels, 1):
        inputs += ["-i", os.path.join(CLIPS, c["file"])]
        chain.append(f"[{j}:v]scale={W}:{H}[l{j}];[{last}][l{j}]overlay=enable='between(t,{c['start'] - t0},{c['end'] - t0})'[o{j}]")
        last = f"o{j}"
    style = "FontName=DejaVu Sans,FontSize=15,PrimaryColour=&H00F0F0F0,OutlineColour=&H80000000,BorderStyle=3,Outline=1,Shadow=0,MarginV=18"
    chain.append(f"[{last}]subtitles={srt}:force_style='{style}'[out]")
    out_dir = os.path.join(MEDIA, "previews")
    os.makedirs(out_dir, exist_ok=True)
    name = "rough-cut-preview.mp4" if not args else f"preview-{'-'.join(args)}.mp4"
    out = os.path.join(out_dir, name)
    aud = ["-i", audio] if audio else []
    amap = ["-map", f"{len(labels) + 1}:a", "-c:a", "aac", "-b:a", "128k", "-shortest"] if audio else []
    ff(inputs + aud + ["-filter_complex", ";".join(chain), "-map", "[out]"] + amap +
       ["-r", str(FPS), "-pix_fmt", "yuv420p", "-c:v", "libx264", "-preset", "veryfast", "-crf", "23",
        "-movflags", "+faststart", out])
    shutil.rmtree(tmp)
    print(out)


if __name__ == "__main__":
    main(sys.argv[1:])
