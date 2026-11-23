# The daily publish routine (the clock and the page)

**SIMULATED.** A claude.ai cloud routine runs this file once a day at 13:00 UTC, after the Bob workers
have finished. It does two jobs:

1. **The clock:** it marks every prediction that has fallen due.
2. **The page:** it republishes the private page.

It runs in Anthropic's cloud, not in Bob, because only there can it publish a private claude.ai artifact
(build log, D1 and D4).

The routine's own message says only: "Follow docs/government/simulation/routine.md on main, exactly."
Everything else is here, so this file is the only thing to change.

## Fixed values

- **The page:** https://claude.ai/artifact/GArjgzYRpi2Hc7C2ZjTi7V. Update this one artifact only. Never
  create a new one, never delete, never share.
- **Today:** `TZ=Europe/London date +%F`.

## 1. Get the issues

```bash
git fetch origin simulation/live main
git worktree add /tmp/live origin/simulation/live
```

## 2. The clock: mark what's due

For every issue file under `/tmp/live/docs/government/simulation/issues/`, every prediction with
`result: "pending"` and `due` on or before today:

- Open its `sources` and the page its `rule` names. Use WebFetch and WebSearch.
- Decide by the `rule`, word for word:
  - `hit`: the claim came true by the due date.
  - `miss`: it didn't.
  - `void`: the rule can't be applied, for example the source no longer exists or the event was
    cancelled for reasons the claim didn't cover.
- Set `result`, set `marked_on` to today, and set `mark_note`: one plain sentence saying what you saw,
  and where.
- Never mark anything before its due date. Never change a mark that's already set.
- If a page you need won't open, leave the prediction pending and try again tomorrow.

Validate each file you changed:

```bash
node scripts/government/sim/sim.mjs validate <file> --today <today>
```

Then commit on a branch made from `origin/simulation/live` and push it to `simulation/live`. Stage only
the files you marked:

```bash
cd /tmp/live && git switch -c clock-<today>
git add <files>
git -c user.name="BadCode simulation" -c user.email="sim@badcode.tv" commit -m "Simulation clock <today>: <n> marked"
git push origin HEAD:simulation/live
```

If the push is refused, carry on anyway. The marks still go on the page today, because the feed is built
from `/tmp/live`. Say in your final line that the push failed.

## 3. Build the feed

Build inside the working directory, because a publish can only read files there or in your scratchpad:

```bash
mkdir -p .sim-page
cp docs/government/simulation/page/index.html .sim-page/index.html
node scripts/government/sim/sim.mjs feed /tmp/live/docs/government/simulation/issues .sim-page/feed.json --today <today>
```

The page is always built from `main`'s `index.html`. The issues come from `simulation/live`. Invalid or
unfinished issues are left out automatically and listed under `skipped`.

## 4. Republish the page

- Read first: call `Artifact` with `action: "read"` on the page URL, then again with
  `path: "feed.json"`. A publish that replaces a file this session hasn't read is refused.
- Then call `Artifact` with:
  - `action: "publish"`;
  - `url`: the page URL;
  - `file_path`: `.sim-page/index.html` (as an absolute path);
  - `files`: `{"feed.json": "<absolute path of .sim-page/feed.json>"}`.
- Don't pass `icon`, `capabilities` or `force`.
- If the publish is refused because of a conflict, read again and publish once more. If it still fails,
  stop.

## 5. Finish

End with one line: `<n> issues, <m> marked today (<hits> hit, <misses> miss), page published | <what failed>`.

## Never

- Publish or create any other artifact.
- Post anywhere public.
- Open a PR.
- Edit `main`.
- Edit `docs/government/policies/`.
- Mark a prediction early.
- Change an issue's words: the clock only adds marks.
