# The vibe desk

**Page:** https://claude.ai/artifact/FVp78gm6kSrWyVVj3NLpCA (P400 "Cabinet Vibe Desk")

The cabinet's latest draft posts as a TweetDeck (one column per day). Kai or Jack click a post and
mark its feelings: **Nailed it**, **Needed more**, **Don't do that again**, plus a note. A
Ministers tab sets a standing mood per minister or for the whole cabinet ("much more deadpan"). The
page only collects tweaks. Claude turns them into brief changes on a PR; nothing reaches Bob
until that PR is merged (then `bob-sync.yml` pushes the briefs, and the next 06:00 cabinet speaks
in the new mood). Kai's ruling, 2026-11-06: **vibe only**: emotional register, not policy and
not schedules.

- Builder: `python3 scripts/government/vibe-page/build.py` (reads the briefs and every draft post from git, writes
  `index.html` here from `scripts/government/vibe-page/template.html`). Rebuild and republish
  after any brief changes so the "Now:" lines are current.
- Store (the artifact's db):
  - `notes/<date>_<post>`: `{statement, post, date, text, good: [], more: [], less: [], note,
    status, updatedAt}`, one per draft post; `text` is the post as it was noted. Verdicts are kept
    after applying (only `status` flips), so the scorecard and the "didn't stick" check can count them.
  - `dials/<post>` (and `dials/cabinet`): `{post, moves: [{word, level}], note, status, updatedAt}`.
    `level` is -2 much less, -1 less, 1 more, 2 much more. `status` is `pending` (waiting),
    `cleared` (emptied by a person) or `applied` (Claude has done it).
  - `history/<id>`: `{post, summary, pr, at}`, one per applied tweak; the page shows the newest.

## Applying tweaks and improving the page

The procedure is the [`government-vibe` skill](../../../.claude/skills/government-vibe/SKILL.md).
This URL is fixed (Kai, 2026-11-06): the desk is the official way to set the government's tone,
and every improvement is a republish to the same link.
