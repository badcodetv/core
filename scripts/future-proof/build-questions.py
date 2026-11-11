#!/usr/bin/env python3
"""Build the public Future Proof questions page (GOVT 2 on badcode.tv) from its prototype.

  python3 scripts/future-proof/build-questions.py
  node apps/site/build.mjs

Source: design/2026-11-11-future-proof-simple/index.html (also the artifact page Kai notes on,
https://claude.ai/artifact/LWVX8GbT8ZyNH9qvzmaewz). The public copy drops the wording-options box,
always uses the first option of each list (Kai's picks), gets a full document skeleton, and shows a
"Back to the TV" link when opened on its own (not inside the TV's iframe).
"""
import re, pathlib, sys
ROOT = pathlib.Path(__file__).resolve().parents[2]
SRC = ROOT / "design/2026-11-11-future-proof-simple/index.html"
OUT = ROOT / "apps/site/public/future-proof/questions/index.html"
s = SRC.read_text()

def sub(pat, rep, flags=re.S | re.M):
    global s
    s, n = re.subn(pat, rep, s, flags=flags)
    if n != 1: sys.exit(f"build-questions: expected one match for {pat!r}, got {n}")

sub(r'\n\s*<details class="words" id="words">.*?</details>', '')                 # the wording box
sub(r'try\{Object\.assign\(pick,JSON\.parse\(localStorage[^\n]*\n', '')        # no remembered picks
sub(r'\n  drawOpts\(id\);', '\n ')                                              # nothing to draw
sub(r'(<a class="mark" href="#home">Future Proof</a>)',
    r'\1<a class="totv" id="totv" href="/future-proof/" hidden>◀ Back to the TV</a>')
sub(r'^(\.mark\{)', r'.totv{font-family:var(--mono);font-weight:700;font-size:12px;letter-spacing:.08em;text-transform:uppercase;margin-right:auto;margin-left:16px}\n\1')
sub(r'(addEventListener\("hashchange",route\);route\(\);)',
    r'try{if(window.top===window)document.getElementById("totv").hidden=false}catch(e){}\n\1')
head = ('<!doctype html>\n<html lang="en-GB">\n<head>\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n'
        '<meta name="description" content="Future Proof: three questions about how Britain decides, and three fixes.">\n'
        '<style>[hidden]{display:none!important}body{margin:0}img{max-width:100%}</style>\n')
# everything before the first <div class="wrap"> is head material
i = s.index('<div class="wrap">')
page = head + s[:i] + '</head>\n<body>\n' + s[i:] + '\n</body>\n</html>\n'
OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(page)
print(f"wrote {OUT.relative_to(ROOT)} ({len(page)} bytes)")
