import json, io, os
OUT='/home/jackt/projects/badcode/badcode/docs/stories/camping/songs/camping.md'
lanes=['garage','reese','jungle','piano']
S={k:json.load(open(k+'.json')) for k in lanes}
T={'garage':[('4735d147-7b13-4da5-b247-d174ddbb1c93','3:09'),('ca5d75c6-b309-4e6f-8eaf-787d7f58c2d3','3:10'),
             ('b86f6223-a95e-4673-a4ba-42682be5ae58','3:09'),('035f8d67-a4b0-4ad0-ac07-65451a8020ed','3:09')],
   'reese': [('ce117a3f-3fbf-4b71-a7f9-203d29a175a2','3:04'),('3e2a516a-0ec2-4036-a351-5b3179a1fb02','3:06'),
             ('daf558be-0dcd-4618-bc28-79a11492b46d','3:05'),('8d095d65-c5fb-402a-8264-68cd475ff5b8','3:05')],
   'jungle':[('23424577-7f04-4f34-802b-1bd35c97144d','2:55'),('fe84c960-ed8c-4468-9b2d-85b47a74eed7','3:07'),
             ('8aad7fe2-8218-433e-b77a-8c820b071c81','2:56'),('99663d09-1b16-4e00-bb73-cde2c2e6f7d2','2:55')],
   'piano': [('257ed183-5fc7-4d8d-bcd4-e56345583f0c','3:10'),('dcb256c1-4cea-4d7b-a9cd-6306a24f1faf','3:09'),
             ('e212f69d-b749-4221-ab59-535774245219','—'),('222f885b-7782-4f32-ab52-94b2e5899aac','—')]}
AX={'garage':('skippy UK garage two-step, swung hats, a bouncing bassline','cheap synth strings **stabbing on the offbeat** with the shuffle','talky and conversational, long unhurried sixteen-bar verses','**190 s**','beat from bar one','warm, bouncy, mid-forward, a pirate radio rip'),
    'reese':('dry sparse minimal two-step roller, almost nothing in it','one solo violin **holding a line an octave above the reese**, bending where it bends','low and murky, drawing single words out with menace','**185 s**','the reese alone, four bars, no drums','narrow, cold, sub-heavy'),
    'jungle':('breakneck chopped amen re-chopping every bar, ragga swing, reverse crashes','a church organ **answering the room** at the turns','short sharp eight-bar bursts traded fast, hyping','**175 s** — the fastest','a room of men on the hook, unaccompanied','big, live, room-y, taped off the desk at a rave'),
    'piano':('soft rolling break, brushed hats, a sub that rolls rather than bites','a grand piano **answering him at the end of every line**, an octave higher each section','hurt and close, line ends half-sung flat and raw, never tuned','**190 s**','piano alone, three lines, then the beat','wide, warm, tape-soft')}
def cell(k,i): return ' · '.join(f'[{s[:8]}](https://suno.com/song/{s})'+(f' ({d})' if d!='—' else '') for s,d in T[k][i:i+2])

b=io.StringIO(); W=b.write
W("""## v6.62 Round r70 — four records, not four mixes: the BOLD rule applied to the merged spine (2026-09-23)

**Brief, Jack 2026-09-23:** *"all of those were way too similar to each other, please mix up the
beat, the orchestral elements, the grime rap voice, speed and flow, experiment using the provided
songs I said I want you to combine and build off of, whilst removing the bad parts."*

### 🔴 He is right and the number is brutal: r69's lanes shared 68–74% of the Style box

| r69 pair | Longest shared run |
|---|---|
| `merge` / `beatfirst` | 462 chars = **74%** |
| `merge` / `opencold` | 461 chars = **74%** |
| `beatfirst` / `opencold` | 461 chars = **68%** |

The sheet's own BOLD rule puts **anything over 40% in the 🔴 meek band** — *"this is one prompt with
a costume. Rewrite before running."* r69 was three copies of one 462-character body with a different
opening sentence bolted on. **It was written to answer "combine the two" and it broke the variety
rule doing it.** Both requirements are live at once and r70 holds both.

### The rule this round obeys, and it is already in the repo

*"A variety round moves THREE things per lane: the d&b subgenre, the instrument family, and the
opening the track starts on — plus a different job for that family and a different production
sentence."* Jack named **four** axes, so r70 moves five per lane — his four plus the opening — and
nothing is shared but the cast sentence.

📎 **And the drums are the right axis to lead with.** Practitioner consensus: *"your ear for drum
programming will often tell you the sub-lane faster than the bass"*
([United By Bass](https://www.unitedbybass.com/every-drum-bass-subgenre-you-need-to-know-2025-edition/),
[Red Bull](https://www.redbull.com/ca-en/an-expert-guide-to-drum-n-bass-sub-genres)). So each lane's
first clause is a different beat.

🔑 **The flows are grime-internal, so Ruling 2 holds.** Grime's own tradition supplies four distinct
cadences without leaving the pool: **8-bar** (concise, high-energy, rapid exchanges), **nu-shape
16/32-bar** (longer, more complex verses), **eskibeat's** quirky syncopated off-beat phrasing, and
**darkside's** slow, heavy, menacing delivery
([Grokipedia](https://grokipedia.com/page/Grime_music), [Eskimo](https://en.wikipedia.org/wiki/Eskimo_(grime_beat))).
⚠️ **The genre words themselves stay out of the boxes** — `eskibeat` names a 140 BPM beat and would
drag the tempo. The cadences go in as description.

### The four lanes — five axes moved per lane

| Lane | Beat | Orchestral element and its **job** | Voice and flow | Speed | Opens on | Production |
|---|---|---|---|---|---|---|
""")
for k in lanes:
    a=AX[k]; W(f"| `{k}` | {a[0]} | {a[1]} | {a[2]} | {a[3]} | {a[4]} | {a[5]} |\n")
W("""
✅ **Measured bold, and asserted in the build:** the longest shared run between any two Style boxes
is **102–124 chars (17–21%)**, and the build **fails** unless that run is contained in the mandated
cast sentence plus `night-bus melancholy`. **No production language, no beat language and no
instrument is shared between any two lanes.**

✅ **And short — r69's finding is kept:** Style **600–639** chars, Exclude **453–474**, against the
liked takes' 805/438 and the rejected r68's 990/948.

### 🔑 Speed is a lane property this round

Jack asked for speed and flow to vary, so **Duration varies with the lane** rather than being held
constant: `jungle` 175 s · `reese` 185 s · `garage` and `piano` 190 s — the whole of the settled
working bracket, spread across four different flows. It is deliberately confounded with the lane,
because that is what "mix up the speed" asks for.

### "Removing the bad parts" — the list, carried as bans

Every complaint Jack has made about this song, kept as a ban in all four lanes and nothing else:
`autotune, pitch-corrected vocals, cheesy` (the cheesy hook) · `shouting, screaming, roaring` (the
shouting) · `steady rap pace` (the drag he disliked in `1127446d`) · `double-time, motormouth` (the
takes that were way too fast) · `American accent, US rap, trap, female vocal` (casting) ·
`jump up, wobble bass, neurofunk, dubstep, EDM drops, glossy production` (the aggression and the
gloss) · `major key, happy, uplifting` · and the bed bans. 🔴 **`air horns` and `snarling` stay
lifted**, and `distorted bass` and `rapid-fire` remain unbanned.

✅ **Not one lyric word changed.** Only the opening cue, the `[Drop]` cue and the two MC delivery
cues differ per lane, so the lyrics carry each lane's flow instead of fighting it.

### Settings

v6 · Style Influence **75** · Variety **Off** · Max Mode off · Vocal Gender Male · Personalize off ·
no Voice · **Duration per lane (175/185/190)** · workspace `camping-Jack` · weirdness **40 and 60**.
8 Creates, 16 takes.

### Generated 2026-09-23 — 8 Creates, 16 takes. Credits 9,080 → 9,000

| Lane | In one line | w40 | w60 |
|---|---|---|---|
""")
for k in lanes:
    W(f"| `{k}` | {AX[k][0]} + {AX[k][1].replace('**','')} | {cell(k,0)} | {cell(k,2)} |\n")
W("""
⚠️ **`piano` w60 returned `create:timeout` twice before succeeding on the third attempt.** Both
failures cost **0 credits** and produced **no takes** — verified against the take list and the
balance before retrying, which is the only safe way to handle a timeout. 🔑 **A `create:timeout` is
not necessarily a spent Create: check the take list and the credit balance before re-running.**

✅ **Duration behaved as the bracket predicts, and the 175 s reading gets a third data point:**
190 s → 3:09–3:10 (4/4) · 185 s → 3:04–3:06 (4/4) · **175 s → 2:55, 2:55, 2:56 and one 3:07** — the
only overshoot in the round, in the only cell set to 175. **185–190 s is reliable; 175 s is not.**

⬜ **Not heard.** Three questions:
1. 🔑 **Do these four sound like four different records?** That is the round's whole point, and it
   is now measurable as well as audible — if they still sound alike at 17% shared text, the
   similarity is coming from somewhere other than the Style box, and the **lyrics box** is the next
   place to look.
2. **Which beat, and which orchestral job?** The two axes are independent and can be recombined
   next round.
3. **Which flow, and at which speed?** `jungle` at 175 s and `garage` at 190 s are the two extremes.

""")
for k in lanes:
    W(f"### r70 {k} atom\n\nStyle:\n\n```\n{S[k]['style']}\n```\n\nExclude styles:\n\n```\n{S[k]['exclude']}\n```\n\n")
W(f"### r70 lyrics (`piano` lane shown — lanes differ only in the opening cue, the `[Drop]` cue and the two MC delivery cues)\n\n```lyrics\n{S['piano']['lyrics']}\n```\n\n---\n\n")
src=open(OUT).read(); anchor="## v6.61 Round r69"
assert anchor in src
open(OUT,'w').write(src.replace(anchor, b.getvalue()+anchor, 1))
print("✅ inserted §v6.62")
