---
name: website-reset-initiative
description: "2026-08-07 website reset — \"The Ledger\" design direction picked, plan at design/2026-08-07-badcode-website-reset.md, deployment out of scope"
metadata: 
  node_type: memory
  type: project
  originSessionId: 16665946-814e-463f-ab2c-348bc827ca34
  modified: 2026-08-07T18:37:39.562Z
---

2026-08-07: full reset of the BadCode website. Plan (17 tickets, reviewed) lives at
`design/2026-08-07-badcode-website-reset.md`. Status: proposed, not yet executed.

**Why it happened:** the site assumed comics-on-the-website while the actual pivot
(Aug 4–6, recorded in every `docs/stories/*/README.md`) is to **narrated story
videos**. Six research agents — three over the repo, three over the web — landed on
one conclusion: *the site is not where people watch*. Kurzgesagt hosts no video;
A24 sends you to Amazon. The site's only defensible job is being the one place a
story exists as several media at once, with the argument connecting them.

**Design direction: "The Ledger"** (chosen by Kai over "The Witness" and "The
Wall"). Homepage is a numbered catalogue. Signature is **the blade** — one line of
light down the gutter that forks; the dead branch terminates with a ring, the
unfinished branch runs as gold dashes through every catalogue entry with a node per
story. That is `future-proof.md:167-172` built rather than illustrated.

**Locked rulings:**
- Deployment/hosting/domain **entirely out of scope** — Kai does it himself.
- Kill the cyan `#46d5ff` — it is why the site read as a crypto project. One accent:
  signal gold `#E8C98A`, meaning only "transmitting now".
- Mono demoted to the catalogue stamp. Archivo variable (width axis) for display/UI,
  Instrument Serif for the narrator's voice **and only that** — it is what makes a
  visually divergent story page still read as BadCode.
- Story metadata = **YAML frontmatter in `docs/stories/<slug>/story.md`** (which
  already had some), extracted by a Vite plugin into a virtual module with HMR.
  Kai's explicit goal: edit the story file with a model, site updates.
- Video: self-host the short cuts, YouTube facade for the long film. Audio: facade
  embed, Bandcamp default (SoundCloud is not a Suno AI partner — see
  `docs/marketing/platform-playbooks.md`). No custom players — rent them.
- Atlas retired and deleted. Four comics deleted; features harvested into ONE
  example comic which *is* the `/origin` page (GPOM as a scroll comic).
- Storyverse and Future Proof become ordinary catalogue entries with a read variant.

**Open:** the homepage hero line — Kai is writing it. Ships as a placeholder
constant `HERO_COPY` in `routes/Home.tsx`; T17 gates on it being real.

Related: [[gitpush-origin-master-arc]], [[storyverse-standalone-initiative]],
[[comic-library-design]], [[marketing-initiative]].
