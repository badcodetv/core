---
name: scene-animation
description: Use to turn a BadCode scene's picked stills into a SEQUENCE OF ANIMATED SHOTS — two or three ways to animate each frame (the shot's job, what Veo does with the camera locked, what Premiere and ffmpeg add), picked on the storyboard page, then run as Flow video clips, checked, named and put in a Premiere bin, with re-rolls from Kai's notes. Stage 3 of new-scene. Triggers on "animate the storyboard", "how should this frame move", "animation options", "turn the picks into videos", "make the clips", "re-roll shot N", "recut <scene> with new shots", "one continuous shot / a long take".
---

# Scene animation: options → clips (BadCode)

**Stage 3 of a scene.** Before it: **`scene-images`** (the storyboard). After it: **`scene-timeline`**.
The whole loop is **`new-scene`**, which also holds the scene folder layout and the tools.

## Read first

- The scene's `storyboard.json` and picks.
- **`shot-craft`** for what each shot should be; **`flow-prompt`** for how Omni actually behaves; **`flow-automation`** for driving and recovering.
- `docs/video-fx/hybrid-method.md`: Veo animates with the camera locked, Premiere moves the camera, ffmpeg draws every word.
- `docs/video-fx/continuous-shot.md` when a beat must be one unbroken shot longer than a clip.
- **`premiere-automation`** for the bin import.

**The gate:** never spend video credits on a still Kai has not picked (the still-approval gate). The one
exception is when Kai says to go ahead without him ("I'm on a call, just make it"): then make the call
yourself, animate the best two so he still chooses, and say so.

## Animation options

For each frame, write 2–3 ways to animate it into `animation-options.json`
(`{sequence_notes:[{rule,why,source}], frames:[{n, job, options:[{id, label, idea, lanes, veo_prompt, cut, seconds, risk}]}]}`). Each option gives:
- the *job* of the shot
- the lanes: what Veo does with the camera locked, what Premiere does to the camera, what ffmpeg draws
- the `veo_prompt`, or none if the option is post-only
- the cut in and out, the seconds, and the risk

Rules that have held:
- **Lock Veo's camera.** "The camera does not move." at the start and end. Premiere does every push, zoom and pan, eased (hybrid method).
- **Animate dramatically**: dive, storm, hard flashes. Not vague twinkle.
- **Few movers.** Omni struggles past about three moving figures. Give the motion to rain, haze, light and one actor.
- **Words are ffmpeg.** Never ask Veo for readable text.
- **Timed events** use timestamp brackets `[00:00-00:01]` in whole seconds. These place things roughly; Premiere puts them on the beat. Keep flashes at **3 a second or fewer** (photosensitivity).
- **6–8s clips.** Eight seconds is never a reason to cut a beat short: chain clips last frame to first instead (`docs/video-fx/continuous-shot.md`). Long clips redraw the scene after a few seconds, so cut before that happens.

**The motion is an argument, not decoration**: one deliberate move that serves the beat. The machine that doesn't care, the wealth piling while the room dims. Imply it; never sermonise it.

## What the model cannot do, whichever model it is

**Added 2026-08-14** (moved here from the archived `animate-slide` by the 2026-10-23 skills audit), paid for with five rounds on one four-second shot (the Karen river
drop). These are properties of video diffusion, not of Veo or Omni, so they survive an
engine change. Engine-specific craft lives in
[`docs/google-flow/omni-flash.md`](../../../docs/google-flow/omni-flash.md) — check it
before writing a prompt for a named engine.

- **⚠️ Never ask for a falling, thrown or dropped object rendered in flight.** There is
  no physics engine behind any of these models — only the absorbed statistical pattern
  that unsupported things move downward — and per-frame drift compounds. Ours flew
  upward, landed on invented terrain, and bounced, across four rewrites.
  **Every frame the object is airborne on screen is a frame the model can get wrong,
  and it will use them all.**

  | Instead of | Do |
  |---|---|
  | render the fall | render the **release**, and let the object leave frame within a few frames |
  | render the landing | let it be a **sound**, delayed by the right beat |
  | one continuous shot covering the event | **cut** — a wide that stages it, an insert that loses it, the aftermath |

  This is not a compromise. A real camera never catches a whole accidental fall, so the
  occluded version is *also* the more truthful shot. Restraint is authority here too.

- **Name the shutter when anything moves fast.** `shot at 24fps with a 180-degree
  shutter, so anything moving fast smears with natural motion blur.` Models render fast
  motion sharp in every frame, which is the single loudest AI tell; a real camera smears
  it. `[confirmed 2026-08-14]` — it turned a phone drop from a crisp artefact into a
  streak, with no post pass needed.

- **State constraints positively.** Most of these engines have no negative-prompt
  support and `no…`/`don't…` phrasing backfires, putting the unwanted thing into the
  prompt as content. Write `the bridge lights hold steady`, not `the bridge does not
  move`. (`no cuts` and `no dialogue` are vendor idiom and safe, and so is our lock line "The camera does not move.", which is proven across every GPOM clip.)

- **Name exactly one ambient motion.** Given none, models tend to animate the whole
  frame; given one — *"the reflections shift on the dark water"* — the rest settles.

- **Prefer the shorter duration.** Drift compounds per frame, so 4s is meaningfully
  safer than 10s on anything with real motion in it. Don't default to the maximum.

## The storyboard page

Build the storyboard page with `python3 scripts/scene/build-storyboard.py <scene-dir> <out.html>` and
publish it like the mood board (`capabilities: {db:{}, user:{}}`, same file path every round, then
`prov.py trail <scene-dir> --stage storyboard … --rebuild "python3 scripts/scene/build-storyboard.py …"`). Kai picks a still and an option per frame (db `picks`,
kinds `still`/`anim`). Dump `picks` and `notes` into the repo before reading them (`ArtifactData list` with `out_dir` from `prov.py feedback-dir`), then `prov.py trail … --feedback --decided "…"` per pick. In the reply, **break each decision down plainly**: the choice, what each option
buys, and your recommendation. Kai has asked for this.

## Video

Write `video-jobs.json` from the picks (`anim_picks`, `still_picks`, `skip` for kept or post-only frames,
`cast`; the format is in `scripts/scene/shots.py`). Then:

```bash
python3 scripts/scene/shots.py docs/stories/<story>/scenes/<scene>        # check the job list
FLOW_CDP_PORT=<port from flow_status> npx tsx scripts/scene/run.mts docs/stories/<story>/scenes/<scene> [keys…]
```

- Run it with `run_in_background` and wait for the notification. **One Flow user at a time**: never run the runner and a Flow MCP call together.
- Settings are fixed: Omni 1.1 Flash, Frames, 16:9, count 1 (`flow_generate_video` fails on Omni Frames; the runner is the route). Ask before spending video credits.
- Each clip's recipe card is written when `match.py` names it (docs/provenance).
- **Check every clip before telling Kai.**
  - Make a contact sheet: `ffmpeg -i clip.mp4 -vf "fps=2,scale=480:-1,tile=4x4" -frames:v 1 sheet.jpg`.
  - Look at it for a redraw, a morph, extra people, or text slop.
  - Crop and enlarge the subject at the first, middle and last frames.
- Import the passing clips to the scene's Premiere bin (`premiere_import` with `bin`). Don't place them unless asked.
- **Choosing between candidates** (two clips for a shot, a re-roll against the original): put them on a picks page, `scripts/scene/build-picks.py` from the scene's `picks.json`, never a hand-made page.
- **Re-rolls.** Kai's notes become `extra` rows in `video-jobs.json`, each with `key` like `12-r2`, the still, the duration, the new motion and `why` in his words. If a new still is needed, go back through a small `scene-images` round first. Show all candidates and let him pick, unless he said to go ahead.

Log every pick and ruling in `picks.md` as it happens.
