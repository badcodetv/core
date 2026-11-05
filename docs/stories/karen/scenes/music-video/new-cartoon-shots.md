# Karen music video re-cut: new cartoon shots (round 1)

**Why (Kai, 2026-11-05):** the re-cut puts cartoon footage in every chorus, and the only cartoon we
own is the eleven 10 s `hitchcock/` clips (110 s, see [`catalogue.md`](./catalogue.md)). Kai: *"make
more in the Hitchcock style … I trust you to make a reasonable selection … proceed autonomously."*
That is the ask that look.md's "Jack's imagery, not a licence to generate unasked" note waits for.

**Look:** Karen's ILLUSTRATED REGISTER, verbatim from [`../../look.md`](../../look.md), with one of
the existing hitchcock plates attached as the style reference (prompts.md §2a's documented move).
Stills: Nano Banana Pro, 16:9, 2 candidates. Clips: Gemini Omni Flash, 8 s, camera locked (look.md
§Engines); camera moves go in post.

**What each shot is for:** the chorus lines (*I'm sorry, I can't help you / You'll have to wait in
line / Somebody will be with you / Take your time / all day to complain*; final chorus *There is
nobody above me / I'm putting you through*), plus the spy-riff break and the President payoff. Every
shot has something in the world that moves, so Veo has a job; nothing asks for faces, hands or
text.

| Id | For | The picture | What moves (the clip) | Style ref |
| --- | --- | --- | --- | --- |
| c01 queue | "wait in line" | an endless snaking queue of silhouettes across an amber plaza to one tiny lit service window | the queue shuffles one step forward | img-8 |
| c02 waiting room | "take your time" | Karen alone on a long bench in a vast navy waiting room, a huge plain wall clock (no numerals) above | the clock's hands sweep round fast; she does not move | img-12 |
| c03 desk behind the desk | "a level above the level" | a line of identical desks receding to a vanishing point, a tiny clerk at each, Karen at the front | desk lamps switch on one after another into the distance | img-12 |
| c04 the stair | "nobody above me" | Karen's silhouette climbing a steep endless stair through floor slabs toward one lit door at the top | she climbs | img-9 |
| c05 switchboard | "putting you through" | a wall-sized switchboard of sockets, cords looping between them | amber lamps flick on across the board; the cords sway | img-10 |
| c06 the wires | "putting you through" | telephone poles marching to the horizon under a low amber sky | pulses of amber light run along the wires toward the horizon | img-4 |
| c07 hold music | "Vivaldi, second movement" | a gramophone horn and a spinning record on a navy plane, one amber wedge of light | the record turns; rings of amber pulse out of the horn | img-2 |
| c08 hanging receivers | "I'm sorry, I can't help you" | a row of empty glass phone booths, every receiver dangling off its hook | the receivers swing on their cords | img-4 |
| c09 the spy | break (spy riff) | Karen in a long coat under a single streetlamp, a long hard shadow, rain | rain falls, her coat moves in the wind, she lifts her chin | img-4 |
| c10 searchlights | break / final chorus | a monumental government building's flat facade, searchlight beams crossing it | the beams sweep across the facade | img-7 |
| c11 the dome | final chorus / President | a domed government building at night, every window dark | windows light up floor by floor, bottom to top | img-7 |
| c12 the room of voices | final chorus | Karen at her payphone, foreground, the cord stretched; behind her a crowd of silhouettes all holding receivers | the crowd raise their receivers together | img-8 |
| c13 chair and flask | "That's OK" | a folding chair and a flask beside the lit booth in the rain, nobody there | steam rises from the flask; rain falls | img-4 |
| c14 the dial | break stabs | a rotary dial from directly above, filling the frame | the dial spins back by itself | img-11 |

## The prompt (what was sent)

Every still: the preamble line, then the ILLUSTRATED REGISTER block exactly as in look.md, then the
shot's SCENE block below. The repeat is the style lock, kept on purpose.

```
Use the attached image as the style reference: match its palette, flatness, hard-edged light and matte painted texture exactly. Not photorealistic. Make a new picture with this content; do not copy the reference's composition.
```

SCENE blocks are recorded with each still's recipe card (the Flow MCP writes it) and listed in
[`new-cartoon-prompts.json`](./new-cartoon-prompts.json).

## Round 1 picks and clips

Picked by Claude on Kai's go-ahead ("I trust you to make a reasonable selection"), so the
still-approval gate was skipped this once; Kai can reject any clip on the timeline page. Picks:
c01-queue **b**, c02-waiting-room **b**, c03-desk-behind-desk **b**, c04-the-stair **b**, c05-switchboard **b**, c06-the-wires **a**, c07-hold-music **b**, c08-hanging-receivers **c**, c09-the-spy **b**, c10-searchlights **b**, c11-the-dome **b**, c12-room-of-voices **b**, c13-chair-and-flask **b**, c14-the-dial **a**.
Plates (borders trimmed on c12): `D:\badcode-videos\karen-music\clips\recut-cartoon\plates\`.
Clips: Omni Flash, 8 s, one fresh Flow project each (flow-automation law 19), audio stripped.
Motion prompts: [`new-cartoon-motion.json`](./new-cartoon-motion.json) (head + motion + the lock line).
