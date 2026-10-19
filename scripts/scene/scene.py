"""Shared loader for a scene folder (the new-scene skill).

A scene folder is docs/stories/<story>/scenes/<scene>/ and holds:
  scene.json              config: titles, media root, Flow project, beats (see SKILL.md)
  brief.md                stage 1: the interview's outcome
  moodboard.json          stage 2: rows [beat, id, look, prompt, style?]
  storyboard.json         stage 2: {acts, frames:[{n, act, title, look, line?, stills, anim}]}
  animation-options.json  stage 3: {sequence_notes, frames:[{n, job, options:[{id, label, veo_prompt?, ...}]}]}
  video-jobs.json         stage 3: picks turned into Flow jobs (see shots.py)
  picks.md                the running record of every pick and ruling

Media lives outside the repo at scene.json's "media" (clips/ convention): moodboard/, video/.
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


def data_uri(path, width):
    from PIL import Image
    im = Image.open(path).convert('RGB')
    if im.width > width:
        im = im.resize((width, round(im.height * width / im.width)), Image.LANCZOS)
    buf = io.BytesIO()
    im.save(buf, 'JPEG', quality=76, optimize=True)
    return 'data:image/jpeg;base64,' + base64.b64encode(buf.getvalue()).decode()
