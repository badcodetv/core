# Same-song traps — every way we made the same song again

Jack, 2026-10-24: *"make sure to not fall into the traps the repo and the skills that make the same
song over and over with basically the same prompts … this prevents creativity and variety which is
exactly the goal … i do not want the same mistakes made over and over, i cannot emphasise this
enough."*

**Read this before every exploring round** (a new voice, a new sound, "experiment", "try different
ones"). The evidence is the Bank Robbery song: 400+ takes, mostly one voice
(`docs/stories/bank-robbery/songs/bank-robbery-jack.md`, `suno-voices.md` §2e–2h).

**The one rule under all of them:** the session that has this repo loaded must not shape the round.
It can't help it: CLAUDE.md, memory and the skills are in its head, and they leak into every
sentence it writes. So exploring rounds run through **`scripts/suno/sealed-round.py`**, and each
guard below is in that script, not in anyone's good intentions.

| # | Trap | Seen in | The guard (mechanical) |
| --- | --- | --- | --- |
| 1 | **House rules on every prompt.** Genre-picks-voice, short voice clauses, a carried-over ban list, Variety Off, style 75, the 30/60 pair, all stacked on every take | Rounds A→GA, 325 takes, one voice | Exploring prompts are written only by sealed writers. The suno-prompt skill's rules are for refining a liked take |
| 2 | **"Clean room" helpers inside the repo.** Agent-tool subagents auto-load CLAUDE.md + memory, and "ignore them" doesn't unload them | CR → GG | `sealed-writer.sh`: separate `claude -p` in an empty /tmp dir, web only. `--check` proves it sees nothing |
| 3 | **One shared music paragraph, only the voice line changes** | VB, SR1, SR2 draft 1 | `sameness.py` fails on any shared voice phrase or copied 6-word run, in the Style boxes **and** the lyric `[directions]` |
| 4 | **Overriding the gate** ("it's just the music") | SR1 | No override flag exists. `write` stops after two rewrites; `run` refuses a round whose `round.json` doesn't match its gate stamp |
| 5 | **The brief leaks the repo.** Old listen logs, old stored prompts, the session's paraphrase of what Jack wants | SR1 | The brief is built by the script from raw files only: `jack.md` verbatim, `lyrics.txt`, ONE fresh `listen.md`, `reference.md` (URL + Suno's raw record), `facts.md` (verdict facts + quotes) |
| 6 | **One writer writes all six prompts** and converges on one picture of the song | SR1, SR2 | Two stages: one writer proposes N different experiments, then N separate writers write one prompt each, none seeing another's text |
| 7 | **Splicing a liked voice sentence onto another prompt** (it went American) | BO | Never splice. A liked take is refined from its own whole prompt |
| 8 | **An accent is not a different singer.** Same delivery, six regions = one voice | VB, KA | The ideas stage is asked for different *performers*, not different accents |
| 9 | **Trusting a take's own box.** "Best one" says psych folk + sitar; it sounds like acoustic flamenco-style guitar over boom-bap | KA → SR2 | `listen.md` is a fresh listen. `reference.md` labels the stored box as "does not describe how it sounds" |
| 10 | **Variety Normal rewrote the box**, so the "liked prompt" wasn't the prompt | J → Z (ed6dd946) | Refining: build from the take's stored tags. Exploring: the writer chooses Variety per prompt |
| 11 | **The same settings on every prompt** (Max Mode on, 300 s, Variety off ×6) | SR1, SR2 | `sameness.py` warns on any setting identical across the round. Settings come from the writers |
| 12 | **Long boxes.** "Best one" was 29 words; SR boxes were 120–140. The liked takes came from drift space | SR1, SR2 (memory: short boxes keep the drift space) | A fact in `reference.md`/`facts.md`, for the writer to weigh. Not a rule we impose |
| 13 | **Denser lyrics change the song.** Best one = Jack's draft 3 (289 words); Kai's = 428. Faster, flatter | KA → SR2 | Stated as a fact in the brief. Which lyrics is Jack's call |
| 14 | **Retyping the writer's JSON**, which drifts | early CR | `run` builds the specs straight from `round.json` |
| 15 | **Changing the lyric words** | (checked every round) | `write` compares the words with `lyrics.txt` and sends any mismatch back |
| 16 | **Covers / Remix** | BA | Jack: covers don't work. `run` only creates fresh |
| 17 | **"Keep the liked prompt, change the voice" done by hand** — splicing a voice sentence onto the box (BO) or rebuilding it from the repo's notes (KA) | BO, KA | REFINE round: put the liked take's own box in `keep.txt`. Sealed writers each rewrite the *whole* box with their voice in it. The gate lets the kept box's words be shared, but never its voice words or any new wording (SR4, 2026-10-24) |

## How to add a trap

When a round fails in a new way: add a row here with the round it came from, **and** add the guard
to `sealed-round.py` or `sameness.py`. A trap with only a sentence of advice will be repeated.
