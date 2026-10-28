#!/usr/bin/env python3
"""Sealed Suno round, end to end, with no hand-editable step (2026-10-24).

Why this exists: across 400+ Bank Robbery takes the same voice kept coming back, and every time
the cause was a step where a session that has the repo loaded put its own hands on the round —
it paraphrased the brief, leaked old listen logs and stored prompts into it, wrote the prompts
itself, retyped the writer's JSON, or overrode a failed sameness gate as "just the music". Jack,
2026-10-24: "i do not want the same mistakes made over and over, i cannot emphasise this enough."
So the whole round is one pipeline, and the session supplies only raw inputs.

  write <dir>                 brief → 1 sealed ideas writer → N sealed prompt writers (one prompt
                              each, in parallel, none sees another's text) → sameness gate → lyric
                              check → rewrite the offenders (max 2 passes) → round.json + gate stamp.
                              A round that still fails is a STOP: nothing is written to run.
  run <dir> <title> [--yes] [--only a,b]
                              checks the stamp against round.json (an edited round will not run),
                              then one Create per prompt, verbatim, via suno.mts grid. Dry run
                              without --yes.

<dir> holds the raw inputs, never a paraphrase:
  jack.md       REQUIRED  the human's message, verbatim (paste it, do not summarise it)
  lyrics.txt    REQUIRED  the lyric words only, no cue tags
  listen.md     optional  ONE fresh listen of the reference, the listener's text verbatim
  reference.md  optional  reference URLs + Suno's own stored record for it, raw
  facts.md      optional  the facts of the last verdict: what was run, what the human said.
                          Facts and the human's quotes only — no theories, no house rules.
  count         optional  how many prompts (default: the ideas writer chooses, 6–10)
  keep.txt      optional  REFINE round: the liked take's own Style box, verbatim from Suno's record.
                          Each writer then keeps that box and changes only what Jack asked (e.g. the
                          voice); the gate lets its words be shared, never its voice words.

Old listen logs, old prompts and anything from docs/suno-gpt/ never go in. That is the whole point.
"""
import concurrent.futures as cf, hashlib, json, os, re, subprocess, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
WRITER = HERE / "sealed-writer.sh"
sys.path.insert(0, str(HERE))
from sameness import gate  # noqa: E402

STANDING = """Jack's standing rules (his own words, always true): no screaming; no fast or double-time rap;
no Covers or remixes — every take is a fresh Create."""

SETTINGS_SPEC = """Settings you choose per prompt: model "v6" or "v6-wild"; variety "off"/"normal"/"high"/"extra"/"max";
weirdness 0–100; styleInfluence 0–100; vocalGender "male"/"female"/null; durationSec 1–300; maxMode true/false."""

PROMPT_KEYS = ["name", "style", "exclude", "lyrics", "model", "variety", "weirdness",
               "styleInfluence", "vocalGender", "durationSec", "maxMode"]


def read(d, name):
    p = d / name
    return p.read_text().strip() if p.exists() else ""


def base_brief(d):
    parts = ["You are writing Suno v6 prompts for a songwriter called Jack. Research the internet "
             "first (search and read pages) and base your work on what you find.",
             "## Jack's request, word for word\n\n" + read(d, "jack.md")]
    if read(d, "facts.md"):
        parts.append("## What happened in earlier rounds (facts)\n\n" + read(d, "facts.md"))
    if read(d, "reference.md"):
        parts.append("## The reference take\n\n" + read(d, "reference.md") +
                     "\n\nFetch its public Suno page yourself as well.")
    if read(d, "listen.md"):
        parts.append("## One fresh AI listening pass on the reference, verbatim\n\n"
                     "(AI listeners are not fully reliable.)\n\n" + read(d, "listen.md"))
    parts.append(STANDING)
    parts.append("## The lyrics\n\nUse these words exactly — do not change, add or remove any word or "
                 "spelling. You may add section tags and short directions in square brackets. Keep "
                 "every line.\n\n```\n" + read(d, "lyrics.txt") + "\n```")
    return "\n\n".join(parts)


def sealed(brief, out, reuse=True):
    """Run one sealed writer. A finished output for the SAME brief is reused untouched (resume)."""
    out.parent.mkdir(parents=True, exist_ok=True)
    bf = out.with_suffix(".brief.md")
    if reuse and out.exists() and bf.exists() and bf.read_text() == brief and "```json" in out.read_text():
        print(f"↺ reusing {out.name} (same brief, finished)")
        return out.read_text()
    bf.write_text(brief)
    subprocess.run([str(WRITER), "--web", str(bf), str(out)], check=True)
    return out.read_text()


def last_json(text):
    blocks = re.findall(r"```json\s*\n(.*?)```", text, re.S)
    if not blocks:
        raise ValueError("writer returned no ```json block")
    return json.loads(blocks[-1])


def words(s):
    return re.findall(r"[a-z0-9']+", re.sub(r"\[[^\]]*\]", " ", s.lower().replace("’", "'")))


def problems(p, lyric_words):
    out = []
    missing = [k for k in PROMPT_KEYS if k not in p]
    if missing:
        out.append(f"missing keys: {', '.join(missing)}")
    if words(p.get("lyrics", "")) != lyric_words:
        out.append("the lyric words are not exactly Jack's lyrics (a word was changed, added, dropped or reordered)")
    style = p.get("style", "").lower()
    if len(p.get("style", "")) > 1000:  # Suno caps the Style box at 1,000 characters (SR7 lost a prompt to it)
        out.append(f"the Style box is {len(p['style'])} characters; Suno's limit is 1000")
    for bad in ("scream", "double-time", "double time", "fast rap"):
        if bad in style:
            out.append(f"the Style box asks for '{bad}', which Jack's standing rules forbid")
    return out


def write(d):
    d = Path(d)
    for f in ("jack.md", "lyrics.txt"):
        if not read(d, f):
            sys.exit(f"🔴 {d/f} is required")
    lyric_words = words(read(d, "lyrics.txt"))
    brief = base_brief(d)
    count = read(d, "count")
    keep = read(d, "keep.txt")
    how_many = f"exactly {count}" if count else ("between 4 and 6 (you choose)" if keep else "between 6 and 10 (you choose)")
    if keep:
        brief += f"""

## The box to keep

Jack wants a prompt very close to the reference take's own Style box, with only what he asks for
changed. Here it is, verbatim from Suno's record:

```
{keep}
```"""
    ask = (f"""Not prompts yet. Propose {how_many} iterations of the box above. Each changes only what
Jack's request asks to change and keeps the rest, and each is genuinely different from the others in
how it does that (if the voice changes, a different singer each time: who is singing and how). A
separate writer will turn each iteration into a close variant of the box above, and none of them will
see the others' prompts, so make each one complete and distinct on its own.""" if keep else
f"""Not prompts yet. Propose {how_many} experiments for this round. Each one is a genuinely different
idea for how to answer Jack's request — different from each other in the voice (who is singing and
how), and in how the music is asked for. A separate writer will turn each idea into one prompt, and
none of them will see the others' prompts, so make each idea complete and distinct on its own.""")
    ideas_txt = sealed(brief + f"""

## What to produce now

{ask}

Answer with a short list of what your research found (with source URLs), then ONE fenced ```json
block: an array of objects with keys "name" (short kebab-case) and "idea" (3–6 sentences).""",
                       d / "writers" / "ideas.md")
    ideas = last_json(ideas_txt)
    names = [i["name"] for i in ideas]

    def one(idea, extra="", reuse=True):
        others = ", ".join(n for n in names if n != idea["name"])
        return sealed(brief + f"""

## Your experiment

Write ONE prompt for this experiment, and only this one:

**{idea['name']}** — {idea['idea']}

{("Your Style box is the box to keep above, changed only as your iteration and Jack's request need: keep the rest of its words. Write every change in your own words — other writers are doing the other iterations (" + others + ") and must not share your new wording.") if keep else ("Other writers are doing the other experiments (" + others + "). Make yours sound like itself, in your own words: do not reuse the wording of the listening pass or of any earlier prompt.")}

{SETTINGS_SPEC}
{extra}
Answer with a short note on what shaped it (with source URLs), then ONE fenced ```json block: a
single object with exactly these keys: {', '.join(PROMPT_KEYS)}. "name" must be "{idea['name']}".""",
                      d / "writers" / f"{idea['name']}.md", reuse)

    with cf.ThreadPoolExecutor(max_workers=len(ideas)) as ex:
        texts = dict(zip(names, ex.map(one, ideas)))
    by_name = {i["name"]: i for i in ideas}
    prompts = {n: last_json(t) for n, t in texts.items()}

    for attempt in range(3):
        round_ = [prompts[n] for n in names]
        print(f"\n═══ gate, pass {attempt + 1}")
        offenders = gate(round_, keep)
        faults = {n: problems(prompts[n], lyric_words) for n in names}
        faults = {n: f for n, f in faults.items() if f}
        for n, f in faults.items():
            print(f"🔴 {n}: " + "; ".join(f))
        todo = sorted(set(offenders) | set(faults))
        if not todo:
            break
        if attempt == 2:
            (d / "round.FAILED.json").write_text(json.dumps(round_, indent=2, ensure_ascii=False))
            sys.exit("🔴 STOP — the round still fails after two rewrites. Nothing will run. "
                     "Tell the human; do not edit the prompts by hand.")
        def redo(n):
            notes = [f"- shares wording with other prompts in this round: {s}" for s in offenders.get(n, [])]
            notes += [f"- {f}" for f in faults.get(n, [])]
            extra = ("\n## Your previous draft failed an automatic check — rewrite it\n\n"
                     "Whenever prompts in a round share wording, the voices come out the same. "
                     "Problems:\n" + "\n".join(notes) +
                     "\n\nYour previous draft:\n```json\n" + json.dumps(prompts[n], indent=2, ensure_ascii=False) + "\n```\n")
            return n, last_json(one(by_name[n], extra, reuse=False))
        with cf.ThreadPoolExecutor(max_workers=len(todo)) as ex:
            for n, p in ex.map(redo, todo):
                prompts[n] = p

    round_ = [prompts[n] for n in names]
    body = json.dumps(round_, indent=2, ensure_ascii=False)
    (d / "round.json").write_text(body)
    (d / "round.gate").write_text(hashlib.sha256(body.encode()).hexdigest() + "\n")
    print(f"\n✅ {len(round_)} prompts passed the gate → {d/'round.json'}")


def run(d, title, yes, only=None):
    d = Path(d)
    body = (d / "round.json").read_text()
    stamp = read(d, "round.gate")
    if hashlib.sha256(body.encode()).hexdigest() != stamp:
        sys.exit("🔴 round.json does not match its gate stamp — it was edited after the gate, or never "
                 "gated. Re-run `write`; never hand-edit a round.")
    round_ = json.loads(body)
    workspace = read(d, "workspace") or None
    for p in round_:
        if only and p["name"] not in only:  # retry a Create that timed out, still from the stamped round
            continue
        spec = {k: p[k] for k in PROMPT_KEYS if k != "name"}
        spec.update(title=f"{title}-{p['name']}", weirdness=[p["weirdness"]], mode="custom",
                    workspace=workspace)
        sp = d / "specs" / f"{p['name']}.json"
        sp.parent.mkdir(exist_ok=True)
        sp.write_text(json.dumps(spec, indent=2, ensure_ascii=False))
        print(f"{spec['title']}: {p['model']} variety={p['variety']} w={p['weirdness']} "
              f"style={p['styleInfluence']} gender={p['vocalGender']} {p['durationSec']}s max={p['maxMode']}")
        if yes:
            subprocess.run(["npx", "tsx", str(HERE / "suno.mts"), "grid", str(sp)], check=False)
    if not yes:
        print(f"\n{len(round_)} Creates — nothing spent. Re-run with --yes to generate.")


if __name__ == "__main__":
    a = sys.argv[1:]
    if a[:1] == ["write"] and len(a) == 2:
        write(a[1])
    elif a[:1] == ["run"] and len(a) >= 3:
        only = a[a.index("--only") + 1].split(",") if "--only" in a else None
        run(a[1], a[2], "--yes" in a, only)
    else:
        sys.exit(__doc__)
