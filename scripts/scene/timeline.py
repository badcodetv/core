"""The timeline page (new-scene stage 4): a rough cut shown as a playable, notable Premiere-style timeline.

Input is one dict in the TIMELINE FORMAT, which a scene's assembler writes as `<media>/cut/edl.json`:

  {
    "sequence": "gpom-second-half-rough2",       # what the cut is called (and its Premiere sequence, if built)
    "title": "Cut 2 Timeline", "heading": "...", "intro": "...",   # optional page words
    "fps": 24, "total": 246.6,                   # seconds
    "beats":  [{"id": "0", "title": "...", "start": 0.0, "dur": 43.2, "see": "...", "act": "...",
                "lines": [{"i": 0, "who": "bot", "name": "Maddie", "t": 2.4, "dur": 3.2,   # t null = no take of its own
                           "text": "Oh, hello!", "by": "kai|claude"}]}],
    "video":  [{"file": ".../rt2/x.mp4", "start": 0.0, "dur": 4.0, "beat": "0",
                "source": ".../x.mp4", "looped": false}],          # looped = ping-ponged to fill time
    "audio":  [{"track": "A1", "name": "vox-ai"}],                  # kind = name before the first '-': vox, mus or sfx
    "events": [{"stem": "vox-ai", "t": 2.4, "dur": 3.2, "what": "beat 0 line 0", "src": ".../00-0-bot.wav"}],
    "flags":  ["substitutions and doubts, one sentence each"]
  }

`build(data, preview, out)` writes out/index.html, out/media/cut.mp4 (a proxy under the 15 MB artifact file
limit) and a thumbnail per clip. Publish out/index.html with every file in out/media/ and
`capabilities: {db:{}, user:{}}`. Notes land in db collection `notes`, doc `<key>__<user>`, key `top`,
`b<beat>`, `l<beat>-<i>`, `c<clip>`, `e<event>` or `at<frame>` (pinned to a frame; doc also has tc, beat).
"""
import json
import pathlib
import subprocess

HERE = pathlib.Path(__file__).resolve().parent


def _ff(*a):
    subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', *map(str, a)], check=True)


def build(data, preview, out):
    preview, out = pathlib.Path(preview), pathlib.Path(out)
    media = out / 'media'
    media.mkdir(parents=True, exist_ok=True)
    proxy = media / 'cut.mp4'
    if not proxy.exists() or proxy.stat().st_mtime < preview.stat().st_mtime:
        # ~300 kb/s keeps a 5-minute cut under the 15 MB file limit; longer cuts need a lower rate.
        kbps = max(120, min(300, int(15e6 * 8 / 1000 / max(data['total'], 1)) - 90))
        _ff('-i', preview, '-vf', 'scale=640:-2', '-c:v', 'libx264', '-preset', 'slow', '-b:v', f'{kbps}k',
            '-maxrate', f'{int(kbps * 1.2)}k', '-bufsize', f'{kbps * 2}k', '-pix_fmt', 'yuv420p',
            '-c:a', 'aac', '-b:a', '64k', '-ac', '2', '-movflags', '+faststart', proxy)
    clips = []
    for k, c in enumerate(data['video']):
        th = media / f'c{k:02d}.jpg'
        if not th.exists() or th.stat().st_mtime < preview.stat().st_mtime:
            _ff('-ss', c['start'] + min(c['dur'] / 2, 1.5), '-i', preview, '-frames:v', '1', '-vf', 'scale=160:-2', '-q:v', '5', th)
        clips.append({'k': k, 't': c['start'], 'd': c['dur'], 'beat': c['beat'],
                      'name': pathlib.Path(c.get('source') or c['file']).name,
                      'looped': bool(c.get('looped')), 'img': f'media/{th.name}'})
    beats = [{'id': b['id'], 'title': b['title'], 't': b['start'], 'd': b['dur'], 'see': b.get('see', ''),
              'act': b.get('act', ''), 'lines': [{**ln, 'd': ln.get('dur', 0)} for ln in b.get('lines', [])]}
             for b in data['beats']]
    tracks = [{'track': a['track'], 'name': a['name'].split('-', 1)[-1], 'kind': a['name'].split('-')[0],
               'events': [{'k': k, 't': e['t'], 'd': e['dur'], 'what': e['what'], 'src': pathlib.Path(e['src']).name}
                          for k, e in enumerate(data['events']) if e['stem'] == a['name']]}
              for a in data['audio']]
    seq = data.get('sequence', 'rough cut')
    page = {'total': data['total'], 'fps': data.get('fps', 24), 'beats': beats, 'clips': clips, 'tracks': tracks,
            'flags': data.get('flags', []), 'sequence': seq,
            'heading': data.get('heading', seq),
            'intro': data.get('intro', f'The {seq} cut. Play it, click any beat, clip, line or sound, and leave a note '
                                        "in its yellow slip. Notes save as you type. Tell Claude when you're done.")}
    html = (HERE / 'timeline-template.html').read_text()
    html = html.replace('<title>Cut Timeline</title>', f"<title>{data.get('title', 'Cut Timeline')}</title>", 1)
    (out / 'index.html').write_text(html.replace('/*DATA*/null', json.dumps(page, ensure_ascii=False)))
    return {'beats': len(beats), 'clips': len(clips), 'tracks': len(tracks), 'events': len(data['events']),
            'proxyMB': round(proxy.stat().st_size / 1e6, 1), 'files': sorted(f'media/{p.name}' for p in media.iterdir())}
