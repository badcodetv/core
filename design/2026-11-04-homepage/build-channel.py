#!/usr/bin/env python3
"""Builds channel-badcode.html from channel-badcode.src.html, inlining small copies of the story stills.
Run from the repo root: python3 design/2026-11-04-homepage/build-channel.py (needs ffmpeg)."""
import base64, pathlib, subprocess, tempfile
here = pathlib.Path(__file__).parent
stills = here.parents[1] / 'apps/site/public/stills'
src = (here / 'channel-badcode.src.html').read_text()
for key, name in [('gpom', 'git-push-origin-master'), ('camping', 'camping'), ('karen', 'karen')]:
    with tempfile.TemporaryDirectory() as t:
        out = pathlib.Path(t) / 's.webp'
        subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', '-i', str(stills / f'{name}.webp'), '-vf', 'scale=640:-1', '-quality', '60', str(out)], check=True)
        src = src.replace('{{STILL_%s}}' % key, 'data:image/webp;base64,' + base64.b64encode(out.read_bytes()).decode())
(here / 'channel-badcode.html').write_text(src)
print('wrote', here / 'channel-badcode.html', len(src), 'bytes')
