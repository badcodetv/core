#!/usr/bin/env python3
"""Measure every Style / Exclude / Lyrics box in a song sheet against Suno's 1,000-char Style cap.

Suno's Style textarea carries maxLength="1000", so an over-cap paste is TRUNCATED, never rejected
— and the tail of a box is where the bans live. A box over the cap does not fail loudly; it just
stops obeying the last thing you wrote. So measure after every edit, never estimate.

Reads the same structure `suno.mts extract` reads: each atom is a "### " heading whose fenced
blocks are, in order, Style, Exclude styles and (for a voice atom) Lyrics.

    python3 scripts/suno/measure-boxes.py docs/stories/gitpush-origin-master/songs/narration-v6.md
"""
import re
import sys

STYLE_CAP = 1000
NAMES = ["style", "exclude", "lyrics"]


def measure(path: str) -> int:
    src = open(path, encoding="utf-8").read()
    parts = re.split(r"\n(### .*)\n", src)
    over = 0
    for i in range(1, len(parts), 2):
        head, body = parts[i], parts[i + 1]
        fences = re.findall(r"\n```([a-z]*)\n(.*?)\n```\n", body, re.S)
        # Skip prose sections whose first fence is a shell/py block rather than a Style box.
        if not fences or fences[0][0] not in ("", "lyrics"):
            continue
        name = head.strip().split("`")[1] if "`" in head else head.strip("# ")
        for j, (_label, text) in enumerate(fences[:3]):
            box = NAMES[j]
            bad = box == "style" and len(text) > STYLE_CAP
            over += bad
            print(f"{name:14s} {box:8s} {len(text):5d}  {'🔴 OVER ' + str(STYLE_CAP) if bad else ''}")
    return over


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    sys.exit(1 if measure(sys.argv[1]) else 0)
