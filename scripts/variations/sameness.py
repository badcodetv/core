#!/usr/bin/env python3
"""Sameness gate for a round of prompts (Suno 2026-10-23, widened 2026-10-24; Flow too since 2026-10-28).

Whatever words are identical across a round's prompts win, and every take comes out as one
voice (Bank Robbery Rounds VB and GG: one shared delivery sentence -> "the same voice again").
This flags every 3-word phrase that appears in more than one Style box, so a round is never
run with a shared voice sentence — or a shared music paragraph (Round SR1, 2026-10-23: one music
paragraph in all six prompts, "the voices sound the same"). A failure is a STOP: send it back to
the writer. Never decide the shared part is "just the music". There is no override flag, on purpose.

Since 2026-10-24 it also reads the lyric box's [bracket directions] (SR2 put the same section
cues in all six) and reports settings that never vary across the round (GA audit: the constants
are what makes takes alike).

REFINE rounds (Jack, 2026-10-24: "a very similar prompt … just change the voice"): pass the liked
take's own Style box as keep.txt. Its words may then be shared across the round — that is the brief —
except its voice words, which still fail if shared. Every NEW phrase still has to be each prompt's own.

Flow rounds (kind=flow) gate the "prompt" field: there is no voice, so any copied 6-word run fails
and shared 3-word phrases are reported for the human to read.

Usage: scripts/variations/sameness.py round.json [keep.txt] [--flow]
  round.json is either {"name": "style box text", ...}
  or the writer's array [{"name", "style", "lyrics", "model", ...}, ...] (Flow: [{"name", "prompt"}, ...])
Exit 1 if any voice-ish phrase is shared, or any run of 6+ words is shared (a copied paragraph),
in the Style boxes or the lyric directions.
"""
import json, re, sys
from collections import defaultdict

VOICE = re.compile(r"voice|vocal|sing|sung|speak|spoken|talk|rap|man|woman|shout|croon|"
                   r"falsetto|baritone|tenor|soprano|basso|bass voice|bass singer|accent|gravel|drawl|whisper|chant|"
                   r"singer|lead|harmon|choir|deliver", re.I)
SETTINGS = ("model", "variety", "weirdness", "styleInfluence", "vocalGender", "durationSec", "maxMode")


def shingles(text, n):
    out = set()
    for seg in text.split("|"):  # one lyric direction never runs into the next
        w = re.findall(r"[a-z0-9']+", seg.lower())
        out |= {" ".join(w[i:i + n]) for i in range(len(w) - n + 1)}
    return out


def directions(lyrics):
    return " | ".join(re.findall(r"\[([^\]]*)\]", lyrics or ""))


def check(texts, label, allowed=frozenset()):
    """texts: {prompt name: text}. Returns (bad voice phrases, copied runs).
    allowed: phrases of the kept reference box, which may be shared (never its voice phrases)."""
    seen, long_seen = defaultdict(set), defaultdict(set)
    for name, text in texts.items():
        for s in shingles(text, 3) - allowed:
            seen[s].add(name)
        for s in shingles(text, 6) - allowed:
            long_seen[s].add(name)
    shared = {s: sorted(n) for s, n in seen.items() if len(n) > 1}
    bad = {s: n for s, n in shared.items() if VOICE.search(s)}
    copied = {s: sorted(n) for s, n in long_seen.items() if len(n) > 1}
    print(f"── {label}")
    for s, n in sorted(shared.items(), key=lambda kv: -len(kv[1])):
        print(f"{'VOICE ' if s in bad else '      '}{len(n)}x  {s!r}  {', '.join(n)}")
    for s, n in copied.items():
        print(f"COPY  {len(n)}x  {s!r}  {', '.join(n)}")
    print(f"{len(shared)} shared phrases, {len(bad)} about the voice, {len(copied)} copied 6-word runs\n")
    return bad, copied


def gate(round_, keep="", kind="suno"):
    """round_: list of prompt dicts or {name: style}. Returns {name: [offending phrases]}.
    keep: a REFINE round's reference box (its non-voice words may be shared).
    kind: "suno" gates the Style boxes and lyric directions; "flow" gates the prompt text."""
    allowed = frozenset(s for s in shingles(keep, 3) | shingles(keep, 6) if not VOICE.search(s))
    prompts = round_ if isinstance(round_, list) else [{"name": k, "style": v} for k, v in round_.items()]
    offenders = defaultdict(set)
    fields = ((("prompt", "Flow prompts", lambda p: p.get("prompt", "")),) if kind == "flow" else
              (("style", "Style boxes", lambda p: p.get("style", "")),
               ("lyrics", "lyric [directions]", lambda p: directions(p.get("lyrics")))))
    for field, label, get in fields:
        texts = {p["name"]: get(p) for p in prompts if get(p)}
        if len(texts) < 2:
            continue
        bad, copied = check(texts, label, allowed if field != "lyrics" else frozenset())
        if kind == "flow":  # no voice in a picture: only copied runs fail
            bad = {}
        # The first prompt (in round order) that uses a shared phrase keeps it; only the others
        # rewrite. Sending ALL of them back made every writer change at once and collide again
        # (SR5, 2026-10-24: three passes, still failing). The rule itself is unchanged.
        order = {p["name"]: i for i, p in enumerate(prompts)}
        for s, names in list(bad.items()) + list(copied.items()):
            for n in sorted(names, key=order.get)[1:]:
                offenders[n].add(f"{label}: {s}")
    constant = [k for k in SETTINGS
                if all(k in p for p in prompts) and len({json.dumps(p[k]) for p in prompts}) == 1]
    if constant and len(prompts) > 1:
        print("⚠ settings identical in every prompt: " +
              ", ".join(f"{k}={json.dumps(prompts[0][k])}" for k in constant))
    return {n: sorted(v) for n, v in offenders.items()}


if __name__ == "__main__":
    a = [x for x in sys.argv[1:] if x != "--flow"]
    off = gate(json.load(open(a[0])), open(a[1]).read() if len(a) > 1 else "",
               "flow" if "--flow" in sys.argv else "suno")
    if off:
        print("🔴 STOP — do not run this round. Send the shared wording back to the writer.")
    sys.exit(1 if off else 0)
