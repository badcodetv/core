#!/usr/bin/env python3
"""A variation round: many genuinely different prompts, written by writers who never see each
other's text, gated for sameness, run verbatim. Driven by the `variations` skill.

History: born 2026-10-24 as scripts/suno/sealed-round.py (Jack). Across 400+ Bank Robbery takes the
same voice kept coming back, and every time the cause was a step where the session put its own
hands on the round. Jack's fix ran each writer as a `claude -p` in an empty /tmp folder, to escape
the house rules the repo loaded into every session. Kai, 2026-10-28: remove the pollution instead of
escaping it (there is no house style; style lives in docs/stories/<story>/look.md and sound.md,
checked by scripts/style-lint.py). So the writers are now ordinary subagents, and this script keeps
the parts that give variety: a brief built from raw files only, one ideas writer, N separate
writers, the sameness gate, and a stamp so nobody hand-edits the round.

  brief <dir>     builds brief.md and writers/ideas.ask.md from the raw inputs.
  asks <dir>      reads writers/ideas.json (written by the ideas writer) and writes one
                  writers/<name>.ask.md per idea.
  gate <dir>      reads writers/<name>.json, runs the sameness gate and the checks. Pass →
                  round.json + round.gate (the stamp). Fail → writers/<name>.redo.md for each
                  offender; after two rewrites a third failure is a STOP.
  check <dir>     verifies round.json against its gate stamp and prints each prompt's settings.
                  Exit 1 if the round was edited after the gate (or never gated). Flow rounds: run
                  this BEFORE the session makes the calls — one flow_generate_image (or
                  flow_generate_video) per round.json prompt, its text, model and aspect verbatim.
  run <dir> <title> [--yes] [--only a,b]
                  Suno: checks the stamp, then one Create per prompt, verbatim, via
                  scripts/suno/suno.mts grid. Dry run without --yes. Flow: the same as `check`.

<dir> holds the raw inputs, never a paraphrase:
  ask.md        REQUIRED  the human's request, verbatim (paste it, do not summarise it).
                          (jack.md is still read, for old rounds.)
  kind          optional  "suno" (default) or "flow"
  story         REQUIRED  the story's slug. Its sound.md (suno) or look.md (flow) goes into the
                          brief verbatim, so a round stays inside the story's style. A round that
                          belongs to no story says so with an empty file named `nostory` instead.
  explore       optional  present = a round to FIND a style: only the story file's "Rules for this
                          story" and "Never" sections go in, not the locked style.
  lyrics.txt    suno: REQUIRED  the lyric words only, no cue tags
  subject.md    flow: REQUIRED  what the still or clip shows (the beat, the shot), verbatim
  listen.md     optional  ONE fresh listen of the reference, the listener's text verbatim
  reference.md  optional  reference URLs + the engine's own stored record for it, raw
  facts.md      optional  the facts of the last verdict: what was run, what the human said.
  keep.txt      optional  REFINE round: the liked take's own box/prompt, verbatim. Writers keep it
                          and change only what was asked; its words may be shared.
  forbid.txt    optional  phrases no prompt may contain, one per line (e.g. a story's "Never")
  locked-settings.json  optional  settings the story's file LOCKS for this part, e.g.
                          {"model": "Nano Banana 2", "aspect": "16:9"}. Writers are told to use them,
                          the gate checks every prompt does, and the sameness gate's all-identical-
                          settings failure then looks only at the other settings.
  preamble.txt  optional  a LOCKED preamble from the story's look.md/sound.md, verbatim. Writers are
                          told to use it as-is; its words are exempt from the sameness gate.
  count         optional  how many prompts (default: the ideas writer chooses)
  workspace     optional  Suno workspace for run
"""
import hashlib, json, re, subprocess, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
sys.path.insert(0, str(HERE))
from sameness import gate as sameness_gate  # noqa: E402

SUNO_SETTINGS = """Settings you choose per prompt: model "v6" or "v6-wild"; variety "off"/"normal"/"high"/"extra"/"max";
weirdness 0–100; styleInfluence 0–100; vocalGender "male"/"female"/null; durationSec 1–300; maxMode true/false."""

FLOW_SETTINGS = """Settings you choose for your prompt, guided by the story's look above (if it names a model or
aspect for this part, use that): "model" — the Flow model, e.g. "Nano Banana 2", "Nano Banana Pro" (stills) or
"Omni Flash", "Veo 3.1 Fast" (clips); "aspect" — "16:9", "9:16", "1:1", "4:3", "3:4", "4:5", "21:9" (stills; clips
are "16:9" or "9:16"). Unless the story fixes them (see above), the round's prompts must not all share one set of settings."""

# Flow writers choose model and aspect too (2026-10-29): before, a Flow round had no way to say,
# and every prompt fell through to the tool's defaults.
KEYS = {"suno": ["name", "style", "exclude", "lyrics", "model", "variety", "weirdness",
                 "styleInfluence", "vocalGender", "durationSec", "maxMode"],
        "flow": ["name", "prompt", "model", "aspect"]}
FLOW_ASPECTS = ("1:1", "3:2", "2:3", "3:4", "4:3", "4:5", "5:4", "9:16", "16:9", "21:9", "1:4", "4:1", "1:8", "8:1")
MAX_REWRITES = 2


def read(d, name):
    p = Path(d) / name
    return p.read_text().strip() if p.exists() else ""


def kind_of(d):
    k = read(d, "kind") or "suno"
    if k not in KEYS:
        sys.exit(f"🔴 kind must be suno or flow, not {k!r}")
    return k


def sections(md, wanted):
    """The '## <heading>' sections of a markdown file whose heading starts with one of `wanted`."""
    out, keep = [], False
    for line in md.splitlines():
        if line.startswith("## "):
            keep = any(line[3:].strip().lower().startswith(w) for w in wanted)
        if keep:
            out.append(line)
    return "\n".join(out).strip()


def story_style(d, kind):
    slug = read(d, "story")
    if not slug:
        return ""
    f = ROOT / "docs" / "stories" / slug / ("sound.md" if kind == "suno" else "look.md")
    if not f.exists():
        sys.exit(f"🔴 {f} does not exist. Write the story's file first (docs/stories/STYLE.md).")
    text = f.read_text().strip()
    if read(d, "explore") or (Path(d) / "explore").exists():
        text = sections(text, ("rules for this story", "never"))
        head = "## This story's standing rules (the round is finding a new style, so only these bind)"
    else:
        head = f"## This story's {'sound' if kind == 'suno' else 'look'} (stay inside it)"
    return f"{head}\n\n{text}" if text else ""


def base_brief(d, kind):
    ask = read(d, "ask.md") or read(d, "jack.md")
    what = ("Suno v6 prompts for a song" if kind == "suno"
            else "Google Flow prompts (Nano Banana stills or Veo/Omni clips)")
    parts = [f"You are writing {what}. Research the internet first (search and read pages) and base "
             "your work on what you find. Do not read files in this repository: everything you are "
             "meant to know is in this brief.",
             "## The request, word for word\n\n" + ask]
    if read(d, "facts.md"):
        parts.append("## What happened in earlier rounds (facts)\n\n" + read(d, "facts.md"))
    if read(d, "reference.md"):
        parts.append("## The reference\n\n" + read(d, "reference.md") +
                     "\n\nFetch its public page yourself as well, if it has one.")
    if read(d, "listen.md"):
        parts.append("## One fresh AI listening pass on the reference, verbatim\n\n"
                     "(AI listeners are not fully reliable.)\n\n" + read(d, "listen.md"))
    style = story_style(d, kind)
    if style:
        parts.append(style)
    if read(d, "forbid.txt"):
        parts.append("## Never write these\n\n" + read(d, "forbid.txt"))
    if locked(d):
        parts.append("## Settings the story fixes for this part\n\nUse exactly these values for these keys "
                     "(choose the others yourself):\n\n```json\n" + json.dumps(locked(d), indent=2) + "\n```")
    if read(d, "preamble.txt"):
        parts.append("## The story's locked preamble\n\nStart your prompt with this text exactly as written "
                     "(it is the story's own, and is exempt from the sameness check); write everything after it "
                     "in your own words.\n\n```\n" + read(d, "preamble.txt") + "\n```")
    if kind == "suno":
        parts.append("## The lyrics\n\nUse these words exactly — do not change, add or remove any word or "
                     "spelling. You may add section tags and short directions in square brackets. Keep "
                     "every line.\n\n```\n" + read(d, "lyrics.txt") + "\n```")
    else:
        parts.append("## What the picture shows\n\n" + read(d, "subject.md"))
    return "\n\n".join(parts)


def keep_block(d):
    keep = read(d, "keep.txt")
    return f"""

## The box to keep

The request wants a prompt very close to this one, with only what it asks for changed. Verbatim from
the engine's record:

```
{keep}
```""" if keep else ""


def locked(d):
    f = Path(d) / "locked-settings.json"
    return json.loads(f.read_text()) if f.exists() else {}


def write_out(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text)
    print(f"→ {path}")


def brief(d):
    d = Path(d)
    kind = kind_of(d)
    need = ["lyrics.txt"] if kind == "suno" else ["subject.md"]
    if not (read(d, "ask.md") or read(d, "jack.md")):
        sys.exit(f"🔴 {d/'ask.md'} is required (the human's words, verbatim)")
    if not read(d, "story") and not (d / "nostory").exists():
        sys.exit(f"🔴 {d/'story'} is required: the story's slug (its sound.md / look.md goes into the brief). "
                 f"A round that belongs to no story must say so: create an empty file {d/'nostory'}.")
    for f in need:
        if not read(d, f):
            sys.exit(f"🔴 {d/f} is required for a {kind} round")
    b = base_brief(d, kind) + keep_block(d)
    write_out(d / "brief.md", b)
    count, keep = read(d, "count"), read(d, "keep.txt")
    how_many = f"exactly {count}" if count else ("between 4 and 6 (you choose)" if keep else "between 6 and 10 (you choose)")
    differ = ("the voice (who is singing and how — different performers, not one performer in "
              "different accents) and in how the music is asked for" if kind == "suno" else
              "what the picture is: the idea, the framing, the camera distance, the light, the palette, "
              "the time of day, what is in focus. Four seeds of one prompt are one idea, not four")
    ask = (f"Not prompts yet. Propose {how_many} iterations of the box above. Each changes only what "
           f"the request asks to change and keeps the rest, and each is genuinely different from the "
           f"others in how it does that." if keep else
           f"Not prompts yet. Propose {how_many} experiments for this round. Each one is a genuinely "
           f"different idea for how to answer the request — different from each other in {differ}.")
    write_out(d / "writers" / "ideas.ask.md", b + f"""

## What to produce now

{ask} A separate writer will turn each idea into one prompt, and none of them will see the others'
prompts, so make each idea complete and distinct on its own.

Write a short list of what your research found (with source URLs) to
`{d.resolve()}/writers/ideas.notes.md`, and write ONLY a JSON array to
`{d.resolve()}/writers/ideas.json`: objects with keys "name" (short kebab-case) and "idea"
(3–6 sentences). Reply with just the two paths.""")


def writer_ask(d, kind, idea, names, extra=""):
    others = ", ".join(n for n in names if n != idea["name"])
    keep = read(d, "keep.txt")
    own = (f"Your box is the box to keep above, changed only as your iteration and the request need: keep "
           f"the rest of its words. Write every change in your own words — other writers are doing the "
           f"other iterations ({others}) and must not share your new wording." if keep else
           f"Other writers are doing the other experiments ({others}). Make yours its own thing, in your "
           f"own words: do not reuse the wording of the listening pass or of any earlier prompt.")
    keys = KEYS[kind]
    return read(d, "brief.md") + f"""

## Your experiment

Write ONE prompt for this experiment, and only this one:

**{idea['name']}** — {idea['idea']}

{own}

{SUNO_SETTINGS if kind == 'suno' else 'Write the prompt as one paragraph of plain description: what is in the frame, the camera, the light, the palette. No film titles, no artist names.' + chr(10) + chr(10) + FLOW_SETTINGS}
{extra}
Write a short note on what shaped it (with source URLs) to `{(Path(d) / 'writers' / (idea['name'] + '.notes.md')).resolve()}`,
and write ONLY a single JSON object to `{(Path(d) / 'writers' / (idea['name'] + '.json')).resolve()}`
with exactly these keys: {', '.join(keys)}. "name" must be "{idea['name']}". Reply with just the two paths."""


def ideas_of(d):
    f = Path(d) / "writers" / "ideas.json"
    if not f.exists():
        sys.exit(f"🔴 {f} is missing — run the ideas writer on writers/ideas.ask.md first")
    return json.loads(f.read_text())


def asks(d):
    d = Path(d)
    kind, ideas = kind_of(d), ideas_of(d)
    names = [i["name"] for i in ideas]
    if len(set(names)) != len(names):
        sys.exit("🔴 two ideas share a name — re-run the ideas writer")
    for i in ideas:
        write_out(d / "writers" / f"{i['name']}.ask.md", writer_ask(d, kind, i, names))
    print(f"\n{len(ideas)} writer asks. Spawn one subagent per ask file, all at once.")


def words(s):
    return re.findall(r"[a-z0-9']+", re.sub(r"\[[^\]]*\]", " ", s.lower().replace("’", "'")))


def problems(d, kind, p):
    out = [f"missing keys: {', '.join(k for k in KEYS[kind] if k not in p)}"] if any(k not in p for k in KEYS[kind]) else []
    text = (p.get("style", "") + " " + p.get("exclude", "")) if kind == "suno" else p.get("prompt", "")
    if kind == "suno":
        if words(p.get("lyrics", "")) != words(read(d, "lyrics.txt")):
            out.append("the lyric words are not exactly the given lyrics (a word was changed, added, dropped or reordered)")
        if len(p.get("style", "")) > 1000:  # Suno caps the Style box at 1,000 characters (SR7 lost a prompt to it)
            out.append(f"the Style box is {len(p['style'])} characters; Suno's limit is 1000")
    if kind == "flow":
        if not str(p.get("model") or "").strip():
            out.append("no model — choose one, guided by the story's look")
        if p.get("aspect") not in FLOW_ASPECTS:
            out.append(f"aspect {p.get('aspect')!r} is not one of {', '.join(FLOW_ASPECTS)}")
    for k, v in locked(d).items():
        if p.get(k) != v:
            out.append(f"{k} is {p.get(k)!r}, but the story fixes it at {v!r} for this part")
    pre = read(d, "preamble.txt")
    if pre and not (p.get("style", "") if kind == "suno" else text).strip().startswith(pre.strip()):
        out.append("it does not start with the story's locked preamble, verbatim")
    for bad in filter(None, (l.strip().lower() for l in read(d, "forbid.txt").splitlines())):
        if bad in (p.get("style", "") if kind == "suno" else text).lower():
            out.append(f"it asks for '{bad}', which this story never allows")
    return out


def gate(d):
    d = Path(d)
    kind, ideas = kind_of(d), ideas_of(d)
    names = [i["name"] for i in ideas]
    missing = [n for n in names if not (d / "writers" / f"{n}.json").exists()]
    if missing:
        sys.exit(f"🔴 no output yet from: {', '.join(missing)}")
    prompts = {n: json.loads((d / "writers" / f"{n}.json").read_text()) for n in names}
    passes_f = d / "writers" / "gate.passes"
    passes = int(passes_f.read_text()) if passes_f.exists() else 0
    round_ = [prompts[n] for n in names]
    print(f"═══ gate, pass {passes + 1}")
    offenders = sameness_gate(round_, read(d, "keep.txt"), kind, read(d, "preamble.txt"), tuple(locked(d)))
    faults = {n: f for n in names if (f := problems(d, kind, prompts[n]))}
    for n, f in faults.items():
        print(f"🔴 {n}: " + "; ".join(f))
    todo = sorted(set(offenders) | set(faults))
    if not todo:
        body = json.dumps(round_, indent=2, ensure_ascii=False)
        (d / "round.json").write_text(body)
        (d / "round.gate").write_text(hashlib.sha256(body.encode()).hexdigest() + "\n")
        print(f"\n✅ {len(round_)} prompts passed the gate → {d/'round.json'}")
        return
    if passes >= MAX_REWRITES:
        (d / "round.FAILED.json").write_text(json.dumps(round_, indent=2, ensure_ascii=False))
        sys.exit("🔴 STOP — the round still fails after two rewrites. Nothing will run. "
                 "Tell the human; do not edit the prompts by hand.")
    passes_f.write_text(str(passes + 1))
    by_name = {i["name"]: i for i in ideas}
    for n in todo:
        notes = [f"- shares wording with other prompts in this round: {s}" for s in offenders.get(n, [])]
        notes += [f"- {f}" for f in faults.get(n, [])]
        extra = ("\n## Your previous draft failed an automatic check — rewrite it\n\n"
                 "Whenever prompts in a round share wording, the results come out the same. "
                 "Problems:\n" + "\n".join(notes) +
                 "\n\nYour previous draft:\n```json\n" + json.dumps(prompts[n], indent=2, ensure_ascii=False) + "\n```\n")
        (d / "writers" / f"{n}.json").rename(d / "writers" / f"{n}.pass{passes + 1}.json")
        write_out(d / "writers" / f"{n}.redo.md", writer_ask(d, kind, by_name[n], names, extra))
    sys.exit(f"\n🟡 {len(todo)} to rewrite: spawn one subagent per .redo.md, then run gate again.")


def stamped(d):
    """round.json's text, or exit if it does not match the stamp the gate wrote."""
    f = d / "round.json"
    if not f.exists():
        sys.exit(f"🔴 {f} does not exist — the round has not passed the gate.")
    body = f.read_text()
    if hashlib.sha256(body.encode()).hexdigest() != read(d, "round.gate"):
        sys.exit("🔴 round.json does not match its gate stamp — it was edited after the gate, or never "
                 "gated. Re-run gate; never hand-edit a round.")
    return body


def check(d):
    """Verify the stamp (both kinds) and print what each prompt will run with."""
    d = Path(d)
    kind = kind_of(d)
    prompts = json.loads(stamped(d))
    print(f"✅ round.json matches its gate stamp ({len(prompts)} prompts)")
    for p in prompts:
        if kind == "flow":
            print(f"  {p['name']}: model={p['model']!r} aspect={p['aspect']!r}")
        else:
            print(f"  {p['name']}: {p['model']} variety={p['variety']} w={p['weirdness']} style={p['styleInfluence']}")
    if kind == "flow":
        print("\nRun each prompt with its own model and aspect, text verbatim (prompt → prompt, model → model, "
              "aspect → aspect), count 1. Never change a word.")


def run(d, title, yes, only=None):
    d = Path(d)
    if kind_of(d) != "suno":
        return check(d)
    body = stamped(d)
    workspace = read(d, "workspace") or None
    for p in json.loads(body):
        if only and p["name"] not in only:  # retry a Create that timed out, still from the stamped round
            continue
        spec = {k: p[k] for k in KEYS["suno"] if k != "name"}
        spec.update(title=f"{title}-{p['name']}", weirdness=[p["weirdness"]], mode="custom",
                    workspace=workspace)
        sp = d / "specs" / f"{p['name']}.json"
        sp.parent.mkdir(exist_ok=True)
        sp.write_text(json.dumps(spec, indent=2, ensure_ascii=False))
        print(f"{spec['title']}: {p['model']} variety={p['variety']} w={p['weirdness']} "
              f"style={p['styleInfluence']} gender={p['vocalGender']} {p['durationSec']}s max={p['maxMode']}")
        if yes:
            subprocess.run(["npx", "tsx", str(ROOT / "scripts" / "suno" / "suno.mts"), "grid", str(sp)], check=False)
    if not yes:
        print("\nNothing spent. Re-run with --yes to generate.")


if __name__ == "__main__":
    a = sys.argv[1:]
    cmds = {"brief": brief, "asks": asks, "gate": gate, "check": check}
    if a[:1] and a[0] in cmds and len(a) == 2:
        cmds[a[0]](a[1])
    elif a[:1] == ["run"] and len(a) >= 3:
        only = a[a.index("--only") + 1].split(",") if "--only" in a else None
        run(a[1], a[2], "--yes" in a, only)
    else:
        sys.exit(__doc__)
