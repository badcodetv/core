# Future Proof v3 draft: THE SUPPORT CALL

**Pitch.** Mel phones Britain's technical support with one question and gets the full treatment: hold music since 1872, "have you tried turning it off and on again?", a ticket closed as "working as designed".
The narrator from the future is the senior engineer the call finally gets escalated to; the three pillars are three support tickets, each one opened by Mel, marked "WORKING AS DESIGNED", explained, and RESOLVED.
The running gag is the support script itself (hold, the reboot question, "working as designed", "remind me later"), and it pays off at the end: the ticket stays open with the status "WAITING ON CUSTOMER", and somebody else has had the mouse since 1872.

Shape rules this draft keeps: every ticket has the same three beats (opened → mechanism → resolved), so the audience knows the pattern by ticket two and can laugh ahead of it. "Working as designed" is said three times, and turns on the third: "that's the bug" is the joke of ticket one, and the line that blames the designers, never Mel. Mel is always the calm, reasonable caller; support is the joke. Narrator "from the future" is used three times (3, 17, 20).

---

### 1 · meme · 9s
- **Visual:** Mel at the kitchen table, phone on speaker, mug in hand, dog asleep on Mel's foot. Calm. Waiting.
- **On-screen:** chat bubble from Mel "Why can't I vote on more than one thing?" / reply "Your call is important to us. It has been since 1872."
- **Say:** "Why can't I vote on more than one thing? Mel asked. Mel was put on hold. Your call is important to us. It has been since 1872."
- **Source:** framing. Secret ballot 1872 (ledger: research/15, https://en.wikipedia.org/wiki/Reform_Acts, OK). The clock date is the deck's look, not a claim.
- **Layout:** `dialog` titled "Britain Support: Live Chat", icon `info`, Mel's question as the heading, the hold reply as `text`, a `progress` bar "Position in queue: 1 of everyone" stuck at 3%, buttons "Keep holding" / "Keep holding", Mel's photo as the `image`.

### 2 · meme · 10s
- **Visual:** none beyond the window; the cursor hovers between the two buttons.
- **On-screen:** "HAVE YOU TRIED TURNING IT OFF AND ON AGAIN?" / Mel: "We only get to do that every five years." / Support: "Brilliant. So it's working."
- **Say:** "First line support. Have you tried turning it off and on again? Mel says: we only get to do that every five years. Support says: brilliant. So it's working. Ticket closed."
- **Source:** framing. "Every five years" is the five-year maximum term: ledger status **CHECK** (parliament.uk, Dissolution and Calling of Parliament Act 2022). Verify before print; fallback line, true without a number: "We only get to do that once a parliament."
- **Layout:** `dialog` titled "First Line Support", icon `question`, heading "Have you tried turning it off and on again?", the exchange revealed line by line (`reveal`), final small text "Ticket #000 closed: working as designed", buttons "Restart now" (greyed) / "Remind me in 5 years" (default).

### 3 · title · 9s
- **Visual:** a boot screen; a small phone icon with a line running off the right edge of the screen.
- **On-screen:** "CALL ESCALATED" / "connecting you to: SENIOR ENGINEER (location: the future)"
- **Say:** "Mel reopened the ticket. It got escalated. A long way. Hi. Senior engineer. I'm calling from the future, where we kept this system right to the end. I know how this fault ends. Let's not."
- **Source:** canon framing (the narrator from the future, docs/voice.md; bad branch finished, research/01-canon.md, OK).
- **Layout:** `title`, heading "CALL ESCALATED", sub "Connecting you to: Senior Engineer. Location: the future.", `progress` {pct 3, label "Transferring call across time..."}.

### 4 · meme · 10s
- **Visual:** a System Information window; the last line is greyed out.
- **On-screen:** "Parliament: 1200s . Reform Act: 1832 . Secret ballot: 1872 . Light bulb: 1878 (not yet installed)" / bottom "YOUR VOTING SYSTEM IS OLDER THAN THE LIGHT BULB."
- **Say:** "First, system info. Parliament: the 1200s. The Reform Act: 1832. The secret ballot: 1872. The light bulb: 1878. The way you pick a government is older than the light bulb."
- **Source:** ledger OK: 1265 de Montfort (research/15, https://www.parliament.uk/demontfort/; say "1200s"); 1832 and 1872 (https://en.wikipedia.org/wiki/Reform_Acts); Swan lamp Dec 1878 (https://gracesguide.co.uk/Electric_Lighting). Never "before electricity". The timeline diagram is NOT used: this draft spends its three diagrams one per pillar.
- **Layout:** `release` titled "System Information", heading "Britain (build 1872)", `lines` as `[key, value]` pairs revealed one per click, the light-bulb row greyed "not yet installed", `bottom` caption "OLDER THAN THE LIGHT BULB".

### 5 · meme · 9s
- **Visual:** the "Remind me later" button is worn shiny, the "Install" button still has dust on it.
- **On-screen:** "UPDATE AVAILABLE. Requirements: 1 pencil. Known issues: all of them." / buttons "Remind me later" (worn) / "Install"
- **Say:** "Requirements: one pencil. Known issues: all of them. And for over a hundred and fifty years, somebody has clicked 'remind me later'. Not Mel. The people whose job was to click install."
- **Source:** framing; "over 150 years" is 1872 to 2026 (ledger: "over 150 years" is the allowed wording). Blame lands on the people who had the decision, by their act.
- **Layout:** `dialog` titled "Britain Update", icon `warn`, heading "An update is available", text "Requirements: 1 pencil. Known issues: all of them.", small "Last checked: 1872", buttons "Remind me later" (default, outlined, rubbed shiny) / "Install".

### TICKET #001: COMPOSITION OVER INHERITANCE

### 6 · meme · 10s
- **Visual:** Mel at a bus stop, holding up a till receipt that runs down to the pavement.
- **On-screen:** "TICKET #001: Can't vote on one thing." Wanted: the bus. Got: the bus + the whole bundle. Duration: 5 years. Can I take the pickles off: no. STATUS: WORKING AS DESIGNED.
- **Say:** "Ticket one. Mel wants the bus. Mel gets the bus, and everything else in the bundle, for five years. Can I take the pickles off? No. Status: working as designed."
- **Source:** analogy (research/12, the till / meal deal), no stat. "Five years" as slide 2 (CHECK; fallback "until next time").
- **Layout:** `ticket` titled "Ticket #001", heading "Can't vote on one thing", `fields` [["Wanted","the bus"],["Got","the bus + the whole bundle"],["Can I take the pickles off","no"],["Status","WORKING AS DESIGNED"]], `highlight` "Status", Mel-with-receipt as `image`.

### 7 · diagram (three.js) · 16s
- **Visual:** the `pub` scene. Five people at a pub table, Mel one of them. Sun party's three policy cards above. Phase 1: each card loses 3-2. Phase 2: everyone slides into party stacks; Sun party wins 3-2.
- **On-screen:** phase 1 "EVERY POLICY LOSES 3-2." / phase 2 "THE PARTY WINS 3-2." / tag "same five people. same pints."
- **Say:** "Here's what the bundle does. Five people in a pub. The Sun party has three policies. Vote on each one: every single one loses, three-two. Vote for the party: the Sun party wins, three-two. Same people. Same pints. Only the ballot changed."
- **Source:** ledger OK: Ostrogorski paradox (https://www.newamerica.org/insights/the-paradoxical-reason-republicans-win-elections-despite-unpopular-policies/ ; https://arxiv.org/abs/2307.11873v1); the worked example is ours, hand-checked in v2 slide 13. Invented parties only.
- **Layout:** `diagram`, scene `pub`, title "Diagnostics: ballot.exe", caption "RUNNING DIAGNOSTIC...", small "same five people. same pints.", steps 2.

### 8 · meme · 8s
- **Visual:** split screen. Left: the ballot box, a speech bubble. Right: Mel, a thought bubble with a bus in it.
- **On-screen:** left "THE BOX HEARD: 'ALL OF IT.'" / right "MEL SAID: 'THE BUS.'" / bottom "IT'S WORKING EXACTLY AS DESIGNED. THAT'S THE BUG."
- **Say:** "Mel votes for the bus. The box hears: all of it. And support is right. It's working exactly as designed. That's the bug."
- **Source:** lands slide 7; no fact. The bug is the design, so the designer is the target, never Mel.
- **Layout:** `split`, left window "ballot_box.log" with heading "Input received: ALL OF IT", right window "mel.txt" with heading "the bus", `bottom` caption revealed on the last click.

### 9 · meme · 9s
- **Visual:** a half-and-half pizza in a small picture inside the dialog.
- **On-screen:** "TICKET #001: RESOLVED. Fix: vote issue by issue." small "(engineers: composition over inheritance. everyone else: half and half.)"
- **Say:** "Fix: vote on things one at a time. Software calls it composition over inheritance. You know it as half and half. If a pizza can manage it, so can a country."
- **Source:** canon pillar 1 (research/01-canon.md); jargon arrives after the picture (research/04). Pizza analogy research/12.
- **Layout:** `dialog` titled "Ticket #001", icon `ok`, heading "RESOLVED: vote issue by issue", small "composition over inheritance (it's pizza)", pizza `image`, buttons "Apply fix" (default) / "Remind me later".

### TICKET #002: CONTINUOUS INTEGRATION

### 10 · meme · 11s
- **Visual:** a ticket window over a picture of a presenter pointing at a tiny model village while the real town looms behind.
- **On-screen:** "TICKET #002: New rule installed on everyone at once." Tested on: the briefing room. Undo: a review in 3-5 years. Who counts the reviews: nobody centrally. STATUS: WORKING AS DESIGNED.
- **Say:** "Ticket two. A new rule goes out to everyone at once. Tested on: the briefing room. Undo: a review, three to five years later. Who counts the reviews? The Lords was told: there's no central record. Status: working as designed."
- **Source:** ledger OK: Acts normally reviewed 3-5 years after enactment (https://www.wfd.org/what-we-do/resources/post-legislative-scrutiny-uk-parliament); no central record of reviews (Lords written answer, https://parallelparliament.co.uk/question/HL2377/legislation-parliamentary-scrutiny). Do not claim a count of unreviewed Acts.
- **Layout:** `ticket` titled "Ticket #002", heading "Installed on everyone at once", `fields` [["Tested on","the briefing room"],["Undo","review in 3-5 years"],["Who counts the reviews","no central record"],["Status","WORKING AS DESIGNED"]], `highlight` "Undo", presenter picture as `image`.

### 11 · diagram (three.js) · 15s
- **Visual:** the `tower` scene. Left: small bricks, each lands and ticks green; one goes red and the undo arm lifts it out, tower stands. Right: a crane drops one monolith; no ticks.
- **On-screen:** left "SMALL. CHECKED. UNDOABLE." / right "ONE DROP. NO TICKS."
- **Say:** "Software does it the other way. Small pieces. Check each one. One breaks, undo it, the tower stays up. Not move fast and break things. Move small, and be able to take it back. Politics drops the whole tower off a crane."
- **Source:** ledger OK: the green-tick explanation, research/13 section 1 (explanatory). No deploy-rate number. "Not move fast and break things" is said aloud (trap guard).
- **Layout:** `diagram`, scene `tower`, title "Compare builds", caption "build A vs build B", small "move small. check. undo.", steps 2.

### 12 · meme · 7s
- **Visual:** an error box over a statute book with a sticky note on its cover.
- **On-screen:** "CTRL+Z IS NOT AVAILABLE FOR THIS LAW." small "Try again in 3-5 years." buttons "OK" / "Also OK"
- **Say:** "Every app on your phone has undo. The law says: try again in three to five years. Both buttons say OK."
- **Source:** same review fact as slide 10 (OK). The two-bad-buttons joke is the look's grammar.
- **Layout:** `dialog` titled "Undo", icon `error`, heading "Ctrl+Z is not available for this law", small "Try again in 3-5 years", buttons "OK" (default) / "Also OK".

### 13 · meme · 7s
- **Visual:** none; a green tick.
- **On-screen:** "TICKET #002: RESOLVED. Change small. Check it. Keep an undo."
- **Say:** "Fix: change small. Check it. Keep an undo. Software calls it continuous integration. You'd call it common sense, if common sense came with a button."
- **Source:** canon pillar 2 (research/01-canon.md). The straight care beat after the diagnosis jokes (voice.md).
- **Layout:** `card` "Tip of the day", icon `ok`, heading "Ticket #002: RESOLVED", `lines` "Change small." / "Check it." / "Keep an undo." one per click.

### TICKET #003: DATA-DRIVEN

### 14 · meme · 9s
- **Visual:** a ticket with two pictures pinned to it: a pill bottle with a "CONTROL GROUP" sign; a megaphone.
- **On-screen:** "TICKET #003: Feature shipped without testing." A pill gets: a trial with a control group. A policy gets: a confident announcement. How will we know: ???. STATUS: WORKING AS DESIGNED.
- **Say:** "Ticket three. A pill gets a trial with a control group. A policy gets a confident announcement. How will we know it worked? Status: working as designed."
- **Source:** ledger OK: RCTs routine in medicine, rare in domestic policy, "Test, Learn, Adapt" (https://www.gov.uk/government/publications/test-learn-adapt-developing-public-policy-with-randomised-controlled-trials).
- **Layout:** `ticket` titled "Ticket #003", heading "Shipped without testing", `fields` [["A pill gets","a control group"],["A policy gets","a confident announcement"],["How will we know","???"],["Status","WORKING AS DESIGNED"]], `highlight` "How will we know".

### 15 · diagram (three.js) · 15s
- **Visual:** the `letters` scene. Two envelopes fan out; two bars rise: plain letter 67.5%, the postcode line 79%.
- **On-screen:** "SAME LETTER, ONE EXTRA LINE: 67.5% → 79% PAID." small "HMRC, overdue tax"
- **Say:** "Here's a test that worked. HMRC tried versions of one letter to people who owed tax. The plain letter: sixty-seven and a half percent paid. Add one line, most people in your postcode have already paid: seventy-nine. Nobody passed a law. They tested a sentence."
- **Source:** ledger OK for 67.5 vs 79 only (https://thedecisionlab.com/intervention/how-normative-messaging-increased-tax-compliance-by-15 ; https://blogs.worldbank.org/voices/ongoing-impact-nudging-people-pay-their-taxes). No "eleven versions", no "best of", no sample size, no £160m.
- **Layout:** `diagram`, scene `letters`, title "A/B test: letter.doc", caption "TESTING ONE SENTENCE", small "HMRC, overdue tax", steps 2.

### 16 · meme · 10s
- **Visual:** a coach of teenagers pulling up to a prison gate, a green "SOUNDS GREAT" stamp on the picture; on the next click a red stamp over it.
- **On-screen:** top "SOUNDED GREAT." / bottom "RESULT: MORE REOFFENDING." / side box "Common sense is a hypothesis."
- **Say:** "And tests cut both ways. Scared Straight: take teenagers to meet prisoners, scare them off crime. People were sure. Nine controlled trials later: it made reoffending worse. Common sense is a hypothesis."
- **Source:** ledger OK: Campbell review, Petrosino et al. 2013, nine randomised studies, harmful effect (https://ideas.repec.org/a/wly/camsys/v9y2013i1p1-55.html). No date for the programme (unsourced). Neutral: the test kills a "tough" idea, the viewer of every side is kept.
- **Layout:** `picture` titled "scared_straight_final_FINAL.jpg", `top` "SOUNDED GREAT.", `bottom` "RESULT: MORE REOFFENDING." revealed on click 1, `side` {title "Hypothesis.exe", icon `warn`, text "Common sense is a hypothesis.", buttons "Test it" / "Announce it anyway"}.

### 17 · meme · 9s
- **Visual:** Mel at the bus stop reading a notice pinned up: "YOUR TOWN IS THE TRIAL. WE ARE MEASURING: ___. THE NUMBER THAT MEANS STOP: ___." Mel nods.
- **On-screen:** "TICKET #003: RESOLVED. No policy without its experiment." small "1 trial town . 1 number that means stop . the town gets told"
- **Say:** "Fix: no policy without its experiment. A trial town, a number that means stop, and the town gets told. Where I'm from, we call that data-driven. We also call it: obviously."
- **Source:** canon pillar 3 (research/01-canon.md; research/14: the method is the hero; public, never secret). No fact asserted. Narrator "from the future" use 2 of 3.
- **Layout:** `dialog` titled "Ticket #003", icon `ok`, heading "RESOLVED: no policy without its experiment", small "1 trial town . 1 number that means stop . the town gets told", Mel-at-notice as `image`, buttons "Apply fix" (default) / "Remind me later".

### CLOSE

### 18 · meme · 10s
- **Visual:** the desktop wallpaper; notifications stack one per click, each with a tiny picture of our own (pothole with a flag, jury envelope "RE: YOUR BIN COLLECTION", a village-hall ballot box, a highlighter on small print, a river with a little bridge, a shelf of boxes).
- **On-screen:** wall "6 OTHER ENGINEERS ARE ALREADY ON THIS TICKET" / toasts: "FixMyStreet . fixmystreet.com . Somebody gave the country a bug tracker. The bug is the pothole." / "Sortition Foundation . sortitionfoundation.org . Jury service, but for the bins." / "PB Scotland . pbscotland.scot . A village hall, a ballot box, real council money." / "TheyWorkForYou . theyworkforyou.com . How your MP voted, issue by issue." / "Pol.is . pol.is . Where the other side secretly agrees with you." / "Participedia . participedia.net . Thousands of democratic experiments, worldwide."
- **Say:** "Good news. You're not the only caller. Other people are already rethinking this, mostly for free. Pause it. Open a tab. Go and look."
- **Source:** explore-directory.md #6, #2, #3, #9, #14, #13 (checked live 2026-11-05; ledger OK, counts perishable, so "thousands" not 2,442). small-ideas.org left out (GATE). No logos, names and URLs as plain text. The other nine sit in the video description and on the web version.
- **Layout:** `toasts`, `wall` {heading "6 other engineers are already on this ticket", small "go and look"}, six `toasts` brought on one per click (`reveal: {}`), each {title: name . url, text: the one line}.

### 19 · meme · 7s
- **Visual:** a five-star rating box; Mel's cursor over the stars, one eyebrow up.
- **On-screen:** "HOW WOULD YOU RATE YOUR COUNTRY TODAY? ☆☆☆☆☆" small "(next survey: 5 years)"
- **Say:** "Before you go, a quick survey. How would you rate your country today? Don't worry. They'll ask again in five years."
- **Source:** callback to slide 2; framing only. "Five years" as slide 2 (CHECK; fallback small "(next survey: whenever we feel like it)"). The joke is the survey's design.
- **Layout:** `dialog` titled "Customer Satisfaction", icon `question`, heading "How would you rate your country today?", five stars, small "Next survey: in 5 years", buttons "Submit" / "Remind me later".

### 20 · title · 9s
- **Visual:** the update box from slide 5 again, same dust, same shiny button. On the last click the "Remind me later" button is struck through and the taskbar clock flips from 1872 to today.
- **On-screen:** "FUTURE PROOF" / "Ticket status: WAITING ON CUSTOMER" / "Somebody's had the mouse since 1872. Ask for a go."
- **Say:** "That's my bit done. Your ticket stays open. Status: waiting on customer. That's you. Somebody's had the mouse since 1872. Ask for a go."
- **Source:** canon (the good branch is unwritten, research/01-canon.md); callback to slides 1 and 5. Narrator use 3 of 3 is implicit ("my bit"). badcode.tv/future-proof NOT printed (deployment unverified).
- **Layout:** `dialog` (or `title` boot screen) titled "Britain Update", icon `info`, heading "FUTURE PROOF", text "Ticket status: WAITING ON CUSTOMER", small "Somebody's had the mouse since 1872. Ask for a go.", buttons "Install" (default) / "Remind me later" (struck through on click 2), `clock` override from "1872" to the current time on the final click (the one deliberate clock gag).

---

**Total: 20 slides, 3 diagrams (pub, tower, letters), 1 title-boot, 16 memes. 9+10+9+10+9+10+16+8+9+11+15+7+7+9+15+10+9+10+7+9 = 199 seconds (3:19).**

To get under 3:00 if needed: cut slide 19 (survey, -7s), fold slide 13 into slide 12's buttons ("OK" / "Change small, check it, keep an undo"), -7s, and trim slide 3 to "Hi. Senior engineer. Calling from the future. I know how this ends. Let's not." (-4s): 181s.

Flags:
- "Five years" (slides 2, 6, 19) is ledger **CHECK**, not OK. The whole opening gag rests on it, so verify the five-year maximum on parliament.uk before this leaves draft. Fallback wording for each is given on the slide.
- Departures from v2: the light-bulb timeline is now a System Information meme, not a diagram, so each pillar keeps its own diagram (3 total). Frome, the poll tax, Horizon, petitions, Pol.is-in-Taiwan and the CTA "write one rule" are all cut for length; the close is "go and look", which the brief says is the close.
