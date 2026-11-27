#!/usr/bin/env python3
"""Every timeline page, served from this machine: no claude.ai upload, no daily upload limit (Kai, 2026-11-27:
"we should be able to operate the timeline tool without needing Claude artifacts").

    python3 scripts/scene/timeline-serve.py [--port 8765] [--as Kai] [--open story/scene[/cut]]

One server for all of them. http://localhost:8765 lists every scene with a cut and each of its earlier cuts;
a timeline is at /t/<story>/<scene>/ (the current cut, with Claude's replies) or /t/<story>/<scene>/<cut>/ (an
earlier cut, by its folder name), so several can be open at once on one port. Windows opens it too (WSL
forwards localhost); --open opens a page in the Windows browser (scripts/open-in-windows.sh).

It is the same page as the artifact (scripts/scene/timeline-template.html, built by build-timeline.py --local):
- the picture is the cut's full preview (1080p) streamed straight from disk, with seeking;
- notes save as files, one per note, in <scene>/feedback/timeline-local/<cut folder>/notes/<key>__<user>.json,
  the same shape as a dump of the artifact's notes, so Claude reads them with nothing in between, and the next
  cut's page shows them "on record";
- a page rebuilds itself on reload when its cut (scene.json, edl, preview) or Claude's replies (cut-notes.json)
  change.

Only this machine can open it (127.0.0.1). Notes are signed as --as (a name in docs/stories/people.json; default
"who" in this machine's badcode.local.json, e.g. "who": "Jack", else the login name), so they carry on from the artifact pages' notes.
"""
import argparse
import html
import json
import os
import pathlib
import re
import subprocess
import sys
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import unquote

HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parents[1]
STORIES = REPO / 'docs' / 'stories'
sys.path.insert(0, str(HERE.parent / 'drive'))
from localmap import localize  # noqa: E402

ap = argparse.ArgumentParser()
ap.add_argument('--port', type=int, default=8765)
ap.add_argument('--as', dest='who', default=None,
                help='who signs the notes; default: "who" in badcode.local.json (this machine), else the login name')
ap.add_argument('--open', help='open story/scene[/cut] in the Windows browser once the server is up')
ap.add_argument('--cache', default=str(pathlib.Path.home() / '.cache' / 'badcode-timeline'))
a = ap.parse_args()

if not a.who:  # each machine signs its own notes (2026-11-27: a fixed default of Kai would have signed Jack's notes as Kai)
    try:
        a.who = json.loads((REPO / 'badcode.local.json').read_text()).get('who')
    except (OSError, ValueError):
        pass
    a.who = a.who or os.environ.get('USER', 'someone').capitalize()
CACHE = pathlib.Path(a.cache)
PEOPLE_FILE = STORIES / 'people.json'
PEOPLE = {k: v for k, v in (json.loads(PEOPLE_FILE.read_text()) if PEOPLE_FILE.exists() else {}).items() if not k.startswith('_')}
ME = next((k for k, v in PEOPLE.items() if v.lower() == a.who.lower()), 'local-' + re.sub(r'\W', '', a.who.lower()))
NAME = re.compile(r'^[A-Za-z0-9_.-]{1,120}$')
LOCKS, BUILT = {}, {}


def scene_cfg(story, scene):
    f = STORIES / story / 'scenes' / scene / 'scene.json'
    if not (NAME.match(story) and NAME.match(scene) and f.exists()):
        return None
    cfg = localize(json.loads(f.read_text()))
    return cfg if cfg.get('cut', {}).get('edl') else None


def cuts(cfg):
    """[(name, folder, is_current)] newest first: the current cut, then earlier cut folders beside it that have
    an edl.json and a preview.mp4 and share its name up to the first '-' (several scenes can share one parent)."""
    cur = pathlib.Path(cfg['cut']['edl']).parent
    out = [(cur.name, cur, True)]
    stem = cur.name.split('-')[0]
    try:
        sibs = [d for d in cur.parent.iterdir() if d.is_dir() and d != cur and (d / 'edl.json').exists()
                and (d / 'preview.mp4').exists() and (d.name == stem or d.name.startswith(stem + '-') or '-' not in cur.name)]
    except OSError:
        sibs = []
    sibs.sort(key=lambda d: (d / 'edl.json').stat().st_mtime, reverse=True)
    return out + [(d.name, d, False) for d in sibs]


def resolve(story, scene, cut):
    cfg = scene_cfg(story, scene)
    if not cfg:
        return None
    for name, folder, current in cuts(cfg):
        if cut in ('', name):
            return {'cfg': cfg, 'dir': STORIES / story / 'scenes' / scene, 'cut': name, 'folder': folder, 'current': current,
                    'out': CACHE / story / scene / name,
                    'edl': pathlib.Path(cfg['cut']['edl']) if current else folder / 'edl.json',
                    'preview': pathlib.Path(cfg['cut'].get('preview', folder / 'preview.mp4')) if current else folder / 'preview.mp4'}
    return None


def ensure_built(t):
    key = str(t['out'])
    with LOCKS.setdefault(key, threading.Lock()):
        deps = [t['dir'] / 'scene.json', t['dir'] / 'cut-notes.json', t['edl'], t['preview'],
                HERE / 'timeline-template.html', HERE / 'timeline.py', HERE / 'build-timeline.py']
        now = {str(f): f.stat().st_mtime for f in deps if f.exists()}
        if now == BUILT.get(key) and (t['out'] / 'index.html').exists():
            return
        cmd = [sys.executable, str(HERE / 'build-timeline.py'), str(t['dir']), str(t['out']), '--local']
        if not t['current']:
            cmd.append(f"--cut={t['folder']}")
        r = subprocess.run(cmd, capture_output=True, text=True)
        if r.returncode:
            raise RuntimeError((r.stderr or r.stdout)[-3000:])
        BUILT[key] = now
        print('built', t['out'], flush=True)


SKELETON = ('<!doctype html><html lang="en"><head><meta charset="utf-8">'
            '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">'
            '<style>body{margin:0;font:14px system-ui,sans-serif}img{max-width:100%}[hidden]{display:none!important}</style>'
            '<script src="/_local/claude.js"></script></head><body>')

# window.claude, as much of it as the timeline page uses: use('db') and use('user'), backed by this server.
# Paths are relative ('_notes'), so each timeline talks to its own notes folder.
SHIM = """
(() => {
  const ME = %s, NAMES = %s;
  const api = (p, o) => fetch('_notes' + p, o).then(r => { if (!r.ok) throw Object.assign(new Error(r.statusText), { code: r.status }); return r });
  const db = {
    doc: path => { const id = encodeURIComponent(path.replace(/^notes\\//, ''));
      return { set: v => api('/' + id, { method: 'PUT', headers: { 'content-type': 'application/json' }, body: JSON.stringify(v) }),
               delete: () => api('/' + id, { method: 'DELETE' }) } },
    collection: () => ({ get: async () => ({ docs: (await (await api('')).json()).map(v => ({ data: () => v })) }) }),
  };
  const user = { id: async () => ME, profiles: async ids => Object.fromEntries(ids.map(i => [i, { name: NAMES[i] }])) };
  window.claude = { use: async name => name === 'db' ? db : name === 'user' ? user : null, local: true };
})();
"""

INDEX_CSS = """
:root{--bg:#f4f2ee;--fg:#1c1b19;--muted:#6d6760;--line:#dcd6ce;--accent:#b8321f}
@media (prefers-color-scheme:dark){:root{--bg:#151413;--fg:#eeeae4;--muted:#a19a91;--line:#35312d;--accent:#e2664f}}
body{background:var(--bg);color:var(--fg);font:15px/1.5 "IBM Plex Sans",system-ui,sans-serif}
.wrap{max-width:980px;margin:0 auto;padding:28px 16px 60px}h1{font:700 28px "Archivo Narrow",sans-serif;margin:0 0 4px}
p.lede{color:var(--muted);margin:0 0 22px}h2{font:600 13px "IBM Plex Mono",monospace;text-transform:uppercase;letter-spacing:.08em;color:var(--accent);margin:26px 0 8px}
.row{border-top:1px solid var(--line);padding:10px 0;display:grid;gap:4px}.row b a{color:var(--fg)}
.old{font:13px "IBM Plex Mono",monospace;color:var(--muted)}.old a{color:var(--muted);margin-right:10px;white-space:nowrap}
"""


def index_page():
    rows = []
    for sj in sorted(STORIES.glob('*/scenes/*/scene.json')):
        story, scene = sj.parents[2].name, sj.parent.name
        cfg = scene_cfg(story, scene)
        if not cfg or not pathlib.Path(cfg['cut']['edl']).exists():
            continue
        cs = cuts(cfg)
        base = f'/t/{story}/{scene}/'
        old = ''.join(f'<a href="{base}{html.escape(n)}/">{html.escape(n)}</a>' for n, _, cur in cs if not cur)
        title = html.escape(cfg.get('title', scene))
        rows.append((story, f'<div class="row"><b><a href="{base}">{title}</a></b>'
                            f'<span class="old">now: {html.escape(cs[0][0])}{" · earlier: " + old if old else ""}</span></div>'))
    body, last = [], None
    for story, r in rows:
        if story != last:
            body.append(f'<h2>{html.escape(story)}</h2>')
            last = story
        body.append(r)
    return ('<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">'
            '<title>Timelines</title><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo+Narrow:wght@700&family=IBM+Plex+Sans&family=IBM+Plex+Mono&display=swap">'
            f'<style>{INDEX_CSS}</style></head><body><div class="wrap"><h1>Timelines</h1>'
            '<p class="lede">Every scene with a cut on this machine. The title opens the current cut; the folder names open earlier ones. '
            'Notes save into the repo as you type.</p>' + ''.join(body) + '</div></body></html>')


class H(BaseHTTPRequestHandler):
    def log_message(self, *x):
        pass

    def send(self, code, body=b'', ctype='text/plain; charset=utf-8', extra=None):
        self.send_response(code)
        self.send_header('Content-Type', ctype)
        self.send_header('Content-Length', str(len(body)))
        self.send_header('Cache-Control', 'no-store')
        for k, v in (extra or {}).items():
            self.send_header(k, v)
        self.end_headers()
        if self.command != 'HEAD':
            self.wfile.write(body)

    def file(self, path, ctype):
        """A file with byte ranges, so the video seeks."""
        size = path.stat().st_size
        start, end, code = 0, size - 1, 200
        m = re.match(r'bytes=(\d*)-(\d*)$', self.headers.get('Range', ''))
        if m and (m.group(1) or m.group(2)):
            if m.group(1):
                start = int(m.group(1))
                end = min(int(m.group(2)), size - 1) if m.group(2) else size - 1
            else:
                start = max(0, size - int(m.group(2)))
            if start > end:
                return self.send(416, extra={'Content-Range': f'bytes */{size}'})
            code = 206
        self.send_response(code)
        self.send_header('Content-Type', ctype)
        self.send_header('Accept-Ranges', 'bytes')
        self.send_header('Content-Length', str(end - start + 1))
        if code == 206:
            self.send_header('Content-Range', f'bytes {start}-{end}/{size}')
        self.end_headers()
        if self.command == 'HEAD':
            return
        with path.open('rb') as f:
            f.seek(start)
            left = end - start + 1
            try:
                while left > 0:
                    chunk = f.read(min(1 << 20, left))
                    if not chunk:
                        break
                    self.wfile.write(chunk)
                    left -= len(chunk)
            except (BrokenPipeError, ConnectionResetError):
                pass

    def route(self):
        """/t/<story>/<scene>/[<cut>/]<rest> -> (timeline, rest), or (None, None)."""
        parts = [unquote(x) for x in self.path.split('?')[0].split('/')]
        if len(parts) < 4 or parts[1] != 't':
            return None, None
        story, scene, tail = parts[2], parts[3], parts[4:]
        # a cut name is the next part unless it is the page's own path (media, _notes, or the page itself)
        cut = tail[0] if tail and tail[0] not in ('', 'media', '_notes', 'index.html') else ''
        rest = '/'.join(tail[1:] if cut else tail)
        t = resolve(story, scene, cut)
        if t:
            t['base'] = f'/t/{story}/{scene}/' + (f'{cut}/' if cut else '')
        return t, rest

    def notes_dir(self, t):
        return t['dir'] / 'feedback' / 'timeline-local' / t['cut'] / 'notes'

    def do_HEAD(self):
        self.do_GET()

    def do_GET(self):
        p = self.path.split('?')[0]
        if p == '/':
            return self.send(200, index_page().encode(), 'text/html; charset=utf-8')
        if p == '/_local/claude.js':
            return self.send(200, (SHIM % (json.dumps(ME), json.dumps({**PEOPLE, ME: a.who}))).encode(), 'text/javascript')
        if p == '/favicon.ico':
            return self.send(204)
        t, rest = self.route()
        if not t:
            return self.send(404, b'No such timeline. See http://localhost:%d/' % a.port)
        if not p.endswith('/') and rest == '':
            return self.send(301, extra={'Location': t['base']})
        if rest in ('', 'index.html'):
            try:
                ensure_built(t)
            except RuntimeError as e:
                return self.send(500, f'This timeline did not build:\n\n{e}'.encode())
            page = (t['out'] / 'index.html').read_text()
            return self.send(200, (SKELETON + page + '</body></html>').encode(), 'text/html; charset=utf-8')
        if rest == '_notes':
            d, notes = self.notes_dir(t), []
            for f in sorted(d.glob('*.json')) if d.exists() else []:
                try:
                    notes.append(json.loads(f.read_text()))
                except ValueError:
                    pass
            return self.send(200, json.dumps(notes).encode(), 'application/json')
        if rest == 'media/cut.mp4':
            return self.file(t['preview'], 'video/mp4')
        if re.fullmatch(r'media/[\w.-]+\.jpg', rest) and (t['out'] / rest).exists():
            return self.file(t['out'] / rest, 'image/jpeg')
        return self.send(404, b'not found')

    def note_file(self):
        t, rest = self.route()
        if not t or not rest.startswith('_notes/'):
            return None
        doc = rest[len('_notes/'):]
        if not NAME.match(doc) or not doc.endswith('__' + ME):
            return None  # only your own notes, and only plain names
        return self.notes_dir(t) / f'{doc}.json'

    def do_PUT(self):
        f = self.note_file()
        if not f:
            return self.send(403, b'not your note')
        try:
            v = json.loads(self.rfile.read(int(self.headers.get('Content-Length', 0))))
        except ValueError:
            return self.send(400, b'bad json')
        v['by'] = ME
        f.parent.mkdir(parents=True, exist_ok=True)
        tmp = f.with_suffix('.tmp')
        tmp.write_text(json.dumps(v, indent=2, sort_keys=True, ensure_ascii=False) + '\n')
        os.replace(tmp, f)
        self.send(200, b'{}', 'application/json')

    def do_DELETE(self):
        f = self.note_file()
        if not f:
            return self.send(403, b'not your note')
        if f.exists():
            # nothing is deleted: a cleared slip's last text is kept beside the live notes
            old = f.parent.parent / 'cleared'
            old.mkdir(exist_ok=True)
            os.replace(f, old / f'{f.stem}.{int(f.stat().st_mtime)}.json')
        self.send(200, b'{}', 'application/json')


srv = ThreadingHTTPServer(('127.0.0.1', a.port), H)
print(f'Timelines: http://localhost:{a.port}  (notes signed {a.who})', flush=True)
if a.open:
    subprocess.Popen([str(HERE.parent / 'open-in-windows.sh'), f'http://localhost:{a.port}/t/{a.open.strip("/")}/'])
srv.serve_forever()
