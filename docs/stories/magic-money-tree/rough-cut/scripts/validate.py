#!/usr/bin/env python3
"""Check the cut list against the disk and against itself. Exit 1 on any ERROR.

    validate.py            every scene in cutlist/
    validate.py 01 02a     some scenes
    validate.py --timeline write cutlist/_timeline.json: every clip with absolute start/end, sorted

Errors: a file that is not on disk; a film clip whose src_in + dur passes src_max or the film's end;
a line id that is not in lines.json; an unknown track, kind or treatment; two clips overlapping on
one track; a _masters file (it carries sound we may not use). Warnings: gaps on V1 that no V3 card
covers; a clip with a `check` still open; a still pushed from an image under 1920 px wide.
"""
import glob, json, os, subprocess, sys
from functools import lru_cache

HERE = os.path.dirname(os.path.abspath(__file__))
RC = os.path.normpath(os.path.join(HERE, ".."))
CLIPS = "/mnt/d/badcode-videos/magic-money-tree/clips"
TRACKS = {"V1", "V2", "V3", "V4"}
KINDS = {"film", "still", "card", "doc", "chart", "illustration", "black"}
TREAT = {"FILM-43", "PUSH", "DRIFT", "INSET", "DOC", "HOLD", "XD", "DIP", "GRADE-BW", "FADE", "PULL", "LIT"}


@lru_cache(None)
def duration(p):
    try:
        return float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                                              "-of", "csv=p=0", p]).strip())
    except Exception:
        return None


@lru_cache(None)
def width(p):
    try:
        from PIL import Image
        Image.MAX_IMAGE_PIXELS = None
        return Image.open(p).size[0]
    except Exception:
        return None


def load(scenes):
    lines = {l["id"]: l for l in json.load(open(os.path.join(RC, "lines.json")))}
    files = sorted(glob.glob(os.path.join(RC, "cutlist", "*.json")))
    files = [f for f in files if not os.path.basename(f).startswith("_")]
    if scenes:
        files = [f for f in files if os.path.basename(f)[:-5] in scenes]
    return lines, [(f, json.load(open(f))) for f in files]


def timeline(lines, scenes):
    out = []
    for f, sc in scenes:
        for c in sc["clips"]:
            l = lines.get(c.get("line"))
            if not l:
                continue
            s = l["start"] + c.get("offset", 0)
            out.append(dict(c, scene=sc["scene"], start=round(s, 3), end=round(s + c["dur"], 3)))
    return sorted(out, key=lambda c: (c["start"], c["track"]))


def main(args):
    want = [a for a in args if not a.startswith("--")]
    lines, scenes = load(want)
    errs, warns = [], []
    for f, sc in scenes:
        for c in sc["clips"]:
            cid = f"{sc['scene']}:{c.get('id')}"
            for k in ("id", "line", "dur", "track", "kind"):
                if k not in c:
                    errs.append(f"{cid} missing {k}")
            if c.get("line") not in lines:
                errs.append(f"{cid} line {c.get('line')} not in lines.json")
            if c.get("track") not in TRACKS:
                errs.append(f"{cid} track {c.get('track')}")
            if c.get("kind") not in KINDS:
                errs.append(f"{cid} kind {c.get('kind')}")
            for t in (c.get("treatment") or "").split("+"):
                if t and t not in TREAT:
                    warns.append(f"{cid} unknown treatment {t}")
            if c.get("kind") == "black":
                continue
            p = os.path.join(CLIPS, c.get("file", ""))
            if "_masters" in c.get("file", ""):
                errs.append(f"{cid} uses a master (has sound): {c['file']}")
            if not c.get("file") or not os.path.exists(p):
                (warns if c.get("kind") == "illustration" else errs).append(f"{cid} file missing: {c.get('file')}")
                continue
            if c["kind"] == "film":
                d = duration(p)
                si, sm = c.get("src_in"), c.get("src_max")
                if si is None:
                    errs.append(f"{cid} film without src_in")
                else:
                    if sm is not None and si + c["dur"] > sm + 0.05:
                        errs.append(f"{cid} src_in {si} + dur {c['dur']} passes src_max {sm}")
                    if d and si + c["dur"] > d:
                        errs.append(f"{cid} runs past the film's end ({d:.1f}s)")
            if c["kind"] == "still" and "PUSH" in (c.get("treatment") or ""):
                w = width(p)
                if w and w < 1920:
                    warns.append(f"{cid} PUSH on a {w}px still (softens past 1.35x)")
            if c.get("check"):
                warns.append(f"{cid} CHECK: {c['check']}")
    tl = timeline(lines, scenes)
    for tr in TRACKS:
        cl = [c for c in tl if c["track"] == tr]
        for a, b in zip(cl, cl[1:]):
            if b["start"] < a["end"] - 0.05:
                errs.append(f"{tr} overlap {a['scene']}:{a['id']} ({a['start']}-{a['end']}) / {b['scene']}:{b['id']} ({b['start']}-{b['end']})")
    # holes: moments with nothing on V1, V2 or V3
    cover = sorted((c["start"], c["end"]) for c in tl if c["track"] in ("V1", "V2", "V3"))
    t = cover[0][0] if cover else 0
    for s, e in cover:
        if s > t + 0.1:
            warns.append(f"HOLE {t:.2f}-{s:.2f} ({s - t:.1f}s with no picture)")
        t = max(t, e)
    if "--timeline" in args:
        json.dump(tl, open(os.path.join(RC, "cutlist", "_timeline.json"), "w"), indent=1, ensure_ascii=False)
    for w in warns:
        print("warn ", w)
    for e in errs:
        print("ERROR", e)
    n = sum(len(sc["clips"]) for _, sc in scenes)
    print(f"{len(scenes)} scenes, {n} clips, {len(errs)} errors, {len(warns)} warnings; ends {t:.1f}s")
    sys.exit(1 if errs else 0)


if __name__ == "__main__":
    main(sys.argv[1:])
