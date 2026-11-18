#!/usr/bin/env python3
"""PreToolUse hook: run fresh.py on every prompt before it reaches Flow or Suno.

Wired in .claude/settings.json for the flow MCP generate tools and for Bash calls to suno.mts, and (2026-11-18) to the
AI Studio voice script (aistudio-tts / --profile files). It also names the story the call is for, from the paths in it,
and runs fresh.py's LEAK check against every other story's words (Jack: "analyse the prompt for pollution before you
even send it"). It
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
    cmd = inp.get("command", "") if tool == "Bash" else ""
    if tool.startswith("mcp__flow__"):
        checks = [(f"prompt {i + 1}", t, "flow") for i, t in enumerate(prompts_in(inp))]
    elif "suno.mts" in cmd:
        checks = [(name, t, "suno") for name, t in suno_styles(cmd)]
    elif "aistudio-tts" in cmd:
        for m in re.findall(r"--profile[= ]+(\S+)", cmd):
            f = Path(m.strip("'\"")).expanduser()
            f = f if f.is_absolute() else fresh.ROOT / f
            try:
                checks.append((f"voice profile {f.name}", f.read_text(), "any"))
            except OSError:
                pass
    if not checks:
        return
    named = fresh.stories_in(json.dumps(inp))
    story = named[0] if named else None
    out = [f"Story for this call: {story or 'UNKNOWN (no story path in the call: say which story it is for)'}."]
    if len(named) > 1:
        out.append(f"MIXED STORIES: this call names {', '.join(named)}. Using one story's file for another is how prompts "
                   "get polluted; take everything from {story}'s own folder.".replace("{story}", str(story)))
    for label, text, kind in checks:
        lines = fresh.report(fresh.check(text, kind, story))
        if lines:
            out.append(f"[{label}] " + " ".join(lines))
    if len(out) > 1:
        msg = ("Same-prompt check (scripts/variations/fresh.py): " + " | ".join(out) +
               " — Before generating, rewrite the repeated wording in new words unless the repeat is "
               "deliberate (a re-roll, or the story's agreed preamble); either way, tell the user what was "
               "flagged and what you did.")
        print(json.dumps({"hookSpecificOutput": {"hookEventName": "PreToolUse", "additionalContext": msg}}))


if __name__ == "__main__":
    main()
