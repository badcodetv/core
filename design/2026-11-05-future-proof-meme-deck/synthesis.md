# Future Proof meme deck: synthesis (2026-11-05)

Built from research files 01-06 (repo) and 10-21 (web). Web figures are mostly search-snippet level: every number on a slide needs a primary-source check first (flagged "CHECK"). Look is NOT chosen here: it goes through `story-style` (no house look).

## 1. The argument and the hook

**One sentence:** We still run the country on a once-every-five-years, all-or-nothing system; software solved "many small choices, tested, reversible" decades ago, so we are allowed to ask for the same, and you do not need a plan from us to start: you have the pen.

(Compressed takeaway from canon: permission to question the system you inherited. End open, as a construction site, never "here is the plan".)

**Fact-checked opening hook.** Kai's "invented before electricity" is FALSE as worded (Faraday induction 1831, Great Reform Act 1832; research 15). Use instead:

- "Parliament is about 760 years old (1265). The secret ballot is 153 (1872). Your phone is about 19. We vote in public, out loud, until 1872: the secret ballot was version 2.0." (1265 parliament.uk; 1872 secondary; phone age CHECK.)
- Or: "Parliament was designed before the light bulb" (Swan Dec 1878, Edison 1879; true).
- Do NOT say "one MP per seat is older than electricity": the single-member map is 1885, after Godalming (1881).
- Alt version-number gag: "v1832, patched to 1.9 in 1928, no update since." Target the decision-makers who never shipped the patch, not "the system" or voters.

## 2. Slide-by-slide outline (36 slides)

Format: **#. Visual** | Caption | Spoken line (Kai) | Type (S static, A animated, 3D three.js). "Own" = original art in meme grammar (legal: no lifted photos). Every factual slide carries source + solidity grade in `spine.json`.

### Cold open (1-5)
1. **Own: a blinking cursor on a dark screen, then a daylight cut** | "Who is talking?" | "I'm Kai. The narrator you've heard in the film wrote the postmortem. I'm here for the part it can't write: the fix." | S. (Ten-second "who is speaking" bridge from GPOM, no signup, film must feel complete without it.)
2. **Timeline strip, three eras (1265 / 1872 / now), phone lit at the end** | "Parliament: 760. Secret ballot: 153. Your phone: 19." | "The way we pick a government is older than the light bulb. Since then we got the internet, and now AI. Nobody has told the ballot." | A.
3. **This Is Fine (own redraw, dog in a ballot-box room)** | "We update the kettle more often than the country." | "Your kettle gets a firmware patch. Government ships on CD every five years." | S.
4. **Own: bank app asking ten questions before moving £50 vs a ballot paper with one cross** | "Bank: 10 questions for £50. Parliament: 1 question for 5 years." | "Not a joke about voters. You are the sane one in this picture." | S. (Source: research 21, framing from 21.)
5. **Title card: "FUTURE PROOF" on a building-site hoarding** | "Probably wrong. Posted on purpose." | "Here are three ideas from software. They might be wrong. Post a better answer and ten thousand experts will turn up to correct me. That's the plan." | S. (Uses canon's "wrong answer on the internet" line.)

### Pillar 1: Composition over inheritance (6-14)
6. **Own: till receipt, 40 items, can't remove any** | "You can't take the pickles off." | "You get the whole meal deal. The sandwich you want, the crisps you don't, the drink you hate." | S.
7. **Own: fake "choose your package" screen (cable-bundle grammar, no brand)** | "Package A: Tax + Water + Schools + Border. Package B: ..." | "Two packages. Each includes things you never ordered. Invented parties, matching nobody." | S/A. (Bundles invented on purpose, from the microsite toy.)
8. **Two Buttons (own redraw): both buttons are whole bundles** | "Sweating over two sets of 200 promises." | "Both buttons are whole bundles. That's the whole trick." | S.
9. **Drake (own redraw): bundle no / one issue at a time yes** | "Package deal / Per issue" | "Spotify let you stop buying the album. Politics still sells the album." | S.
10. **THREE.JS SCENE 1: the party slab cracks into bricks** | "A party is a slab. An issue is a brick." | "Left: one solid slab you inherit whole. Right: the same stuff as bricks you pick up one at a time. Software calls it composition over inheritance. Nobody asked for 'inheritance'; you also inherited the debt." | 3D (<15s).
11. **Ostrogorski in one slide: bars flip when voted per issue** | "A party can win with policies most people don't want." | "Same voters, same views. Vote in a bundle and A wins. Vote issue by issue and B wins." | 3D or A. (Arxiv 2307.11873 secondary; needs worked example and UK case, CHECK.)
12. **Switzerland: ballot with several boxes** | "Swiss voters have been asked 332 times since 1848." | "In Switzerland they vote on one question at a time, about ten federal votes a year. It's not sci-fi, it's Sunday." | S. (332: admin.ch via search, CHECK; quote 332 only, other counts conflict. Reader trap: result can go either way, keep it on process.)
13. **Expectation vs reality: "just referendums?"** | "No. Not referendums." | "Pre-empt: asking more often is not the same as a binding secret ballot. We start with advisory, low stakes, paper kept for the big vote." | S. (Answers canon flag "so, referendums?" and the internet-voting objection, research 21.)
14. **Awe slide: thousands of small ideas -> one policy** | "Taiwan: thousands of people, one agreed rule." | "vTaiwan used Pol.is: four camps collapsed to two and the government agreed to ratify the consensus points. Say 'thousands' until we have the primary." | A. (secondary, CHECK counts; pair every grumble with an awe slide.)

### Pillar 2: Continuous integration (15-23)
15. **Own: phone update popup vs government update popup** | "Update available: Government v1832.1.9. Remind me in 5 years." | "Your phone patches itself every week. Parliament waits five years, then ships everything at once." | S.
16. **CD-ROM government (own)** | "Shipped on disc, no tests" | "The whole thing arrives in one box every five years, and nobody checks the box." | S.
17. **THREE.JS SCENE 2: brick tower, each brick turns green on test vs a monolith dropped by crane** | "The green tick" | "Left: bricks lit green one by one, and a revert arm if one fails. Right: five years of building, dropped in one go. The point isn't speed, it's that tests make fast change safe." | 3D.
18. **"Works on my machine" (own)** | "Works on my machine." | "A policy that worked in a briefing paper, in a room." | S.
19. **Receipts: nobody keeps the count** | "Post-legislative review: due 3-5 years after the Act. Central record: none." | "A Lords written answer says there's no central record of how many reviews are done. I'm not saying none. I'm saying nobody keeps count." | S. (Hansard mirror, secondary; do NOT assert a count of unreviewed Acts.)
20. **Sandbox gag: staging exists for fintech start-ups, not benefits** | "Fintech gets a sandbox. Benefits get production." | "The FCA runs a regulatory sandbox for new financial products. Applies to a start-up. Not to a benefit." | S. (FCA claim of world first unverified.)
21. **Poll tax timeline with a red git revert button** | "Tested in Scotland a year early. No stop condition." | "Scotland, 1989. Abolished 1991. Council Tax 1993. A test in production with no stop condition." | A. (Wikipedia only, CHECK primary. Aim at the decision-makers who set no stop rule.)
22. **Water: "shipped, never ran a test"** | "Sewage: a top priority for voters across parties." | "This is the one thing voters on all sides keep saying." | S. (Snippet-level polling, no hard numbers on the slide; New Statesman secondary.)
23. **Fix slide, played straight: "Undo button"** | "Change small. Check. Keep an undo." | "Not move fast and break things. Move small, check, and be able to undo it." | S. (Trap guard: do not read as break-things.)

### Pillar 3: Data-driven decisions (24-30)
24. **Drake (own): pill trials vs policy trials** | "Pills: tested. Policies: ... also tested, sometimes." | "We test a pill on 500 people before it hits your bathroom shelf. A law goes straight to 60 million." | S. (Test, Learn, Adapt, Cabinet Office/BIT 2012, primary: gov.uk.)
25. **Own: 11 versions of one letter** | "One sentence changed. 67.5% -> 79.0% paid." | "HMRC changed one line in a letter and measured it. That is the whole method." | S. (Secondary; sample sizes CHECK. The £160m figure is estimate.)
26. **Scared Straight (own)** | "Common sense is a hypothesis, not a result." | "A review of nine trials found it made reoffending worse. Everybody was sure it'd work." | S. (Campbell review primary abstract.)
27. **"99% turned around" vs independent evaluation** | "Counted success vs measured success." | "The government counted ~99% of 120,000 families 'turned around'. The independent evaluation found no consistent impact. Different numbers measuring different things." | S. (NIESR 2016; not a lie framing.)
28. **THREE.JS SCENE 3: two identical towns, one trial town, a lever locked until a result grows** | "No proposal without its experiment." | "Two towns. One gets the policy first. The lever only unlocks when the number says go." | 3D.
29. **Nutrition label: "How we'll know"** | "What we're testing / who gets it first / what number means stop" | "Every policy gets a label. If it can't fill the label, it isn't ready." | S. (Reusable template slide.)
30. **Billionaire Coin as a model small idea (optional)** | "Cap hoarding at $1bn, the rest builds hospitals." | "A small idea, with its test written on the label." | S. (Canon idea; do not state coin trust claims, per CLAUDE.md.)

### The small-ideas bridge (31-33)
31. **Expanding Brain (own)** | "Panel picks 50 / vote per idea / run it as an experiment / standing pipeline" | "Martin Lewis, with Nesta and Involve, is asking for small ideas. Great start. The instinct is mainstream. The vote is the next step." | S. (All secondary; site opened by nobody, VERIFY who runs it, submission, deadline 12 Nov 2026 first. Not an endorsement of us. No Lewis face/logos/colours.)
32. **Network of ideas: dots clustering into 'views' (Pol.is style)** | "Maps of agreement, not a winner." | "Imagine every idea sorted into the views people actually hold, and the best of each shown. No algorithmic winner." | 3D (optional, ties to Political Social Network seed).
33. **Who is obliged to answer?** | "An idea with no wire to a decision is a suggestion box." | "Petitions get a response at 10,000. The reply can still be 'no'. The wire to policy is what's missing." | S. (petition.parliament.uk primary.)

### Close + call to action (34-36)
34. **Daylight construction site, empty plot labelled "Yours"** | "The good branch isn't written." | "The bad branch is finished; I wrote its postmortem. The good one is blank. That's the point." | S. (From canon + microsite empty plot.)
35. **"You are not gambling by changing the system. You are gambling by keeping it."** | text only | "That one's from the canon. It's a straight line. I mean it." | S.
36. **CTA: "Post a wrong answer"** | "Write one rule. Test it with someone it affects." | "Pick one thing you'd change. Write the rule. Say how we'd know. Submit it, here or at the small ideas site if it's still open. Ten thousand experts will correct you. Good." | S.

Notes: 36 slides at 6-12s each is about 5-6 minutes; punchline slides 2-4s, diagrams 15-25s. For the ~2-minute talk cut take slides 2,4,6,10,15,17,24,28,31,36. Slides 3,6,9,15,18,24,26 double as 9:16 shorts. A 7-10 slide vertical carousel comes from master layouts.

## 3. Top 5 three.js visual metaphors (ranked)

1. **Party slab cracks into bricks** (pillar 1; clear in 10s, one variable, doubles as logo-grade explainer). Slide 10.
2. **Test-gate conveyor / green-tick brick tower with revert arm vs one crane-dropped monolith** (pillar 2). Slide 17.
3. **Two identical towns, one trial, a locked "enact" lever** (pillar 3). Slide 28.
4. **Ostrogorski flip: same voters, bars reorder when voting goes issue by issue** (pillar 1 proof; also best for the "wait, what?" reaction). Slide 11.
5. **Network of ideas: dots drifting into view clusters; the best of each lights up** (the small-ideas bridge; "composition at scale"). Slide 32.

Runners-up: Colorado quadratic-voting tokens (100 each, 107 bills, nobody went all-in; non-binding pilot), set menu vs choose-your-own plates, plank bridge vs crane.

Build rules: at most ~4 three.js slides, each under 15s; one shared canvas swaps scenes by slide index; drive animation from a deck-owned clock; static fallback image for cheap phones.

## 4. Tech stack and repo placement

- **Stack:** custom React deck on what `apps/web` already has: React 18, Vite 5.4, three 0.169, @react-three/fiber 8.17, drei 9.114, gsap 3.12. Do NOT upgrade to React 19 (R3F v9 needs React 19 + drei 10; do not mix). Skip Slidev (Vue) and reveal.js (a second framework; v6.0.1 per secondary).
- **Slides as data:** `slides.ts` / `deck.json` (id, kind, image, caption, spoken, steps, source, grade, imageSource). Keyboard keys, hash `#/7`, per-slide steps (~150 lines). Presenter mode = second window via BroadcastChannel. A teleprompter view reads the `spoken` field.
- **Aspect:** `?aspect=9x16` for 1080x1920 shorts; caption text stays live HTML.
- **Recording:** lane 1 = OBS real-time with Kai pressing keys. Lane 2 = Playwright script sets deck time per frame, screenshots, pipes to ffmpeg (libx264 crf 18). Avoid Playwright `recordVideo` (real-time, VP8, ~1 Mbps).
- **Repo:** content in `docs/stories/gitpush-origin-master/future-proof-deck/` (spine.json, deck.json, look.md, picks, feedback/), generic renderer as `packages/deck` (names no story, like the chain toolkit), route in `apps/web` (or the TV homepage's government channel, a ruling for Kai) with the doorway link `/future-proof`. Prototype can first be an artifact in vanilla JS + three.js from cdnjs at a pinned version, keeping the data format portable.
- **Fit with existing site:** daylight-means-Future-Proof is settled (Kai 2026-10-17); everything else about the look is open. The 2026-10-17 microsite prototype's toys (bundle table, update slider, test gate) become slides 7, 15/17, 29.

## 5. The `meme-deck` skill design

Group: "Words, ideas, look", beside `new-story` and `variations`. Reuses rather than rebuilds.

| Stage | What | Reuses |
| --- | --- | --- |
| 0 Look | Find the deck's own look (not a default) | `story-style`, read `look.md` before any image |
| 1 Brief | Interview: canon doc, reader, hook, who fronts it, length | `scene-beats` pattern; `the-reader.md` |
| 2 Spine | `spine.json`: argument, running metaphor ("politics as a codebase"), per-idea beat sheet (pain, meme, mechanism, fix, punchline), callback ledger, claims with source + grade | `story-craft`; research-grade table |
| 3 Options | About 10 meme-shape writers, each pushing one shape (Drake, Two Buttons, receipt, fake UI, dispatch, label...), sameness gate | `variations`, `scripts/variations/fresh.py`, `scene-dialogue` writer/synthesis pattern |
| 4 Picking page | Artifact, tab per section, 3 versions per slide, pick button + note on every line | `build-dialogue.py` + template, `dialogue-workflow.js` |
| 5 Art | Stills in meme grammar from our own images; three.js only where motion explains a mechanism | `new-image`, `flow-prompt`, `find-footage` |
| 6 Build | one `deck.json` -> web page, teleprompter view, talk-cut track, 9:16 carousel | new renderer; `scene-timeline` for the talk cut |
| 7 Rounds + release | Notes dumped to `feedback/r<N>/` first, answered on the page, republished to the same URL; decisions in `prov.py trail`; hand to `chief-of-staff` for shorts, captions, board | provenance rules, `chief-of-staff` |

Gates baked into the skill: (a) Lee/Coe test on every slide (a viewer who believes the opposite sees only this slide: whose contempt does it confirm? If the scapegoat's or the smug side's, rebuild); (b) every claim has URL + grade before it can leave draft; (c) image-source column (original / public domain URL / cleared URL / template) and a recipe card per image; (d) cold-read test on 3 viewers, cut any slide that earns no laugh or nod; (e) same-prompt check on every generated image.

New code needed: deck spine schema, deck picks template, renderer, teleprompter view. Already exists: everything else.

## 6. Risks and open questions

**Legal** (not legal advice; research 19)
- UK s30A CDPA fair dealing (caricature, parody, pastiche) is undefined and narrow; Shazam v Only Fools [2022] rejected the defence. A meme must add its own comment.
- Green: self-made originals in meme grammar, public-domain art (pre-1900 engravings fit the electricity gag), cleared footage, text/diagrams/three.js. Amber: famous-photo templates (re-create the pose with our own image), film clips (a few seconds, commenting on the clip, source on screen, never in a thumbnail). Red: watermarked stock, film/TV/pop music, real-org branding, fake quotes.
- No impersonation: no Lewis face, logos, colours, the "Small Ideas" title as ours; no implied endorsement. UK status of AI-generated outputs (s9(3) CDPA) is under review: check before claiming ownership.
- Moving clips/audio carry Content ID risk; remove-or-swap on a claim.

**Reader traps** (research 04, 20)
- Memes default to smug: butt of every joke is the mechanism or the decision-maker, never the voter. No wojaks/NPC/soyjak, no cosplaying the demographic, no "duped/wake up".
- Avoid proposing PR (Reform voters' support fell from 67% to 45% in YouGov data, snippet-level); lead with unbundling.
- The "system is ancient" hook can read as cynicism about democracy and feed the wrong drift: every slide names a decision-maker and ends on a fix.
- Referendum objection and internet-voting security are pre-empted (slide 13); AI is a summariser of disagreement, never a decider, with an auditor named.
- Keep "competence-qualified participation" off the deck.
- Pair "the data says" with a person's consequence.

**Accuracy** (CHECK before any slide goes out)
- Drop "100,000+ deploys a day" (unsourced). Sourced alternative: "every 11.6 seconds" (2011, Jon Jenkins, secondary, internal services included) or "every few seconds".
- Estonia (51% online in 2023, Wikipedia), vTaiwan counts (3,000 / 4,000 / 1,875 conflict), Habermas Machine figures, Finland / Stockton numbers, HMRC sample sizes, Switzerland 332, Paris 5% budget: re-source.
- Poll tax from Wikipedia only. Universal Credit: say badly piloted, not unpiloted.
- Small Ideas: nothing verified from the live site; the deadline year (assumed 2026) and the panel names (one outlet) are unconfirmed. The deadline of 12 Nov is a week away: a topical slide only works if it ships now and after verification.
- Bell 1876, 1918/1969 franchise dates and Old Sarum: general knowledge only.
- Do not assert Estonia's security or the Colorado pilot as evidence of safety or effect.

**Open questions for Kai and Jack**
1. Front door: GPOM's doorway question ("who should decide how the gains from automation are shared?") vs Kai's "vote on more than one thing". Which opens the deck, and how do they bridge?
2. Who fronts it: Kai to camera, or the narrator for sarcasm with Kai playing the re-aim straight?
3. Does a topical slide go out before 12 Nov (hook fades) or does the whole deck wait until after Camping part 1 (chief-of-staff plan defers Future Proof)?
4. Where does it live: gitpushoriginmaster.com, the TV homepage's government channel, or its own page? Jack dislikes teletext, so no teletext default.
5. Look: Jack to run `story-style`; the "daylight" rule is settled, the blueprint palette was only a proposal.
6. Do the Billionaire Coin and Political Social Network ideas go in as fleet items, or stay out?
7. Is a small-ideas.org bridge slide welcome at all given no verified relationship? Needs Kai to open the site and the Nesta/Involve pages.
8. Who speaks for the people the new scoreboard leaves out (canon R9)? Open thread on the deck's closing slide.
9. Budget: image generation is free; accept a cold-read test with 3 outsiders before the full build?
