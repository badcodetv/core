"""Shared loader for a scene folder (the new-scene skill).

A scene folder is docs/stories/<story>/scenes/<scene>/ and holds:
  scene.json              config: titles, media root, Flow project, beats, "video" settings (see SKILL.md)
  brief.md                stage 1: the interview's outcome
  moodboard.json          stage 2: rows [beat, id, look, prompt, style?]
  storyboard.json         stage 2: {acts, frames:[{n, act, title, look, line?, stills, anim}]}
  animation-options.json  stage 3: {sequence_notes, frames:[{n, job, options:[{id, label, veo_prompt?, ...}]}]}
  video-jobs.json         stage 3: picks turned into Flow jobs (see shots.py)
  picks.md                the running record of every pick and ruling

Media lives outside the repo at scene.json's "media" (clips/ convention): moodboard/, video/.

Video settings (stage 3) are the STORY'S choice, read from its look.md and written into scene.json
(design/2026-10-29-style-leak-audit.md §1 — until then run.mts forced one story's settings on all):
  "video": {"model": "<Flow menu name>", "aspect": "16:9" | "9:16", "mode": "Frames", "duration": 8}
video-jobs.json may override any of them with its own "video" block (or a top-level "duration"),
and an "extra" job may carry its own "duration". A missing field is an error, never a default.
"""
import base64
import io
import json
import pathlib
import sys

REPO = pathlib.Path(__file__).resolve().parents[2]


class Scene:
    def __init__(self, path):
        self.dir = pathlib.Path(path).resolve()
        if not (self.dir / 'scene.json').exists():
            sys.exit(f'no scene.json in {self.dir}')
        self.cfg = json.loads((self.dir / 'scene.json').read_text())
        self.slug = self.cfg.get('scene', self.dir.name)
        self.prefix = self.cfg.get('prefix', self.slug)
        self.media = pathlib.Path(self.cfg['media'])
        self.moodboard = self.media / 'moodboard'
        self.video = self.media / 'video'

    def load(self, name, default=None):
        p = self.dir / name
        return json.loads(p.read_text()) if p.exists() else default

    def still(self, sid):
        """A still by id, from moodboard/ or its current/ and text/ subfolders."""
        for d in ('.', 'current', 'text'):
            p = self.moodboard / d / f'{sid}.jpg'
            if p.exists():
                return p
        return None


VIDEO_FIELDS = ('model', 'aspect', 'mode', 'duration')
VIDEO_MODES = ('Frames',)  # run.mts fills the Start frame slot; it does not drive Ingredients


def video_settings(scene, jobs=None):
    """The scene's Flow video settings: scene.json "video", overridden by video-jobs.json "video".

    Exits with a clear message when any field is missing: there is no default model, aspect, mode
    or length. They come from the story's look.md (docs/stories/STYLE.md)."""
    jobs = scene.load('video-jobs.json', {}) if jobs is None else jobs
    v = {**(scene.cfg.get('video') or {}), **(jobs.get('video') or {})}
    if 'duration' not in v and 'duration' in jobs:
        v['duration'] = jobs['duration']
    missing = [f for f in VIDEO_FIELDS if v.get(f) in (None, '')]
    if missing:
        sys.exit(f"{scene.dir / 'scene.json'}: no video {', '.join(missing)}. Add "
                 '"video": {"model": …, "aspect": "16:9"|"9:16", "mode": "Frames", "duration": <s>} '
                 "from the story's look.md (docs/stories/STYLE.md). There is no default.")
    if v['aspect'] not in ('16:9', '9:16'):
        sys.exit(f"video aspect {v['aspect']!r} is not 16:9 or 9:16")
    if v['mode'] not in VIDEO_MODES:
        sys.exit(f"video mode {v['mode']!r}: scripts/scene/run.mts only drives {', '.join(VIDEO_MODES)}")
    v['duration'] = int(v['duration'])
    return {f: v[f] for f in VIDEO_FIELDS}


def data_uri(path, width):
    from PIL import Image
    im = Image.open(path).convert('RGB')
    if im.width > width:
        im = im.resize((width, round(im.height * width / im.width)), Image.LANCZOS)
    buf = io.BytesIO()
    im.save(buf, 'JPEG', quality=76, optimize=True)
    return 'data:image/jpeg;base64,' + base64.b64encode(buf.getvalue()).decode()
