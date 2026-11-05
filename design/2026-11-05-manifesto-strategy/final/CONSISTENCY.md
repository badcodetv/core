# Consistency check: the staged final pages

2026-11-05. One pass over the ten staged manifesto pages (`manifesto/*.md`) and the ten staged briefs
(`ministers/*.md`), checked against `../README.md` §2 (the one-owner table, the four standing
amendments, the vocabulary rule), Kai's ruling (every §8 item is option A) and the four files in
`../factcheck/`. Nothing in `docs/government/` or `apps/` was touched.

## What was checked, and the result

| Check | Result |
| --- | --- |
| Renderer | `render-check.mjs` (this folder) imports `apps/site/manifesto.mjs` unchanged and renders all ten staged pages: every file parses, has `title` and `line`, one `## Position` heading, no markdown that would print literally, every `line` under 100 characters with no colon and no opening quote mark. The Chancellor's opening four-line "till slip" joins into one paragraph, which is exactly what happens to the live Chancellor page today (the renderer joins single newlines). Same parse as live. Run: `node design/2026-11-05-manifesto-strategy/final/render-check.mjs` |
| Lethal wording | "No UK weapon selects a person to attack." is word for word on Defence and Foreign. Foreign's second sentence paraphrased Defence's; **fixed**. Home uses the rights-list line ("No machine uses force on a person"), not the lethal one, which is correct |
| One owner per shared policy | Two counts only: Housing's roof count said "monthly" against the quarterly Transition Count it is a row of; **fixed**. Right to a human: benefits 4 weeks (W&P), clinical same working day (Health), tenancy 10 working days (Housing) were on their pages, policing "at the stop" was missing from Home; **fixed**. Windfall Act, public slice, NHS data exception, retraining ("paid training for a job that exists"), resilience money (held by Defence) all match the owner. Two items remain, below |
| Time-machine lines | Only on the PM page ("I've seen how this goes when nobody tests it"; "Drafted by AI, checked and signed by people. Not a real party. Yet."), per ruling 2A. The Chancellor's brief said "has seen the final balance sheet", a future-knowledge hint outside the PM; **fixed** |
| "Not ready" cap (one a page) | Education 1 (SEND money), Health 1 (full care funding), Housing 1 (council funding); the rest 0. Within the cap |
| Pass clause and undo | All ten pages carry "unless Parliament votes to keep it" and "Passes, and it goes national" |
| Reader traps | No "you've been duped/lied to"; deciders named (boards, ministers, Whitehall, the Department), never "AI" or "the market" as the actor; immigration given its size (MAC wording, as the fact check sanctioned) with no denial and no scare claim repeated; no sneer at the reader. Vocabulary: "postmortem" was on the PM page; **fixed** to "the write-up of what went wrong" |
| Six-word phrases on more than two pages | Only the mandated field-8 formula repeats (see unresolved 2). "answers to Parliament within 30 days" and "and the minister answers to Parliament" were on three pages each; **fixed** (Health and Housing reworded, PM and Defence keep it) |
| Briefs over 300 words | None. After the fixes: 295 to 300 words each (`wc -w`) |
| Numbers against `factcheck/` | Every figure on the pages traces to a fact-check row or is a provisional policy number, except the items in unresolved 5. Wordings the fact check required (Linton "may", "up to 1,200"; "first decision"; backlog including appeals; no student dependants; the Art. 22A–D sentence; 437,900 as "counted"; local connection with abuse victims and care leavers protected; Hormuz "on and off"; the NCSC wording; £24/MWh as decided policy; generator levy ending March 2028; "employee NI ... rates") are all in place |

## Fixes made (file: old → new)

1. `manifesto/02-foreign.md`: "Missiles and drones coming at us are fair game for a fast machine." → "Incoming missiles and drones are fair game for a fast machine." (Defence's wording, word for word.)
2. `manifesto/02-foreign.md`: switch list "It stops on its date, year three, unless Parliament votes to keep it." → "It stops with Defence's drills, five years in, unless Parliament votes to keep it." (One resilience programme held by Defence, so one stop date; Defence's run-by-hand stops five years in.)
3. `manifesto/03-home.md`: added "If a camera flags you, an officer decides, and tells you so, at the stop." (The policing deadline for the right to a human, which README §2 says each page states.)
4. `manifesto/08-housing.md`: "Counted monthly." → "Counted every quarter."; "You get the count monthly" → "You get the count every quarter" (roofs are a row in the quarterly Transition Count; no ministerial counts of their own).
5. `ministers/08-housing.md`: "The roof count: homes finished, by council, monthly." → "The roof count: homes finished, by council, quarterly (Transition Count)."
6. `manifesto/08-housing.md`: "A data centre pays for its own grid capacity or waits behind the houses." → "A data centre pays for its own wires, under Energy's grid rule, and waits behind the houses." (The connection rule is Energy's; Housing keeps the queue.)
7. `manifesto/08-housing.md`: "Councils built 9,241 for social rent last year." → "... in 2024-25." (Fact check HO3 is the 2024-25 financial year; "last year" in November 2026 reads as 2025-26.)
8. `manifesto/00-prime-minister.md`: "Publish the postmortem: an independent write-up of what went wrong, no blame." → "Publish the write-up of what went wrong: independent, no blame." (Vocabulary rule.)
9. `manifesto/00-prime-minister.md`: "Nobody's benefit is cut before ..." → "Nobody's benefit is lowered before ..." (W&P owns the rule and its brief says "a change that lowers your income", not "cuts".)
10. `manifesto/01-chancellor.md`: "Bank Rate today: up to 4%." → "Bank Rate since 5 November: 4%, up from 3.75%." ("Up to" reads as a ceiling; "today" goes stale. Fact check E1.)
11. `manifesto/01-chancellor.md` and `ministers/01-chancellor.md`: "income tax, NI or VAT" → "income tax, employee NI or VAT" (README §6 promises employee NI only; the Rung Fund and the bridge charge employers, so a bare "NI" over-promised).
12. `ministers/01-chancellor.md`: "a deadpan accountant who has seen the final balance sheet" → "who has read every balance sheet" (no fiction outside the PM). One sentence tightened to stay under 300 words.
13. `manifesto/06-health.md`: "the Health Secretary answers to Parliament within 30 days" → "the Health Secretary explains why to MPs within 30 days".
14. `manifesto/08-housing.md`: "and the minister answers to Parliament" → "and the Housing Secretary explains why to MPs".

## Unresolved

1. **Page length.** All ten staged pages are 366 to 421 words. `docs/government/workers/cabinet.md` §6 tells the cabinet "at most about 250 words ... rewrite and tighten", and README §2 says about 250. Unless the machinery PR (README §9 step 3) raises the cap to about 400, the first morning run will cut every page and may cut the tests first. Decide: raise the cap, or cut the pages here before wave 1.
2. **The contract formula repeats on all ten pages** ("It stops on its date unless Parliament votes to keep it, on the published review. Passes, and it goes national."). README §2 field 8 mandates it, so the six-word check exempts it, but it is the visible template reader X4 warned about. Decide: keep it verbatim (a brand mark), or let pages vary the wording around the fixed clause.
3. **The host-town deal has two fails-ifs from two ministers.** Energy: "Fails if developers quit deal towns at twice the usual rate." Housing (which owns the form): "Fails if a housing site is delayed anyway, or consents slow three months for nothing." Housing should carry the deal's one test and Energy the grid and water section's; needs the owners to agree which number belongs where.
4. **The Chancellor's page never mentions the Windfall Act it owns**, while Energy's page points to "the Chancellor's Windfall Act". Not a contradiction, but a reader of the owner's page can't find it. One sentence would fix it, against unresolved 1.
5. **Numbers on the pages with no row in `factcheck/`:** the £2 bus fare from January (Energy; sourced [M] only in `drafts/gaps.md`); the 2% digital services tax (Chancellor; sourced [H] only in `drafts/ai-profits-copyright.md`); the ledger bands "under £100m a year" (Education) and "under £1 billion a year" (Defence), which README §6 says the fact pass fills from named comparables and it has not; "as the new towns did" (Housing, no source); Nest as "the state's own scheme" ([M] in `drafts/pension-vote.md`).
6. **"No Right to Buy on the new homes" (Housing)** may already be government policy (the 2024 Right to Buy reform's new-build exemption, fact check L9). If it is in force, the page must say "we keep new homes out of Right to Buy for good" rather than present it as new.
7. **The Foreign switch list's stop date** was changed from year three to Defence's five years (fix 2) to make one programme carry one date. The Foreign and Defence files should confirm; the alternative is that the switch list is its own trial with its own date, in which case the one-owner table needs a line saying so.
8. **The policing deadline is on the Home page but not in the Home brief**, which is at the 300-word cap. Add it in the machinery PR by trimming another line, or the cabinet may drop it.
9. **Dated figures will go stale within weeks:** the NHS waiting list (September data on 12 Nov), NEET (30 Nov), Ofgem cap (January cap on 25 Nov), Bank Rate (December MPC), Linton-on-Ouse (live decision), Hormuz (weekly). Each has a review date in its fact-check evidence item; the evidence set must carry them before wave 1.
10. **Small unsourced characterisations:** Home "Whitehall sets it alone today" (immigration rules are laid before Parliament, so "alone" is arguable); Defence "spent on kit, not on keeping the lights on" (unclear what it claims, and "keeping the lights on" collides with Energy's beat); W&P "the law makes it consult" (collective consultation, fact check W13, not fetched).
11. **The Chancellor's "rates" line invites "your allowance is frozen till 2031"** (fact check E6, item 13). Optional fix, left off for length: "The allowance you pay them on: frozen till 2031."
