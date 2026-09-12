# Thread 07 — Magic Money Tree: research the real footage (the war and the NHS)

You are in `~/projects/badcode/badcode`. Read `CLAUDE.md`, then `.claude/skills/find-footage/SKILL.md`
and `docs/video-fx/footage-sources.md` (68 sources tiered green / amber / red, with the verification table
of what was proven live versus only read), then the story: `docs/stories/magic-money-tree/README.md`,
`storyboard.md` (**The Future He Never Saw** — the single canonical documentary storyboard, chosen
2026-09-11), the per-shot records `storyboard/p01.md`–`p08.md`, and
`research/documentary-austerity-emergency-investigation-2026-09-11.md` (the historical spine: 2008 crisis,
2010 austerity, the nurse's 2017 Question Time question, "magic money tree", Covid). Read
`docs/marketing/the-reader.md` too: name the decision-maker, never the technology; never "you've been duped".

## Goal

For every beat in `storyboard.md` that shows something that really happened — the war footage, the NHS,
Parliament, Question Time, the Bank, the Covid response — find footage **we are allowed to publish in a
political film**, and record it so Premiere can open it. Deliverable: `docs/stories/magic-money-tree/footage.md`,
one row per beat: what the beat needs, the source, the exact item URL, the licence *as verified* (not as
asserted), tier, resolution and duration, the download command, the SHA-256 of the file, and the fallback
if nothing green exists (a public-domain still, or Flow if the thing never existed).

## The rules that decide everything here

- **"Royalty-free" is a pricing model, not a permission.** Stock-house EULAs routinely bar political use,
  which is what all our work is. Read the licence text for each item; quote the clause.
- **archive.org's `licenseurl` is uploader-asserted.** Nothing amber ships without a per-item human check;
  list those for Kai with the specific doubt.
- **The free tier is US federal film, newsreel with expired copyright, NASA, and Wikimedia Commons CC0 /
  public domain.** UK material is the hard case: Crown copyright expiry, the Open Government Licence,
  Parliament's own licence (Question Time is BBC — not ours; say so and offer the alternative), IWM's terms.
- **We buy no footage.** Never end at "British Pathé sells it": state the free route or say there is none.
- If the thing never existed, it is Flow, not sourcing.

## 🔴 Gates

- The WebSearch budget is ~200 per session shared by all subagents: cap each researcher, stagger them,
  and prefer WebFetch of known primary URLs.
- Nothing is marked green unless *you* opened the licence page in this session. Report what you could
  not verify as ⬜, never as a guess.
- Downloads go to `clips/mmt/<beat>/` (media only), never into the repo; the words go in `footage.md`.

## House rules

Shared checkout: commit per pass on `main`, stage only your files, never push, never switch branches.
Rundown style.

## First action

List the beats that need real footage with the historical event each one shows, group them by likely
source family (US federal / UK Crown / Parliament / Commons / none), and start with the war beats.
Report after the first family is done.
