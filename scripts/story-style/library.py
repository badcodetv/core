#!/usr/bin/env python3
"""The style library: a menu of looks and sounds that ONLY the story-style interview reads.

There is no house style (docs/stories/STYLE.md). The library is how a new story finds its own:
a wide, honest menu, one file per style, each saying what it is good for AND what it would
undermine. It is not a default and nothing else reads it (scripts/style-lint.py checks).

    python3 scripts/story-style/library.py build <research.json>   write docs/style-library/{look,sound}/*.md
    python3 scripts/story-style/library.py index                    rebuild docs/style-library/README.md
    python3 scripts/story-style/library.py apply-check <check.json>  fold a web check into the entries

research.json is a list of families: {kind: visual|music, family, family_note, styles:[...], left_out}
(the 2026-10-28 research workflow's output). `index` also reads every docs/stories/*/look.md and
sound.md for a line starting "**Library:**" and lists which stories already drew on each style, so
the interview can avoid handing two stories the same look.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
LIB = ROOT / "docs" / "style-library"
KIND_DIR = {"visual": "look", "music": "sound"}


def slugify(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")


def entry_md(kind, fam, s):
    refs = "\n".join(
        f"- *{r['title']}* — {r['maker']}{', ' + r['year'] if r.get('year') else ''}. {r['why']}"
        for r in s["references"])
    traits = "\n".join(f"- {t}" for t in s["signature_traits"])
    srcs = "\n".join(f"- <{u}>" for u in s.get("sources", []))
    engine = "Flow (Nano Banana stills, Veo clips)" if kind == "visual" else "Suno"
    return f"""---
slug: {s['slug']}
name: {s['name']}
kind: {KIND_DIR[kind]}
family: {fam}
checked: {s.get('checked', 'no — written from model knowledge 2026-10-28, not yet checked on the web')}
---

# {s['name']}

> {s['one_line']}
>
> Library entry: read only by the `story-style` interview. A story that picks this copies what it
> needs into its own look.md / sound.md; it never links here as its style.

{s['what_it_is']}

## Signature traits

{traits}

## References

{refs}

## What it carries

{s['feels_like']}

## What it suits, and what it would undermine

{s['suits']}

## Asking {engine} for it

{s['engine_prompting']}

## How generators get it wrong

{s['ai_failure_modes']}

## Production cost

{s['production_cost']}
{f'''
## Sources

{srcs}
''' if srcs else ''}"""


def build(path):
    fams = json.loads(Path(path).read_text())
    n = 0
    seen = set()
    for fam in fams:
        kd = KIND_DIR[fam["kind"]]
        fdir = LIB / kd
        fdir.mkdir(parents=True, exist_ok=True)
        for s in fam["styles"]:
            s["slug"] = slugify(s["slug"] or s["name"])
            if (kd, s["slug"]) in seen:
                s["slug"] += "-" + slugify(fam["family"]).split("-")[0]
            seen.add((kd, s["slug"]))
            (fdir / f"{s['slug']}.md").write_text(entry_md(fam["kind"], fam["family"], s))
            n += 1
    (LIB / "families.json").write_text(json.dumps(
        [{"kind": KIND_DIR[f["kind"]], "family": f["family"], "note": f["family_note"],
          "styles": [s["slug"] for s in f["styles"]], "left_out": f.get("left_out", [])} for f in fams],
        indent=2, ensure_ascii=False) + "\n")
    print(f"{n} entries written under {LIB.relative_to(ROOT)}/")
    index()


def used_by():
    used = {}
    for f in sorted((ROOT / "docs" / "stories").glob("*/*.md")):
        if f.name not in ("look.md", "sound.md"):
            continue
        for line in f.read_text().splitlines():
            if line.startswith("**Library:**"):
                for slug in re.findall(r"`([a-z0-9-]+)`", line):
                    used.setdefault((f.stem, slug), []).append(f.parent.name)
    return used


def front(p):
    m = re.search(r"^name: (.+)$", p.read_text(), re.M)
    one = re.search(r"^> (.+)$", p.read_text(), re.M)
    return (m.group(1) if m else p.stem), (one.group(1) if one else "")


def index():
    fams = json.loads((LIB / "families.json").read_text())
    used = used_by()
    out = [HEADER]
    for kd, title in (("look", "Looks"), ("sound", "Sounds")):
        out.append(f"\n## {title}\n")
        for fam in (f for f in fams if f["kind"] == kd):
            out.append(f"\n### {fam['family']}\n\n{fam['note']}\n")
            out.append("| Style | In one line | Used by |\n| --- | --- | --- |")
            for slug in fam["styles"]:
                p = LIB / kd / f"{slug}.md"
                if not p.exists():
                    continue
                name, one = front(p)
                u = ", ".join(used.get((kd, slug), [])) or "—"
                out.append(f"| [{name}](./{kd}/{slug}.md) `{slug}` | {one} | {u} |")
            if fam.get("left_out"):
                out.append(f"\n*Not yet written up:* {'; '.join(fam['left_out'])}.")
    (LIB / "README.md").write_text("\n".join(out) + "\n")
    print(f"index: {LIB.relative_to(ROOT)}/README.md")


def apply_check(path, date="2026-10-28"):
    """check.json: [{kind, styles:[{slug, references:[{title, verdict, correction?, source?}],
    engine_ok, engine_fix?, sources?}]}]. False references are removed, corrected and doubtful ones
    are marked, and a "Web check" section records the engine verdict and the sources."""
    counts = {}
    for fam in json.loads(Path(path).read_text()):
        kd = KIND_DIR.get(fam.get("kind"), fam.get("kind"))
        for s in fam["styles"]:
            f = LIB / kd / f"{slugify(s['slug'])}.md"
            if not f.exists():
                print(f"  no entry for {kd}/{s['slug']}")
                continue
            text = f.read_text()
            notes = []
            for r in s["references"]:
                v = r["verdict"]
                counts[v] = counts.get(v, 0) + 1
                lines = text.splitlines()
                i = next((n for n, l in enumerate(lines) if l.startswith(f"- *{r['title']}*")), None)
                if v == "false" and i is not None:
                    notes.append(f"- Removed *{r['title']}*: {r.get('correction', 'could not be confirmed to exist')}")
                    del lines[i]
                elif v in ("corrected", "doubtful") and i is not None:
                    mark = f" **(Corrected: {r.get('correction', '')})**" if v == "corrected" else " **(Unconfirmed on the web.)**"
                    lines[i] += mark
                text = "\n".join(lines) + "\n"
            eng = {"supported": "supported by what the checker found",
                   "plausible-untested": "plausible, not documented anywhere the checker found: treat as a first guess to test",
                   "contradicted": "contradicted by what the checker found"}[s["engine_ok"]]
            counts["engine-" + s["engine_ok"]] = counts.get("engine-" + s["engine_ok"], 0) + 1
            fix = f"\n\n**Correction:** {s['engine_fix']}" if s.get("engine_fix") else ""
            srcs = "".join(f"\n- <{u}>" for u in s.get("sources", []) + [r["source"] for r in s["references"] if r.get("source")])
            text = text.rstrip() + f"\n\n## Web check ({date})\n\nEngine notes: {eng}.{fix}\n" + ("\n".join([""] + notes) + "\n" if notes else "") + (f"\nSources:{srcs}\n" if srcs else "")
            text = re.sub(r"^checked: .*$", f"checked: {date}, references and engine notes (see Web check)", text, count=1, flags=re.M)
            f.write_text(text)
    print("checked:", ", ".join(f"{k} {v}" for k, v in sorted(counts.items())))


HEADER = """# The style library

> **Read only by the `story-style` interview** (Kai, 2026-10-28). Not a house style, not a
> default, not a shortlist. It is a wide menu so a new story can find a look and a sound of its
> own. No other skill, CLAUDE.md or memory may point here: `scripts/style-lint.py` fails if one does.

**How it is used.** The interview starts from the story (what it argues, who it is for, how the end
should feel), and only then opens this index. It proposes options from **at least three different
families**, **at least one off the library** (invented for this story), and avoids a style another
story already uses (the *Used by* column) unless asked. The picked style is **copied** into the
story's `look.md` / `sound.md` (the parts it needs, adapted) and named on its `**Library:**` line.
Editing an entry here never changes a story that has already picked it.

**Where it came from.** 20 research agents, 2026-10-28, one per family (10 visual, 10 music), each
told to say what a style undermines as well as what it serves. They wrote from model knowledge; a
second pass of 20 agents then checked every entry on the web (67 searches): 627 references
confirmed, 48 corrected, 23 unconfirmed (marked in place), none found to be invented outright. Engine
notes are mostly **untested first guesses** (136 of 159), 7 documented, 16 corrected; each entry's
*Web check* section says which. Recurring engine fact: **Flow has one prompt box and no exclude
field**, so what a style must avoid is written into the prompt as what it should be instead. Rebuild this index with
`python3 scripts/story-style/library.py index`. Add an entry by writing a file in `look/` or
`sound/` with the same sections, and its slug to `families.json`.
"""

if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else ""
    if cmd == "build":
        build(sys.argv[2])
    elif cmd == "apply-check":
        apply_check(sys.argv[2])
    elif cmd == "index":
        index()
    else:
        sys.exit(__doc__)
