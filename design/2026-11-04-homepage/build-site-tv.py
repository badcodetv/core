#!/usr/bin/env python3
"""Builds the deployable test TV at apps/site/public/tv/index.html from channel-badcode.src.html:
drops the ideas-and-votes section, points the stills at the site's own /stills files, adds a head.
Run from the repo root: python3 design/2026-11-04-homepage/build-site-tv.py"""
import pathlib, re
here = pathlib.Path(__file__).parent
site = here.parents[1] / 'apps/site/public'
s = (here / 'channel-badcode.src.html').read_text()
s = re.sub(r'<section class="ideas">.*?</section>\n', '', s, flags=re.S)
s = re.sub(r'/\* ===== ideas and votes ===== \*/.*?(\}\)\(\);\n</script>)', r'\1', s, flags=re.S)
s = s.replace(' Under the set are all the ideas for growing this, to vote on.', '')
for key, name in [('gpom', 'git-push-origin-master'), ('camping', 'camping'), ('karen', 'karen')]:
    s = s.replace('{{STILL_%s}}' % key, f'/stills/{name}.webp')
assert '{{' not in s and 'claude.use' not in s
head = ('<!doctype html>\n<html lang="en-GB">\n<head>\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n'
        '<meta name="robots" content="noindex">\n<link rel="icon" href="/favicon.svg" type="image/svg+xml">\n')
title_end = s.index('</title>') + len('</title>')
style_end = s.index('</style>') + len('</style>')
s = head + s[:style_end] + '\n<style>html,body{margin:0}img{max-width:100%}[hidden]{display:none!important}</style>\n</head>\n<body>\n' + s[style_end:] + '\n</body>\n</html>\n'
out = site / 'tv' / 'index.html'
out.parent.mkdir(exist_ok=True)
out.write_text(s)
print('wrote', out, len(s), 'bytes')
