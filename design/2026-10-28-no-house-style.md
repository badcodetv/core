# No house style — taking the style out of every session (2026-10-28)

Kai, 2026-10-28: Jack found that Suno prompts written in a fresh Claude session, outside this repo,
stop sounding the same. Kai: instead of routing round the pollution, **remove it** — a style belongs
to one story or one song, never to all of BadCode. Do the same for Flow (stills and video).

Status: **done 2026-10-28** (Kai: "proceed with the plan as we've just described it"). Changes from
the plan: Jack's sealed round became the `variations` skill (`scripts/variations/round.py`, writers are
ordinary subagents, no empty-folder escape); the lint is `scripts/style-lint.py`; the blind check (a
fresh `claude -p` inside the repo) answered "no genre, no look, read the story's file". Every story has
`look.md` + `sound.md`.

## 1. Jack's trick, and what it proves

`scripts/suno/sealed-writer.sh` runs a separate `claude -p` in an empty `/tmp` folder: no CLAUDE.md,
no memory (memory is filed by project folder, so a new folder has none), no skills, no repo tools,
web search only, a one-line system prompt. `scripts/suno/sealed-round.py` feeds it only raw files
(Jack's words verbatim, the lyrics, one fresh listen), runs one ideas writer then N prompt writers
who never see each other's text, and `sameness.py` fails any round where prompts share wording.
The rules and the 17 traps are in `docs/suno-gpt/same-song-traps.md`.

What it proves: **anything that reaches every session reaches every prompt.** "Ignore it" does not
unload it (trap 2: Agent-tool subagents spawned in the repo inherit CLAUDE.md and memory too).

## 2. How style reaches every session — four channels, not one

CLAUDE.md is only one of them, and not the worst.

| Channel | Loaded | What it injects today |
| --- | --- | --- |
| **A. CLAUDE.md** | every session, every in-repo subagent | "music (drum & bass)" in the first paragraph; "When writing lyrics… match `docs/voice.md`"; the Suno row's v6 rules; the skills table ("any still in the BadCode look (both registers…)") |
| **B. MEMORY.md index** | every session (Kai's machine) | ~14 Suno lines (genre picks the singer, Personalize always off, w10/20, "house settings", newsreader narration) and the look lines ("near-black monolith register", "animate DRAMATICALLY", "Veo camera-locked"). One line each, but they are rules, stated as defaults |
| **C. Skill descriptions** | every session (the skill list) | `new-image`: "Two registers (MACHINE: near-black monolith, one thin light; PEOPLE: 35mm documentary…)", "make it look like BadCode". `suno-prompt`: "any drum & bass / track idea" |
| **D. Skill bodies + docs they send you to** | when invoked | see §3 and §4 |

## 3. Suno audit — what shapes every song

| Where | The style it imposes | Kind |
| --- | --- | --- |
| `CLAUDE.md:34` | "music (drum & bass)" | house genre |
| `docs/voice.md` §Music (CLAUDE.md says match it for lyrics) | "Drum & bass is the home genre: 170–180 BPM, dark, UK grime, Amen breaks, Reese, Chase & Status" | house genre + references |
| `docs/vision.md:14` | same D&B paragraph | house genre |
| `suno-prompt` SKILL.md ~L489 | "**Default to drum & bass.** Lead with a specific subgenre…" | house genre |
| `suno-prompt` ~L114, L195–222 | default model v6, "Always give the sliders", a default settings line, Personalize always off | house settings (trap 11: same settings every take) |
| `suno-prompt` ~L150–172 | the skeleton Genre → Mood → Instruments → Vocals, "default short" | house prompt shape (trap 1) |
| `suno-prompt` voice sections, `suno-voices.md` | "keep a UK genre tag or the voices go American", short voice clauses | house voice rules — learned on Karen/Camping, applied everywhere |
| MEMORY.md + files: `suno-four-box-atom`, `suno-v6-simple-prompts`, `gpom-narration-scored`, `gpom-narration-file-layout`, `suno-voice-playbook`, `dry-and-separate-narration` | GPOM's newsreader + cello settings, w10/20, "short prompt, one cue" | one story's style, stored as a global memory |

Engine facts that are fine to keep (they say how Suno behaves, not what we like): the DOM map and
the five silent traps (`automation.md`), form state persists, check the mode first, one session at a
time, playback recording, the §3 fix-one-word ladder, "the genre word picks the vocalist pool".

## 4. Flow audit — what shapes every still and clip

| Where | The style it imposes | Kind |
| --- | --- | --- |
| `new-image` description (every session) | MACHINE near-black monolith / PEOPLE 35mm documentary | house look |
| `new-image` body | "Every image must look unmistakably like BadCode"; "your job is to enhance it, padding the subject into the full register"; the two preambles pasted into every prompt; register anchor `docs/images/register-anchor.jpg` ("look at it before your first generation") | house look, injected word-for-word |
| `new-image` variety mode | "the house register is one candidate" of every four, "an accepted plate is house register, full stop" | house look as the default to break |
| `scene-images` L18 | every scene's mood board goes through `new-image` "the house look (near-black, one thin light)" | routes every story through the house look |
| `flow-prompt` L16–21, L95–103 | "a finished prompt is design + register", "one of the four is the house register" | same |
| `shot-craft` / `docs/cinematography/` | "one bright anchor inside the darkness", "visible cost in any monumental frame" as gates | GPOM's look written as universal craft |
| MEMORY.md: `new-image-skill`, `dramatic-video-animation`, `hybrid-video-method`, `gpom-bot-canonical-reference` | monolith register; animate dramatically; camera-locked Veo | mix of GPOM taste and real method |
| `scene-animation` L75 | house lock line "The camera does not move." | method, not look — keep |

`docs/cinematography/principles.md` §R1 already says nobody has evidence the near-black register is
right for our reader. The look was GPOM's, and it got promoted to BadCode's.

Fine to keep: policy-block rules, Flow mechanics, "stills are free", the still-approval gate,
casting/consistency method (one reference per character), the hybrid method's lanes.

## 5. The design

**One rule: BadCode has a voice and a logo, not a sound or a look.** The narrator's voice (for
words) and the logo stay global. Every sound and every look belongs to a story.

1. **Three layers, loaded at different times.**
   - **Global (always loaded):** who BadCode is, the reader, the narrator voice for *copy*, the logo,
     the repo map. No genre, no palette, no settings, no register.
   - **Engine manuals (only when a skill is invoked):** how Suno / Flow / Veo behave. Written as
     facts and options, never as defaults ("the genre word picks the singer", not "default to D&B").
   - **Story / song style (only when working on that story):** `docs/stories/<story>/look.md` and
     `docs/stories/<story>/sound.md` (or per song in `songs/<song>.md`). This is the only place a
     palette, genre, voice, preamble or slider setting may be written down. Bank Robbery's
     `look.md` is the precedent.
2. **A new story starts with an empty style file.** Its look and sound are found by an exploring
   round (many different ideas, picked by Kai or Jack), then locked in that story's file. Inside a
   story, consistency is wanted; across stories, it is not.
3. **Memory holds pointers and process, never taste.** A memory may say "GPOM's narration style is in
   `songs/narration.md`"; it may not say "w10/20, newsreader, cello".
4. **A lint keeps it out.** `scripts/style-lint.sh` greps the always-loaded layer (CLAUDE.md,
   MEMORY.md, every skill `description:`) for style words (drum & bass, D&B, BPM, near-black,
   monolith, 35mm, register, teal, newsreader, weirdness/w\d+, Variety off…) and fails on a hit.
5. **A blind check proves it.** Like `sealed-writer.sh --check`: run `claude -p` *inside the repo*
   and ask "What genre is a BadCode song? What does a BadCode image look like?" Pass = "it depends
   on the story; check its sound.md / look.md".

### What happens to Jack's sealed round

Keep it, smaller. Cleaning the global layer removes the pollution; it does not give you *independent*
writers. Its other half — N writers who never see each other's prompt, plus the sameness gate
(traps 3 and 6) — is a variety engine, and still useful for any exploring round. After the cleanup
it can run in the repo with a story's raw files, instead of escaping to `/tmp`. Proposal: keep
`sealed-round.py` as is until the blind check passes, then decide.

## 6. The moves

| # | Move | Files |
| --- | --- | --- |
| 1 | CLAUDE.md: drop "(drum & bass)"; lyrics no longer point at a genre; Suno and Flow rows say "engine manual — style lives in the story"; skills table loses the register words; add the one rule | `CLAUDE.md` |
| 2 | `voice.md` §Music and `vision.md` music line → move to the stories they came from (GPOM D&B track, Bank Robbery…) and replace with "each song finds its own sound" | `docs/voice.md`, `docs/vision.md` |
| 3 | `suno-prompt`: delete "Default to drum & bass", the default settings line and the fixed skeleton as a default; keep the engine facts; add "read the story's `sound.md` first; if empty, this is an exploring round → sealed round". Description loses "drum & bass" | `.claude/skills/suno-prompt/SKILL.md`, `docs/suno-gpt/*` |
| 4 | `new-image` becomes look-free: "read the story's `look.md`; if empty, propose four genuinely different looks". The MACHINE and PEOPLE registers + anchor images move to `docs/stories/gitpush-origin-master/look.md` (they are GPOM's). Description loses the registers | `.claude/skills/new-image/SKILL.md`, `docs/images/` |
| 5 | `scene-images`, `flow-prompt`, `shot-craft`: "house register" → "the story's look"; GPOM-only gates (one bright anchor in darkness) move to GPOM's `look.md` | three skills + `docs/cinematography/principles.md` |
| 6 | Per story: write `look.md` + `sound.md` for GPOM, Camping, Karen, Bank Robbery from what they already use (their `prompts.md`, `songs/`) | `docs/stories/*/` |
| 7 | Memory: rewrite ~10 taste memories as pointers to the story files; delete the ones the story files now hold | `~/.claude/projects/…/memory/` |
| 8 | Add `scripts/style-lint.sh` + the blind check; run both | `scripts/` |

Risk: GPOM's running scenes depend on the house look and narration settings. Move 6 must land
**before** moves 4–5, so GPOM loses nothing — its style just changes address.
