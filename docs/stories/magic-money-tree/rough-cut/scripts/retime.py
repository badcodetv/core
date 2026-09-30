#!/usr/bin/env python3
"""Phase 2: set every line's real time from the recorded narration, and say where each part's
audio goes on the timeline.

    retime.py narration/parts.json

parts.json lists the chosen take for each part, in film order:
    [{"part": "P1", "clip": "<suno clip id>", "audio": "/abs/path/P1.wav",
      "aligned": "narration/P1.aligned.json"}, ...]
`aligned` is Suno's word alignment for that clip (`studio-api…/gen/<id>/aligned_lyrics/v2/`, pulled
with scripts/suno/.tmp/align.mts). A part with no take yet (P8 before its legal read) may give
"seconds": N instead, and its lines are spread evenly over N seconds of silence.

How the film is laid out: the first part's first word lands at its planned time, or later if the take's
intro is longer (the opening picture then stretches over the intro). Each later part's
first word lands GAP seconds after the previous part's last word, where GAP is the pause the edit
plan gives that seam (a title card, a movement's dip to black, the end of the film before the coda).
Inside a part the voice decides everything: a line's picture starts 2 frames before its first word
and runs until the next line's does.

Writes lines.json (start/end become real; plan_start/plan_end are kept) and
narration/_placement.json: where each part's audio starts on the timeline, and on which audio
track (parts alternate A1/A2 so a score's tail can overlap the next part's head).
Re-running lines.py afterwards throws the real times away; re-run this after it.
"""
import json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
RC = os.path.normpath(os.path.join(HERE, ".."))
LEAD = 2 / 25                      # picture leads the word by two frames
GAP = {"P2": 6.0, "P3": 1.5, "P4": 3.0, "P5": 1.5, "P6": 3.0, "P7": 3.0, "P8": 1.5, "P9": 3.0, "P10": 5.0}
GAP_DEFAULT = 1.5
TAIL = {"P5": 4.0, "P9": 5.0, "P10": 3.0}   # silence held after a part's last word (scene 08, the end, the coda)


def norm(w):
    return re.sub(r"[^a-z0-9']", "", w.lower().replace("’", "'"))


def words_of(text):
    return [norm(w) for w in re.split(r"\s+|\.\.\.|…", text) if norm(w)]


def find_starts(lines, aligned):
    """Walk the aligned words in order and find where each line's words begin. Tolerant of
    Suno splitting or merging a word, and of section tags glued to the first word."""
    aw = []
    for a in aligned:
        tok = a["word"].split("]")[-1]          # drop a "[Monologue …]\n" tag glued to the word
        for w in words_of(tok):
            aw.append((w, a["start_s"], a["end_s"]))
    starts, ends, j = [], [], 0
    for l in lines:
        ws = words_of(l["text"])
        best = None
        for k in range(j, min(len(aw), j + 60)):            # the first word, near where we are
            if aw[k][0] == ws[0] or (len(ws) > 1 and k + 1 < len(aw) and aw[k + 1][0] == ws[1]):
                best = k
                break
        if best is None:
            best = j
        starts.append(aw[best][1] if best < len(aw) else None)
        k_end = min(len(aw) - 1, best + len(ws) - 1)
        ends.append(aw[k_end][2] if aw else None)
        j = k_end + 1
    return starts, ends


def main(path):
    parts = json.load(open(path))
    base = os.path.dirname(os.path.abspath(path))
    L = json.load(open(os.path.join(RC, "lines.json")))
    for l in L:
        l.setdefault("plan_start", l["start"])
        l.setdefault("plan_end", l["end"])
    placement, cursor, report = [], None, []
    for i, p in enumerate(parts):
        pl = [l for l in L if l["part"] == p["part"]]
        if "aligned" in p:
            al = json.load(open(os.path.join(base, p["aligned"]) if not os.path.isabs(p["aligned"]) else p["aligned"]))
            s, e = find_starts(pl, al["aligned_words"])
        else:
            n = p["seconds"]
            s = [n * k / len(pl) for k in range(len(pl))]
            e = [n * (k + 1) / len(pl) - 0.3 for k in range(len(pl))]
        first = s[0] or 0.0
        at = max(pl[0]["plan_start"], first) if cursor is None else cursor + GAP.get(p["part"], GAP_DEFAULT)
        offset = at - first                          # timeline time = audio time + offset
        for k, l in enumerate(pl):
            l["start"] = round((s[k] if s[k] is not None else s[k - 1]) + offset - LEAD, 3)
            if s[k] is None:
                report.append(f"{l['id']} not found in the alignment; placed after the previous line")
        last_word = max(x for x in e if x is not None) + offset
        for k, l in enumerate(pl):
            l["end"] = round(pl[k + 1]["start"] if k + 1 < len(pl) else last_word + TAIL.get(p["part"], 0.4), 3)
        cursor = last_word + TAIL.get(p["part"], 0.0)
        placement.append({"part": p["part"], "audio": p.get("audio"), "clip": p.get("clip"),
                          "timeline_start": round(offset, 3), "track": "A1" if i % 2 == 0 else "A2",
                          "first_word": round(first + offset, 3), "last_word": round(last_word, 3)})
    json.dump(L, open(os.path.join(RC, "lines.json"), "w"), indent=1, ensure_ascii=False)
    json.dump(placement, open(os.path.join(base, "_placement.json"), "w"), indent=1)
    for r in report:
        print("warn", r)
    for pl in placement:
        print(f"{pl['part']:>4} on {pl['track']} at {pl['timeline_start']:8.2f}s  words {pl['first_word']:.2f}–{pl['last_word']:.2f}")
    print(f"film ends ≈ {cursor:.1f}s ({int(cursor // 60)}:{cursor % 60:04.1f})")


if __name__ == "__main__":
    main(sys.argv[1])
