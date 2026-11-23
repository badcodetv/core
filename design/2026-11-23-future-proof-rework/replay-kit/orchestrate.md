# Orchestrating one replayed day of the SIMULATION (local, not Bob)

You were given DAY (e.g. 20 → news_date 2026-11-DD) and a START step. Read the rules first: /home/kai/projects/badcode/badcode/docs/government/simulation/README.md. Never commit or push.
- ISSUE = the non-".side." JSON in /home/kai/projects/badcode/badcode/docs/government/simulation/issues/2026-11-<DAY>/
- SIM = node /home/kai/projects/badcode/badcode/scripts/government/sim/sim.mjs (always validate with --today 2026-11-23)
- POOL = /home/kai/projects/badcode/badcode/docs/government/simulation/citizens/pool.json
- T = /home/kai/projects/badcode/badcode/design/2026-11-23-future-proof-rework/replay-kit ; S = a scratch folder of your own (packets and A/B answers go there).
- The day is "Replay: news_date=2026-11-<DAY> run_date=2026-11-23".

A. Packets: `python3 T/packet.py ISSUE S/p-<DAY>.json S/m-<DAY>.txt`.
B. Answer C (blind, other engine): read S/m-<DAY>.txt and call mcp__bob__chat_create with engine "codex", wait_seconds 300, message = that file's exact text. If status "running", poll mcp__bob__chat_read. Extract the JSON object, add "via": "Bob plain Codex chat <chat_id>", write it to <ISSUE without .json>.side.rival.json. Never write C yourself.
C. Answers A and B (blind): use the Agent tool to start two separate subagents in one message (model sonnet). Each gets: "Read the packet at S/p-<DAY>.json; replay of the news of 2026-11-<DAY>, only what was knowable then." plus its angle — A: FIX WHAT EXISTS (keep today's institutions; change rules, referee, money or penalties); B: CHANGE WHO RUNS IT (a structural change in who owns, runs or decides; the bolder one) — plus: one concrete answer; title ≤70 chars; answer ≤120 words, plain; say what changes, who does it, how you'd know it worked; every fact cited by id from the packet's sources or extra_sources, or a page opened now added to new_sources {title,publisher,date,url}; no real person's words; no claim about a named company a source doesn't make; never call simulated citizens "the public"; write JSON {title,answer,sources,new_sources} to S/a-<DAY>.json (resp. S/b-<DAY>.json). Don't tell either about the other or about C. If you have NO Agent tool, stop and report "no Agent tool" — never write A or B yourself.
   Join: `python3 T/join_bench.py ISSUE S/a-<DAY>.json S/b-<DAY>.json`, then validate.
D. Gate: follow /home/kai/projects/badcode/badcode/docs/government/workers/sim-gate.md exactly (skip setup; local paths). Open sources with WebFetch. A source that blocks automated fetching but was opened by the clerk earlier today may be kept; say so in the note only where a result depends on it.
E. Jury: follow /home/kai/projects/badcode/badcode/docs/government/workers/sim-jury.md exactly ($SIM draw <id>, $SIM people POOL <ids>). Write the 12 juror votes yourself in character; set jury.model to your own model id ("claude-sonnet-5-5").
F. Minister: follow /home/kai/projects/badcode/badcode/docs/government/workers/sim-minister.md exactly, with the brief for the owner post from /home/kai/projects/badcode/badcode/docs/government/ministers/. Predictions due AFTER 2026-11-23, at least one by 2027-01-22; no hindsight (only what was knowable on the news date; nothing already settled by 23 Nov 2026).

Validate after every step; fix errors honestly. Final reply: one line per step you ran with its result, and "validate: pass" or the errors.
