# Flow — the operating block

**The single copy of "how to drive Flow" that every Flow-using skill points at.**

There are six skills that touch Flow (`badcode-art-direction`, `new-image`, `edit-panel`,
`animate-slide`, `make-comic`, `music-video-short`). Before 2026-08-18 each carried its own
paraphrase of the launch recipe and the policy-block rules — six copies of the launch
sequence and six of the block triggers. They drifted, exactly as duplicated instructions
always do: `badcode-art-direction` still said *"tell the user to run flow-chrome.sh"* long
after the other five had been updated to launch it themselves, so a session that entered
through that skill stalled and asked the user to do something the agent could have done.

**Skills reference this file. They do not restate it.** If you find yourself pasting any of
the below into a SKILL.md, link here instead — and if the guidance is wrong, fix it *here*,
once.

---

## 1. Bring the browser up yourself

Image and video generation run through the `flow` MCP server. If `flow_status` — or any flow
call — returns `{ error: true, code: "NOT_RUNNING" }`, **do not bounce this to the user.**

1. `Bash` with `run_in_background: true` → `./scripts/flow-chrome.sh`
   (Chrome with CDP on port 9222 and the persistent `.flow-profile/` session).
2. Wait for the port:
   `for i in $(seq 1 20); do curl -s -m 2 http://localhost:9222/json/version >/dev/null && break; sleep 1; done`
3. `flow_status` → if `loggedIn: true`, proceed. **Only** if `loggedIn: false` (first run, or
   an expired session) ask the user to log into Google in the window that opened.

- The login persists in `.flow-profile/`, so a relaunch is normally already signed in.
- **Don't relaunch Chrome between generations** — the MCP caches its CDP attachment.
- Characters are **project-scoped**. Open the right project before casting or generating, or
  the character silently will not exist.

## 2. A policy block looks exactly like a timeout

This is the single biggest time-saver in the whole toolkit. Over half the generations on the
camping recut were blocked by the usage filter, not slow — and over CDP a block is
indistinguishable from a slow generation. The natural instinct (retry) burns minutes on a
prompt that can never pass.

**Diagnosis rule:** two failures with no candidates, while the session is otherwise healthy
(`flow_status` fine, project loads, other prompts working) = **policy block**. Rewrite it; do
not retry it. Glance at the Flow window to confirm.

### The four triggers

1. **Real brand names**, prominent or repeated — a supermarket fascia, a marque plus a
   plate, branded packaging. Asking for a **legible** real logo is the most reliable block
   there is.
2. **Likeness phrasing for faces** — "same face, same bone structure as the reference" reads
   as reproducing a specific real person.
3. **Stacked destitution** — burn barrels + tent city + collapsed figures + "gaunt" in one
   prompt, especially beside a real identifiable business.
4. **Legible text attributed to real institutions** — invented headlines quoting a real
   central bank, government body or newspaper.

### Rewrite table

| Instead of | Write |
| --- | --- |
| "Waitrose storefront, green signage" | "an upmarket supermarket fascia in green and white, lettering indistinct" |
| "black BMW X7, plate T4RQ 1N" | "a large black luxury SUV, private plate" |
| "same face, same bone structure as the reference" | "keep this character's design consistent with the reference — same hairstyle, build, colouring and wardrobe" |
| "gaunt, squalid, collapsed among rubbish" | "weary, worn, sitting among the debris" |
| a headline quoting a real bank | describe the newspaper; put the line in a `NarrationBox` overlay |

**Load-bearing text belongs in the comic, not the image.** A sign or headline the story needs
readable should be a bubble/narration overlay in `@badcode/comic` — sharper, editable,
translatable, and unblockable.

## 3. Casting a recurring character

A recurring character must read as the **same person** in every frame, and that likeness comes
from a **Flow Character** attached as a reference. Naming them in prose binds nothing.

- Cast via the `character` parameter on `flow_generate_image` / `flow_edit_image` /
  `flow_generate_video`.
- **HARD RULE — never regenerate a face-bearing panel without casting the Character.** Prose
  plus image references provably do not hold a face: the 2026-07-25 camping recut tried it and
  produced a third face matching neither previous version. If the character can't be cast
  (wrong project, MCP failure), **stop and fix that** rather than falling back to prose.

## 4. Which surface to reach for

| You want | Use |
| --- | --- |
| A still | `flow_generate_image` |
| A change to an existing still | `flow_edit_image` (reference-anchored) |
| Motion where something in the world moves | `flow_generate_video` |
| A camera-only move on a still | **post (ffmpeg / the edit)** — see `video-prompting.md` §9 |
| Runway: continue a clip with its own context | `flow_scene_extend` (Scene Builder) |
| A frame out of a clip, into the gallery | `flow_scene_save_frame` |

## 5. Review what you generated — properly

**Do not judge a clip from three sampled frames.** A door that swings open for 1.5 seconds sits
entirely between them, and you will report success on a broken clip (done, 2026-08-18).

```bash
scripts/video-contact-sheet.sh clip.mp4              # every frame at 4fps, one image
REGION=left scripts/video-contact-sheet.sh clip.mp4  # crop a band + brighten it
```

Near-black BadCode frames hide motion at full-frame scale — use `REGION` when the suspect
detail is small or dark.

---

**Platform craft** (how Flow behaves) is the rest of [`docs/flow/`](./README.md).
**The BadCode look** stays in `badcode-art-direction` (panels) and `new-image` (brand imagery).
**Per-story prompts** live in `docs/stories/<story>/prompts.md`.
