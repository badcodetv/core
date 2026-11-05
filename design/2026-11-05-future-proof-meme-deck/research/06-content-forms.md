# 06 — Content forms: where a "meme-deck" skill fits

Repo only, no web claims. Sources read: `docs/marketing/short-form-funnel.md`, `chief-of-staff/plan.md`, `board.md`, `.claude/skills/` (listing + `scene-dialogue`, `variations`), `scripts/scene/` listing.

## 1. What the plan says (relevant facts)
- Funnel (short-form-funnel.md): **short-form -> long-form art (the EP) -> actual answers**. Future Proof is named as "the deeper layer", *deliberately deferred until the EP is rolling*. The deck is therefore the "actual answers" end, not a top-of-funnel post.
- Plan goal (plan.md s2): get finished work out, keep it going out, start a mailing list. Nothing is published; the stated bad pattern is "a new idea gets a research document; nothing goes out". **This research round is exactly that pattern; the deck must not be allowed to jump the queue of board items 1-5 (accounts, list, Camping serial).**
- Lanes (plan.md s5): A Money For Something (topical monologue, balaclava host, TTS, pipeline not built), B back catalogue, C Archive, D song. "Opening a lane: only once open lanes go out steadily; newest lane pauses first." Short wins (~2 min).
- Gaps (plan.md s4) the deck answers: **"Showing the fix, not just the fault"** (reader needs hope as well as anger) and **"Somewhere to send people"** (website not live). Martin Lewis / small-ideas is a topical hook of the Money For Something kind.
- Short-form funnel names a "meme tier" (10-second content standing alone but advertising the universe) already in `docs/ideas/`.

## 2. Where it fits
**Not a new marketing lane yet.** Recommended placement:
1. **Form, not lane.** A meme deck is a *content form* (like a comic or music video). Its outputs feed existing lanes: (a) the full deck = a page on the website ("somewhere to send people") and a ~2 min talk-to-camera cut; (b) single slides = meme-tier shorts; (c) a topical slide set = Lane A material when Money For Something exists (Kai as talking head is a conflict with the balaclava host: **open question for Kai**, who fronts it).
2. **Board:** add as a "Then" item after Camping part 1 is posted, owned by Kai (talk) + Claude (build). Add "Showing the fix" gap as its reason. Do **not** insert above items 1-3.
3. **Time-sensitive exception:** the Martin Lewis hook decays. A *single* topical slide/short (one meme, 10s) can ride Lane A scratch-pad rules now; the full deck waits. Chief-of-staff should put this to Kai as one of the three decisions.
4. **Plan vs canon:** Future Proof canon stays `docs/stories/gitpush-origin-master/future-proof.md`; the deck is a *story-like production* so it gets its own folder (`docs/stories/future-proof-deck/` or under GPOM) with its own `look.md`. No house look; the skill must route through `story-style` first.

## 3. How BadCode skills are shaped (observed)
- Frontmatter `name` + long `description` with explicit **Triggers on "..."** phrases and a "Mechanics belong to X" boundary line.
- Body order: Why/Kai quote -> When (and when not) -> numbered stages -> page build command -> Rounds -> Into the scene -> Worked example.
- **House pattern (scene-dialogue, variations, scene-images):** talk first (brief in one message) -> N separate writers who can't see each other, one pushed to an extreme each -> one synthesis ranks harshly -> a **picking page** (artifact, `capabilities: {db:{}, user:{}}`, one tab per unit, Pick button + note per line, republished to the **same path** each round) -> **dump notes into `feedback/r<N>/` before acting** -> answer on the page with `notes-r<N>.json` -> log with `prov.py trail ... --decided` -> hand off to the next skill.
- Mechanics live in `scripts/scene/*` (`dialogue-workflow.js`, `build-*.py`, `*-template.html`); a skill is mostly procedure + the facts that save time. Rules are guides, not gates (Jack, 29 Oct): say which you depart from.
- Map groups: The film / Engines / Judgement / Words, ideas, look / Marketing. A meme-deck skill is **Words, ideas, look** (beside `new-story`, `variations`), reusing `story-craft`, `new-image` and `scene-dialogue`; it calls `chief-of-staff` for release.

## 4. Proposed skill: `meme-deck`
**Name/description:** "Use to make a slideshow of memes, jokes and diagrams that argues one idea, as a website and a talk-to-camera video. Triggers: 'meme deck', 'slideshow', 'explain X in memes', 'make this a talk', 'slides for the video'. Words stay with scene-dialogue/story-craft, stills with new-image, the look with story-style, release with chief-of-staff."

**Stages (house pattern):**
0. **Look first.** If `look.md` empty -> `story-style` (a deck is a story; no default look, no inherited meme-template aesthetic).
1. **Brief interview** (one message): the one sentence the deck argues; the reader (the-reader.md rules: no "duped", name the decision-maker); length (target ~2 min talk, N slides); the hook (e.g. "invented before electricity"); who speaks (Kai to camera / narrator voice); what the deck must hand over (a share, a sign-up, an action) so it serves the goal (mailing list).
2. **Spine -> `spine.json`.** The argument as an ordered list of slides, ending first: each = claim, evidence slot (source + solidity grade), the laugh, the picture, the spoken line, seconds. Evidence is checked before jokes (claim ledger idea from the coin docs: every factual slide carries a source).
3. **Options round (variations-style):** ~8-10 separate writers, each pushes one *meme shape* to an extreme (e.g. reaction-image, the-diagram-that-lies, two-panel-compare, "nobody: / me:", fake-UI/software metaphor [composition = pick-and-mix], timeline-then-vs-now, the narrator-from-the-future dispatch, deadpan-chart, understatement). Each writes every slide. A **sameness gate** (reuse `scripts/variations/fresh.py` thinking) refuses shared wording. Synthesis ranks harshly and assembles 3 drafts of the deck.
4. **Picking page** (`build-deck-picks.py` + template, like build-dialogue): tab per section of the deck; each slide shows 3 versions as slide thumbnails with Pick + note; ranked writers underneath; Open questions tab. Phone-width checked. Republish to same path.
5. **Art round (scene-images pattern):** for picked slides, stills via `new-image` in the deck's `look.md`; free (stills read 0 credits). Rights check on meme imagery: **never use real people's likeness or copied meme templates without licence; originals or generated only** (law/licence rules are not loosened). 3D scenes (three.js) are an *option per slide* only where motion explains a mechanism (e.g. votes bundles splitting); default is a still.
6. **Build the deck** (website: scroll or arrow-key slides, one `deck.json` source -> HTML) and the **talk cut**: the same `deck.json` drives (a) the web page, (b) a teleprompter/notes view for Kai, (c) a screen-recorded or rendered video track fed into `scene-timeline` for the talk-to-camera composite. One source, three outputs.
7. **Rounds on notes**, as scene-dialogue s4 (dump -> reply on page -> rebuild); edit `deck.json` by hand for small changes, rerun writers only if the brief changes.
8. **Release hand-off:** `chief-of-staff` cuts it into meme-tier shorts (one slide + one line each), a caption set past the gatekeeper, and a board entry; provenance: `prov.py trail` per page, `final.json` frozen at the end.

## 5. Risks / open questions for Kai (max three)
1. **Sequencing:** the plan defers Future Proof until the EP rolls and bans new research-before-publishing. Ship one topical slide now, rest after Camping part 1? 
2. **Who is the face:** Kai to camera vs. the planned balaclava host (lane A). Both could coexist (host intro, Kai explains) but this is a brand call.
3. **Reader risk:** the deck's hook ("system is ancient") can drift into "politicians are idiots" / anti-democratic cynicism, which feeds the drift-right reader the wrong way. Each slide should name a *decision-maker and a fix* (composable voting is the hope, per the "show the fix" gap). Also: Martin Lewis is a real person; reference small-ideas.org as a thing happening, do not use his likeness or imply endorsement.

## 6. Reusable parts already in repo
`scripts/scene/dialogue-workflow.js` (writers + synthesis), `build-dialogue.py` + `dialogue-template.html` (tabbed picking page), `build-picks.py`, `scripts/variations/fresh.py`, `prov.py trail`, `story-craft` checklist, `new-image`. New code needed: deck spine schema, deck picks template, deck renderer (HTML/three.js), notes/teleprompter view.
