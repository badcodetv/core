# Thread 06 — GPOM: propose the storyboard stills, scene by scene, as a spread of options

You are in `~/projects/badcode/badcode`. Read `CLAUDE.md`, then `design/2026-09-12-work-board.md`
(§ "The style-guide question" and § "Rules to add to the image skills"), then
`docs/stories/gitpush-origin-master/README.md`, `scenes/remaining-storyboard.md` (text package completed
2026-09-11, no images yet, cuts 7–17 / canon scenes 10–20, with a paste-ready prompt per still in the four
`remaining-*-prompts.md` sheets), `prompts.md` (the story's canonical image memory), and the skills
`.claude/skills/badcode-art-direction/SKILL.md`, `.claude/skills/shot-craft/SKILL.md`,
`.claude/skills/flow-prompt/SKILL.md` and `docs/cinematography/principles.md` (the visible-cost gate on
every monumental shot; ruling R1 on the near-black register is OPEN — do not call it settled).

## Why this thread exists

Images are free at the margin; video is not. So we storyboard hard up front. Kai has noticed every image
comes back muted and dystopian, and the cause is in the skills: `badcode-art-direction` rule 1 says the
muted 35mm documentary preamble "is not a stylistic option — it is the format". The images are obedient,
not inspired. From now on stills are proposed as **genuinely different options** and honed the way we
hone music: Kai picks, describes the change in words, we refine from the pick, we narrow.

## Step 1 — write the rule into the skills (first commit, before any image)

Add a "Variety mode for storyboard stills" section to `badcode-art-direction/SKILL.md` and a pointer in
`make-comic` and `flow-prompt`:

1. A storyboard beat is proposed as a **spread**, default four candidates, each a *different idea*
   (framing, distance, palette, register, time of day, what is in focus) — never four seeds of one prompt.
2. **The house register is one candidate, never all four.** At least one deliberately breaks the muted
   palette, so muted is chosen, not defaulted. The visible-cost gate still applies to every monumental
   frame.
3. **Hone like the music loop**: pick → describe the change → refine from the pick (`flow_edit_image`,
   reference-anchored, from the golden original) → narrow. Every candidate's exact prompt is recorded in
   the story's `prompts.md` and the beat's record, so "like that but X" is one cheap step.
4. Kai approves every plate before any video credit is spent (standing rule).

Show the wording in your first reply and wait for a yes before generating.

## Step 2 — the stills

Work through `remaining-storyboard.md` in its order (cuts 7–10 first, from `remaining-07-10-prompts.md`).
For each beat: read the beat and its recorded prompt; use `shot-craft` to design four different shot
specs; phrase them with `flow-prompt`; generate via the Flow MCP (`flow_generate_batch`), one channel
claimed with `./scripts/browser-channel.sh claim`; harvest to the beat's record with prompts; present the
four to Kai as a contact sheet (a small HTML page in the scratchpad or an artifact is fine) with one line
each on what the idea is. Then wait. Batch by scene, not by beat, so Kai reviews once per scene.

## 🔴 Gates

- No generation before the Step 1 yes. No video credits at all in this thread.
- A Flow policy block looks exactly like a timeout: rewrite, don't retry.
- Prompts and words stay in the repo; media goes where the beat's record says (`clips/` is media only).

## House rules

Shared checkout: commit per scene on `main`, stage only your files, never push, never switch branches.
Rundown style. Gloss every scene number with its name.

## First action

Reply with the Step 1 wording as a diff, the list of beats in cuts 7–10 with a one-line idea for each of
the four candidates of the first beat, and the channel you claimed.
