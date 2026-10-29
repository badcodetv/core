#!/usr/bin/env python3
"""Style lint: no house style anywhere a session picks it up (Kai, 2026-10-28; widened 2026-10-29).

Anything in CLAUDE.md, the memory index or a skill/agent description reaches every prompt every
session writes. That is how GPOM's near-black look and its drum & bass became every story's
(design/2026-10-28-no-house-style.md). The 2026-10-29 audit (design/2026-10-29-style-leak-audit.md)
found the same leak one layer down: skill bodies, the shared docs skills send you to, and code
defaults that fire with nobody choosing them. Style lives in docs/stories/<story>/look.md and
sound.md (docs/stories/STYLE.md), which are only read when working on that story.

ALWAYS-LOADED (the HARD check, unchanged — exit 1 on any hit):
  CLAUDE.md                                  every line
  the memory index (MEMORY.md)               every line
  .claude/skills/*/SKILL.md, .claude/agents/*.md   the description: line only
  any skill body but story-style, any agent, CLAUDE.md outside its repo-map row, the memory index
                                             a pointer to docs/style-library/

WIDE (2026-10-29 — exit 1 on any unlabelled hit):
  skill bodies       .claude/skills/**/*.md, .claude/agents/*.md (every line)
  shared docs        docs/**/*.md except docs/stories/ (where style belongs), any archive/ folder,
                     docs/style-library/ (the menu itself), docs/provenance/ and docs/listening/log/
                     (records of what was run), docs/ideas/ (story seeds)
  generic code       scripts/** and packages/** (.py .ts .mts .mjs .js .sh, and packages' .md),
                     except story-named folders (scripts/bank-robbery, camping*, gpom, karen, …),
                     .tmp/, archive/, node_modules/, dist/
  code defaults      generic code only, tests and smoke probes excluded: a hard-coded voice name,
                     a slider literal, a model fallback (`?? 'Veo …'`, `model = 'Nano Banana …'`)

WARN (exit 0): the memory files themselves, which load when recalled.

THE ALLOW RULE — a hit is allowed, not failed, when:
  - the same line names a story: GPOM / GitPush, Camping, Karen, Bank Robbery, MMT / Magic Money
    Tree, Money For Something / MFS, Speakeasy, Galileo, Storyverse, Downfall (a labelled example:
    "GPOM's newsreader" passes, "the newsreader" fails);
  - it sits under a markdown heading that says History, Archive, Retired, Superseded, Changelog,
    Rejected or "was" (what was tried, not what to do), or one that starts "If …" / "When …";
  - the line is written as history or a condition: "used to", "was removed", "retired",
    "superseded", "until 2026-…", "if the song / story / look … is";
  - the file declares itself story-scoped in its first 40 lines: `style-lint: story=<slug>`
    (for a story-only script that has to live in a shared folder);
  - the line carries `style-lint: ok` (an engine fact that happens to use a style word — say why);
  - the word is the rule itself, negated: "no house style", "not a house style", "never a …".
  Tests and smoke probes (*.test.*, smoke-*, test_*) are not scanned: their fixtures are not defaults.

Usage: python3 scripts/style-lint.py [--memory <dir>] [--hard-only] [--summary]
  --memory     defaults to ~/.claude/projects/<this repo's path, / → ->/memory (each machine has its own).
  --hard-only  only the always-loaded check (the pre-2026-10-29 behaviour).
  --summary    counts per file instead of every hit.
"""
import re, sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# The always-loaded list (HARD). Deliberately broad: nothing style-shaped belongs there at all.
STYLE = re.compile("|".join([
    r"drum ?(&|and|n) ?bass", r"\bd&b\b", r"\bdnb\b", r"\bbpm\b", r"\bjungle\b", r"amen break",
    r"near-black", r"monolith", r"\b35 ?mm\b", r"documentary (look|register)", r"cool-neutral",
    r"teal", r"one thin (light|blade)", r"thin light", r"newsreader", r"cello",
    r"house (look|sound|register|settings|voice|preamble|style)", r"badcode (look|sound|register)",
    r"look like badcode", r"(machine|people) register", r"\bw(eirdness)? ?\d{2}\b",
    r"style influence \d", r"\bsi \d{2}\b", r"\bpair 20/35\b",
    # 2026-10-29: the words the first lint did not know (audit §"Why the lint missed it").
    r"\bopera\b", r"\brasta\b", r"\breggae\b", r"\bgrime\b", r"\bzimmer\b", r"black[- ]and[- ]white",
    r"double[- ]time", r"\bbrixton\b", r"zubenelgenubi", r"\balgenib\b", r"sadaltager", r"\bkore\b",
    r"style lock",
]), re.I)

# The WIDE list: words that name a particular story's look or sound, or a setting value. Engine
# vocabulary that every story may use (BPM, cello, teal, jungle as a word) is left out on purpose.
WIDE = re.compile("|".join([
    r"drum ?(&|and|n) ?bass", r"\bd&b\b", r"\bdnb\b", r"amen break", r"liquid (dnb|d&b|drum)",
    r"near-black", r"\bmonolith", r"documentary (look|register)", r"one thin (light|blade)",
    r"\bthe thin light\b", r"newsreader",
    r"house[- ](style|look|sound|register|settings|voice|preamble|genre|palette|grade|default)",
    r"(the |our )?badcode (look|sound|register|palette)", r"look like badcode",
    r"(machine|people) register", r"weirdness \d{2}", r"style influence \d{2}", r"audio influence \d{2}",
    r"\bopera\b", r"\brasta\b", r"\breggae\b", r"\bgrime\b", r"\bzimmer\b", r"black[- ]and[- ]white",
    r"double[- ]time", r"\bbrixton\b", r"zubenelgenubi", r"\balgenib\b", r"sadaltager", r"\bkore\b",
    r"style lock",
]), re.I)

# Code defaults: a choice written into generic code, so it fires with nobody choosing it.
VOICES = ("Achernar Achird Algenib Algieba Alnilam Aoede Autonoe Callirrhoe Charon Despina Enceladus "
          "Erinome Fenrir Gacrux Iapetus Kore Laomedeia Leda Orus Puck Pulcherrima Rasalgethi Sadachbia "
          "Sadaltager Schedar Sulafat Umbriel Vindemiatrix Zephyr Zubenelgenubi").split()
CODE_DEFAULT = re.compile("|".join([
    r"""['"](%s)['"]""" % "|".join(VOICES),                                  # a voice literal
    r"\b(styleInfluence|weirdness|audioInfluence)\s*(\?\?|=(?!=)|:)\s*\[?\s*\d",  # slider literal
    r"setSlider\([^)]*'(Style Influence|Weirdness|Audio Influence)',\s*\d",    # slider set to a literal
    r"\?\?\s*['\"](Nano Banana|Veo|Omni|Gemini Omni)",                         # model fallback
    r"\b(model|MODEL|VOICE|voice)\s*=\s*['\"](Nano Banana|Veo|Omni)",          # model default
    r"\bmodel\s*:\s*['\"](Nano Banana|Veo|Omni|Gemini Omni)",                  # model literal in a call
    r"\baspect\s*(:|\?\?)\s*['\"]\d+:\d+['\"](?!\s*\|)",                               # aspect literal / fallback
]))

STORY_LABEL = re.compile(
    r"\bGPOM\b|gitpush|git push origin master|\bcamping\b|\bkaren\b|bank[- ]robbery|\bBR\b|\bMMT\b|"
    r"magic money tree|money for (something|nothing)|\bMFS\b|speakeasy|\bgalileo\b|\bstoryverse\b|"
    r"\bdownfall\b|\btarquin\b", re.I)
HISTORY_HEAD = re.compile(r"^#{1,6} (.*\b(history|archive[sd]?|retired|superseded|changelog|rejected|"
                          r"what was tried|was\b)|(if|when) )", re.I)
# A line written as history or as a condition is not a default: "used to", "was removed",
# "if the song is drum & bass".
CONDITIONAL = re.compile(r"\b(used to|was removed|were removed|retired|superseded|until 2026-\d\d-\d\d)\b|"
                         r"\b(if|when|unless) (the|a|this|your) (song|story|track|look|part|scene|film|round)\b", re.I)
FILE_STORY = re.compile(r"style-lint:\s*story=\S+")
LINE_OK = re.compile(r"style-lint:\s*ok")

STORY_DIRS = {"bank-robbery", "camping", "camping-mv2", "downfall", "gaze-board", "gpom", "karen",
              "money-for-something", "magic-money-tree", "galileo", "storyverse", "palettes"}
SKIP_DIRS = {"node_modules", "dist", ".tmp", "archive", "__pycache__", ".git"}
CODE_EXT = {".py", ".ts", ".mts", ".mjs", ".js", ".sh"}
DOC_SKIP = ("docs/stories/", "docs/style-library/", "docs/provenance/", "docs/listening/log/", "docs/ideas/")


def memory_dir():
    a = sys.argv
    if "--memory" in a:
        return Path(a[a.index("--memory") + 1])
    return Path.home() / ".claude" / "projects" / str(ROOT).replace("/", "-") / "memory"


def rel(path):
    return path.relative_to(ROOT) if path.is_relative_to(ROOT) else path


NEGATED = re.compile(r"\b(no|not an?|never an?|there is no)\s+(badcode\s+|one\s+)?$", re.I)


def scan(path, lines, label, rx=STYLE, negation_ok=True):
    hits = []
    for n, line in lines:
        for m in rx.finditer(line):
            if negation_ok and NEGATED.search(line[:m.start()]):
                continue
            hits.append(f"{label} {rel(path)}:{n}  “{m.group(0)}”  {line.strip()[:110]}")
    return hits


def numbered(path):
    try:
        return list(enumerate(path.read_text(errors="replace").splitlines(), 1))
    except (OSError, UnicodeDecodeError):
        return []


def description(path):
    return [(n, l) for n, l in numbered(path) if l.startswith("description:")][:1]


LIBRARY = re.compile(r"style-library")


def library_pointers(mem):
    """Only story-style may send a session to the library; anywhere else it becomes a menu every
    story picks from, which is a house style again."""
    hits = []
    files = [f for f in sorted((ROOT / ".claude" / "skills").glob("*/SKILL.md")) if f.parent.name != "story-style"]
    files += sorted((ROOT / ".claude" / "agents").glob("*.md"))
    for f in files:
        hits += [f"🔴 {f.relative_to(ROOT)}:{n}  points at the style library  {l.strip()[:90]}"
                 for n, l in numbered(f) if LIBRARY.search(l)]
    for n, l in numbered(ROOT / "CLAUDE.md"):
        if LIBRARY.search(l) and not l.startswith("| `docs/style-library/` |"):
            hits.append(f"🔴 CLAUDE.md:{n}  points at the style library outside its repo-map row")
    if (mem / "MEMORY.md").exists():
        hits += [f"🔴 MEMORY.md:{n}  points at the style library" for n, l in numbered(mem / "MEMORY.md") if LIBRARY.search(l)]
    return hits


# ── the wide scan ───────────────────────────────────────────────────────────────────────────────

def allowed_lines(path, lines):
    """The (line number, text) pairs the allow rule does NOT excuse. A file declared story-scoped
    in its first 40 lines is excused whole."""
    if any(FILE_STORY.search(l) for _, l in lines[:40]):
        return []
    out, in_history = [], False
    md = path.suffix == ".md"
    for n, line in lines:
        if md and line.startswith("#"):
            in_history = bool(HISTORY_HEAD.match(line))
        if in_history or STORY_LABEL.search(line) or LINE_OK.search(line) or CONDITIONAL.search(line):
            continue
        out.append((n, line))
    return out


def walk(base, exts, skip_dirs=SKIP_DIRS, story_dirs=frozenset()):
    for p in sorted(base.rglob("*")):
        if not p.is_file() or p.suffix not in exts:
            continue
        parts = set(p.relative_to(base).parts[:-1])
        if parts & skip_dirs or parts & story_dirs:
            continue
        yield p


def wide_targets():
    """(category, path) for every file the wide scan reads."""
    for p in walk(ROOT / ".claude" / "skills", {".md"}):
        yield "skill", p
    for p in sorted((ROOT / ".claude" / "agents").glob("*.md")):
        yield "skill", p
    for p in walk(ROOT / "docs", {".md"}):
        r = str(p.relative_to(ROOT))
        if not r.startswith(DOC_SKIP):
            yield "doc", p
    for p in walk(ROOT / "scripts", CODE_EXT | {".md"}, story_dirs=STORY_DIRS):
        if p.name != "style-lint.py":  # this file names every word it looks for
            yield "code", p
    for p in walk(ROOT / "packages", CODE_EXT | {".md"}):
        yield "code", p


def is_test(p):
    n = p.name
    return ".test." in n or n.startswith(("smoke", "test_")) or "/test/" in str(p)


def wide():
    fails = []
    for cat, p in wide_targets():
        if cat == "code" and is_test(p):
            continue
        lines = allowed_lines(p, numbered(p))
        if not lines:
            continue
        fails += scan(p, lines, f"🔴 [{cat}]", WIDE, negation_ok=True)
        if cat == "code" and p.suffix in CODE_EXT:
            fails += scan(p, lines, "🔴 [code default]", CODE_DEFAULT)
    return fails


def summarise(hits):
    """One line per file: count, category, path."""
    c = Counter()
    for h in hits:
        cat = re.search(r"\[[a-z ]+\]", h)
        where = re.search(r"(\S+):\d+\s", h)
        c[f"{cat.group(0) + ' ' if cat else ''}{where.group(1) if where else h[:60]}"] += 1
    return [f"{n:4d}  {k}" for k, n in c.most_common()]


def main():
    summary = "--summary" in sys.argv
    fails = scan(ROOT / "CLAUDE.md", numbered(ROOT / "CLAUDE.md"), "🔴")
    for f in sorted((ROOT / ".claude" / "skills").glob("*/SKILL.md")) + sorted((ROOT / ".claude" / "agents").glob("*.md")):
        fails += scan(f, description(f), "🔴")
    mem = memory_dir()
    fails += library_pointers(mem)
    warns = []
    if (mem / "MEMORY.md").exists():
        fails += scan(mem / "MEMORY.md", numbered(mem / "MEMORY.md"), "🔴")
        for f in sorted(mem.glob("*.md")):
            if f.name != "MEMORY.md":
                warns += scan(f, allowed_lines(f, numbered(f)), "🟡", WIDE, negation_ok=True)
    else:
        print(f"(no memory index at {mem} — skipped)")
    hard = len(fails)
    wide_fails = [] if "--hard-only" in sys.argv else wide()

    for w in (summarise(warns) if summary else warns):
        print(w)
    if wide_fails:
        print(f"\n── WIDE: skill bodies, shared docs, generic code ({len(wide_fails)} unlabelled hits)")
        for f in (summarise(wide_fails) if summary else wide_fails):
            print(f)
    if fails:
        print("\n── ALWAYS-LOADED")
        for f in fails:
            print(f)
    if hard:
        print(f"\n🔴 {hard} style words in always-loaded files. Move them into the story's "
              "look.md / sound.md (docs/stories/STYLE.md).")
    # Shared docs are engine manuals: many hits are measured facts about a genre or a slider, so they
    # report without failing; --strict fails on them too. Skill bodies and generic code always fail.
    strict = "--strict" in sys.argv
    doc_hits = [h for h in wide_fails if "[doc]" in h]
    failing = wide_fails if strict else [h for h in wide_fails if "[doc]" not in h]
    if doc_hits and not strict:
        print(f"\n🟡 {len(doc_hits)} unlabelled style words in shared docs (not failing; --strict to fail). "
              "Label each with its story, or move it to the story's look.md / sound.md.")
    if failing:
        print(f"\n🔴 {len(failing)} unlabelled style words / code defaults in skill bodies"
              f"{', shared docs' if strict else ''} or generic code. Move the style into the story's look.md / "
              "sound.md, label the example with its story on the same line, or (code) take the value from the "
              "spec / scene / story file.")
    if hard or failing:
        sys.exit(1)
    where = ("CLAUDE.md, the memory index or any skill description" if "--hard-only" in sys.argv else
             "CLAUDE.md, the memory index, any skill description, skill body or generic code")
    print(f"✅ no style in {where}{f' ({len(warns)} warnings in memory files)' if warns else ''}")


if __name__ == "__main__":
    main()
