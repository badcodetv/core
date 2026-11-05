#!/usr/bin/env python3
"""Build a BadCode slideshow preview (and its reading page) from a deck folder.

    python3 scripts/slideshow/build.py docs/stories/<story>/slideshows/<deck>/

A deck folder holds:
  deck.md       the script: every slide's On-screen / Visual / Say / Source (source of truth for words)
  slides.json   how each slide is drawn in this deck's look: {"title":..., "round":N, "slides":[{id, layout, ...}]}
  theme/        the deck's own look: head.html (fonts), theme.css, layouts.js, scenes/*.js, LAYOUTS.md
  images/       picture manifest + recipe cards (the media itself lives on D:, see docs/provenance)
Writes preview.html (the slideshow) and reading.html (the script page) into the deck folder.
There is no house theme: a deck without a theme/ folder fails on purpose.
"""
import json, re, sys
from pathlib import Path

ENGINE = Path(__file__).parent / "engine.template.html"
READING = Path(__file__).parent / "reading.template.html"
SLIDE = re.compile(r"^### (A?\d+) · (?:([a-z]+(?: \(three\.js\))?) · )?(.+)$")  # appendix may omit the type
FIELD = re.compile(r"^- \*\*([A-Za-z /-]+):\*\* ?(.*)$")
H2 = re.compile(r"^## (\d+)\. (.+)$")


def parse_deck(md: str):
    sections, slides, notes = [], [], {}
    part = cur = cur_field = h2 = None
    for raw in md.splitlines():
        line = raw.rstrip()
        m = H2.match(line)
        if m:
            h2 = int(m.group(1)); cur = None
            if h2 not in (3, 4):
                notes[h2] = {"title": m.group(2), "md": []}
            if h2 == 4:
                part = {"id": "appendix", "title": "Appendix: backup slides and Q&A", "note": ""}
                sections.append(part)
            continue
        if h2 not in (3, 4):
            if h2 in notes:
                notes[h2]["md"].append(line)
            continue
        m = SLIDE.match(line)
        if m:
            sid, typ, third = m.groups()
            appx = sid.startswith("A")
            secs = 0 if appx else int(re.match(r"(\d+)", third).group(1))
            cur = {"id": sid, "type": (typ or "meme").replace(" (three.js)", ""), "secs": secs,
                   "title": third.strip('"') if appx else "", "part": part["id"], "fields": {}}
            slides.append(cur); cur_field = None
            continue
        if line.startswith("### ") and h2 == 3:
            title = line[4:].strip()
            if title.isupper():
                title = re.sub(r"(^|: )([a-z])", lambda m: m.group(1) + m.group(2).upper(), title.lower())
            part = {"id": f"p{len(sections)}", "title": title, "note": ""}
            sections.append(part); cur = None
            continue
        if cur:
            m = FIELD.match(line)
            if m:
                cur_field = m.group(1); cur["fields"][cur_field] = m.group(2)
            elif line.strip() and cur_field and not line.startswith("---"):
                cur["fields"][cur_field] += " " + line.strip()
        elif part and line.strip() and not line.startswith("---") and not line.startswith(("Not in the ten", "Format per slide")):
            part["note"] += (" " if part["note"] else "") + line.strip()
    t = 0
    for s in slides:
        if s["secs"]:
            s["at"] = t; t += s["secs"]
    notes = [{"n": k, "title": v["title"], "md": "\n".join(v["md"]).strip()} for k, v in sorted(notes.items())]
    return {"slides": slides, "sections": sections, "runtime": t, "notes": notes}


def inject(tpl: str, **parts) -> str:
    for k, v in parts.items():
        tail = {"DATA": "null", "PUBLIC": "false"}.get(k, "")
        tpl = tpl.replace(f"/*__{k}__*/{tail}", v)
    return tpl


def main(folder: Path, public_out: Path | None = None, home: str = "/"):
    deck = parse_deck((folder / "deck.md").read_text())
    theme = folder / "theme"
    if not theme.is_dir():
        sys.exit(f"{theme} missing: every deck brings its own look (no house theme).")
    layout = json.loads((folder / "slides.json").read_text()) if (folder / "slides.json").exists() else {"slides": []}
    by_id = {s["id"]: s for s in layout["slides"]}
    images = {}
    man = folder / "images" / "manifest.json"
    if man.exists():
        images = json.loads(man.read_text())  # {"mel-booth.jpg": "https://...asset url"}
    out = []
    for s in deck["slides"]:
        f = s["fields"]
        v = {"id": s["id"], "type": s["type"], "secs": s["secs"], "at": s.get("at"), "title": s["title"],
             "say": f.get("Say", ""), "visual": f.get("Visual", ""), "onscreen": f.get("On-screen", ""),
             "layout": "fallback"}
        v.update(by_id.get(s["id"], {}))
        for key in ("image",):
            if isinstance(v.get(key), dict) and v[key].get("file") in images:
                v[key]["src"] = images[v[key]["file"]]
        for side in ("left", "right"):
            img = (v.get(side) or {}).get("image") if isinstance(v.get(side), dict) else None
            if img and img.get("file") in images:
                img["src"] = images[img["file"]]
        out.append(v)
    missing = [s["id"] for s in out if s["layout"] == "fallback"]
    data = {"title": layout.get("title", folder.name), "round": layout.get("round", 1), "slides": out}
    js = "\n".join(p.read_text() for p in sorted((theme / "scenes").glob("_*.js")))
    js += "\n" + (theme / "layouts.js").read_text()
    js += "\n" + "\n".join(p.read_text() for p in sorted((theme / "scenes").glob("[!_]*.js")))
    dump = lambda o: json.dumps(o, ensure_ascii=False).replace("</", "<\\/")
    html = inject(ENGINE.read_text(), PUBLIC="false", HOME="/", TITLE=data["title"], THEME_HEAD=(theme / "head.html").read_text(),
                  THEME_CSS="<style>\n" + (theme / "theme.css").read_text() + "\n</style>",
                  THEME_JS=js.replace("</script", "<\\/script"), DATA=dump(data))
    (folder / "preview.html").write_text(html)
    if public_out:
        # the website copy: no notes, no picture briefs, a link home; a full HTML document
        pub = inject(ENGINE.read_text(), TITLE=data["title"], THEME_HEAD=(theme / "head.html").read_text(),
                     THEME_CSS="<style>\n" + (theme / "theme.css").read_text() + "\n</style>",
                     THEME_JS=js.replace("</script", "<\\/script"), DATA=dump({**data, "slides": [
                         {k: v for k, v in s.items() if k not in ("visual", "note", "notes")} for s in out if s["secs"]]}),
                     PUBLIC="true", HOME=home)
        pub = ('<!doctype html>\n<html lang="en-GB"><head><meta charset="utf-8">'
               '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover"></head><body>\n' + pub + '\n</body></html>\n')
        public_out.parent.mkdir(parents=True, exist_ok=True)
        public_out.write_text(pub)
        print("wrote public copy", public_out)
    if READING.exists():
        (folder / "reading.html").write_text(inject(READING.read_text(), TITLE=data["title"], DATA=dump(deck)))
    main_n = sum(1 for s in out if s["secs"])
    print(f"{main_n} main + {len(out) - main_n} appendix slides, runtime {deck['runtime']//60}:{deck['runtime']%60:02d}")
    print(f"scenes: {sorted({s.get('scene') for s in out if s.get('scene')})}")
    if missing:
        print(f"no layout yet (drawn as fallback): {', '.join(missing)}")
    print("wrote", folder / "preview.html")


if __name__ == "__main__":
    # build.py <deck-folder> [--public <out.html> [--home <url>]]
    a = sys.argv[1:]
    pub = Path(a[a.index("--public") + 1]) if "--public" in a else None
    home = a[a.index("--home") + 1] if "--home" in a else "/"
    main(Path(a[0]), pub, home)
