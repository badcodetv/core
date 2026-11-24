# Karen story film: overnight brief for cut r4

> Written 2026-11-24 by the session that ran rounds 2–4 with Kai, as a hand-over to an autonomous overnight run.
> Read this whole file, then `docs/stories/karen/badcode.md`, then `scenes/story/beats-r4.md`. Those three are the context.

## The job

Make **cut r4** of the Karen story film from the beat sheet `scenes/story/beats-r4.md`, as an exciting, watchable
film, and put it on the existing timeline page for Kai to watch in the morning. Kai, 2026-11-24: *"use as much of Flow
and as much of the voice model as you want… with all autonomy and permission given… producing this like you get the
story… an exciting version of Karen… autonomously working overnight get a version cut that I could watch."*

**What that permission covers tonight:** Flow stills **and** clips with no approval stop (it waives the usual
still-approval gate for this run only), AI Studio voices freely, re-rolls freely, the Gemini listen tool on our own
renders for self-review (Kai's explicit say-so for this run; the standing rule otherwise is "only when asked"). It does
**not** cover: anything public (YouTube, sharing), editing Jack's Premiere sequence `Karen v4`, deleting anything, or
force-pushing.

## The story in one breath (what Kai wants it to feel like)

A New York HR manager is fired by an AI, gets drunk, tells the AI to fuck off and throws her phone in the river, wakes up
with nothing but a payphone and a grudge, and **complains her way up the entire chain of power through sheer
persistence**, day after night after rain after snow, until a busker samples her, she goes viral, a desperate talk show
puts her on the phone to the President, and at that exact moment the AI sacks the President live on air. The sacked
President calls Karen: her persistence is what humanity needs now. To be continued.

**The joke engine is persistence.** The centrepiece is the escalation (beats 3.1–3.12): map + org chart + weather moving
together, accelerating ("logarithmic", Kai). Every note Kai gave says: **cut dead air, be snappy, don't indulge.**
Target about 4 minutes (cut r3 was 5:41), a guess, not a rule; what matters is that nothing drags.

## Kai's rulings to keep (all are in the beat sheet; listed so none is lost)

- Fish-in-the-microwave joke **stays** (Jack's), minus "Who knew", and it must end before the cut to the boss scene.
- "Karen is told to see her boss" starts on the cut, as they're sat. No overlap of lines across cuts there.
- Office archetype = Karen in **the office**, stood over a colleague's shoulder wagging her finger (not a coffee shop).
- After the boss is fired: boss shocked → straight to the bar. **Defenestrate line cut.**
- River: Karen only says **"You hear that, Sean? Fuck you, Sean!"** as one move with the throw. No "fuck this
  technology", no Susan "mad lad". Kai: the r3 "fuck you, Sean" read "sounds a bit weird": make several takes, pick the
  most natural drunk one.
- Phone sinking → straight to "In these moments, even atheists pray to Christ" (the "Lesson learned…" line is cut).
- Susan's reminder + the grey flashback to the river: **Kai loved it**, keep, cut it tight.
- The map is **Jack's cartoon street map with coloured pins** (`vids/red pin map/red pin zoom map.mp4`,
  `vids/yellow pin map/yellow pin map.mp4`, plus `part 1/2`), **not** the aerial-photo pins made in r3. Kai: "I want to
  keep that… part of the music video… looks really nice".
- Three named rungs: **Martha** (City Hall reception, the long call), **Clive** (Borough of Manhattan), **Harriet**
  (State of New York). Never the President during the climb.
- **"I've got all day to complain"** is said twice, by Karen in her own voice: end of call 1 (to Martha), and again to
  Harriet as Aaron walks past (that's what he samples).
- Viral = a ruthless edit, minimum beats; it ends on the TV camera (Kai loves that cut into the show).
- Writers' room: the President is tonight's guest, they're out of ideas, jobs on the line; the coffee girl shows the
  Karen meme; punchline "She wants to speak to the manager?" / "There's only one manager left."
- Coup: the studio screen (Sean in gold) sacks the President and takes over the government; **real drama**; Secret
  Service rush him out; then GitPush Origin Master's Piccadilly Circus screen shot (Kai asked for exactly this nod) with
  the headline swapped to "PRESIDENT SACKED ON LIVE TV BY SEAN AI"; then the President in the Beast calls Karen: work
  together to beat this, meet me in the Situation Room, **and he brings in his guy in England (Tarquin)**: Kai wants
  Tarquin kept as the link to the wider BadCode universe. "To be continued" + the spray logo.
- Joke slots: Kai picked Claude's first suggestion in every slot ("go with your suggestions"). If a pick plays flat in
  the cut, you may try the next option, and say so.

## Where everything is

| What | Where |
| --- | --- |
| Story rules, look, voices | `docs/stories/karen/badcode.md` (read first; its look and sound blocks are LOCKED) |
| The words, shot by shot | `docs/stories/karen/scenes/story/beats-r4.md` |
| Kai's notes, every round | `scenes/story/feedback/timeline-r1…r4/notes/*.json`, answered in `scenes/story/cut-notes.json` |
| Scene record | `scenes/story/scene.json` (cut pointer), `trail.json` |
| Last cut's script (reuse it) | `scripts/karen/story-cut-r3.py`: block-based assembly (picture timed to voice, lead/gap 0.35 s), placeholder cards, Sean's screen card, flashback grade, lower thirds, audio mix, edl writer |
| New-line voicing | `scripts/karen/narration-r3.tsv` + `render-narration-r3.sh` (copy to r4 versions) |
| Media root | `/mnt/d/badcode-videos/karen-story/` (clips in `new clips/`, `old clips/`, `vids/`, `clips/ending/final/`) |
| Cut r3 / v4 edls | `timeline/cut-r3/edl.json`, `timeline/cut-v4/edl.json` (v4 = Jack's Premiere cut, with every narration file path and the score cues) |
| Jack's v4 render | `renders/karen-v4-r0.mp4` (4K): **lift unchanged stretches from it** (picture + mix) rather than rebuilding them, especially the Tarquin lip-synced ending, whose sync was hand-placed |
| Timeline page | https://claude.ai/artifact/3Mw9ucc4wRiDESP2nhgAdC (republish to this URL; **someone published a newer version on 2026-11-24: read it first and merge**) |
| Timeline index | https://claude.ai/artifact/KVLjAMnfz3NerFP9RQhxn6 (rebuild after) |

## Voices

- **Narrator:** AI Studio `Algenib`, model `gemini-3.1-flash-tts-preview`, profile
  `docs/stories/karen/narration/profiles/narrator-algenib.md` (LOCKED for this story; this is the story's own recipe).
  Write `Ay-Eye Sean` in transcripts.
- **Karen:** `Gacrux`; **Susan:** `Kore` (badcode.md). The r3 takes used `--plain --model gemini-3.8-flash-tts` with a
  short bracket cue (`[drunk, shouting]`); Kai found the shout odd, so try a few readings and pick the most natural.
- **President:** `Charon`; **Tarquin:** `Zubenelgenubi` (LOCKED in the cut; the old lines are in the v4 edl/render).
- **New roles** (Martha, Harriet, coffee girl, a writer, Clive if he speaks): cast per `docs/rules/voices.md` (pick from
  the voice library by metadata, render plain, choose); write the picks into `docs/stories/karen/sound.md`.
- Run: `set -a; . ./.env; set +a; uv run -q --with "google-genai<2" python3 scripts/aistudio-tts.py <txt> <out.wav> …`
  (pin `google-genai<2`; the key is paid, no daily cap; keep ~22 s between calls).
- Finishing: trim edge silence (`silenceremove` −55 dB, 0.12 s), level each line to **−18 LUFS** (the v2 narration's
  level), split takes at pauses with `silencedetect`, check words with faster-whisper
  (`~/.cache/badcode-whisper/venv/bin/python`). Card everything with `scripts/provenance/prov.py card`.
- Dubbed on-screen talking: follow `lip-sync-dub` / `docs/rules/voices.md`; where lips can't be matched, play the line
  over a back, a wide or a cutaway (the r3 river shout used the women seen from behind).

## Flow

- Read `docs/rules/flow.md` and the `flow-automation` / `flow-prompt` / `shot-craft` skills first. Stills: one at a time
  in the session's tab, newest Nano Banana per the rules file. **Every video through the tab pool**
  (`scripts/scene/pool.mts`), Omni 1.2 Flash, 8 s, camera locked, count per the rules (x2). Check mediaId, duration, md5
  and a frame strip after every call (Flow can save the previous clip under the new name).
- Look: paste the Super-8 **STYLE LOCK** block verbatim from `docs/stories/karen/look.md` §Preamble (+ the CANDID CLAUSE
  for New York walk plates). Cast with Flow Characters `Karen`, `Susan`, `Aarron` (`@Tarquin` for Tarquin) in the
  story's Flow project `da8feea7`; never describe a face. Story rules that bite tonight: no legible text in any generated
  frame (screens and headlines go on in post); present-day or reject; **never write news, reporter, broadcast, live,
  television or President in a prompt** (the President is "a man in a dark suit", fictional, from behind); two people in
  relative motion merge, so shoot two-handers as singles; Sean is a screen, never a face.
- Shots to make (from the beat sheet): Karen wagging her finger over a colleague (1.2); Karen at the railing, phone
  held high, shouting (2.3); a delivery rider handing food into the phone box (3.4); Secret Service rushing the man in
  the dark suit off the set (6.5); the man in the dark suit in the back of an armoured car on the phone (6.7). Add
  anything else that makes it better (the escalation can take more Karen-at-the-box beats), and say what you added.
- GitPush Origin Master's Piccadilly Circus screen shot: find it under `docs/stories/gitpush-origin-master/` and its
  media (localmap.py); if it can't be found, make a stand-in and flag it.

## How to work (what Kai and Jack expect)

- Copy `story-cut-r3.py` to `story-cut-r4.py` and build the **whole** film from clips + new material + lifted v4
  stretches. Picture timed to the voice. Snappy: the escalation accelerates (long call 1, then each rung faster), and
  every line ends before its cut unless the overlap is deliberate.
- Before publishing: watch your own cut. Contact-sheet every shot, transcribe the mix to prove every line is there and
  whole, check levels (~−18 LUFS, music under the voice), and run a `story-craft` style review against Kai's notes:
  does anything drag, does the escalation build, does the coup feel like real drama, does the ending make Karen's
  persistence the point. Fix what you find, then re-cut. Two or three passes is fine.
- Page: `scripts/scene/build-timeline.py <scene-dir> <out-dir>`; publish with `capabilities {db:{}, user:{}}`; the
  publish root must be under the working directory or the scratchpad (copy the page there); max 64 MB per publish, so
  send `hq-*` parts in batches to the same URL. Write `cut-notes.json` round 4: the plan at the top (what changed, what
  you invented and why, what's still a placeholder), a reply under each round-4 note saying where it landed.
- Record: `prov.py trail … --round 4`, cards for every generated file, `scene.json` cut → `cut-r4`, the Karen line in
  `badcode.md` "Parts", rebuild + republish the timeline index.
- Premiere: if the bridge is up, build a **new** sequence `karen-1-story-r4` in `Karen vid.prproj` (never touch
  `Karen v4`); if it isn't, skip it and say so.
- 🔴 Git: the main checkout at `~/projects/badcode/badcode` is often on another session's branch. Work in your own
  worktree on `main` (`git worktree add <scratch>/karen-r4 origin/main`), commit there, push to `main`. Never commit
  Karen work onto someone else's branch.
- Gotchas met in r3: decoding the 4K v4 render with many threads ran out of memory and truncated it silently (use
  `-threads 4`, then check the duration); ffmpeg input indexes in a big mix must count inputs, not arguments.

## Done means

Kai can open the timeline page and watch cut r4 from start to finish, with the plan at the top saying what changed and
what's still a placeholder; everything is committed on `main` and pushed; the morning reply (house style: TL;DR first,
plain words) says what was made, what it cost in Flow, what you're unsure of, and the sync line
`page round 4 · <sequence or "Premiere not built"> · <state>`.
