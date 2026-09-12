#!/usr/bin/env python3
"""Measure every Style / Exclude / Lyrics box in a song sheet against Suno's 1,000-char Style cap.

Suno's Style textarea carries maxLength="1000", so an over-cap paste is TRUNCATED, never rejected
— and the tail of a box is where the bans live. A box over the cap does not fail loudly; it just
stops obeying the last thing you wrote. So measure after every edit, never estimate.

Reads the same structure `suno.mts extract` reads: each atom is a "### " heading whose fenced
blocks are, in order, Style, Exclude styles and (for a bed) nothing else.

🔴 **Silence is not a pass.** Every "### " section is reported, including the ones with no boxes in
them, and the script exits non-zero if it measured nothing or if a section's fence count is not 2
or 3. That rule exists because of a real near-miss (2026-09-12, camping-v6): a sheet whose three
boxes sat under *separate* sub-headings made `extract` return a shell example as the Style box,
shift every box by one and drop the lyrics entirely — a silent instrumental for 20 credits. The
first version of this script skipped that section and exited 0, which read exactly like a pass.

    python3 scripts/suno/measure-boxes.py docs/stories/gitpush-origin-master/songs/narration-v6.md
"""
import re
import sys

STYLE_CAP = 1000
NAMES = ["style", "exclude", "lyrics"]
# A box fence carries no language, or `lyrics`. Anything else (bash, python, taste) is not a box.
BOX_LABELS = ("", "lyrics")


def measure(path: str) -> int:
    src = open(path, encoding="utf-8").read()
    parts = re.split(r"\n(### .*)\n", src)
    problems = 0
    measured = 0
    for i in range(1, len(parts), 2):
        head, body = parts[i], parts[i + 1]
        name = head.strip().split("`")[1] if "`" in head else head.strip("# ").strip()
        fences = re.findall(r"\n```([a-z]*)\n(.*?)\n```\n", body, re.S)
        if not fences:
            print(f"{name[:28]:28s} —        prose section, no fences")
            continue
        if fences[0][0] not in BOX_LABELS:
            # Not an atom: its first fence is a shell/python example, not a Style box.
            print(f"{name[:28]:28s} —        SKIPPED: first fence is ```{fences[0][0]}, not a box")
            continue
        measured += 1
        if len(fences) not in (2, 3):
            print(f"{name[:28]:28s} 🔴 {len(fences)} fences — an atom is style + exclude (+ lyrics). "
                  f"`extract` will mis-assign them")
            problems += 1
        for j, (label, text) in enumerate(fences[:3]):
            box = NAMES[j]
            over = box == "style" and len(text) > STYLE_CAP
            problems += over
            if label not in BOX_LABELS:
                print(f"{name[:28]:28s} 🔴 fence {j} is ```{label} — not a box")
                problems += 1
            print(f"{name[:28]:28s} {box:8s} {len(text):5d}  {'🔴 OVER ' + str(STYLE_CAP) if over else ''}")
    if not measured:
        print(f"🔴 no atoms found in {path} — every '### ' section was prose or skipped. "
              f"If this sheet has boxes, `extract` will not find them either.")
        problems += 1
    print(f"\n{measured} atom(s) measured, {problems} problem(s).")
    return problems


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    sys.exit(1 if measure(sys.argv[1]) else 0)
