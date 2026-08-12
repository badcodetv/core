# Wave B — live validation checklist

**Date:** 2026-08-12 · **Status:** not started
**Companion to:** [`2026-08-12-flow-automation-coverage.md`](./2026-08-12-flow-automation-coverage.md)

Wave A was written **blind** — one logged-in browser, strictly serial, so no coding agent
could check its selectors against Flow. This is where the code meets the real UI for the
first time.

**Run it in one session, serially, with the browser open.** Work down the list; fix-ups
are small commits, not new agent work.

---

## Before anything

1. `./scripts/flow-chrome.sh`, log in if needed, `flow_status` → `loggedIn: true`.
2. Reconnect the `flow` MCP (`/mcp`) — the server runs `tsx` on source, so none of Wave A
   exists in a running server process until it restarts.
3. Open `magic-money-tree-story`. It has real, cluttered media, which several checks need.

---

## The two that already cost us a session

### 1 · `POLICY_BLOCKED` aborts fast

Generate with a prompt naming a real person (that is the reliable trigger — it is how we
lost a morning on 2026-08-12).

- [ ] Returns `POLICY_BLOCKED`, **not** `TIMEOUT`
- [ ] Returns in **seconds**, not ~90s. This is the entire value of the task
- [ ] ⚠️ **Highest-risk check in this file:** `detectFailureCard()` finds the card via
      `getByText(ANY_CARD_RE)` — a text match, because **the card's DOM shape was never
      mapped**. Confirm it actually resolves. If it finds nothing, the classifier is
      correct but unreachable, and everything above silently reverts to timeout behaviour
- [ ] Run a video generation that legitimately queues under load → the `queued` state must
      **not** trip a false abort (a `warning Failed`-looking icon can show while queued)
- [ ] Confirm the `error` → re-approve-the-credit-gate retry still fires, now that it is
      routed through the classifier rather than its own inline `getByText`

### 2 · `flow_list_media` feeds `flow_create_character_from_media`

- [ ] `flow_list_media()` returns the gallery in order, with sane titles
- [ ] Titles are **single**, not Flow's doubled accessible name ("Man in suit holding
      papers Man in suit holding papers Image")
- [ ] Duplicate auto-captions appear as separate rows with distinct `index`
- [ ] `mediaId` populated where a `getMediaUrlRedirect` src exists
- [ ] `query` filters (selector `getByRole('textbox', { name: 'Search assets' })` — this
      one **is** confirmed, from a live snapshot 2026-08-12, despite the agent flagging it)
- [ ] Take a returned `title` and pass it straight to `flow_create_character_from_media`.
      **That round-trip is the point of the task** — if the title needs hand-editing to
      match, the parse is wrong

---

## Video — the largest blind surface

Nothing here has ever been automated. Expect breakage; that is the point of doing it once,
deliberately.

### 3 · The `tune Settings` panel (A6)

- [ ] Open Settings on a **fresh** project and confirm the recorded claim that it defaults
      to **Omni Flash** — the whole reason `ensureVideoSettings` exists
- [ ] ⚠️ **GUESSED:** the model menu's *option row* shape. `flow-video.md` maps the
      trigger's accessible name but never the opened menu. Code assumes a plain button
      named exactly for the model (`flow-client.ts:1020`)
- [ ] ⚠️ **GUESSED:** aspect/count tab scoping (`flow-client.ts:1006`). The model dropdown
      is scoped by text (`Omni Flash|Veo` can't collide with `Nano Banana`), but the aspect
      and count tabs use `.first()` with **no section scoping**. **Check specifically
      whether the panel also has an "Image generation default" section with identically
      named tabs** — if it does, `.first()` is landing on the wrong one
- [ ] `videoModelAlreadySelected` short-circuits correctly: a second `generateVideo` with
      identical settings should **skip** the panel entirely
- [ ] The `Veo 3.1 Lite` / `Veo 3.1 Lite[Lower Priority]` prefix trap — confirm asking for
      Lite does not select Lower Priority
- [ ] One clip end-to-end with explicit `model: "Veo 3.1 Quality"`, and **verify the
      returned clip is actually at that tier**. ⚠️ **Costs 100 credits** — do it once

### 4 · Animate targeting (A7)

- [ ] ⚠️ **The one behaviour change with no prior live proof:** `hoverElement` dispatches
      synthetic `pointerover`/`mouseover`/`mousemove` instead of a real hover. Confirm it
      actually reveals `more_vert`. If not, `openAnimateMenu` throws `ANIMATE_NOT_FOUND`
      cleanly rather than hanging, so the failure will at least be legible
- [ ] **On a cluttered project** (not a fresh one), confirm the before/after media diff
      picks the just-uploaded still. The sole-tile fallback is easy to hit on an empty
      project and proves nothing — the cluttered case *is* the original bug
- [ ] Time `waitForNewAnimateTile`: it should resolve in a few ticks, not creep to the 90s
      timeout

---

## Projects (A3)

- [ ] `flow_list_projects()` returns names + ids
- [ ] `flow_open_project({ id })` navigates cleanly (mirrors `ensureProjectRoot`'s proven
      pattern, so lower risk)
- [ ] `flow_create_project()` returns a real id, and the readback finds it within the grace
      window
- [ ] ⚠️ **GUESSED** (`flow-client.ts:188`, `:216`): the project-title textbox locator
      `getByRole('textbox', { name: /project name|untitled/i })`. **No accessible name for
      this field is recorded anywhere.** Check whether it matches anything at all — and if
      it does, whether it is genuinely the rename field or something unrelated
- [ ] ⚠️ **GUESSED:** the literal `"Untitled Project"` fallback, extrapolated from the
      confirmed `"Untitled Character"`. Verify the real default
- [ ] Rename is **expected to fail** (`flow-selectors.md:280` — fill and keystrokes both
      revert on blur). Confirm it fails *gracefully*: `flow_create_project` must return the
      project's **actual** name, never the requested one. If a rename approach is ever found
      that survives blur, that is a genuine discovery worth recording
- [ ] **Not covered by design:** the fully anchor-less div tile variant
      (`flow-selectors.md:269-276`). No selector for it exists anywhere, so
      `flow_list_projects` degrades (never throws) but cannot see those tiles. `id`-based
      open is the workaround. If you can reproduce the variant, **map it** — that closes a
      long-standing gap

---

## Images (A4) and characters (A5)

- [ ] `model` and `aspect` honoured per call on `flow_generate_image` / `flow_edit_image`
- [ ] The aspect prefix-trap pairs resolve correctly against the concatenated trigger label
- [ ] ⚠️ **Regression watch:** `refine()` previously asserted **no** project or image mode,
      deliberately trusting session state. Confirm the **no-arguments** path behaves exactly
      as before — an edit loop mid-session must not be disturbed
- [ ] `flow_list_characters()` finds `Economist` in `magic-money-tree-story`
- [ ] `flow_get_character({ name: 'Economist' })` returns info + both media ids, and
      harvests both views when given out-paths
- [ ] `hasBody` correctly distinguishes a Portrait-only character from one with a Body

---

## Cross-cutting

- [ ] **No `.click({ force: true })` regressions.** `grep -n "click({ force" packages/flow-mcp/src/flow-client.ts`
      should be empty — the file bans it, and Wave A fixed every remaining site
- [ ] The MCP tool list matches `server.ts` (the README count was wrong twice in one hour;
      it now says to count in the code)
- [ ] After all fix-ups: `npx tsc --noEmit` and `npx vitest run` clean

## Recording what you learn

**Every ⚠️ GUESSED marker resolved in this pass must be written into
`docs/superpowers/flow-selectors.md` or `flow-video.md`** with the real selector, and the
marker removed from the code. That is what turns this from a one-off validation into
knowledge the next session inherits — the same reason those maps exist at all.
