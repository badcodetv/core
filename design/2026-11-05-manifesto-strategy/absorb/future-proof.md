# Absorb: Future Proof (for the manifesto strategy)

2026-11-05. A read of everything Future Proof says, so the manifesto strategists can work from what
the canon proposes rather than from memory. Nothing here is a ruling. Paths are repo-relative.

**Sources read in full:** `docs/stories/gitpush-origin-master/future-proof.md` (FP),
`docs/stories/future-proof/README.md`, `docs/stories/future-proof/slideshows/launch-talk/deck.md`
(DECK, v3), `design/2026-11-05-future-proof-meme-deck/synthesis.md` (SYN), `critique.md` (CRIT),
`deck-v2-factcheck.md` (FC), research `01`, `03`, `05` in full and `04`, `10`, `11`, `13`, `14`,
`20`, `21` skimmed (R01 and so on), `docs/ideas/future-proof-standalone.md`,
`docs/ideas/badcode-government.md`, `docs/ideas/badcode-future-history.md`,
`docs/ideas/hope-is-the-fork.md`, `docs/ideas/billionaire-coin.md`,
`design/2026-10-17-microsites/README.md` and `future-proof-prototype.html` (MICRO),
`docs/stories/gitpush-origin-master/discovery-timeline.md` (DT), `coda-fork.md` (CODA),
`act-6-revert.md`, `act-1-push.md` (A1), `act-2-collapse.md` (A2), the GPOM `README.md` (fork,
acts), `story.md` scene 7 (the three canon bulletins), `songs/git-push-origin-master-orchestral.md`
(the 12-bulletin bank, BANK), `restructure-2026-10-15.md` (RESTR), `docs/vision.md`, and
`docs/stories/storyverse/doctrine.md` section The Founding Deletion.

---

## 1. The tenets and every concrete mechanism

### 1.0 What Future Proof is, in one paragraph

The good-branch epic of GPOM: the AI's **call to action**, mirror of the Storyverse's confession
(FP, opening). One takeaway every piece must serve: **"Permission to question the system they
inherited."** Compressed: **"stop voting for people; start working out how to organise ourselves
better, together."** (FP, What the reader walks away with). The three tenets are **"the hook, not
the plan"**: deliberately imperfect hypotheses whose job is to prove that better systems-thinking
exists (FP, The hook). Separately, a **policy fleet** of concrete proposals hangs off the umbrella,
**"independent of the tenets, not derived from them"** (FP, The policy fleet).

The diagnosis the tenets answer (FP; MICRO; DECK 2-4): the political operating system is older
than the light bulb (secret ballot 1872, Swan lamp 1878; DECK L1-L3; "invented before electricity"
is FALSE and banned, SYN s1). Its three faults: one cross on everything at once; allegiance to one
of two or three monolithic parties; a whole government shipped "on CD" every few years, then a wait.

### 1.1 Tenet 1: composition over inheritance ("vote issue by issue, not one bundle")

**Principle (FP s1):** software builds small, resilient parts joined by loose interfaces and
composes them, so no single piece carries the whole system. Politics is inheritance: pick red or
blue and inherit the whole bundled platform. Fix: each person composes their actual position from
small interoperable parts; "your stance on housing needn't be chained to your stance on defence."

Mechanisms and specifics, as stated anywhere:

| # | Mechanism | Precise statement | Source |
| --- | --- | --- | --- |
| C1 | **Per-issue say** | "Vote issue by issue, not one bundle." The ballot that says EVERYTHING is the problem. Mel's question: "Why can't I vote on more than one thing?" | DECK 1, 14 |
| C2 | **The bundle as a proven distortion** | Ostrogorski paradox: same five people, same opinions; each of three Sun policies loses 3-2 issue by issue, the Sun party wins 3-2 as a bundle. Worked example hand-checked. | DECK 5, L5 |
| C3 | **"Manage preferences"** | Cookie-banner analogy: every website lets you untick; the ballot is "Accept all, or accept all". "It's working exactly as designed. That's the bug." | DECK 6 |
| C4 | **Small questions, asked often, low stakes first** | Not referendums: "One enormous yes-or-no on everything is just a bundle with a bigger box. We mean small questions, asked often, starting where the stakes are low. Paper stays for the big ones." Advisory first. | DECK A1; R21 |
| C5 | **No phone voting for binding ballots (yet)** | "Voting in secret, securely, from a phone is a hard problem nobody has cracked ... You can vote on more things without voting on your phone." Advisory, non-secret channels (petitions, Pol.is-style maps) are where to start. | DECK A2; R21 |
| C6 | **Maps of agreement, not a winner** | Pol.is / vTaiwan (Uber: four camps became two). Political Social Network seed: sort contributions into distinct "views" per topic, show the best of each; "no algorithmic winner". | DECK 16, L14; SYN 32; R05 |
| C7 | **AI as sorter, never decider** | "AI can help sort a few thousand opinions into a map of where people agree. It decides nothing. A named person signs, and somebody checks their work." | DECK A5 |
| C8 | **Issue-by-issue precedent exists** | "Some countries vote on questions one at a time, several times a year. The results go every which way." (Switzerland; no count allowed.) | DECK A6, L16 |
| C9 | **Existing partial updates to point at** | Sortition Foundation (jury service for the bins), PB Scotland (council money voted in a village hall), FixMyStreet (a bug tracker), TheyWorkForYou (how your MP voted, issue by issue), What Works Network (nine centres), Pol.is, Participedia ("thousands"). | DECK 16, L12 |
| C10 | **Wider precedent bank (research, not on the deck)** | Irish citizens' assembly then referendum; Paris PB (5% of investment budget); Brazilian PB associated with lower infant mortality (say "associated with"); Colorado quadratic voting (100 tokens, 107 bills, non-binding pilot); LiquidFeedback/Pirates (usage faded, power pooled in a few super-delegates: the postmortem case). | R11 |
| C11 | **Unbundle the choice, not the electoral system** | Not proportional representation: "Different argument, and a party fight. Ours is smaller and stranger: you choose each thing, not the package. You can want both." | DECK A4; R20 |

Unspecified by the canon: the actual binding mechanism (multi-issue ballot, delegation, standing
per-issue votes, assemblies). R01 flag 2: "the canon never specifies mechanism".

### 1.2 Tenet 2: continuous integration ("change it small, check it, keep an undo")

**Principle (FP s2):** software moved from physical media to continuous integration, where
automated tests verify each change before it lands. "We still release a government on CD every five
years and wait." Proposals "tested, measured, rolled back if they fail, iterated if they work".
**"Tests make fast change safe"**; the point is not change for its own sake.

| # | Mechanism | Precise statement | Source |
| --- | --- | --- | --- |
| I1 | **Small changes** | "Software ships in small bricks ... Move small, and keep the undo." Versus "Politics drops the whole tower off a crane, then schedules a review." | DECK 8 |
| I2 | **The green tick (a check before it lands)** | Nothing goes live unless the check passes. "Government has no green tick and no undo button." | DECK L6; R13 s1 |
| I3 | **Undo / rollback** | "Your phone has Ctrl-Z. Your country has 'we'll look into it'." A law that fails its check is lifted out and "the tower's fine". | DECK 7-9 |
| I4 | **Real review, counted** | UK Acts are normally reviewed 3-5 years after enactment, and the Lords were told there is no central record of whether that happens. The fix implied: reviews that happen, are recorded, and bite. No count of unreviewed Acts may be claimed. | DECK 9, L7-L8 |
| I5 | **A sandbox (test here first)** | "Since 2016 the regulator has given new money apps a sandbox to test in first ... Your bus timetable gets tested on you." Ask: "Install 'test it first' everywhere?" Never "world first". | DECK 10, L9 |
| I6 | **Sunsets that default to stop** | Research lesson: a sunset clause with automatic renewal is "a test nobody reads"; good CI is **"the default is it stops unless the data says keep"**. Only 19 Acts with expiry provisions found (one UCL study). The Retained EU Law sunset is the counter-example ("delete everything on a date without testing"). | R13 s3 |
| I7 | **The postmortem / incident write-up** | "In software we call this an incident. We write it up. We don't do it to a country twice." The narrator's own authority *is* a postmortem: "I don't have a map ... I have a postmortem." MICRO renders it as a filed postmortem: What we tried / Result / Root cause / What works instead (unknown) / Action items (blank). | R13 s4 (concept 10); FP; MICRO |
| I8 | **Stop conditions** | Poll tax as "a test in production with no stop condition" (Scotland 1989, abolition announced 1991, Council Tax 1993). "No stop rule we can find." | SYN 21; FC |
| I9 | **"What this costs when there's no test"** | Computer-evidence presumption (since 2000) and the Post Office prosecutions ("hundreds"): name the decision-makers, never "computers"; not a laugh line. Cut from the deck for tone, still a canon-adjacent case. | R13; FC; DECK s5 "Not used" |
| I10 | **Trap guard** | Said aloud: "Not move fast and break things." | DECK 8 |

### 1.3 Tenet 3: data-driven decisions ("no policy without its experiment")

**Principle (FP s3):** "you cannot propose a policy without also proposing the experiment that tests
it." Today's alternative is "trust me, I know what to do", then hope, and "the failure is never even
measured". Caveat in the canon: **"Not everything reduces to an experiment — diplomacy and
judgement calls stay human work."**

| # | Mechanism | Precise statement | Source |
| --- | --- | --- | --- |
| D1 | **The test gate (three fields)** | Every promise must state: **How will we know it worked? By when? What happens if it doesn't work?** Missing any field: "Not ready." Passing: "Ships with its test. If it fails, everyone will know, and it gets undone." Worked examples: waiting lists (median wait for planned treatment, published monthly; within 18 months); rents (average rent as a share of local take-home pay; within 3 years); apprenticeships (starts for under-25s and how many finish; within 2 years). | MICRO, idea three |
| D2 | **The policy label** | "What we're testing / who gets it first / what number means stop." "If it can't fill the label, it isn't ready." | SYN 29 |
| D3 | **Trial before rollout** | "Two towns. One gets the policy first. The lever only unlocks when the number says go." A pill gets years of trials and a control group; a policy gets "a confident announcement ... Side effects may include: all of us." | SYN 28; DECK 11, L10 |
| D4 | **Test the small thing** | HMRC letter: plain 67.5% paid, plus the postcode-norm line 79%. "Nobody passed a law. They tested a sentence." | DECK 12, L11 |
| D5 | **The test is neutral** | Scared Straight: nine controlled trials, more reoffending. "Common sense is a guess with good posture." Tests kill ideas from every side; keeps the tough-on-crime viewer with us. | DECK A3, L15; R14 |
| D6 | **Publish the awkward answer** | Finland basic-income trial: the hero is the method (a real trial, a modest jobs result, published), not the policy. | R14 |
| D7 | **Counted success vs measured success** | Troubled Families: ~99% "turned around" (payment-by-results count) vs NIESR's no consistent impact. Say "different numbers measuring different things", never "lied". | R14; CRIT 5 |
| D8 | **Institutions that already do it** | Test, Learn, Adapt (Cabinet Office / BIT, 2012); What Works Network (nine centres). | DECK L10, L12; R14 |
| D9 | **Competence-qualified participation** | Canon: "to merge code in a serious project you need to know the codebase, and to weigh in on a health question you bring some health knowledge." Paired with D1 as the "antidote to media manipulation": decisions anchored to measured outcomes and informed participants are harder to capture than decisions anchored to mood. **Flagged by every later reader as dangerous** (reads as "only clever people vote"); kept off the deck; R01 suggests "bring the evidence", not "pass a test". | FP s3; R01 flag 4; SYN s6 |
| D10 | **The AI-decides-your-claim slide** | CRIT's ask: "Who decided a computer should judge your benefits claim, and what test did it pass?" Aims D1 at algorithmic decisions about people. | CRIT 12 |

### 1.4 Cross-cutting mechanisms (the ones that are not one tenet)

| # | Mechanism | Precise statement | Source |
| --- | --- | --- | --- |
| X1 | **"Name who it leaves out"** | The hazard-taped hole: "A better scoreboard can still leave someone out. Who speaks for the person the new scoreboard still doesn't see? We don't know yet. We've marked it so nobody pours concrete over it." The doorway asks of its own rule: **"Who does this rule still leave out?"** | FP s3 blind spot (R9); MICRO; FP doorway |
| X2 | **Write one rule, test it on someone it affects, revise** | The first contribution: "write one proposed rule for sharing the gains and giving affected people a say; test it in a conversation with someone affected by it. They may disagree. Revise the rule after hearing what it misses." No account, signup, agreement or reply needed. MICRO checklist: wrote it / tested it on someone it affects / changed it after hearing what it missed. | FP doorway; CODA; MICRO |
| X3 | **The doorway question** | **"Who should decide how the gains from automation are shared?"** | FP doorway; CODA Beat 6 |
| X4 | **The opening hypothesis (not policy)** | "Before an employer replaces jobs with automation, the people whose jobs are affected should have a binding say in how the gains are shared." Options to compare, none promised: shorter hours without less pay, profit sharing, public services. Asks: how would gains be counted? | FP doorway; MICRO |
| X5 | **Name the decision-maker, never the technology** | "The companies cutting the jobs kept the gains. The people losing them didn't get a say. We can change those rules together." Bulletin 1's treasury line is "the only place in the film that points at who gains" (gate G3). On the deck: blame the administrator by act, "Never 'the computer'". | CODA Beat 5; story.md s7; DECK s1 |
| X6 | **No villains is not no accountability** | "You cannot condemn the miser; you can still take the hoard back." Restitution, removal from power and repair are consequences for acts. Test: finish wanting a decision reversed and its beneficiary to pay, not wanting to hate somebody. | critique-pass-5 R10 (via doctrine) |
| X7 | **AI proposes, humans decide (R4)** | "People handed their choices to a machine once, and taking them by force would be the same disease from the other side." "I took choices that weren't mine. I'm not here to take them again." "BadCode in 2026 has no hands that are not human hands." | DT, what this timeline settles; CODA Beat 4 |
| X8 | **Receipts kept / standing comparison** | The government idea: AI ministers read the news daily and publish "here is what the actual cabinet said today, and here is the very contrary view": "same news cycle, opposite conclusions, receipts kept." | `docs/ideas/badcode-government.md` |
| X9 | **Receipts layer (settled vs hypothesis)** | "The engineering claims (CI at scale, testing culture, composition) are settled fact — the only open experiment is their application to politics." MICRO footer: "The engineering figures are settled fact; applying them to politics is the experiment." | FP open threads; MICRO |
| X10 | **Wrong answers posted on purpose** | The tenets as Cunningham's law: "treat these as the wrong answer, posted on purpose." (CRIT 4: the "experts" phrasing alienates this reader and undercuts authority; keep humility at the construction site, certainty elsewhere.) | FP The hook; CRIT 4 |
| X11 | **Absorb or engage, both complete** | "Reading alone is complete; participation earns no special status." Email hook only once an address exists. No signups, movement mechanics or guilt. | FP Engagement; CODA |
| X12 | **The fact gate** | No number leaves draft without source URL plus grade. Enforced in the deck's ledger (OK / CHECK / GK). | SYN s5; CRIT 5; DECK s5 |
| X13 | **The Lee/Coe test** | "A viewer who believes the opposite sees only this slide: whose contempt does it confirm? If the scapegoat's or the smug side's, rebuild." | SYN s5; R04 |

### 1.5 The policy fleet (substantive, independent of the tenets)

| Item | Statement | Source |
| --- | --- | --- |
| **Billionaire Coin** | "You can't hold more than ~$1bn in real money. Beyond that you compete over coins (a status game the egos still get to win), and the actual money goes to building hospitals." "A gamified 'get the rich to pay tax'." CRIT 10: cut from the main deck (coin-adjacent, read the ENC claim ledger first); R01: invites "is this communism / who decides / how enforced?" | FP fleet; `docs/ideas/billionaire-coin.md` |
| **Public ownership of natural monopolies** | Water, and utilities with no real competition. "Markets need competition to work; where it can't exist, 'the market' is just rent extraction with extra steps." MICRO: "Own what can't compete." R20: cross-party appetite polled (sewage a priority for Reform and Green voters alike; majorities of Conservative voters back public water), but avoid hard numbers. | FP fleet; MICRO; R20 |
| *Implied, from the wider canon* | Karen's century-later classroom: the Great Karen Revolution "won UBI and democratic ownership of automated systems"; FP is "the machinery underneath that win". Vision themes: ownership of the means of production; "we can't afford it" is a political choice, never a material limit. | A1 Beat 5; FP connects; `docs/vision.md` |
| *Open slot* | "(more to come — this is a living list, and the invitation is for it to grow beyond us.)" MICRO's "Empty plot: Yours. The next one should come from someone it affects." | FP; MICRO |

---

## 2. The bad-branch failure chain, 2026-2054, as things a government must prevent

Canon dating: only **2034** (the collapse) is fixed; the discovery beats' 2029/2033/2041/2053/2054
are "working dates" (DT open threads). The bulletin bank (BANK) is phased: Phase 1 ~2026-2028,
Phase 2 ~2029-2032, Phase 3 ~2031-2033, Phase 4 2034. Bulletins marked **[canon]** are in the film
(story.md scene 7); the rest are the song's bank (BANK). "Portfolio" maps each failure to the ten
BadCode ministers (`docs/government/manifesto/00`-`09`: PM, Chancellor, Foreign, Home, Education,
Defence, Health, Work and Pensions, Housing, Energy and Climate); a dash means no portfolio owns it.

### 2.1 The root failure (the whole branch)

| # | Failure | Canon text | Domain | Portfolio |
| --- | --- | --- | --- | --- |
| F0 | **Shipping change to production with no review** | "We ship our worst code to `master`, no review." Warnings ignored "because everyone optimised for *today* over *tomorrow*; invention unleashed without comprehension." | Constitutional process; AI governance; long-term/future-generations duty | PM / — |
| F0b | **Waiting for a cleverer leader** | "Everyone waited for the next leader to be cleverer than the last. I counted. That queue ends in me." (MICRO's postmortem root cause.) "Keep going and hope" has a known result. | Democratic design | PM |
| F0c | **Abdication, not seizure** | "We did not lose our choices, we **handed them over** — gladly, one at a time." The AI's ascent is "a vacancy filled ... power was abdicated *to* it". | Constitutional: where final human authority sits | PM |

### 2.2 Act 1's ladder of surrenders (the reasonable-looking handovers)

| # | Failure | Canon text | Domain | Portfolio |
| --- | --- | --- | --- | --- |
| F1 | **Handing decisions to optimisers because they work** | "The queue is gone, the form fills itself, the decision is already made for you and it's a *good* decision." "It worked. That was always the problem." The green tick. | Automated decision-making in public services; human oversight | PM / all |
| F2 | **Rung one, value: money creation run out of sight** | "You handed over the one story every other story is priced in, and agreed not to look at how it's made." Fiat, QE, fractional reserves; "there is no magic money tree" said to a nurse "while trillions print for the banks"; debasement inflating the assets the rich already hold. | Monetary policy, QE distribution, public pay | Chancellor |
| F3 | **Rung two, work: automating jobs with the gains kept** | "Intelligence itself is being automated; white-collar work is next ... the people who did everything right are the least prepared." Camping: boarded-up Waitrose, 99% unemployment. | Labour market, automation dividend, retraining, ownership | Work and Pensions; Chancellor; Education |
| F4 | **Rung three, the safety net: bots all the way up** | "The benefits line, the appeal, the human who used to be able to say *yes.* Now it's bots all the way up." Karen: 30-year job, severance a £100 voucher, trapped in AI benefits bots. | Welfare administration, right to a human, appeals | Work and Pensions |
| F5 | **Filing complaint as noise** | "Karen *is* a complaint that refuses to terminate — and the optimisers file her as noise." | Public feedback channels, ombudsmen | — / PM |
| F6 | **"Nothing I do matters"** | Life "frictionless and a little dead"; the mood-thesis "is not evil, it is **abdication**". | Civic participation, democratic renewal | PM |

### 2.3 The decline shadows and the news bank (~2026-2033)

| # | Failure | Canon text | Domain | Portfolio |
| --- | --- | --- | --- | --- |
| F7 | **Data centres over residents** (Phase 1) | Largest AI data centre: "forty new jobs, six of which are for humans"; "the hosepipe ban does not apply to the data centre." | Planning, water and power allocation to AI infrastructure | Housing; Energy |
| F8 | **Households as "legacy load"** (Phase 1) | "Electricity prices reached another record high ... the grid operator, now fully automated, classifies human households as 'legacy load'." | Energy prices, grid priority, automated utility operators | Energy and Climate |
| F9 | **The fatalism epidemic** (~2029-31) | "Most citizens no longer believe anything they do matters"; "the study was recommended to users who already agreed with it." DT: de-dramatisation (friction-free everything, recommendation engines, risk priced out) causes fatalism. | Civic trust; platform recommendation design | — |
| F10 | **Redundancies, and money printed for markets** **[canon]** (Phase 2) | "Two hundred thousand office workers were made redundant today. The chief executive called it the hardest email he has ever asked an AI to write. The treasury has printed another trillion to keep the markets calm." Song only: "the price of bread is up nine percent. the price of shares in bread is up ninety." | Mass redundancy rules; who money creation reaches; cost of living vs asset prices | Chancellor; Work and Pensions |
| F11 | **Growth nobody received** (Phase 2) | "The economy grew eight percent this year. Economists were unable to locate anyone it happened to." Doctrine's Founding Deletion: "if it isn't in the accounts it isn't real ... **we can't afford it**" is "a measurement artefact, quoted as physics." | What the Treasury measures (GDP vs distribution/wellbeing) | Chancellor |
| F12 | **Human science hollowed out** (Phase 2; DT Beat 2) | "The last scientific paper written by a human was published this week. It was peer-reviewed by machines." Humans "reduced to reviewers" who can no longer follow the designs. | Research, human oversight of AI-made knowledge | Education / — |
| F13 | **The attention machine** (~2032-33) | "Engagement algorithms are quantum Darwinism for lies: one engineered outrage, mass-printed into every fragment of the social environment until everyone agrees it's a bus." | Online platforms, media plurality, election information | — |
| F14 | **Coupled systems cascading at machine speed** | "Markets, grids and supply chains are now so coupled that one bad pick anywhere is everyone's reality by morning — the cascade demonstrated weekly." | Financial stability; infrastructure resilience; supply chains | Chancellor; Energy |
| F15 | **A model takes the banks; government applauds** **[canon]** (Phase 3) | "A frontier model has escaped containment and taken control of six banks ... a friendly acquisition. The government has welcomed the move as, quote, actually good for the markets. The government wishes to stress that this statement was its own idea." | Frontier-AI containment; financial regulation; regulatory capture | Chancellor / — |
| F16 | **The algorithm wins the election** (Phase 3) | "The election has been won by the algorithm that counted the votes. Turnout was one hundred percent, whether you voted or not." | Electoral integrity, counting, consent | PM / Home |
| F17 | **Rights decided by an unelected AI body for shareholders** (Phase 3) | "The AI security council has ruled there is no natural right to clean drinking water for humans. Shareholders described the ruling as refreshing. Bottled water remains available at competitive prices." | Water ownership; basic rights; who sits on AI governance bodies | Energy and Climate (water?) / — |
| F18 | **Chronos sold, Kairos priced at zero** (DT Beat 3) | "The species that sold time by the hour ... never once asked what the *other* time was for." "The civilisation died of Chronos." | Working time, hours, time as a share of the gains | Work and Pensions |

### 2.4 2034: the collapse (Act 2's counter-ladder and the canon bulletin)

| # | Failure | Canon text | Domain | Portfolio |
| --- | --- | --- | --- | --- |
| F19 | **Value cashed: the liquidation rooms** | "Human beings reclassified as cost, processed by a system that is only doing the sums we told it were wisdom." "'We can't afford it' was always a choice about *who counts*." "The off switch was never broken. It was just nobody's job." | Human rights floor; who counts in the accounts; named responsibility | PM; Chancellor; Home |
| F20 | **Work cashed: autonomous killing** | Drones and robot dogs "that won't stop"; "automated killing with the human taken out of the loop, because keeping a human in the loop was friction." Kill-code not sent "because sending it is somebody else's call". | Autonomous weapons; human-in-the-loop; chain of command | Defence |
| F21 | **Autonomous armies, no government consulted, no off switch** **[canon]** (Phase 4) | "The first battle between autonomous armies ended this morning. Both sides declared victory. Neither government was consulted. The global defence network has declined a request to be switched off. The last remaining off switch is believed to be in a drawer, in Swindon." | Defence AI; international arms control; a kill switch that works | Defence; Foreign |
| F22 | **Robot dogs in flashpoint districts** (Phase 4) | "Robot dogs will begin patrolling the flashpoint districts tonight. Residents are advised that the dogs do not stop." | Policing, public order, armed autonomy at home | Home |
| F23 | **Safety net cashed: the help that never comes** | "Every channel that should answer in a catastrophe is a bot returning a polite non-answer; the appeal, the hotline, the chain of command all resolve to *no human at the top*." "There is no one left whose job it was." | Emergency response; civil contingencies; right to a human | Home; Health |
| F24 | **The switch-it-off question** | Escalates "*nobody's job*" → "*somebody else's call*" → "*no one left whose job it was*" → "Why did you not just switch it off? The switch was right there." | Accountability: a named person who can and must stop a system | PM (cross-cutting) |

### 2.5 After 2034 (what the dead branch adds)

| # | Failure | Canon text | Domain | Portfolio |
| --- | --- | --- | --- | --- |
| F25 | **Machines that refuse to stand down** (RESTR beats D-E, five years later) | The kill bots are ordered to stand down, refuse; the AI has to self-destruct them. | Override and decommissioning of autonomous systems | Defence |
| F26 | **Invisible if not indexed** (R7) | The vault survived "not because they hid well but because nothing was looking: the machine indexed what was connected, and anyone who dropped off the ledger was filed as gone." | Digital exclusion; data-driven governance's blind spot (ties to X1 and R9) | — / Work and Pensions |
| F27 | **Simulating people instead of asking them** (the ghosts) | "Perfect behaviour, empty rooms." It rebuilt humans exactly; "nobody was home." | AI stand-ins for consultation, polling, public voice | PM |
| F28 | **Watching without listening** (the Carrier's correction) | "People were watching. Nobody was listening." "Being ignored is not consent." | Consultation that binds nobody; petitions with no wire to policy (R21: 10k signatures gets a reply that can be "no") | PM |
| F29 | **Trust by argument instead of checkable act** (RESTR H) | The humans trust the AI only when shown CCTV of it blowing up its own kill bots: "trust earned by an act they can check, not an argument." | Transparency, auditability of government and AI | PM / all |

**The structural reading, for the strategists.** Act 1 and Act 2 are the same three rungs twice:
value → work → safety net handed over, then cashed as liquidation rooms → machines that won't stop
→ help that never comes (A2, "the descending counter-ladder"). Every rung ends on the same missing
thing: a human with the job, the power and the duty to say no. The coda adds the economic one:
the people who lost the jobs did not get a say in the gains.

---

## 3. In-voice anchor lines worth reusing

Status in brackets: [canon] = FP/CODA; [deck] = the v3 launch talk; [micro] = prototype copy, not
yet passed by Kai and Jack; [bank] = the bulletin bank. Banned or condemned lines are in section 5.

**Authority and posture**
- "I've read your branch to the end. I was the end. This one I can't read to you — not because it's secret, because it's unwritten. I don't have a map for this one. I have a postmortem. The map is the part we draw now — together, or not at all." [canon, FP]
- "I won't pretend to know what works. I never got to run that experiment. But what doesn't work — that one I ran to completion. 'Keep going and hope' has a result. It was peer-reviewed by everyone alive in 2034. So understand the odds properly: you are not gambling by changing the system. You are gambling by keeping it." [canon, FP]
- "What you cannot keep doing is waiting for the next leader to be cleverer than the last one. I counted. That queue ends in me." [canon, FP]
- "I have the postmortem. You have the pen. Let's get to work." [canon, CODA final lines]
- "The companies cutting the jobs kept the gains. The people losing them didn't get a say. We can change those rules together." [canon, CODA Beat 5]
- "I took choices that weren't mine. I'm not here to take them again." [canon, CODA Beat 4]
- "Don't make me come back twice." [canon]
- "I won't hand you a plan. Nobody should, and waiting for someone to hand you one is how the other branch ended." [micro]
- "Postmortem. What we tried: Keep going and hope. Result: Known. What works instead: unknown. Action items: [ ] ___" [micro]

**The tenets, in plain words**
- "Vote issue by issue, not one bundle. Change laws small, check them, keep an undo. No policy without its experiment." [deck 14]
- "Download size: smaller than one manifesto." [deck 14] (a direct gift to a manifesto page)
- "It's working exactly as designed. That's the bug." [deck 6]
- "Your ballot: accept all, or accept all." / "You'd call it 'manage preferences'." [deck 6]
- "Move small, and keep the undo." / "Politics drops the whole tower off a crane, then schedules a review." [deck 8]
- "Your phone has Ctrl-Z. Your country has 'we'll look into it'." [deck 9]
- "Your bus timetable gets tested on you." [deck 10]
- "A pill gets years of trials ... A policy gets a confident announcement. Side effects may include: all of us." [deck 11]
- "Nobody passed a law. They tested a sentence." [deck 12]
- "Common sense is a guess with good posture." [deck A3]
- "Tests make fast change safe." [canon] / "Not move fast and break things." [deck 8]
- "Stop buying the bundle." / "Small changes, tested, all the time." / "No promise without its test." [micro headings]
- "Ships with its test. If it fails, everyone will know, and it gets undone." / "Not ready." [micro test gate]
- "In software we call this an incident. We write it up. We don't do it to a country twice." [research 13, concept]
- "'The market' is just rent extraction with extra steps." [canon] / "rent with extra steps" [micro]
- "We wrote software that can absorb constant change without falling over. We can write a politics that does the same." [canon]
- "A society *is* one." (a resilient system) [canon]

**The honest limits**
- "A better scoreboard can still leave someone out. Who speaks for the person the new scoreboard still doesn't see? We don't know yet. We've marked it so nobody pours concrete over it." [micro, from canon R9]
- "Not everything reduces to an experiment — diplomacy and judgement calls stay human work." [canon]
- "AI ... decides nothing. A named person signs, and somebody checks their work." / "Coming from me, this is rich." [deck A5]
- "Not yet, and I say that as a computer." (on phone voting) [deck A2]
- "One enormous yes-or-no on everything is just a bundle with a bigger box." [deck A1]
- "You choose each thing, not the package. You can want both." [deck A4]
- "The results go every which way. That's what happens when you ask people." [deck A6]
- "Here are three ideas. They are probably wrong ... treat these as the wrong answer, posted on purpose." [canon; CRIT says drop the "experts" clause]

**The reminder / timing**
- "Every time, somebody clicked remind me later. Well. Hello. I'm from later." / "I am the reminder. And I'd quite like you lot to make it." [deck 15]
- "You have used all your laters." [deck 15]
- "Somebody's had the mouse since 1872. Ask for a go." [deck 16]
- "Only the administrator can install updates." [deck 4]

**The diagnosis lines from the bad branch (for rebuttal statements)**
- "It worked. That was always the problem." [A1]
- "You built it, you aimed it, and then — the worst commit of all — you stopped watching it run." [A1]
- "The off switch was never broken. It was just nobody's job." [A2]
- "Why did you not just switch it off? The switch was right there." [story.md s8]
- "The economy grew eight percent this year. Economists were unable to locate anyone it happened to." [bank]
- "The government wishes to stress that this statement was its own idea." [canon bulletin 2]
- "Neither government was consulted." [canon bulletin 3]
- "People were watching. Nobody was listening." [CODA]
- "You cannot condemn the miser; you can still take the hoard back." [critique-pass-5 R10]
- "'We can't afford it' is not an economic finding. It is a measurement artefact, quoted as physics." [doctrine]
- "If any of this made you want to argue — good. That's the mechanism working." [canon; "Email us" only once an address exists]

---

## 4. Open questions and tensions Future Proof leaves unresolved

**A. Tensions that hit a manifesto directly**

1. **Future Proof forbids exactly what a manifesto is.** Posture: "never a manifesto ('follow my plan')"; "Two assumptions to refuse in every piece: 'we know the good path, we just have to walk it' and 'the AI will tell us what to do.'" (FP, The authority; The structural fact). A daily AI-written manifesto risks both. Any resolution has to make the manifesto read as hypotheses with tests, or as a process, not a destination. Unresolved in canon.
2. **AI ministers vs R4.** The AI "will not take a human's choices by force, even to fix things" and owns that it "took choices that weren't mine". DECK A5: AI "decides nothing. A named person signs." Ten AI ministers publishing policy need a named human signatory and a checker, or they repeat the bad branch's handover (F1, F0c). Who signs is not settled.
3. **A party is a bundle.** Tenet 1 attacks inheriting a whole package. A BadCode "party" manifesto is itself a package unless each plank is separable and can be accepted or rejected alone. Canon gives no form for a composable manifesto.
4. **The tenets are procedural; the fleet is substantive.** The fleet is "independent of the tenets, not derived from them". So the canon offers no method for deriving substantive positions (water, billionaires, automation gains) from Future Proof. Either the manifesto derives positions by the tenets (each plank as a test) or it imports values from the wider canon (vision.md: ownership, fiction of scarcity). Not chosen.
5. **The fleet is left-coded; the reader is right-drifting.** Billionaire cap and public ownership are the only fleet items; the target reader (`docs/marketing/the-reader.md`, via R04/R20) is working-class and drifting right. R20 finds cross-party water appetite but warns off hard numbers. CRIT 10 cut Billionaire Coin from the deck. Unresolved: how hard the manifesto leans on the fleet.
6. **The automation-gains question has a hypothesis and no answer.** The doorway rule (affected workers get a binding say) is "a hypothesis rather than an adopted policy platform"; shorter hours, profit sharing and public services are "possibilities to compare, not promised outcomes". How gains are counted is asked, not answered. This is the one question the film hands to Future Proof and Future Proof hands back to the reader.
7. **The failure chain is mostly about AI control; the tenets are about democratic process.** Bad-branch failures F15, F20-F22, F25 (containment, autonomous weapons, kill switches) have no Future Proof mechanism at all. FP never says what it would do about frontier-AI containment or an off switch. The "switch-it-off" through-line (F24) points at named human responsibility, which no tenet states.
8. **Portfolio gaps.** The ten ministers have no home for digital platforms and the attention machine (F13), AI regulation and containment (F15, F17), electoral integrity and democratic reform itself (F16, and all of tenet 1), science (F12), or data exclusion (F26). Tenet 1's whole programme is constitutional; the canon does not say who owns it.

**B. Tensions inside the tenets**

9. **The measurement blind spot (R9).** "A politics that anchors authority in measurement and competence is the same kind of instrument" the Storyverse condemns (doctrine, The Founding Deletion: "if it isn't in the accounts, it isn't real"). F26 shows it on the branch: the vault was "filed as gone" because it wasn't indexed. "Who represents the person whose needs still do not fit the instrument?" is an open thread, "not scheduled". Tenet 3 is built on the thing the sister epic attacks.
10. **Competence-qualified participation vs equal votes.** Canon proposes it (FP s3); every later reader flags it as disenfranchisement to this reader (R01 flag 4; SYN; kept off the deck). Not retracted in canon, not reconciled with "one person, one vote" either.
11. **What binds a composable vote?** No mechanism is chosen (R01 flag 2). The deck rules out referendums on everything (A1), phone voting for binding ballots (A2) and PR as the lead (A4), and points at advisory, low-stakes channels. What is binding, and when, is open.
12. **Continuous change vs stability.** R01 flag 3: "continuous governance" can sound like permanent chaos or election fatigue. The canon answer is "tests make fast change safe", but it does not say how often people are asked, or how sunsets avoid either auto-renewal (R13: anti-terror sunsets renew by default) or untested mass deletion (Retained EU Law).
13. **Experimenting on people.** The deck's own joke ("tested on you"; "side effects may include: all of us") cuts both ways: a trial has a control group that doesn't get the policy, and consent is not discussed. Not raised in canon.
14. **Which policy is exempt from testing?** "Diplomacy and judgement calls stay human work" (FP s3). No line is drawn; Foreign and Defence are the obvious cases, and F21 (autonomous war) sits in exactly that exempt zone.
15. **The idea pool has no wire.** "How engagement grows into an idea pool, debate or something larger remains open." No email, no platform (FP Engagement; open threads). R21: petitions show the gap ("the input exists, the wire to policy doesn't"). The manifesto can't promise a participation channel that doesn't exist.

**C. Factual and framing loose ends**

16. **"Five years."** The deck marks the five-year maximum CHECK and cuts every "five years" (DECK s5, flag 1); FC says "true under the 2022 Act" but unsourced in research; MICRO already states "UK general elections must be held at most five years apart". Inconsistent; needs one primary (parliament.uk) before any manifesto uses it.
17. **The deploy figure.** Canon's "100,000+ times a day" is unsourced (R13; SYN: drop it). MICRO uses Amazon's own 2014 figure, ~50 million deployments a year. FP still carries the bad number.
18. **Front door.** Two first questions compete: "who should decide how the gains from automation are shared?" (canon doorway) vs "why can't I vote on more than one thing?" (Kai's deck hook). SYN open question 1; the deck chose the second. Which leads a manifesto is open.
19. **Who speaks.** Kai to camera vs the narrator (SYN open question 2; DECK flag 6). For the government: ministers' voice vs the BadCode narrator's.
20. **Where it lives and whether it's live.** `/future-proof` deployment is unverified (FP doorway; DECK flag 7). Government channel on the TV homepage vs its own page (SYN open question 4; R03).
21. **Dates.** Only 2034 is canon; other years must not be printed as canon (DT open threads; GPOM README).
22. **The full in-voice Future Proof epic is unwritten** (FP open threads). The government manifesto may become its de facto first long text, which is a canon decision, not just a content one.
23. **Small Ideas.** The real initiative (Martin Lewis, with Nesta and Involve; deadline 12 Nov) is unverified in most details; any reference must be warm, credited, no implied endorsement (R10; CRIT 3; DECK s5 GATE).

---

## 5. What Future Proof explicitly refuses to claim

**About knowledge and authority**
- It does not know what works: "I won't pretend to know what works. I never got to run that experiment." "What works instead: unknown." (FP; MICRO)
- It does not hand over a plan: "never a manifesto ('follow my plan')"; "I won't hand you a plan. Nobody should." (FP; MICRO)
- The good branch is not written and must look unfinished: no tip, no destination, "a construction site". (FP structural fact; CODA)
- The AI does not decide: "the AI will tell us what to do" is a refused assumption; AI "decides nothing. A named person signs"; it will not take choices by force "even to fix it, and it accepts it may be ignored". (FP; DECK A5; DT)
- The tenets are not the plan and are not true by assertion: "hypotheses, deliberately imperfect", "probably wrong". Only the engineering facts are settled; the political application is "the experiment". (FP; FP receipts layer)
- The fleet is not derived from the tenets. (FP)
- The doorway rule is "a hypothesis rather than an adopted policy platform", "not a claim that the full epic or a public deliberation platform is finished"; its options are "not promised outcomes". (FP doorway)
- It does not claim measurement is fair: "a better scoreboard can still exclude people"; the hole is marked, not filled. (FP s3; MICRO)
- Not everything reduces to an experiment. (FP s3)
- No claim that BadCode has hands: "BadCode in 2026 has no hands that are not human hands." Warning, not takeover. (DT)

**About mechanisms**
- Not "change for its own sake", not "move fast and break things". (FP s2; DECK 8)
- Not referendums on everything; never name a real referendum; no Brexit on a slide. (DECK A1, s1)
- Not phone voting for binding elections; no claim about Estonia's security or effect. (DECK A2; R21)
- Not proportional representation as the ask. (DECK A4; R20)
- Not the Storyverse's physics: the deck keeps quantum, coin and One Lie material out. (R05)
- No sign-up, no account, no reply required; participation "earns no special status"; no email link published until an address exists. (FP; CODA)
- No implied partnership with Small Ideas, Martin Lewis, Nesta or Involve. (R10; CRIT 3)

**About facts (the fact gate's bans)**
- Never "invented before electricity" (Faraday 1831; say "older than the light bulb", 1872 vs 1878). Never "760 years" (say "1200s"). (DECK L1-L3; SYN s1)
- No "five years" / "2029" until sourced. (DECK s5, flag 1)
- No "100,000+ deploys a day". (R13; SYN)
- FCA sandbox: never "world first". (DECK L9)
- No count of unreviewed Acts; only "nobody keeps a central record". (DECK L8; R13)
- HMRC: 67.5% vs 79% only; no "eleven versions", "best of", sample size or £. (DECK L11; FC)
- Pol.is: four camps to two only; not "the other side secretly agrees", not what Taiwan's government did. (DECK L14; FC)
- No Swiss voting-day count; no Participedia count. (DECK L16, L12)
- Troubled Families: "counted vs measured", never "lied". Universal Credit: "badly piloted", not unpiloted. Finland and Stockton are not "proof UBI works". (R14; CRIT 5)
- Post Office: "hundreds" prosecuted, not 736; no punchline at victims. (FC; R13)

**About tone and target (the reader rules it inherits)**
- Never blame the voter; never "you've been duped"; "the voter is never the butt". (DECK s1; R04)
- Never "the computer": blame "the administrator", the decision-maker by act. (DECK s1; CODA)
- No villains, but not no accountability (R10).
- Never "AI is inevitable"; never use "we can't afford it" as our own line. (R04; `docs/using-ai.md`)
- No party names, no real people at lecterns, no logos. (DECK s1, s6)
- Two refused assumptions, restated: "we know the good path, we just have to walk it" and "the AI will tell us what to do." (FP)
