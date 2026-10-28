#!/usr/bin/env python3
"""Build a story-style round's picking page: the story in a few lines, a card per look (its test
still), a card per sound (its references, and a preview if one was recorded), This / Maybe / No on
every card and a note on looks, on sounds and on how the two belong together. Votes and notes go
to the artifact db (collections `votes`, `notes`), like the mood board. Publish with
capabilities {db:{}, user:{}} and republish to the same file path each round.

    python3 scripts/story-style/build-page.py <story-dir>/style/round-<n> <out.html>

Reads <round>/options.json:
  {"title", "intro", "story": [[label, text], ...],
   "looks":  [{"id", "name", "family", "from": [library slugs] | [], "pitch", "why", "risk",
               "image": path, "prompt"}],
   "sounds": [{"id", "name", "family", "from", "pitch", "why", "risk",
               "references": [{"title", "maker", "url"?}], "audio"?: path, "style_box"?}]}
A look whose image is missing shows "not generated" (blocked or failed), so the record stays honest.
"""
import base64
import html
import json
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "scene"))
from scene import data_uri  # noqa: E402

HERE = pathlib.Path(__file__).parent
e = html.escape


def lib_line(o):
    if not o.get("from"):
        return '<span class="fam">off the library</span>'
    return f'<span class="fam">{e(o.get("family", ""))} · {e(", ".join(o["from"]))}</span>'


def vote(iid):
    return f'''<div class="vote" role="group" aria-label="Your verdict on {iid}">
    <button type="button" data-v="yes">This</button><button type="button" data-v="maybe">Maybe</button><button type="button" data-v="no">No</button>
  </div><div class="tally" aria-live="polite"></div>'''


def note(key, label, hint):
    return f'''<label class="note" for="note-{key}">{label}</label>
<textarea id="note-{key}" data-scene="{key}" rows="2" placeholder="{e(hint)}"></textarea>
<div class="saved" data-for="{key}"></div>'''


def look_card(o):
    p = pathlib.Path(o["image"]) if o.get("image") else None
    img = (f'<img src="{data_uri(p, 900)}" alt="{e(o["name"])}" loading="lazy">' if p and p.exists()
           else '<div class="missing">Not generated (blocked or failed)</div>')
    return f'''<figure class="card" data-id="{o['id']}">
  <button class="frame" type="button" aria-label="Open {e(o['name'])} large">{img}</button>
  <div class="head"><span class="name">{e(o['name'])}</span><span class="iid">{o['id']}</span></div>
  {lib_line(o)}
  <p>{e(o['pitch'])}</p><p class="why"><b>For this story:</b> {e(o['why'])}</p><p class="risk"><b>Risk:</b> {e(o['risk'])}</p>
  {vote(o['id'])}
  {f'<details><summary>Test-still prompt</summary><p>{e(o["prompt"])}</p></details>' if o.get('prompt') else ''}
</figure>'''


def ref(r):
    title = f'<i>{e(r["title"])}</i>'
    if r.get("url"):
        title = f'<a href="{e(r["url"])}" target="_blank" rel="noopener">{title}</a>'
    return f'<li>{title} — {e(r["maker"])}</li>'


def sound_card(o):
    refs = "".join(ref(r) for r in o.get("references", []))
    audio = ""
    a = pathlib.Path(o["audio"]) if o.get("audio") else None
    if a and a.exists():
        audio = f'<audio controls preload="none" src="data:audio/mpeg;base64,{base64.b64encode(a.read_bytes()).decode()}"></audio>'
    return f'''<figure class="card" data-id="{o['id']}">
  <div class="head"><span class="name">{e(o['name'])}</span><span class="iid">{o['id']}</span></div>
  {lib_line(o)}
  <p>{e(o['pitch'])}</p><p class="why"><b>For this story:</b> {e(o['why'])}</p><p class="risk"><b>Risk:</b> {e(o['risk'])}</p>
  {audio}{f'<ul>{refs}</ul>' if refs else ''}
  {vote(o['id'])}
  {f'<details><summary>Suno Style box sketch</summary><p>{e(o["style_box"])}</p></details>' if o.get('style_box') else ''}
</figure>'''


def main(rnd, out):
    rnd = pathlib.Path(rnd)
    cfg = json.loads((rnd / "options.json").read_text())
    story = "".join(f"<dt>{e(k)}</dt><dd>{e(v)}</dd>" for k, v in cfg.get("story", []))
    sections = [
        f'<section id="story"><h2>The story</h2><p class="sub">What the interview settled. Every option below is judged against this.</p><dl class="story">{story}</dl></section>',
        f'''<section id="looks"><h2>Looks</h2><p class="sub">One test still per look, all of the same moment: {e(cfg.get("subject", ""))}</p>
<div class="grid">{"".join(look_card(o) for o in cfg.get("looks", []))}</div>
{note("looks", "Note on the looks", "e.g. L3's light with L5's palette")}</section>''',
        f'''<section id="sounds"><h2>Sounds</h2><p class="sub">Words and references, not takes: listen to the references. Suno tests come after a pick.</p>
<div class="grid">{"".join(sound_card(o) for o in cfg.get("sounds", []))}</div>
{note("sounds", "Note on the sounds", "e.g. S2, but sung by a choir")}</section>''',
        f'''<section id="pair"><h2>Together</h2><p class="sub">A look and a sound have to be one world. Which pairs, and what must they share?</p>
{note("pair", "Note on the pairing", "e.g. L2 + S4: both hand-made, both a bit wrong")}</section>''',
    ]
    page = ((HERE / "page-template.html").read_text()
            .replace("<!--TITLE-->", e(cfg["title"]))
            .replace("<!--HEADING-->", e(cfg["title"]))
            .replace("<!--INTRO-->", e(cfg.get("intro", "")))
            .replace("<!--SECTIONS-->", "\n".join(sections)))
    pathlib.Path(out).write_text(page)
    print(f"{out}: {len(cfg.get('looks', []))} looks, {len(cfg.get('sounds', []))} sounds, {len(page) / 1e6:.1f} MB")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    main(*sys.argv[1:3])
