# The cabinet's evidence file

Standing facts a minister may cite on a day with no news on its beat, grouped by post. Each line is
one fact: **id · fact · URL · grade · review by**.

**How the cabinet uses it.**

- A manifesto page or statement may state a fact about the world only if it is in today's
  `kind=news` memories or in an unexpired item here (shared section, "Facts").
- **Expired means unusable.** An item whose review-by date is before today may not be cited. List it
  in the minutes; the Cabinet Secretary refreshes or removes it on Sunday.
- **Grades.** A = primary (gov.uk, ONS, Bank of England, OBR, NHS England, Ofgem, legislation.gov.uk,
  Hansard, a regulator or an official international body). B = reputable secondary (major outlet,
  Commons Library, Full Fact, law firm, think tank, trade press). C = weak (one aggregator or blog):
  background only, **never printed**. A fact marked "reported" is printed as reported.
- Print the fact as worded, with its date or window ("1 January to 30 October 2026", "in August").
  Never round it, widen it or drop its caveat.
- Where today's news and an item disagree, the newer sourced figure wins; say so in the minutes.
- Cite the id (e.g. `home-06`) in the decision memory and the PR changelog, not on the page.
- A note in brackets after the URL says how to upgrade the source; until then the grade stands.

**Who may change it.** Only Kai or Jack (by a human PR or a push to the rolling branch) and the
Cabinet Secretary (its Sunday run, under its own rules). The cabinet never edits this file. First
filled 2026-11-05 from the manifesto-strategy fact check
(`design/2026-11-05-manifesto-strategy/factcheck/`).

---

## Prime Minister (`prime-minister`)

- `pm-01` · Since 5 Feb 2026, UK GDPR Art. 22 is replaced by Arts. 22A–22D (Data (Use and Access) Act 2025 s.80): significant solely automated decisions are allowed with safeguards (information, representations, human intervention, contest); special category data (including health) keeps the stricter rule. · https://www.legislation.gov.uk/ukpga/2025/18/section/80/enacted · A · review by 2027-05-05
- `pm-02` · The safeguards apply only to *solely* automated significant decisions; a decision a machine helped with, where a human is meaningfully involved, carries none of them. · https://www.gov.uk/guidance/data-use-and-access-act-2025-data-protection-and-privacy-changes · A · review by 2027-05-05
- `pm-03` · Texas's Sunset process has abolished 95 state agencies since 1977, 42 of them outright. · https://www.sunset.texas.gov/about-us · A · review by 2027-11-05
- `pm-04` · The Governor of the Bank of England must write an open letter to the Chancellor whenever CPI is more than 1 point from target, and every three months while it stays there. · https://www.gov.uk/government/collections/hmt-open-letters-between-the-governor-of-the-bank-of-england-and-the-chancellor-of-the-exchequer · A · review by 2027-05-05
- `pm-05` · A 2019 review, reported by the NAO in 2021, found only 8% of £432bn of major-project spending had robust evaluation plans. · https://www.civilserviceworld.com/news/article/most-government-projects-not-properly-evaluated-nao · B (the NAO report is A) · review by 2027-11-05
- `pm-06` · Australia's Robodebt has cost its government more than A$2.4bn in settlements; the second (up to A$548m) was approved in June 2026. · https://aapnews.aap.com.au/news/australia-s-biggest-class-action-settlement-approved · B · review by 2027-11-05

## Chancellor of the Exchequer (`chancellor`)

- `ch-01` · Bank Rate is 4%, raised 0.25 points on 5 Nov 2026 by 8–1; the one dissenter wanted 4.25%, not a hold. · https://www.bankofengland.co.uk/monetary-policy-summary-and-minutes/2026/november-2026 · A · review by 2026-12-10 (or the December MPC decision, if sooner)
- `ch-02` · CPI inflation was 3.5% in the year to September 2026, up from 3.1% in August; CPIH 3.6%. · https://www.ons.gov.uk/economy/inflationandpriceindices/bulletins/consumerpriceinflation/september2026 · A · review by 2026-11-18 (October CPI)
- `ch-03` · John Healey is Chancellor of the Exchequer (since 20 July 2026); his first Budget was 28 Oct 2026. · https://news.bgov.com/daily-tax-report-international/uk-chancellor-john-healey-to-deliver-first-budget-on-october-28 · B (upgrade to a gov.uk ministers page) · review by 2027-02-05 (or any reshuffle)
- `ch-04` · The fiscal rules are the stability rule (current budget balanced by 2029/30, ±0.5% of GDP) and the investment rule (PSNFL falling as a share of GDP in 2029/30); October 2026 headroom £15bn and £24bn; the welfare cap is forecast to be missed by £3bn in 2029/30. · https://www.instituteforgovernment.org.uk/explainers/fiscal-rules · B (upgrade to the OBR EFO) · review by 2027-03-31 (the spring fiscal event)
- `ch-05` · The 28 Oct 2026 Budget left income tax, NI and VAT rates unchanged; thresholds stay frozen to April 2031. · https://www.ii.co.uk/analysis-commentary/autumn-budget-2026-what-it-means-your-money-ii540710 · B (the threshold freeze: C, not printed until checked against the red book) · review by 2026-11-12
- `ch-06` · Employers pay 15% NI on pay above £5,000 a year (2026/27), and 0% up to £50,270 for under-21s and apprentices under 25; Employment Allowance £10,500. · https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2026-to-2027 · A · review by 2027-04-06
- `ch-07` · Companies can deduct 100% of new main-pool plant and machinery in year one (full expensing, permanent since Autumn Statement 2023). · https://www.gov.uk/government/publications/capital-allowances-permanent-full-expensing/capital-allowances-permanent-full-expensing-for-companies-investing-in-plant-and-machinery · A · review by 2026-11-12 (check against the Oct 2026 Budget documents)
- `ch-08` · The 2010–13 regional employer NI holiday for new firms reached about 25,000 businesses against 400,000 first claimed. · https://parallelparliament.co.uk/mp/david-mowat/debate/2013-11-04/commons/commons-chamber/national-insurance-contributions-bill (Hansard, Commons, 4 Nov 2013) · B (upgrade to an HMRC figure) · review by 2027-11-05
- `ch-09` · Electricity Generator Levy: 45% on generators' receipts above £75/MWh (CPI-indexed), first £10m exempt, CfD output excluded, biomass included; it ends 31 Mar 2028. · https://www.gov.uk/government/publications/electricity-generator-levy/electricity-generator-levy-on-exceptional-electricity-generation-receipts · A · review by 2027-03-31
- `ch-10` · Energy Profits Levy: 38% (78% headline), to 31 Mar 2030, or earlier if oil and gas both sit below the price floor for six months; then a permanent Oil and Gas Price Mechanism. · https://www.gov.uk/government/publications/uk-fossil-fuel-incentives-and-subsidies-inventory/uk-fossil-fuel-incentives-and-subsidies-inventory · A · review by 2027-03-31

## Foreign Secretary (`foreign`)

- `fo-01` · Hormuz: shipping collapsed from about 1 March 2026; partial reopenings and re-closures since; its status on 5 November is disputed. · https://www.aljazeera.com/news/2026/9/14/us-says-its-clearing-hormuz-traffic-why-are-oil-futures-beyond-100 · B · review by 2026-11-12
- `fo-02` · Brent crude peaked at $126.41 (30 Apr 2026) and traded at about $102–111 on 2–4 Nov 2026. · https://finance.biggo.com/news/c33d8ad5-88f7-41d0-9f74-6f05afb2e964 · C (swap for EIA or ICE; not printed until then) · review by 2026-11-12
- `fo-03` · IEA members that import oil must hold stocks equal to 90 days of net imports. · https://www.iea.org/about/oil-security-and-emergency-response · A · review by 2027-11-05
- `fo-04` · UK aid is being cut from 0.5% to 0.3% of GNI by 2027 to fund defence (announced 25 Feb 2025). · https://www.gov.uk/government/speeches/pm-statement-on-defence-25-february-2025 · A · review by 2027-12-31
- `fo-05` · The US and China (16 Nov 2024) affirmed that a human, not a machine, controls the decision to use nuclear weapons. · https://bidenwhitehouse.archives.gov/briefing-room/statements-releases/2024/11/16/readout-of-president-joe-bidens-meeting-with-president-xi-jinping-of-the-peoples-republic-of-china-3/ · A · review by 2027-11-05
- `fo-06` · Removing Huawei from UK 5G was put at up to £2bn and two to three years' delay (DCMS, 14 Jul 2020). · https://www.gov.uk/government/speeches/digital-culture-media-and-sport-secretarys-statement-on-telecoms · A · review by 2027-11-05

The UN review conference on autonomous weapons is `de-08`; Foreign cites it from there.

## Home Secretary (`home`)

- `home-01` · Net long-term migration was 171,000 in the year to December 2025 (provisional), down from 331,000 the year before; immigration 813,000, emigration 642,000. · https://www.ons.gov.uk/peoplepopulationandcommunity/populationandmigration/internationalmigration/bulletins/longterminternationalmigrationprovisional/yearendingdecember2025 · A · review by 2026-11-30 (next ONS release)
- `home-02` · The ONS publishes net migration twice a year (May and November); it is not a monthly series. · https://www.ons.gov.uk/peoplepopulationandcommunity/populationandmigration/internationalmigration/bulletins/longterminternationalmigrationprovisional/yearendingdecember2025 · A · review by 2027-05-31
- `home-03` · 21,869 people crossed the Channel in small boats between 1 January and 30 October 2026, 41% fewer than the 36,954 at the same point in 2025 (a PA count the same day had 21,198, 43% down). · https://asylumstats.co.uk/explained/how-many-small-boats-have-crossed-this-year/ · B (replace with the gov.uk daily series before print) · review by 2026-11-12
- `home-04` · Small-boat arrivals in January–June 2026 were 11,884, down 41% on 19,982 in January–June 2025. · https://www.wam.ae/en/article/c10ozxe-uk-channel-crossings-migrants-down-41-first-half (primary: the gov.uk small-boat time series) · B · review by 2026-11-30
- `home-05` · Small-boat arrivals in the year to June 2026 were 33,374, down 23% on the year to June 2025 (43,309); 41,472 crossed in 2025 as a whole. · https://www.gov.uk/government/statistics/immigration-system-statistics-year-ending-june-2026/how-many-people-come-to-the-uk-via-illegal-entry-routes · A · review by 2026-11-30 (next quarterly release)
- `home-06` · 40,168 people were awaiting an initial asylum decision at end June 2026, the lowest since June 2019 and 77% below the June 2023 peak. · https://www.gov.uk/government/statistics/immigration-system-statistics-year-ending-june-2026/how-many-people-are-in-the-uk-asylum-system · A · review by 2026-11-30
- `home-07` · 87,450 asylum and protection appeals were open at the First-tier Tribunal at end March 2026, up from 6,319 in June 2022: the backlog has moved to appeals. · https://www.gov.uk/government/statistics/immigration-system-statistics-year-ending-june-2026/how-many-people-are-in-the-uk-asylum-system (citing HMCTS) · A · review by 2026-12-31
- `home-08` · 16,021 people were in asylum hotels at end June 2026, 50% fewer than a year earlier and 71% below the September 2023 peak. · https://www.gov.uk/government/statistics/immigration-system-statistics-year-ending-june-2026/how-many-people-are-in-the-uk-asylum-system · A · review by 2026-11-30
- `home-09` · In the year to June 2026 there were 9,669 enforced returns (up 7%) and over 30,000 voluntary returns, the most in over ten years. · https://www.gov.uk/government/statistics/immigration-system-statistics-year-ending-june-2026/how-many-people-are-returned-from-the-uk · A · review by 2026-11-30
- `home-10` · The Migration Advisory Committee estimated that EU migration 1993–2017 was associated with UK-born nominal wages about 5% lower at the 5th percentile and about 4% higher at the 90th, a short-run effect it expects to fade; over the same period real wages at the 5th percentile rose 55%. · https://assets.publishing.service.gov.uk/media/5ba26c1de5274a54d5c39be2/Final_EEA_report.PDF · A · review by 2027-11-05
- `home-11` · The MAC's chair: the post-referendum fall in sterling "probably raised prices by 1.7 per cent", almost certainly more than the effect on residents' wages and jobs of all EEA migration since 2004 (over a different period). · https://assets.publishing.service.gov.uk/media/5ba26c1de5274a54d5c39be2/Final_EEA_report.PDF (foreword) · A · review by 2027-11-05
- `home-12` · The OBR's stylised sums (2024): a migrant arriving at 25 on about half the average wage costs the public finances more than they pay over a lifetime; one on the average wage pays in more, and more than a UK-born worker on the same pay. Order of magnitude, not a measure of actual flows. (Never "net-negative by their early 40s": false as worded.) · https://obr.uk/docs/dlm_uploads/FRS-migration-supplementary-forecast-information-release-Mar-2025.pdf · A · review by 2027-07-31 (next Fiscal Risks and Sustainability report)
- `home-13` · Linton-on-Ouse: the Home Office is considering the former RAF base for up to 1,200 single adult male asylum seekers; no final decision; North Yorkshire Council unanimously opposes it. · https://www.northyorks.gov.uk/news/2026/planned-use-ministry-defence-site-linton-ouse-home-office-single-adult-male-asylum-seekers · A · review by 2026-11-19 (live story)
- `home-14` · The Conservatives and Reform UK both say they would take the UK out of the ECHR; the Labour government says it will stay and seek to change how Articles 3 and 8 are applied. · https://www.lawsociety.ie/gazette/top-stories/2026/september/britain-will-stay-in-echr-says-minister/ and https://www.expressandstar.com/uk-news/conservatives-to-take-uk-out-of-echr-if-it-wins-election-badenoch-announces-5664573 · B · review by 2026-12-31
- `home-15` · The Fair Work Agency, a single labour-enforcement body merging minimum-wage enforcement, the GLAA and the Employment Agency Standards Inspectorate, started on 7 April 2026. · https://assets.publishing.service.gov.uk/media/696126a5d6532b76df7dcd75/fair-work-agency-factsheet.pdf · A · review by 2027-04-30
- `home-16` · Banks have had to refund authorised push-payment scam victims since 7 October 2024, split between sending and receiving bank, up to £85,000 a claim; in year one about £173m was refunded and in-scope losses fell about 21%. · https://www.regulationtomorrow.com/2026/07/payment-fraud-falls-by-73m-following-psr-reimbursement-scheme/ (upgrade to psr.org.uk) · B · review by 2027-01-31 (PSR consultation due December 2026)
- `home-17` · Platforms' Online Safety Act duty to tackle paid scam ads is not yet enforceable: Ofcom consulted on the codes until 2 October 2026 and decides in 2027. The duty is to prevent and remove, not to refund. · https://www.ofcom.org.uk/online-safety/online-fraud/consultation-fraudulent-advertising-code-of-practice · A · review by 2027-03-31
- `home-18` · Police live facial recognition has no dedicated statute; the Home Office consulted on a legal framework from 4 December 2025 to 12 February 2026 and, as of 5 November 2026, no response or bill was found. · https://www.gov.uk/government/consultations/legal-framework-for-using-facial-recognition-in-law-enforcement/consultation-on-a-new-legal-framework-for-law-enforcement-use-of-biometrics-facial-recognition-and-similar-technologies-accessible · A · review by 2026-12-31
- `home-19` · The January 2026 policing White Paper set aside about £26m for a national facial-recognition system and £11.6m for live facial recognition. · https://dwfgroup.com/en/news-and-insights/insights/2026/3/policing-at-the-ai-frontier-facial-recognition-is-here-to-stay · B · review by 2026-12-31

## Education (`education`)

- `ed-01` · Age discrimination, unlike other direct discrimination, can be justified as a proportionate means to a legitimate aim (Equality Act 2010 s.13(2)); acts required by an enactment are exempt (Sch. 22 para 1). · https://www.legislation.gov.uk/ukpga/2010/15/section/13 · A · review by 2027-11-05
- `ed-02` · 16–24 unemployment was 16.2% in February–April 2026. · https://www.ep-advisory.com/wp-content/uploads/2026/07/ep-briefing-youth-unemployment-uk-europe.pdf · B (replace with the ONS A06 table) · review by 2026-11-17
- `ed-03` · 981,000 young people (13.0% of 16–24s) were not in education, employment or training in April–June 2026. · https://youthfuturesfoundation.org/wp-content/uploads/2026/08/NEET-Trends-Analysis-2026-Q1.pdf · B (the ONS NEET bulletin is the A source) · review by 2026-11-30
- `ed-04` · Apprenticeship starts in England: 226,620 in August 2025–January 2026 (up 11.9%); only 110 were the new foundation apprenticeships. · https://explore-education-statistics.service.gov.uk/find-statistics/apprenticeships/2025-26 · A · review by 2026-12-05

## Defence (`defence`)

- `de-01` · UK defence: 3% of GDP by 2030 and NATO's 3.5% core by 2035, confirmed in the 28 Oct 2026 Budget; about 2.7% by 2027; the route is deferred to the 2027 Spending Review. · https://www.forcesnews.com/politics/govt-aims-spend-3-gdp-defence-2030-chancellor-says-not-everyones-convinced · B · review by 2027-06-30 (Spending Review)
- `de-02` · OBR: reaching 3% needs an extra £17.3bn in 2029-30. · https://www.lbc.co.uk/politics/uk-politics/budget-5bn-defence-investment-nato-ukraine/ (replace with the OBR EFO October 2026) · B · review by 2027-03-31
- `de-03` · NATO (The Hague, June 2025): 5% of GDP by 2035 = at least 3.5% core defence + up to 1.5% for resilience, critical infrastructure and civil preparedness; the trajectory is reviewed in 2029. · https://www.nato.int/cps/en/natohq/official_texts_236705.htm · A · review by 2029-06-30
- `de-04` · NATO estimate: UK defence spending was about 2.4% of GDP in 2025. · https://fullfact.org/news/uk-gdp-defence-spending/ · B · review by 2027-06-30 (next NATO estimates)
- `de-05` · The NCSC's chief executive: by 2028 it is highly likely attackers will use AI to exploit known weaknesses in the old technology running UK critical national infrastructure; 200+ such incidents in a year, about three in four linked to hostile states. · https://www.computerweekly.com/news/366644872/Hostile-states-launched-200-attacks-on-UK-infrastructure-in-five-months-says-NCSC-chief · B (upgrade to the ncsc.gov.uk speech text) · review by 2027-06-30
- `de-06` · UK military AI policy requires only "context-appropriate human involvement" in weapons with autonomous functions, and the UK is "unconvinced" by a new binding treaty. · https://docs-library.unoda.org/General_Assembly_First_Committee_-Seventy-Ninth_session_%282024%29/78-241-UK-EN.pdf · A · review by 2026-12-31
- `de-07` · Reported (FT, May 2026): the MoD is considering allowing lethal autonomous strikes without a human's final sign-off in exceptional cases. · https://article36.org/statements-updates/campaigners-say-uk-rejection-of-killer-robots-is-not-yet-watertight (find the FT URL before print) · B, reported · review by 2026-12-31
- `de-08` · The UN weapons convention's (CCW) Seventh Review Conference meets 16–20 Nov 2026 to take forward the autonomous-weapons "rolling text"; 70+ states back negotiations; the UN Secretary-General asked for a binding instrument by 2026. · https://disarmament.unoda.org/en/updates/briefing-chair-ccw-gge-laws-margins-first-committee · A · review by 2026-11-21 (the outcome)
- `de-09` · Recent attacks: Synnovis (London hospital blood tests, June 2024), M&S and Co-op (April–May 2025), and JLR, whose production halted about five weeks and which got a £1.5bn government loan guarantee (September 2025). · https://www.gov.uk/government/news/government-backs-jaguar-land-rover-with-15-billion-loan-guarantee · A · review by 2027-11-05

## Health (`health`)

- `he-01` · End of August 2026: 7.4m waits for planned hospital treatment in England (about 6.2m people), 113,339 over a year, median wait 12.2 weeks, 65.2% within 18 weeks against a 92% standard. · https://www.england.nhs.uk/statistics/wp-content/uploads/sites/2/2026/10/Aug26-RTT-statistical-press-notice-PDF-389K-vjgRdG.pdf · A · review by 2026-11-12 (September data)
- `he-02` · End of March 2026: 7.1m waits, 65.3% within 18 weeks (interim target 65%). · https://www.england.nhs.uk/statistics/wp-content/uploads/sites/2/2026/05/Mar26-RTT-statistical-press-notice-PDF-545K-Dc1i9U.pdf · A · review by 2027-05-05
- `he-03` · NHS England's planning framework (October 2025) directs providers to adopt AI note-takers (ambient voice technology) from 2026/27. · https://www.england.nhs.uk/wp-content/uploads/2025/10/medium-term-planning-framework-delivering-change-together-2026-27-to-2028-29.pdf · A · review by 2027-04-01
- `he-04` · MHRA (29 Jul 2026): an AI scribe is a medical device only if its intended purpose is medical; transcription-only tools are not regulated as devices. · https://www.england.nhs.uk/long-read/guidance-on-the-use-of-ai-enabled-ambient-scribing-products-in-health-and-care-settings/ · A · review by 2027-01-31
- `he-05` · The NHS Federated Data Platform contract (Palantir) has a break clause that can be used in February 2027; the government is reviewing whether to use it. · https://www.digitalhealth.net/2026/06/fdp-here-to-stay-says-patel-as-palantir-contract-faces-review/ · B · review by 2026-12-31
- `he-06` · £500m for the first Fair Pay Agreement for care workers, in force from 2028; the Casey Commission reports in summer 2027. · https://www.gov.uk/government/news/500m-for-first-ever-fair-pay-agreement-for-care-workers · A · review by 2027-06-30
- `he-07` · About 5 million unpaid carers in England and Wales (Census 2021). · https://www.ons.gov.uk/peoplepopulationandcommunity/healthandsocialcare/socialcare/bulletins/unpaidcareenglandandwales/census2021 · A · review by 2028-11-05

## Work and Pensions (`work-pensions`)

- `wp-01` · UK unemployment was 4.7% in June–August 2026; payrolled employees were down 111,000 on the year to August. · https://www.ons.gov.uk/employmentandlabourmarket/peopleinwork/employmentandemployeetypes/bulletins/uklabourmarket/october2026 · A · review by 2026-11-17
- `wp-02` · Universal Credit regulations can be piloted by area or group for up to three years (Welfare Reform Act 2012 s.41); the power covers UC, not PIP. · https://www.legislation.gov.uk/ukpga/2012/5/section/41 · A · review by 2027-05-05 (or any welfare bill that amends it)
- `wp-03` · The PIP four-point rule was removed from the UC and PIP Bill on 1 July 2025; PIP eligibility changes wait for the Timms Review, whose final recommendations are due autumn 2026. · https://www.gov.uk/government/news/first-comprehensive-review-into-pip-finds-it-is-not-fit-for-purpose · A · review by 2026-11-12 (weekly until the Timms final report is out)
- `wp-04` · New UC claimants since 6 April 2026 get a health element of £217.26 a month (about £50 a week), frozen for four years; existing claimants are protected. · https://www.gov.uk/government/news/government-reforms-welfare-system-to-support-people-into-work · A · review by 2027-04-06
- `wp-05` · Two in three (67%) PIP appeals decided at a tribunal hearing go the claimant's way (April–June 2026, the same as January–March). · https://www.gov.uk/government/statistics/tribunals-statistics-quarterly-april-to-june-2026/tribunal-statistics-quarterly-april-to-june-2026 · A · review by 2026-12-10 (next tribunal statistics)
- `wp-06` · A social-security appeal takes on average 37 weeks from lodging to decision (April–June 2026). · https://www.gov.uk/government/statistics/tribunals-statistics-quarterly-april-to-june-2026/tribunal-statistics-quarterly-april-to-june-2026 · A · review by 2026-12-10
- `wp-07` · A PIP mandatory reconsideration takes a median 45 days (July 2026); 26% change the award. · https://www.gov.uk/government/statistics/personal-independence-payment-statistics-to-july-2026/personal-independence-payment-statistics-to-july-2026 · A · review by 2026-12-10 (next PIP statistics)
- `wp-08` · Of all initial PIP decisions, 3% end up overturned at tribunal (April 2021–March 2026). Say it ourselves before an opponent does. · https://www.gov.uk/government/statistics/personal-independence-payment-statistics-to-july-2026/personal-independence-payment-statistics-to-july-2026 · A · review by 2026-12-10

Australia's Robodebt is `pm-06`; Work and Pensions cites it from there.

## Housing (`housing`)

- `ho-01` · Since 30 Apr 2024 (England), a compulsory purchase order for affordable housing, health or education may carry a direction that hope value is disregarded in compensation (LURA 2023 s.190, LCA 1961 s.14A); widened by the Planning and Infrastructure Act 2025. · https://legislation.gov.uk/ukpga/2023/55/section/190/enacted/data.pdf · A · review by 2027-02-05
- `ho-02` · Street votes are in LURA 2023 but have never been switched on; the government said in October 2025 no final decision had been taken. · https://parallelparliament.co.uk/question/HL9253/planning-permission-public-consultation · B · review by 2026-12-05
- `ho-03` · Councils may set local-connection rules for social housing, but since 10 Jul 2025 must exempt domestic-abuse victims who must move and care leavers under 25. · https://www.gov.uk/government/publications/improving-access-to-social-housing-for-victims-of-domestic-abuse/improving-access-to-social-housing-for-victims-of-domestic-abuse · A · review by 2027-05-05
- `ho-04` · The government counted about 437,900 net additional homes in England (an estimate including conversions) from 9 Jul 2024 to 20 Sep 2026: 29% of the 1.5m target. · https://fullfact.org/government-tracker/1-5-million-homes/ · B · review by 2026-12-05
- `ho-05` · In 2024-25 councils in England delivered 9,241 new social rent homes; housing associations 37,629. · https://www.gov.uk/government/statistics/social-housing-sales-and-demolitions-2024-25-england/social-housing-sales-and-demolitions-2024-25-net-supply-of-social-housing-for-rent · A · review by 2026-12-31
- `ho-06` · From 1945 to the late 1970s councils often built over 120,000 homes a year. · https://england.shelter.org.uk/professional_resources/policy_and_research/policy_library/briefing_the_slow_pace_of_social_rent_home_delivery · B · review by 2028-11-05

## Energy and Climate (`energy-climate`)

- `en-01` · Ofgem's cap for a typical dual-fuel household rose 4% to £1,723 a year for 1 October–31 December 2026, driven by Middle East gas prices. · https://www.ofgem.gov.uk/news/changes-energy-price-cap-between-1-october-and-31-december-2026 · A · review by 2026-11-25 (January cap announced)
- `en-02` · Standing charges October–December 2026: electricity 54.83p a day, gas 29.68p a day, about £307 a year before any energy is used. · https://www.ofgem.gov.uk/your-energy-supply/your-energy-bill/energy-price-cap-unit-rates-and-standing-charges · A · review by 2026-11-25
- `en-03` · VAT is off household electricity from 1 Oct 2026 to 31 Mar 2027; gas still carries 5%. · https://www.ofgem.gov.uk/news/changes-energy-price-cap-between-1-october-and-31-december-2026 · A · review by 2027-03-31
- `en-04` · AI Growth Zone data centres are to get power discounts from April 2027 (subject to legislation): for a 500 MW site up to £24/MWh in Scotland, £16 in Cumbria, £14 in the North East, up to £80m a year; the government says other bill payers bear no cost; the consultation closed 15 Apr 2026. · https://www.gov.uk/government/publications/delivering-ai-growth-zones/delivering-ai-growth-zones · A · review by 2026-12-31 (watch for the consultation response and the bill)
- `en-05` · The five AI Growth Zones: Culham/Oxfordshire, North East, North Wales, South Wales, Lanarkshire (29 Jan 2026). · https://questions-statements.parliament.uk/written-statements/1876468 · A · review by 2027-01-31
- `en-06` · Drax, Brookfield and Radiant (3 Nov 2026) announced a data centre of over 1 GW at Drax power station that "could exceed £20bn", 100 MW by 2028; not yet through planning; Drax's own AI Growth Zone bid was rejected. · https://www.theregister.com/on-prem/2026/11/03/drax-wants-to-feed-britains-ai-habit-with-20b-datacenter-at-biomass-power-station/5307237 · B · review by 2027-03-31
- `en-07` · Gas set GB wholesale power prices about 97% of the time in 2021. · https://www.ucl.ac.uk/news/2022/sep/gas-power-stations-set-price-electricity-97-time · B · review by 2027-11-05
- `en-08` · GB electricity distribution: 14 licence areas, 6 operator groups under 5 owners (CKI, National Grid, SSE, Iberdrola for both SP Energy Networks and Electricity North West, Berkshire Hathaway). · https://www.energynetworks.org/customers/find-my-network-operator · B · review by 2027-03-31
- `en-09` · Ireland: data centres used 21% of metered electricity in 2023 (CSO). · https://www.cso.ie/en/releasesandpublications/ep/p-dcmec/datacentresmeteredelectricityconsumption2023/ · A · review by 2027-07-31
- `en-10` · Homes within 500m of new pylons get up to £250 a year off bills for 10 years. · https://www.gov.uk/government/news/households-living-near-new-pylons-to-receive-up-to-2500-off-energy-bills · A · review by 2027-03-31

The generator levy and the Energy Profits Levy are `ch-09` and `ch-10` (the Windfall Act is the
Chancellor's); Energy cites them from there.
