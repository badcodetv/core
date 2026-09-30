"""Check every GPOM narration scene's Style and Exclude boxes against the house template.

The live sheet (narration.md) carries one template fence with four {{BLANKS}}, the two allowed
endings, and one house Exclude box. Each scene atom (a level-3 heading naming the atom in
backticks, followed by Style / Exclude / Lyrics fences) must be that template with the blanks
filled, and that exact Exclude box. Anything else is drift: this prints the sentences that differ,
so a change is deliberate rather than accidental. An atom whose heading carries a lock emoji is
frozen (picked before the template existed) and is reported but never fails the check.

Usage:
    python3 scripts/suno/narration-drift.py [sheet.md]
"""
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
SHEET = REPO / "docs/stories/gitpush-origin-master/songs/narration.md"
FENCE = re.compile(r"^```([a-z]*)\n(.*?)\n```$", re.S | re.M)
BLANK = re.compile(r"\\\{\\\{[A-Z]+\\\}\\\}")


def sentences(text):
    return [s.strip() for s in re.split(r"(?<=[.!?])\s+", text.strip()) if s.strip()]


def compare(style, template):
    """Sentences the template has that the style lacks, and sentences the style adds."""
    pats = [re.compile("^" + BLANK.sub(".+?", re.escape(t)) + "$") for t in sentences(template)]
    have = sentences(style)
    missing = [t for t, p in zip(sentences(template), pats) if not any(p.match(s) for s in have)]
    extra = [s for s in have if not any(p.match(s) for p in pats)]
    return missing, extra


def main(path):
    src = path.read_text()
    template = next(body for label, body in FENCE.findall(src) if label == "template")
    house = src[src.index("## House style"):]
    house = house[: house.index("\n## ", 1)]
    house_exclude = next(body for label, body in FENCE.findall(house) if label == "")
    endings = dict(re.findall(r"- \*\*(\w+):\*\* `([^`]+)`", house))
    candidates = {name: template.replace("{{ENDING}}", text) for name, text in endings.items()}

    drift = 0
    for atom in re.split(r"\n(?=### `)", src)[1:]:
        head = atom.split("\n", 1)[0]
        name = head.split("`")[1]
        body = re.split(r"\n#{2,3} ", atom)[0]
        boxes = [b for label, b in FENCE.findall(body) if label in ("", "lyrics")]
        if len(boxes) < 2:
            continue
        style, exclude = boxes[0], boxes[1]
        frozen = "🔒" in head
        tag = "  (🔒 frozen — reported, not failed)" if frozen else ""
        # Judge against whichever ending fits best.
        ending, (missing, extra) = min(
            ((n, compare(style, t)) for n, t in candidates.items()),
            key=lambda r: len(r[1][0]) + len(r[1][1]),
        )
        if not missing and not extra:
            print(f"✅ {name}: Style matches the template (ending: {ending})")
        else:
            drift += 0 if frozen else 1
            print(f"⚠️  {name}: Style drifts from the template{tag}")
            for t in missing:
                print(f"      missing: {t}")
            for s in extra:
                print(f"      extra:   {s}")
        if exclude.strip() == house_exclude.strip():
            print(f"✅ {name}: Exclude matches the house box")
        else:
            drift += 0 if frozen else 1
            print(f"⚠️  {name}: Exclude differs from the house box{tag}")
    return 1 if drift else 0


if __name__ == "__main__":
    sys.exit(main(Path(sys.argv[1]) if len(sys.argv) > 1 else SHEET))
