#!/usr/bin/env python3
"""The timeline index: one page listing every timeline page we have, film by film, with the Premiere
sequence each one drives and when it last moved.

    python3 scripts/scene/build-timeline-index.py <out.html>

Order and grouping: docs/stories/timelines-index.json. Everything else is read from each scene's
scene.json (boards.timeline, premiere.current) and trail.json (last entry), so a new timeline shows up
on the next run. Shorts (docs/stories/short-*/ and docs/stories/shorts/*) are found by themselves.
Republish the page to the same file path so the link stays (url in timelines-index.json).
"""
import datetime
import html
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
STORIES = ROOT / 'docs' / 'stories'
cfg = json.loads((STORIES / 'timelines-index.json').read_text())


def scene(rel):
    d = STORIES / rel
    s = json.loads((d / 'scene.json').read_text())
    pr = s.get('premiere', {})
    rec = pr.get(pr.get('current') or '', {}) if isinstance(pr, dict) else {}
    last, last_full = '', ''
    t = d / 'trail.json'
    if t.exists():
        try:
            tr = json.loads(t.read_text())
            tr = tr if isinstance(tr, list) else tr.get('entries', [])
            last_full = (tr[-1].get('at') or '') if tr else ''
            last = last_full[:10]
        except (ValueError, AttributeError):
            pass
    proj = rec.get('project') or s.get('premiere_project') or ''
    return {'title': s.get('title') or d.name, 'url': (s.get('boards') or {}).get('timeline'),
            'seq': rec.get('sequence', ''), 'project': pathlib.PurePosixPath(proj).name if proj else '',
            'last': last, 'done': frozen(d, last_full)}


def frozen(d, last_full):
    """Frozen only if nothing has happened since the freeze: a short reopened after its final.json (Priority Lane,
    frozen 2026-11-11 at round 2, reopened as round 3 on 2026-11-13) is live again."""
    f = d / 'final.json'
    if not f.exists():
        return False
    try:
        at = json.loads(f.read_text()).get('frozen') or ''
    except ValueError:
        return True
    return not (last_full and at and last_full[:19] > at[:19])


films = []
for f in cfg['films']:
    films.append({**f, 'mainS': scene(f['main']) if f.get('main') else None,
                  'partsS': [scene(p) for p in f.get('parts', [])], 'alsoS': [scene(p) for p in f.get('also', [])]})
shorts = []
for sj in sorted(list(STORIES.glob('short-*/scenes/*/scene.json')) + list(STORIES.glob('shorts/*/scene.json'))):
    s = scene(str(sj.parent.relative_to(STORIES)))
    if s['url']:
        shorts.append(s)
shorts.sort(key=lambda s: s['last'], reverse=True)

today = datetime.date.today()


def age(d):
    if not d:
        return ''
    n = (today - datetime.date.fromisoformat(d)).days
    return 'today' if n == 0 else 'yesterday' if n == 1 else f'{n} days ago'


e = html.escape


def row(s, label=None):
    link = (f'<a class="open" href="{e(s["url"])}" target="_blank" rel="noopener">Open timeline</a>' if s['url']
            else '<span class="none">No page yet</span>')
    seq = (f'<span class="seq">{e(s["seq"])}</span>' if s['seq'] else '<span class="dim">no Premiere sequence recorded</span>')
    proj = f'<span class="proj">{e(s["project"])}</span>' if s['project'] else ''
    fresh = ' fresh' if s['last'] == today.isoformat() else ''
    done = '<span class="chip done">Frozen</span>' if s['done'] else ''
    return (f'<li class="row"><div class="what"><span class="t">{e(label or s["title"])}</span>{done}</div>'
            f'<div class="pr">{seq}{proj}</div><div class="when{fresh}">{e(age(s["last"]))}</div><div class="go">{link}</div></li>')


cards = []
for f in films:
    body = []
    if f.get('overview'):
        body.append(f'<p class="ov"><a class="open strong" href="{e(f["overview"])}" target="_blank" rel="noopener">'
                    f'Open the overview board</a> the whole film in order, and which timeline to open for each part.</p>')
    rows = ([row(f['mainS'])] if f['mainS'] else []) + [row(s) for s in f['partsS']]
    body.append(f'<ul class="rows">{"".join(rows)}</ul>')
    if f['alsoS']:
        body.append(f'<details><summary>{len(f["alsoS"])} side page{"s" if len(f["alsoS"]) > 1 else ""}</summary>'
                    f'<ul class="rows">{"".join(row(s) for s in f["alsoS"])}</ul></details>')
    cards.append(f'<section class="film"><header><h2>{e(f["name"])}</h2><span class="kind">{e(f["kind"])}</span></header>{"".join(body)}</section>')

page = f"""<title>BadCode Timelines</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wght@500;700;800&family=IBM+Plex+Mono:wght@400;500&family=IBM+Plex+Sans:wght@400;500&display=swap">
<style>
/* Layout: an edit-bay rundown, one block per film in release order, each row = one timeline page and the sequence it drives. */
:root {{
  --bg: #f3f2ef; --panel: #ffffff; --ink: #1b1d22; --muted: #5d6270; --line: #dcdad4; --accent: #c8321e; --fresh: #1d7a46;
  --display: "Archivo", "Helvetica Neue", Arial, sans-serif; --body: "IBM Plex Sans", system-ui, sans-serif;
  --mono: "IBM Plex Mono", ui-monospace, Menlo, monospace;
}}
@media (prefers-color-scheme: dark) {{ :root:not([data-theme="light"]) {{
  --bg: #131418; --panel: #1b1d23; --ink: #ecebe7; --muted: #9a9fab; --line: #2d3039; --accent: #ef5a40; --fresh: #4cc27f; color-scheme: dark; }} }}
:root[data-theme="dark"] {{ --bg: #131418; --panel: #1b1d23; --ink: #ecebe7; --muted: #9a9fab; --line: #2d3039; --accent: #ef5a40; --fresh: #4cc27f; color-scheme: dark; }}
body {{ background: var(--bg); color: var(--ink); font: 15px/1.5 var(--body); }}
.wrap {{ max-width: 1040px; margin: 0 auto; padding-block: 32px 64px; padding-left: max(16px, env(safe-area-inset-left, 0px)); padding-right: max(16px, env(safe-area-inset-right, 0px)); display: grid; gap: 20px; }}
h1 {{ font: 800 clamp(28px, 5vw, 40px)/1.05 var(--display); letter-spacing: -0.02em; margin: 0; text-wrap: balance; }}
h1 b {{ color: var(--accent); }}
.lede {{ color: var(--muted); max-width: 65ch; margin: 6px 0 0; }}
.stamp {{ font: 500 12px var(--mono); color: var(--muted); letter-spacing: .04em; text-transform: uppercase; }}
.film {{ background: var(--panel); border: 1px solid var(--line); border-radius: 6px; padding: 16px 18px; display: grid; gap: 10px; }}
.film header {{ display: flex; align-items: baseline; gap: 12px; flex-wrap: wrap; }}
h2 {{ font: 700 20px/1.2 var(--display); margin: 0; }}
.kind {{ font: 500 12px var(--mono); text-transform: uppercase; letter-spacing: .06em; color: var(--accent); }}
.ov {{ margin: 0; color: var(--muted); }}
.rows {{ list-style: none; margin: 0; padding: 0; display: grid; }}
.row {{ display: grid; grid-template-columns: minmax(0, 1.3fr) minmax(0, 1.5fr) 100px 130px; gap: 12px; align-items: center; padding: 8px 0; border-top: 1px solid var(--line); }}
.what {{ display: flex; gap: 8px; align-items: center; min-width: 0; flex-wrap: wrap; }}
.t {{ font-weight: 500; }}
.pr {{ display: grid; min-width: 0; }}
.seq {{ font: 500 13px var(--mono); overflow-wrap: anywhere; }}
.proj {{ font: 12px var(--mono); color: var(--muted); overflow-wrap: anywhere; }}
.dim, .none {{ color: var(--muted); font-size: 13px; }}
.when {{ font: 12px var(--mono); color: var(--muted); font-variant-numeric: tabular-nums; }}
.when.fresh {{ color: var(--fresh); font-weight: 500; }}
.go {{ text-align: right; }}
a.open {{ color: var(--accent); font-weight: 500; text-decoration: none; border-bottom: 1px solid currentColor; }}
a.open:hover, a.open:focus-visible {{ color: var(--ink); outline: none; }}
a.open.strong {{ font-weight: 700; }}
.chip.done {{ font: 500 11px var(--mono); text-transform: uppercase; letter-spacing: .05em; padding: 1px 6px; border: 1px solid var(--line); border-radius: 3px; color: var(--muted); }}
details summary {{ cursor: pointer; color: var(--muted); font-size: 13px; padding-top: 4px; }}
@media (max-width: 720px) {{
  .row {{ grid-template-columns: 1fr auto; }}
  .pr {{ grid-column: 1 / -1; order: 3; }}
  .when {{ order: 2; text-align: right; }}
  .go {{ grid-column: 1 / -1; order: 4; text-align: left; }}
}}
</style>
<div class="wrap">
  <div><span class="stamp">Rebuilt {today.isoformat()} · {sum(1 for f in films for _ in ([f['mainS']] if f['mainS'] else []) + f['partsS'] + f['alsoS']) + len(shorts)} timeline pages</span>
  <h1>BadCode <b>timelines</b></h1>
  <p class="lede">Every timeline page we can note on, one block per film. Each row says which Premiere sequence the page drives,
  the project it lives in, and when the page last changed. Notes go on the timeline page itself.</p></div>
  {''.join(cards)}
  <section class="film"><header><h2>BadCode Shorts</h2><span class="kind">{len(shorts)} shorts, newest first</span></header>
  <ul class="rows">{''.join(row(s) for s in shorts)}</ul></section>
</div>
"""
out = pathlib.Path(sys.argv[1])
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(page)
print(json.dumps({'films': len(films), 'shorts': len(shorts), 'out': str(out)}))
