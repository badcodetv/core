#!/usr/bin/env python3
"""PreToolUse hook: run fresh.py on every prompt before it reaches Flow or Suno.

Wired in .claude/settings.json for the flow MCP generate tools and for Bash calls to suno.mts. It
never blocks: when a prompt repeats an old one or carries habit phrases, it hands the report to the
session as context, and the session rewrites it or says why the repeat is meant.
"""
import json, re, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import fresh  # noqa: E402

PROMPT_KEYS = {"prompt", "motion", "motion_prompt"}


def prompts_in(obj):
    if isinstance(obj, dict):
        for k, v in obj.items():
            if k in PROMPT_KEYS and isinstance(v, str):
                yield v
            else:
                yield from prompts_in(v)
    elif isinstance(obj, list):
        for v in obj:
            yield from prompts_in(v)


def suno_styles(command):
    for m in re.findall(r"[\w./@~-]+\.json", command):
        p = Path(m).expanduser()
        if not p.is_absolute():
            p = fresh.ROOT / p
        try:
            data = json.loads(p.read_text())
        except (OSError, ValueError):
            continue
        for spec in data if isinstance(data, list) else [data]:
            if isinstance(spec, dict) and isinstance(spec.get("style"), str):
                yield spec.get("name") or spec.get("title") or p.name, spec["style"]


def main():
    try:
        ev = json.load(sys.stdin)
    except ValueError:
        return
    tool, inp = ev.get("tool_name", ""), ev.get("tool_input") or {}
    checks = []
    if tool.startswith("mcp__flow__"):
        checks = [(f"prompt {i + 1}", t, "flow") for i, t in enumerate(prompts_in(inp))]
    elif tool == "Bash" and "suno.mts" in inp.get("command", ""):
        checks = [(name, t, "suno") for name, t in suno_styles(inp["command"])]
    out = []
    for label, text, kind in checks:
        lines = fresh.report(fresh.check(text, kind))
        if lines:
            out.append(f"[{label}] " + " ".join(lines))
    if out:
        msg = ("Same-prompt check (scripts/variations/fresh.py): " + " | ".join(out) +
               " — Before generating, rewrite the repeated wording in new words unless the repeat is "
               "deliberate (a re-roll, or the story's agreed preamble); either way, tell the user what was "
               "flagged and what you did.")
        print(json.dumps({"hookSpecificOutput": {"hookEventName": "PreToolUse", "additionalContext": msg}}))


if __name__ == "__main__":
    main()
