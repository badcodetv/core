#!/usr/bin/env python3
"""Turn the cut list into exactly what Premiere needs: per clip, the track, the timeline start/end,
the source in-point, and the Motion/Opacity values (with keyframes) that realise its treatment.

    premiere-plan.py            -> cutlist/_premiere.json (and a one-line summary per track)

Sequence: 1920x1080, 25 fps, square pixels (edit-plan §0.2). Tracks V1..V4 = videoTrack 0..3.
Motion (component 1): param 0 Position {x,y} as 0-1 fractions of the frame, param 1 Scale (%).
Opacity (component 0) param 0. Keyframe times are seconds FROM THE CLIP'S START; the executor
adds the clip's timeline start if the API wants sequence time (check once with export_frame).

Treatments (edit-plan §0.3), in Premiere terms:
  FILM-43   scale so the picture's height fills 1080 (Premiere applies the pixel aspect itself), centred
  still     fit inside 1920x1080; PUSH = fit -> fit x 1.12 (bezier); DRIFT = x 0.46 -> 0.54 at fit x 1.1;
            HOLD = fit, no keys; `move` overrides with explicit from/to (centre as a fraction of the IMAGE)
  INSET     fit x 0.62, capped at 135% of native, push at most x 1.05
  DOC       fit x 0.9 on V2, and V1 underneath dimmed to 35% opacity for the same span
  card      100% (they are rendered at 1920x1080)
  FADE/DIP  opacity keys 0->100 at the head / 100->0 at the tail over 12 frames
"""
import json, os, subprocess, sys
from functools import lru_cache

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import validate  # noqa: E402

CLIPS = validate.CLIPS
W, H, FR = 1920, 1080, 1 / 25


@lru_cache(None)
def size(rel):
    p = os.path.join(CLIPS, rel)
    if rel.lower().endswith((".mov", ".mp4", ".mpg", ".mpeg")):
        out = subprocess.check_output(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries",
                                       "stream=width,height,sample_aspect_ratio", "-of", "csv=p=0", p]).decode().strip()
        w, h, sar = out.split(",")[:3]
        n, d = (sar.split(":") + ["1"])[:2] if sar not in ("N/A", "0:1") else ("1", "1")
        return int(w) * int(n) / int(d), int(h)          # display size
    from PIL import Image
    Image.MAX_IMAGE_PIXELS = None
    return Image.open(p).size


def motion(c):
    tr = (c.get("treatment") or "").split("+")
    if c["kind"] == "black":
        return None
    w, h = size(c["file"])
    if c["kind"] in ("film", "chart") and "FILM-43" in tr or c["kind"] == "film":
        s = 100 * H / h
        return {"scale": [[0, round(s, 2)]], "pos": [[0, [0.5, 0.5]]]}
    fit = 100 * min(W / w, H / h)
    if c["kind"] in ("card", "chart") and (w, h) == (W, H):
        return {"scale": [[0, 100]], "pos": [[0, [0.5, 0.5]]]}
    if "INSET" in tr:
        base = min(fit * 0.62, 135.0)
        end = base * (1.05 if "PUSH" in tr else 1.0)
        return {"scale": [[0, round(base, 2)], [c["dur"], round(end, 2)]], "pos": [[0, [0.5, 0.5]]]}
    if "DOC" in tr or c["kind"] == "doc":
        base = fit * 0.9
        return {"scale": [[0, round(base, 2)], [c["dur"], round(base * 1.05, 2)]], "pos": [[0, [0.5, 0.5]]]}
    mv = c.get("move")
    if mv:
        keys_s, keys_p = [], []
        for t, (cx, cy, z) in ((0, mv["from"]), (c["dur"], mv["to"])):
            s = fit * z
            # put image point (cx, cy) at frame centre: offset of that point from the image centre, scaled
            px = 0.5 - (cx - 0.5) * w * s / 100 / W
            py = 0.5 - (cy - 0.5) * h * s / 100 / H
            keys_s.append([t, round(s, 2)])
            keys_p.append([t, [round(px, 4), round(py, 4)]])
        return {"scale": keys_s, "pos": keys_p}
    if "DRIFT" in tr:
        s = fit * 1.1
        return {"scale": [[0, round(s, 2)]], "pos": [[0, [0.46, 0.5]], [c["dur"], [0.54, 0.5]]]}
    if "PUSH" in tr:
        return {"scale": [[0, round(fit, 2)], [c["dur"], round(fit * 1.12, 2)]], "pos": [[0, [0.5, 0.5]]]}
    return {"scale": [[0, round(fit, 2)]], "pos": [[0, [0.5, 0.5]]]}


def opacity(c):
    tr = (c.get("treatment") or "").split("+")
    k = []
    if "FADE" in tr or "DIP" in tr and c.get("offset", 0) == 0:
        k += [[0, 0], [12 * FR, 100]]
    if "DIP" in tr:
        k += [[max(0, c["dur"] - 12 * FR), 100], [c["dur"], 0]]
    return k or None


def main():
    lines, scenes = validate.load([])
    tl = validate.timeline(lines, scenes)
    out = []
    docs = [(c["start"], c["end"]) for c in tl if c["track"] == "V2" and ("DOC" in (c.get("treatment") or "") or c["kind"] == "doc")]
    for c in tl:
        e = {"id": f"{c['scene']}:{c['id']}", "track": int(c["track"][1]) - 1, "kind": c["kind"],
             "file": c.get("file"), "start": c["start"], "end": c["end"], "dur": c["dur"],
             "in": c.get("src_in", 0.0) or 0.0, "motion": motion(c), "opacity": opacity(c),
             "xd_out": "XD" in (c.get("treatment") or ""), "grade_bw": "GRADE-BW" in (c.get("treatment") or ""),
             "check": c.get("check"), "credit": c.get("credit")}
        if c["track"] == "V1":
            dim = [(max(a, c["start"]) - c["start"], min(b, c["end"]) - c["start"]) for a, b in docs
                   if a < c["end"] and b > c["start"]]
            if dim:
                e["dim_under_doc"] = [[round(a, 3), round(b, 3)] for a, b in dim]
        out.append(e)
    json.dump(out, open(os.path.join(validate.RC, "cutlist", "_premiere.json"), "w"), indent=1, ensure_ascii=False)
    for t in range(4):
        cl = [e for e in out if e["track"] == t]
        print(f"V{t + 1}: {len(cl)} clips" + (f", {cl[0]['start']:.1f}–{cl[-1]['end']:.1f}s" if cl else ""))


if __name__ == "__main__":
    main()
