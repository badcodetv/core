# Run one replayed day from citizens to published (local, not Bob)

You are given DAY (two digits; news_date = 2026-11-DAY, run_date = 2026-11-23). Never commit or push. Never edit anything outside the day's own folder and your scratch folder.

Path override (applies to every instruction below and inside orchestrate.md): the issues are NOT in /home/kai/projects/badcode/badcode/docs/government/simulation/issues. They are in
ISSUES = /tmp/claude-1000/-home-kai-projects-badcode-badcode/43a1a379-cceb-4386-a276-20a36fdfe9c4/scratchpad/live/docs/government/simulation/issues
ISSUE = the one non-".side." JSON in $ISSUES/2026-11-DAY/ (stage clerk when you start).
S (your scratch folder) = /tmp/claude-1000/-home-kai-projects-badcode-badcode/43a1a379-cceb-4386-a276-20a36fdfe9c4/scratchpad/day-DAY (mkdir -p it).

1. Citizens: use the Agent tool to start ONE subagent with model "haiku" and exactly this prompt (fill in DAY):
"""
You are running ONE step of a labelled SIMULATION, locally (not in Bob). Follow the step's instructions exactly, with these local substitutions:
- Instructions: read /home/kai/projects/badcode/badcode/docs/government/workers/sim-citizens.md and /home/kai/projects/badcode/badcode/docs/government/simulation/README.md (rules).
- ISSUES = <the ISSUES path above> ; SIM = node /home/kai/projects/badcode/badcode/scripts/government/sim/sim.mjs (validate with --today 2026-11-23). Pool: /home/kai/projects/badcode/badcode/docs/government/simulation/citizens/pool.json
- Message: "Replay: news_date=2026-11-DAY run_date=2026-11-23". The issue is the one file in $ISSUES/2026-11-DAY/ not containing ".side." (stage clerk); read its side.clerk.json.
- Use "unsure" only for someone who would genuinely shrug; real polls usually find about one in five don't know.
- Count backers directly from the 100 lines you wrote (a citizen backs a test if their wants/limit clearly supports it).
- If the topic divides people sharply, let the answers reflect real disagreement, but no slurs and no claims about groups of people as facts.
- Do NOT commit or push. Skip the setup block. Only write the issue file and its side.citizens.json file.
Final reply: one line as the instructions say, plus "validate: pass" or the errors.
"""
   When it returns, check the ISSUE is at stage citizens and validates. If not, fix honestly or stop and report.

2. Then follow /home/kai/projects/badcode/badcode/design/2026-11-23-future-proof-rework/replay-kit/orchestrate.md steps A to F exactly, with START = A, T = /home/kai/projects/badcode/badcode/design/2026-11-23-future-proof-rework/replay-kit, and the path override above. Load Bob tools with ToolSearch "select:mcp__bob__chat_create,mcp__bob__chat_read" for step B.

3. Final check: SIM validate ISSUE --today 2026-11-23 passes and stage is "published"; every prediction's due is after 2026-11-23; run.stamp is exactly "Replayed on 23 Nov 2026 from the news of <D> Nov 2026" in the form the validator requires.

Final reply (short): one line per step with its result; the Codex chat id; the jury ruling in one line; the minister's decision in one line; total subagent tokens you saw; "validate: pass" or the errors.
