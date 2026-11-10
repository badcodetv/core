---
name: new-short
description: Use to start or make a BadCode SHORT (a 5-20 second piece of social commentary, "BadCode Shorts") — sets the short up as its own project (an ID, its own Google Drive folder, this machine's media folder, a repo folder with its own look and sound), then hands it to new-scene to make. Also keeps the running list of every short. Triggers on "new short", "let's make a short", "build this short", "short idea", "add a short to the list", "what shorts have we got", or any short named on the list (Priority Lane, The Rules, Howard Street…).
---

# New short (BadCode)

A short is **a project**, exactly like a story or a music video (Kai, 2026-11-10). It is not filed under a
"shorts" hierarchy: each short has its **own ID**, its **own Drive folder**, and each machine points that ID
at whatever folder it likes. Kai and Jack keep their own workflows; the ID is the protocol.

This skill only **sets the short up**. Making it is `new-scene` (beats → stills → clips → timeline), run on the
short's one scene. Nothing in `new-scene` is duplicated here.

## The list

**Every short, idea or made, is on [`docs/marketing/badcode-shorts.md`](../../../docs/marketing/badcode-shorts.md)**:
the 20-second cut list at the top (one line each) and a section per idea below. New ideas get the next number,
at the foot of both. When a short is being built, mark it `BUILDING` there and link its project folder; when it
ships, `DONE` with the link. Jack writes the jokes; an idea's punchline may be a blank for him.

What a short is (from the 2026-11-10 meeting, written up in that file): 5 to 20 seconds, social commentary not news,
no format. The `🔴 Lines that apply to every short` section there (no AI people in real footage, no AI likeness
of a real politician, the reader rules) applies to every one, and `marketing-gatekeeper` checks a short before it goes out.

## Set up a short (once per short)

ID: `short-<slug>` (kebab case, e.g. `short-the-rules`). Ask only what you can't work out.

1. **Drive folder.** Make it inside "Badcode - Official", under `Shorts/` for tidiness (the ID, not the path,
   is what matters):
   `rclone mkdir "badcode:Shorts/<Title>" --drive-root-folder-id <drive_root from folders.json>`, then read its ID with
   `rclone lsjson "badcode:Shorts" --drive-root-folder-id <root> --dirs-only`.
2. **Row in `scripts/drive/folders.json`:** `"short-<slug>": {"drive": "<id>", "drive_name": "Shorts/<Title>", "homes": []}`.
3. **This machine's folder.** 🛑 Never guess it: ask "which folder on this computer holds this short?" (Kai, 2026-11-10:
   his live in `D:\badcode-videos\shorts\<slug>`, but that is his choice, not a rule; Jack's will differ). Create it if
   they ask, then `scripts/drive/drive.sh where short-<slug> "<folder>"`. That adds it to the row's `homes`.
4. **Repo folder** `docs/stories/short-<slug>/`. It sits beside the stories on purpose: every scene tool, the
   style lint and provenance already work there unchanged. It holds:
   - `README.md`: the idea in the pitcher's own words, the point, the checks owed, a State table.
   - `look.md` and `sound.md` (templates in `docs/stories/STYLE.md`): **each short finds its own**; there is no
     shorts look or sound. EMPTY until found. A recurring cast (the balaclava gang) is listed under Cast with its
     reference stills; the mask itself is fixed by `docs/brand/README.md`, the rest is free.
   - `scenes/<slug>/scene.json` (`story` = the ID, `media` = this machine's folder, `beats` = the pitch's rough beats)
     and `picks.md` (dated rulings, the pitcher's words kept).
5. **Commit and push** `folders.json` and the new folder together (the other machine needs the row to read cuts).
6. **Mark it `BUILDING`** on the list.

## Make it

Invoke the `new-scene` skill on `docs/stories/short-<slug>/scenes/<slug>/`. Its gates stand (Kai approves the brief,
picks the stills, OKs words and spend). What is different for a short:

- **A short is ONE scene** (Kai, 2026-11-10: *"we shouldn't tinker out scenes, we should call it one big scene, and let's get the look and feel for each of the cuts"*). Never split a short into scenes; its beats are its cuts, and the mood board finds the look and feel of each cut.
- **Length is the joke.** Brief to three beats or fewer, timed in seconds; cut the fat (Jack: "jokes are funnier when
  you trim the fat").
- **Look and sound are found per short**, inside stage 1 or 2: `story-style` when the short wants an interview,
  or a quick pick on the mood board for a 6-second gag. Write the pick into the short's `look.md` / `sound.md`.
- **Aspect: offer portrait (9:16) as the sensible default, and ask.** Kai, 2026-11-10: "the skill shouldn't assume, but it should have the options of sensible defaults." Offer 9:16 first (phones), with 16:9 and both as the alternatives; put the answer in `scene.json` `video.aspect`.
- **Music** is a Suno track of its own when the short has music (suno-prompt / suno-automation / variations, reading the short's `sound.md`).
- **Shipping:** the cut goes to `chief-of-staff` (it writes the caption via `marketing-producer`, checks via
  `marketing-gatekeeper`, and logs the post). Then mark the short DONE on the list.
