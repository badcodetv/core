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

  --story <slug>         the story this prompt is for: turns on the LEAK check (below)

LEAK (Jack, 2026-11-18: "why does the pollution stuff happen to the prompts… analyse the prompt for pollution before
you even send it"): with a story, any run of LEAK_RUN+ words shared with ANOTHER story's prompts or its own files
(badcode.md, look.md, sound.md, voice profiles and notes) is reported as "LEAK from <story>". A run that sits in
LEAK_COMMON+ stories, or in docs/brand/, is shared house wording, not a leak. The hook works out the story from
the paths in the call (docs/stories/<slug>/…, or a story's media folder from its scene.json).

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
LEAK_RUN = 7           # words in a row shared with another story = a leak
LEAK_COMMON = 3        # ...unless that run sits in this many stories (house wording)
STORY_MD = ("badcode.md", "look.md", "sound.md")
STORY_MD_DIRS = ("voices", "narration", "profiles", "notes")
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


def staged(path):
    """A clean-room prompts file written in the last 6 hours holds prompts staged for THIS run (2026-11-17:
    every Priority Lane call was flagged IDENTICAL against its own just-written file, so the real warnings
    drowned in noise and got ignored). Its exact match is not a repeat; near copies against it still count."""
    import time
    f = ROOT / path
    try:
        return f.name.startswith("prompts") and time.time() - f.stat().st_mtime < 6 * 3600
    except OSError:
        return False


def check(prompt, kind="any", story=None):
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
            if staged(path):
                continue  # the prompt's own staged copy, written just before this run: not a repeat
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
    res["leaks"] = leaks(prompt, story)
    res["habits"] = [{"phrase": g, "in_past_prompts": n} for g, n in counts.most_common() if n >= HABIT_MIN][:8]
    return res


def story_of(path):
    """docs/stories/<slug>/… → slug (a path from the corpus or a call)."""
    m = re.search(r"docs/stories/([^/]+)/", str(path).replace("\\", "/"))
    return m.group(1) if m else None


def media_roots():
    """Each story's media folder (scene.json "media"), normalised, → slug. Lets a call's output path name its story."""
    out = {}
    for sj in (ROOT / "docs/stories").glob("*/scenes/*/scene.json"):
        try:
            m = json.loads(sj.read_text()).get("media")
        except (OSError, ValueError):
            continue
        if m:
            out[norm_path(m)] = sj.parts[sj.parts.index("stories") + 1]
    return out


def norm_path(s):
    s = str(s).replace("\\", "/").lower()
    s = re.sub(r"^([a-z]):/", lambda m: f"/mnt/{m.group(1)}/", s)
    return s.rstrip("/")


def stories_in(text):
    """Every story a tool call names: media folders first (where the output goes), then docs/stories/<slug> paths."""
    t, found = norm_path(text), []
    for root, slug in sorted(media_roots().items(), key=lambda kv: -len(kv[0])):
        if root in t and slug not in found:
            found.append(slug)
    for s in re.findall(r"docs/stories/([^/\\\"' ]+)/", str(text).replace("\\\\", "/")):
        if s not in found and (ROOT / "docs/stories" / s).is_dir():
            found.append(s)
    return found


def story_in(text):
    """The story a tool call is for: where its output goes, else the first story path in it."""
    s = stories_in(text)
    return s[0] if s else None


def story_texts():
    """(path, text, story) for every story's own words: its prompts (JSON corpus) and its style/voice files."""
    out = [(p, x, story_of(p)) for p, x in corpus("any") if story_of(p)]
    for sd in (ROOT / "docs/stories").iterdir():
        if not sd.is_dir():
            continue
        files = [sd / n for n in STORY_MD if (sd / n).exists()]
        for d in STORY_MD_DIRS:
            files += list(sd.rglob(f"{d}/**/*.md")) + list(sd.rglob(f"{d}/*.md")) + list(sd.rglob(f"{d}/*.txt"))
        for f in set(files):
            try:
                out.append((str(f.relative_to(ROOT)), f.read_text(), sd.name))
            except (OSError, UnicodeDecodeError):
                pass
    return out


def brand_grams():
    g = set()
    for f in [*(ROOT / "docs/brand").rglob("*"), ROOT / "scripts/variations/house-wording.txt"]:
        if f.suffix in (".md", ".txt"):
            try:
                g |= grams(words(f.read_text()), LEAK_RUN)
            except (OSError, UnicodeDecodeError):
                pass
    return g


def leaks(prompt, story):
    """Runs of LEAK_RUN+ words this prompt shares with another story's words."""
    ws = words(prompt)
    if not story or len(ws) < LEAK_RUN:
        return []
    house5 = {g for x in brand_grams() for g in grams(x.split(), 5)}
    mine = {g for g in grams(ws, LEAK_RUN) if not grams(g.split(), 5) & house5}  # a run touching shared wording is not a leak
    if not mine:
        return []
    where = {}  # gram -> {story: path}
    for path, text, s in story_texts():
        for g in mine & grams(words(text), LEAK_RUN):
            where.setdefault(g, {}).setdefault(s, path)
    hits = {}
    for g, by in where.items():
        if len(by) >= LEAK_COMMON or story in by:
            continue  # house wording, or wording this story already uses
        for s, path in by.items():
            if s != story:
                hits.setdefault((s, path), []).append(g)
    out = []
    for (s, path), gs in sorted(hits.items(), key=lambda kv: -len(kv[1])):
        out.append({"from_story": s, "file": path, "shared": " ".join(gs[0].split()), "runs": len(gs)})
    return out[:4]


def report(res):
    lines = []
    for r in res.get("leaks", []):
        lines.append(f"LEAK from {r['from_story']}: shares \"{r['shared']}…\" ({r['runs']} overlapping runs) with {r['file']}. "
                     "Another story's wording; rewrite it from this story's own badcode.md, or say why it belongs.")
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
    ap.add_argument("--story", help="the story the prompt is for (turns on the leak check)")
    a = ap.parse_args()
    text = a.prompt if a.prompt is not None else sys.stdin.read()
    res = check(text, a.kind, a.story)
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
