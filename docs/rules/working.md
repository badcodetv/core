# How Jack and Kai like to work: standing rules
> Moved out of Claude's per-machine memory on 2026-11-17 (the context reset) so both Kai and Jack have them.
> Mechanics and working habits only: no look or sound belongs here (that lives in a story's `badcode.md`).
> Originals: `archive/messy-context-2026-11-17/memory/`.

## Jack 2026-11-23: "please only do desktop notifications when its time for me to type or do something"

Every end of a turn fires the desktop toast (the Stop hook in `~/.claude/settings.json`). So never end a turn while
work I started is still running (a Flow queue, the pool, a writer, a Suno run): wait on it in the same turn
(`flow_queue_status` with `waitSeconds`, a blocking command) and end the turn only when there is something for Jack or
Kai to look at, pick or answer. No "it's rendering, I'll tell you" turns. The Stop hook is `~/.claude/hooks/toast-if-yours.sh`: it toasts only after a turn a human message started, never after a
turn a background task started. Permission prompts and questions toast on
their own (the Notification hook). The project's duplicate Stop toast (`.claude/settings.local.json`) was removed the
same day.

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

## Jack and Kai write the jokes, in every story, short and script: give them a beat brief (what each line conveys, what to joke about), never written jokes

Jack, 2026-10-07, on the Bank Robbery script: "instead of writing the jokes, just say what to joke about and what the scene/line is supposed to convey, I'll write it."

**Why:** he wants to write the comedy himself; my drafted punchlines were not what he asked for.

**How to apply:** per scene, hand over a beat list: who speaks, what the beat must convey, what the joke is about, with the line left blank for them. Jack, 2026-11-18: this holds for everything, and for Kai as well as Jack, not one story (a fresh test session drafted a Freddo joke because the rule was only written for one story). Applies to beats, scripts, shorts and captions with a gag in them, unless he asks for a draft. See `bank-robbery-register-brutal-and-silly`.
Jack, 2026-11-20, on a list of short ideas: "whats failing to grab me are the descriptions of these shorts trying to be funny, i think make the point of the story/short first, then we will make the jokes after". Pitching ideas counts too: a short is pitched as **the point** (what it argues), **the story** (who, what happens, what is at stake, in plain words) and **the way out** (the better choice, or ⬜ if it has none yet). No punchlines, no quoted gag lines, no "the meme lands". The jokes come after he picks.

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

**Update 2026-11-17:** the writers must be truly sealed: run them with `scripts/variations/sealed-writer.sh`, never `general-purpose` (which loads CLAUDE.md + this memory). See `sealed-writers-must-not-see-repo`.

## 2026-11-17 tested: general-purpose subagents load all of CLAUDE.md + the memory index, so "clean room" writers were not sealed; use scripts/variations/sealed-writer.sh; lean on Unsplash real photos

Jack asked (2026-11-17) to stop "stuff in the repo affecting the prompts … it's just a merry-go-round" and to look where no one had looked. Found: a `general-purpose` subagent sees the full CLAUDE.md and this memory index (probe, 2026-11-17), so every clean-room writer since Kai's 2026-10-28 switch to subagents was reading other stories' looks and rules. Jack's original 2026-10-24 fix (writers as `claude -p` in an empty /tmp) is restored as `scripts/variations/sealed-writer.sh` (CLAUDE_CODE_DISABLE_CLAUDE_MDS=1, CLAUDE_CODE_DISABLE_AUTO_MEMORY=1, temp folder; tested blank). (The `clean-room-writer` subagent that did the same job was removed on 2026-11-23, Kai: one way to run a sealed writer is enough.)

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

**Older shorts moved (found 2026-11-24):** The Rules, Sponsor a Chancellor, Signs, Magic Money Tree, Same Bench, No
Master Recording and The Envelope now sit in `...\animation\shorts\other\<slug>` (Jack: "they are all in the shorts
folder"); their `badcode.local.json` entries and `folders.json` homes point there. `other\` also holds an older
`hello-im-badcode` copy; the live one stays in `shorts\hello-im-badcode`. If a recorded short folder is missing, look
in `shorts\other` before asking. The Freddo Mortgage was in neither (ask Jack).

## Bringing bp-videos (the Platinum repo) up to date with our tools (2026-11-24)

`~/projects/bp/bp-videos` is a reworded copy of our video toolkit (copied 2026-11-23 15:58, then a hand-made update
package). Jack asked twice whether it had "all of the optimising"; the package had missed eight lip-sync lessons, the
clean-room-writer route and the sounds-straight-to-Suno rule.
**How to apply:** when asked to check or bring it up to date: (1) list our files under `.claude/`, `scripts/`,
`packages/*-mcp`, `docs/rules`, `docs/flow`, `docs/ai-studio` changed since the last bp sync, and compare each with bp's
copy (same / stale / reworded); (2) fuzzy-compare the skill and rule TEXT line by line (bp renames stories to "one past
short", so exact diffs are noise), and read each unmatched line; (3) leave out BadCode-only material (chief-of-staff,
government, marketing agents, the BadCode voice, logo, comics, our story examples) and offer extra skills rather than
copy them; (4) write the changes in bp's own wording, commit only those files (bp usually has another session's
uncommitted story work), and tell Jack open bp sessions need a restart. Last sync: bp `2f522e7`, 2026-11-24.

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

---

# From Kai's machine memory (moved 2026-11-18)

> Kai's per-machine memory was archived to `archive/messy-context-2026-11-17/memory-kai/` on 2026-11-18. Kai,
> 2026-11-18: these two are "very important"; keep them.

## Media goes in the project's clips folder; prompts and words stay in the repo [clips-folder-convention]

Kai, 2026-08-26, amended 2026-08-27. **Never state one half without the other.**
- **Media** lives in the open Premiere project's `clips/<scene>/` folder (`<mediaRoot>/<story>/clips/<scene>/` +
  `.../final/`), created if missing. Find the root with `premiere_status()` (`dirname(project.path)`) before the first
  generation of a session. Never the project root; never the Desktop when a project exists. A short follows its own
  media folder (*Jack's short media folders* above; Kai's are `D:\badcode-videos\shorts\<slug>`).
- **Words** (prompts, beat lists, motion plans, rulings, revision logs) stay **in the repo**, in the story's scene
  folder. Kai: "we work on prompts and reference stills inside the repository, and then larger video iterations
  happen inside the clips folder." A prompt written into a media folder is unversioned, invisible to other sessions
  and on an unbacked-up drive.
- Before saying media is missing, resolve the path with `localmap.py` (above).

**Why:** scratch had drifted across the Desktop and D: at once and Kai thought clips were lost; a day later a whole
prompt sheet was written into a clips folder because only the media half of the rule had been stated.

## The provenance trail: the prompts for everything we make live in the repo [provenance-trail]

Kai, 2026-10-23, and again 2026-11-18 ("we absolutely need to keep the provenance trail"). The goal: rerun a whole
story's exact prompts on a better model one day. The repo holds every word; D: (backed up to Drive) holds the media;
together they are everything. Full convention: `docs/provenance/README.md`.
- **A recipe card for every generated file.** The Flow MCP, `run.mts`, the TTS script and Suno `record` write them
  themselves; anything else gets `scripts/provenance/prov.py card`.
- **Artifacts are the UI, the repo is the record.** Every page is built by a builder whose command goes in the trail
  (`--rebuild`). Every read of a page's votes and notes is dumped raw into the scene's `feedback/` first
  (`ArtifactData list … out_dir=$(prov.py feedback-dir …)`), then logged with `prov.py trail … --feedback --decided "<words>"`.
- `prov.py trail` after every page publish, `check` before showing a cut, `freeze` when Kai or Jack says a cut is done.
  A lost page is rebuilt, then refilled with `prov.py restore`.
- Going forward only: no backfill of older stories. The replay script stays unbuilt until a better model arrives.

## Jack 2026-11-18: every track on a page gets a player with a time slider, never just a link

"when you have tracks on the timeline page, can you make a player with a slider on it for the time, and then do that without
downloading it? ... So that I don't have to click the link every time? for songs".

**How to apply:** record each take (`suno.mts record <songId>`, no download spent; set `LISTEN_MEDIA_ROOT` to the short's
`<media>/audio/<round>/` on Jack's machine) and put its `.preview.mp3` on the page as an `audio` row (`build-picks.py` kind
`audio` draws a player with play and a time slider), published with the page. A Suno link can sit beside it, never instead.

## 2026-11-18: never run two browser scripts at once (Flow runner, Suno record, a Flow edit script)

Every Playwright connection points Chrome's download folder at its own temp folder, so two scripts on the one browser steal
each other's downloads: seven Flow stills rendered and none downloaded while a Suno recording ran. Run them one after
another; if it happens, the images are in the Flow gallery (collect them, don't regenerate).

## Jack 2026-11-18: work at Kai's speed ("do this", after asking why Kai's Bank Robbery pass felt quicker)

- **Clips through the tab pool**, always (`scripts/scene/pool.mts`, `docs/rules/flow.md`): 20 clips in about 5 minutes,
  not 25 one wave at a time.
- **Bigger rounds, fewer of them: aim for 2-3 rounds a pass, not 9.** Each round offers a wider spread (about 8 options
  for an open question, not 4-6), covers every open beat at once, and puts pictures, music and words on one page when
  they're all open. Narrow down only once Jack has picked a direction.
- **Keep working while Jack reviews.** The moment a page goes out, start the next thing that doesn't depend on his pick:
  the music round, the cut script, footage searches, sealed writers for the next round. Browser jobs (Flow, Suno, record)
  still run one after another, never at once (the rule above); the parallel work is everything else.
- **Fixed tool bugs stay fixed:** a new failure gets fixed and written into the engine's rules the same day.

## Jack 2026-11-20: read the page's notes before EVERY rebuild, not once ("did you read the notes on the last one")

On Pub Quiz: Housing I listed the timeline page's notes once (none yet), then built cuts 2 and 3 without looking again;
Jack's three notes (the logo, the fall, Bob) sat unread for two rounds. **Before every rebuild or republish of a page,
dump its notes** (scene-timeline "Rounds"), file each under the cut it was left on (match its `at` time to the publish
times in trail.json), and answer each on the page.

## Jack 2026-11-20: I pick, Jack vetoes (after "I feel like I've been working on this same short all day")

Every still, clip and voice take round: **Claude picks** the best option per slot, checks it (full size, frame by frame,
words heard), and carries straight on to the next stage; the picks page still goes up with every option and the pick
marked, so Jack can overrule any of them. Don't stop and wait for a pick. Wait only on what is Jack's and Kai's by rule:
the script and its jokes, the look and sound of a new story, money (Suno credits), the logo, and anything going public.
**Why:** on Pub Quiz: Housing the rounds that waited for a pick (script, three voice rounds, six still rounds, five clip
rounds) took the day; the evening's stages where Claude picked (stills → clips → cut) took under an hour.
**How to apply:** say "my pick, overrule on the page" in the reply, and treat a later veto as a normal note for the next round.
Setting a short's length up front was considered and left out (Jack: "might complicate things").

## Jack 2026-11-18: why prompts get polluted, and the check that runs before every send

Jack: "why does the pollution stuff happen to the prompts… is there a way we can check it every time? Like, analyse the
prompt for pollution before you even send it?"

**Why it happens:** shared files (skills, engine rules, engine docs, script help text) quote what worked on one story as
an example ("the Bank Robbery recipe"). Every session reads them, and when a session wants something that works it
copies the proven example, so one story's recipe becomes every story's. `scripts/style-lint.py` lets a labelled
example through and only hunts style words, so it never caught these. On 2026-11-18 it put Bank Robbery's narrator
note into Hello, I'm BadCode's voices; ~530 lines in shared docs still name a story.

**The check (built 2026-11-18):** the same pre-send hook as the same-prompt check (`scripts/variations/fresh-hook.py`)
now, before every Flow call, Suno call and AI Studio voice call:
- names the story the call is for, from the paths in it (where the output goes, or `docs/stories/<slug>/`);
- flags **MIXED STORIES** when a call touches two stories' files (the clearest sign of a leak);
- flags **LEAK from <story>** when the prompt shares 7+ words in a row with another story's prompts or its own files
  (badcode.md, look.md, sound.md, voice notes). Shared engine wording (`scripts/variations/house-wording.txt`) and the
  brand files (`docs/brand/`) are exempt.
It reports and never blocks. On a LEAK or MIXED flag: rewrite from this story's own `badcode.md`, and tell Jack or Kai.
**Its limit:** it catches copied words, not a copied idea reworded. So when writing any prompt, take it only from the
story's own `badcode.md` and the engine's rules, never from another story's folder or a shared doc's example.

## Jack 2026-11-23: sound options go straight to Suno takes ("just make them in suno and skip this step going forward thanks")

Said after a story-style round showed seven sounds as words and reference links only, with Suno held back until a pick.
**How to apply:** when proposing a story's sounds, make one Suno take per option in the same round (a `variations`
round, kind `suno`, in the story's workspace) and put the takes on the page with players; never a words-only sound
page first. Written into `.claude/skills/story-style/SKILL.md` step 3.2.
