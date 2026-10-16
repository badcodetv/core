#!/usr/bin/env python3
"""Build the GPOM second-half mood board (one self-contained HTML page).

Usage: python3 scripts/gpom/build-moodboard.py <prompts.json> <clips-root> <out.html>
prompts.json rows: [scene, id, look, prompt, style?] (style: original | threads | noir | ...). Each new image is found at
<clips-root>/second-half/moodboard/<id>.jpg; EXISTING lists stills already made.
Images are shrunk to 760px JPEGs and inlined as data URIs (the page may not fetch).
"""
import base64, html, io, json, os, sys
from PIL import Image

SCENES = [
    ("povroam", "C", "The kill bots on patrol", "Meanwhile, near Swindon. The bot trundles off; the kill bots roam, seen through their own eyes like Predator: grainy CCTV under an AI HUD."),
    ("signal", "C", "Organic signal detected", "Ping, ping, ping. A muffled sound reaches them as a waveform. We don't hear the words."),
    ("argument", "C2", "The row", "Cut underground: the toilet-seat argument at full volume. The joke is the jump from muffled waveform to full row."),
    ("bunker", "C2", "The bunker", "A Cold War government bunker like the one under Corsham. A hundred people have lived here for five years."),
    ("killmode", "D", "Kill mode", "Back to their eyes. They activate and race off, past the bot we just saw."),
    ("killbots", "D", "More kill-bot looks", "First-round looks for the machines on the move, from the CCTV and the bot's height."),
    ("destruct", "E", "The self-destruct", "The AI orders them to stop. They refuse. It blows them up just in time."),
    ("meeting", "F", "The meeting", "The humans come out to the bot. The AI speaks through its speaker. An old lady is not impressed."),
    ("machine", "I", "The time machine: the clean room", "Not in the bunker. A high-tech building the AI made: clean room, lab, chip-fab light. They walk out of the mud into it, and the contrast is the point. It runs on consciousness and can only send the AI. All hundred power it."),
    ("ending", "J", "The ending", "Zoom out of a screen, over the shoulder of someone watching this film. \u201cI made it. Don\u2019t make me come back twice.\u201d"),
]
EXISTING = {}  # scene -> [(id, look, path relative to clips root)]; the drain grates left with the drain (16 Oct)

def data_uri(path):
    im = Image.open(path).convert("RGB")
    im.thumbnail((760, 760))
    buf = io.BytesIO(); im.save(buf, "JPEG", quality=74, optimize=True)
    return "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode()

def main(prompts_path, root, out):
    rows = json.load(open(prompts_path))
    cards = {s[0]: [] for s in SCENES}
    for scene, items in EXISTING.items():
        for iid, look, rel in items:
            p = os.path.join(root, rel)
            if os.path.exists(p): cards[scene].append((iid, look, "", data_uri(p), True, "original"))
    for row in rows:
        scene, iid, look, prompt = row[:4]
        if scene not in cards: continue  # a scene cut from the film (the drain) stays in the record, off the board
        style = row[4] if len(row) > 4 else "original"
        p = os.path.join(root, "second-half/moodboard", iid + ".jpg")
        cards[scene].append((iid, look, prompt, data_uri(p) if os.path.exists(p) else None, False, style))
    for key in cards:  # keep each original next to its style variants
        order = {}
        for c in cards[key]: order.setdefault(c[0].split("-")[0] if not c[4] else c[0], len(order))
        cards[key].sort(key=lambda c: order.get(c[0].split("-")[0] if not c[4] else c[0], 0))
    sections = []
    for key, beat, name, blurb in SCENES:
        figs = []
        for iid, look, prompt, uri, made, style in cards[key]:
            img = f'<img src="{uri}" alt="{html.escape(look)}" loading="lazy">' if uri else '<div class="missing">Not generated (blocked or failed)</div>'
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
  <header><span class="beat">Beat {beat}</span><h2>{html.escape(name)}</h2><p>{html.escape(blurb)}</p></header>
  <div class="grid">{''.join(figs)}</div>
  <label class="note" for="note-{key}">Note on this scene's look</label>
  <textarea id="note-{key}" data-scene="{key}" rows="2" placeholder="e.g. B4's scale with B3's warmth"></textarea>
  <div class="saved" data-for="{key}"></div>
</section>''')
    tpl = open(os.path.join(os.path.dirname(__file__), "moodboard-template.html")).read()
    open(out, "w").write(tpl.replace("<!--SECTIONS-->", "\n".join(sections)).replace("<!--NAV-->", "".join(f'<a href="#{k}">{b} · {html.escape(n)}</a>' for k, b, n, _ in SCENES)))

if __name__ == "__main__":
    main(*sys.argv[1:4])
