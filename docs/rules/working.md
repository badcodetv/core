# How Jack and Kai like to work: standing rules
> Moved out of Claude's per-machine memory on 2026-11-17 (the context reset) so both Kai and Jack have them.
> Mechanics and working habits only: no look or sound belongs here (that lives in a story's `badcode.md`).
> Originals: `archive/messy-context-2026-11-17/memory/`.

## Jack 2026-11-17 "why arent you reading the notes and asking me everytime": always dump the picks page's votes AND notes myself before replying or acting; never ask Jack to vote or say what he picked

Before every reply on a scene with a live picks / mood board / timeline page, dump its `votes` and `notes` (ArtifactData list → the scene's `feedback/` dir) and act on them. Never end with "your move: vote on the page" or ask what he picked: he has usually already clicked or written a note, and "a maybe + a note" is an instruction.

**Why:** Jack, 2026-11-17 (Priority Lane rounds 12-15): I kept asking him to pick or confirm when his votes and notes were already on the page.
**How to apply:** at the start of each turn about that scene, and again after any long job, read the page's db; treat "This" as the pick, "Maybe" + a note as "fix this one", and a note alone as the brief for the next round. Only ask when the board is genuinely empty for a beat. See `clean-room-stills-work`.

## Jack 2026-11-17 speed-ups for picture rounds: answer every note on the board in one round, clean room only for new shots (small fixes = direct prompt edit), shared brief carries the look as one line

Jack, 2026-11-17, after Priority Lane took 9 rounds for 4 shots ("it feels like this process takes way longer than it should"): do these three things.
- **One round clears the whole board**: read all votes and notes, answer every beat in the same round; never one note per round.
- **Clean room for new shots only**: a small fix ("make the poster bigger") is a direct edit of the existing prompt, logged in the round folder; no new sealed writer.
- **The shared clean-room brief carries the look as one line** from the story's look.md; the shot's own facts first.

**Why:** rounds themselves were not slower (6-38 min); the count was, mostly rework and one-fix-per-round.
**How to apply:** written into `.claude/skills/scene-images/SKILL.md`; see also `read-the-board-dont-ask` and `lookalike-drifts-to-the-real-person`.

## Jack writes the jokes, in every story, short and script: give him a beat brief (what each line conveys, what to joke about), never written jokes

Jack, 2026-10-07, on the Bank Robbery script: "instead of writing the jokes, just say what to joke about and what the scene/line is supposed to convey, I'll write it."

**Why:** he wants to write the comedy himself; my drafted punchlines were not what he asked for.

**How to apply:** per scene, hand over a beat list: who speaks, what the beat must convey, what the joke is about, with the line left blank for him. Jack, 2026-11-18: this holds for everything, not one story (a fresh test session drafted a Freddo joke because the rule was only written for one story). Applies to beats, scripts, shorts and captions with a gag in them, unless he asks for a draft. See `bank-robbery-register-brutal-and-silly`.

## When Jack says "forget all that" before a new brief, he means keep earlier prompts out of the new one — not cancel the earlier request.

"Okay forget all that, try …" means **don't let earlier prompts/rounds influence the new one**. It does
not cancel a request he made earlier in the same session. Do every brief, each built in isolation.

**Why:** 2026-09-26 he sent two combine-with-reference briefs (Gnome Dub, then Desert Chill), each opening
"forget all that". I dropped the first; he had to come back and ask for it: "i just meant do not let other
prompts influence the new ones".

**How to apply:** queue both briefs. Build each round only from its named take and its reference, never
from a sibling round. If it's unclear whether an earlier brief still stands, finish the new one and offer
the earlier one in a line; don't silently drop it. Related: `suno-generate-after-prompt`.

## Jack 2026-10-30 — the words \"clean room\" mean: web research only, sealed writers, no repo prompts or skill phrasing, prompts run verbatim, same-prompt check; the fix for the same-prompt bug

Jack, 2026-10-30: *"i dont want to have to remind you about the same prompt being made bug over and over, so what do i say so that you are aware of that"*. Answer given: he says **"clean room"**.

**Why:** prompts written inside the repo inherit habit wording from old prompts, skills and memory, so everything comes out the same.

**How to apply:** on "clean room", follow `clean-room-stills-work`: fresh web research, sealed writers who read only one brief file, run verbatim, `scripts/variations/fresh.py` afterwards, and don't load shot-craft or flow-prompt into the writing. For Bank Robbery MV stills, this is the default even if he doesn't say it. The current scene is `docs/stories/bank-robbery/songs/mv-colour-noir/`.

**Update 2026-11-17:** the writers must be truly sealed: run them with `scripts/variations/sealed-writer.sh` or the `clean-room-writer` agent, never `general-purpose` (which loads CLAUDE.md + this memory). See `sealed-writers-must-not-see-repo`.

## 2026-11-17 tested: general-purpose subagents load all of CLAUDE.md + the memory index, so "clean room" writers were not sealed; use scripts/variations/sealed-writer.sh or the clean-room-writer agent; lean on Unsplash real photos

Jack asked (2026-11-17) to stop "stuff in the repo affecting the prompts … it's just a merry-go-round" and to look where no one had looked. Found: a `general-purpose` subagent sees the full CLAUDE.md and this memory index (probe, 2026-11-17), so every clean-room writer since Kai's 2026-10-28 switch to subagents was reading other stories' looks and rules. Jack's original 2026-10-24 fix (writers as `claude -p` in an empty /tmp) is restored as `scripts/variations/sealed-writer.sh` (CLAUDE_CODE_DISABLE_CLAUDE_MDS=1, CLAUDE_CODE_DISABLE_AUTO_MEMORY=1, temp folder; tested blank). `.claude/agents/clean-room-writer.md` (omitClaudeMd: true) does the same as a subagent after a session restart.

**Why:** the leak came back through memory growth; the sameness gate and fresh.py only catch it after the fact.
**How to apply:** every clean-room / variations writer runs sealed; the brief is raw inputs + geometry map + one look line. For real-world scenes start from Unsplash photos (`scripts/scene/unsplash-refs.py`), Jack: "the Unsplash fix does seem to solve a lot of these problems". Keep this index lean: story details belong in the story's files, not here. See `rounds-clear-the-board`, `clean-room-stills-work`.

## Jack 2026-11-12 — shorts cut from a finished film are fast trailers (best lines from across it), never straight slices

When clipping a finished story film into shorts, make **fast trailers**, not consecutive slices. Jack, 2026-11-12, after seven sentence-clean slices of Camping: "all of them dont feel like shorts, i feel like if we are clipping up this story, they should be more like fast trailers."

**Why:** batch 1 (Sept) was rejected as "random"; straight slices of the film then felt like pieces of a film, not shorts. A trailer pulls the best lines from across the whole film, cuts picture faster than the words, and ends sending people to the full film.

**How to apply:** offer 2-3 trailer angles (one character's arc / the clash / rapid-fire punchlines) on a picking page before any Premiere work. Cut lines on word timings (faster-whisper word timestamps; Gemini timestamps are too loose) and re-transcribe the result to catch clipped words and stray words carried in by picture flashes. Camping round 1: docs/marketing/camping-serial-plan.md. Related: `shorts-karen-camping-only`, `verify-a-cut-against-the-script`.

## Jack 2026-10-12 — for BadCode marketing work, profit is the main goal; followers and money-making ready before the album release

Jack, 2026-10-12: "profit is the main goal full stop"; "we need followers and money making ways to be cooked up for badcode now, so when we release the album of stuff... we have a bunch of marketing stuff ready". He said he is "completely lost in this department" and worried "no eyes will be on it".

**Why:** the work is piling up unreleased; he wants the audience and the income routes built before the album, stories, songs and music videos go out together.

**How to apply:** in marketing work, rank ideas by what they earn and say what each is worth in pounds, with how weak the evidence is. The research and the ranked table are in `docs/marketing/profit.md`. Same day he said: "lets not do any social media stuff yet before i talk to kai, but lets have it all ready to" — prepare, do not post. My reading: this is about marketing priorities, not a change to the voice or the reader rules. See `mfs-shorts-and-marketing-plans`.

## Raise the BadCode Spotify account once, early in a session, until it is opened or dropped

Asked 2026-10-20: remind about making a BadCode Spotify account. Spotify artist profiles need a distributor
(e.g. DistroKid) first, and the chief-of-staff plan lists it as "not now". The other accounts
(YouTube, Facebook, TikTok, SoundCloud, Instagram, X) all use the badcode.tv@gmail.com login.
Raised again 2026-10-21 (logo session).

**Why:** they asked for the reminder explicitly.
**How to apply:** raise it once, early in a session; when Spotify is opened or dropped, update
`docs/marketing/social-media-accounts.md` and delete this memory.

## Jack 2026-11-10 — Drive uploads carry only the agreed cut (scripts/drive/push-agreed.sh), never the whole story folder

Upload only the agreed cut of a story to Drive, never the whole folder ("only use the cut we agree on, ie the latest one on the timeline", "do only the agreed cut for all of them").

**Why:** whole folders were ~32 GB of old cuts, renders and per-cut work folders on Jack's ~0.5 MB/s upload; the agreed cuts were ~2.5 GB.

**How to apply:** `scripts/drive/push-agreed.sh <story>` then `--go`, lists in `scripts/drive/agreed/`; never `drive.sh push` for a story that has a list. Procedure in the drive-sync skill and scripts/drive/README.md. State on 2026-11-10: bank-robbery-music, bank-robbery-story, camping-story extras and the cut 10 render all up (0 left); camping-music finished 16:07 (77 copied, 0 left): all four agreed cuts are on Drive; next is the timeline test. 2026-11-11: everything else deleted on Drive (bin) and on Jack's PC (permanent) for these three; old sequences are offline for good. The Drive sync comes before the timeline test (Kai: one step at a time). Related: `resolve-media-paths-via-localmap`.

2026-11-11: Camping Story added: agreed cut = `0 synced` in `Camping Video NEW!/camping jack/camping jack.prproj`; Jack's camping-story folder is `Camping Comic` (Drive mirrors that level, not `Camping Video NEW!`). Cleaned to it on Drive and PC; `Camping Comic/badcode camping`, `music video`, `other`, `shorts` untouched. Before any clean-up: read the agreed sequence's media from the saved .prproj (nested sequences followed) AND scan every recent .prproj for refs to the delete list — Jack warned new cuts borrow old clips. All five agreed cuts on Drive; record in docs/misc/2026-11-10-drive-cleanup-call.md.

## Before saying media is missing, resolve the path with scripts/drive/localmap.py; repo paths are the writer's machine (/mnt/d is Kai's)

Paths in edl.json / scene.json / final-edl.json are whatever machine wrote them (Kai's are `/mnt/d/badcode-videos/...`). On Jack's machine there is no /mnt/d; the same story sits under his `badcode.local.json` folder (e.g. Karen music = `C:\Users\jackt\OneDrive\Desktop\Youtube Vids\animation\songs\Karen`). Always check a file with `python3 scripts/drive/localmap.py path "<path>"` (or `localize()`) before declaring it absent.

**Why:** 2026-11-10 I told Jack the Karen footage "isn't on this machine" after `ls /mnt/d` failed. It had been pulled with drive-sync and all 105 shots were there. He had to stop the work to debug a sync that was fine.

**How to apply:** any media-existence check, in any skill. `renders/` really is never synced (exclude.txt), so a missing render is expected, not a sync fault. See `drive-sync`.

## Jack 2026-11-12 — a short's media folder shows only what the film uses; scratch, rejected and unpicked go in _ folders

Keep a short's media folder down to what the video is made of (kept clips, picked takes, picked stills, the cut's edl/preview/stems, `cut\premiere\rN\`, the .prproj). Working renders go in `cut\_scratch\`, raw downloads in `video\_scratch\`, re-rolled clips in `video\_rejected\`, unpicked stills in `moodboard\_unpicked\`.

**Why:** Jack: "there a lot of unneccary stuff in the folder, other than what we really need which are the clips, music or whatever else is in the video."

**How to apply:** write new cut scripts to a `_scratch` folder from the start; never move a file a Premiere sequence uses (`never-rm-imported-premiere-media`). Rule and table: `docs/marketing/shorts-release.md` §1a.

## Jack's short media folders are always Desktop Youtube Vids\animation\shorts\<slug> — use it without asking (2026-11-12)

On Jack's machine every short's media folder is `C:\Users\jackt\OneDrive\Desktop\Youtube Vids\animation\shorts\<slug>` (WSL `/mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/shorts/<slug>`); he picked it every time.

**Why:** Jack asked for the process to be faster (2026-11-12, "fix it all"); asking where to put the folder was one of the avoidable stops.

**How to apply:** for a new short on this machine, create that folder and run `drive.sh where`, then say where it is in one line instead of asking. Kai's machine differs (D:\badcode-videos\shorts\<slug>). Keep the tidy layout (`tidy-media-folders`).

## Unsplash API key LIVE since 2026-11-17 (production tier, 5000 req/hr); scripts/scene/unsplash-refs.py works, offer photo options in scenes

2026-11-17: Jack put the Unsplash keys in `.env` (as `export UNSPLASH_...=` lines; the script now accepts the `export ` prefix). Live test passed: HTTP 200, rate limit 5000/hour (production tier, so the app was approved).

**Why:** the real-photo step of new-scene / scene-beats / scene-images (`scripts/scene/unsplash-refs.py`) was blocked from 2026-11-13 waiting on Unsplash's review.
**How to apply:** use the script for reference-photo options instead of asking Jack to paste photos. Only the Access Key is used; the Secret Key also sits in `.env` (not needed by anything). Jack 2026-11-17: the licence question for using them in Flow "doesn't matter, we'll figure it out later": do not raise it. See `meeting-2026-11-13`.

## Jack's machine needs LISTEN_MEDIA_ROOT overridden; GEMINI_API_KEY is in .env since 2026-09-24 but the listen MCP only reads it at startup.

On Jack's machine (`/home/jackt`) the Suno listening loop records, measures and — since
2026-09-24 — listens:

- `LISTEN_MEDIA_ROOT` must be set to `/mnt/c/Users/jackt/OneDrive/Desktop/suno-recordings` — the
  default is Kai's desktop and fails with EACCES. Jack's Desktop is OneDrive-redirected;
  `/mnt/c/Users/jackt/Desktop` does not exist.
- ✅ **`GEMINI_API_KEY` is in `.env`** (added 2026-09-24). 🔴 The listen MCP reads `.env` only
  at startup, so if `listen_status` says `apiKeySet: false`, reconnect `listen` via `/mcp` — or run
  `describe()` from a one-off tsx script (`scripts/suno/.tmp/describe-once.mts`, args: path lens
  start end question), which worked first time.
- 🔴 2026-09-26: `gemini-3.5-flash` returned **429 quota** on this key; `gemini-3-flash-preview` worked — run
  `GM=gemini-3-flash-preview npx tsx scripts/suno/.tmp/describe-model.mts <wav> music "" "" "<question>"`.
  (`gemini-2.5-flash*` are 404, retired.)
- `record` only finds takes visible on the create page: type the title into the **Search clips**
  box first for an older take — and **clear it before any Create**, or the new rows are hidden.
- WSLg's PulseAudio wedges here. `./scripts/audio-server.sh` starts the private server, then the
  channel **must be relaunched** (`browser-channel.sh down 1 && up 1`) because Chrome reads
  `PULSE_SINK` at launch.
- Installed 2026-09-18 (all were missing): `pulseaudio-utils`, `pulseaudio`, `ffmpeg`,
  `python3-pip`, and numpy/librosa/soundfile via `--break-system-packages`.

Full table: `docs/listening/automation.md` §0. Related: `suno-account-is-kais-google-login`.
- 🔴 2026-09-27: `gemini-3-flash-preview` then ALSO hit 429 after ~15 calls in a day; `gemini-3.5-flash` worked again —
  alternate the two, and call them one at a time (parallel calls tripped the quota).
- 🔴 `record-yt-seg.mts` can capture a YouTube **mid-roll advert** inside a segment on long mixes (2026-09-27, Liquid Rasta: <!-- style-lint: ok (a mix's name in a tool-failure record) -->
  a clip "switched to a funky breakbeat" at 0:25, another was "tropical pop"). Ask Gemini "could this be an advert?" and
  discard those clips.
- 🔴 2026-09-27 later: 3.5-flash, 3-flash-preview AND 3.1-pro-preview all 429'd; **`gemini-3.5-flash-lite` still worked** (lower
  confidence — say so). `3-pro-preview` and `3.1-flash-preview` are 404. The describe tool's `tempo` measurement returned
  132.51 for five different clips — it is broken; use `librosa.beat.beat_track` directly (reggae reads double: ~130 = ~65). <!-- style-lint: ok (engine fact: a tempo measurement) -->
