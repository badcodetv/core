# Future Proof v3 draft: PATCH NOTES FOR BRITAIN

**Pitch.** The whole talk is the release notes for "Britain v2.0", read out in a deadpan voice: Known issues (three bug tickets, reported by Mel), Fixed in this version (one fix per pillar), Breaking changes, and the install dialog.
**Why it's funnier.** The software format does the joking, so the narrator never has to. Every slide is a ticket, an installer or a dialog with two bad buttons, and the three bugs, the three fixes and the breaking changes are one rule of three told three times.
**The button.** "Remind me later" gets clicked from the boot screen onward. The narrator turns out to be the reminder, and when Mel clicks "Update now" the taskbar clock moves off 1872 for the first and only time.

Callbacks: the **pencil on a string** (slides 4, 10, 17); **"remind me later"** (2, 19); **Mel as the tester** who filed every bug (5-7, 16, 19). "Where I'm from" is said twice (2, 19). Diagrams: three (timeline, pub, letters), each one followed at once by a meme. Pillar 2 is told with memes, because "small, checked, undoable" is quicker to say than to show.

---

### 1 · meme · 9s
- **Visual:** Mel in a polling booth holding a ballot paper with one box on it. The dog waits outside, its lead on the hook.
- **On-screen:** top "WHY CAN'T I VOTE ON MORE THAN ONE THING?" / dialog "You may select 1 (one) item." buttons "OK" / "Cancel (unavailable)"
- **Say:** "Why can't I vote on more than one thing? Good question. Nobody's ever answered it. So instead, I'm going to read you the release notes."
- **Source:** framing, no fact. UK ballot is one cross (common knowledge).
- **Layout:** `dialog` with `image` (Mel in the booth): title "Ballot", icon `warn`, heading "Selection limit reached", text "You may select 1 (one) item.", buttons ["OK", "Cancel (unavailable)"], with the question in `top`.

### 2 · title · 10s
- **Visual:** a boot screen. A small "Update available" balloon sits in the corner, and a cursor clicks "Remind me later" on it. The taskbar clock reads 1872.
- **On-screen:** "FUTURE PROOF" / "Britain v2.0: release notes" / progress bar "Update available since 1872" at 3%
- **Say:** "Where I'm from, this little box popped up every morning for over a hundred and fifty years. And every morning, somebody in charge clicked 'remind me later'."
- **Source:** secret ballot 1872, the last big install (https://en.wikipedia.org/wiki/Reform_Acts, OK). "Over 150 years" = 1872 to now. Blame sits with "somebody in charge", never the voter.
- **Layout:** `title`: heading "FUTURE PROOF", sub "Britain v2.0 release notes", progress {pct: 3, label: "Update available since 1872. Remind me later?"}; `sticky` "clicked: every time".

### 3 · diagram (three.js) · 15s
- **Visual:** the timeline scene. Markers land one per beat: 1200s Parliament, 1832 Reform Act, 1872 secret ballot. Then a bulb lights up at 1878, and the camera pulls back to show all three markers sitting to the left of it.
- **On-screen:** "OLDER THAN THE LIGHT BULB" (markers carry only a year and a two-word label; no phone marker)
- **Say:** "Parliament: the twelve hundreds. The Reform Act: 1832. The secret ballot: 1872. The light bulb: 1878. The way you choose a government is older than the light bulb."
- **Source:** ledger OK: 1265 (say "1200s"), 1832, 1872, Swan lamp Dec 1878 (research/15; parliament.uk/demontfort; Reform_Acts; gracesguide Electric_Lighting). Never say "before electricity". The v2 "your phone is nineteen" is dropped (GK, unverified).
- **Layout:** `diagram`, scene `timeline`, title "history.exe", caption "OLDER THAN THE LIGHT BULB", steps 4.

### 4 · meme · 8s
- **Visual:** two windows side by side. Left: a modern smart bulb glowing, with a phone beside it controlling it. Right: a polling-booth shelf with a pencil tied on a string.
- **On-screen:** left "LIGHT BULB: dimmable. Colours. Talks to your phone." / right "BALLOT: got a pencil. On a string."
- **Say:** "Since then the light bulb has had a few updates. It's dimmable. It changes colour. It talks to your phone. The ballot got a pencil. On a string."
- **Source:** observation, no ledger claim (the pencil on a string is the joke, not a statistic).
- **Layout:** `split`: left {title "lightbulb.exe", label "v1878 → today", lines ["Dimmable", "16 million colours", "Talks to your phone"]}, right {title "ballot.exe", label "v1872 → today", lines ["Pencil", "String (added)"]}, with `bottom` "CHANGELOG".

### 5 · meme · 10s
- **Visual:** a bug-tracker ticket. In the corner, a small picture of Mel holding the long receipt for a whole party bundle.
- **On-screen:** "BUG #1: Can only select one item" / "Status: WON'T FIX"
- **Say:** "Known issues. Bug one, reported by Mel. Steps to reproduce: want a bus. Vote. Receive the whole party. Status: won't fix."
- **Source:** framing, no fact. Blame is assigned to the ballot's designer, by act.
- **Layout:** `ticket`: title "Known issues (3)", heading "BUG #1: Can only select one item", fields [["Reported by", "Mel"], ["Steps", "1. Want the bus. 2. Vote. 3. Receive everything else."], ["Expected", "The bus"], ["Actual", "All of it, for years"], ["Assigned to", "Whoever designed the ballot"], ["Status", "WON'T FIX"]], highlight "Status".

### 6 · meme · 9s
- **Visual:** a ticket with a keyboard pictured in its corner, the Ctrl and Z keys lit up.
- **On-screen:** "BUG #2: No undo" / "Reviews done: NO CENTRAL RECORD"
- **Say:** "Bug two. There's no undo. A law is meant to get a review three to five years later. How many of those reviews happen? There's no central record. Nobody's counting."
- **Source:** ledger OK: Acts normally reviewed 3-5 years after enactment (https://www.wfd.org/what-we-do/resources/post-legislative-scrutiny-uk-parliament); no central record of the reviews (https://parallelparliament.co.uk/question/HL2377/legislation-parliamentary-scrutiny). No count of unreviewed Acts is given.
- **Layout:** `ticket`: heading "BUG #2: No undo", fields [["Steps", "1. Pass a law. 2. It goes wrong. 3. Press Ctrl+Z."], ["Actual", "\"We'll review it in 3-5 years.\""], ["Reviews done", "No central record"], ["Assigned to", "The department that passed it"]], highlight "Reviews done".

### 7 · meme · 8s
- **Visual:** a ticket with a small picture: a pill bottle with a thick stack of trial paperwork behind it, next to a lone megaphone.
- **On-screen:** "BUG #3: Ships without testing" / "Resolution: WORKS ON MY MACHINE"
- **Say:** "Bug three. A pill gets years of trials. A policy gets a press conference. Resolution: works on my machine."
- **Source:** ledger OK: trials routine in medicine, rare in domestic policy ("Test, Learn, Adapt", https://www.gov.uk/government/publications/test-learn-adapt-developing-public-policy-with-randomised-controlled-trials).
- **Layout:** `ticket`: heading "BUG #3: Ships without testing", fields [["Expected", "Tested first (like a pill)"], ["Actual", "A confident announcement"], ["Closed by", "The person who announced it"], ["Resolution", "WORKS ON MY MACHINE"]], highlight "Resolution".

### 8 · diagram (three.js) · 18s
- **Visual:** the pub scene. Five people sit at a pub table, Mel among them, with Sun party and Moon party beer mats. The Sun party's three policies float above the table. Phase 1: each policy loses 3-2. Phase 2: everyone votes for a party, and the Sun party wins 3-2.
- **On-screen:** caption "FIXED IN THIS VERSION. FIX #1: VOTE ISSUE BY ISSUE" / phase 1 "EVERY POLICY LOSES 3-2" / phase 2 "THE PARTY WITH ALL THREE WINS 3-2" / small "same five people. same pints."
- **Say:** "Fix one. Five people in a pub. Vote on the Sun party's policies one at a time, and every single one loses, three-two. Vote for the party, and the party wins, three-two. Same people. Same pints. Only the ballot changed."
- **Source:** ledger OK: Ostrogorski paradox (newamerica.org link; arxiv 2307.11873v1). The worked example is ours and was checked by hand. The parties are invented.
- **Layout:** `diagram`, scene `pub`, title "fix-1.exe", caption "FIX #1: VOTE ISSUE BY ISSUE", small "same five people. same pints.", steps 3.

### 9 · meme · 8s
- **Visual:** the classic software installer, with Mel's cursor hovering over a ticked checkbox that won't untick.
- **On-screen:** "[x] Also install 399 other things you didn't ask for (this box cannot be unticked)"
- **Say:** "That's the current ballot. You know when an installer sneaks in a toolbar you didn't want? It's that. For the whole country."
- **Source:** joke over the mechanism, no fact ("399" is an installer gag, not a policy count).
- **Layout:** `dialog`: title "Party Setup Wizard", icon `info`, heading "Installing: The Bus", text "[x] Also install 399 other things you didn't ask for\n(this box cannot be unticked)", buttons ["Next >", "Next >"], progress {pct: 3, label: "Installing all of it"}.

### 10 · meme · 8s
- **Visual:** release notes, with a pizza in the corner split half and half.
- **On-screen:** "FIX #1 notes" / "Every issue gets its own box." / "Already shipped in some other countries. Their pencils coped." / footer "Engineers call this composition over inheritance. You can call it 'obviously'."
- **Say:** "Every issue gets its own box. Some countries already do this, and their pencils coped fine. Engineers call it composition over inheritance. You can call it 'obviously'."
- **Source:** ledger OK: some countries vote issue by issue (https://www.admin.ch/gov/en/start/documentation/votes.html). No country is named and no number or result is given; the word "referendum" never appears. "Bundling" is a named concept (Wikipedia Bundling_(public_choice), OK).
- **Layout:** `release`: title "Britain v2.0", heading "FIX #1: Issue-by-issue voting", lines ["Every issue gets its own box", "Already shipped elsewhere. Pencils coped.", "Pizza can now be half and half"], footer "Engineers call this composition over inheritance. You can call it 'obviously'."

### 11 · meme · 10s
- **Visual:** two windows. On the left, a phone's "updates installed" list: dozens of tiny updates, each with a green tick, one with a red cross and an "Undone" label beside it. On the right, one enormous grey block labelled "THE LAW", with no ticks on it.
- **On-screen:** caption "FIX #2: CHANGE SMALL. CHECK IT. KEEP AN UNDO." / left "YOUR PHONE: 40 tiny updates. All checked. One undone." / right "THE LAW: one big one. Good luck."
- **Say:** "Fix two. Your phone updates in tiny pieces. Each one's checked. If one's wrong, it undoes just that one. Not move fast and break things. Move small, and fix things."
- **Source:** canon pillar 2; research/13 section 1 ("the green tick"; no deploy-rate figure). "40" is a picture detail, not a statistic. The "not move fast and break things" line is said aloud, as the trap guard. (The `tower` scene is kept back to stay within three diagrams; swap it in here if Kai would rather lose the timeline diagram.)
- **Layout:** `split`: left {title "Updates", label "installed today", lines ["✓ small fix", "✓ small fix", "✗ small fix (undone)", "✓ small fix"]}, right {title "law.exe", label "installed: all at once", heading "THE LAW", text "One big one. Good luck."}, with `top` "FIX #2: CHANGE SMALL. CHECK IT. KEEP AN UNDO."

### 12 · meme · 8s
- **Visual:** the grey block from the slide before, now an installer window stuck at 3%. A tiny Mel stands under it holding a mug.
- **On-screen:** "Installing NEW LAW (all of it, all at once)... 3%" / "Please do not turn off your country."
- **Say:** "Here's how we do it now. Install the whole thing at once. Stuck at three percent. Please do not turn off your country."
- **Source:** joke, no fact.
- **Layout:** `dialog`: title "Law Installer", icon `warn`, heading "Installing NEW LAW (all of it, all at once)", progress {pct: 3, label: "Time remaining: a general election", err: true}, text "Please do not turn off your country.", buttons ["Cancel (unavailable)"].

### 13 · meme · 9s
- **Visual:** release notes, with two doors pictured in the corner. One door says "SANDBOX: NEW MONEY APPS" and opens onto a bright test room; the other says "BUS TIMETABLE" and opens onto a drop.
- **On-screen:** "FIX #2 notes" / "Laws ship in small pieces." / "Each piece checked before the next." / "Undo included." / footer "Already in use: new money apps get a test sandbox (since 2016). The bus timetable is still waiting."
- **Say:** "Small pieces, each one checked, undo included. And it already exists: since 2016 the financial regulator has given new money apps a sandbox to test in. The bus timetable is still waiting."
- **Source:** ledger OK: FCA sandbox, first cohort 7 Nov 2016 (crowdfundinsider link). Never say "world first".
- **Layout:** `release`: heading "FIX #2: Continuous integration", lines ["Laws ship in small pieces", "Each piece checked before the next", "Undo button included"], footer "Already in use: new money apps get a sandbox (since 2016). The bus timetable is still waiting."

### 14 · diagram (three.js) · 15s
- **Visual:** the letters scene. Two envelopes fan out, then two bars rise: "plain letter" to 67.5% and "one extra line" to 79%.
- **On-screen:** caption "FIX #3: NO POLICY WITHOUT ITS EXPERIMENT" / "SAME LETTER, ONE EXTRA LINE: 67.5% → 79% PAID" / small "HMRC, overdue tax"
- **Say:** "Fix three. HMRC tested a letter to people who owed tax. Plain letter: sixty-seven and a half percent paid. Add one line, 'most people in your postcode have already paid': seventy-nine. Nobody passed a law. They tested a sentence."
- **Source:** ledger OK for 67.5% vs 79% only (thedecisionlab.com; World Bank blog). The slide never says "eleven", "best of", gives a sample size, or mentions £160m.
- **Layout:** `diagram`, scene `letters`, title "fix-3.exe", caption "FIX #3: NO POLICY WITHOUT ITS EXPERIMENT", small "HMRC, overdue tax", steps 3.

### 15 · meme · 10s
- **Visual:** a changelog ticket with a small picture: a coach full of teenagers pulling up at a prison gate, stamped green "SOUNDED GREAT".
- **On-screen:** "FEATURE REMOVED: Scared Straight" / "Reason: WE CHECKED."
- **Say:** "Scared Straight. Take teenagers to meet prisoners, frighten them off crime. Everyone who ran it was sure. Nine controlled trials said it did more harm than good. Removed. Reason: we checked."
- **Source:** ledger OK: Campbell review, 9 trials, 946 youths, likely harmful (https://ideas.repec.org/a/wly/camsys/v9y2013i1p1-55.html). The people named are the ones who ran it, by act; no date is given. A test can kill an idea from any side, which keeps the "tough on crime" viewer with us.
- **Layout:** `ticket`: title "Changelog", heading "FEATURE REMOVED: Scared Straight", fields [["What it did", "Took teenagers to meet prisoners"], ["Sounded", "Great"], ["Tested", "9 controlled trials"], ["Result", "More harm than good"], ["Reason removed", "WE CHECKED."]], highlight "Reason removed".

### 16 · meme · 8s
- **Visual:** Mel at the bus stop, looking at a phone, gives a small satisfied nod. Notifications stack in the corner.
- **On-screen:** wall "YOUR TOWN IS THE TRIAL." / toasts "Testing: new bus timetable" · "Measuring: buses that turn up" · "Stop if: the number drops" · "Ends: on a date. In writing."
- **Say:** "And when your town is the trial, you're told. What's being tested. The number that means stop. The date it ends. A public experiment, not a secret one."
- **Source:** canon pillar 3; research/14 (make the test public and give the reader a consequence). The bus timetable is a neutral example on purpose.
- **Layout:** `toasts` with `image` (Mel at the stop): wall {heading "YOUR TOWN IS THE TRIAL.", small "reported to: Mel"}, four toasts, reveal one per click.

### 17 · meme · 11s
- **Visual:** release notes with a red "BREAKING" banner. In the corner, the pencil on its string, with three pencils now tied to it.
- **On-screen:** "BREAKING CHANGES" / "'Trust me' is no longer a valid test result." / "Policies without a stop number will not install." / "A computer can summarise. A named person signs." / "One cross is now several crosses. Pencil: still on a string."
- **Say:** "Breaking changes. 'Trust me' is no longer a valid test result. Policies without a stop number will not install. A computer can summarise; a named person signs. And you now get several crosses. The pencil is still on a string. We're not animals."
- **Source:** canon framing, no new fact. "A named person signs" follows research/21 (AI summarises, never decides). This is the pencil callback's third and last appearance.
- **Layout:** `release`: title "Britain v2.0", heading "BREAKING CHANGES", lines (one per click) as on-screen, footer "These changes cannot be reverted by clicking 'remind me later'."

### 18 · meme · 13s
- **Visual:** a desktop that fills up with notifications from other people's projects, one per beat. Each comes with a small original picture of our own: a pothole with a bug flag in it, a jury summons addressed "RE: YOUR BIN COLLECTION", a highlighter on small print, a village-hall ballot box beside a bag marked "COUNCIL MONEY", a shelf of boxed experiments, an office door marked "DID IT WORK?".
- **On-screen:** wall "COMPATIBLE PLUGINS" / small "other people are already rethinking this" / six toasts (names and URLs as plain text, no logos)
- **Say:** "You don't have to wait for us. Other people are already writing this update. FixMyStreet. Sortition Foundation. TheyWorkForYou. PB Scotland. Participedia, with thousands of experiments. The What Works Network. Links below. Go and look."
- **Source:** explore-directory.md, checked live 2026-11-05 (ledger OK, dates and counts perishable): fixmystreet.com, sortitionfoundation.org, theyworkforyou.com, pbscotland.scot, participedia.net ("thousands", not 2,442), gov.uk/guidance/what-works-network. small-ideas.org is left OUT (GATE).
- **Layout:** `toasts`: wall {heading "COMPATIBLE PLUGINS", small "other people are already rethinking this"}, toasts [{title "FixMyStreet", text "The country finally has a bug tracker. The bug is the pothole."}, {title "Sortition Foundation", text "Jury service, but for the bin collection."}, {title "TheyWorkForYou", text "How your MP actually voted. Someone read the small print."}, {title "PB Scotland", text "A village hall, a ballot box, the council's actual money."}, {title "Participedia", text "Thousands of democratic experiments. Somebody said nobody had tried."}, {title "What Works Network", text "Nine centres that check what works. Free to read."}], reveal one per click.

### 19 · meme · 9s
- **Visual:** one last system dialog in the middle of the desktop. Mel's cursor moves from "Remind me in 5 years" across to "Update now". On the click, the taskbar clock flips from 1872 to today's date for the first time in the deck.
- **On-screen:** "Britain v2.0 is ready to install." buttons "Update now" / "Remind me in 5 years"
- **Say:** "Where I'm from, everybody clicked 'remind me later'. Every single time. I'm the reminder."
- **Source:** canon (narrator from the future; the bad branch is finished, research/01-canon.md). FLAG: "5 years" is a button label, not a claim, but it leans on the CHECK item "five-year maximum". If parliament.uk isn't checked first, use "Remind me after the next election".
- **Layout:** `dialog`: title "Britain Update", icon `question`, heading "Britain v2.0 is ready to install.", text "Mel has reviewed the release notes.", buttons ["Update now", "Remind me in 5 years"]; on the last step `clock` changes from "1872" to today. `bottom` (revealed on that step) "FUTURE PROOF. go and look."

---

**Total: 19 slides, 196s scripted (3:16). Three diagrams (timeline, pub, letters), each one followed at once by a meme.**
To get to about 180s, cut slide 13 (the sandbox fact, -9s) and slide 16 (Mel is told, -8s), giving 17 slides and 179s.

Used from v2: slides 3, 13, 24, 27, 28, the tickets idea (23), "works on my machine" (18) and the montage lines (41, 42, 45, 49, 51, 53). Dropped as CHECK, GATE or CUT-IF: five years / 2029 as spoken facts, "your phone is nineteen", public voting before 1872, Frome, the poll tax, sewage, small-ideas.org, Horizon.
