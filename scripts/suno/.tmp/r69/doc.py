import json, io, os
OUT='/home/jackt/projects/badcode/badcode/docs/stories/camping/songs/camping.md'
lanes=['merge','beatfirst','opencold']
S={k:json.load(open(k+'.json')) for k in lanes}
T={'merge':[('b3110997-7333-43b9-89ab-41e1831357c7','3:04'),('fae9996d-cbb5-4c88-a606-1f9cfd6e8a0e','3:05'),
            ('1672b535-60ab-4ebd-9b8f-738dc36fca09','3:04'),('1a6e27d1-fdd2-4fa6-ac34-94b0d5ded58a','3:07')],
   'beatfirst':[('f2bbdfec-2529-4714-8c62-6c5d783d0a85','3:05'),('15ca6f44-ce51-47bd-a687-0823b87051c9','3:05'),
            ('ba4c3847-911f-49f8-b696-03d9d6284fd8','3:05'),('ffa10291-e7b6-4154-889c-0963e6dfc235','3:05')],
   'opencold':[('d98f3055-46ec-46ec-ba9f-6b07a4abf50f','—'),('7158fdc9-0963-4a58-a852-87088a79cd87','—'),
            ('a288159f-00fb-402a-b1a9-2837d54c3fca','—'),('9e6e9572-5617-48ab-a493-2d4de39029b2','—')]}
D={'merge':"**nothing said about the opening at all** — the largest drift space of the three",
   'beatfirst':"`1127446d`'s opening: *the beat hits hard from the very first bar, no intro*",
   'opencold':"`1b2aa79c`'s opening: no drums, a piano and a lone violin, three lines, then the beat on 'you keep on walking'"}
def cell(k,i): return ' · '.join(f'[{s[:8]}](https://suno.com/song/{s})'+(f' ({d})' if d!='—' else '') for s,d in T[k][i:i+2])

b=io.StringIO(); W=b.write
W("""## v6.61 Round r69 — 🔴 THE RESET: the two liked takes merged, and the boxes cut back to their size (2026-09-23)

**Brief, Jack 2026-09-23:** *"the newest generations are nothing like these two
[[1127446d](https://suno.com/song/1127446d-abe8-4079-9bbe-6b281e12aa74)]
[[1b2aa79c](https://suno.com/song/1b2aa79c-9b06-44e8-b463-63809306060b)]. Please start again and
combine the two."*

### 🔴 The diagnosis, with numbers: we over-specified the drift space shut

Both takes Jack likes were made by boxes that were **disobeyed** — the sheet has said so since r47:
*"every liked feature was a disobedience."* The piano opening, the orchestral violins and the sung
chorus on `1127446d` are **all drift**; its box bans `piano`, names no orchestral instrument and
contains no chorus. So the boxes do not describe the records — they describe the space the records
drifted inside.

**r67 and r68 kept adding instructions to that space until there was none left:**

| | Style | Exclude | Lyric cues |
|---|---|---|---|
| `1127446d` (liked) | 805 | **438** | short |
| `1b2aa79c` (liked) | 997 | 835 | 1,245 |
| r68 (rejected) | 990 | **948** | **1,662** |
| 🆕 **r69** | **625–758** | **443** | **677** |

🔑 **The exclude box more than doubled the liked take's, and the cues grew by a third.** Our own rule
says a bloated Exclude box out-votes the Style box, and that cues *"are read, but they compete."*
Every r67/r68 addition was individually justified by a note from Jack — and collectively they turned
a loose brief into a specification, which is exactly the failure the sheet already recorded once at
r53–r57 (*"each tried to write the liked accidents in, and each got further away"*).

**So r69 is a reset, not another iteration.** Every instruction added since r66 that Jack did not
ask for by name is gone.

### What each parent contributes — sentences lifted from their own boxes, verbatim where possible

| From `1127446d` | From `1b2aa79c` |
|---|---|
| *a solid punchy beat, full breakbeats and a heavy rolling sub, never jump up, and the track builds from there* | *chopped amen fills at every section turn* (both had this) |
| *skippy two-step garage shuffles folded into the drum and bass* | *handclaps on the backbeat* |
| 🔑 *a dark **reese** bass that grows meaner every section* | 🔑 *a room of men answers him on the hook, low and close* |
| *cheap synth strings* — the only orchestral word either box ever had | *a church organ at the turns* |
| *night-bus melancholy* | the **grime cast** (Ruling 2), kept verbatim |

🔴 **Three things from `1127446d` were deliberately NOT carried over.** Its cast (*a gravelly older
English storyteller / a BBC newsreader*) loses to Ruling 2, which Jack made standing. Its
*"steady rap pace"* is the one thing he has ever disliked about that take, so it stays **banned**
rather than asked for. And its `piano` ban is gone — that ban was banning the opening he loves.

### The one variable: which parent's opening the merged body wants

| Lane | The opening |
|---|---|
""")
for k in lanes: W(f"| `{k}` | {D[k]} |\n")
W("""
🔑 **`merge` says nothing about the opening on purpose.** It is the round's real bet: give Suno the
merged body and let the arrangement drift, which is the only way either liked take was ever made.

### The excludes, rebuilt from scratch at `1127446d`'s scale (443 chars)

**Kept:** the nationality and vocalist guards, `jump up, wobble bass, neurofunk, dubstep, EDM drops,
glossy production`, `major key, slow tempo, half time, tempo change`, `steady rap pace, double-time,
motormouth`, `shouting, screaming, roaring`, `autotune, pitch-corrected vocals, gospel choir,
cheesy`, and the bed bans.
**Dropped:** `piano` · `choir, crowd noise, audience, applause` (the room is the point of the lane
Jack likes) · `air horns, snarling` (Jack removed them by name) · and the whole accreted middle
layer — the anti-loudness bans, the clarity bans, the cross-lane instrument bans, the drum-loss
guards. 🔴 **Those drum-loss guards bought real protection at r65, so if the drums go soft in this
round, that is the first block to put back — and it is the round's stated risk.**

✅ **Not one lyric word changed** — asserted byte for byte, 80 lines. Only the cues shrank.

### 🔑 And the shorter route, which is one human action, not a prompt

Jack's actual request — *combine these two songs* — is a **feature**, and it is the one thing this
automation cannot do (any attachment on the create form aborts `load` by design). **Suno v6's
multi-song mashup**, `files/suno-v6.md` §5, marked *tested twice*:

1. **Simple** mode → **Add** → drag both songs in (2–3 allowed).
2. One plain-English instruction naming which element comes from which — e.g. *"the drums, the reese
   and the grime vocal from the second one, the piano and violin opening and the string melody from
   the first."*
3. Create. **What it should sound like:** a single record carrying both, not a crossfade. **Failure
   sign:** it returns a cover of one of them — check both songs actually attached before Create.

**That is 10 credits and one drag, and it is a genuinely different mechanism from anything in this
sheet.** Worth doing alongside r69 rather than instead of it — the prompt round is reproducible and
the mashup is not.

### Settings

v6 · Style Influence **75** · Variety **Off** · Max Mode off · Vocal Gender Male · Personalize off ·
no Voice · **Duration 185 s** · workspace `camping-Jack` · weirdness **40 and 60**. 6 Creates, 12 takes.

⬜ **Style Influence stays at 75 so the box length is the only thing that moved.** If r69 is still
too obedient, **SI 70 then 65 is the next lever** — it is the adherence control, and both liked
takes are records of disobedience.

### Generated 2026-09-23 — 6 Creates, 6 clean. Credits 9,140 → 9,080

| Lane | Opening | w40 | w60 |
|---|---|---|---|
""")
for k in lanes: W(f"| `{k}` | {D[k].split(':')[0]} | {cell(k,0)} | {cell(k,2)} |\n")
W("""
✅ **Six Creates, six clean** — 10 credits each, balance read around every one.
✅ **Duration 185 s held a third time** (3:04–3:07 on the eight measured).

⬜ **Not heard.** Three questions:
1. 🔑 **Does it sound like a relative of the two takes again?** That is the whole round. If yes, the
   diagnosis is confirmed and **short boxes become the house default for this song.**
2. **Which opening?** Unspecified (`merge`) · beat-from-bar-one (`beatfirst`) · drumless piano and
   violin (`opencold`).
3. 🔴 **Did anything the stripped bans were holding back come back in** — soft drums, a tuned
   chorus, an American vocal? Each has a named block ready to reinstate on its own.

""")
for k in lanes:
    W(f"### r69 {k} atom\n\nStyle:\n\n```\n{S[k]['style']}\n```\n\nExclude styles:\n\n```\n{S[k]['exclude']}\n```\n\n")
W(f"### r69 lyrics (shared — the canon words, cues cut 1,662 → 677 chars)\n\n```lyrics\n{S['merge']['lyrics']}\n```\n\n---\n\n")
src=open(OUT).read(); anchor="## v6.60 Round r68"
assert anchor in src
open(OUT,'w').write(src.replace(anchor, b.getvalue()+anchor, 1))
print("✅ inserted §v6.61")
