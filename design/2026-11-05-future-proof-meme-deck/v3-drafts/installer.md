# Future Proof v3 draft: THE INSTALLER (one running gag)

**Pitch.** The whole talk is one install wizard: "Democracy 2.0 Setup", stuck at 3% since 1872, three steps, one per pillar.
At the end of each step the administrator (whoever is in charge that year, never Mel, never "the computer") clicks the default button, and "Remind me later" escalates three times: *later* → *after the next election* → *when it's someone else's problem*.
The turn: the narrator is from later, so it IS the reminder; the "later" button greys out ("154 years used"), Mel's cursor presses Install, the bar moves to 4%, and the taskbar clock finally changes from 1872.

Format as v2 main deck. Facts used are only v2 ledger rows marked OK (see the check at the bottom). 19 slides, 3 diagrams (pub, tower, letters), every diagram followed at once by a meme.

---

### COLD OPEN (1-4)

### 1 · meme · 9s
- **Visual:** a system dialog over the desktop. Mel's cursor hovers between two buttons. Mel (small, mug in hand) in the image slot on the left.
- **On-screen:** heading "Why can't I vote on more than one thing?" / text "You may select **1** box." / buttons "Everything" · "Also everything"
- **Say:** "Why can't I vote on more than one thing? Go on, ask it out loud. Nobody has ever answered it."
- **Source:** framing, no fact (one cross for one candidate, common knowledge).
- **Layout:** `dialog`, title "GENERAL ELECTION", icon question, buttons ["Everything", "Also everything"], the first one outlined as the default.

### 2 · meme · 12s
- **Visual:** the "About this system" window every old computer has: a version number, an install date, a small picture of a candle where the logo would be.
- **On-screen:** heading "Democracy, version 1872" / lines "Parliament: 1200s" · "Secret ballot: 1872" · "Last big patch: 1928" · "Light bulb: not invented yet (1878)" / bottom caption "OLDER THAN THE LIGHT BULB."
- **Say:** "Here's what you're running. Parliament: the twelve-hundreds. Secret ballot: 1872. Last big patch: 1928. The light bulb turns up in 1878. The way we pick a government is older than the light bulb."
- **Source:** ledger rows 3 / 3,4 / 5 (OK): 1265 (said "1200s"), 1872 Ballot Act, Swan Dec 1878, Equal Franchise Act 1928. Never "before electricity".
- **Layout:** `release`, title "About This System", heading "Democracy, version 1872", lines as above revealed one per click, the light-bulb line last; buttons ["Check for updates", "Remind me later"]; bottom "OLDER THAN THE LIGHT BULB."

### 3 · title · 8s
- **Visual:** a boot screen for the new version. The progress bar is at 3% and has clearly been there a while (cobweb in the corner of the bar).
- **On-screen:** heading "DEMOCRACY 2.0 SETUP" / sub "3 updates ready" / progress 3% "Installing... (since 1872)"
- **Say:** "Good news. The update exists. Three of them, actually. It's been sitting at three percent since 1872, because every time it's ready, somebody clicks..."
- **Source:** framing; the three updates are the three pillars (canon, research/01-canon.md).
- **Layout:** `title`, heading "DEMOCRACY 2.0 SETUP", sub "3 updates ready", progress {pct: 3, label: "Installing... (since 1872)"}.

### 4 · meme · 8s
- **Visual:** the classic update nag. Behind it, a padlock on the Install button and a little notice: you are a standard user.
- **On-screen:** heading "Restart Britain to finish installing?" / buttons "Remind me later" · "Restart now" (greyed) / small "Only the administrator can install updates." / sticky (Mel) "who's the administrator?"
- **Say:** "...remind me later. Not you, Mel. You're a standard user. The administrator is whoever's in charge that year. And they've got a lot on."
- **Source:** framing. Blames the decider by act (who holds the button), never the voter, never "the computer".
- **Layout:** `dialog`, title "Update Available", icon warn, buttons ["Remind me later", "Restart now"] (Remind me later outlined default), small "Only the administrator can install updates.", sticky "who's the administrator?"

### STEP 1 OF 3: COMPOSITION OVER INHERITANCE (5-8)

### 5 · meme · 9s
- **Visual:** the "choose install type" page of a wizard. Typical install is one giant box. Custom install has tick boxes per issue (Buses, Bins, Bills, Housing) and is greyed out.
- **On-screen:** heading "Step 1 of 3: Choose install type" / "Typical: everything, as one bundle. Pick a party." / "Custom: choose each part (not available in this version)"
- **Say:** "Step one. Every installer you've ever met has a Custom button. Untick the free toolbar. Untick the screensaver. Politics only offers Typical. All of it, in one box, take it or leave it."
- **Source:** framing; bundling is a named concept (ledger row 11, OK).
- **Layout:** `dialog`, title "Democracy 2.0 Setup", heading "Step 1 of 3: Choose install type", text with the two options (Custom greyed), buttons ["Typical (everything)", "Custom"] with Custom disabled-looking, small "Custom install is a Democracy 2.0 feature."

### 6 · diagram (three.js) · 18s
- **Visual:** the `pub` scene. Five people at a pub table, Mel one of them; three policy cards for the Sun party. Phase 1, one vote per card: each loses 3-2. Phase 2, one vote for the party: Sun party wins 3-2.
- **On-screen:** phase 1 "EVERY POLICY LOSES 3-2." phase 2 "THE PARTY THAT OFFERS ALL THREE WINS 3-2." tag "same five people. same opinions."
- **Say:** "Five people in a pub. The Sun party has three policies. Vote on them one at a time: every single one loses, three-two. Vote for the party: Sun party wins, three-two. Same people. Same pints. Only the ballot changed."
- **Source:** ledger row 13 (OK): Ostrogorski paradox; worked example ours, hand-checked (three Sun voters each dislike a different policy, two Moon voters dislike all three).
- **Layout:** `diagram`, title "pub.exe", scene `pub`, caption phase lines as above, small "software calls it composition over inheritance", steps 2.

### 7 · meme · 7s
- **Visual:** the ballot box as a dialog, reporting what it recorded. Mel's thought bubble in the image slot: a bus.
- **On-screen:** heading "Vote recorded." / text "You selected: **the bus**.\nWe saved: **all of it**." / bottom "I VOTED FOR THE BUS."
- **Say:** "Mel voted for the bus. The box saved all of it. Somebody built the box that way. Wasn't Mel."
- **Source:** lands slide 6; no fact. The decision-maker is whoever designed the ballot.
- **Layout:** `dialog`, title "ballot_box.exe", icon info, buttons ["OK", "OK (all of it)"], image of Mel with the bus thought bubble, bottom "I VOTED FOR THE BUS."

### 8 · meme · 7s
- **Visual:** the nag again, one button longer than before.
- **On-screen:** heading "Install 'Vote issue by issue'?" / buttons "Remind me after the next election" · "Install" / small "The next election is also a bundle."
- **Say:** "Install vote-issue-by-issue? Remind me after the next election. Which is... also a bundle. Lovely."
- **Source:** framing, no fact. Laters count: 2 of 3.
- **Layout:** `dialog`, title "Update Available", icon warn, buttons ["Remind me after the next election", "Install"], small "Note: the next election is also a bundle."

### STEP 2 OF 3: CONTINUOUS INTEGRATION (9-12)

### 9 · meme · 9s
- **Visual:** the wizard's "how should updates be installed?" page, two radio buttons. The bad one is ticked, labelled "(current setting)".
- **On-screen:** heading "Step 2 of 3: How should changes be installed?" / "( ) Small pieces, each one checked, with an undo (recommended)" / "(•) All at once, from a height, no undo (current setting)"
- **Say:** "Step two. Your phone updates in little pieces, and if one goes wrong, it rolls back. Software calls that continuous integration. Laws get dropped in one lump, from a height."
- **Source:** ledger row 19 (OK, explanatory): the green-tick idea, research/13 section 1. No deploy-rate figure.
- **Layout:** `dialog`, title "Democracy 2.0 Setup", heading "Step 2 of 3", text with the two radio lines, buttons ["< Back", "Next >"].

### 10 · diagram (three.js) · 16s
- **Visual:** the `tower` scene. Left: small bricks land one at a time, each lights a green tick; one lights red and the undo arm lifts it out, tower still standing. Right: one monolith dropped whole, no ticks.
- **On-screen:** left "SMALL. CHECKED. UNDOABLE." right "ONE DROP. NO TICKS."
- **Say:** "Small brick, check it, tick. Small brick, tick. That one's wrong: lift it out, tower's fine. It isn't move fast and break things. It's move small, and be able to take it back."
- **Source:** ledger row 19 (OK). Trap guard: "isn't move fast and break things" said aloud.
- **Layout:** `diagram`, title "deploy.exe", scene `tower`, caption the two labels, steps 3.

### 11 · meme · 10s
- **Visual:** a greyed-out Edit menu, "Undo" disabled, over a huge statute book. A search bar under it, still spinning.
- **On-screen:** heading "Undo is not available for this law." / text "Review: in 3-5 years.\nRecord of reviews done: **no central record**." / bottom "NOBODY'S COUNTING THE UNDO BUTTON."
- **Say:** "Every app you own has undo. A law gets a review, three to five years later. And the Lords were told there's no central record of how many of those reviews even happen."
- **Source:** ledger row 20 (OK): Acts normally reviewed 3-5 years after enactment, https://www.wfd.org/what-we-do/resources/post-legislative-scrutiny-uk-parliament ; ledger row 21 (OK): no central record, https://parallelparliament.co.uk/question/HL2377/legislation-parliamentary-scrutiny . No count of unreviewed Acts.
- **Layout:** `dialog`, title "Edit > Undo", icon error, buttons ["OK", "Remind me in 3-5 years"], progress {pct: 40, label: "Searching for the reviews..."}, bottom "NOBODY'S COUNTING THE UNDO BUTTON."

### 12 · meme · 10s
- **Visual:** the nag for the third time, plus an "installed on" list: one row ticked, the rest not.
- **On-screen:** heading "Install 'Small changes, with an undo'?" / text "Already installed on: **new money apps** (sandbox, since 2016).\nNot installed on: the bus timetable." / buttons "Remind me when it's someone else's problem" · "Install everywhere"
- **Say:** "Here's the funny bit: we already have it. The financial regulator has let new money apps test in a safe sandbox since 2016. Fintech gets a sandbox. The bus timetable gets the live version. Remind me when it's someone else's problem."
- **Source:** ledger row 24 (OK): FCA sandbox, first cohort 7 Nov 2016, https://www.crowdfundinsider.com/2016/11/92162-first-class-fca-reveals-24-fintech-firms-accepted-regulatory-sandbox/ . No "world first". Bus timetable is a joke, not a claim. Laters count: 3 of 3.
- **Layout:** `dialog`, title "Update Available", icon warn, buttons ["Remind me when it's someone else's problem", "Install everywhere"], the long button so wide it shoves the other to the window edge.

### STEP 3 OF 3: DATA-DRIVEN (13-16)

### 13 · meme · 8s
- **Visual:** two installer windows side by side. Left: a pill's installer with a long checklist of trials, all ticked. Right: a policy's installer with one line and a big "Skip" button.
- **On-screen:** left "A PILL: Running trials... control group... years." / right "A POLICY: Confident announcement... done." button "Skip testing (recommended by the person announcing it)"
- **Say:** "Step three. A pill gets years of trials before it's allowed in your bathroom cabinet. A policy gets a confident announcement."
- **Source:** ledger row 26 (OK): Test, Learn, Adapt (2012), https://www.gov.uk/government/publications/test-learn-adapt-developing-public-policy-with-randomised-controlled-trials .
- **Layout:** `split`, left {title "pill_setup.exe", heading "A PILL", lines of ticked trials}, right {title "policy_setup.exe", heading "A POLICY", text "Confident announcement... done.", buttons ["Skip testing (recommended by the person announcing it)"]}, top "Step 3 of 3: Testing".

### 14 · diagram (three.js) · 15s
- **Visual:** the `letters` scene. Two envelopes fan out; two bars rise, plain letter 67.5%, letter with the postcode line 79%.
- **On-screen:** "SAME LETTER, ONE EXTRA LINE: 67.5% → 79% PAID." small "HMRC, overdue tax"
- **Say:** "HMRC tried different versions of one letter to people who owed tax. Plain letter: sixty-seven and a half percent paid. Add 'most people in your postcode have already paid': seventy-nine. Nobody passed a law. They tested a sentence."
- **Source:** ledger row 27 (OK for 67.5 vs 79 only): https://thedecisionlab.com/intervention/how-normative-messaging-increased-tax-compliance-by-15 . No variant count, no sample size, no £ figure.
- **Layout:** `diagram`, title "letters.exe", scene `letters`, caption as above, small "HMRC, overdue tax", steps 2.

### 15 · meme · 10s
- **Visual:** a bug ticket for a policy that sounded great. The result row is highlighted yellow.
- **On-screen:** heading "FEATURE: take teenagers round a prison to scare them off crime" / fields "Status: SOUNDED GREAT" · "Tested by: 9 controlled trials" · "Result: MORE REOFFENDING" / bottom "COMMON SENSE IS A HYPOTHESIS."
- **Say:** "And sometimes the test says no. Scared Straight: walk teenagers round a prison, frighten them off crime. The people running it were sure. Nine controlled trials later: more reoffending, not less. Common sense is a hypothesis."
- **Source:** ledger row 28 (OK): Petrosino et al. 2013 Campbell review, 9 randomised studies, https://ideas.repec.org/a/wly/camsys/v9y2013i1p1-55.html . Names who was sure by act (the people running it). The test is neutral, which keeps the tough-on-crime viewer on side.
- **Layout:** `ticket`, title "Issue tracker: policy", heading as above, fields [["Status", "SOUNDED GREAT"], ["Tested by", "9 controlled trials"], ["Result", "MORE REOFFENDING"]], highlight "Result", bottom "COMMON SENSE IS A HYPOTHESIS."

### 16 · meme · 8s
- **Visual:** the release notes for the version nobody has installed. Three lines. That's the whole talk.
- **On-screen:** heading "DEMOCRACY 2.0: what's new" / "1. Vote issue by issue, not one bundle." / "2. Change laws small, check them, keep an undo." / "3. No policy without its experiment."
- **Say:** "So that's the update. Vote issue by issue. Change laws small, check them, keep an undo. No policy without its experiment. Three lines. It's been ready for ages."
- **Source:** canon, research/01-canon.md (the three tenets).
- **Layout:** `release`, title "Release notes", heading "DEMOCRACY 2.0: what's new", lines the three tenets (one per click), footer "Download size: three sentences.", buttons ["Install", "Remind me later"].

### THE TURN AND THE CLOSE (17-19)

### 17 · meme · 12s
- **Visual:** the nag one last time. "Remind me later" is greyed out. Mel's cursor drifts onto "Install now". On click 2, a toast pops: "Reminder: it's later."
- **On-screen:** heading "Remind me later?" / small "You have used all your laters. (154 years of them.)" / buttons "Remind me later" (greyed) · "Install now" / toast on click 2 "Reminder from: later. It's later."
- **Say:** "Every time, somebody clicked remind me later. Well. I'm from later. I've seen how it goes when nobody installs it. This is the reminder. I am the reminder."
- **Source:** framing; narrator-from-the-future (used once, here). 154 = 2026 minus 1872 (ledger row 3,4, OK).
- **Layout:** `dialog`, title "Update Available", icon warn, heading "Remind me later?", small "You have used all your laters. (154 years of them.)", buttons ["Install now", "Remind me later"] with Install now now the outlined default and Remind me later greyed; reveal a sticky/toast "Reminder from: later. It's later." at step 1; steps 2.

### 18 · meme · 12s
- **Visual:** notifications stacking in the bottom-right, one per click, while the wallpaper says other machines have already started.
- **On-screen:** wall "Partial updates found nearby" / small "other people are already rethinking this" / toasts: "Sortition Foundation: jury service, but for the bin collection. sortitionfoundation.org" · "PB Scotland: the council's actual money, voted on in a village hall. pbscotland.scot" · "CONSUL: free software councils use for proposals and budget votes. consuldemocracy.org" · "FixMyStreet: somebody gave the country a bug tracker. fixmystreet.com" · "TheyWorkForYou: how your MP voted, issue by issue. theyworkforyou.com" · "Pol.is: in Taiwan, four camps on one row ended up as two. pol.is"
- **Say:** "And you're not the first. Jury service for the bin collection. Council money voted on in a village hall. A bug tracker for potholes. How your MP voted, one issue at a time. In Taiwan, a tool that turned four camps into two. Pause it. Open a tab."
- **Source:** ledger row 40-54 (OK): explore-directory.md, all URLs checked live 2026-11-05; Pol.is line from ledger row 37 (OK for four-to-two camps only, no participant counts, no government-outcome claim). small-ideas.org left out (GATE). Names and URLs as plain text, no logos.
- **Layout:** `toasts`, wall {heading "Partial updates found nearby", small "other people are already rethinking this"}, six toasts each {title: project name, text: one line + URL}, reveal one per click.

### 19 · title · 7s
- **Visual:** the boot screen from slide 3, Mel's cursor still on it. The bar has moved: 4%. Then the taskbar clock flips from 1872 to today.
- **On-screen:** heading "DEMOCRACY 2.0" / progress 4% "Installing... (fastest it's moved since 1872)" / sub "other people are already rethinking this. go and look." / clock: 1872 → 2026 on click
- **Say:** "Four percent. Fastest it's moved in a hundred and fifty years. Other people are already rethinking this. Go and look."
- **Source:** framing; links as slide 18. "150 years" is the rounded 154.
- **Layout:** `title`, heading "DEMOCRACY 2.0", progress {pct: 4, label: "Installing... (fastest it's moved since 1872)"}, sub as above, `clock` override "2026" revealed on the last click (the one deliberate clock gag the look allows).

---

**Total: 195 seconds (3:15), 19 slides: 3 diagrams (pub, tower, letters), 1 split, 15 OS memes; 2 title screens among them.**
Breakdown: cold open 37s · step 1 41s · step 2 45s · step 3 41s · turn and close 31s. To land under 3:00, cut slide 13 (the pill; slide 14 still makes the point) and trim slide 18 to four toasts: 177s.

**Fact check against the v2 ledger (section 5):** every claim is a row marked OK. Deliberately left out: "five years" / "2029" (row 2,6 is CHECK, so the five-year joke becomes "after the next election"); the iPhone "nineteen" (GK); Frome (CHECK); poll tax (CHECK); sewage (CUT-IF); small-ideas.org (GATE); Post Office / Horizon (victims are real, and a comedy installer is the wrong room for it).

**Running gag ledger:** "Remind me later" is clicked by the administrator on slides 4, 8, 12 (rising: later → after the next election → when it's someone else's problem), sits on the window as an option on 2, 11 and 16, greyed out on 17. The 3% bar (3) pays off at 4% (19). The 1872 clock pays off by changing once, at the very end. Mel is the standard user who notices, and the one whose cursor finally presses Install.
