#!/usr/bin/env python3
"""Build the GPOM second-half storyboard page: frames in story order, each with its still(s) and
animation options from the cinematography pass.

Usage: python3 scripts/gpom/build-storyboard.py <storyboard.json> <animation-options.json> <clips-root> <out.html>
Stills come from <clips-root>/second-half/moodboard/<id>.jpg or .../storyboard/<id>.jpg.
"""
import base64, io, json, pathlib, sys
from PIL import Image

HERE = pathlib.Path(__file__).parent


def data_uri(path, width):
    im = Image.open(path).convert("RGB")
    if im.width > width:
        im = im.resize((width, round(im.height * width / im.width)), Image.LANCZOS)
    buf = io.BytesIO()
    im.save(buf, "JPEG", quality=76)
    return "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode()


def main(sb_path, anim_path, clips, out):
    sb = json.loads(pathlib.Path(sb_path).read_text())
    anim = json.loads(pathlib.Path(anim_path).read_text())
    by_n = {str(f["n"]): f for f in anim.get("frames", [])}
    root = pathlib.Path(clips) / "second-half"
    images = {}
    for f in sb["frames"]:
        f["anim"] = by_n.get(str(f.get("anim", f["n"])), {})
        for sid in f["stills"]:
            for d in ("storyboard", "moodboard"):
                p = root / d / f"{sid}.jpg"
                if p.exists():
                    images[sid] = data_uri(p, 1100)
                    break
            else:
                print("missing still:", sid, file=sys.stderr)
    payload = {"acts": sb["acts"], "frames": sb["frames"], "notes": anim.get("sequence_notes", []), "img": images}
    html = (HERE / "storyboard-template.html").read_text()
    html = html.replace("/*DATA*/null", json.dumps(payload, ensure_ascii=False).replace("</", "<\\/"))
    pathlib.Path(out).write_text(html)
    print(f"{out}: {len(sb['frames'])} frames, {len(images)} stills, {len(html) / 1e6:.1f} MB")


if __name__ == "__main__":
    main(*sys.argv[1:5])
