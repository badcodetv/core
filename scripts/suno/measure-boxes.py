#!/usr/bin/env python3
"""Measure every Style / Exclude / Lyrics box in a song sheet against Suno's 1,000-char Style cap.

Suno's Style textarea carries maxLength="1000", so an over-cap paste is TRUNCATED, never rejected
— and the tail of a box is where the bans live. A box over the cap does not fail loudly; it just
stops obeying the last thing you wrote. So measure after every edit, never estimate.

Reads the same structure `suno.mts extract` reads: each atom is a "### " heading holding two or
three fenced boxes — Style, Exclude styles, and (for a voice atom) Lyrics. Fences may be bare or
labelled ```style / ```exclude / ```lyrics; both spellings are in use across our sheets.

🔴 **Silence is not a pass.** Every "### " section is reported, including the ones with no boxes in
them, and the script exits non-zero if it measured no atoms at all, or if an atom holds more boxes
than `extract` will read. That rule exists because of a real near-miss (2026-09-12, camping-v6): a
sheet whose boxes sat under *separate* sub-headings made `extract` return a shell example as the
Style box, shift every box by one and drop the lyrics entirely — a silent instrumental for 20
credits. The first version of this script skipped that section and exited 0, which read exactly
like a pass.

⚠️ **A lone fence is named from its heading, not from its position.** In an atom the boxes are
identified by order; a section holding one fence could be a retired ```taste block, a lyrics
excerpt or a real Style box, and calling it "style" because it came first is how a 1,660-character
taste block gets reported as over-cap. So a lone fence under a heading naming taste, lyrics, style
or excludes is named that, and anything else is reported without a verdict. **The cap is applied to
every box we can actually identify as a Style box** — suppressing it for lone fences would have
stopped checking camping.md's real Style box, which sits three characters under the cap.

🔑 **The cap's real victim is a box nobody measured, and a box typed straight into the browser is
one of those.** Thread 05, 2026-09-12: across 33 written camping lanes and every GPOM narration box,
not one was over the cap — but a box grown by hand in Suno, fusing clauses from several lanes,
reached 1,186 characters, and the drum mechanics at its tail were never sent. Measure the sheet;
then keep the browser honest by pasting from the sheet rather than typing into it.

    python3 scripts/suno/measure-boxes.py docs/stories/gitpush-origin-master/songs/narration-v6.md
"""
import re
import sys

STYLE_CAP = 1000
POSITIONAL = ["style", "exclude", "lyrics"]
# A box fence is bare or carries a box name. Anything else — bash, ts, python, the retired
# ```taste block — is not a box and must not be counted as one.
BOX_LABELS = ("", "style", "exclude", "excludes", "lyrics")


def name_from_heading(head: str) -> str:
    """Name a lone fence from the heading above it. '?' when the heading does not say."""
    h = head.lower()
    for word, box in (("taste", "taste"), ("exclude", "exclude"), ("lyric", "lyrics"), ("style", "style")):
        if word in h:
            return box
    return "?"


def measure(path: str) -> int:
    src = open(path, encoding="utf-8").read()
    parts = re.split(r"\n(### .*)\n", src)
    problems = 0
    atoms = 0
    for i in range(1, len(parts), 2):
        head, body = parts[i], parts[i + 1]
        name = (head.strip().split("`")[1] if "`" in head else head.strip("# ").strip())[:28]
        fences = re.findall(r"\n```([a-z]*)\n(.*?)\n```\n", body, re.S)
        boxes = [(lab, txt) for lab, txt in fences if lab in BOX_LABELS]
        if not fences:
            print(f"{name:28s} —        prose section, no fences")
            continue
        if not boxes:
            kinds = ", ".join(sorted({lab or 'bare' for lab, _ in fences}))
            print(f"{name:28s} —        SKIPPED: fences are ```{kinds}, not boxes")
            continue
        is_atom = 2 <= len(boxes) <= 3
        if is_atom:
            atoms += 1
        elif len(boxes) > 3:
            print(f"{name:28s} 🔴 {len(boxes)} boxes — `extract` reads only the first three "
                  f"and will mis-assign them")
            problems += 1
        for j, (label, text) in enumerate(boxes):
            if label:
                box = label
            elif is_atom and j < 3:
                box = POSITIONAL[j]          # in an atom, order IS the identity
            else:
                box = name_from_heading(head)  # a lone fence: ask the heading
            if box == "excludes":
                box = "exclude"
            over = box == "style" and len(text) > STYLE_CAP
            problems += over
            note = f"🔴 OVER {STYLE_CAP}" if over else ("(unidentified fence — no verdict)" if box == "?" else "")
            print(f"{name:28s} {box:8s} {len(text):5d}  {note}")
    if not atoms:
        print(f"🔴 no atoms found in {path} — no '### ' section held 2-3 boxes together. "
              f"`extract` will not find an atom here either: on an older sheet the boxes are under "
              f"one heading each, and they have to be pasted by hand or the sheet restructured.")
        problems += 1
    print(f"\n{atoms} atom(s) measured, {problems} problem(s).")
    return problems


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    sys.exit(1 if measure(sys.argv[1]) else 0)
