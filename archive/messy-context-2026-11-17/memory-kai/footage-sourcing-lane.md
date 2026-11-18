---
name: footage-sourcing-lane
description: "2026-08-23 (updated 2026-09-29: free British Crown films pre-1957 found): the fifth video lane — real footage that already exists and is free to PUBLISH. find-footage skill + docs/video-fx/footage-sources.md (68 sources tiered). The green tier is tiny and the traps are legal, not technical."
metadata:
  node_type: memory
  type: project
---

**Built 2026-08-23** by a 13-agent workflow (10 Sonnet researchers verifying with live HTTP calls,
then synthesis → adversarial critic → integration). Reference:
`docs/video-fx/footage-sources.md`. Procedure: the **`find-footage`** skill.

**The lane rule:** *if the thing is real and already filmed, source it; if it never existed,
invent it in Flow.* Sits alongside Flow / ffmpeg / Premiere / (AE-not-installed).

**🔴 The findings that matter, because they are counter-intuitive:**
- **"Royalty-free" is a pricing model, not a permission.** The stock houses' EULAs routinely bar
  *political* use — which is the one thing all BadCode work is. **Pexels, Pixabay and Adobe Stock
  Free all carry an explicit political-context / political-endorsement exclusion.** Adobe's
  Additional Terms §3.1(E) names *"implied or stated endorsements of political parties or other
  opinion-based movements"* verbatim.
- **archive.org's `licenseurl` is uploader-asserted, never verified.** Much of its video is
  YouTube mirrors uploaded without rights. "It's on the Internet Archive" is not a licence.
- **The adversarial pass cut the green tier from 12 to 7** — ESO, NPS, DVIDS, NARA and Adobe all
  demoted. Standing rule adopted: **green means *we verified it ourselves*, not *it ought to be
  fine*.** Every CC-BY and CC-BY-SA source is amber until a credit surface exists.
- **UK archival FILM houses are all paid** (IWM, BFI, British Pathé, Huntley). **But two free UK routes
  now exist:** `PD-UKGov` stills on Commons (Kai ruled 2026-09-12: use them) and, found 2026-09-29,
  **Crown films made before 1 June 1957** (archive.org `british_gov_public_films`, 22 items, picture
  only, audio still in copyright; **ruled usable by Kai 2026-09-29**, see [[footage-rulings-2026-09-29]]).
  Crown copyright on 1940 film has expired but those houses assert rights over their own prints
  and restorations (contested, unresolved). The one untested free UK route is **OGL v3 / the Open
  Parliament Licence** — worth twenty minutes before concluding otherwise.
- **Videvo and Mazwai are dead** (both 301 to Freepik). Any blog describing their CC tiers is stale.
- **You cannot guess an archive.org filename** — `<id>.mp4` 404s; read the exact name from
  `/metadata/<id>` (the real one was `<id>_512kb.mp4`).

**Proven end to end:** Dunkirk *is* findable green — Capra's *Divide and Conquer* (`Dividean1943_2`)
and `gov.dod.dimoc.30172`. The NARA reel that looked best (`FB-56`) **failed our own check on
re-test** and is amber.

**Open call for Kai:** whether to build a `badcode footage` CLI. The doc recommends **no** —
archive.org needs no key and no daemon, so a server would only add another port to fight over.

**Craft flag, unresolved:** Dunkirk is the most load-bearing nationalist myth in British politics
and MMT targets a right-drifting reader. Using it is a deliberate choice, not a default.

See [[premiere-bridge-initiative]] and [[target-reader-pivot]].
