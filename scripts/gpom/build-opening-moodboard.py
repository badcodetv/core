#!/usr/bin/env python3
"""Build the GPOM opening-recut mood board (one self-contained HTML page).

Usage: python3 scripts/gpom/build-moodboard.py <prompts.json> <clips-root> <out.html>
prompts.json rows: [scene, id, look, prompt, style?] (style: original | threads | noir | ...). Each new image is found at
<clips-root>/opening-recut/moodboard/<id>.jpg; EXISTING lists stills already made.
Images are shrunk to 760px JPEGs and inlined as data URIs (the page may not fetch).
"""
import base64, html, io, json, os, sys
from PIL import Image

SCENES = [
    ("text", "0:46", "After the push: the ownership text", "Enter is hit. Over the server cabinets and the flashing LED, while the crowd chants the developers line, two lines arrive: ACQUIRING RESOURCE LOCK, then NEW OWNERSHIP TRANSFERRED. The push hands the keys to a new master. Mock-ups on the real frames; the real thing is an ffmpeg text layer."),
    ("street", "0:15", "Replaces the near-miss car", "Two hundred thousand office workers made redundant. The shot to beat is the one we keep: workers in the rain, server cabinets wheeled past them. Round 2 (17 Oct, your note): ST1 scrapped; ST2 made messy; one desk, one box made obvious with KEEP-rain's cabinets."),
    ("toast", "0:23", "Replaces the champagne table and the two men at the graph", "The chief executive's hardest email, written by an AI. The win must be visibly paid for by the people in the last section. Round 2 (17 Oct, your note): TO2's look, real unglamorous owners at the table, no headcount graph."),
    ("bread", "0:29", "Replaces the shop queue", "The price of bread is up nine percent. One person, one loaf, no crowd of old men behind her."),
    ("market", "0:34", "Replaces the old stock exchange", "The price of shares in bread is up ninety, and the treasury printed another trillion. Modern money, not a 1920s floor. Round 2 (17 Oct, your note): a modern market, not glitzy and not the 70s."),
    ("choir", "1:02", "The drop: the robot choir", "Replaces the building site. Git push origin master, this code is a fucking disaster, sung by an army-scale choir of robots in crimson hooded cloaks with red eyes. Operatic, War of the Worlds meets the clone army, at the scale of a starship hangar. Round 2 (17 Oct, your note): CH5's well joined to CH6's ship and army; start inside the well, rise out of it, the ship's light is the light; CH7's face moved into the well."),
    ("colossus", "1:06", "The drop: the colossus lights up", "The developers ain't fixing shit, the compiler is stuck on sixteen bit. The big AI machine itself, with the blinding white light of a headline festival rig: beams, blinders, strobe. Round 2 (17 Oct, your note): CO6, the futuristic Sauron eye, much bigger, on a mountain top in dust with ranges round it and the sun setting; the Oracle Project caption is gone. Animation idea: as the words are sung, the red dots round the ring light up one after another, so a dot seems to travel round the ring while the lights themselves stay still."),
]
EXISTING = {"text": [("TX1", "On the CRT, under the command", "opening-recut/moodboard/text/TX1.jpg"), ("TX2", "Terminal lines over the server hall", "opening-recut/moodboard/text/TX2.jpg"), ("TX3", "Centred title over the LED (white, then red)", "opening-recut/moodboard/text/TX3.jpg"), ("TX4a", "Progress bar over the servers...", "opening-recut/moodboard/text/TX4a.jpg"), ("TX4b", "...then the red line over the LED", "opening-recut/moodboard/text/TX4b.jpg")]}
EXISTING = {}  # scene -> [(id, look, path relative to clips root)]; the drain grates left with the drain (16 Oct)

CUR = "opening-recut/moodboard/current/"
EXISTING["street"] = [("NOW-car", "On the timeline now: the near-miss car (replace)", CUR + "NOW-car.jpg"), ("KEEP-rain", "On the timeline now: rain and server cabinets (keep)", CUR + "KEEP-rain.jpg")]
EXISTING["toast"] = [("NOW-champagne", "Now: the champagne table (replace)", CUR + "NOW-champagne.jpg"), ("NOW-graph", "Now: two men at the graph (replace)", CUR + "NOW-graph.jpg")]
EXISTING["bread"] = [("NOW-shop", "Now: the shop queue (replace)", CUR + "NOW-shop.jpg")]
EXISTING["market"] = [("NOW-exchange", "Now: the old stock exchange (replace)", CUR + "NOW-exchange.jpg"), ("KEEP-laughing", "Now: the laughing traders (keep)", CUR + "KEEP-laughing.jpg")]
EXISTING["choir"] = [("NOW-site", "Now at the drop: the building site (replace)", CUR + "NOW-site.jpg"), ("NOW-site2", "Now at the drop: the floodlit site (replace)", CUR + "NOW-site2.jpg")]

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
        p = os.path.join(root, "opening-recut/moodboard", iid + ".jpg")
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
  <header><span class="beat">{beat}</span><h2>{html.escape(name)}</h2><p>{html.escape(blurb)}</p></header>
  <div class="grid">{''.join(figs)}</div>
  <label class="note" for="note-{key}">Note on this scene's look</label>
  <textarea id="note-{key}" data-scene="{key}" rows="2" placeholder="e.g. B4's scale with B3's warmth"></textarea>
  <div class="saved" data-for="{key}"></div>
</section>''')
    tpl = open(os.path.join(os.path.dirname(__file__), "opening-moodboard-template.html")).read()
    open(out, "w").write(tpl.replace("<!--SECTIONS-->", "\n".join(sections)).replace("<!--NAV-->", "".join(f'<a href="#{k}">{b} · {html.escape(n)}</a>' for k, b, n, _ in SCENES)))

if __name__ == "__main__":
    main(*sys.argv[1:4])
