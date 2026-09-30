#!/usr/bin/env python3
"""Build rough-cut/lines.json: every spoken line, keyed by part (P1.01 …), with its planned clock.

The words come from songs/narration.md (what Suno will speak). The planned clock and scene come from
edit-plan.md, matched by normalised text. A line the edit plan does not carry gets clock null and is
reported, so drift between the two files is visible rather than silent.

    lines.py            write lines.json and print the unmatched lines
"""
import json, os, re, difflib

HERE = os.path.dirname(os.path.abspath(__file__))
MMT = os.path.normpath(os.path.join(HERE, "..", ".."))
NUM = {"nineteen forty": "1940", "nineteen forty-eight": "1948", "nineteen twenty-three": "1923",
       "nineteen forty-five": "1945", "nineteen forty-six": "1946", "nineteen forty-two": "1942",
       "two thousand and eight": "2008", "twenty ten": "2010", "twenty seventeen": "2017",
       "twenty twenty": "2020", "nineteen thirties": "1930s", "july the fifth": "july 5th"}


def norm(s):
    s = s.lower().replace("…", " ").replace("...", " ").replace("’", "'").replace("‘", "'")
    s = re.sub(r"[\"“”*_()\[\]]", "", s)
    s = re.sub(r"[^a-z0-9£%' ]+", " ", s)
    return re.sub(r"\s+", " ", s).strip()


def parts():
    txt = open(os.path.join(MMT, "songs", "narration.md")).read()
    out = []
    for m in re.finditer(r"^### (P\d+) · (.+?)\n(.*?)(?=^### P\d+|^## )", txt, re.S | re.M):
        pid, title, body = m.group(1), m.group(2), m.group(3)
        lyr = re.search(r"```lyrics\n(.*?)```", body, re.S)
        lines = [l.strip() for l in lyr.group(1).splitlines() if l.strip() and not l.startswith("[")]
        out.append((pid, title, lines))
    return out


def plan_rows():
    txt = open(os.path.join(MMT, "edit-plan.md")).read()
    rows, scene = [], None
    for l in txt.splitlines():
        m = re.match(r"^### Scene (\w+) — (.+?) · (\d\d:\d\d)", l)
        if m:
            scene = m.group(1)
        m = re.match(r"^\| (\d\d):(\d\d) \| (.*?) \|", l)
        if m and scene:
            words = re.findall(r"[\"“](.+?)[\"”](?=[^\"”]*$|\s|$)", m.group(3)) or [m.group(3)]
            rows.append({"scene": scene, "clock": int(m.group(1)) * 60 + int(m.group(2)), "text": m.group(3)})
    return rows


SCENE_END = 910  # 15:10, the end of scene 15 in the edit plan


def plan_times(out):
    """Give every line a planned start and end. Lines that share an edit-plan row share its time,
    split by word count; a row runs until the next row's clock."""
    clocks = sorted({l["clock"] for l in out if l["clock"] is not None})
    for i, c in enumerate(clocks):
        nxt = clocks[i + 1] if i + 1 < len(clocks) else SCENE_END
        grp = [l for l in out if l["clock"] == c]
        total = sum(l["words"] for l in grp) or 1
        t = float(c)
        for l in grp:
            span = (nxt - c) * l["words"] / total
            l["start"], l["end"] = round(t, 2), round(t + span, 2)
            l["plan_start"], l["plan_end"] = l["start"], l["end"]
            t += span


def main():
    rows = plan_rows()
    for r in rows:
        r["n"] = norm(r["text"])
    out, unmatched = [], []
    for pid, title, lines in parts():
        for i, line in enumerate(lines, 1):
            spoken = line
            for k, v in sorted(NUM.items(), key=lambda kv: -len(kv[0])):
                spoken = re.sub(k, v, spoken, flags=re.I)
            n = norm(spoken)
            best, score = None, 0.0
            for r in rows:
                if n and n in r["n"]:
                    s = 1.0
                else:
                    s = difflib.SequenceMatcher(None, n, r["n"]).ratio()
                if s > score:
                    best, score = r, s
            rec = {"id": f"{pid}.{i:02d}", "part": pid, "text": line, "words": len(line.split())}
            if best and score >= 0.55:
                rec.update(scene=best["scene"], clock=best["clock"], match=round(score, 2))
            else:
                rec.update(scene=None, clock=None, match=round(score, 2))
                unmatched.append(rec)
            out.append(rec)
    # a reworded line keeps its slot: the plan row, between its neighbours, that no line took
    used = {l["clock"] for l in out if l["clock"] is not None}
    for i, l in enumerate(out):
        if l["clock"] is None:
            prev = next((o["clock"] for o in reversed(out[:i]) if o["clock"] is not None), -1)
            nxt = next((o["clock"] for o in out[i + 1:] if o["clock"] is not None), 10 ** 6)
            free = [r for r in rows if prev < r["clock"] < nxt and r["clock"] not in used]
            if free:
                l.update(scene=free[0]["scene"], clock=free[0]["clock"], match="slot")
                used.add(free[0]["clock"])
                unmatched.remove(l)
            elif prev >= 0:
                src = next(o for o in reversed(out[:i]) if o["clock"] is not None)
                l.update(scene=src["scene"], clock=src["clock"], match="prev")
                unmatched.remove(l)
    plan_times(out)
    json.dump(out, open(os.path.join(MMT, "rough-cut", "lines.json"), "w"), indent=1, ensure_ascii=False)
    print(f"{len(out)} lines, {len(unmatched)} unmatched")
    for u in unmatched:
        print("  ", u["id"], u["match"], u["text"][:90])


if __name__ == "__main__":
    main()
