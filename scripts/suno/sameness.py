#!/usr/bin/env python3
"""Sameness gate for a round of Suno Style boxes (2026-10-23).

Whatever words are identical across a round's prompts win, and every take comes out as one
voice (Bank Robbery Rounds VB and GG: one shared delivery sentence -> "the same voice again").
This flags every 3-word phrase that appears in more than one Style box, so a round is never
run with a shared voice sentence — or a shared music paragraph (Round SR1, 2026-10-23: one music
paragraph in all six prompts, "the voices sound the same"). A failure is a STOP: send it back to
the writer. Never decide the shared part is "just the music".

Usage: scripts/suno/sameness.py styles.json   # {"name": "style box text", ...}
Exit 1 if any voice-ish phrase is shared, or any run of 6+ words is shared (a copied paragraph).
"""
import json, re, sys
from collections import defaultdict

VOICE = re.compile(r"voice|vocal|sing|sung|speak|spoken|talk|rap|man|woman|shout|croon|"
                   r"falsetto|baritone|tenor|soprano|accent|gravel|drawl|whisper|chant", re.I)

def shingles(text, n=3):
    w = re.findall(r"[a-z']+", text.lower())
    return {" ".join(w[i:i + n]) for i in range(len(w) - n + 1)}

styles = json.load(open(sys.argv[1]))
seen = defaultdict(set)
for name, text in styles.items():
    for s in shingles(text):
        seen[s].add(name)

shared = {s: sorted(n) for s, n in seen.items() if len(n) > 1}
bad = {s: n for s, n in shared.items() if VOICE.search(s)}
long_seen = defaultdict(set)
for name, text in styles.items():
    for s in shingles(text, 6):
        long_seen[s].add(name)
copied = {s: sorted(n) for s, n in long_seen.items() if len(n) > 1}
for s, n in sorted(shared.items(), key=lambda kv: -len(kv[1])):
    print(f"{'VOICE ' if s in bad else '      '}{len(n)}x  {s!r}  {', '.join(n)}")
for s, n in copied.items():
    print(f"COPY  {len(n)}x  {s!r}  {', '.join(n)}")
print(f"\n{len(shared)} shared phrases, {len(bad)} about the voice, {len(copied)} copied 6-word runs")
if bad or copied:
    print("🔴 STOP — do not run this round. Send the shared wording back to the writer.")
sys.exit(1 if bad or copied else 0)
