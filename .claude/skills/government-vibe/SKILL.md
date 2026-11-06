---
name: government-vibe
description: Use for anything about the TONE and FEEL of the BadCode government's ministers — the official place to set it is the vibe desk artifact https://claude.ai/artifact/FVp78gm6kSrWyVVj3NLpCA (a TweetDeck of the cabinet's latest draft posts, each noted Nailed it / Needed more / Don't do that again with feelings; plus a Ministers tab of standing moods per minister). Reads Kai's and Jack's tweaks from its store, turns them into minister-brief edits on a `Vibe:` PR, writes back what was applied, and improves the page itself (always republished to that same URL). Triggers on "apply the vibe tweaks", "vibe desk", "government vibe", "government tone", "make the Chancellor more sarcastic", "the Health minister is too angry", "how does the cabinet feel", "change a minister's tone", "improve the vibe page", "add X to the vibe desk", "what is the government saying", "show me the latest posts", "rebuild the deck".
---

# Government vibe (the vibe desk)

**The vibe desk is THE way BadCode edits the government's tone and feel (Kai, 2026-11-06).**

> **https://claude.ai/artifact/FVp78gm6kSrWyVVj3NLpCA**

This URL is fixed. Kai and Jack note tone on it, and the page gets better over time **at this same
link**. Its shape (Kai, 2026-11-06):

- **Posts (the hero):** every draft post the cabinet has written, as a TweetDeck, one column per
  day, newest first; posts in an open government PR are marked, since they are what goes out next.
  Click a post and mark feelings in three rows: **Nailed it** (keep doing this), **Needed more**
  (should have gone further), **Don't do that again** (wrong feeling, or too much), plus a note.
  This is how Kai judges what the content did against what it should do instead.
- **Ministers tab:** a standing mood per minister or for the whole cabinet (much less / less /
  more / much more), independent of any one post.

"What's the government saying?" → rebuild the page (step 2) so the deck is current, and send the
link; read a couple of posts out in the reply if asked. Never publish a second vibe page: every change is
a republish to this URL. If a tone request arrives in chat instead ("make Housing angrier"), put it
on the desk too (write the `dials/<post>` doc), so the desk stays the one record of what was asked.

**Scope: vibe only.** The desk sets the emotional register: deadpan, sarcastic, aggressive, warm,
weary and the like. Policy, schedules, what a minister owns and what it may promise are not vibe:
those go through an ordinary human PR on `docs/government/` (see its README). The government's
machinery (Bob, the rolling PR, the sync) is described in
[`docs/government/README.md`](../../../docs/government/README.md); read it if any of that is new.

## Where things live

| What | Where |
| --- | --- |
| The page | the URL above; source `docs/government/vibe/index.html`, **built, never hand-edited** |
| Builder | `scripts/government/vibe-page/build.py` + `template.html` beside it |
| Store (the artifact's db) | `notes/<date>_<post>` (one per draft post); `dials/<post>` and `dials/cabinet`; `history/<id>`. Schema: [`docs/government/vibe/README.md`](../../../docs/government/vibe/README.md) |
| What a minister *is* | `docs/government/ministers/NN-<post>.md`: tone lives in **Temperament**, **Guards against**, **Sounds like** |
| The record | `docs/government/vibe/feedback/<date>.json`: every read of the store, dumped before acting |

Posts: `prime-minister`, `chancellor`, `foreign`, `home`, `education`, `defence`, `health`,
`work-pensions`, `housing`, `energy-climate`, plus `cabinet` (all ten at once).

## 1. Apply the vibe tweaks: five routes, fastest first

The cabinet is a fresh session every morning. It learns only from what it reads: its prompts (git),
Bob memory, and PR comments. So one round of notes goes out by every route that reaches it
(Kai, 2026-11-06: "effect this feedback as much as we can").

1. **Read and record.** ArtifactData `list` on `notes` and `dials`. Act on `status: pending` only.
   **Dump** the raw docs (with versions) to `docs/government/vibe/feedback/<YYYY-MM-DD>.json`
   before anything else (`-2`, `-3` if today's exists). Group by minister: its noted posts (text
   quoted, with `good` / `more` / `less` / note), its own dial, and the `cabinet` dial (which
   applies to all ten).
2. **Route 1, next morning: Bob memory.** One memory per minister with anything pending,
   `memory_create` with labels `kind=feedback`, `minister=<post>`, `source=vibe-desk`,
   `date=<today>` (add `vibe_pr=<n>` after step 3; never a bare `pr`, which the cabinet's PR
   dedupe reads). Content, in this shape, quoting posts word for word:

   ```
   Vibe desk, <date>, from Kai/Jack. <Title>.
   NAILED IT (write like this): "<post>" (<feelings>; note: <note>)
   NEEDED MORE: "<post>" (more <feelings>; note: <note>)
   DON'T DO THAT AGAIN: "<post>" (<feelings>; note: <note>)
   Standing mood: <much more deadpan, less warm>. Cabinet-wide: <…>.
   ```

   The cabinet prompt (step 6.2) reads the newest 5 of these per minister: nailed posts are models,
   "don't" posts are banned moves. This route needs no merge: it works from the next 06:00.
3. **Route 2, the persona: a `Vibe:` PR on the briefs.** Branch `government/vibe-<YYYY-MM-DD>` from
   `main` (never `government/rolling`: that is the cabinet's PR). Change only Temperament, Guards
   against and Sounds like; leave Owns, Watches, Instinct, Standing platform and Never promise
   alone. The best "Nailed it" post may **become** the Sounds like sample (the strongest steer
   there is); a feeling marked "don't" twice becomes a **Guards against** line. A `cabinet` dial
   lands in all ten briefs. Keep each brief at most 300 words, heading exact. Where a vibe fights a
   guard ("much more scornful" vs "never contempt for people who are skint"), aim the feeling at the
   decision-maker, never the reader, and say so; [`the-reader.md`](../../../docs/marketing/the-reader.md)
   and [`voice.md`](../../../docs/voice.md) still hold. Commit subject starts `Vibe:` (load-bearing:
   the Cabinet Secretary keeps tone set by `Vibe:` commits). PR body: before/after per minister,
   plus the route-5 report. Kai or Jack merge; the sync then pushes the briefs into Bob.
4. **Route 3, weekly: the Cabinet Secretary** reads the week's `source=vibe-desk` memories on
   Sundays and turns repeated notes into brief edits. Nothing to do here beyond route 1; check its
   Sunday changelog entry respected the notes.
5. **Route 4, cabinet-wide: `shared.md`.** If the same verdict on the same feeling hits **three or
   more ministers** (e.g. "needed more funny" across the board), it is the shared voice, not ten
   briefs. Propose the edit to `docs/government/shared.md` in the same `Vibe:` PR, flagged as
   cabinet-wide.
6. **Route 5, proof: is it learning?** Before writing back, compare with earlier rounds
   (`docs/government/vibe/feedback/*.json` and the store's applied notes): per minister, nailed
   vs don't counts, and **repeats**: a feeling marked "don't" on a post after it was already noted
   "don't" for that minister (the page flags these too). Put it in the PR body and the reply:
   "stuck" (a feeling noted before, now nailed), "regressed" (a banned feeling back), "new".
7. **Write back** in one ArtifactData `batch`, pinned with `if_version` (if a doc changed since the
   read, leave it pending and say so):
   - each acted-on `notes/<id>` → `update` `{status: "applied", pr, appliedAt}`. **Keep `good`,
     `more`, `less` and `note`**: the page's scorecard and the repeat check are built from them.
   - each acted-on `dials/<post>` → `{post, moves: [], note: "", status: "applied", pr, appliedAt}`.
   - one `history` doc per minister: `{post, summary, pr, at}`, summary in plain words.
8. **After the merge**, rebuild and republish the page (section 2) so "Now:" lines are current.

## 2. Rebuild and republish the page

```bash
python3 scripts/government/vibe-page/build.py
```

It fetches `origin`, reads the briefs and every `statements/<date>/<post>.md` from `origin/main`,
and adds the open government PR's posts (via `gh`) marked "Draft in PR #n". Rebuild after each
cabinet sitting you want to review, after any merge, and whenever Kai asks what the government is
saying.

Then Artifact publish `file_path: docs/government/vibe/index.html`. **From a session that did not
publish it, pass `url: https://claude.ai/artifact/FVp78gm6kSrWyVVj3NLpCA`** and read it first
(`action: "read"`), or the publish makes a new artifact. Omit `capabilities` and `icon` on a
republish so the page keeps its store (`db`, `user`) and icon. Do this whenever a brief changes,
including after a merged Cabinet Secretary PR.

## 3. Improve the page

The desk is meant to grow. Change `template.html` (or `build.py` for new brief fields), rebuild,
republish to the same URL. Rules that keep it working:

- Never put tweaks or history into the page source: they live in the store, which survives
  republishes. A schema change must still read the old docs, or migrate them with one ArtifactData
  `batch` (dump to `feedback/` first).
- Keep it vibe-shaped: feelings in, brief edits out. A new control that is really policy or
  scheduling belongs somewhere else; ask Kai before widening the desk.
- Note what changed and why in `docs/government/vibe/README.md`.
