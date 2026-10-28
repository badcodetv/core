#!/usr/bin/env python3
"""Style lint: no house style in what every session loads (Kai, 2026-10-28).

Anything in CLAUDE.md, the memory index or a skill/agent description reaches every prompt every
session writes. That is how GPOM's near-black look and its drum & bass became every story's
(design/2026-10-28-no-house-style.md). Style lives in docs/stories/<story>/look.md and sound.md
(docs/stories/STYLE.md), which are only read when working on that story.

Checks (exit 1 on any hit):
  CLAUDE.md                                  every line
  the memory index (MEMORY.md)               every line
  .claude/skills/*/SKILL.md, .claude/agents/*.md   the description: line only
Warns (exit 0): the memory files themselves, which load when recalled.

Usage: python3 scripts/style-lint.py [--memory <dir>]
  --memory defaults to ~/.claude/projects/<this repo's path, / → ->/memory (each machine has its own).
"""
import re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

STYLE = re.compile("|".join([
    r"drum ?(&|and|n) ?bass", r"\bd&b\b", r"\bdnb\b", r"\bbpm\b", r"\bjungle\b", r"amen break",
    r"near-black", r"monolith", r"\b35 ?mm\b", r"documentary (look|register)", r"cool-neutral",
    r"teal", r"one thin (light|blade)", r"thin light", r"newsreader", r"cello",
    r"house (look|sound|register|settings|voice|preamble)", r"badcode (look|sound)",
    r"look like badcode", r"(machine|people) register", r"\bw(eirdness)? ?\d{2}\b",
    r"style influence \d", r"\bsi \d{2}\b", r"\bpair 20/35\b",
]), re.I)


def memory_dir():
    a = sys.argv
    if "--memory" in a:
        return Path(a[a.index("--memory") + 1])
    return Path.home() / ".claude" / "projects" / str(ROOT).replace("/", "-") / "memory"


def scan(path, lines, label):
    hits = []
    for n, line in lines:
        for m in STYLE.finditer(line):
            where = path.relative_to(ROOT) if path.is_relative_to(ROOT) else path
            hits.append(f"{label} {where}:{n}  “{m.group(0)}”  {line.strip()[:110]}")
    return hits


def numbered(path):
    return list(enumerate(path.read_text().splitlines(), 1))


def description(path):
    return [(n, l) for n, l in numbered(path) if l.startswith("description:")][:1]


def main():
    fails = scan(ROOT / "CLAUDE.md", numbered(ROOT / "CLAUDE.md"), "🔴")
    for f in sorted((ROOT / ".claude" / "skills").glob("*/SKILL.md")) + sorted((ROOT / ".claude" / "agents").glob("*.md")):
        fails += scan(f, description(f), "🔴")
    mem = memory_dir()
    warns = []
    if (mem / "MEMORY.md").exists():
        fails += scan(mem / "MEMORY.md", numbered(mem / "MEMORY.md"), "🔴")
        for f in sorted(mem.glob("*.md")):
            if f.name != "MEMORY.md":
                warns += scan(f, numbered(f), "🟡")
    else:
        print(f"(no memory index at {mem} — skipped)")
    for w in warns:
        print(w)
    for f in fails:
        print(f)
    if fails:
        print(f"\n🔴 {len(fails)} style words in always-loaded files. Move them into the story's "
              "look.md / sound.md (docs/stories/STYLE.md).")
        sys.exit(1)
    print(f"✅ no style in CLAUDE.md, the memory index or any skill description"
          f"{f' ({len(warns)} warnings in memory files)' if warns else ''}")


if __name__ == "__main__":
    main()
