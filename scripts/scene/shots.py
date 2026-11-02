#!/usr/bin/env python3
"""A scene's Flow video jobs: the storyboard picks turned into one job per clip, for run.mts.

    python3 scripts/scene/shots.py <scene-dir>        # JSON for the runner

Video settings (model, aspect, mode, duration) come from scene.json "video" — the story's look.md
— and may be overridden here by a "video" block; see scene.video_settings. No defaults.

video-jobs.json (all fields optional):
  {
    "option": "a",                        # animation option used where a frame has no pick
    "video": {"duration": 8},             # overrides scene.json "video" (legacy: top-level "duration")
    "anim_picks":  {"2": "c"},            # frame -> option id, from the storyboard's db `picks`
    "still_picks": {"5": "TO1T-a"},       # frame -> still id (default: the frame's first still)
    "skip": [2, 9],                       # kept clips, ffmpeg or Premiere frames: no credits
    "cast": {"9": "West Country Bot"},    # frame -> Flow Character name, cast with "@"
    "extra": [                            # re-rolls and new shots after Kai's notes
      {"key": "12-r2", "n": 12, "still": "WL3-a", "duration": 4, "motion": "...", "character": null,
       "why": "Kai 17 Oct: mouth opens much less"}
    ]
  }
A frame whose picked option has no veo_prompt is a post job (Premiere camera, ffmpeg text, a hold)
and is left out. Clips land at <media>/video/<prefix>-<key>-<still>.mp4.
"""
import json
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from scene import Scene, video_settings  # noqa: E402


def shots(scene_dir):
    sc = Scene(scene_dir)
    jobs = sc.load('video-jobs.json', {})
    sb = sc.load('storyboard.json', {'frames': []})['frames']  # a scene may have extra rows only
    ao = {str(f['n']): f for f in sc.load('animation-options.json', {}).get('frames', [])}
    skip = set(jobs.get('skip', []))
    video = video_settings(sc, jobs)
    dur = video['duration']
    out = []
    for f in sb:
        n = f['n']
        if n in skip or not f.get('stills'):
            continue
        a = ao.get(str(f.get('anim', n)), {})
        oid = jobs.get('anim_picks', {}).get(str(n), jobs.get('option', 'a'))
        opt = next((o for o in a.get('options', []) if o['id'] == oid), None)
        if not opt or not opt.get('veo_prompt'):
            continue
        out.append({'key': f'{n:02d}', 'n': n, 'title': f['title'], 'option': oid, 'label': opt.get('label', ''),
                    'still': jobs.get('still_picks', {}).get(str(n), f['stills'][0]),
                    'motion': opt['veo_prompt'], 'duration': dur,
                    'character': jobs.get('cast', {}).get(str(n))})
    for e in jobs.get('extra', []):
        out.append({'title': 're-roll', 'option': None, 'label': e.get('why', 're-roll'), 'duration': dur,
                    'character': None, **e})
    for s in out:
        for k in ('model', 'aspect', 'mode'):
            s.setdefault(k, video[k])  # an "extra" job may carry its own
        src = sc.still(s['still'])
        if not src:
            sys.exit(f"{s['key']}: no still {s['still']} under {sc.moodboard}")
        s['src'] = str(src)
        s['plate'] = f"{sc.prefix}-{s['key']}-{s['still']}.jpg"
        s['out'] = str(sc.video / f"{sc.prefix}-{s['key']}-{s['still']}.mp4")
    return sorted(out, key=lambda s: s['key'])


if __name__ == '__main__':
    json.dump(shots(sys.argv[1]), sys.stdout, indent=1)
