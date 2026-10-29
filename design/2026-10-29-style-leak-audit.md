# Style-leak audit — everything that still puts a style into a prompt (2026-10-29)

Jack, 2026-10-29: Kai found the Suno problem (one story's sound in every song) happening with the videos
too. Jack: *"scan through all of the prompts for everything to make sure nothing like this automatically
goes into any prompt, whether its images/videos/songs/etc… all the skills and all of the repo."*

Follows [`2026-10-28-no-house-style.md`](./2026-10-28-no-house-style.md). That pass cleaned the
always-loaded layer (CLAUDE.md, memory index, skill descriptions) and `style-lint.py` passes. This pass
looked everywhere else: skill bodies, shared docs, code, memory files, story files. Four read-only
sweeps.

**Status: fixed 2026-10-29** (Jack: "fix the code and words"). Code, skills, shared docs, memory and
story files done; handoffs placed (`2026-10-29-skill-moves.md`, `2026-10-29-doc-moves.md`). `style-lint.py`
now also scans skill bodies and generic code (fail) and shared docs (report only, `--strict` to fail; ~390
mostly engine-manual hits left to label). Open for Kai: MMT's GPOM-borrowed narration and coda (labelled
"candidate, Kai to rule"), visible-cost gate beyond GPOM, the Suno duration rule conflict, "Bulletin
realism", the site copy "Drum & bass from the end of the world". Open for Jack: Camping r77 boxes still
say "gruff" against the r82 ruling; whether Bank Robbery's cut-8 colour rules are rules. Line numbers are as of commit `0494159`.

**Why the lint missed it:** it checks only CLAUDE.md, MEMORY.md and skill descriptions, by keyword. It
does not read code, skill bodies or the docs skills send you to, and it doesn't know words like opera,
Rasta, grime, Zimmer, Brixton, Algenib, Zubenelgenubi, double-time, black-and-white, STYLE LOCK.

HIGH = goes into a prompt automatically, or is written as the default. MED = a strong anchor (paste
block, example, one story's taste written as general craft). LOW = wording.

## 1. Code — injected with nobody choosing it

| Sev | Where | What reaches the prompt | Fix |
|---|---|---|---|
| HIGH | `scripts/aistudio-tts.py:36-47, 89-90, 101` | No `--profile` → every line is read as **Camping's Bob** (Reading/Guildford accent) in voice **Algenib**. GPOM `sound.md:367` and `camping/narration/voice.md:103` show commands that hit this | Make `--profile` and `--voice` required; delete the built-in `PROFILE` |
| HIGH | `scripts/suno/take-row.mts:83-108` (+ `suno.mts:1981-1987`) | `explore` / `narrow` overwrite model, weirdness 30/60, Style Influence 75, Audio 75/40, Variety off on every story | Read the cells from the spec; refuse if missing |
| HIGH | `scripts/suno/suno.mts:874, 1431` (+887, 1424, 1429, 1586, 2035) | Missing slider → silently `styleInfluence 75`, `weirdness [30,60]`, `audioInfluence 50` | Require them, as `model` already is |
| HIGH | `scripts/scene/run.mts:7, 138-139`; `scene/match.py:72, 76` | Generic scene runner forces Omni 1.1 Flash, 16:9, Frames, no override; card records the constants | Read model/aspect/mode from `scene.json` (from `look.md`); record what was used |
| MED | `packages/flow-mcp/src/flow-client.ts:58-63` | No `model` → **Nano Banana Pro** ("what BadCode ships"); contradicts the Nano Banana 2 rule | Require `model` on image tools |
| MED | `flow-client.ts:67, 77` | Video defaults 16:9 and Veo 3.1 Fast | Require, or report what was used |
| MED | `scripts/shorts/cut.sh:16-18, 54-57, 87-92, 130`; `panel.sh:38, 57`; `remix.sh:63` | Every short framed on GPOM's near-black card, "the one thin light", "house style in real pixels" | Per-story shorts config from `look.md` |
| MED | `scripts/variations/round.py:52-57, 204, 288-311` | Flow writers can't choose model/aspect (fall through to the defaults above); Flow rounds have no stamp check; `story` optional | Add model/aspect to Flow keys; check the stamp; require `story` |
| MED | `scripts/variations/sameness.py:381-383, 408-421` | Shared genre/look phrases of ≤5 words ("near-black", "one thin light", "liquid dnb") pass; identical settings only warn | Fail any 3+ word phrase shared by most of the round; fail all-identical settings |
| MED | `docs/listening/lenses/suno-diff.md:47-48` (loaded by listen-mcp) | The one worked Style-box rewrite is D&B, so Gemini's suggested fixes lean D&B | Genre-neutral example |
| LOW | `scripts/lipsync/mouth-*.py` import `scripts/bank-robbery/lips.py` | Coupling only, no style | Move `lips.py` to `scripts/lipsync/` |
| LOW | `scripts/suno/camping.mts`, `style-ab.mts`, `cover-ab.mts`, `scan-takes.mts`, `gpom-narration-spec.py`, `narration-drift.py` | Story-only scripts in the shared folder ("House style" = GPOM); `style-ab`/`cover-ab` import files now in `archive/` (broken) | Move to `scripts/camping/`, `scripts/gpom/` |
| LOW | `mfs-voice.py` (Zubenelgenubi/Brixton copied from Bank Robbery); Bank Robbery spawning `mfs-clip.mts` | Cross-story reuse, nothing leaks today | Note in each `sound.md` |
| LOW | `docs/listening/lenses/music.md` | Electronic-music headings (drop, breakdown) in every listen | Neutral headings |

Clean: everything else in flow-mcp (prompts go in verbatim), listen-mcp, premiere-mcp, `.mcp.json`,
`scripts/scene/*` builders, `scripts/story-style/`, `scripts/provenance/`. "Thanks." is never
appended by code, only written in story prompts.

## 2. Skills — read on every run, and they shape what gets written

| Sev | Where | Words | Fix |
|---|---|---|---|
| HIGH | `suno-automation/SKILL.md:60, 180-181, 313-323` | "Every attempt is a PAIR — Style influence 75, weirdness 30 and 60… Never generate at only one setting" | Delete the numbers; values come from `sound.md` |
| HIGH | `suno-prompt/SKILL.md:155-178` | The Genre → Mood → Instruments → Vocals skeleton + "default short" | Delete; keep the engine facts |
| HIGH | `suno-prompt/SKILL.md:524-537` | "BadCode's whole register is dark satire played straight… holds even when the user literally asks for a funny song" + Exclude list | Move to `karen/sound.md`; keep the kazoo engine fact |
| HIGH | `suno-prompt/SKILL.md:448-452` | "keep a UK genre tag, or the voices go American" | Rephrase as the engine fact; UK choice to the story |
| HIGH | `shot-craft/SKILL.md:69-73, 97, 102-111` | Visible-cost gate mandatory; "What moves… Default is nothing"; movement once per sequence | GPOM's `look.md` |
| HIGH | `scene-images/SKILL.md:15` | "darkness that reads as depth" on every mood board | Drop |
| HIGH | `scene-animation/SKILL.md:34` | "Animate dramatically: dive, storm, hard flashes" | GPOM's `look.md` |
| HIGH | `flow-prompt/SKILL.md:71-72` (from `docs/google-flow/README.md:54`) | "saturated colour named per place… two lights of different colours" on every Omni prompt | Bank Robbery's `look.md` |
| MED | `shot-craft/SKILL.md:30, 42, 74-75, 84-91, 121-122` | Register menu = GPOM's two; "one bright anchor" on near-black; "never leave the foreground empty"; grain/photographed; realism light gate | Story's look; make conditional |
| MED | `scene-animation/SKILL.md:36, 40, 66-70` | "rain, haze, light and one actor"; "the room dims"; 24fps/180° shutter text | Label GPOM / conditional on photographic |
| MED | `scene-images/SKILL.md:47` | visible-cost critique step | Delete |
| MED | `new-scene/SKILL.md:75-76` | scene.json template carries "1980s BBC 16mm", "Bulletin realism" | Placeholders |
| MED | `new-image/SKILL.md:57-64, 79` | default avoid-list (over-lit, symmetry); "one named light?" | Diagnostic only; GPOM items to GPOM |
| MED | `suno-prompt/SKILL.md:66, 81, 376-389, 436, 458-460, 579-583, 621-624` | Copyable voice clauses (Bank Robbery's North London contralto, newsreader), "short prompt or the voice loses", Camping narration boxes, GPOM narrator recipe, "Variety off" anti-slop | Move to the story `sound.md` files |
| MED | `story-craft/SKILL.md:50` + `docs/story-craft/forms.md` | every song framed as a "D&B track"; BREAKDOWN as default narration home | "a song"; club form conditional |
| MED | `suno-prompt:501-504`, `new-story:20-21` | every lyric in the narrator persona | Narrator-voiced lyrics only |
| MED | descriptions of `flow-automation`, `premiere-automation`, `flow-prompt`, `shot-craft` | name the retired `badcode-art-direction` as owner of "the look" (always loaded) | "the story's `look.md`" |
| LOW | `suno-automation:3, 48-50, 205-217, 325-334, 481`; `suno-prompt:8, 296-303, 512-514, 665-678`; `flow-prompt:49, 104, 167`; `new-image:10-11, 39-40, 78`; `scene-beats:29`; `scene-timeline:43` | "weirdness pair" in the description; GPOM duration table; voice named `badcode newsreader`; "stock+grade" lever in every still; "pad into a full paragraph"; GPOM note anchors | Label or rephrase |

Clean: story-style, variations, overview-board, chief-of-staff, new-idea, find-footage, scene-dialogue,
lip-sync-dub, video-fx, the five agents, settings hooks.

## 3. Shared docs — where the skills send you

| Sev | Where | Words | Fix |
|---|---|---|---|
| HIGH | `docs/storytelling.md:54-60` | "## Image direction (house style) — Default visual target is hyper-realistic documentary photography" | Delete; point to `story-style` |
| HIGH | `docs/premiere/mogrt-catalogue.md:78-83` | "The register is near-black with one thin light… first move on any template is to take the fill to near-black" | Story's palette |
| HIGH | `docs/premiere/effects-catalogue.md:394-395` | "the BadCode control… exactly the near-black register" | "GPOM's" |
| HIGH | `docs/ai-studio/README.md:683-690` | "not very BadCode, it needs to be gritty, deadpan… anger" as a universal ruling | Camping's narrator → `camping/sound.md` |
| MED | `docs/ai-studio/README.md:330-382, 742-744, 1008-1015` | paste-ready Mancunian "Gaz M." profile; Brixton/south-London "safest"; "RP is wrong for the reader" | To story files; recipe with `<accent>` |
| MED | `docs/google-flow/README.md:51-56` | saturated colours + two lights, "read before any shot" | Bank Robbery |
| MED | `docs/google-flow/2026-10-26-pretty-not-slop.md:3-5, 29-60` | Speakeasy Mint look as a numbered recipe; "for all images going forward" unscoped | Scope; move rules to BR `look.md` |
| MED | `docs/google-flow/nano-banana-2.md:310-312, 365-368, 595` | anti-slop = 35mm documentary ("worth applying on any image model", "the stack we already use") | "for a photographic look" |
| MED | `docs/flow/README.md:117-119`, `docs/flow/image-prompting.md:67-79` | grain/light-leak realism as a core rule | Conditional |
| MED | `docs/cinematography/` — `motion-and-cutting.md:38-43`, `principles.md:28-29, 224, 252`, `README.md:39-48`, `frame.md:101`, `evidence.md:34`, `symptoms.md:41, 52`, `registers.md:9, 127` | "the economy that governs our whole form… movement once per sequence"; handheld rejected; realism light gate; dark-anchor as "our #1 craft rule"; "our whole frame" is dark; documentary register "for the money film" | Options, conditional, story files |
| MED | `docs/story-craft/forms.md:131-155, 219-225` | `{FLAT}` "Default narrator voice"; BREAKDOWN default; "the narrator is a Suno voice" | Story's register; club form conditional |
| MED | `docs/suno-gpt/automation.md:305-319` | "Every attempt is a PAIR… 75/30, 75/60" | "Refining a sheet (Kai's method)" |
| MED | `docs/suno-gpt/files/suno-tag-mechanics.md:112-122`, `producer-vocabulary.md:17` | the fixed prompt order / skeleton | One possible order |
| MED | `docs/images/` + `register-anchor.md:16` + `docs/README.md:23` | GPOM's monolith anchors filed as "brand imagery" | Move to GPOM's folder |
| LOW | `docs/flow/camera-vocabulary.md:148, 246-251`; `video-prompting.md:378`; `docs/video-fx/ffmpeg-catalogue.md:231-232`; `hybrid-method.md:67`; `docs/premiere/api-notes.md:1161, 1615`; `omni-flash.md:2089`; `suno-voices.md:368-372`; `automation.md:605-607`; `nano-banana-2.md:401, 1331` (Pro as default); `CLAUDE.md:93`; brand exploration logo prompts ("making drum and bass") | Grain "not optional"; "most BadCode effects"; "house-grade"; one GPOM test as a principle | Label GPOM / conditional / superseded |
| FYI | `apps/web/src/home/catalog.ts:139`, `TransmissionIndex.tsx:114` | Public copy: "Drum & bass from the end of the world" | Kai's call; it's site copy, not a prompt |

Process rules that shape every look but are rulings, not leaks: Veo camera-locked + move in post;
stills first; no dialogue in Flow video; "any crew is a film crew" (policy); atmospherics on black;
Personalize off; v6 only.

Clean: `docs/style-library/` (a real menu), `docs/stories/STYLE.md`, `same-song-traps.md`,
`suno-v6.md`, `delivery.md`, `footage-sources.md`, `recipes.md`, `docs/brand/README.md`.

## 4. Memory — recalled by relevance into any session

**The index lines themselves leak** (loaded every session, missed by the lint): "opera backing with
normal voices", "Zimmer-style score + grime MCs; `cheap synth strings`", "aggressive Rasta voice every
lane", "MMT look is colour only, no black-and-white", "Never double-time rap", "Zubenelgenubi + British
(Brixton)".

| Sev | Memory | Problem | Fix |
|---|---|---|---|
| HIGH | `never-double-time-rap` | Camping/BR ruling stated for every song; MMT's song asks for "fast double-time flow" | Scope or delete (already in both `sound.md`s) |
| HIGH | `genre-names-the-music-not-the-voice` | Camping taste under an engine-fact title | Engine half is in suno-gpt; taste to `camping/sound.md` |
| HIGH | `variety-comes-from-named-instruments` | Generic title, Camping D&B body | Engine fact to `suno-tag-mechanics.md`; delete rest |
| HIGH | `bank-robbery-prompts-short-colour-design-round` | Newer colour rules live only here; `bank-robbery/look.md:49, 65` still LOCKS the grey, no-fill look Jack rejected | Update `look.md`, memory → pointer |
| HIGH | `money-for-something-cast-and-voices` | Calls MFS's voice "the BadCode narrator" — Bank Robbery then used it | "the MFS narrator" |
| HIGH | `style-tests-stay-in-flow-prompts-in-repo` | Hides MMT's "colour only, no B&W"; not in `magic-money-tree/look.md` | Move to `look.md` |
| HIGH | `camping-r41-from-scratch-rules` | Prompt words + settings, superseded twice | Delete |
| MED | `camping-r27`, `-r37`, `-r42`, `-always-the-grime-voice`, `-reference-artists`, `-orchestra-is-garnish`, `-drums-loud-record-clean`, `-jack-likes-r19-reese`, `-frozen-spine`, `-reference-is-now-r66`, `-vocal-pacing-is-the-gate` | Dead D&B-era recipes and settings; some say "house-rap rounds start from r27" | Delete; history is in `songs/camping.md` |
| MED | `camping-reggae-passage-r74` | "Rasta voice always, never gravel/gruff" missing from `camping/sound.md` (whose r77 box says "gruff") | Add to `sound.md`, memory → pointer |
| MED | `flow-hand-driven-not-automated` | `STYLE LOCK + SCENE: + Thanks.` template as a global rule | "the story's look.md preamble" |
| MED | `narration-not-lipsync`, `suno-clean-room-for-exploring` | BR/Karen rulings worded for all films/songs | Scope |
| MED | `bank-robbery-jack-notes-on-cut3` | Model town banned, but `bank-robbery/look.md:138` still lists it | Fix `look.md` |
| MED | `bank-robbery-mv-speakeasy-mint`, `mmt-topical-show-october`, `bank-robbery-resume`, `bank-robbery-jack-song`, `money-for-something-host` | Resume notes grown into look/sound stores, partly not in the story files | Move rules to story files; cut to state + pointer |
| MED | `short-boxes-keep-the-drift-space`, `a-ban-loses-to-a-positive-instruction` | Engine facts with ready Camping sentences/values | Keep fact, strip Camping |
| LOW | `every-flow-prompt-ends-with-thanks` ("house style"), `never-write-uniformity-words`, `describe-the-song-not-the-box`, `audit-inherited-excludes`, mv2 memories, voice-name memories | Wording / examples | Trim to pointers |
| ? | `always-run-shot-craft-then-flow-prompt` | Sends every prompt through the three gates incl. GPOM's visible-cost gate | Kai to rule |

## 5. Stories borrowing each other's style

| Sev | Where | Problem |
|---|---|---|
| HIGH | `magic-money-tree/sound.md:54-57`, `songs/narration.md:41, 61-80`, `RESUME.md:46`, `rough-cut/README.md:101` | MMT narration (EXPLORING) = GPOM's settings, template and `badcode newsreader` voice, "inherited from GPOM" |
| HIGH | `magic-money-tree/edit-plan.md:413`, `rough-cut/illustrations.md:50-55` | MMT coda prompted in GPOM's "near-black, one light" via "the brand register" |
| HIGH | `gitpush-origin-master/README.md:223, 326` | Points at the storytelling.md house style |
| MED | `gitpush-origin-master/prompts.md:10-11`, `karen/prompts.md:26-27`, `scenes/still-fine.md:69` | "Read badcode-art-direction first (the global BadCode register)" — retired skill |
| MED | `camping/look.md:43` = `gitpush-origin-master/look.md:46` | Same 35mm documentary preamble in two stories (the old house PEOPLE register) |
| MED | `magic-money-tree/characters/dawn.md:25`, `camping/characters/tarquin.md:213` | "house style: hyper-realistic documentary" labels |
| MED | `magic-money-tree/sound.md:76` | GPOM's West Country robot voice floated for MMT's narrator |
| MED | `camping/narration/voice.md:1112-1118` | Open proposal for "one house voice" (Karen's) — settled by the no-house-style rule |
| MED | `bank-robbery/sound.md:125` | Still says write rounds sealed (retired; now `variations`) |
| MED | `docs/ideas/ableton-bed-suno-voice.md:3` | GPOM's newsreader as "the narrator's voice" |
| LOW | GPOM "House settings / House style" headings; `badcode newsreader` Voice name; "house register" round labels in BR, Camping, GPOM, downfall, future-proof | Rename "GPOM …" |

Empty / exploring (a session must run `story-style` or `variations`, never fill from a default):
Galileo look+sound, Storyverse look+sound (EMPTY); MMT look+sound, BR song + ALT cut, Camping re-cut
score, Karen song/score (EXPLORING).

## Suggested order

1. **Code** (§1 HIGH) — the only items that fire with nobody choosing them.
2. **Always-loaded words**: memory index lines, the four skill descriptions; widen `style-lint.py`
   to scan skill bodies, shared docs and code, with the missing words.
3. **Skills and storytelling.md** (§2, §3 HIGH).
4. **Story files** catch up with memory (BR grey lock + model town, Camping Rasta rule, MMT colour-only),
   then cut the Camping-era memories to pointers.
5. **MMT narration and coda**: Kai rules whether the GPOM borrowing stays.
6. MED/LOW wording.
