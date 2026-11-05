# 11 - Pillar 1 precedent: composable / issue-by-issue democracy

Researched 2026-11-05, 6 web searches. Solidity: **P** primary, **S** secondary, **H** hearsay/unverified. Search snippets only; no page was opened in full, so treat every number as "re-check before it goes on a slide".

## Ranking for a UK lay audience (one slide each)

| Rank | Precedent | Why it works on a slide | Killer stat | Solidity |
|---|---|---|---|---|
| 1 | **Switzerland: vote per issue, several times a year** | The literal answer to "why can't I vote for more than one thing at a time?" No software needed, 177 years old. Tests the pillar directly. | Called to the ballot 332 times since 1848 (federal Chancellery); ~10 federal votes a year since 1991; in 1848-1900 about one a year. | S via search of admin.ch: https://www.admin.ch/gov/en/start/documentation/votes.html ; counts of proposals vary 617-689 by source, so quote the 332 "voting days" only. |
| 2 | **Ireland: citizens' assembly then referendum** | UK-adjacent, culturally familiar, a story with an ending. Randomly chosen citizens settled what politicians had dodged for 35 years. | Referendum 2018: 66.4% yes, turnout 64.1% (record for a referendum). Assembly met late 2016 to spring 2017, chaired by a judge. | S (BBC/Al Jazeera/Statista in results): https://www.aljazeera.com/news/2018/5/26/scenes-of-joy-as-ireland-votes-to-repeal-abortion-law . NB: the 66% is the referendum, not the assembly vote. Pick a less divisive Irish topic or the framing "the parties couldn't, strangers in a room could" to avoid a culture-war fight on the slide. |
| 3 | **vTaiwan + Pol.is** | Closest to Martin Lewis' small-ideas: lots of people, find what everyone already agrees on, feed to law. Pol.is rewards consensus, not shouting. | Uber: ~3,000 survey participants, a handful of consensus points, government agreed to ratify them (23 May 2016). Whole vTaiwan: 200,000+ participants over dozens of issues. | S/H: https://www.shareable.net/open-data-hactivists-help-taipei-craft-regulatory-response-to-uber/ ; https://boingboing.net/2018/08/22/reasoning-together.html . Counts conflict (3,000 / 4,000 / 1,875 meeting attendees). Say "thousands". Verify on vtaiwan.tw / Audrey Tang before quoting. |
| 4 | **Participatory budgeting: Paris** | Concrete money, concrete streets. Easy visual: 5p in every £1 of capital spend chosen by residents. | Since 2014 Paris sets aside 5% of its investment budget (~EUR 100m a year, reached 2016); EUR 30m of it earmarked for poorer neighbourhoods (2019). | S: https://www.banquedesterritoires.fr/la-mairie-de-paris-debloque-100-millions-deuros-par-pour-son-budget-participatif ; https://www.paris.fr/pages/194-projets-gagnants-pour-le-budget-participatif-2019-7178 (P, city's own page) |
| 5 | **Participatory budgeting: Porto Alegre / Brazil** | The "it works" evidence, strongest outcome stat of the lot, but needs care. | Brazilian cities adopting PB saw infant mortality fall ~1-2 per 1,000 (5-10% of baseline); shifted spend to health and sanitation. | S academic, observational (Gonçalves, World Development 2013; Touchton and Wampler): https://library.uniteddiversity.coop/Decision_Making_and_Democracy/Participatory_Budgeting/The_Effects_of_Participatory_Budgeting_on_Municipal_Expenditures_and_Infant_Mortality_in_Brazil.pdf . Correlation not proof; slide must say "associated with". Do not attribute it to Porto Alegre alone. |
| 6 | **Quadratic voting: Colorado House Democrats** | Best explainer of "vote on many things, show how much you care": 100 tokens across 107 bills. Fun to animate in three.js (tokens as blocks). | 41 lawmakers, 100 tokens each, 107 bills; nobody put all 100 on one bill. Paid-leave bill won. | S: https://www.radicalxchange.org/wiki/colorado-qv/ ; https://coloradosun.com/2024/01/05/colorado-legisalture-quadratic-voting-lawsuit/ . Non-binding, secret, later ruled non-compliant with open-meetings law; no independent evaluation. Honest framing: "a pilot", not "proof". |
| 7 | **Liquid democracy: LiquidFeedback / German Pirates** | The cautionary tale and the purest "composition": delegate per topic, take it back any time. Good for the "here's what went wrong" slide, a credibility win. | Biggest installation: 13,836 registered users (2010-13). Activity dropped sharply ~180 days after the 2011 congress; power concentrated in few super-delegates. | S academic: https://arxiv.org/pdf/1503.07723 ; https://ese-journals.unisalento.it/index.php/paco/article/view/25695 . Search did not confirm any "collapse"; do not say it collapsed. Say "usage faded, power pooled in a few delegates". |

## Suggested use in the deck
- **Hero slide:** Switzerland. "They vote on things one at a time, ~10 times a year. We vote on 650 bundles at once, every 5 years." (UK: 650 MPs is common knowledge; the "bundle" framing is Kai's, not a sourced stat.)
- **Small-ideas slide:** vTaiwan/Pol.is as the machine that does what Martin Lewis is asking for. Found by search to be live; small-ideas.org itself NOT researched here (outside my brief; another agent).
- **"Won't it be mob rule?" slide:** Ireland assembly, then Colorado tokens for "intensity".
- **"Does it work?" slide:** Brazil PB infant mortality, hedged.
- **Honesty slide (voice: total authority, nurturing):** Pirates' liquid democracy, "we tried the pure version, here is the bug." Fits software-engineering framing: postmortem.

## Reader-fit notes (docs/marketing/the-reader.md)
- Name decision-makers: the story is "who decides what gets bundled", not "democracy is broken".
- Ireland slide: stay on process (random citizens, judge in chair), avoid litigating the topic.
- Swiss slide: invites "they also voted against minarets / immigration limits". Have an answer ready; do not hide that direct votes can go either way (the reader is right-drifting; that is a feature, not a risk to hide).
- Paris/Brazil are foreign and left-coded municipal projects; pair with a UK example if one is found (not searched).

## Gaps to verify before publishing
1. Swiss 332 figure: open admin.ch page and confirm date and wording.
2. vTaiwan participant counts: primary source (vtaiwan.tw, Audrey Tang).
3. Gonçalves infant-mortality range: open the paper, confirm 1-2 per 1,000.
4. Any UK precedent (citizens' assemblies on climate 2020, Scottish/Welsh PB) not searched.
