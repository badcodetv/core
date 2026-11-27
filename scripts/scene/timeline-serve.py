#!/usr/bin/env python3
"""The timeline page, served from this machine: no claude.ai upload, no daily upload limit (Kai, 2026-11-27:
"we should be able to operate the timeline tool without needing Claude artifacts").

    python3 scripts/scene/timeline-serve.py docs/stories/<story>/scenes/<scene> [--port 8765] [--as Kai]

then open http://localhost:8765 (from Windows too: WSL forwards localhost). It is the same page as the artifact
(scripts/scene/timeline-template.html, built by build-timeline.py --local) with three differences:
- the picture is the cut's full preview (scene.json cut.preview, 1080p) streamed straight from disk, with seeking;
- notes save as files, one per note, in <scene>/feedback/timeline-local/notes/<key>__<user>.json, the same
  shape as a dump of the artifact's notes, so build-timeline.py and Claude read them with nothing in between;
- the page rebuilds itself on reload when the cut (edl, preview) or Claude's replies (cut-notes.json) change.

Only this machine can open it (it listens on 127.0.0.1). Notes are signed as --as (a name in docs/stories/people.json,
default Kai), so they carry on from the artifact page's notes.
"""
import argparse
import json
import os
import pathlib
import re
import subprocess
import sys
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent / 'drive'))
from scene import Scene  # noqa: E402
from localmap import localize  # noqa: E402

ap = argparse.ArgumentParser()
ap.add_argument('scene')
ap.add_argument('--port', type=int, default=8765)
ap.add_argument('--as', dest='who', default='Kai')
ap.add_argument('--out', help='where the local page is built (default ~/.cache/badcode-timeline/<story>-<scene>)')
a = ap.parse_args()

SC = Scene(a.scene)
SCENE_DIR = pathlib.Path(a.scene).resolve()
STORY = SCENE_DIR.parents[1].name
OUT = pathlib.Path(a.out or pathlib.Path.home() / '.cache' / 'badcode-timeline' / f'{STORY}-{SCENE_DIR.name}')
NOTES = SCENE_DIR / 'feedback' / 'timeline-local' / 'notes'
PEOPLE_FILE = SCENE_DIR.parents[2] / 'people.json'
PEOPLE = {k: v for k, v in (json.loads(PEOPLE_FILE.read_text()) if PEOPLE_FILE.exists() else {}).items() if not k.startswith('_')}
ME = next((k for k, v in PEOPLE.items() if v.lower() == a.who.lower()), 'local-' + re.sub(r'\W', '', a.who.lower()))
DOC_ID = re.compile(r'^[A-Za-z0-9_-]{1,120}$')
LOCK = threading.Lock()
built = {}


def cut_paths():
    cut = SC.cfg.get('cut', {})
    edl = pathlib.Path(localize(cut.get('edl', str(SC.media / 'cut' / 'edl.json'))))
    preview = pathlib.Path(localize(cut.get('preview', str(SC.media / 'cut' / 'preview.mp4'))))
    return edl, preview


def inputs():
    """Everything a rebuild depends on, with its modification time."""
    SC.cfg = json.loads((SCENE_DIR / 'scene.json').read_text())  # scene.json may point at a new cut since start-up
    edl, preview = cut_paths()
    files = [SCENE_DIR / 'scene.json', SCENE_DIR / 'cut-notes.json', edl, preview,
             HERE / 'timeline-template.html', HERE / 'timeline.py']
    return {str(f): f.stat().st_mtime for f in files if f.exists()}


def ensure_built():
    with LOCK:
        now = inputs()
        if now == built.get('inputs') and (OUT / 'index.html').exists():
            return
        r = subprocess.run([sys.executable, str(HERE / 'build-timeline.py'), str(SCENE_DIR), str(OUT), '--local'],
                           capture_output=True, text=True)
        if r.returncode:
            raise RuntimeError(r.stderr or r.stdout)
        built['inputs'] = now
        print('built', OUT, flush=True)


SKELETON = ('<!doctype html><html lang="en"><head><meta charset="utf-8">'
            '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">'
            '<style>body{margin:0;font:14px system-ui,sans-serif}img{max-width:100%}[hidden]{display:none!important}</style>'
            '<script src="/_local/claude.js"></script></head><body>')

# window.claude, as much of it as the timeline page uses: use('db') and use('user'), backed by this server.
SHIM = """
(() => {
  const ME = %s, NAMES = %s;
  const api = (p, o) => fetch('/_local/notes' + p, o).then(r => { if (!r.ok) throw Object.assign(new Error(r.statusText), { code: r.status }); return r });
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

    def do_HEAD(self):
        self.do_GET()

    def do_GET(self):
        p = self.path.split('?')[0]
        if p in ('/', '/index.html'):
            try:
                ensure_built()
            except RuntimeError as e:
                return self.send(500, f'The page did not build:\n\n{e}'.encode())
            html = (OUT / 'index.html').read_text()
            return self.send(200, (SKELETON + html + '</body></html>').encode(), 'text/html; charset=utf-8')
        if p == '/_local/claude.js':
            names = {**PEOPLE, ME: a.who}
            return self.send(200, (SHIM % (json.dumps(ME), json.dumps(names))).encode(), 'text/javascript')
        if p == '/_local/notes':
            notes = []
            for f in sorted(NOTES.glob('*.json')) if NOTES.exists() else []:
                try:
                    notes.append(json.loads(f.read_text()))
                except ValueError:
                    pass
            return self.send(200, json.dumps(notes).encode(), 'application/json')
        if p == '/media/cut.mp4':
            return self.file(cut_paths()[1], 'video/mp4')
        if re.fullmatch(r'/media/[\w.-]+\.jpg', p) and (OUT / p[1:]).exists():
            return self.file(OUT / p[1:], 'image/jpeg')
        return self.send(404, b'not found')

    def note_path(self):
        doc = self.path.split('?')[0].removeprefix('/_local/notes/')
        from urllib.parse import unquote
        doc = unquote(doc)
        if not DOC_ID.match(doc) or not doc.endswith('__' + ME):
            return None  # only your own notes, and only plain names
        return NOTES / f'{doc}.json'

    def do_PUT(self):
        f = self.note_path()
        if not f:
            return self.send(403, b'not your note')
        try:
            v = json.loads(self.rfile.read(int(self.headers.get('Content-Length', 0))))
        except ValueError:
            return self.send(400, b'bad json')
        v['by'] = ME
        NOTES.mkdir(parents=True, exist_ok=True)
        tmp = f.with_suffix('.tmp')
        tmp.write_text(json.dumps(v, indent=2, sort_keys=True, ensure_ascii=False) + '\n')
        os.replace(tmp, f)
        self.send(200, b'{}', 'application/json')

    def do_DELETE(self):
        f = self.note_path()
        if not f:
            return self.send(403, b'not your note')
        if f.exists():
            # notes are never deleted from the record: a cleared slip is kept beside the live ones
            old = NOTES.parent / 'cleared'
            old.mkdir(exist_ok=True)
            os.replace(f, old / f'{f.stem}.{int(f.stat().st_mtime)}.json')
        self.send(200, b'{}', 'application/json')


ensure_built()
print(f'Timeline for {SCENE_DIR.relative_to(SCENE_DIR.parents[3])}: http://localhost:{a.port}  (notes in {NOTES}, signed {a.who})', flush=True)
ThreadingHTTPServer(('127.0.0.1', a.port), H).serve_forever()
