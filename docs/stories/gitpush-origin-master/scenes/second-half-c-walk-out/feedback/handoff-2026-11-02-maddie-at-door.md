# Handoff → session "maddie-at-door" (from gpom-second-half, 2026-11-02)

The job: the bridge between the kill bots standing down (end of scene A) and the humans following
Maddie into the AI's building (scene C → D). Scene A (Maddie's intro speech) stays in the
gpom-second-half session; this session owns the door/bridge only.

## Kai's words (2026-11-02, verbatim from the voice note)

> I also have another task, which might be a handoff scenario. And that is that we dropped the Maddy at the door. So the kill bots stand down. And then we've decided to not have the big negotiation between Maddie and the group, which is good because it saves a lot of dialogue. The problem is it cuts very quickly now to the humans are just going to go with the time machine. It feels too fast. And I quite like the fact that the humans get into the building. Derek says, what's that? And Maddy says, it's the time machine. And that's the first time you hear about a time machine. That works. But some negotiation later is too weak a link between kill bots were about to arrive to kill you, and now you're willing to just get into the machine that the AI made. So we do need some kind of bridge there.

Full message: `docs/stories/gitpush-origin-master/scenes/second-half-a-killbots/feedback/chat-2026-11-02/kai-maddie-intro.md`.

So, Kai's constraints:
- NO return of the big doorstep negotiation (too much dialogue, removed mystery).
- Keep the time machine unmentioned until scene D beat 3: Derek "What is it?" / Maddie "It's the time machine. You do understand what this will cost you." (`second-half-d-crossing/scene.json`, cut-notes `bd3`). Kai likes that this is the first mention.
- The gap to fill: why would people who were about to be killed by the AI's kill bots follow its robot into its building? Trust has to be earned in some way, quickly.

## How we got here (history)

- **28 Oct, round 3–4:** the doorstep (scene B, `second-half-b-the-door/`) was a long talk between Maddie and the old lady. Kai: "Nothing about Maddy sat talking to the old lady is exciting… by spelling it out it's boring, and removes mystery." His words: `second-half-b-the-door/feedback/watch-2026-10-28/kai-chat.md` and `kai-chat-bridge.md`.
- **Bridge research (28 Oct):** `design/2026-10-28-gpom-door-bridge/proposal.md` (+ research-*.md). Five options: 1 the short door (~24 s), 2 the door three times (no words), 3 the gesture (one line), 4 the smash cut, 5 the door shut, the morning after (~35 s, recommended by Fable). Built as B round 4 / cut tag `br` (`scripts/gpom/second-half-video/cut3.py --tag br`, Premiere `gpom-3-B-door-r5`): a held look, the door, muffled talk behind it. Kai then went further:
- **Kai's own call (28 Oct):** cut B entirely. Kill bots stand down → black card **"Some negotiation later."** → zoom out on Maddie leading the humans (first frame of C03f-reveal). Built as scene C round 7 (`scripts/gpom/second-half-video/ending/cut_end.py --tag later`, output `ending/C/cut-later/`, 46.96 s; Premiere `gpom-4-C-walkout-r2`). Card options offered, never picked: "Some negotiation later." (current), "Several cups of tea later.", "One very long chat later.", "The next morning."
- **Now (2 Nov):** Kai says that card is too weak a link. We overshot.
- Scene B's footage and its old voiced lines (draft 2J etc.) still exist: `second-half-b-the-door/script.json` (lines moved to `dropped`), cut `cut3/B-br/`. The old scene C round 6 still had Maddie's walk lines; C now opens on the card then "Careful now, humans." + the radiation line.

## Where it sits in the film

Track/opening → **A** kill bots + Maddie's intro (being rewritten now: she now explains the storyverse and the AI's regret, "Patrol's out. Mind how you go.") → **[the gap]** → **C** walk out → **D** clean room + crossing (the time machine) → **E** bus. Overview board: https://claude.ai/artifact/AXJqmgAWTRhxK7fzMkKukp (source `docs/stories/gitpush-origin-master/timelines.json`).

Worth knowing: Maddie's new intro (design/2026-11-02-gpom-dialogue-maddie-storyverse/, draft 1E) already lands the AI's regret and "you drove it, now you're gone… we fucked this up", so the bridge doesn't need to re-explain consciousness; it needs the humans' decision to trust.

## Standing rules (Kai)

- Only build NEW Premiere sequences; never touch Kai's sequences or music; don't drive Premiere while he's in it; one session drives the bridge at a time (gpom-second-half may hold port 7890 — don't kill it, ask).
- Page and Premiere move together each round (no split brain). Dump page notes to `feedback/` before acting. Log with `prov.py trail`.
- Kai approves stills before any video credit. Read GPOM's `look.md`/`sound.md` before any Flow/Suno/voice prompt.
- Dialogue rewrites → scene-dialogue skill (brief first). Commit only when asked. Rundown reply style, every identifier glossed.
