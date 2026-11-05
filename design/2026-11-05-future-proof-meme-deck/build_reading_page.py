#!/usr/bin/env python3
"""Build the Future Proof deck reading page from deck-v2.md.

Usage: python3 build_reading_page.py [deck.md] [out.html]
Parses every slide (main deck + appendix) and the deck's notes sections into JSON,
then injects it into deck-reading.template.html. Re-run whenever the deck changes,
then republish deck-reading.html to the same artifact URL.
"""
import json, re, sys
from pathlib import Path

HERE = Path(__file__).parent
src = Path(sys.argv[1]) if len(sys.argv) > 1 else HERE / "deck-v2.md"
out = Path(sys.argv[2]) if len(sys.argv) > 2 else HERE / "deck-reading.html"
lines = src.read_text().splitlines()

SLIDE = re.compile(r"^### (A?\d+) · ([a-z]+(?: \(three\.js\))?) · (.+)$")
FIELD = re.compile(r"^- \*\*([A-Za-z /-]+):\*\* ?(.*)$")
H2 = re.compile(r"^## (\d+)\. (.+)$")

sections, slides, notes = [], [], {}
part, cur, cur_field, h2 = None, None, None, None
for raw in lines:
    line = raw.rstrip()
    m = H2.match(line)
    if m:
        h2 = int(m.group(1)); cur = None
        if h2 not in (3, 4):
            notes[h2] = {"title": m.group(2), "md": []}
        if h2 == 4:
            part = {"id": "appendix", "title": "Appendix: backup slides and Q&A", "note": "", "appendix": True}
            sections.append(part)
        continue
    if h2 not in (3, 4):
        if h2 in notes:
            notes[h2]["md"].append(line)
        continue
    m = SLIDE.match(line)
    if m:
        sid, typ, third = m.groups()
        appendix = sid.startswith("A")
        secs = 0 if appendix else int(re.match(r"(\d+)", third).group(1))
        cur = {"id": sid, "type": typ.replace(" (three.js)", ""), "secs": secs,
               "title": third.strip('"') if appendix else "", "part": part["id"], "fields": {}}
        slides.append(cur); cur_field = None
        continue
    if line.startswith("### ") and h2 == 3:
        title = line[4:].strip()
        if title.isupper():  # deck uses ALL CAPS part names; show them in sentence case
            title = re.sub(r"(^|: )([a-z])", lambda m: m.group(1) + m.group(2).upper(), title.lower())
        part = {"id": f"p{len(sections)}", "title": title, "note": "", "appendix": False}
        sections.append(part); cur = None
        continue
    if cur:
        m = FIELD.match(line)
        if m:
            cur_field = m.group(1)
            cur["fields"][cur_field] = m.group(2)
        elif line.strip() and cur_field and not line.startswith("---"):
            cur["fields"][cur_field] += " " + line.strip()
    elif part and line.strip() and not line.startswith("---") and not line.startswith("Not in the ten") and not line.startswith("Format per slide"):
        part["note"] += (" " if part["note"] else "") + line.strip()

t = 0
for s in slides:
    if s["secs"]:
        s["at"] = t; t += s["secs"]
data = {
    "slides": slides, "sections": sections, "runtime": t,
    "notes": [{"n": k, "title": v["title"], "md": "\n".join(v["md"]).strip()} for k, v in sorted(notes.items())],
}
main = [s for s in slides if s["secs"]]
print(f"{len(main)} main slides, {len(slides) - len(main)} appendix, runtime {t//60}:{t%60:02d}")
tpl = (HERE / "deck-reading.template.html").read_text()
out.write_text(tpl.replace("/*__DATA__*/null", json.dumps(data, ensure_ascii=False).replace("</", "<\\/")))
print("wrote", out)
