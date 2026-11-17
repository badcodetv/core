Kai, the context reset is done and merged to main. How it works now:

1. CLAUDE.md is one page (7 KB, down from 31 KB) and holds only what's true for every task: what BadCode is, your four ideas (offer a way out not a complaint, democracy means changing how government works, more than materialism, the logo), a few working rules, and where things live.
2. Every story and short has a short badcode.md at the top of its folder: its current look, sound, rules, Flow project and library pieces, with no history and no other story named. It's the only story file read before a prompt; the long look.md / sound.md stay as the record.
3. docs/library/ is the tool shed: 80 looks, 79 sounds and a tricks page (Unsplash photo as the look, clean room, music before picture, the balaclava). It applies to nothing until a story copies a piece into its badcode.md.
4. Starting a story, Claude proposes which library pieces to take in and we pick. First test: #89 The Freddo Mortgage, where I picked clean room only.
5. The engine rules that were in my private memory are now in the repo under docs/rules/ (flow, suno, voices, premiere, working), so your machine has them too.

Why the earlier clean-ups leaked: memory carried story looks into every session; look.md files kept crossed-out rules inline and got pasted whole into writer briefs; and the compulsory cinematography and Nano Banana docs treated GPOM's dark register and "camera + film stock + ISO" as the default. That's where 35mm came from. Full write-up: docs/context.md.

Two things for you:
- 🔴 Your machine has its own Claude memory, which I can't reach, and it'll keep leaking until it's reset too. Paste this into Claude Code in the repo: "Context reset, see docs/context.md. Copy my memory folder into archive/messy-context-2026-11-17/memory-kai/, commit it, then empty my memory except one file saying rules go in the repo (docs/rules/, the story's badcode.md, or CLAUDE.md). Move any engine rule that isn't already in docs/rules/ into it first."
- 🟡 Flow driver: the MCP generate tools still use whichever project tab is open. For now there's a written rule (one Flow project per story, opened before its first call; ids are in each badcode.md), and a plain generate now refuses if a leftover reference image is still attached. Your parallel-tabs rework is the place to tie each tab to a story's project for real.
