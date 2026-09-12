#!/usr/bin/env python3
"""Build a SunoSpec for one GPOM narration atom, straight out of the v6 sheet.

The three prompt boxes are never retyped: they come from
`suno.mts extract`, so the spec cannot drift from the sheet. Everything else
(model, the v6 controls, the Voice, the duration, the workspace, the title) is
the per-atom settings table below, which mirrors §3 of

    docs/stories/gitpush-origin-master/songs/narration-v6.md

Usage:
    python3 scripts/suno/gpom-narration-spec.py cut1-voice > /tmp/c1voice.json

Then, and only with Kai's yes for that round:
    npx tsx scripts/suno/suno.mts explore /tmp/c1voice.json --round 1          # dry run, spends nothing
    npx tsx scripts/suno/suno.mts explore /tmp/c1voice.json --round 1 --yes    # spends credits
"""
import json
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
SHEET = REPO / "docs/stories/gitpush-origin-master/songs/narration-v6.md"
VOICE = "badcode newsreader"  # 🔴 the LIVE display name. Never the internal label, never just "badcode".
WORKSPACE = "gpom-story"

# durationSec: None means Auto. A bed is flat and loopable, so its length does not matter.
# voice: beds get NO Voice — a vocal persona is exactly what a bed is written to repel.
ATOMS = {
    "cut1-voice": {"title": "gpom-c1voice-v6A", "durationSec": 70, "voice": VOICE},
    "cut1-bed": {"title": "gpom-c1bed-v6A", "durationSec": None, "voice": None},
    "cut2-voice": {"title": "gpom-c2voice-v6A", "durationSec": 30, "voice": VOICE},
    "cut2-bed": {"title": "gpom-c2bed-v6A", "durationSec": None, "voice": None},
    "cut3-voice": {"title": "gpom-c3voice-v6A", "durationSec": 65, "voice": VOICE},
    "cut3-bed": {"title": "gpom-c3bed-v6A", "durationSec": None, "voice": None},
}


def build(atom: str) -> dict:
    cfg = ATOMS[atom]
    # 🔴 The key must carry the backtick and the dash: `extract` takes the FIRST match in the file,
    # and a bare atom name matches the sheet's own prose long before it reaches the heading.
    key = f"{atom}` — "
    out = subprocess.run(
        ["npx", "tsx", "scripts/suno/suno.mts", "extract", str(SHEET), key],
        cwd=REPO, capture_output=True, text=True,
    )
    if out.returncode != 0:
        sys.exit(f"extract failed for {atom}:\n{out.stderr.strip()[-400:]}")
    boxes = json.loads(out.stdout)
    spec = {
        "style": boxes["style"],
        "exclude": boxes["exclude"],
        "lyrics": boxes["lyrics"],          # "" for a bed — `setLyrics('')` CLEARS the box
        "title": cfg["title"],
        "workspace": WORKSPACE,
        "mode": "custom",                   # 🔴 a leftover Cover source silently makes covers
        "model": "v6",                      # required since v6; the form remembers the last one
        "variety": "off",                   # above Off, Suno rewrites the Style box
        "maxMode": False,
        "vocalGender": None,                # the Voice supplies it
        "personalize": False,               # 🔴 always. My Taste is retired
        "styleInfluence": 75,
        "weirdness": [30],
    }
    if cfg["voice"]:
        spec["voice"] = cfg["voice"]
        spec["audioInfluence"] = 50
    if cfg["durationSec"]:
        spec["durationSec"] = cfg["durationSec"]
    return spec


if __name__ == "__main__":
    if len(sys.argv) != 2 or sys.argv[1] not in ATOMS:
        sys.exit(f"usage: {sys.argv[0]} <{' | '.join(ATOMS)}>")
    print(json.dumps(build(sys.argv[1]), indent=2))
