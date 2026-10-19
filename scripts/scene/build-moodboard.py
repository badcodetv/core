#!/usr/bin/env python3
"""Build a scene's mood board: one self-contained HTML page, a section per beat, a card per still,
This / Maybe / No votes and a note per beat shared through the artifact db (collections `votes`,
`notes`). Publish with capabilities {db:{}, user:{}}.

    python3 scripts/scene/build-moodboard.py <scene-dir> <out.html>

Reads scene.json (title, heading, moodboard_intro, beats, existing, styles) and moodboard.json
(rows [beat, id, look, prompt, style?]). Each still is <media>/moodboard/<id>.jpg; a row whose image
is missing shows as "not generated" (blocked or failed), so the record stays honest. Images are
shrunk to 760px and inlined, because the page may not fetch.
"""
import html
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from scene import Scene, data_uri  # noqa: E402

HERE = pathlib.Path(__file__).parent


def main(scene_dir, out):
    sc = Scene(scene_dir)
    cfg = sc.cfg
    beats = cfg['beats']
    cards = {b['key']: [] for b in beats}
    for key, items in cfg.get('existing', {}).items():
        for iid, look, rel in items:
            p = sc.media / rel
            if p.exists() and key in cards:
                cards[key].append((iid, look, '', data_uri(p, 760), True, 'original'))
    for row in sc.load('moodboard.json', []):
        key, iid, look, prompt = row[:4]
        if key not in cards:
            continue  # a beat cut from the scene stays in the record, off the board
        style = row[4] if len(row) > 4 else 'original'
        p = sc.still(iid)
        cards[key].append((iid, look, prompt, data_uri(p, 760) if p else None, False, style))
    sections = []
    for b in beats:
        key = b['key']
        figs = []
        for iid, look, prompt, uri, made, style in cards[key]:
            img = (f'<img src="{uri}" alt="{html.escape(look)}" loading="lazy">' if uri
                   else '<div class="missing">Not generated (blocked or failed)</div>')
            figs.append(f'''<figure class="card{' made' if made else ''}" data-id="{iid}" data-scene="{key}" data-style="{style}">
  <button class="frame" type="button" aria-label="Open {html.escape(look)} large">{img}</button>
  <figcaption><span class="look">{html.escape(look)}</span><span class="iid">{iid}</span></figcaption>
  <div class="vote" role="group" aria-label="Your verdict on {iid}">
    <button type="button" data-v="yes" id="v-{iid}-yes">This</button><button type="button" data-v="maybe" id="v-{iid}-maybe">Maybe</button><button type="button" data-v="no" id="v-{iid}-no">No</button>
  </div>
  <div class="tally" aria-live="polite"></div>
  {f'<details><summary>Prompt</summary><p>{html.escape(prompt)}</p></details>' if prompt else ''}
</figure>''')
        sections.append(f'''<section class="scene" id="{key}">
  <header><span class="beat">{html.escape(b.get('at', ''))}</span><h2>{html.escape(b['name'])}</h2><p>{html.escape(b.get('blurb', ''))}</p></header>
  <div class="grid">{''.join(figs)}</div>
  <label class="note" for="note-{key}">Note on this beat's look</label>
  <textarea id="note-{key}" data-scene="{key}" rows="2" placeholder="e.g. B4's scale with B3's warmth"></textarea>
  <div class="saved" data-for="{key}"></div>
</section>''')
    styles = cfg.get('styles', {})
    tpl = (HERE / 'moodboard-template.html').read_text()
    page = (tpl.replace('<!--TITLE-->', html.escape(cfg['title'] + ' mood board'))
            .replace('<!--HEADING-->', cfg.get('heading', html.escape(cfg['title'])))
            .replace('<!--INTRO-->', cfg.get('moodboard_intro', ''))
            .replace('<!--FILTERS-->', ''.join(f'<button type="button" data-f="{k}" aria-pressed="false">{html.escape(v)}</button>' for k, v in styles.items()))
            .replace('<!--NAV-->', ''.join(f'<a href="#{b["key"]}">{html.escape(b.get("at", ""))} · {html.escape(b["name"])}</a>' for b in beats))
            .replace('<!--SECTIONS-->', '\n'.join(sections)))
    pathlib.Path(out).write_text(page)
    n = sum(len(v) for v in cards.values())
    print(f'{out}: {len(beats)} beats, {n} cards, {len(page) / 1e6:.1f} MB')


if __name__ == '__main__':
    main(*sys.argv[1:3])
