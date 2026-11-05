import pathlib, sys
HERE = pathlib.Path(__file__).parent; sys.path.insert(0, str(HERE))
from shots import STILLS, GANG
spec = __import__("importlib.util").util
s7 = spec.spec_from_file_location("mb7", HERE.parent / "r7" / "make_briefs.py")
src7 = (HERE.parent / "r7" / "make_briefs.py").read_text()
FACTS = src7.split('FACTS = """')[1].split('"""')[0]; RULES = src7.split('RULES = """')[1].split('"""')[0]; JOB = eval(src7.split("JOB = (")[1].split(")\nfor w")[0].join(["(", ")"]))
jack = (HERE / "jack.md").read_text(); r8 = (HERE / "research.md").read_text()
r6 = (HERE.parent / "r6" / "research.md").read_text(); look = r6[r6.index("## 3."):r6.index("## 4.")]
for w, shots in STILLS.items():
    lines = [f"# Your {len(shots)} shots: closer, cleaner versions of shots the director rejected\n"]
    for sid, t, line, what in shots: lines.append(f"## {sid}: {t} in the song, the line \"{line}\"\n{what}\n")
    txt = "\n\n".join([JOB, jack, FACTS, "- New this round: the masks went wrong whenever a masked head was small in frame or turned away. In every shot each visible mask must be LARGE (a head at least a fifth of the frame height) and face-on or three-quarter to the camera.", GANG, "\n".join(lines), "# Web research (this round)\n\n" + r8, "# Web research: the film-still look\n\n" + look, RULES.format(out=HERE / f"{w}.md")])
    (HERE / f"brief-{w}.md").write_text(txt); print(w, len(txt.split()))
