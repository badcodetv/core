# Same-song traps — every way we made the same song again

Jack, 2026-10-24: *"make sure to not fall into the traps the repo and the skills that make the same
song over and over with basically the same prompts … this prevents creativity and variety which is
exactly the goal … i do not want the same mistakes made over and over, i cannot emphasise this
enough."*

**Read this before every exploring round** (a new voice, a new sound, "experiment", "try different
ones"). The evidence is the Bank Robbery song: 400+ takes, mostly one voice
(`docs/stories/bank-robbery/songs/bank-robbery-jack.md`, `suno-voices.md` §2e–2h).

**The one rule under all of them:** nothing the session carries may shape the round. Two halves:

1. **The pollution is removed at the source** (Kai, 2026-10-28). There is no BadCode house sound:
   no genre, voice, slider value or Style box in CLAUDE.md, memory or any skill description, and
   `scripts/style-lint.py` checks. A song's sound lives only in its story's
   `docs/stories/<story>/sound.md` ([`STYLE.md`](../stories/STYLE.md)).
2. **The writers are separate.** Exploring rounds run through the **`variations` skill**
   (`.claude/skills/variations/SKILL.md`): one ideas writer, then N separate subagent writers who
   never see each other's text, each given only the brief that `python3 scripts/variations/round.py
   brief` builds from raw files. The session does not write a word of any prompt. Each guard below
   is in `round.py` or `sameness.py`, not in anyone's good intentions.

**Bank Robbery's standing rules** (Jack's, e.g. no screaming) are that story's, not every song's:
they live in `docs/stories/bank-robbery/sound.md`, and reach a round only through its brief.

| # | Trap | Seen in | The guard (mechanical) |
| --- | --- | --- | --- |
| 1 | **House rules on every prompt.** Genre-picks-voice, short voice clauses, a carried-over ban list, Variety Off, style 75, the 30/60 pair, all stacked on every take | Rounds A→GA, 325 takes, one voice | No house rules exist to stack: style is in the story's `sound.md` only (`style-lint.sh`). Exploring prompts are written only by the `variations` skill's writers. The suno-prompt skill's rules are for refining a liked take |
| 2 | **"Clean room" helpers inside the repo.** Agent-tool subagents auto-load CLAUDE.md + memory, and "ignore them" doesn't unload them | CR → GG | Remove what they inherit instead of escaping it: no style in CLAUDE.md, memory or skill descriptions (`scripts/style-lint.py`). The writers are `variations` subagents that see only the brief `round.py brief` built from raw files. *(History: 2026-10-24 to 10-28 this was `sealed-writer.sh`, a `claude -p` in an empty /tmp dir; Kai retired it once the pollution was removed at the source)* |
| 3 | **One shared music paragraph, only the voice line changes** | VB, SR1, SR2 draft 1 | `sameness.py` fails on any shared voice phrase or copied 6-word run, in the Style boxes **and** the lyric `[directions]` |
| 4 | **Overriding the gate** ("it's just the music") | SR1 | No override flag exists. `round.py gate` sends offenders back and stops after two rewrites; `round.py run` refuses a round whose `round.json` doesn't match its gate stamp |
| 5 | **The brief leaks the repo.** Old listen logs, old stored prompts, the session's paraphrase of what Jack wants | SR1 | The brief is built by `round.py brief` from raw files only: `ask.md` (the human's words verbatim; `jack.md` in old rounds), `lyrics.txt`, ONE fresh `listen.md`, `reference.md` (URL + Suno's raw record), `facts.md` (verdict facts + quotes), and the story's `sound.md` verbatim |
| 6 | **One writer writes all six prompts** and converges on one picture of the song | SR1, SR2 | Two stages: one writer proposes N different experiments, then N separate writers write one prompt each, none seeing another's text |
| 7 | **Splicing a liked voice sentence onto another prompt** (it went American) | BO | Never splice. A liked take is refined from its own whole prompt |
| 8 | **An accent is not a different singer.** Same delivery, six regions = one voice | VB, KA | The ideas stage is asked for different *performers*, not different accents |
| 9 | **Trusting a take's own box.** "Best one" says psych folk + sitar; it sounds like acoustic flamenco-style guitar over boom-bap | KA → SR2 | `listen.md` is a fresh listen. `reference.md` labels the stored box as "does not describe how it sounds" |
| 10 | **Variety Normal rewrote the box**, so the "liked prompt" wasn't the prompt | J → Z (ed6dd946) | Refining: build from the take's stored tags. Exploring: the writer chooses Variety per prompt |
| 11 | **The same settings on every prompt** (Max Mode on, 300 s, Variety off ×6) | SR1, SR2 | `sameness.py` warns on any setting identical across the round. Settings come from the writers |
| 12 | **Long boxes.** "Best one" was 29 words; SR boxes were 120–140. The liked takes came from drift space | SR1, SR2 (memory: short boxes keep the drift space) | A fact in `reference.md`/`facts.md`, for the writer to weigh. Not a rule we impose |
| 13 | **Denser lyrics change the song.** Best one = Jack's draft 3 (289 words); Kai's = 428. Faster, flatter | KA → SR2 | Stated as a fact in the brief. Which lyrics is Jack's call |
| 14 | **Retyping the writer's JSON**, which drifts | early CR | `round.py run` builds the specs straight from `round.json` |
| 15 | **Changing the lyric words** | (checked every round) | `round.py gate` compares the words with `lyrics.txt` and sends any mismatch back |
| 16 | **Covers / Remix** | BA | Jack (Bank Robbery): covers didn't work for that song. `round.py run` only creates fresh |
| 17 | **"Keep the liked prompt, change the voice" done by hand** — splicing a voice sentence onto the box (BO) or rebuilding it from the repo's notes (KA) | BO, KA | REFINE round: put the liked take's own box in `keep.txt`. The `variations` writers each rewrite the *whole* box with their voice in it. The gate lets the kept box's words be shared, but never its voice words or any new wording (SR4, 2026-10-24) |
| 18 | **The same prompt written outside a round.** A single prompt, a re-roll or a hand-paste drifts back to the wording of the last twenty, and nothing compared it with them | Flow and Suno, 2026-10-29 (Kai found the Suno trap in the videos) | `scripts/variations/fresh.py` compares every prompt with every past one (cards, specs, rounds); a PreToolUse hook in `.claude/settings.json` runs it before each Flow call and `suno.mts` call. It reports identical prompts, near copies and habit phrases; it never blocks |

## How to add a trap

When a round fails in a new way: add a row here with the round it came from, **and** add the guard
to `scripts/variations/round.py` or `scripts/variations/sameness.py`. A trap with only a sentence of advice will be repeated.
