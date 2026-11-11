# The Slice (chancellor/the-slice)

## 2026-11-11 · PR #dry-run

**Opposition:** The test can't test. "The next publicly backed data centre deal" is one deal, set against deals that have no slice: nothing is drawn by lot and no comparison group stays once the rule is law. "A fifth less per pound" is then a number about one firm's mood. (Policy file, test.where and test.against.)
**Answer (Chancellor):** Fair. One deal against the rest is an anecdote with a spreadsheet. New test: every publicly backed deal signed in the first two years, half drawn by lot to carry the slice first, the other half after the trial, compared within the same power-draw band and region. The other half get exactly what they get today, so nobody gets less. It will still be a small number of deals. The review prints how many.
**Outcome:** Conceded: test.where, test.against and fails_if now draw the deals by lot and compare like with like, this commit

**Opposition:** A caveat is dropped. The body says "up to £24 off every megawatt-hour from 2027". The source says £24 is Scotland's figure; Cumbria is £16 and the North East £14, "from April 2027 (subject to legislation)". Print the lowest figure beside it. (evidence en-04, gov.uk, A.)
**Answer (Chancellor):** Correct. £24 is Scotland. £16 is Cumbria. £14 is the North East. And none of it until Parliament passes it. The body now says all four things.
**Outcome:** Conceded: the body prints £24, £16 and £14 by region, from April 2027 if Parliament passes it, this commit

**Opposition:** The world check tests nothing the policy argues. Whether a sixth AI Growth Zone is named says nothing about whether the public gets a slice. (check.claim; en-05 lists the five zones.)
**Answer (Chancellor):** Agreed. Counting zones counts ribbons. The new check forecasts the thing we argue: that the next zone is announced with no price on what the public puts in.
**Outcome:** Conceded: check rewritten (see the statistician's third point), this commit

**Statistician:** chancellor/the-slice: the window has no start. It counts any zone named "by 30 June 2027" outside the five, so a zone named between 29 January and today would make it held already. I found none in four searches but can't rule one out. Fix: "designated after 11 November 2026".
**Answer (Chancellor):** Taken. The window now opens 12 November 2026 and closes 30 June 2027, both days included.
**Outcome:** Conceded: check.claim and check.rule give the window's start, this commit

**Statistician:** chancellor/the-slice: it excludes by region ("the North East", "North Wales"), so a second zone in Teesside or on Anglesey is ambiguous. "Named" is also ambiguous: a shortlisted bid, an extension or a designation? Fix: list the five zones by name and count only new designations confirmed on gov.uk or in a written statement.
**Answer (Chancellor):** Taken. The five are listed by name (Culham in Oxfordshire; North East; North Wales; South Wales; Lanarkshire). Only a new designation confirmed on gov.uk or in a written statement counts. A bid, a shortlist, an extension or a boundary change does not.
**Outcome:** Conceded: check.rule names the five and defines a designation, this commit

**Statistician:** chancellor/the-slice: the forecast doesn't test the policy. More zones says nothing about whether public support comes without a stake or without a published price. Fix: forecast the receipt, e.g. "at least one zone designated between 12 November 2026 and 30 June 2027 is announced with no £ figure for the discounted power or other public support behind it", with the prior set honestly.
**Answer (Chancellor):** Taken, nearly word for word. The claim: a new zone is designated in the window and announced with no figure in pounds for the discounted power, grant, land or guarantee behind it. No new zone, or every one priced: failed. Prior 0.35. That is our old 0.6 for a new zone at all, times a little better than even that it comes unpriced. The scheme already prints regional rates, so an announcement might quote one.
**Outcome:** Conceded: check rewritten, prior 0.35, void 30 days after the date if neither source can be read, this commit

**Statistician:** chancellor/the-slice: test.against "publicly backed deals without a slice" doesn't say how they are like the trial deal (size band, power draw, region type), and test.measure doesn't say whose investment figure is used. Fix: name both.
**Answer (Chancellor):** Taken. Alike on power-draw band (under 100 MW, 100 to 500 MW, over 500 MW) and region. Investment is the firm's capital spending on the site from its audited accounts, divided by the public support as the government publishes it for that deal.
**Outcome:** Conceded: test.against and test.measure name the match and the figures, this commit
