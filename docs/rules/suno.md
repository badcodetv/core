# Suno: standing rules
> Moved out of Claude's per-machine memory on 2026-11-17 (the context reset) so both Kai and Jack have them.
> Mechanics and working habits only: no look or sound belongs here (that lives in a story's `badcode.md`).
> Originals: `archive/messy-context-2026-11-17/memory/`.

## In Suno, an Exclude-box ban cannot beat a Style-box or lyric-cue instruction asking for the same thing — delete the positive words first, and use the ban only as the third line of defence

**Found on Camping, 2026-09-23** (`docs/stories/camping/songs/camping.md` §v6.59): a word sat in the Exclude box the whole time and the thing still arrived, because the Style box and three lyric cues asked for it in the positive. A second time the same day, a banned quality was summoned by one phrase in the Style box (asking the voices to hype each other summons a hype man's shouts).

🔑 **A ban only removes an option the model was not already being pushed toward.** Lyric cues out-vote the Style box. The reliable fix is a three-part stack, in this order: **(1) a positive target in the Style box** that the unwanted thing cannot satisfy, **(2) matching section cues**, **(3) the bans last** ([Jack Righteous](https://jackrighteous.com/en-us/blogs/guides-using-suno-ai-music-creation/stop-suno-adding-crowd-vocals-choirs-backing-voices)).

**How to apply:** when something unwanted keeps arriving, grep all three boxes for the positive words that summon it before touching the Exclude list, and check the sheet's own listening notes for a known leak. The words themselves belong to the story's `sound.md`, not here. Related: `audit-inherited-excludes`, `never-write-uniformity-words`, `describe-the-song-not-the-box`.

## Every round, check the inherited Exclude list against the brief — a ban carried forward from an old box can ban the exact thing being asked for

Found on Camping, 2026-09-21/22: six bans across four rounds, carried forward from an old box or from cross-lane bans, were blocking the very thing the next brief asked for (the table is in `docs/stories/camping/songs/camping.md` around §v6.56).

🔑 **A cross-lane ban is the most dangerous kind:** banning each lane's instrument in every other lane forces spread, and those bans then travel forward as if they were rules.

🔑 **An exclude list is a set of instructions that outlives the reason it was written.** Before generating, read the ban list against this round's brief and delete whatever is now fighting it. A ban costs nothing to remove and can cost a whole round to keep.

Related: `describe-the-song-not-the-box`, `a-ban-loses-to-a-positive-instruction`.

## To build on a Suno take you like, write a prompt that describes what it SOUNDS like — its own Style box is not a description of it, because drift made the parts you like

Found on Camping, 2026-09-21: re-running a liked take's own boxes lost everything liked about it, because every liked feature had been drift against those boxes, and drift did not repeat. A measurement that had sat unread for three days showed the structural difference (the liked take had four breakdown/drop cycles; every rewrite had one). Record: `docs/stories/camping/songs/camping.md` §v6.50–53.

🔑 **The method: describe the OUTPUT.** Practitioner reverse-prompt checklist — tempo · dominant texture · vocal character · mood/era · production quirk — filled in from measurement, not memory ([songsmith.studio](https://songsmith.studio/blog/suno-reference-track-prompt-builder)).

**How to apply:** before building on a liked take, (1) measure it or re-read the measurement, (2) write the description from what it sounds like, (3) self-critique that description against the story's standing rules (its `sound.md`) before generating. Related: `never-write-uniformity-words`, `short-boxes-keep-the-drift-space`.

## In a Suno prompt, a uniformity word (never, throughout, from here to the end, every bar) is a flatness instruction — scope the guard to where the bug was instead

Found on Camping, 2026-09-21 (Jack: *"they all sound flat and boring"*): three clauses we had written to fix real bugs each told the record never to change. The rule, the table and the corollary (differentiate repeated section headers; make the last one `[Final Chorus]`) are in `docs/suno-gpt/files/suno-tag-mechanics.md` (~L245), promoted there the same day.

🔑 **Watch the words `never`, `throughout`, `from here to the end`, `every bar`, `start to finish`.** Scope the guard to where the bug actually was.

**Same family:** the Lyrics box out-votes the Style box on casting. When the cast or the arrangement changes, rewrite every section cue and assert the old words are gone in code (a no-op replace looks like success). Related: `a-ban-loses-to-a-positive-instruction`.

## When a liked Suno take was made by drift, every extra instruction closes the space that made it — keep the boxes at the liked take's size and fix by deleting

**Measured on Camping, 2026-09-23** (`docs/stories/camping/songs/camping.md` §v6.60–61): after rounds of precise, individually justified fixes, the rejected round's Exclude box and lyric cues were roughly twice the liked takes' size, and the result stopped resembling either. The liked features had all been drift against the boxes, so the boxes described the space the take drifted inside, not the take. The same failure happened twice. It is also trap 12 in `docs/suno-gpt/same-song-traps.md`.

**How to apply, on any song with a liked take:**
1. Measure the liked take's boxes and treat those lengths as a budget, not a floor.
2. Fix by deleting: a new complaint is a reason to remove the instruction causing it, not to add a counter-instruction.
3. After three or four rounds of accretion, rebuild from the liked take's own sentences and re-add only what a named complaint requires.
4. Style Influence is the other drift lever, but move box length first so only one thing changes.

Related: `describe-the-song-not-the-box`, `audit-inherited-excludes`, `never-write-uniformity-words`.

## BadCode's Suno account is kaiyadavenport@gmail.com via Continue with Google; Suno is single-session so only one account fits the Chrome profile.

The Suno account that owns the BadCode workspaces is **kaiyadavenport@gmail.com**, signed in
with **Continue with Google** (not email/password).

Suno's Clerk config has `singleSessionMode: true` — there is **no account switcher**, so the
`.flow-profile` Chrome can hold exactly one Suno login at a time. On 2026-09-05 it was found
signed in as `jacktttt330@gmail.com` instead, which cost several rounds to spot: the create
page loads normally with someone else's `?wid=` and silently falls back to their own default
workspace.

**How to check in one call, from the page context:**
an authenticated `fetch('https://studio-api.prod.suno.com/api/project/<wid>')` with
`Authorization: Bearer <await window.Clerk.session.getToken()>` returns **403** when the
signed-in account does not own that workspace, and the account itself reads from
`window.Clerk.user.primaryEmailAddress.emailAddress`.

**Switching accounts is a human step.** The auto-mode classifier blocks both `Clerk.signOut()`
and clicking the profile menu, so hand over the two clicks: profile name bottom-left → Sign out
→ Continue with Google → pick the address. Related: `flow-hand-driven-not-automated`.

## Jack 2026-10-22 — Suno prompts written inside the repo kept making the same song; exploring rounds now go through the variations skill, run verbatim

Jack, 2026-10-22: "remember that the repo and suno skills just make the same song, so it is useful to use the clean room or basic version." Learned on The Bank Robbery song: 400+ takes written inside the repo came out as one voice. Since 2026-10-28 the method is Kai's **`variations` skill** (`scripts/variations/round.py`, Suno and Flow); the old `sealed-writer.sh` / `sealed-round.py` are retired.

**What the round must keep (each one cost Jack a round when broken):**
- The writers get raw files only: the user's words verbatim, the lyric words, one fresh listen, the reference's own record. Never my paraphrase, never old listen logs or old prompts.
- Writers never see each other's prompts. A failed sameness gate is a STOP: send it back, never explain the shared part away.
- I never write, retype, edit or "improve" a prompt; the round runs verbatim. My checks are only that the lyric words are unchanged and that the story's own standing rules hold (they are in its `sound.md`).
- Vary the delivery category per prompt, never just the accent. A liked voice sentence moved onto another prompt loses its nationality.
- Agent-tool subagents spawned in the repo inherit CLAUDE.md and memory; "ignore them" does not unload them.

**How to apply:** read `docs/suno-gpt/same-song-traps.md` first; a new failure gets a row there and a guard in the script. The story's style lives in its `sound.md` (`no-house-style-story-files`). Suno's cookie banner covers Create (Reject All first). Related: `bank-robbery-jack-song`.

**Update 2026-11-17:** the writers must be truly sealed: run them with `scripts/variations/sealed-writer.sh` or the `clean-room-writer` agent, never `general-purpose` (which loads CLAUDE.md + this memory). See `sealed-writers-must-not-see-repo`.

## Jack 2026-10-22 — never use Suno Cover (Remix → Cover) for his songs; covers don't work

Never use Suno Cover (Remix → Cover, `suno.mts narrow`) on Jack's songs. Jack, 2026-10-22: "covers dont work please dont use them thanks" — said while we were trying to put the Bank Robbery liked take's music under new voices.

**Why:** in his experience a Cover doesn't give the result; it was the route being used to keep the music of ed6dd946 (`bank-robbery-jack-song`).
**How to apply:** fresh Creates only; to keep a take's music, use its stored prompt at Variety Off, or ask before trying stems / Add Vocals (a Remix, not a Cover — still ask).

## Once a new Suno prompt round is written and loaded, run the pair straight away — don't stop to ask before spending credits.

Once I've written a new Suno prompt and loaded it, run the pair right away (`suno.mts pair`, weirdness per the sheet). Don't stop at "loaded, say do it". Then report the take links and record them in the sheet.

**Why:** Jack, 2026-09-16, during the Camping r24–r26 rounds: *"Always do it once you have made the prompt going forward rememeber that please."* He said "do it" after every load anyway, so stopping to ask only slowed the loop down.

**How to apply:** This is standing permission for the suno-automation rule "credits are Kai's to spend — don't run pair unless asked". It covers prompt rounds the user asked for in a Suno session. Still stop for problems: if the load assertions fail, or another session owns the form. Still report credits before and after. Related: `suno-account-is-kais-google-login`.

## On Suno v6 always set Duration explicitly — Auto runs long, and a set target is obeyed to about a second.

**Proven 2026-09-18 (Camping r47 vs r48, same lyrics, same day).**

- **Duration Auto on v6 runs long** — takes came back at **4:38 and 4:55** from a song whose
  reference take was 2:46.
- **A set Duration is obeyed tightly**: a 195 s target gave **12 takes out of 12 at 3:14–3:16**,
  across three different Style boxes and two weirdness settings. About ±1 s.

This supersedes the v5.5-era reading that duration "shortens but does not obey". **Always set the
number**, aiming slightly above the target, since it still shortens more readily than it stretches.

⚠️ Still unknown: whether Custom duration doubles the credit cost (r17's suspicion) — the credit
counter read `null` on both rounds, so two uses have gone by unpriced. Related:
`listening-setup-jacks-machine`.

⚠️ **The ±1 s obedience loosens when the target squeezes the words (2026-09-21, Camping r55).** At
195 s the hit rate was 12/12 then 24/24 within a second. At **155 s** — the same ~60 lines, 20%
less room — nine of fourteen landed at 2:34–2:36, but `action` w30 came back at **2:43** (both
takes) and `adventure` w30 at **2:58**, a 23-second overshoot. ⬜ Unverified as a rule; one more
round decides it. **Practical effect: when duration is being used as a pacing lever, check the
returned length before blaming the prompt** — a long take simply had more room to slow down in.

## Jack 2026-11-15 — Suno tracks for shorts are music and sound effects only, never dialogue/speech unless he asks specifically

Jack, 2026-11-15 (The Envelope, after a round whose takes all spoke the line): "never should be dialogue on these suno tracks for shorts unless i ask specifically, please only do music and sounds, not dialogue."

**Why:** he wants the Suno track to be the score and the sounds; spoken lines are a separate decision.
**How to apply:** every shorts Suno round is instrumental (an empty `instrumental` file in the variations round folder, no `lyrics.txt`); say "no voice, no words" in the facts. This narrows Kai's "speech mode" idea in `shorts-audio-through-suno`; Suno still makes the stings and the bed. Jack, 2026-11-15, straight after: "only dialogue should be ai studio" — every spoken line in a short is an AI Studio voice (`voice-casting`), never Suno.

## Kai 2026-11-13, all shorts — audio comes from Suno (speech mode, stings, foreboding bed); order is script → Suno track → pictures; AI Studio voices still sound AI

For every BadCode short, build the sound in Suno (Jack 2026-11-15: music and sounds only, no dialogue unless he asks, see `shorts-suno-no-dialogue`). Order: script first, then the Suno track, then the pictures built around it. Where AI Studio voices are still used, use the good model (Kai's upgraded key) and pick from 4–5 takes (`voice-casting skill`).

**Why:** Kai: "ears are way more sensitive than eyes"; the AI Studio voices still sound like AI, and the balaclava gets round lip-sync. No Master Recording sounded AI because it was on the free voices.
**How to apply:** each short's own sound.md still decides how it sounds (`no-house-style-story-files`). Use a Suno workspace per short (`short-<slug>`). Source: `meeting-2026-11-13`.
