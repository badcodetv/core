# Google Flow: standing rules
> Moved out of Claude's per-machine memory on 2026-11-17 (the context reset) so both Kai and Jack have them.
> Mechanics and working habits only: no look or sound belongs here (that lives in a story's `badcode.md`).
> Originals: `archive/messy-context-2026-11-17/memory/`.


## One Flow project per story (2026-11-17 context reset)

Flow follows a reference image more than the prompt, and a project carries its references, Characters, aspect
and gallery forward. The MCP generate tools take no project: they use whichever project tab is open. So:

- **Before the first Flow call for a story in a session, open that story's project**: `flow_open_project` with the
  id in the story's `badcode.md` (*Look* → Flow project) or its scene's `scene.json` `flow_project`. A story with no
  project yet gets `flow_create_project`, and its id is written into `badcode.md`.
- **Never generate one story's shots in another story's project**, and never attach another story's still or
  Character as a reference.
- **The tab pool's worker projects count as the story's own** (Jack, 2026-11-18: "do this"). `scripts/scene/pool.mts`
  gives each worker tab a project of its own, made once per story and listed in `<media>/video/inbox/pool.json`; they
  only ever hold that story's stills and clips, and every job that casts a Character stays on the main project (w0).
  So **every video, for every story, goes through the pool** (Jack, 2026-11-18, twice: "make that a rule for all videos going forward"), even a single clip; never `run.mts` alone, never `flow_generate_video`: `FLOW_CDP_PORT=<port> npx tsx scripts/scene/pool.mts <scene-dir>`.
  A story's queue helper projects (`flow_queue`, below) are its own too: the queue only ever uses the helpers made
  for the project it was given.
- A plain `flow_generate_image` now refuses to run if a reference chip is left on the bar from an earlier call
  (`packages/flow-mcp/src/flow-client.ts`, generateImage). If it refuses, remove the chip in Flow or open a fresh project.

## 2026-11-18: three Flow tool bugs found and fixed (Jack: "why is flow failing so much")

- **`UPLOAD_STUCK`** was the tool, not Flow: the picker's finished option now reads "image <file> Image" and the tool
  waited for one starting with the file name; in the raw text Playwright matches there is no space after the icon word
  ("imageJS3-top-b.jpg"), so the match allows the word with or without a space. Fixed; a stuck upload now also reloads and retries once by itself, and a
  second failure lists the picker's options plus a screenshot in `/tmp/flow-upload-stuck/`.
- **`REFERENCE_COPY_ONLY` on a small edit** was the copy guard throwing away real results (a small added figure scored
  1.5-2.0; the cut-off was 3; true copies score 0.06). Cut-off now 0.5. If it fires, look in the Flow gallery first.
- **`run.mts` downloads failing with "Failed to find browser context"** (every clip, then the runner resends the batch and
  spends credits twice): the tab is in Chrome's default context; the download call now retries with no context id. If
  clips render but none download, stop the run and collect them with `HARVEST_KEYS=` (in submit order) before resending.
- After changing `packages/flow-mcp`, the running tool keeps the old code until `/mcp` → reconnect **flow**.

## Jack's standing rule for Flow stills — the free Nano Banana, never Nano Banana Pro

> **Updated 2026-11-18:** "Nano Banana 2" has left Flow's menu (Kai, 2026-11-17; the menu now reads Nano Banana Pro ·
> Nano Banana 2 Lite · Nano Banana 2.1). Use **`"Nano Banana 2.1"`** wherever this section says Nano Banana 2.
> 🔴 **Unchecked:** whether 2.1 costs credits like Pro or is free like 2 was. Read the credit count before and after
> the first 2.1 still of a session and write the answer here.

For Flow still images always use **Nano Banana 2**. Never switch to Nano Banana Pro, even if he says "Nano Banana Pro 2" in a request (Flow has no model by that name; he means the free one).

**Why:** Jack, 2026-10-01, after I ran ten Magic Money Tree style tests on Pro (about 12 credits each by an unchecked third-party figure): "always use nb2 since it is free."

**How to apply:** pass `model: "Nano Banana 2"` on every `flow_generate_image` / `flow_generate_batch` call — the tool's default is Pro, so omitting it spends credits. If a frame seems to need Pro, say so and let him choose. Related: `style-tests-stay-in-flow-prompts-in-repo`, `use-omni-flash-not-veo`.

## Never hand over an image-edit prompt — always write a complete fresh generation prompt with the changes folded in.

When a generated image needs changing, write a **complete new prompt** with the
change folded in. Never produce an `flow_edit_image`-style edit prompt ("Using the
provided image, change only…"), and never hand over isolated replacement blocks for
the user to splice — give the whole prompt, ready to paste.

**Why:** Kai's repeated experience is that editing an existing generation does not
work — the edit either ignores the instruction or drags the rest of the frame with
it. Stated twice: 2026-08-24 ("editing existing ones never work") and again the same
day as a standing rule ("always make new prompts instead of editing images going
forward"). Regeneration from a reference image is reliable; editing is not.

**How to apply:** Keep the accepted image as the reference attachment, restate the
entire prompt with the revision inside it, and end it with "Thanks."
See `every-flow-prompt-ends-with-thanks` and `flow-hand-driven-not-automated`.

Caveat worth remembering: `docs/flow/image-prompting.md` §6 and the `edit-panel`
skill still document the edit path. This preference overrides them in practice —
if that ever needs reconciling in the repo, raise it rather than silently following
the docs.

## Every Flow prompt Kai is handed — image and video alike — must end with \"Thanks.\" on its own line.

Every prompt written for Kai to paste into Google Flow ends with `Thanks.` on its own line — **image prompts and video prompts equally**. Where one prompt is pasted as two blocks (a reference block, then the main block), only the final block carries it, because the two are one paste.

**Why:** it is Kai's convention for the whole Flow prompt corpus (a sign-off, not a look), and it was already written into the Karen briefs' conventions before it slipped — I kept it on the plates and quietly dropped it from the clips, and he asked for it back on 2026-08-18.

**How to apply:** append it to the last line of every fenced prompt block, at the moment of writing rather than as a cleanup pass. Related: `flow-hand-driven-not-automated`.

## 2026-11-05 — never start the Flow Chrome from Bash (the command sandbox makes it render nothing); call flow_status and the flow MCP launches it

On 2026-11-05 the Flow browser was launched with `scripts/flow-chrome.sh` from a Bash call. Inside Claude's command sandbox Chromium loads no page at all (even `data:` URLs hang) and every `connectOverCDP` times out after 30s. Running it unsandboxed was refused. `mcp__flow__flow_status` launched its own browser outside the sandbox (`resolvedBy: needs-launch`), logged in, and scripts using `FlowClient.connect` worked at once.

**Why:** an hour went on debugging extensions, GPU and network flags before the real cause turned up.

**How to apply:** if CDP on 9222 is not up, call `flow_status` first; do not launch Chrome from Bash. If a CDP attach times out, check whether the browser was started from a sandboxed shell. See `flow-unusual-activity-refresh-retry`.

## One job per tab: a single job in the session's tab, two or more through the queue (Kai, 2026-11-18)

This replaces "never send Flow MCP calls in parallel" (Jack, 2026-11-17). That rule was right about **one tab** and
still is: two jobs in the same tab fight over its prompt box, uploads, overlays and downloads, and the results get
crossed or lost. What changed is that we no longer have only one tab.

- **One job** (a single still or edit): the ordinary `flow_*` tool, in the session's own tab. One `flow_*` call
  per message; wait for its result and check it before the next.
- **Two or more jobs** (a notes round that needs ten stills or edits redone, a mood board, a variations round):
  **`flow_queue`** with the whole list. It opens up to **10 tabs**, each in a Flow project of its own, and each tab takes
  the next job the moment it is free; jobs beyond 10 wait for a tab. Follow it with `flow_queue_status` (pass
  `waitSeconds` to wait), check every file as it lands, and stop a run with `flow_queue_stop`.
- **Every clip, even one** (Jack's rule above): `scripts/scene/pool.mts` (scene-animation), which runs the scene
  runner in several tabs. It takes its tabs from the same budget of 10, so a pool and a queue together never pass 10.
  Measured 2026-11-18: 25 Omni clips on 10 tabs in 6.9 min, about 2.3 min a clip with no slowdown at 10 tabs; ask for
  jobs in tens so the last round isn't half empty.
- **Never send several `flow_*` calls in one message.** They all land in the session's one tab. That is what broke
  on 2026-11-17, and it still would. Batch them into one `flow_queue` call instead.

How it stays safe (`packages/flow-mcp/src/queue-*.ts`):
- **Each tab has its own project.** A tab finds its results by diffing its project's grid, so no two tabs ever share a
  project at once. A story's queue work goes in that story's **helper projects** (made on first use, reused, listed in
  `.flow-queue/helpers.json` on each machine), so it never mixes with another story or with the session's own tab.
  A job that casts a Flow **Character** runs in the story's own project, because Characters live there; while such a run
  is going, make no `flow_*` calls of your own in that project.
- **Downloads can't cross.** Chrome has one download folder, and every attachment re-points it. Every attach, detach
  and download (MCP, queue, scene runner) takes one machine-wide lock (`packages/flow-mcp/src/lock.ts`).
- **Re-sending a run only pays for what is missing**: a job whose file is already on disk is skipped. Stills and edits
  are retried up to 3 times on a flaky failure; a video only when nothing was submitted yet. Policy blocks and refused
  uploads are never retried: rewrite them.
- **Google's own limit is per account and unmeasured.** If a run shows throttling (slow or refused jobs across every
  tab), ask for fewer `tabs`.

The incident behind the original rule:

On 2026-11-17 (Priority Lane round 19) three `flow_edit_image` calls sent in one message collided in the single Flow browser: two failed (a download into a missing temp file, a click blocked by another call's overlay) and one ran on into the background. Re-run one at a time, all three worked.

## Standing instruction — any research about how a Flow/Gemini engine behaves must be written into docs/google-flow/, not left in a story file or the chat.

Kai's standing instruction (2026-08-14): **always** write engine research into
`docs/google-flow/` at the time it is found — `omni-flash.md` for Gemini Omni
Flash (video), `nano-banana-2.md` for the image model. Not into a story's prompt
file, not only into the conversation.

**Why:** research is worth nothing the second time somebody has to find it again.
The trigger was a Karen river-drop clip that kept failing; the cause (Omni
supports no negative prompts, and `no`/`don't` phrasing backfires) was in a blog
post three clicks away and nobody had recorded it the first time.

**How to apply:** the test is *"would this still be true for a different story?"*
Yes → `docs/google-flow/`. No → the story's own file. Tag every claim with the
folder's evidence tier (`[vendor]`, `[runware]`, `[community]`, `[yt]`,
`[untested]`, `[confirmed <date>]`), date the section, cite the URL. The rule is
also written into `docs/google-flow/README.md` and the CLAUDE.md repo map, so
prefer reading those — they may have moved on from this note.

**⚠ Contested since 2026-08-14.** Kai independently built a second Flow tree,
`docs/flow/` (7 files, paired with the `flow-prompt` skill), on the branch that
became `badcodetv/core` main. Both trees now exist. The merge left an interim
split written into the CLAUDE.md repo map — `docs/flow/` = prompt craft,
`docs/google-flow/` = engine behaviour — but **a real consolidation call is still
owed by Kai and Jack.** Check the repo map before trusting the "always" above.

Related: `repo-records-intent-flow-holds-assets`.

## On Flow's \"unusual activity\" failure OR when the start-frame slot doesn't fill, refresh the page and retry ~10s later; no long back-off, no pause between clips.

**Every Flow retry starts with a real page refresh.** It applies in two cases:
- the **"We noticed some unusual activity"** failure card
- the **start-frame slot not filling** (`FRAME_SLOT_NOT_FILLED`)

Refresh, wait about **10 seconds**, retry. Don't back off for minutes, and don't pad the gap between clips.

**Why:** Jack, 2026-09-28, during the Camping mv2 26-clip Omni run:
- *"just needs a refresh and retry. Drop the long back-off … and cut the pause between clips."*
- then, *"remember to refresh the page when you retry, as well as when … the start-frame slot didn't fill."*

The card says "You have not been charged", so a retry is free. The old advice ("wait a couple of minutes") was too slow. Jack asked for a real refresh (`page.reload()`), not just navigating to the project URL again.

**How to apply:**
- In any automated Flow loop: refresh, then retry in ~10s, for a handful of tries.
- If one clip keeps failing, defer it to the end rather than stopping the run.
- Upload each plate once per project, then reuse it; re-uploading on every retry piles up duplicates.
- The rule is also in `.claude/skills/flow-automation/SKILL.md` §3.

Related: `flow-hand-driven-not-automated`.

**Fast detect (Jack 2026-11-09, "please remember that trick and save it"):** the image tools (`flow_generate_image`,
`flow_edit_image`) never read the "unusual activity" card, so each one sat out a 90 s TIMEOUT (half the tries on the
Paraguay presenter run). Trick: count "unusual activity" in `document.body.innerText` before submitting, poll every 2 s
while the generation runs, and the moment the count goes up, abandon it → real reload → 10 s → retry the SAME prompt
straight away (not deferred to the end). Seconds lost instead of ~2 min. Worked example:
`docs/stories/magic-money-tree/scenes/paraguay-presenter/cleanroom/r2/run_stills.mts`. Also: a real reload before
EVERY prompt kept most tries clean. The proper fix is to wire `detectFailureCard()` into the image wait loop in
flow-client.ts (failure-card.ts already classifies the card as `refused`); not done yet.

## Jack 2026-11-17 \"remember and save this so that it doesnt happen again\": a lookalike in Flow turns into the real famous person when the face is small or the prompt stacks that person's cues; two-step fix

An invented lookalike of a famous person (Priority Lane's Boris-alike minister, `BM9-b`) came out as the REAL person in rounds 8-11, with the invented man's photo attached and no name in any prompt. Jack's summary of why (2026-11-17):
- **The face was too small**: a face ~5-8% of the frame (~70 px, e.g. on a poster in a street shot) loses the reference, so Flow fills it from memory. Big faces (the car shots) kept the invented face.
- **The prompt described the real man without naming him**: each cue is harmless alone, together they are one person: his hair, nationality/class/job words ("English", "posh", "minister", "politician"), a "campaign" poster echoing his famous slogan, his photo-op trademarks (hard hat, hi-vis, thumbs up, pointing).

**Why:** four rounds and many takes were wasted before the cause was found; Jack asked for it never to happen again.

**How to apply** (any lookalike, any story):
- Never stack the real person's signature cues in a prompt (hair + job + nationality + slogan + props + poses). Drop job/nationality/"campaign" words and the photo-op props; write the invented face's own distinguishing features (nose, eyes, skin, age) even with a reference attached (a deliberate exception to `never-describe-a-referenced-character`).
- Never name the real person in a prompt OR in a clean-room writer's brief (the briefs named him in rounds 8-9).
- A face that will be small in frame: make it big first (e.g. the poster artwork alone, face ≥ a third of the height, a face-crop reference), then attach that finished image as the reference for the wide shot ("reproduced exactly").
- Check every output face for a real-person likeness before it goes on a board.

Evidence and sources: `docs/google-flow/nano-banana-2.md` (section "A small reference face on a poster drifts to a famous politician") and `docs/stories/shorts/priority-lane/cleanroom/r12/research-likeness.md`. See `clean-room-stills-work`.

## When a Character or reference image is attached, never describe the person's appearance — only what they are doing and their facial expression.

**If a Flow Character is cast or a reference image is attached, write nothing about how the
person looks.** No wardrobe, no age, no build, no hair, no skin, no stubble, no "a coat a size
too big". Say **"the man from the character reference"** and move on.

⚠️ **A "keep the same" clause is not a loophole.** *"in the same dark jeans and tan shoes as in
the reference image"* still names the garments, and Jack caught it on camping 8c(ii) the same day
he made the rule. **Naming a garment is naming a garment**, whatever verb wraps it. Write *"the
standing man from the reference image"* — the reference already holds the clothes.

**Do describe:** what they are doing (posture, action, where they are in the frame), and the
face as physical muscle description — brows, eyelids, mouth, where the eyes are aimed. That is
needed and it is not appearance.

**Why:** Jack, 2026-08-27, on camping 8c(i) — *"Bob's outfit is different… please don't describe
the character when there is a reference image or character attached, because Flow messes it
up."* This is the repo's own rule and it was being applied to locations but not to people:
`docs/google-flow/nano-banana-2.md` fourth pass §2 — *"Your job is not to restate all this"* —
a prose re-description **competes** with the attached reference and is a known drift source.
Same mechanism, same fix, for people as for sets.

🔴 **Condition changes count too (Jack, 2026-09-28, Camping mv2 s24).** *"Do not describe Tarquin, or any
character, let the @ Flow characters do that … it is messing with his image."* "Five years on: thinner, unshaven,
matted hair, filthy clothes" was cut. **With a Character cast, write no variant or condition prose at all.** This
overrides `variants-by-reference-not-flow-characters` whenever a Flow Character is attached.

**The one exception, and it is narrow:** when the figure is too small or too turned away for the
Character to bind at all (`nano-banana-2.md` §12 — a Character binds to a face), prose is the
only lever left. That was camping 8b's forty-metre long lens. **A face in frame at any workable
size means the reference carries it — describe nothing.**

Related: `always-run-shot-craft-then-flow-prompt`, `every-flow-prompt-ends-with-thanks`,
`always-new-prompt-never-edit-an-image`.

## Flow video prompts must ask for sound effects only, never dialogue — the narration is recorded separately and must not be competed with.

**Every Flow video prompt ends its audio line with `No dialogue, no music.` and asks only for
sound effects** — rain, tyres, wind, an engine, a trolley's wheels, a train.

**Why:** Jack records the narration himself afterwards. Any generated speech collides with it
and makes the clip unusable. Sound effects are the opposite — they are *wanted*, because
generated ambience makes the clip read as captured rather than rendered, and it sits
underneath narration without fighting it.

**How to apply:** write a specific, motivated SFX list for every clip — name what is actually
in the frame making the noise. Never write a line of speech, a voice, a shout or a
conversation into a prompt. Non-verbal human sound tied to an on-screen action is fine
(a laugh, a breath) as long as it carries no words.

⚠️ This **amends** Camping's standing rule in `docs/stories/camping/shot-list.md`, which read
*"never model-generated audio"* — generated SFX are now welcome; only dialogue is barred.
Related: `one-shot-at-a-time-still-then-video`.

**Second exception, 2026-10-07:** Jack asked for dialogue in The Bank Robbery clips too ("make the videos in a david lynch way, add dialogue in them"). So the exceptions are Money For Something and The Bank Robbery; every other film keeps the rule. Recipe that works: Frames, the speaker's Character chip attached, `He says:` then the words, no quotation marks, about twelve words a clip. Record: `docs/stories/bank-robbery/clips-v3.md`.

**2026-10-15 meeting: the Bank Robbery exception is withdrawn.** Films move to multi-narrator narration with no on-screen speech (`narration-not-lipsync`). Money For Something was not discussed.

**2026-11-10, Jack: "never do flow speech, only do the ai google studio thing where we do the lip sync tool."** Said for the BadCode Shorts (Priority Lane), worded as never. Talking characters are muted Omni clips dubbed with AI Studio voices through the `lip-sync-dub` skill (`dubbed-talking-clips-recipe`).

## Omni Flash video defaults — 720p x2 8s, an 8s prompt carries two beats, never suggest a 360p draft.

**Default Flow video settings: Omni Flash · 720p · x2 · 16:9 · 8s.** **Never suggest a 360p draft.**

**Why:**
- 360p: Jack, 2026-09-15: *"these always come out awfully."* A fresh 720p generation is a new take
  (no seed), so a draft can't predict it.
- 8s: Jack, same day, overruling a shorter default: *"the video being longer is helpful, so that when
  the narration goes over the clip's length, we have more video to put there as filler."*

**How to apply:** Omni pads one action stretched over 8s with drift, so **write every 8s prompt with two
beats**: the action the shot is for, then one small later beat (a gaze moving, a weight shift). Upscale to
1080p (free) only for delivery, and never pay for 4K. Settings go on the Settings line above the prompt
(`label-paste-blocks-with-destination-field`). Ruling: `docs/google-flow/omni-flash.md` → *Default
settings*. Related: `use-omni-flash-not-veo`.

## Assets (esp. Flow Characters) are often created by hand outside the repo; don't treat repo silence as \"doesn't exist\" or prescribe an all-in-repo workflow.

Kai and Jack routinely create things directly in Flow — Characters, images —
without any record landing in this repo. When the repo has no `**Flow Character:**`
line for a character, that means *the repo doesn't know*, **not** that the asset
doesn't exist. Ask for the name/id; don't conclude it needs creating.

Do not prescribe a workflow where every prompt and asset must be authored and
stored in the repo. Kai stated this explicitly on 2026-08-11: it is fine and
expected that some work happens manually in Flow.

**Why:** the repo is the canon for *intent* (story, beats, prompts, decisions);
Flow is the store for *assets*. Treating repo silence as absence produces wrong
conclusions (e.g. "Karen is uncast") and wasted regeneration — which Karen's
README already forbids, because her visuals are Jack's.

**How to apply:** when a prompt needs a Character, write a `**Cast:**` instruction
line naming it and ask for the exact Flow tile name — casting matches the tile
label with `exact: true`. See `karen-visuals-are-jacks`.

**⚠️ It is not just Flow — ElevenLabs too (2026-09-03).** The camping narration
sheet said *"the voice does not exist yet — no `voice_id` is recorded anywhere in
the repo."* I wrote that line myself, treating repo silence as absence. Jack's
screenshot showed **"Camping Narrator" already built and saved**, and a 1,212-credit
voice-design plan sitting in `voice.md` as work still ahead when it was already
paid. **Before writing "not yet made" about any external asset — a Flow Character,
an ElevenLabs voice, a Suno persona — ask.** The repo is silent about assets by
default; that is its normal state, not a finding.

**⚠️ `flow_list_characters` also lies (found 2026-08-14).** It scrapes
`a[href*="/character/"]` from the *project root*, but Flow's redesigned UI keeps
Characters behind a left-nav **Characters** tab, and `flow_open_project` lands on
All Media. So it returns `[]` on a project that has plenty. On 2026-08-14 this made
me sweep seven projects, report "no Karen Character exists anywhere", and propose
creating one — while Karen, Susan and Aarron were all sitting in the very project
Jack had given me. **A `[]` from that tool is not evidence of absence.** Click the
Characters nav item first, then call it. See `flow-mcp-selectors-stale-2026-08`.

## Run scripts/scene/run.mts (and any Flow download) with the Bash sandbox off, or every clip renders, bills and then fails to download (ENOENT playwright-artifacts)

2026-11-16 (Malevolent Force clips): run.mts started inside the Bash sandbox rendered 10 clips, lost every download (`download.saveAs: ENOENT … /tmp/playwright-artifacts-*`), thought the wave failed and resent the same five jobs, billing them twice. The files were in `~/Downloads` under Flow's titles (3 copies each), readable only unsandboxed.

**Why:** the browser writes downloads outside the sandbox's private /tmp (docs/flow/automation-2026-09-rebuild.md item 28).

**How to apply:** always launch run.mts with `dangerouslyDisableSandbox: true`. If it happens anyway, don't re-run: take the files from `~/Downloads` by time (newest grid tile first) and write recipe cards with `prov.py card`. Do not run Suno or a flow MCP batch while run.mts or another Flow download is in flight: a Suno run attaching to the same Chrome broke a Flow image download (2026-11-16). WSLg audio was wedged on 2026-11-16 too: `suno.mts record` needs Chrome relaunched onto the private PulseAudio (scripts/audio-server.sh, then pkill the 9222 Chrome and flow_status). Suno's workspace picker also fails on the first try after each Create; round.py aborts safely, retry with --only.

## Jack does not want test images saved into a Desktop folder; he reviews them in Flow, and only the prompts are kept, in the repo

When Jack asks for look or style tests in Flow, do not save the images into a folder on his Desktop. He looks at them in the Flow project. Keep the prompts in the repo so a liked one can be reused.

**Why:** 2026-10-01, Magic Money Tree style tests. I wrote seven stills to a Desktop folder and he deleted them: "Don't save them in a folder, I just mean remember the prompts, if I like them." By "make a file called that" he meant the prompt record, not an image folder.

**How to apply:** the flow tools need an `outPath`, so point it at the session scratchpad. Record every prompt in the story's repo file. What Jack ruled about a look goes in that story's `look.md`, not here (`no-house-style-story-files`). <!-- style-lint: ok (the rule's name) -->

## Standing preference — generate all Flow video on Omni Flash, not Veo 3.1.

Always use **Omni Flash** for video generation in Google Flow. Jack judges it clearly
better than Veo 3.1 on our footage.

**Why:** stated as a standing preference on 2026-08-25, from watching the actual
output across the camping shots. It overrides the repo's earlier
`Veo 3.1 Fast` default in `docs/flow/video-prompting.md`, which was ruled from a
bounded n=3 A/B on one plate and one near-static prompt.

**How to apply:** default to Omni Flash without asking. Two known limits worth
raising *at the time* rather than switching silently — Omni Flash **rejects a last
frame**, so the first+last-frame interpolation lock is Veo-only; and on 2026-08-25
Omni Flash on Frames lost both faces on a big expression arc where Veo held them
(see `always-new-prompt-never-edit-an-image` and the tab-rule bound in
`docs/google-flow/omni-flash.md`).

## Age/condition variants of a character are made with a reference image plus prose, never a separate Flow Character.

To make a character younger, older, more wrecked, etc., **attach a reference image
of them and describe the change in the prompt**. Do not create a separate Flow
Character per variant, and never treat a missing Character record as a blocker.

**Why:** stated by Jack 2026-08-25 — *"all we did was describe them with a reference
image to change them to younger/older/more homeless"*. The repo's character files
list Flow Character IDs, which had me repeatedly flagging absent ones
(`@Tarquin-2008`, `@Bob-2008`, Bob's wife) as work owed. They are not.

**How to apply:** write the whole prompt with the variant in prose — *"the man in the
reference image, here in his mid-twenties, the same bone structure but leaner in the
face…"* — and never name the character in the prompt. Pair with
`always-new-prompt-never-edit-an-image`.

⚠️ **Limit (Jack, 2026-09-28):** this prose-variant method is for a **plain reference image**. When a **Flow Character**
is cast, write no condition or variant prose at all; it messes with the Character. See `never-describe-a-referenced-character`.

## MANDATORY — load the shot-craft skill and docs/cinematography/ before ANY image or video prompt, including rewrites; then flow-prompt for phrasing.

**Before writing or rewriting any image or video prompt — every time, no exceptions, including a
small revision to a prompt that already exists — load the `shot-craft` skill and read the
matching file in `docs/cinematography/`.** Then, and only then, `flow-prompt` for phrasing.

Jack calls these "the cinematography skills". Two skills, strict order:

1. **`shot-craft`** → `docs/cinematography/` — what the shot should **be**. Gates, then a shot
   spec a human can argue with. `symptoms.md` when something is wrong, `principles.md` for the
   gates, `frame.md` for composition, **`stills.md` for any held image under narration**, `registers.md` for the register the story's `look.md` names.
2. **`flow-prompt`** → `docs/flow/` — how to **phrase** it so the generator obeys.

**Never do design and phrasing in one breath.** The skill says outright that the design step is
the one that gets skipped and it is the one that decides whether the shot is interesting.

**Why:** camping 8b(i) burned four generations and two rewrites on a face that kept reading sad.
Each layer caught a different fault, and none of them was reachable from the layer above:
`flow-prompt` found that the prompt *named the emotion* (Nano Banana has no negative-prompt
field, so "not sad, not troubled" is sad in the scene). `principles.md` found gate 1 and gate 2
failing — a still face asked to carry a change of inner state, in Camping's monumental frame with the
cost blurred out. **`stills.md` §1 found the real one:** every draft described a *finished*
action, and a resting pose dies no matter how well composed. The fix was to move the moment
earlier, not to describe the face harder.

**The gates are not all universal** (2026-10-29 audit): gate 1 (a still needs an unresolved question) and gate 3 (name the light source) are craft. **Gate 2, a visible cost in any monumental frame, is a gate only where the story's `look.md` makes it one** — GPOM's does; for another story, read its `look.md`. Whether it should hold everywhere is Kai's to rule.

**The three that catch the most:** a still needs an **unresolved question**; **geometry and event
must arrive together**; and **when a shot is not landing, delete a clause — never add one**.
Related: `every-flow-prompt-ends-with-thanks`, `always-new-prompt-never-edit-an-image`,
`one-shot-at-a-time-still-then-video`.

## Jack 2026-10-29 — the clean-room method for Flow stills (fresh web research + sealed writers who never see repo prompts) is what finally beat \"AI slop\"; use it for stills going forward

Jack, 2026-10-29, on the Bank Robbery MV ALT scene 1 round 2 stills: *"i love this new style, see this unlocks so much more stuff using this clean room approach, please remember this."*

The method that worked:
1. A web-only researcher (told not to read the repo) writes a fresh, tiered research note on the engine (here: Nano Banana 2.1 anti-slop).
2. Run the last round's prompts and write an honest "what came back" list of the slop tells (`baseline-r1.md`).
3. Sealed writers (one per staging/scene batch) read ONE brief file only: Jack's verbatim words + plain facts + the research + the failure list + the task. No repo prompts, no skill phrasing.
4. Run their prompts verbatim in Flow, put them on a picks page.

**Why:** repo/skill prompts carry habit wording that makes every image the same glossy AI look; the clean room broke it at once  (the look that came back is that story's, not a default).

**How to apply:** for Flow stills (and likely clips) when Jack wants new or better looks, default to this clean room; Kai's in-repo `variations` skill is the alternative `suno-clean-room-for-exploring`. Worked example: `docs/stories/bank-robbery/songs/mv-speakeasy-mint-alt/cleanroom/`. See `rules-are-a-loose-guide`.


**Breach found 2026-11-07 (Camping rappers, "like a geography teacher"):** the clip briefs pasted in a RECYCLED research file (Bank Robbery's action-clip research) and quoted Jack's note about another video, so restraint wording leaked through the clean room. Step 1 means fresh web research every job; never paste an old research file or another video's notes into a brief. Traps: docs/google-flow/same-clip-traps.md.

**Update 2026-11-17:** the writers must be truly sealed: run them with `scripts/variations/sealed-writer.sh` or the `clean-room-writer` agent, never `general-purpose` (which loads CLAUDE.md + this memory). See `sealed-writers-must-not-see-repo`.

## Kai drives Google Flow by hand (2026-08-16); but Jack (2026-10-21) wants Claude to run Flow itself and pick the best take.

Do **not** drive Google Flow through the browser/MCP automation by default when **Kai** is driving. Kai ruled on 2026-08-16 that it is too buggy and too slow to be worth it. Deliver **researched, copy-paste-ready prompts** instead and let Kai fire them in Flow.

**Why:** the Aug-2026 Flow redesign kept breaking the `@badcode/flow-mcp` client (character attach silently no-opping, stale selectors, page crashes), so each image cost several failed rounds. The prompt research is the part that has consistently produced accepted takes.

**How to apply:** for every plate, output one fenced block — the story's own preamble from its `look.md` if it has one (none is a default), then the scene, then `Thanks.` — with a short header above it stating cast (`@X` or none), time of day, and whether ingredients/frames or a reference image are attached. One plate at a time so Kai can edit before firing. Source the craft from `flow-engine-research-goes-in-docs-google-flow` (`docs/google-flow/`) and `docs/flow/`. Only touch the Flow automation if Kai asks for it explicitly.

**Jack, 2026-10-21 (Bank Robbery):** "just do the stuff in flow and we'll change it if it does not fit, just pick the best one." When **Jack** is driving, run the stills and clips through the Flow tooling yourself, choose the best candidate, put it on the timeline, and report what was picked and why. Handing him a paste block instead cost a round. Kai's 2026-08-16 rule above still stands for Kai.

---

# From Kai's machine memory (moved 2026-11-18)

> Kai's per-machine memory was archived to `archive/messy-context-2026-11-17/memory-kai/` on 2026-11-18.
> These are the Flow mechanics from it that were not already above. Slugs in brackets name the original file.

## Two no-candidate failures on a healthy session = a policy block: rewrite, don't retry [flow-policy-blocks]

Kai, 2026-07-25: over half of Flow prompts were being policy-blocked, and the MCP tools report a block as a timeout or
a missing candidate. If `flow_status` is fine and sibling prompts succeed, two failures on one prompt mean it is
blocked. The usual triggers: real brand names or legible logos; likeness phrasing ("same face, same bone structure");
stacked destitution words next to a real business; legible text attributed to a real institution. Rewrite: invented
near-miss brands, "character-design consistency" for faces, no legible real text, softer degradation words.
Not built yet: a distinct `POLICY_BLOCKED` code in `@badcode/flow-mcp`.

## Credits and the still gate (Kai) [flow-stills-are-free, flow-video-credits-plentiful, still-approval-gate, flow-video-count-one]

- **Stills cost nothing on Kai's account** (2026-10-20: "Generating will use 0 credits"); make several options per
  shot without asking. ⚠️ That was Nano Banana 2; whether 2.1 is free is unchecked (see the top of this file).
- **Video credits are plentiful for now** (Kai, 2026-10-23): no per-round caps for agents, no asking before a
  re-roll; still log spend in the ledgers. Drop this if Kai says credits are tight.
- **The gate that stays: Kai sees every still candidate and picks before any video credit is spent.** Contact sheet per
  subject, state your pick and every defect, then stop. (GPOM cut 4 shot a whole beat on the wrong plate when Claude
  picked alone.)
- **Video count follows Jack's default: x2** (see *Omni Flash video defaults* above). Kai, 2026-11-18: "take Jack's
  standard". This replaces Kai's older count-1 rule.

## Video model: Omni 1.2 Flash [omni-1-2-default]

Kai, 2026-11-09: Omni 1.2 Flash replaces Omni 1.1 Flash and any Veo 3.1 Fast/Quality use. Google retires Veo 3.1
Fast, Veo 3.1 Quality and Omni 1.1 Flash from Flow on 5 Dec 2026 (Omni 1.2 and Veo 3.1 Lite stay). An A/B came out
2 better / 2 ties / 0 worse. 1.2 costs about twice 1.1 at 720p; it can insert a cut of its own, so ask for one
continuous shot; length is a 3-15 s slider. Untested on 1.2: start+end frame, cast Characters, "Do not X" phrasing.
Record: `docs/google-flow/2026-11-09-omni-1-2-sweep.md`; re-test with `scripts/flow-tests/model-ab.mts`.

## Check every Flow output by content, never by the return value [flow-late-tile-shifts-batch]

A late tile from an earlier call can be saved under the new call's name. Seen in batches after a TIMEOUT (2026-10-16,
every file off by one) and in single `flow_generate_video` calls with no timeout (2026-11-10, three times in one
session). After every call check: a repeated `mediaId`, a duration that doesn't match `durationSeconds`, an md5 equal
to another file, and a 1 fps frame strip against the prompt. Rename by content, fix the recipe card's `source_id`, and
regenerate a missing tail item on its own.

## Video composer facts (settled by clicking, 2026-08-12; the UI has since been rebuilt) [flow-video-modes]

The rebuilt UI is `docs/flow/automation-2026-09-rebuild.md` (the old 2026-08 write-up is no longer in the repo).
- One composer, picked by the images passed: start only = animate, start+end = first/last frame, none =
  text-to-video. End-only does not exist. Omni rejects a last frame.
- Duration and count live in the compose-bar popover, which overrides the Settings panel (that is how `count` was
  once silently ignored).
- Refine a clip = its own *Reuse prompt*, which restores prompt + source still, so `flow_refine_video` needs only
  the `mediaId`.
- The asset picker lists only what the current mode can use (video mode lists no clips).

## Flow moved to flow.google.com (Angular rebuild, 2026-09-13) [flow-moved-to-flow-google-com, flow-wave-b-validation]

Source of truth: `docs/flow/automation-2026-09-rebuild.md`. Silent traps: an old media URL returns HTML with 200;
the tile `src` is a re-encode (harvest via More options → Download → Original size); an upload still "Uploading" lets
Add to prompt attach a different image; a bare refine prompt makes an unrelated picture.
- After editing `packages/flow-mcp`, `/mcp` reconnect `flow`. `.mcp.json` runs the server by a **relative** path, so
  it runs the primary checkout's source: a fix on a worktree branch does nothing until it is merged.
- Free test tiers (2026-09): Nano Banana 2 images and Veo 3.1 Lite [Lower Priority] video.

## The shared browser [concurrent-browser-sessions, playwright-mcp-hijacks-shared-chrome, runmts-tmpdir-downloads]

- **Never run `scripts/browser-channel.sh claim` in a session** (superseded 2026-09-28: it opened a second Chrome).
  Call `flow_status`; flow-mcp launches and holds its own channel. Branded Google Chrome on every channel (Kai,
  2026-09-13). Each channel's profile is a separate login.
- **Don't `/mcp` reconnect `flow` while another session is doing Flow work** (2026-10-23: it took over the shared
  Chrome's download path and cost the other session an hour). Check `ListAgents` first; a session that doesn't need
  Flow leaves the server disconnected.
- **Never give a subagent the Playwright MCP for general browsing.** It drives the live Suno/Flow Chrome on 9222; a
  `browser_navigate` replaced the Suno create tab and wiped the form (2026-09-30). Use curl/WebFetch, or a fresh
  headless `chromium.launch()`. If the MCP must be used: new tab first, never navigate an existing one.
- **run.mts downloads:** besides running unsandboxed (above), launch it as
  `TMPDIR=$HOME/.cache/pw-tmp FLOW_CDP_PORT=<port> npx tsx scripts/scene/run.mts …`. If the log shows `download-retry`
  with ENOENT, kill it at once. Duplicate takes in `video/inbox/dupes/` are often usable.

## Video lanes are layers: Flow animates the world, Premiere moves the camera, ffmpeg does the exact parts [hybrid-video-method]

Kai, 2026-08-26 (measured on Veo; untested on Omni 1.2). Write-up: `docs/video-fx/hybrid-method.md`.
- Animate the plate with the camera **explicitly locked**; camera translation is what triggers regeneration drift.
  Six of eight locked plates held at 0-2 px drift (vs 34-66 px).
- A **hinge-able surface in the near field** (doors, a louvre wall) drifts whatever the wording, tier or duration:
  plan it as a locked plate + procedural life in post. Read `docs/flow/video-prompting.md` §9 before the first roll.
- Move the camera in Premiere over the finished clip. ffmpeg is the only lane that puts text on screen.
- Length: chain clips (last frame of N → first frame of N+1); never pin an `endImage` to join them.
- On a frozen plate add moving grain; reverse or ping-pong only light, never settling matter.
