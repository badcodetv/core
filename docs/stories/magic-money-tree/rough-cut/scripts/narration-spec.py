#!/usr/bin/env python3
"""Build a SunoSpec for one Magic Money Tree narration part, straight from the live sheet
(songs/narration.md): the template with its palette, arc and ending filled; the shared Exclude box;
the part's lyrics block; and the house settings in the sheet's §2.

    narration-spec.py P1 A voice   > /tmp/mmt-P1-A-voice.json     # palette A, with badcode newsreader
    narration-spec.py P1 C novoice > /tmp/mmt-P1-C-novoice.json   # palette C, no Voice (Male)
    narration-spec.py --round1                                    # writes all six round-1 specs to /tmp/mmt-specs/

Then (phase 2 is authorised; each Create costs 10 credits and makes two takes):
    npx tsx scripts/suno/suno.mts pair /tmp/mmt-P1-A-voice.json
The spec's single weirdness (25, the house) makes `pair` one Create, not two.
Nothing is ever downloaded by script; the takes are recorded from preview (house rule).
"""
import json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
SHEET = os.path.normpath(os.path.join(HERE, "..", "..", "songs", "narration.md"))
VOICE = "badcode newsreader"          # the LIVE display name of GPOM's saved Voice
WORKSPACE = "magic-money-tree"
DURATION = {"P1": 65, "P2": 95, "P3": 50, "P4": 85, "P5": 75, "P6": 110, "P7": 110, "P8": 85, "P9": 100, "P10": 20}


def sheet():
    t = open(SHEET).read()
    template = re.search(r"```template\n(.*?)\n```", t, re.S).group(1).strip()
    pal = {}
    for m in re.finditer(r"^\| \*\*([ABC]) · [^|]+\*\* \| (.+?) \|", t, re.M):
        pal[m.group(1)] = m.group(2).strip()
    endings = {k: v for k, v in re.findall(r"\*\*(hollow|resolve):\*\* `(.+?)`", t)}
    exclude = re.search(r"\*\*The Exclude box[^\n]*\n\n```\n(.*?)\n```", t, re.S).group(1).strip()
    parts = {}
    for m in re.finditer(r"^### (P\d+) · (.+?)\n(.*?)(?=^### P\d+|^## )", t, re.S | re.M):
        body = m.group(3)
        parts[m.group(1)] = {
            "arc": re.search(r"`\{\{ARC\}\}`: (.+)", body).group(1).strip(),
            "ending": re.search(r"`\{\{ENDING\}\}`: (.+)", body).group(1).strip(),
            "lyrics": re.search(r"```lyrics\n(.*?)```", body, re.S).group(1).rstrip("\n"),
        }
    return template, pal, endings, exclude, parts


def build(part, palette, voice):
    template, pal, endings, exclude, parts = sheet()
    p = parts[part]
    style = (template.replace("{{PALETTE}}", pal[palette]).replace("{{ARC}}", p["arc"])
             .replace("{{ENDING}}", endings.get(p["ending"]) or re.search(r"`(.+?)`", p["ending"]).group(1)))
    spec = {
        "style": style, "exclude": exclude, "lyrics": p["lyrics"],
        "title": f"mmt-{part}-{palette}-{'voice' if voice else 'novoice'}",
        "workspace": WORKSPACE, "mode": "custom", "model": "v6",
        "variety": "off", "maxMode": False, "personalize": False,
        "styleInfluence": 50, "weirdness": [25], "durationSec": DURATION[part],
    }
    if voice:
        spec.update(voice=VOICE, audioInfluence=65, vocalGender=None)
    else:
        spec["vocalGender"] = "male"
    return spec


if __name__ == "__main__":
    a = sys.argv[1:]
    if a == ["--round1"]:
        os.makedirs("/tmp/mmt-specs", exist_ok=True)
        for pl in "ABC":
            for v in (True, False):
                s = build("P1", pl, v)
                path = f"/tmp/mmt-specs/{s['title']}.json"
                json.dump(s, open(path, "w"), indent=2, ensure_ascii=False)
                print(path)
    elif len(a) == 3 and a[2] in ("voice", "novoice"):
        print(json.dumps(build(a[0], a[1], a[2] == "voice"), indent=2, ensure_ascii=False))
    else:
        sys.exit(__doc__)
