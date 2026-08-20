# Flow — the operating block

> ⚠️ **This file is being dissolved, 2026-08-20.** It was the single copy of "how to drive
> Flow" that six skills pointed at — a good idea that turned out to be two ideas.
>
> - **The automation half has moved into the `flow-automation` skill** (launching the browser,
>   the tool surface, the failure decision table, batches, verifying output). No skill points
>   here any more. `flow-automation` is the front door.
> - **The prompt-craft half is still below**, waiting for `scene-prompt` to absorb it. When it
>   does, this file goes.
>
> Nothing new should be added here. Add to the skill, or to the file in `docs/flow/` that owns
> the subject.

**Why the single copy existed at all**, since the lesson still applies: before 2026-08-18 each
Flow-using skill carried its own paraphrase of the launch recipe and the policy-block rules —
six copies of each. They drifted exactly as duplicated instructions always do:
`badcode-art-direction` still said *"tell the user to run flow-chrome.sh"* long after the other
five had been updated to launch it themselves, so a session entering through that skill stalled
and asked the user to do something the agent could have done.

---

## 1. A policy block looks exactly like a timeout

*(Destined for `scene-prompt` — this is about how to WRITE, not how to drive.)*

The single biggest time-saver in the whole toolkit. Over half the generations on the camping
recut were blocked by the usage filter, not slow — and over CDP a block is indistinguishable
from a slow generation. The natural instinct (retry) burns minutes on a prompt that can never
pass.

**Diagnosis rule:** two failures with no candidates, while the session is otherwise healthy
(`flow_status` fine, project loads, other prompts working) = **policy block**. Rewrite it; do
not retry it. Glance at the Flow window to confirm.

⚠️ Refined 2026-08-18: a block is the *likeliest* cause of an empty result, not the only one.
An audio failure and a rate limit look identical and want the opposite response. The full
decision table is **`flow-automation` §3**.

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

## 2. Casting a recurring character

*(Destined for `scene-prompt` — the discipline. The `character` parameter that implements it
is `flow-automation`'s.)*

A recurring character must read as the **same person** in every frame, and that likeness comes
from a **Flow Character** attached as a reference. Naming them in prose binds nothing.

- Cast via the `character` parameter on `flow_generate_image` / `flow_edit_image` /
  `flow_generate_video`.
- **HARD RULE — never regenerate a face-bearing panel without casting the Character.** Prose
  plus image references provably do not hold a face: the 2026-07-25 camping recut tried it and
  produced a third face matching neither previous version. If the character can't be cast
  (wrong project, MCP failure), **stop and fix that** rather than falling back to prose.
- 🔴 **A cast character cannot be generated on Veo 3.1 Quality**, and forces 8s
  ([`platform-controls.md`](./platform-controls.md) §1). Character shots top out at Fast.

---

**Platform craft** (how Flow behaves) is the rest of [`docs/flow/`](./README.md).
**Driving it** is the `flow-automation` skill.
**The BadCode look** stays in `badcode-art-direction` (panels) and `new-image` (brand imagery).
**Per-story prompts** live in `docs/stories/<story>/prompts.md`.
