# Deck v3: layouts and window text, for the dresser

Companion to `docs/stories/future-proof/slideshows/launch-talk/deck.md` (v3, 17 slides). For each slide this file gives the layout from `theme/LAYOUTS.md`, the window chrome and text, the click order (`reveal` / `steps`), the picture slot, and the draft each idea came from. Spoken lines live only in deck.md. Where a draft named a real product (for example standup's "Windows Update for Britain"), the title is changed to a neutral one, because the OS is made up.

**Global rules.**
- The taskbar clock reads `1872` on every slide except 17. Override it with `clock` only there.
- **The nag** is the same dialog every time: title "Update Available", icon `warn`, two buttons, with the bad one FIRST so it is the outlined default. Its long button grows at each pillar: 4 → 6 → 10. On 15 it is greyed, and on 17 it is struck through.
- **The 3% bar** is `progress {pct: 3, label: "Installing... (since 1872)"}` on 4. It moves to 4% on 17 and appears nowhere else. Slide 7's frozen bar shows no percentage and has `err: true`.
- No "Remind me in 5 years" anywhere. Do not use the `link` layout (its button rests on a CHECK fact).

---

### 1 · `dialog` (from standup 1, ruthless 1)
- title "Ballot.exe" · icon `error` · `image` {file "mel-booth.jpg", prompt "Mel in a polling booth, mug in hand, ballot with a single box printed EVERYTHING; dog outside with its lead on the hook"}
- heading "Why can't I vote on more than one thing?"
- text "You have selected **ONE (1)** cross.\nYour cross will now be applied to: **EVERYTHING**."
- buttons ["OK", "Also OK"]
- reveal {text: 1} · steps 1

### 2 · `release` (from installer 2, ruthless 2)
- title "About This System" · heading "Democracy, version 1872" · a small candle where the logo goes (image slot, optional)
- lines [["Parliament", "1200s"], ["Secret ballot", "1872"], ["Light bulb", "not invented yet (1878)"]], one per click
- footer "Known issues: all of them."
- buttons ["Remind me later", "Check for updates"]
- bottom "OLDER THAN THE LIGHT BULB." on the bulb line's click
- reveal {lines: 1, bottom: 3, footer: 3} · steps 3

### 3 · `split` (from patch-notes 4)
- left {title "lightbulb.exe", label "v1878 → today", image "smart bulb glowing, phone beside it", lines ["Dimmable", "16 million colours", "Talks to your phone"]}
- right {title "ballot.exe", label "v1872 → today", image "polling-booth shelf, a pencil tied on a string", lines ["Pencil", "String (added)"]}
- reveal {right: 1} · steps 1
- (optional `bottom` "CHANGELOG")

### 4 · `dialog` over a boot screen (installer 3 + 4, merged)
- behind (in the window text, or a second window if the theme allows): "DEMOCRACY 2.0 SETUP · 3 updates ready", with a cobweb in the corner of the bar
- title "Update Available" · icon `warn` · heading "Restart Britain to finish installing?"
- progress {pct: 3, label: "Installing... (since 1872)"}
- buttons ["Remind me later", "Restart now"]: "Restart now" greyed, with a padlock
- small "Only the administrator can install updates."
- sticky "who's the administrator?" (Mel's hand)
- reveal {sticky: 1} · steps 1
- (if one dialog can't hold all of it, split it into `title` 4a with the bar, then `dialog` 4b with the nag, and keep the timing)

### 5 · `diagram` (standup 7, installer 6)
- title "pub.sim" · scene `pub`
- caption step 1 "VOTE ON EACH POLICY: ALL THREE LOSE 3-2" · step 2 "VOTE FOR THE PARTY: SUN PARTY WINS 3-2"
- small "same five people. same opinions."
- steps 2

### 6 · `dialog` (ruthless 5 + customer-support 8 + installer 8)
- title "Your vote: cookie settings" · icon `info` · `image` {file "mel-ballot-banner.jpg", prompt "a cookie-consent banner across Mel's ballot paper, Mel in the corner, mug up, one eyebrow raised"}
- heading "We value your democracy."
- text "By voting, you accept all policies in this bundle, including the ones you can't stand."
- buttons ["Accept all", "Accept all"]
- small "Manage preferences (coming soon since 1872)", greyed, link style
- bottom "IT'S WORKING EXACTLY AS DESIGNED. THAT'S THE BUG." on click 1
- window (the nag, stacked on top) on click 2: {title "Update Available", icon `warn`, heading "Install 'Manage preferences'?", buttons ["Remind me after the next election", "Install"], small "Note: the next election is also a bundle."}
- sticky (optional) "software calls it composition over inheritance"
- reveal {bottom: 1, window: 2} · steps 2

### 7 · `dialog` (standup 9 + patch-notes 12)
- title "Parliament.exe" · icon `question` · `image` "one huge red button on an empty desk"
- heading "Apply this law to **EVERYONE, ALL AT ONCE**?"
- buttons ["Yes", "YES"]
- window on click 1: {title "Law Installer", icon `error`, text "Undo is not available for this action.", progress {pct: null, label: "Installing... please do not turn off your country.", err: true}, buttons ["OK"]}
- reveal {window: 1} · steps 1

### 8 · `diagram` (installer 10, standup 10)
- title "build.log" · scene `tower`
- caption left "SMALL. CHECKED. UNDOABLE." · right "ONE DROP. NO TICKS."
- small "one of these has an undo"
- steps 2 (left builds and reverts; right drops)

### 9 · `dialog` (ruthless 7, installer 11)
- title "Edit" · icon `warn` · `image` "keyboard with Ctrl and Z glowing beside a thick statute book with a sticky note: UNDO?"
- heading "Undo is not available for this law."
- text "Review: normally 3 to 5 years later."
- small "Central record of whether that happened: **none**."
- buttons ["We'll look into it", "OK"] on click 1
- (optional) progress {pct: 40, label: "Searching for the reviews..."}
- reveal {buttons: 1}, or show the buttons at once and put bottom "YOUR COUNTRY HAS 'WE'LL LOOK INTO IT'." on click 1 · steps 1

### 10 · `split` + nag (standup 12, installer 12)
- left {title "sandbox", heading "New money apps", text "A safe sandbox to test in first (since 2016)", image "bright room, TEST HERE FIRST banner, little boxes of app icons"}
- right {title "live", heading "Your bus timetable", text "Straight to live", image "Mel at a bus stop under a sign 14: DELAYED, timetable pinned to the post"}
- bottom "TESTED ON YOU." on click 1
- window (the nag) on click 2: {title "Update Available", icon `warn`, heading "Install 'test it first' everywhere?", buttons ["Remind me when it's someone else's problem", "Install"]}: the long button so wide it shoves "Install" against the window edge
- reveal {bottom: 1, window: 2} · steps 2
- The "14: DELAYED" sign must be readable: slide 17 pays it off.

### 11 · `split` (standup 13 + ruthless 9)
- left {title "pill.exe", heading "A PILL", lines ["Years of trials", "A control group"], buttons ["Prescribe"], image "pill bottle trailing a long paper trial record, CONTROL GROUP sign"}
- right {title "policy.exe", heading "A POLICY", text "A confident announcement.", buttons ["Run on everyone", "Run on everyone"], image "microphone on an empty lectern under a TRUST US banner, nobody at it"}
- bottom (small print style if the theme allows, otherwise the bottom caption) "Side effects may include: all of us." on click 1
- reveal {bottom: 1} · steps 1

### 12 · `diagram` (installer 14, ruthless 8)
- title "letters.xls" · scene `letters`
- caption "SAME LETTER, ONE EXTRA LINE: 67.5% → 79% PAID"
- small "HMRC, overdue tax"
- tag on the tall bar: "most people in your postcode have already paid"
- steps 2

### 13 · `dialog` (standup 16)
- title "Letter from the taxman" · icon `info` · `image` {file "mel-doormat.jpg", prompt "Mel on the doormat opening a brown envelope, dog looking up at it"}
- heading "Most people in your postcode have already paid."
- buttons ["Pay", "Move house"] on click 1
- bottom "PEER PRESSURE. NOW EVIDENCE-BASED." on click 1
- reveal {buttons: 1, bottom: 1} · steps 1

### 14 · `release` (installer 16 + standup 17)
- title "Release notes" · heading "DEMOCRACY 2.0: what's new"
- lines ["1. Vote issue by issue, not one bundle.", "2. Change laws small. Check them. Keep an undo.", "3. No policy without its experiment."], one per click
- footer "Download size: smaller than one manifesto." on click 4
- buttons ["Install", "Remind me later"]
- reveal {lines: 1, footer: 4} · steps 4

### 15 · `dialog` (installer 17)
- title "Update Available" · icon `warn` · heading "Remind me later?"
- small "You have used all your laters. (154 years of them.)"
- buttons ["Install now", "Remind me later"]: "Install now" is the outlined default for the first time, and "Remind me later" is greyed
- sticky (as a toast if the theme has no toast in `dialog`) "Reminder from: later. It's later." on click 1
- reveal {sticky: 1} · steps 1
- (Rejected alternative from standup 19: `fatal` code "LATER_HAS_ARRIVED", "I'm the error message." Use one turn, not both.)

### 16 · `toasts` (installer 18, ruthless 12)
- wall {heading "PARTIAL UPDATES FOUND NEARBY", small "other people are already rethinking this.\nthousands more: participedia.net"}
- toasts, one per click:
  1. {title "Sortition Foundation", text "jury service, but for the bin collection · sortitionfoundation.org"}
  2. {title "PB Scotland", text "the council's actual money, voted on in a village hall · pbscotland.scot"}
  3. {title "FixMyStreet", text "somebody gave the country a bug tracker · fixmystreet.com"}
  4. {title "TheyWorkForYou", text "how your MP voted, issue by issue · theyworkforyou.com"}
  5. {title "What Works Network", text "nine centres that check what works · gov.uk/guidance/what-works-network"}
  6. {title "Pol.is", text "in Taiwan, an argument about Uber went from four camps to two · pol.is"}
- reveal {} (each toast on its own click) · steps 6
- No logos. Names and URLs as plain text. small-ideas.org stays off.

### 17 · `title` + nag (standup 20 + installer 19 + mel-day 17)
- heading "DEMOCRACY 2.0"
- window (the nag): {title "Update Available", buttons ["Install now", "~~Remind me later~~"] with the second disabled and struck through, small "(button removed by the future)"}
- sticky "...me?" (Mel's hand; callback to slide 4)
- progress {pct: 3 → 4 on click 1, label: "Installing... (fastest it's moved since 1872)"}
- clock "1872" → "1873" on click 2 (the one deliberate clock override)
- one toast on click 3: {title "Bus 14", text "arriving (unrelated)"}
- steps 3
- Do not print `badcode.tv/future-proof` until it is live.

---

**Scenes used:** pub, tower, letters. **Not used:** timeline, slab, towns, pipe, dots, tokens; the files stay in `theme/scenes/` for the appendix or a long cut.

**New theme needs (check `layouts.js`):**
- a stacked second `window` on a `dialog` (slides 6, 7);
- a `window` on a `split` (10);
- a `progress` that steps from 3 to 4 on a click (17);
- a `clock` change on a given step (17);
- a single toast on `title` (17).

If any of these is missing, it is a small layout change, not a script change.
