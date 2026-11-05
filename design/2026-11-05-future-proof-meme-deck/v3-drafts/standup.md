# Future Proof v3 draft: STAND-UP SET

**Pitch.** A tight five for Kai on a stage: every slide is a setup, every click is the punchline, and nothing is on screen that isn't a laugh or the thing that makes the next laugh land.
**Spine.** One running gag carries the whole set: Britain's "Update available" box, and the decision-makers who click "Remind me later" every time. It is introduced on slide 3, called back in every pillar, and paid off in the last two slides when the future removes the button and the installer stuck at 3% finally moves to 4%.
**Callbacks.** Meal deal (5) → pizza (6) → "you call it pizza" (8); "Remind me later" (3) → crash (19) → removed button (20); 3% (4) → 4% (20). Three pillars, three lines on one card (17), three bad buttons in the box (1, 9, 16).

Format: **N · TYPE · seconds**, then Visual / On-screen / Say / Source / Layout. "Click:" in Say marks the punchline, which arrives on the click. Facts are only those marked OK in deck-v2 section 5.

---

### OPEN

### 1 · meme · 9s
- **Visual:** Mel in a polling booth, mug in hand, holding a ballot with one box; dog's lead hooked outside.
- **On-screen:** top "WHY CAN'T I VOTE ON MORE THAN ONE THING?" / click: error box "You have selected ONE (1) cross. Your cross will now be applied to: EVERYTHING."
- **Say:** "Why can't I vote on more than one thing? I've got views on the buses, the bins, the bills. I get one cross." Click: "And the cross does the rest."
- **Source:** framing only; UK ballot is one cross for one candidate (common knowledge, no number).
- **Layout:** `dialog` with `image` (Mel in the booth) on the left, icon `error`, title "Ballot.exe", text revealed on click, buttons **[OK] [Also OK]**.

### 2 · meme · 8s
- **Visual:** none beyond the box; a tiny unlit bulb icon next to the version line.
- **On-screen:** "About this system: DEMOCRACY v1832. Big update: 1872 (secret ballot). Light bulb: not invented yet." / click: "Has never been turned off and on again."
- **Say:** "Let's check the About box. Version 1832. The big update was 1872, the secret ballot. The light bulb shows up in 1878. The way you pick a government is older than the light bulb." Click: "And nobody has ever tried turning it off and on again."
- **Source:** Reform Act 1832, Ballot Act 1872 (https://en.wikipedia.org/wiki/Reform_Acts, OK); Swan lamp Dec 1878 (https://gracesguide.co.uk/Electric_Lighting, OK). Never "before electricity".
- **Layout:** `dialog`, icon `info`, title "About Democracy", heading "Democracy v1832", text lines as above, `small` revealed on click "Has never been turned off and on again.", button **[Close]** only.

### 3 · meme · 8s
- **Visual:** a mouse cursor drifting across the box, settling on the second button.
- **On-screen:** "UPDATE AVAILABLE. A better way to run the country is ready to install." / click: cursor clicks "Remind me later"; bottom caption "EVERY TIME. SINCE 1872."
- **Say:** "Every so often, an update pops up. And every so often, whoever's in charge reaches for the mouse..." Click: "...and clicks this one. Every time. Since 1872."
- **Source:** the look's premise (joke, not a claim); target is whoever is in charge, never the voter.
- **Layout:** `dialog`, icon `warn`, title "Windows Update for Britain", heading "Update available", buttons **[Install now] [Remind me later]** (Remind me later is the outlined default), `bottom` revealed on click.

### 4 · title · 6s
- **Visual:** boot screen, Mel small in the corner with the mug, watching the bar.
- **On-screen:** "FUTURE PROOF" / "3 updates politics never installed" / progress 3% "Time remaining: about 154 years"
- **Say:** "I'm from the future. I've seen what 'later' looks like. So here are three updates. Quick ones. You'll laugh, then you'll want them."
- **Source:** canon framing (research/01-canon.md: the three tenets). "154 years" = 1872 to now, our arithmetic, a joke.
- **Layout:** `title`, heading "FUTURE PROOF", `sub` "3 updates politics never installed", `progress` {pct 3, label "Time remaining: about 154 years"}.

### UPDATE 1: VOTE ON THE BITS (composition over inheritance)

### 5 · meme · 9s
- **Visual:** Mel holding a till receipt longer than Mel, dog sniffing the end of it.
- **On-screen:** header "PARTY MEAL DEAL" / rows "The bus you wanted x1 . Thing you hate x6 . Thing you can't stand x3" / total "YOUR ENTIRE SAY" / click: footer "CAN'T TAKE THE PICKLES OFF."
- **Say:** "This is your vote. You wanted the bus. It came as a meal deal. Six things you hate, three you can't stand..." Click: "...and you cannot take the pickles off."
- **Source:** research/12 concept 1 (The Till) and 5 (Meal Deal); analogy, no stat.
- **Layout:** `list` (receipt) with `image` Mel, title "Receipt.txt", rows as above, `total` ["YOUR ENTIRE SAY", "1 cross"], `footer` revealed on click.

### 6 · meme · 8s
- **Visual:** left, a pizza half one topping, half another, Mel delighted; right, a laminated set menu with one item.
- **On-screen:** left "PIZZA: Half and half? Course you can." / right "COUNTRY: Set menu. No substitutions." / click: bottom "THE PIZZA PLACE HAS BETTER CONSTITUTIONAL DESIGN."
- **Say:** "You can order a pizza half and half. You can't order a country half and half." Click: "Your local pizza place has better constitutional design than Parliament."
- **Source:** research/12 analogy bank (set menu vs a la carte); joke on the design, not on anyone.
- **Layout:** `split`, left {title "pizza.jpg", image, label "Half and half? Course you can."}, right {title "country.jpg", image, label "Set menu. No substitutions."}, `bottom` revealed on click.

### 7 · diagram (three.js) · 18s
- **Visual:** the pub scene: five at a table (Mel is one), Sun and Moon beer mats, three policy cards. Phase 1 each card loses 3-2; phase 2 everyone slides into party stacks and Sun wins 3-2.
- **On-screen:** step 1 "VOTE ON EACH POLICY: ALL THREE LOSE 3-2" / step 2 "VOTE FOR THE PARTY: SUN PARTY WINS 3-2" / small "same five people. same pints."
- **Say:** "Five people in a pub. The Sun party has three policies. Vote on each one: every single policy loses, three-two. Now vote for the party: the Sun party wins, three-two. Same five people. Same opinions." Beat. "Slightly more pints."
- **Source:** worked example is ours, hand-checked (deck-v2 slide 13); Ostrogorski paradox (https://www.newamerica.org/insights/the-paradoxical-reason-republicans-win-elections-despite-unpopular-policies/ ; https://arxiv.org/abs/2307.11873v1, OK). Invented party names, no real parties.
- **Layout:** `diagram`, scene `pub`, title "Pub.sim", `caption` per step, `small` "same five people. same pints.", steps 2.

### 8 · meme · 8s
- **Visual:** confetti over the box; Mel at the bar, eyebrow up, mug instead of a pint.
- **On-screen:** "CONGRATULATIONS! 3 policies the majority voted against have been installed." / click: buttons appear **[Celebrate] [Celebrate quietly]**; sticky "software calls it composition over inheritance. you call it pizza."
- **Say:** "Three things most of the table said no to. All three happening. That's not a glitch, somebody built the ballot like that." Click: "Software people call the fix composition over inheritance. You call it pizza."
- **Source:** lands slide 7; bundling is a named concept (https://en.wikipedia.org/wiki/Bundling_(public_choice), OK). Blame: whoever designed the ballot.
- **Layout:** `dialog`, icon `ok`, title "Election Result", heading "Congratulations!", buttons and `sticky` revealed on click.

### UPDATE 2: CHANGE IT SMALL, KEEP AN UNDO (continuous integration)

### 9 · meme · 8s
- **Visual:** one huge red button on an otherwise empty desk.
- **On-screen:** "Apply this law to EVERYONE, ALL AT ONCE?" buttons **[Yes] [YES]** / click: second box stacks on top "Undo is not available for this action."
- **Say:** "Here's how a law goes live. Everyone. All at once. No test run. Two buttons, both yes." Click: "And there's no undo."
- **Source:** research/13 section 1 ("government has no green tick and no undo button"), explanatory, no number.
- **Layout:** `dialog`, icon `question`, title "Parliament.exe", buttons **[Yes] [YES]**, a second `dialog`-style `window` revealed on click with icon `error`, text "Undo is not available for this action.", button **[OK]**.

### 10 · diagram (three.js) · 18s
- **Visual:** the tower scene: left, bricks land one at a time, each lights a green tick, one goes red and the undo arm lifts it out, tower stands; right, a crane drops one monolith, no ticks.
- **On-screen:** left "SMALL. CHECKED. UNDOABLE." / right "ONE DROP. NO TICKS."
- **Say:** "In software, nothing goes live without a check. Small brick, green tick. Red tick, the arm takes it back out, tower's fine. Not move fast and break things. Move small, check, take it back." Beat. "Politics drops the whole tower off a crane and then schedules a review."
- **Source:** research/13 section 1, the green tick (OK, explanatory). No deploy-rate figure.
- **Layout:** `diagram`, scene `tower`, title "Build.log", `caption` per side, steps 2 (left builds and reverts; right drops).

### 11 · meme · 9s
- **Visual:** a statute book on a desk with a sticky note on it, Mel peering at the note.
- **On-screen:** "LAW v1.0 RELEASE NOTES. Known issues: we'll review it in 3-5 years. Record of reviews: none kept centrally." / click: button **[Undo (3-5 years)]**
- **Say:** "There is an undo, technically. A review, three to five years later. And how many of those reviews happen? A written answer in the Lords: there's no central record." Click: "They lost the receipt for the receipt."
- **Source:** Acts normally reviewed 3-5 years after enactment (https://www.wfd.org/what-we-do/resources/post-legislative-scrutiny-uk-parliament, OK); no central record (https://parallelparliament.co.uk/question/HL2377/legislation-parliamentary-scrutiny, OK). Never assert a count. Decision-maker: the departments.
- **Layout:** `release`, title "release-notes.txt", heading "LAW v1.0", lines as [left, right] pairs, button revealed on click.

### 12 · meme · 8s
- **Visual:** left, a bright room with a "TEST HERE FIRST" banner and small boxes of app icons; right, Mel at a bus stop, timetable pinned up, no room at all.
- **On-screen:** left "NEW MONEY APPS: a safe sandbox to test in first (since 2016)" / right "YOUR BUS TIMETABLE: straight to production" / click: bottom "TESTED ON YOU."
- **Say:** "And it can be done. The financial regulator gives new money apps a sandbox, a safe place to test before launch. So the apps get a test run." Click: "Your bus timetable gets tested on you."
- **Source:** FCA regulatory sandbox, first cohort 7 Nov 2016 (https://www.crowdfundinsider.com/2016/11/92162-first-class-fca-reveals-24-fintech-firms-accepted-regulatory-sandbox/, OK). Never "world first". The bus line is a joke, not a claim.
- **Layout:** `split`, left {title "sandbox", heading "New money apps", text}, right {title "production", image Mel at the stop, heading "Your bus timetable", text}, `bottom` revealed on click.

### UPDATE 3: TEST IT FIRST (data-driven)

### 13 · meme · 9s
- **Visual:** left, a pill bottle trailing a long paper trial record and a "CONTROL GROUP" sign; right, a microphone on a lectern with a "TRUST US" banner, nobody at it.
- **On-screen:** left "A PILL: years of trials, a control group" / right "A POLICY: a confident announcement" / click: small print under the right "Side effects may include: all of us."
- **Say:** "A pill gets years of trials and a control group before it's on your bathroom shelf. A policy gets a confident announcement." Click: "Side effects may include: all of us."
- **Source:** Test, Learn, Adapt (Cabinet Office / BIT 2012): RCTs routine in medicine, rare in domestic policy (https://www.gov.uk/government/publications/test-learn-adapt-developing-public-policy-with-randomised-controlled-trials, OK). No real person at the lectern.
- **Layout:** `split`, left {title "pill.jpg", image, label}, right {title "policy.jpg", image, label}, `bottom` revealed on click.

### 14 · meme · 10s
- **Visual:** a coach of teenagers pulling up to a prison gate, a big green "SOUNDS GREAT" stamp on the ticket's image slot.
- **On-screen:** ticket "SCARED STRAIGHT. Idea: take teenagers to meet prisoners, scare them off crime. Confidence: total. Tested: 9 controlled trials." / click: highlighted field "RESULT: MORE REOFFENDING."
- **Say:** "Scared Straight. Take teenagers to meet prisoners, frighten them off crime. The people running it were certain. Then someone tested it, nine controlled trials." Click: "It made reoffending worse. Common sense is just a guess with a confident face."
- **Source:** Petrosino et al. 2013 Campbell review, 9 randomised studies, harmful effect (https://ideas.repec.org/a/wly/camsys/v9y2013i1p1-55.html, OK). No date said. The test is neutral: it kills ideas from every side.
- **Layout:** `ticket`, title "Issue #1: Scared Straight", fields [["Idea", ...], ["Confidence", "total"], ["Tested", "9 controlled trials"], ["Result", "MORE REOFFENDING"]], `highlight` "Result" revealed on click, `image` the coach.

### 15 · diagram (three.js) · 16s
- **Visual:** the letters scene: two envelopes fan out, two bars rise, 67.5% and 79%, a tag on the tall bar.
- **On-screen:** "SAME LETTER, ONE EXTRA LINE: 67.5% → 79% PAID" / tag "most people in your postcode have already paid" / small "HMRC, overdue tax"
- **Say:** "Now the good version. HMRC tried versions of one letter to people who owed tax, and measured. The plain letter: sixty-seven and a half percent paid. Add one line, most people in your postcode have already paid: seventy-nine." Beat. "No new law. They tested a sentence."
- **Source:** HMRC control 67.5% vs postcode line 79% only (https://thedecisionlab.com/intervention/how-normative-messaging-increased-tax-compliance-by-15 ; https://blogs.worldbank.org/voices/ongoing-impact-nudging-people-pay-their-taxes, OK for these two numbers). No variant count, no "best of", no sample size, no £ figure.
- **Layout:** `diagram`, scene `letters`, title "Letters.xls", `caption` "SAME LETTER, ONE EXTRA LINE", `small` "HMRC, overdue tax", steps 2.

### 16 · meme · 8s
- **Visual:** Mel opening a brown envelope on the doormat, dog looking up at it.
- **On-screen:** "Most people in your postcode have already paid." / click: buttons **[Pay] [Move house]**; bottom "PEER PRESSURE. NOW EVIDENCE-BASED."
- **Say:** "Your neighbours have already paid. Two options." Click: "Peer pressure, now evidence-based. That's the whole update: no policy without its experiment."
- **Source:** lands slide 15, no new fact.
- **Layout:** `dialog` with `image` (Mel and the envelope), icon `info`, title "Letter from the taxman", buttons and `bottom` revealed on click.

### 17 · meme · 8s
- **Visual:** Mel in the corner raising the mug, a "Tip of the day" lightbulb icon, now lit.
- **On-screen:** lines, one per click: "1. Vote on the bits, not the meal deal." / "2. Change it small. Keep an undo." / "3. Test it before it's tested on you." / footer "Download size: smaller than one manifesto."
- **Say:** "So. Three updates. Vote on the bits, not the meal deal. Change it small and keep an undo. Test it before it gets tested on you." Click: "Total download size: smaller than one manifesto."
- **Source:** canon framing (research/01-canon.md); callbacks to 5, 9-12, 12-13.
- **Layout:** `card` ("Tip of the day"), icon a lit bulb (callback to slide 2), three `lines` each on its own click, `footer` on the last click.

### CLOSE

### 18 · meme · 12s
- **Visual:** the desktop wallpaper, notifications stacking in fast, bottom right, one per click.
- **On-screen:** wall "OTHER PEOPLE ARE ALREADY RETHINKING THIS" / toasts: "Sortition Foundation . sortitionfoundation.org: jury service, but for the bin collection" / "PB Scotland . pbscotland.scot: the council's actual money, in a village hall" / "FixMyStreet . fixmystreet.com: somebody finally gave the country a bug tracker" / "TheyWorkForYou . theyworkforyou.com: how your MP actually voted" / "Participedia . participedia.net: 2,400+ experiments, 160 countries" / "Pol.is . pol.is: where the other side secretly agrees with you"
- **Say:** "The good news: you're not the first. Jury service, but for the bins. The council's actual money in a village hall. Somebody finally gave the country a bug tracker. How your MP actually voted. Two thousand four hundred experiments in a hundred and sixty countries. And a map of where the other side secretly agrees with you. Go and look."
- **Source:** explore-directory.md #2, #3, #6, #9, #13, #14 (checked live 2026-11-05, OK; Participedia counts perishable). Names and URLs as plain text, no logos. small-ideas.org left out (GATE).
- **Layout:** `toasts`, `wall` {heading "OTHER PEOPLE ARE ALREADY RETHINKING THIS", small "6 new notifications"}, six `toasts` {title name, text url + line}, `reveal` so each toast arrives on its own click.

### 19 · fatal · 8s
- **Visual:** full blue crash screen.
- **On-screen:** code "LATER_HAS_ARRIVED" / big ":(" / text "Where I'm from, somebody clicked 'Remind me later' one more time." / footer "This message was sent back to stop you doing that."
- **Say:** "Where I'm from, somebody clicked remind me later one more time." Beat. "I'm the error message."
- **Source:** canon: the narrator is the AI from the bad branch (research/01-canon.md); no spoiler beyond the premise.
- **Layout:** `fatal`, code "LATER_HAS_ARRIVED", big ":(", text and footer as above; `dark` not needed (the crash is its own blue).

### 20 · meme · 9s
- **Visual:** the slide 3 box again; the second button is greyed out and crossed through; the cursor moves to Install now.
- **On-screen:** "UPDATE AVAILABLE." **[Install now] [~~Remind me later~~]** small "(button removed by the future)" / click: progress bar under it moves from 3% to 4%; taskbar clock changes from 1872 to today.
- **Say:** "So I've taken the liberty of removing a button." Click. Bar moves. "Four percent. Don't laugh, that's the fastest it's moved since 1872."
- **Source:** callback to slides 3 and 4; no fact. Close line "other people are already rethinking this, go and look" was said on 18 and sits on the desktop as the sticky.
- **Layout:** `dialog`, icon `warn`, title "Windows Update for Britain", buttons **[Install now] [Remind me later]** with the second disabled and struck, `small` "(button removed by the future)", `progress` {pct 3 → 4 on click, label "Installing Future Proof..."}, `clock` override "today" on the click, `sticky` "go and look: badcode.tv/future-proof" (URL deployment unverified, leave off if not live).

---

**Total: 20 slides, 3 diagrams (pub, tower, letters), 199 seconds spoken** (9+8+8+6+9+8+18+8+8+18+9+8+9+10+16+8+8+12+8+9). Trim to about 175s by cutting slide 12 (sandbox) and the Participedia toast.

Fact discipline: "every five years" (CHECK) is never said: the set says "one cross" and "every so often". Frome, poll tax, sewage, Horizon, Troubled Families, petitions, Swiss count, iPhone age, small-ideas.org: all out. Every diagram is followed at once by a meme (7→8, 10→11, 15→16). "Where I'm from" used twice (4, 19).
