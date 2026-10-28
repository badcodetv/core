#!/usr/bin/env python3
"""A story's running order page: every part of the film, start to end, and its timeline page.

    python3 scripts/provenance/build-timelines.py docs/stories/<story>

Reads <story>/timelines.json (the running order, written by the overview-board skill: sections in film
order, each with the beat it must land, its state, its current timeline page, and earlier pages under
"history") and fills in from each section's scene folder:
  scene.json "boards"   the scene's pages (timeline, mood board, storyboard)
  trail.json            every page published for that scene (prov.py trail), oldest first
  final.json            the cut is frozen: shown as "recipe frozen"
Writes <story>/timelines/index.html. Publish it to the URL in timelines.json ("url") every time it
changes, so the link never moves. See docs/provenance/README.md.
"""
import html
import json
import pathlib
import sys

KIND = {'moodboard': 'mood board', 'storyboard': 'storyboard', 'timeline': 'timeline', 'clips': 'clips board', 'picks': 'picks page'}
TONES = {'premiere': ('ok', 'In Premiere'), 'ok': ('ok', ''), 'wip': ('wip', ''), 'gap': ('gap', ''), 'done': ('ok', '')}


def esc(s):
    return html.escape(str(s or ''))


def fill(sec, story):
    """Merge what the scene folder knows into a section: its pages, its trail, its frozen recipe."""
    hist = list(sec.get('history', []))
    seen = {h['url'] for h in hist} | {sec.get('timeline')}
    d = story / sec['scene'] if sec.get('scene') else None
    if d and (d / 'scene.json').exists():
        cfg = json.loads((d / 'scene.json').read_text())
        boards = cfg.get('boards', {})
        if not sec.get('timeline') and boards.get('timeline'):
            sec['timeline'] = boards['timeline']
            seen.add(sec['timeline'])
        for k, url in boards.items():
            if url not in seen:
                hist.append({'name': f"{cfg.get('title', d.name)} {KIND.get(k, k)}", 'url': url, 'kind': KIND.get(k, k)})
                seen.add(url)
        trail = json.loads((d / 'trail.json').read_text()) if (d / 'trail.json').exists() else []
        rounds = [t for t in trail if t.get('url')]
        for t in rounds:
            if t['url'] not in seen:
                hist.append({'name': t.get('what', ''), 'url': t['url'], 'kind': KIND.get(t['stage'], t['stage']),
                             'date': t.get('at', '')[:10], 'decided': list(t.get('decided') or [])})
                seen.add(t['url'])
            else:  # a later round of a page already listed: its decisions still belong on the record
                for h in hist + [sec]:
                    if h.get('url', h.get('timeline')) == t['url'] and t.get('decided'):
                        h.setdefault('decided', []).extend(t['decided'])
        if rounds:
            last = [t for t in rounds if t['url'] == sec.get('timeline')]
            if last and last[-1].get('round') is not None:
                sec['round'] = last[-1]['round']
        pr = cfg.get('premiere') or {}
        if pr.get('current'):  # which Premiere sequence this page currently drives, and the ones it replaced
            cur = pr[pr['current']]
            sec['pr'] = {'sequence': cur['sequence'], 'check': cur.get('check', {}),
                         'older': [r['sequence'] for k, r in pr.items() if isinstance(r, dict) and k != pr['current']]}
        if (d / 'final.json').exists():
            sec['frozen'] = json.loads((d / 'final.json').read_text()).get('frozen', '')[:10]
    sec['history'] = sorted(hist, key=lambda h: h.get('date', ''), reverse=True)
    for p in sec.get('parts', []):
        fill(p, story)
    return sec


def row(sec, now, child=False):
    tone, default = TONES.get(sec.get('tone', 'wip'), ('wip', ''))
    bits = [f'<span class="name">{esc(sec["name"])}</span>']
    for k in ('at', 'length'):
        if sec.get(k):
            bits.append(f'<span class="tc">{esc(sec[k])}</span>')
    bits.append(f'<span class="st {tone}">{esc(sec.get("state") or default)}</span>')
    if sec.get('frozen'):
        bits.append(f'<span class="st ok">recipe frozen {esc(sec["frozen"])}</span>')
    out = [f'<li class="{"now" if sec["id"] == now else ""}{" part" if child else ""}">',
           f'<div class="row">{"".join(bits)}</div>']
    if sec.get('beat'):
        out.append(f'<div class="beat">{esc(sec["beat"])}</div>')
    if sec.get('what'):
        out.append(f'<div class="what">{esc(sec["what"])}</div>')
    links = []
    if sec.get('timeline'):
        rnd = f' (round {sec["round"]})' if sec.get('round') is not None else ''
        links.append(f'<a href="{esc(sec["timeline"])}">Open the timeline{rnd}</a>')
    if sec.get('pr'):
        st = sec['pr']['check'].get('state', 'not checked')
        links.append(f'<span class="tc">Premiere: <b>{esc(sec["pr"]["sequence"])}</b> · {esc(st)}</span>')
    elif sec.get('premiere'):
        links.append(f'<span class="tc">Premiere: {esc(sec["premiere"])}</span>')
    if sec.get('scene'):
        links.append(f'<span class="tc">repo: {esc(sec["scene"])}/</span>')
    if links:
        out.append(f'<div class="links">{"".join(links)}</div>')
    if sec.get('decided'):
        out.append('<div class="decs">' + ''.join(f'<div class="dec">→ {esc(x)}</div>' for x in sec['decided']) + '</div>')
    if sec.get('history'):
        items = ''.join(f'<li><a href="{esc(h["url"])}">{esc(h["name"])}</a> <span class="tc">{esc(h.get("kind", ""))}'
                        f'{" · " + esc(h["date"]) if h.get("date") else ""}</span>'
                        + (''.join(f'<div class="dec">→ {esc(x)}</div>' for x in h['decided']) if h.get('decided') else '')
                        + '</li>' for h in sec['history'])
        out.append(f'<details><summary>Earlier pages ({len(sec["history"])})</summary><ul>{items}</ul></details>')
    if sec.get('parts'):
        out.append('<ol class="parts">' + ''.join(row(p, now, True) for p in sec['parts']) + '</ol>')
    out.append('</li>')
    return ''.join(out)


CSS = """
/* Layout: one column in film order, like a timeline ruler; the "open now" row is lit; parts nest under their section. */
:root {
  --bg: #f3f2f0; --panel: #ffffff; --fg: #1b1a19; --muted: #6b6762; --line: #dcd8d3;
  --red: #c8281e; --amber: #a86a00; --green: #2f7a3e; --now: #fff4ec;
  --sans: "IBM Plex Sans", system-ui, sans-serif; --mono: "IBM Plex Mono", ui-monospace, monospace;
}
@media (prefers-color-scheme: dark) { :root:not([data-theme="light"]) {
  --bg: #121212; --panel: #1b1b1b; --fg: #ece9e5; --muted: #9a958f; --line: #2c2b2a;
  --red: #ff5a4c; --amber: #e0a440; --green: #6cc27e; --now: #2a1714; color-scheme: dark } }
:root[data-theme="dark"] {
  --bg: #121212; --panel: #1b1b1b; --fg: #ece9e5; --muted: #9a958f; --line: #2c2b2a;
  --red: #ff5a4c; --amber: #e0a440; --green: #6cc27e; --now: #2a1714; color-scheme: dark }
body { background: var(--bg); color: var(--fg); font: 15px/1.5 var(--sans); }
main { max-width: 760px; margin: 0 auto; padding-block: 28px 48px;
  padding-left: max(16px, env(safe-area-inset-left, 0px)); padding-right: max(16px, env(safe-area-inset-right, 0px)); }
h1 { font: 600 22px/1.2 var(--mono); margin: 0 0 4px; text-wrap: balance; }
h1 .tri { color: var(--red); }
.sub { color: var(--muted); margin: 0 0 24px; }
h2 { font: 600 12px var(--mono); letter-spacing: .08em; text-transform: uppercase; color: var(--muted); margin: 28px 0 8px; }
ol { list-style: none; margin: 0; padding: 0; display: grid; gap: 8px; }
li { background: var(--panel); border: 1px solid var(--line); border-radius: 6px; padding: 12px 14px; display: grid; gap: 6px; min-width: 0; }
li.now { background: var(--now); border-color: var(--red); }
ol.parts { margin-top: 4px; }
li.part { background: transparent; border-style: dashed; padding: 8px 12px; }
.row, .links { display: flex; flex-wrap: wrap; gap: 6px 12px; align-items: baseline; }
.name { font-weight: 600; }
.tc { font: 12px var(--mono); color: var(--muted); overflow-wrap: anywhere; }
.st { font: 600 11px var(--mono); letter-spacing: .05em; text-transform: uppercase; padding: 1px 7px; border-radius: 99px; border: 1px solid currentColor; }
.ok { color: var(--green); } .wip { color: var(--amber); } .gap { color: var(--red); }
.what { color: var(--muted); }
.beat { font-style: italic; }
.dec { font-size: 13px; color: var(--muted); }
.count { font: 12px var(--mono); color: var(--muted); margin: -16px 0 24px; }
details summary { font: 12px var(--mono); color: var(--muted); cursor: pointer; }
details ul { margin: 6px 0 0; padding-left: 18px; display: grid; gap: 2px; }
details li { background: none; border: 0; padding: 0; display: list-item; }
a { color: var(--fg); text-underline-offset: 3px; }
a:focus-visible, summary:focus-visible { outline: 2px solid var(--red); outline-offset: 2px; }
.tbl { overflow-x: auto; } table { border-collapse: collapse; width: 100%; background: var(--panel); border: 1px solid var(--line); border-radius: 6px; }
th, td { text-align: left; padding: 8px 10px; border-bottom: 1px solid var(--line); vertical-align: top; font-size: 14px; }
th { font: 600 11px var(--mono); letter-spacing: .06em; text-transform: uppercase; color: var(--muted); }
.upd { font: 12px var(--mono); color: var(--muted); margin-top: 28px; }
"""


SYNC = {'in sync': 'ok', 'page ahead': 'wip', 'edited in Pr': 'gap'}


def premiere_map(secs, t):
    """One table: each timeline page, the Premiere sequence it drives now, whether they still match,
    and the sequences it replaced; then every other sequence in the project and whose it is."""
    rows = []
    for s in secs:
        kids = [p for p in s.get('parts', []) if p.get('pr')]
        if kids and s.get('timeline') and not s.get('pr'):  # a reel page over several parts drives all of theirs
            rows.append(f'<tr><td><a href="{esc(s["timeline"])}">{esc(s["name"])}</a></td>'
                        f'<td class="tc" colspan="3">drives all of: {esc(", ".join(k["pr"]["sequence"] for k in kids))}</td></tr>')
        for p in [s] + s.get('parts', []):
            if p.get('pr'):
                c = p['pr']['check']
                page = f'<a href="{esc(p["timeline"])}">{esc(p["name"])}</a>' if p.get('timeline') else esc(p['name'])
                rows.append(f'<tr><td>{page}</td><td class="tc"><b>{esc(p["pr"]["sequence"])}</b></td>'
                            f'<td><span class="st {SYNC.get(c.get("state"), "wip")}">{esc(c.get("state", "not checked"))}</span>'
                            f'{"<div class=tc>" + esc(c["why"]) + "</div>" if c.get("why") else ""}</td>'
                            f'<td class="tc">{esc(", ".join(p["pr"]["older"]) or "none")}</td></tr>')
    if not rows:
        return ''
    pm = t.get('premiere', {})
    other = ''.join(f'<li><span class="tc"><b>{esc(o["sequence"])}</b></span> <span class="tc">· {esc(o["what"])}</span></li>'
                    for o in pm.get('other', []))
    when = {p['pr']['check'].get('at', '')[:16] for s in secs for p in [s] + s.get('parts', []) if p.get('pr')} - {''}
    return ('<h2>Premiere map</h2>'
            f'<p class="what">{esc(pm.get("project", ""))}. The bold sequence is the one each timeline page drives: '
            'notes on the page land there as a new round. Checked against Premiere '
            f'{esc(max(when).replace("T", " ") if when else "never")}.</p>'
            '<div class="tbl"><table><tr><th>Timeline page</th><th>Current sequence</th><th>Matches the page?</th>'
            f'<th>Older, replaced</th></tr>{"".join(rows)}</table></div>'
            + (f'<details><summary>Every other sequence in the project ({len(pm.get("other", []))})</summary><ul>{other}</ul></details>' if other else ''))


def main(story_dir):
    story = pathlib.Path(story_dir).resolve()
    t = json.loads((story / 'timelines.json').read_text())
    secs = [fill(s, story) for s in t['sections']]
    leaves = [p for s in secs for p in (s.get('parts') or [s])]
    tally = {'on a timeline': sum(bool(p.get('timeline')) for p in leaves),
             'in Premiere': sum(not p.get('timeline') and p.get('tone') == 'premiere' for p in leaves),
             'not made': sum(not p.get('timeline') and p.get('tone') == 'gap' for p in leaves)}
    count = f'{len(leaves)} parts · ' + ' · '.join(f'{v} {k}' for k, v in tally.items() if v)
    body, group = [premiere_map(secs, t)], None
    for s in secs:
        if s.get('group') != group:
            if group is not None:
                body.append('</ol>')
            group = s.get('group')
            body.append(f'<h2>{esc(group)}</h2><ol>')
        body.append(row(s, t.get('open_now')))
    body.append('</ol>')
    short = ''.join(w[0] for w in t['title'].split()).upper() if len(t['title']) > 20 else t['title']
    page = (f'<title>{esc(short)} Timelines</title>\n'
            '<meta name="claude:viewport-fit-sides" content="cover">\n'
            '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;600'
            '&family=IBM+Plex+Sans:wght@400;600&display=swap">\n'
            f'<style>{CSS}</style>\n<main>\n'
            f'<h1>{esc(t["title"])} <span class="tri">▲</span> timelines</h1>\n'
            f'<p class="sub">{esc(t.get("intro", "The whole film, start to end. Open the lit one first."))}</p>\n'
            f'<p class="count">{esc(count)}</p>\n'
            + '\n'.join(body) +
            f'\n<p class="upd">Updated {esc(t.get("updated", ""))}. Built from <code>docs/stories/{esc(story.name)}/timelines.json</code>; '
            'Claude rebuilds it whenever a timeline changes state.</p>\n</main>\n')
    out = story / 'timelines' / 'index.html'
    out.parent.mkdir(exist_ok=True)
    out.write_text(page)
    print(json.dumps({'page': str(out), 'url': t.get('url'), 'sections': len(secs),
                      'timelines': sum(bool(s.get('timeline')) + sum(bool(p.get('timeline')) for p in s.get('parts', [])) for s in secs)}))


if __name__ == '__main__':
    main(sys.argv[1])
