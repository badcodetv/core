#!/usr/bin/env python3
"""fresh.py — is this prompt the same prompt again?

Jack, 2026-10-29: "make sure there is a check for this 'same prompt' problem every time you write one."
sameness.py checks a variations round against itself; this checks ONE new prompt against every
prompt we have already sent: the recipe cards (docs/provenance/cards) and every JSON spec, round or
job file in docs/stories and scripts (any "prompt", "style" or "motion" string in them).

It never blocks. It reports, and the writer decides:
  - IDENTICAL to a past prompt    → fine for a deliberate re-roll, otherwise rewrite
  - NEAR COPY (a long shared run) → the old prompt is being reused with a word swapped
  - HABIT PHRASES                 → phrases that sit in many past prompts: the wording that turns
                                    every prompt into the same prompt (the 400-take Bank Robbery trap)

  python3 scripts/variations/fresh.py "the prompt text"        (or pipe it on stdin)
  python3 scripts/variations/fresh.py --kind suno --json  < style.txt
  --kind flow|suno|any   which corpus to compare against (default any)
  --json                 machine output (used by the PreToolUse hook)

Exit 0 always; with --quiet it prints nothing when the prompt is fresh.
"""
import argparse, json, re, sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
KEYS = {"prompt", "style", "motion", "motion_prompt", "image_prompt", "video_prompt"}
NEAR_RUN = 10          # words in a row shared with one past prompt
HABIT_MIN = 6          # a 4-word phrase in at least this many past prompts is a habit
SKIP = {"node_modules", ".git", "archive", ".tmp"}
# Four words made only of these is not a phrase anyone chose.
FUNCTION = set("a an the of in on at to and or but with from by for is are was be it its this that "
               "his her their our your one two no not as into over under up down out off so very".split())


def words(t):
    return re.findall(r"[a-z0-9']+", t.lower())


def grams(ws, n):
    return {" ".join(ws[i:i + n]) for i in range(len(ws) - n + 1)}


def longest_run(a, b):
    """Longest run of words in a that also appears in b (word lists)."""
    best, prev = 0, {}
    for x in a:
        cur = {}
        for j, y in enumerate(b):
            if x == y:
                cur[j] = prev.get(j - 1, 0) + 1
                best = max(best, cur[j])
        prev = cur
    return best


def strings_in(obj, kind_hint):
    if isinstance(obj, dict):
        for k, v in obj.items():
            if k in KEYS and isinstance(v, str) and len(v.split()) >= 6:
                yield ("suno" if k == "style" else "flow"), v
            else:
                yield from strings_in(v, kind_hint)
    elif isinstance(obj, list):
        for v in obj:
            yield from strings_in(v, kind_hint)


def corpus(kind):
    seen, out = set(), []
    paths = list((ROOT / "docs").rglob("*.json")) + list((ROOT / "scripts").rglob("*.json"))
    for p in paths:
        if set(p.relative_to(ROOT).parts) & SKIP:
            continue
        try:
            data = json.loads(p.read_text())
        except (OSError, ValueError, UnicodeDecodeError):
            continue
        card_kind = None
        if isinstance(data, dict) and data.get("engine") in ("flow", "suno"):
            card_kind = data["engine"]
        for k, text in strings_in(data, None):
            k = card_kind or k
            if kind != "any" and k != kind:
                continue
            key = text.strip()
            if key in seen:
                continue
            seen.add(key)
            out.append((str(p.relative_to(ROOT)), text))
    return out


def check(prompt, kind="any"):
    ws = words(prompt)
    past = corpus(kind)
    res = {"compared_with": len(past), "identical": [], "near": [], "habits": []}
    if len(ws) < 6:
        return res
    norm = " ".join(ws)
    mine4 = {g for g in grams(ws, 4) if not set(g.split()) <= FUNCTION}
    counts = Counter()
    for path, text in past:
        pw = words(text)
        if " ".join(pw) == norm:
            res["identical"].append(path)
            continue
        g4 = grams(pw, 4)
        shared = mine4 & g4
        counts.update(shared)
        if len(shared) >= 3:
            run = longest_run(ws, pw)
            if run >= NEAR_RUN:
                res["near"].append({"file": path, "shared_run": run, "of_words": len(ws)})
    res["near"].sort(key=lambda r: -r["shared_run"])
    res["near"] = res["near"][:3]
    res["habits"] = [{"phrase": g, "in_past_prompts": n} for g, n in counts.most_common() if n >= HABIT_MIN][:8]
    return res


def report(res):
    lines = []
    if res["identical"]:
        lines.append(f"IDENTICAL to a past prompt ({res['identical'][0]}). Fine if this is a deliberate re-roll; "
                     "otherwise write a new one.")
    for r in res["near"]:
        lines.append(f"NEAR COPY: shares {r['shared_run']} words in a row with {r['file']} "
                     f"(prompt is {r['of_words']} words). Rewrite the shared part in new words.")
    if res["habits"]:
        lines.append("HABIT PHRASES (already in many past prompts — the wording that makes every prompt the same): "
                     + "; ".join(f"\"{h['phrase']}\" ×{h['in_past_prompts']}" for h in res["habits"]))
    return lines


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("prompt", nargs="?")
    ap.add_argument("--kind", default="any", choices=["flow", "suno", "any"])
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--quiet", action="store_true")
    a = ap.parse_args()
    text = a.prompt if a.prompt is not None else sys.stdin.read()
    res = check(text, a.kind)
    if a.json:
        print(json.dumps(res))
        return
    lines = report(res)
    if lines:
        print("\n".join(lines))
        print("A loose guide, not a rule: keep a repeat only if you mean it, and say so.")
    elif not a.quiet:
        print(f"fresh: nothing close among {res['compared_with']} past prompts")


if __name__ == "__main__":
    main()
