---
name: flow-automation
description: Use when DRIVING Google Flow — bringing the browser up, calling the flow MCP tools, recovering from a failed or hung call, running a batch, or changing @badcode/flow-mcp itself. Triggers on "generate this in Flow", "the flow call failed/hung/timed out", "flow_status says NOT_RUNNING", "run the batch", "why did that tool return nothing", "add a Flow tool", or any tool-level step inside make-comic, animate-slide, edit-panel, music-video-short, badcode-art-direction or new-image. Mechanics only — what to WRITE in the prompt belongs to scene-prompt; what it should LOOK like belongs to badcode-art-direction (panels) and new-image (brand imagery).
---

# Flow Automation

**The machine half of Flow.** Everything about making a tool call succeed, and nothing about
what to put in it.

## What this is not

Three jobs touch Flow and they are deliberately separate. Reaching for the wrong one is how
guidance drifts.

| Job | Skill | Question it answers |
| --- | --- | --- |
| **Driving it** | **this skill** | Why did the call fail? What tool? How do I not spend credits twice? |
| **Writing for it** | `scene-prompt` | What words go in the box? |
| **The BadCode look** | `badcode-art-direction` (panels) · `new-image` (brand) | What should it look like? |

If you are choosing adjectives, you are in the wrong skill.

---

## 0. Before you open the browser at all

🔴 **Ask: does anything in the world actually move?** Cloth, water, smoke, a crowd, a machine
turning, a face — or **only the camera**?

If only the camera moves, this is not a Flow job. It is a scale-and-crop on one still in `ffmpeg`:
free, any length, an exact ease curve, and **no artefact is possible** because it is one image.
Veo can only make it worse — GPOM scene 0 burned four generations on a camera-only move that post
rendered perfectly in five seconds.

And when Veo refuses a move, ask whether it will do the **inverse**. A push-in reversed in post is
a rigid pull-back, and that is how scene 0's reveal was finally solved.

**Plan every shot as `prompt → generate → transform`.** The ffmpeg step is part of the design, not
a rescue. Recipe book, all tested on our own footage:
[`post-production.md`](../../../docs/flow/post-production.md).

| Symptom | Try in post first |
| --- | --- |
| Camera-only move (push, pull, pan, drift) on a still | Eased `zoompan` — §3.4 |
| Veo will not hold a rigid subject on the move you want | Shoot the inverse, `-vf reverse` — §2 |
| Clip is too short for the narration | Ping-pong loop — §3.3 — or retime — §3.7 |
| Move is too fast inside 8s | Retime — §3.7 |
| A stray burned-in subtitle | Crop the bottom — §3.8 |
| Need the last frame to chain from | `-sseof` — §3.5 (or `flow_scene_save_frame`) |
| Every clip that lands | Strip audio — §3.1 |

⚠️ **The limit that decides it: Flow returns 1376×768 stills.** A post zoom is native only to about
**1.07×**; past ~2.5× it is visibly soft. A big reveal cannot be one post move off one Flow still —
`post-production.md` §4 has the table and the three routes around it.

---

## 1. Get a working browser

Everything runs through the `flow` MCP server. **Never puppeteer Flow by hand with the
Playwright MCP** — the tools exist because hand-driving is slow, and it fights the same
stalls documented in §4.

```
flow_status
```

| Result | Do |
| --- | --- |
| `{ loggedIn: true }` | Go. |
| `{ error: true, code: "NOT_RUNNING" }` | **Bring it up yourself. Do not bounce this to the user.** ↓ |
| `{ loggedIn: false }` | *Now* ask the user to sign in, in the window that just opened. Nothing else will work. |

```bash
# 1. background, never foreground — it does not return
./scripts/flow-chrome.sh
# 2. wait for CDP
for i in $(seq 1 20); do curl -s -m 2 http://localhost:9222/json/version >/dev/null && break; sleep 1; done
# 3. flow_status again
```

- Login persists in `.flow-profile/`, so a relaunch is normally already signed in.
- **Don't relaunch between generations** — the MCP caches its CDP attachment.
- It renders through WSLg, so the user can watch. That is often the fastest diagnosis available:
  **look at the window.**

Then open the project **once**: `flow_open_project({ name | id })`.

⚠️ **Characters and assets are project-scoped.** Cast in the wrong project and the character
silently does not exist. Confirm the project before generating, not after.

⚠️ **Prefer a project that is not full of test media.** The start-only animate path identifies
your upload by diffing the tile grid, and that diff degrades in a cluttered project
(`ANIMATE_NOT_FOUND` observed at ~30 items). `flow_create_project` gives you a clean one.

---

## 2. The tool surface — 22 tools

| Group | Tools |
| --- | --- |
| **Session** | `flow_status` |
| **Projects** | `flow_list_projects` · `flow_open_project` · `flow_create_project` |
| **Stills** | `flow_generate_image` · `flow_edit_image` · `flow_refine` · `flow_generate_batch` |
| **Video** | `flow_generate_video` · `flow_refine_video` |
| **Scene Builder** | `flow_scene_open` · `flow_scene_extend` · `flow_scene_extend_model` · `flow_scene_save_frame` |
| **Characters** | `flow_create_character` · `flow_create_character_from_media` · `flow_edit_character` · `flow_get_character` · `flow_list_characters` · `flow_character_body` · `flow_character_info` |
| **Assets** | `flow_list_media` |

**Which one:**

| You want | Call |
| --- | --- |
| A still | `flow_generate_image({ prompt, outPath, character? })` |
| A change to an existing still | `flow_edit_image` — reference-anchored, always from the golden |
| A same-session correction | `flow_refine` — cheaper than a fresh generation, keeps context |
| Many stills | `flow_generate_batch({ prompts, outDir, resume: true })` — ~12s/image on the cheap tier |
| Motion where something moves | `flow_generate_video({ startImage?, endImage?, motion, outPath, durationSeconds?, aspect?, model?, character? })` |
| "That clip, but slower" | `flow_refine_video({ mediaId, motion, outPath })` — needs only the clip's **mediaId**, not the source still |
| A camera-only move on a still | 🔴 **Not Flow.** ffmpeg. See §6. |
| A frame out of a clip | `flow_scene_save_frame` — `position: "end"` parks the playhead for you |
| Continue a clip from its own context | `flow_scene_extend` — ⚠️ runs at Veo 3.1 Lite whatever the source tier |

**Video mode selection is implicit**, from what you pass:

| Pass | Mode | Note |
| --- | --- | --- |
| `motion` only | text→video | |
| `startImage` | animate | The path with the most live proof. Falls back to Frames on `ANIMATE_NOT_FOUND`, visibly (`via: 'frames-fallback'`) |
| `startImage` + `endImage` | frames | Needs a Veo 3.1 tier — Omni Flash rejects a last frame |
| `endImage` alone | ✗ | Not a mode. Refused up front |

**Two constraints that decide the call before you write it** (Google-published, see
[`platform-controls.md`](../../../docs/flow/platform-controls.md) §1):

- **A cast character cannot run on Veo 3.1 Quality**, and forces 8s. Character shots top out at Fast.
- **Veo audio is always on and cannot be disabled.** Strip it: `ffmpeg -i in.mp4 -c:v copy -an out.mp4`.

---

## 3. When a call fails — the decision table

**Read the error's `hint` first.** Every failure mode names its own fix. Then:

| Symptom | Almost certainly | Do |
| --- | --- | --- |
| No candidate, session healthy, **twice** | **Policy block** | **Rewrite, never retry.** Triggers + rewrite table: `scene-prompt`. Glance at the window to confirm |
| `POLICY_BLOCKED` | Same, detected | Same. In a batch it is *one prompt's* problem — the batch carries on |
| Card reads **"Audio Generation Failed"** | Veo killed its own output over audio | **Retry unchanged.** Credits refunded. Not a prompt verdict |
| **"You're requesting generations too quickly"** | Rate limit, tightens with the day's volume | **Wait.** Rewriting changes nothing |
| **"We noticed some unusual activity"** | Anti-abuse | Wait a couple of minutes; **disable any VPN** |
| A stuck **"Pending"** card | Failed on policy or credits, left a husk | Manually retry or delete it. It will not clear itself |
| `TIMEOUT` after ~90s on a *control* | A hard wait on something that already vanished, or never arrived | §4 law 13. Look at the window |
| `TIMEOUT` on a *generation* | Queue, or a block | Veo Quality queues for minutes under load. Two clean failures ⇒ block |
| `ANIMATE_NOT_FOUND` | Tile diff ambiguous in a cluttered project | It self-heals via `frames-fallback`. Or use a fresh project |
| `ANIMATE_WRONG_SOURCE` | Guard caught the wrong still, **before credits** | Good. That is the guard working |
| `PROJECT_NOT_FOUND` on a project you can see | Project tiles rendered without `<a href>` | `goto` the known `/project/<uuid>` directly; reload through the error boundary |
| Tools hang **right after a video call** | Video mode poisoned the picker | Known and fixed, but if it recurs: any image call flips the bar back. §4 law 2 |
| `VIDEO_DURATION_UNAVAILABLE` | 10s asked of a Veo tier | 10s is Omni Flash only — and absent on our account since 2026-08-18 |
| `VIDEO_REFINE_NOT_A_MEDIA_ID` | You passed the `.mp4` path | Pass the **mediaId** `flow_generate_video` returned |

**You are not charged for a failed generation**, including an audio-stage kill. Protect the
clock, not the balance.

Full taxonomy: [`failure-modes.md`](../../../docs/flow/failure-modes.md) — Part A policy,
Part B0 the other empty results, Part B silent quality failures.

---

## 4. The eighteen laws

These are why the client looks the way it does. Every one was paid for live. If you are
changing `@badcode/flow-mcp`, they are the spec; if you are just calling tools, laws 1–5
explain most of what you will see.

1. **The compose bar's mode is global project state.** Video mode survives navigation, and in
   it the `add_2 Create` picker trigger does not exist and the picker lists stills only. So a
   tool that merely *reads* the gallery is not read-only — `listMedia` asserts image mode first.
2. **Settings persist, so assert them every call.** Duration, model, aspect, count all carry
   across turns and projects. One 4s clip silently makes every later clip 4s. Omitting
   `durationSeconds` asserts 8 rather than leaving it alone.
3. **Read the state back off the label. Never trust a click.** The trigger concatenates
   model + aspect + count, so the whole config is readable without opening anything.
4. **Absent ≠ disabled.** The 10s tab is *missing from the DOM* on Veo tiers, not greyed out.
   A click-if-present guard is then a silent no-op that returns a healthy clip you already
   paid for. Same shape as `x1` vs `1x`, which billed two images and harvested the straggler
   into the *next* turn at the *previous* turn's aspect.
5. **Accessible names glue the Material icon ligature to the label with no space.** Submit is
   `arrow_forwardCreate`. Match `/arrow_forward\s*Create/i`; a literal space matches nothing.
   This one fact invalidated a whole generation of spike-era selectors.
6. **`getByRole` does not work inside the Agent settings panel.** It sits under an
   `aria-hidden` ancestor: `getByRole('tab')` counts 0 while `button[role="tab"]` counts 15.
   Use CSS + text in there. `getByText` still works.
7. **Coordinate-based clicking is untrustworthy on WSLg** — the window scales coordinates
   (`innerWidth` 3828 vs a 1538px screenshot), so a force-click aimed at "Add to Prompt" landed
   on "Upload media". Everything goes through in-page `evaluate`. Per control: plain buttons →
   native `el.click()`; Radix menu triggers → synthetic `PointerEvent`; Radix tabs → `focus()`
   + `MouseEvent`. Menus open on **pointerdown**, so a synthetic `click()` misses them.
8. **Never `waitForEvent('filechooser')`.** With a second Playwright client attached the
   chooser hangs. Set the hidden input directly:
   `locator('input[type=file][accept*=image]').setInputFiles(path)`.
9. **Detect a NEW media name, not "any media".** Snapshot names before submit, wait for one not
   in the set — and wait for the grid to *settle* first, because it hydrates after load. A
   text-to-video call once returned a healthy mp4 that was byte-for-byte an older generation.
10. **Fail closed on ambiguity.** Animating the wrong still returns a real clip, a real media
    id and a real file, with no error and nothing downstream able to notice. Guess and you ship
    it.
11. **Look at a frame. File size proves nothing.** Our own video smoke test passed on the wrong
    picture. Same rule at review time — §6.
12. **Scope a hover menu to its own tile's card.** Never `.first()` (the first `more_vert` on
    the page is the project menu) and never `:near()` (matches a control near *any* tile). A
    clip card is also not a still card: hovering swaps the `img` out for a `<video>`, so anchor
    on `video[src*=<mediaId>]` after the hover, not on the element you hovered.
13. **A hard wait on a control that already went burns the full 90s.** The single most common
    bug family here. "Add to Prompt" closes the picker by itself; the credit gate's options are
    plain `<div>`s with no role at all. **Wait for either outcome**, and make waits conditional.
14. **Every entry point has two states: empty project and populated.** Zero characters goes
    straight into the composer; one or more requires clicking the `New Character` tile first.
    Code tested only on an empty project ships broken and passes review — that is exactly how
    `createCharacterFromMedia` shipped.
15. **Navigation clears the bar and resets the pickers.** Model reverts to Nano Banana 2, chips
    detach, frame slots wipe. That is also the reliable way to *guarantee* a clean bar before
    `Reuse prompt`.
16. 🔴 **One browser, one generation at a time — and a second call kills BOTH.** Added
    2026-08-20 after doing exactly this. A `flow_generate_video` that runs past ~116s is moved
    to the background, and it *keeps owning* the cached CDP attachment, the compose bar and the
    asset picker. Firing a second call into that same bar **overwrites the prompt the first one
    is still waiting on**: the second died with a 90s picker timeout on a file that was
    definitely present, and the first ran its full 480s clock and returned TIMEOUT. The dump
    proved it — an empty compose bar carrying the *second* call's Frames slots, no error card,
    no credit warning, account healthy.
    **A backgrounded Flow task is not free parallelism. Wait for it.** Do non-browser work
    instead. And read the timeout dump before retrying: the failure impersonates a wedged
    picker, so the reflex (reload and retry) disturbs the job that is still working.
17. **99% is not done, and the 480s clock can expire while Flow sits there.** Two runs on
    2026-08-20 returned TIMEOUT with the gallery tiles reading **99%** — rendered, billed, and
    never harvested, with no tool to fetch an existing clip afterwards. The dump is what proves
    it: check the tiles for a percentage before assuming a block or a credit problem. Suspect it
    more as a project fills up (ours was ~25 items; harvest is known to degrade around 30).
    Cheapest guard: keep projects small and one shot per project when a shoot gets long.
18. **The compose-trigger label gains segments over time.** It read `Video · 8scrop_9_16x1`; on
    2026-08-20 it read `Video · 720p · 8scrop_16_9x2`. A parser that walks from the mode to the
    first digits will break on the next segment Flow adds. Anchor on the token *and its
    neighbour* (`(\d+)s(?=crop|$)`), never on position. This one aborted every video call while
    reporting the opposite of the truth.

---

## 5. Batches and unattended runs

`flow_generate_batch({ prompts, outDir, resume: true })` opens the project once and fires the
list in one session. **Always pass `resume: true`.**

1. **Plan every prompt first**, and get them agreed. That is the gate; everything after is
   machinery. (Prompt planning is `scene-prompt`'s job, not this skill's.)
2. **Batch-generate.**
3. **Review all N together**, never one at a time.
4. **Iterate only the weak ones** — `flow_refine` for a same-session correction, `edit-panel`
   once it is a finished panel. Never regenerate the batch.

### The unattended loop

A batch does not fail all-or-nothing. It returns `{ items, failed, partial }`, and the two
failure kinds mean **opposite** things:

- **`POLICY_BLOCKED` is about that one prompt.** The batch records it and carries on. It leaves
  a hole, and the hole is a prompt that needs **rewriting, never retrying**.
- **Anything else** (`TIMEOUT`, `SUBMIT_FAILED`, a raw Playwright error) is about the
  **session**. The batch stops there deliberately, because a wedged page fails the next prompt
  too.

```
round 1: flow_generate_batch({ prompts, outDir, resume: true })
         │
         ├─ failed is empty ────────────────────────────────► done
         │
         ├─ POLICY_BLOCKED entries ──► rewrite those prompts in place (scene-prompt),
         │                             then re-run the SAME list, resume: true
         │
         └─ any other code ──────────► the session is hurt, not the prompt.
                                       flow_status, re-open the project, re-run
                                       the SAME list, resume: true
```

**`resume: true` is what makes re-running free.** It skips any prompt whose output file is
already on disk, so round 2 only pays for the holes. Same prompts, same `outDir`, every time.
Delete one bad image and re-run to regenerate exactly that one.

**Stop after three rounds** and report what is still missing. A prompt that survives two
rewrites is a *content* problem, not a prompting problem — take it back to the human.

⚠️ **Never re-run a `POLICY_BLOCKED` prompt unchanged**, even rounds later. It cannot pass, and
it costs a full turn-timeout to learn that again.

Rate limiting tightens as the day's volume grows, so a batch that flew this morning may crawl
this afternoon — expected, not a fault.

---

## 6. Verify what came back

**Never judge a clip from sampled frames.** A door that swings for 1.5s sits between them, and
you will report success on a broken clip — done, 2026-08-18.

```bash
scripts/video-contact-sheet.sh clip.mp4              # every frame at 4fps, one image
REGION=left scripts/video-contact-sheet.sh clip.mp4  # crop a band + lift exposure
```

Near-black BadCode frames hide motion at full-frame scale — use `REGION` when the suspect
detail is small or dark.

🔴 **A camera-only move on a still is not a Flow job.** If nothing in the world actually moves,
it is a scale-and-crop on one image: no 8s cap, no 720p ceiling, no artefacts, no credits.
Render it with ffmpeg. Worked example:
`docs/stories/gitpush-origin-master/storyboard/img/s00-pullback-post-12s.mp4` — 12s at 1080p,
after Veo failed at it four times.

---

## 7. Changing the automation

Source: `packages/flow-mcp/src/`. Pure modules with `.test.ts` siblings (vitest, 226 tests);
`flow-client.ts` holds the Playwright; `server.ts` registers tools and maps errors.

- **The two automation docs are the spec.** `flow-client.ts` cites
  `automation-images.md` by **line number** in ~19 places, so **do not reflow those files** —
  append and mark corrections in place, dated, as they already do.
- **A new tool needs an MCP restart** before this session can call it.
- **Smoke scripts are the proof**, not the tests: `packages/flow-mcp/src/smoke-*.ts` each drive
  one live mechanism. Add one for any new mechanism, and say what it cost in credits.
- **Prove a fallback by forcing it**, not by waiting for the failure — that is how
  `frames-fallback` was verified.
- **Make degradation visible.** `via: 'frames-fallback'` is on the result for a reason: a
  degradation nobody can see is one nobody fixes.

---

## 8. Write back what you learn — every session, not eventually

🔴 **This is part of the job, not admin after it.** Every hour at the Flow face produces at least
one fact that cost credits and wall-clock to discover, and the *only* thing that makes the next
session cheaper is that the fact got written down. A finding that stays in a chat transcript is
a finding we will pay for again.

**Route it by kind. Three destinations, and the split is deliberate:**

| You learned… | Goes in | Example |
| --- | --- | --- |
| **How to drive it** — a selector drifted, a control lies, a call collides, a failure impersonates another | **§4 of this skill**, as a new numbered law | Laws 16 (concurrent calls kill each other) and 17 (the label gained a `720p` segment) |
| **How the model behaves** — what wording works, what it invents, what a tier does | [`docs/flow/`](../../../docs/flow/README.md), in the file that owns the subject | "describe the middle" → `video-prompting.md` §4; the hinge fix → §9 |
| **What happened on this shot** — takes, verdicts, why one won | The story's scene file, `docs/stories/<story>/scenes/` | `s00-awakening.md`'s four-run comparison table |

**Rules for writing it back:**

1. **Correct in place, and say the old thing was wrong.** Don't quietly overwrite — a reader who
   remembers the old rule needs to see it struck. `video-prompting.md` §9 keeps the refuted
   version visible above the fix.
2. **Carry the evidence with the claim.** What was run, how many times, on which tier, what the
   comparison was. A rule with no measurement behind it becomes folklore in a month.
3. **Say when it is weak.** `n=2, observed not established` is a useful thing to read. An
   overstated finding is worse than none, because it stops the next person testing.
4. **A finding that contradicts an existing rule is the most valuable kind.** Write it up loudly
   and flag it to the human rather than resolving it quietly — several of our rules are measured
   on this account and should usually win over a blog, but not over a fresh measurement.
5. **Update the count in the heading** when you add a law, and check nothing else cites the old
   number.

**The test:** could someone opening a fresh session tomorrow hit the same wall? If yes, it isn't
written down well enough yet.

---

## Knowledge base

| File | What | Read when |
| --- | --- | --- |
| [`automation-images.md`](../../../docs/flow/automation-images.md) | Stills: selectors, DOM roles, the asset picker, characters, reference images, harvest | A still tool misbehaves, or you're editing the client |
| [`automation-video.md`](../../../docs/flow/automation-video.md) | Motion: completion signals, the compose popover, Frames mode, what a finished clip offers, refine, the picker traps | Same, for video |
| [`platform-controls.md`](../../../docs/flow/platform-controls.md) | Google's feature matrix, credits, watermarking, model auto-switching | Planning a shoot or a budget |
| [`failure-modes.md`](../../../docs/flow/failure-modes.md) | Full failure taxonomy | §3 didn't cover it |
| [`post-production.md`](../../../docs/flow/post-production.md) | 🔴 **The ffmpeg half.** The Veo-or-post decision, tested recipes, the resolution ceiling | §0 — before generating, and after every clip lands |
| `packages/flow-mcp/README.md` | Tool schemas and the client's own contract | Editing the server |

⚠️ **Both automation docs are chronological logs, not manuals.** They record what was learned
and when, corrections marked in place — which is why they are trustworthy and why they are hard
to read straight through. **§4 above is the distillation**; go to the files for the DOM detail
behind a specific failure, not to learn the system.

**Known stale, as of the 2026-08-20 audit** (left in place because they are the record of why
the code exists, not because they are current):

- Both files open with a **"TL;DR — the loop that works"** describing a hand-driven
  Playwright-MCP session with `browser_run_code_unsafe`. The MCP does all of it now. Read them
  as history.
- They refer to a **`badcode flow` command** that was never built; it became `@badcode/flow-mcp`.
- `automation-images.md` **"Still to spike"** items 3 and 4 are answered — aspect is a per-turn
  control (`crop_` popover) and rate limiting is documented in `platform-controls.md` §9.
- The **Characters** section carries two superseded recipes above the current map. The ⚠️
  markers are accurate; read to the bottom of the section before acting on anything in it.
