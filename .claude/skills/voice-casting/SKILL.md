---
name: voice-casting
description: Use to CAST the speaking voices of a BadCode film, scene or short by options. For each speaking role it writes three to five genuinely different AI Studio voice profiles (a different voice, age, region and delivery each), renders that role's real lines in every one, and puts them on a PICKS PAGE where Kai or Jack play, pick one per role and leave a note. Rounds run on the notes; the pick is written into the story's sound.md and the profile becomes the voice used from then on. Triggers on "cast the voices", "voice options", "pick the voices", "which voice for the reporter", "voices I can pick from", "audition voices", "try different voices", "this voice is wrong, give me options". Making the voice engine work is docs/ai-studio; syncing lips is lip-sync-dub; placing the voices in a cut is scene-timeline.
---

# Voice casting (BadCode)

**A picking page for voices, like the mood board is for stills.** Jack asked for it on 2026-11-11 (Priority Lane:
"put the voices in a skill that I can pick from like the new scene artifact"). First run:
`docs/stories/shorts/priority-lane/voices/`.

## Before anything
- Read the story's `sound.md`. If a role is already ruled, don't recast it unless asked. If the file is empty, this
  skill fills its **Voices** part. Never carry a voice over from another story (CLAUDE.md, no house style).
- Read `docs/ai-studio/README.md`: the engine, the traps, and **the free-tier limits: 3 calls a minute, 10 a day per
  model**. A casting round is roughly 4 roles × options, so budget it, and say so if it won't fit in today's 10.

## The round
1. **Roles and lines** come from the scene's `script.json` (`lines[].who`). Each option reads that role's real lines,
   joined into one take, so the pick is made on the actual words.
2. **Options: 3-4 per role, each one different on purpose.** Change the voice name and at least two of: age,
   gender, region or accent, class, delivery (deadpan / petulant / booming / hissing...). Name the region and don't
   spell out phonetics (README: "too northern"). One profile per file in
   `docs/stories/<story>/…/voices/profiles/<role>-<letter>-<voice>.md`, in Google's shape
   (`# Audio Profile` / `## Scene:` / `## Sample Context:`; example: any file there).
3. **The same-prompt check** on every profile: `python3 scripts/variations/fresh.py < profile.md`. Scene facts that
   repeat (a car's back seat) can stay; a repeated *description of a voice* means rewrite it.
4. **Render**, paced (one call every ~22 s):
   `set -a; . ./.env; set +a; uv run -q --with "google-genai<2" python3 scripts/aistudio-tts.py <lines.txt> <out.wav> --profile <p.md> --voice <Name>`
   into the media folder's `audio/casting/` (from `scene.json` `media`, through `scripts/drive/localmap.py`).
   **Check every take's length**: about one in five comes back cut short, so re-run those.
5. **Recipe card** for each take: `scripts/provenance/prov.py card` (docs/provenance).
6. **The page**: a `voices/picks.json` for `scripts/scene/build-picks.py`. There is one section, one group per
   role (`kind: "audio"`), and each option's label names the voice and the idea. Build it, then publish it with
   every wav at its `src` path and `capabilities: {db:{}, user:{}}`. Log the page in the scene's `trail.json`.
7. **Read the picks**: dump the db collection `picks` into `feedback/` before acting on it ("Artifacts are the UI").
   A note like "older" or "less posh" is the next round: new profiles for that role only, with the page's `round` set to N+1.
8. **When a role is picked**, write it into the story's `sound.md` (voice name + profile path + Jack's or Kai's
   words), log it in `picks.md`, and move on to `lip-sync-dub` / `scene-timeline`.
