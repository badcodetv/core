---
name: repo-records-intent-flow-holds-assets
description: "Assets (esp. Flow Characters) are often created by hand outside the repo; don't treat repo silence as \"doesn't exist\" or prescribe an all-in-repo workflow."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 58c48cec-e761-4d68-a9f0-4cb4dc2a4c3c
  modified: 2026-08-14T13:31:29.075Z
---

Kai and Jack routinely create things directly in Flow — Characters, images —
without any record landing in this repo. When the repo has no `**Flow Character:**`
line for a character, that means *the repo doesn't know*, **not** that the asset
doesn't exist. Ask for the name/id; don't conclude it needs creating.

Do not prescribe a workflow where every prompt and asset must be authored and
stored in the repo. Kai stated this explicitly on 2026-08-11: it is fine and
expected that some work happens manually in Flow.

**Why:** the repo is the canon for *intent* (story, beats, prompts, decisions);
Flow is the store for *assets*. Treating repo silence as absence produces wrong
conclusions (e.g. "Karen is uncast") and wasted regeneration — which Karen's
README already forbids, because her visuals are Jack's.

**How to apply:** when a prompt needs a Character, write a `**Cast:**` instruction
line naming it and ask for the exact Flow tile name — casting matches the tile
label with `exact: true`. See [[karen-visuals-are-jacks]].

**⚠️ It is not just Flow — ElevenLabs too (2026-09-03).** The camping narration
sheet said *"the voice does not exist yet — no `voice_id` is recorded anywhere in
the repo."* I wrote that line myself, treating repo silence as absence. Jack's
screenshot showed **"Camping Narrator" already built and saved**, and a 1,212-credit
voice-design plan sitting in `voice.md` as work still ahead when it was already
paid. **Before writing "not yet made" about any external asset — a Flow Character,
an ElevenLabs voice, a Suno persona — ask.** The repo is silent about assets by
default; that is its normal state, not a finding.

**⚠️ `flow_list_characters` also lies (found 2026-08-14).** It scrapes
`a[href*="/character/"]` from the *project root*, but Flow's redesigned UI keeps
Characters behind a left-nav **Characters** tab, and `flow_open_project` lands on
All Media. So it returns `[]` on a project that has plenty. On 2026-08-14 this made
me sweep seven projects, report "no Karen Character exists anywhere", and propose
creating one — while Karen, Susan and Aarron were all sitting in the very project
Jack had given me. **A `[]` from that tool is not evidence of absence.** Click the
Characters nav item first, then call it. See [[flow-mcp-selectors-stale-2026-08]].
