#!/usr/bin/env python3
"""Is each timeline page's Premiere sequence still what the page says? One line per scene.

    python3 scripts/scene/premiere-check.py docs/stories/<story> [--write]

For every scene in the story's timelines.json whose scene.json names a current Premiere build
(premiere.current -> premiere.<round>.sequence + .edl), compare the bridge's last state dump of that
sequence (<project dir>/.bridge/state-<sequence>.json, written by premiere_get_sequence) with the edl
the page was built from:
  in sync        V1 shots, their start/in/dur and the total match the edl, and nobody added effects
                 (effects are only seen in a dump read with params on)
  page ahead     the edl changed after the sequence was built (notes answered, not yet in Premiere)
  edited in Pr   the sequence differs from the edl: Kai worked on it by hand, so never rebuild over it
  no state       no dump yet: call premiere_get_sequence({name, params:false}) first
  Premiere ahead differs from the edl, but on purpose: the round record carries `premiere_ahead`
                 (why, in words: Kai's hand edits kept in Premiere, an effect only Premiere can do)
  Premiere only  the scene's cut file is not a timeline edl (a hand cut with no timeline page),
                 so there is nothing to compare: Premiere is the truth
The state dump is only as fresh as the last get_sequence call, so read every sequence just before
running this. --write stores the result on the round record (premiere.<round>.check), which the
overview board shows.
"""
import json
import subprocess
import os
import pathlib
import sys
from datetime import datetime
import os as _os, sys as _sys  # cut files written on another machine open on this one (scripts/drive/localmap.py)
_sys.path.insert(0, _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', 'drive'))
from localmap import localize  # noqa: E402


# Every clip carries these built-in slots (a dump read with params on lists them). They are not
# effects anyone added; they count only once a value moves off its default or gets keyframes.
# (2026-11-10: GPOM E r3 read "26 effects added" = 5 x Opacity+Motion + 8 x Volume+Channel Volume.)
_ZERO_DB = 0.17782793939113617
_DEFAULTS = {
    'AE.ADBE Opacity': {'Opacity': 100},
    'AE.ADBE Motion': {'Position': [0.5, 0.5], 'Scale': 100, 'Scale Width': 100, 'Rotation': 0,
                       'Anchor Point': [0.5, 0.5], 'Anti-flicker Filter': 0, 'Crop Left': 0,
                       'Crop Top': 0, 'Crop Right': 0, 'Crop Bottom': 0},
    'Internal Volume Stereo': {'Level': _ZERO_DB, 'Mute': False},
    'Internal Channel Volume Stereo': None,  # every channel at 0 dB
}


def _close(a, b):
    if isinstance(a, list) and isinstance(b, list):
        return len(a) == len(b) and all(_close(x, y) for x, y in zip(a, b))
    if isinstance(a, (int, float)) and isinstance(b, (int, float)) and not isinstance(a, bool):
        return abs(a - b) < 1e-3
    return a == b


def _added(comp):
    """True if this component is a real effect, or a built-in slot Kai has changed."""
    d = _DEFAULTS.get(comp.get('matchName'), 'none')
    if d == 'none':
        return True
    for p in comp.get('params', []):
        if p.get('keyframes'):
            return True
        if d is None:
            if isinstance(p.get('value'), (int, float)) and not isinstance(p['value'], bool) \
                    and not _close(p['value'], _ZERO_DB):
                return True
        elif p.get('name') in d and not _close(p.get('value'), d[p['name']]):
            return True
    return False


def _trimmed(path, x):
    # the edl's 'in' points into the original source but 'file' is the trimmed piece: then in-point 0 is right
    try:
        d = float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', path],
                                 capture_output=True, text=True).stdout)
    except ValueError:
        return False
    return x['in'] + x['dur'] > d + 0.02


def check(rec, scene_dir=None):
    edl_p = pathlib.Path(rec['edl'])
    if not edl_p.is_absolute() and scene_dir is not None:  # a cut file named relative to its scene folder
        edl_p = scene_dir / edl_p
    st_p = pathlib.Path(rec['project']).parent / '.bridge' / f'state-{rec["sequence"]}.json'
    if not st_p.exists():
        return 'no state', ''
    edl = localize(json.loads(edl_p.read_text()))
    if 'video' not in edl:
        return 'Premiere only', f'{edl_p.name} is not a timeline edl: Kai\'s cut in Premiere is the truth'
    st = localize(json.loads(st_p.read_text()))
    v1 = st['videoTracks'][0]['items']
    diffs = []
    if len(v1) != len(edl['video']):
        diffs.append(f'{len(v1)} shots on V1, edl has {len(edl["video"])}')
    for i, (c, x) in enumerate(zip(v1, edl['video'])):
        if c['name'].replace('-noaudio', '') != os.path.basename(x['file']):
            diffs.append(f'shot {i + 1} is {c["name"]}, edl has {os.path.basename(x["file"])}')
        elif max(abs(c['start'] - x['start']), abs(c['duration'] - x['dur']),
                 min(abs(c['inPoint'] - x['in']), abs(c['inPoint']) if c.get('mediaPath') and _trimmed(c['mediaPath'], x) else 99)) > 0.05:
            diffs.append(f'shot {i + 1} retimed')
    if abs(st['sequence']['end'] - edl['total']) > 0.05:
        diffs.append(f'length {st["sequence"]["end"]:.2f}s, edl {edl["total"]:.2f}s')
    fx = sum(_added(x) for t in st['videoTracks'] + st['audioTracks'] for c in t['items']
             for x in c.get('components', []))
    if fx:
        diffs.append(f'{fx} effects added')
    if diffs:
        if rec.get('premiere_ahead'):
            return 'Premiere ahead', rec['premiere_ahead'] + ' (' + '; '.join(diffs[:4]) + ')'
        return 'edited in Pr', '; '.join(diffs[:4])
    built = rec.get('built_at') or rec.get('built', '')
    edl_t = datetime.fromtimestamp(edl_p.stat().st_mtime).isoformat(timespec='minutes')
    if built and edl_t[:len(built)] > built:
        return 'page ahead', f'edl changed {edl_t}'
    return 'in sync', ''


def scenes(story):
    t = json.loads((story / 'timelines.json').read_text())
    for s in t['sections']:
        for p in [s] + s.get('parts', []):
            if p.get('scene') and (story / p['scene'] / 'scene.json').exists():
                yield p, story / p['scene'] / 'scene.json'


def main(argv):
    story = pathlib.Path(argv[0]).resolve()
    write = '--write' in argv
    for part, path in scenes(story):
        raw = path.read_text()
        cfg = json.loads(raw)
        pr = cfg.get('premiere') or {}
        cur = pr.get('current')
        if not cur:
            continue
        rec = localize(dict(pr[cur]))  # translated copy only: cfg is written back untouched
        rec.setdefault('project', next((r['project'] for r in pr.values() if isinstance(r, dict) and r.get('project')), ''))
        state, why = check(rec, path.parent)
        print(f'{part["id"]:<12} {rec["sequence"]:<20} {state:<13} {why}')
        if write:
            pr[cur]['check'] = {'at': datetime.now().isoformat(timespec='minutes'), 'state': state, 'why': why}
            indent = len(raw.split('\n')[1]) - len(raw.split('\n')[1].lstrip())
            path.write_text(json.dumps(cfg, indent=indent or 2, ensure_ascii=False) + '\n')


if __name__ == '__main__':
    main(sys.argv[1:])
