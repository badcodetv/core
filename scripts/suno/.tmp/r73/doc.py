import json, io, os
OUT='/home/jackt/projects/badcode/badcode/docs/stories/camping/songs/camping.md'
lanes=['spiccato','harpcello','dubecho','machine','square']
S={k:json.load(open(k+'.json')) for k in lanes}
T={'spiccato':[('1dc611c3-be98-4ce5-bd79-db274a5b2946','3:09'),('954f20c5-bf4f-4ecc-8ea0-e06ab0f6c955','3:09'),
               ('504ea667-69d7-4d14-9d11-65e25c06bf45','3:10'),('9466dc63-96bf-487e-aca1-524e8dece7f1','3:10')],
   'harpcello':[('40c91647-f8bd-4284-a294-60c30127b6af','3:10'),('02854716-d906-43d2-91df-f4aa5229e4df','3:09'),
               ('67fa4f2b-c793-43aa-bddc-5e906e02d4f1','3:09'),('aa19093d-dc40-482f-acd0-2335748ab91f','3:10')],
   'dubecho':[('7722c22a-64bb-4ab3-be5e-f19515cc2d04','3:10'),('acecb8f6-46ad-4396-9137-53e58d6f2dcf','3:10'),
               ('e3324d4f-443f-49b0-969b-403fc7d9330e','3:10'),('b27cf690-888d-4ff6-a839-767c1b493220','3:11')],
   'machine':[('0d773754-0e51-4297-925a-1cf254c07088','3:10'),('401c086d-bb91-4238-9ddf-fd29af94a8fe','—'),
               ('2eb264ad-9df1-40fa-84b7-54704451f3b9','3:09'),('ca84dbaa-351e-494a-9fdc-9f18aecd6dce','3:10')],
   'square':[('833f1b0d-9152-4248-ab46-b44ac812d186','—'),('1220c06e-00b4-4efa-a5e6-c72f6c2da286','—'),
               ('0f264d79-602a-4e64-b00f-4382a9d2c4c3','—'),('36619360-2e1f-4dc3-a1c2-8551fb4b7383','—')]}
KIND={'spiccato':'🎻 orchestral','harpcello':'🎻 orchestral','dubecho':'🧪 free','machine':'🧪 free','square':'🧪 free'}
ONE={'spiccato':"tight rolling break, crisp dry snare; **spiccato violin stabs locked to the hats** playing the break's own pattern back, one lone violin answering him at the end of every bar",
     'harpcello':"loose swung broken beat; **a harp running one arpeggio under the break like a hi-hat**, low cellos doubling the sub an octave up",
     'dubecho':"half-stepping with big gaps and an offbeat skank; **tape echo throwing his line-ends across a long spring reverb**, one siren sweeping the field",
     'machine':"relentless, no swing; **metallic clicks on the snares, hi-passed pots and pans on the kick, banging pipes and a construction-site clang**, a distorted machine loop grinding under it",
     'square':"one eight-bar loop, very clear single hits, no percussion layers; **detuned square-wave stabs and a gliding sine lead** carry the tune, filter opening at every turn"}
def cell(k,i): return ' · '.join(f'[{s[:8]}](https://suno.com/song/{s})'+(f' ({d})' if d!='—' else '') for s,d in T[k][i:i+2])

b=io.StringIO(); W=b.write
W("""## v6.65 Round r73 — five worlds on a frozen spine: the take Jack likes, kept exactly, everything else free (2026-09-23)

**Brief, Jack 2026-09-23, on [36d0b981](https://suno.com/song/36d0b981-5ffb-482b-9b9b-ab9e50f3a56b)
(= `camping-r71-wordsonly-v6-w40`):** *"I like this one, the voice is cool, the begging being slow
until the beat drops is nice, the pacing is perfect, chorus being quick keep that. Please build on
this, keep all of the elements I like and make variations — only make some variations with
orchestral elements, but be free with the other ones, as in experiment with it and make each
generation vary from each other, whilst using this song as the base."*

🔑 **This is the first round where the brief names exactly what is frozen and exactly what is free**,
so the round is built as a **frozen spine + five worlds** rather than as either a variety round or a
deepening round.

### 🔒 Frozen — the four things he named, byte-identical in all five lanes

| What he said | What is locked |
|---|---|
| *"the voice is cool"* | the r43 grime cast sentence, unchanged |
| *"the begging being slow until the beat drops is nice"* | *"No drums at first: three lines of him alone, quiet and begging, then the beat drops on 'you keep on walking'"* — and the lyric cue now says **begging** and **unhurried** in as many words |
| 🔑 *"the pacing is perfect"* | **Duration 190 s**, and the cast tail verbatim: *"eight-bar bursts traded between them, heavy and unhurried, every bar landing clean and on the grid, never hurried and never dragging"* |
| *"chorus being quick keep that"* | *"The hook comes quick, a room of men saying it with him flat and low, words only"* |

Plus the anti-ooh clause, which stays because r71 was the round that introduced it.
✅ **And the Lyrics box is identical across all five lanes** — when the vocal is the thing being
kept, the lyrics box has no business varying.

### 🎛 Free — and the lane clause goes FIRST

Each lane's world is written **before** the frozen spine, because Suno weights the opening tokens
hardest: the first thing it reads is the thing that differs. Each lane moves its **drums**, its
**instrument family and that family's job**, and its **production sentence**.

| Lane | | The world |
|---|---|---|
""")
for k in lanes: W(f"| `{k}` | {KIND[k]} | {ONE[k]} |\n")
W("""
✅ **Asserted in the build:** the longest shared run between any two Style boxes is **498 chars — and
it is the frozen spine, exactly**. No drum language, no instrument and no production sentence is
shared between any two lanes. (This is deliberately *not* the sub-10% BOLD target: r69 was rejected
for sharing 68–74% of a *body nobody asked to freeze*, whereas here 61–63% is shared **because Jack
listed it**.)

### The references behind the two experimental sound-designs

| Lane | What went in the box | Source |
|---|---|---|
| `machine` | *metallic clicks layered on the snares · hi-passed pots and pans on the kick · banging pipes and a construction-site clang* — the actual practitioner recipe for industrial drums, rather than the word "industrial" | [DOA](https://www.dogsonacid.com/threads/how-to-make-industrial-style-drums.640083/), [ModeAudio](https://modeaudio.com/product/bolt-industrial-drum-samples) |
| `square` | *detuned square-wave stabs and a gliding sine lead · very clear single hits and no percussion layers · the filter opening further at every turn · a twisty gliding bass* — grime's own synthesis, including Wiley's "twisty synth bass" and the genre's refusal to layer percussion | [Attack](https://www.attackmagazine.com/technique/tutorials/grime-synth-basics/), [MusicRadar](https://www.musicradar.com/tuition/tech/22-pro-grime-production-tricks-170428), [Wikipedia](https://en.wikipedia.org/wiki/Grime_music) |

⚠️ **`dubecho` carries an extra ban block** — the repo's standing warning that a dub layer smuggles
in its own vocalist (`ragga MC, toasting, Jamaican accent, dancehall vocal`) and, with an offbeat
chord, the whole `ska, oompah, brass band` family. All banned in that lane only, so the dub
*production* arrives without the dub *voice*.
⚠️ **And the grime-synth lane never says "grime" as a genre word or names a tempo but 174** — naming
the genre drags the track toward 140 BPM.

### Settings

v6 · Style Influence **75** · Variety **Off** · Max Mode off · Vocal Gender Male · Personalize off ·
no Voice · **Duration 190 s** · workspace `camping-Jack` · weirdness **40 and 60**. 10 Creates, 20 takes.

🔑 **The liked take is a w40.** Jack's three previous favourites were w60; this one is not, so
weirdness remains genuinely unsettled and the pair still runs.

### Generated 2026-09-23 — 10 Creates, 10 clean. Credits 8,880 → 8,780

| Lane | | w40 | w60 |
|---|---|---|---|
""")
for k in lanes: W(f"| `{k}` | {KIND[k]} | {cell(k,0)} | {cell(k,2)} |\n")
W("""
✅ **Ten Creates, ten clean**, 10 credits each. ✅ **Every measured take came back 3:09–3:11 against
a 3:10 target** — 190 s has now been on target 36 times out of 36 across r70–r73, and it is the
setting Jack has called *"perfect"* by ear.

⬜ **Not heard.** Three questions:
1. 🔑 **Did the frozen spine survive five different worlds?** If the voice, the begging opening or
   the quick hook changes character in a lane, the lane's own language is overriding it — and the
   fix is in that lane's clause, not in the spine.
2. **Orchestral or free?** `spiccato` and `harpcello` are the two he asked for; `dubecho`, `machine`
   and `square` are the experiments. This is the round that says whether the orchestra is actually
   wanted or was a habit.
3. **Which world?** Any of the five can become the next spine, and the frozen block travels with it
   unchanged.

""")
for k in lanes:
    W(f"### r73 {k} atom\n\nStyle:\n\n```\n{S[k]['style']}\n```\n\nExclude styles:\n\n```\n{S[k]['exclude']}\n```\n\n")
W(f"### r73 lyrics (identical in all five lanes)\n\n```lyrics\n{S['spiccato']['lyrics']}\n```\n\n---\n\n")
src=open(OUT).read(); anchor="## v6.64 Round r72"
assert anchor in src
open(OUT,'w').write(src.replace(anchor, b.getvalue()+anchor, 1))
print("✅ inserted §v6.65")
