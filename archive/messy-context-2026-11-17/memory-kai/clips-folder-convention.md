---
name: clips-folder-convention
description: "clips/<scene>/ holds MEDIA ONLY (2026-08-26 ruling); PROMPTS AND WORDS STAY IN THE REPO (2026-08-27 amendment) — the two halves must always be stated together"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 64a16109-6f7e-49f6-a47d-274a9605b3cb
  modified: 2026-08-26T14:50:13.185Z
---

**Ruled 2026-08-26 by Kai:** generated media lives in the open Premiere project's
`clips/<scene>/` folder, auto-created if missing. Only when no Premiere project is
known does it go to a Desktop folder.

Layout: `<mediaRoot>/<story>/clips/<scene>/` + `.../final/`. Never the project root,
never the Desktop when a project exists. Derive the root from
`premiere_status().project.path` — that call is the decision.

**Why:** scratch had drifted across `C:\Users\kai\Desktop\gpom-*` and
`D:\badcode-videos\gitpush-origin-master\` at once, and it stopped being obvious where
a scene's footage was. Kai believed clips had been **lost**; they had only been split
across two homes. One root, derived from the project, ends that class of question.

🔴 **AMENDED 2026-08-27 (Kai): this ruling is about MEDIA and only media.** Prompts, beat
lists, motion plans, rulings and revision logs stay **in the repo** —
`docs/stories/<story>/scenes/<scene>.md`, with the pre-production board in
`docs/stories/<story>/prompts.md`. Kai: *"we work on prompts and reference stills inside the
repository, and then larger video iterations happen inside the clips folder."*

**Why the amendment exists:** one day after the media ruling landed, a whole GPOM cut-3 prompt
sheet got written out to `clips/plant-room/recut-plates/`. Kai's diagnosis was right — a rule
with only one half stated gets applied to the other half too. A prompt out there is unversioned,
ungreppable, invisible to other sessions and on an unbacked-up drive. **Never state one half
without the other.** Written into `flow-prompt` (new §"Where the prompt gets written down"),
`flow-automation` and `premiere-automation`.

**How to apply:** before the first Flow generation of a session, call `premiere_status`.
Project open → write into `<dirname(project.path)>/clips/<scene>/`. No project → Desktop.
Written into `.claude/skills/flow-automation/SKILL.md` (§"While you are working") and
`.claude/skills/premiere-automation/SKILL.md` (§1b).

Related: [[premiere-import-clips-individually]], [[premiere-bridge-initiative]],
[[flow-automation-integration]], [[gpom-clip-inventory]]
