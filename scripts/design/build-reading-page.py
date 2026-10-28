#!/usr/bin/env python3
"""Turn a design markdown file (and, optionally, a folder of companion files) into one reading page.

    python3 scripts/design/build-reading-page.py <main.md> <out.html> [--appendix <dir>] [--appendix-title "Heading"] [--title "Name"]

The main file is the page. Each other .md in --appendix becomes a fold-out section below it, in name order.
Handles the markdown these design files use: headings, pipe tables, lists, paragraphs, **bold**,
*italic*, `code`, [links](url), --- rules. Links to the appendix files jump to their fold-out.
The page is the reading surface; the markdown stays the record, so edit the .md and rebuild.
"""
import html
import pathlib
import re
import sys

CSS = r"""
:root{--bg:#f6f3ee;--paper:#fffdf9;--fg:#1f1b17;--muted:#6f665c;--rule:#e2dbd0;--accent:#b4232c;--chip:#efe8dd;--row:#faf6f0;color-scheme:light}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--bg:#15130f;--paper:#1d1a16;--fg:#ece6dc;--muted:#a59b8e;--rule:#352f28;--accent:#e2555c;--chip:#2a251f;--row:#221e19;color-scheme:dark}}
:root[data-theme="dark"]{--bg:#15130f;--paper:#1d1a16;--fg:#ece6dc;--muted:#a59b8e;--rule:#352f28;--accent:#e2555c;--chip:#2a251f;--row:#221e19;color-scheme:dark}
body{background:var(--bg);color:var(--fg);font:17px/1.6 "Source Serif 4",Georgia,serif}
main{max-width:860px;margin:0 auto;padding-block:40px 80px;padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px))}
h1,h2,h3,h4{font-family:"Inter",system-ui,sans-serif;text-wrap:balance;line-height:1.25}
h1{font-size:2rem;margin:0 0 .4em}
h2{font-size:1.4rem;margin:2.2em 0 .6em;padding-top:.6em;border-top:2px solid var(--fg)}
h3{font-size:1.12rem;margin:1.8em 0 .4em;color:var(--accent)}
h4{font-size:1rem;margin:1.4em 0 .3em}
p,li{max-width:68ch}
a{color:var(--accent)}
code{font:0.85em ui-monospace,Menlo,monospace;background:var(--chip);padding:.05em .35em;border-radius:3px}
hr{border:0;border-top:1px solid var(--rule);margin:2.4em 0}
.tbl{overflow-x:auto;margin:1em 0;border:1px solid var(--rule);border-radius:6px;background:var(--paper)}
table{border-collapse:collapse;width:100%;font:15px/1.45 "Inter",system-ui,sans-serif}
th{text-align:left;font-size:.72rem;letter-spacing:.06em;text-transform:uppercase;color:var(--muted);padding:.6em .8em;border-bottom:1px solid var(--rule)}
td{padding:.55em .8em;border-top:1px solid var(--rule);vertical-align:top}
tr:nth-child(even) td{background:var(--row)}
td.line{font:16px/1.5 "Source Serif 4",Georgia,serif}
td.who{font-weight:600;white-space:nowrap}
td.num{white-space:nowrap;color:var(--muted);font-variant-numeric:tabular-nums}
td.tag{color:var(--muted);font-size:.8rem;white-space:nowrap}
.stage{color:var(--muted);font-style:italic}
nav{font:14px/1.5 "Inter",system-ui,sans-serif;background:var(--paper);border:1px solid var(--rule);border-radius:6px;padding:.8em 1em;margin:1.5em 0}
nav b{display:block;font-size:.72rem;letter-spacing:.06em;text-transform:uppercase;color:var(--muted);margin-bottom:.3em}
nav a{display:inline-block;margin:.15em .9em .15em 0;text-decoration:none}
details{background:var(--paper);border:1px solid var(--rule);border-radius:6px;margin:.7em 0;padding:0 1em}
summary{cursor:pointer;font:600 15px/1.4 "Inter",system-ui,sans-serif;padding:.8em 0}
details[open] summary{border-bottom:1px solid var(--rule);margin-bottom:.4em}
details h1{font-size:1.3rem;margin-top:.8em}
details h2{font-size:1.1rem;border-top-width:1px}
.lede{color:var(--muted);font-size:.95rem}
"""


def inline(s):
    s = html.escape(s, quote=False)
    s = re.sub(r'`([^`]+)`', r'<code>\1</code>', s)
    s = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', s)
    s = re.sub(r'(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])', r'<i>\1</i>', s)
    s = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', lambda m: f'<a href="{link(m.group(2))}">{m.group(1)}</a>', s)
    s = re.sub(r'\[((?:pause|beat|big pause|ahem|whispered[^\]]*|rushed|gently[^\]]*|door slam|long pause[^\]]*|through the door[^\]]*|eyes on[^\]]*)[^\]]*)\]',
               r'<span class="stage">[\1]</span>', s)
    return s


def link(href):
    name = pathlib.Path(href).name
    return '#' + slug(name[:-3]) if href.endswith('.md') and not href.startswith('http') else href


def slug(s):
    return re.sub(r'[^a-z0-9]+', '-', s.lower()).strip('-')


def cell_class(header, i, text):
    h = header[i].strip().lower() if i < len(header) else ''
    if h in ('line', 'verdict'):
        return 'line'
    if h == 'speaker':
        return 'who'
    if h in ('tag',):
        return 'tag'
    if h in ('est. s', 'est. sec', 'length', 'rank', '#', 'shape'):
        return 'num'
    return ''


def table(rows):
    split = lambda r: [c.strip() for c in r.strip().strip('|').split('|')]
    head = split(rows[0])
    body = [split(r) for r in rows[2:]]
    out = ['<div class="tbl"><table><thead><tr>' + ''.join(f'<th>{inline(c)}</th>' for c in head) + '</tr></thead><tbody>']
    for r in body:
        out.append('<tr>' + ''.join(f'<td class="{cell_class(head, i, c)}">{inline(c)}</td>' for i, c in enumerate(r)) + '</tr>')
    out.append('</tbody></table></div>')
    return '\n'.join(out)


def render(md, toc=None, prefix=''):
    lines, out, i = md.split('\n'), [], 0
    while i < len(lines):
        ln = lines[i]
        if not ln.strip():
            i += 1
        elif ln.startswith('|'):
            j = i
            while j < len(lines) and lines[j].startswith('|'):
                j += 1
            out.append(table(lines[i:j]))
            i = j
        elif m := re.match(r'(#{1,4}) (.*)', ln):
            n, text = len(m.group(1)), m.group(2)
            hid = prefix + slug(text)
            if toc is not None and n in (2, 3):
                toc.append((n, hid, text))
            out.append(f'<h{n} id="{hid}">{inline(text)}</h{n}>')
            i += 1
        elif ln.strip() == '---':
            out.append('<hr>')
            i += 1
        elif re.match(r'\s*(-|\d+\.) ', ln):
            tag = 'ol' if re.match(r'\s*\d+\.', ln) else 'ul'
            items = []
            while i < len(lines) and re.match(r'\s*(-|\d+\.) ', lines[i]):
                items.append(re.sub(r'^\s*(-|\d+\.) ', '', lines[i]))
                i += 1
            out.append(f'<{tag}>' + ''.join(f'<li>{inline(x)}</li>' for x in items) + f'</{tag}>')
        else:
            para = []
            while i < len(lines) and lines[i].strip() and not re.match(r'(#{1,4} |\||---$|\s*(-|\d+\.) )', lines[i]):
                para.append(lines[i])
                i += 1
            out.append('<p>' + inline(' '.join(para)) + '</p>')
    return '\n'.join(out)


def main(argv):
    main_md, out = pathlib.Path(argv[0]), pathlib.Path(argv[1])
    title = argv[argv.index('--title') + 1] if '--title' in argv else main_md.stem
    text = main_md.read_text()
    h1 = re.match(r'# (.*)\n', text)
    toc = []
    body = render(text[h1.end():] if h1 else text, toc)
    nav = '<nav><b>Jump to</b>' + ''.join(f'<a href="#{hid}">{html.escape(t)}</a>' for n, hid, t in toc if n == 2 or t.startswith('Draft')) + '</nav>'
    appendix = ''
    if '--appendix' in argv:
        d = pathlib.Path(argv[argv.index('--appendix') + 1])
        parts = []
        for f in sorted(d.glob('*.md')):
            if f.resolve() == main_md.resolve():
                continue
            ft = f.read_text()
            fh = re.match(r'# (.*)\n', ft)
            name = fh.group(1) if fh else f.stem
            parts.append(f'<details id="{slug(f.stem)}"><summary>{inline(name)}</summary>'
                         + render(ft[fh.end():] if fh else ft, None, slug(f.stem) + '-') + '</details>')
        at = argv[argv.index('--appendix-title') + 1] if '--appendix-title' in argv else 'The ten shapes in full'
        appendix = (f'<h2 id="{slug(at)}">{html.escape(at)}</h2><p class="lede">Each file in full. Tap one to open it.</p>'
                    + ''.join(parts))
        nav = nav.replace('</nav>', f'<a href="#{slug(at)}">{html.escape(at)}</a></nav>')
    page = (f'<title>{html.escape(title)}</title>\n<meta name="claude:viewport-fit-sides" content="cover">\n'
            '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600&family=Source+Serif+4:ital,wght@0,400;0,600;1,400&display=swap">\n'
            f'<style>{CSS}</style>\n<main><h1>{inline(h1.group(1) if h1 else title)}</h1>{nav}\n{body}\n{appendix}</main>\n'
            # a jump to a fold-out opens it
            '<script>function o(){const d=document.getElementById(location.hash.slice(1));if(d&&d.tagName==="DETAILS")d.open=true}'
            'addEventListener("hashchange",o);o()</script>\n')
    out.write_text(page)
    print(out, len(page), 'bytes')


if __name__ == '__main__':
    main(sys.argv[1:])
