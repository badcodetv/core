import json, io, os
OUT='/home/jackt/projects/badcode/badcode/docs/stories/camping/songs/camping.md'
lanes=['violin','pizz','cello']
S={k:json.load(open(k+'.json')) for k in lanes}
T={
 'violin':[('6e71e777-e10d-4ea6-9584-376937502324','3:04'),('0df113c2-eca0-4da6-9b73-e20b5c68cdbe','3:06'),
           ('e425a5b3-4dc3-4141-81ce-211ac6c73f52','3:03'),('87aeee9c-3574-43d5-954e-c77ddffa6214','3:04')],
 'pizz':  [('2f3cd143-4247-4a48-b5ca-2e06454b64ce','3:05'),('030872cf-bc25-47de-831e-9cb628980b2b','3:05'),
           ('5764c19f-e44d-4d06-8c39-fb39841a827c','3:05'),('e986cabe-370c-4afd-b445-8515f4df1965','3:05')],
 'cello': [('711e75d0-1af9-49ee-97cb-438cddb230c7','—'),('9dbac783-dc43-4a28-96b1-11b35fc689b2','—'),
           ('2000687f-348b-4f5c-80ca-dc430d8d3632','—'),('3a6c47d4-58ea-42a6-9fc2-fe06013a9264','—')],
}
JOB={'violin':'**answers** the MC in the gap at the end of every bar, and doubles the bassline an octave up in the drops',
     'pizz':'**plays the break\'s own pattern back** in short plucked sixteenths — percussion, not melody',
     'cello':'**doubles the sub an octave up** in long bowed lines — weight from register, not from volume'}
def cell(k,i): return ' · '.join(f'[{s[:8]}](https://suno.com/song/{s})'+(f' ({d})' if d!='—' else '') for s,d in T[k][i:i+2])

b=io.StringIO(); W=b.write
W("""## v6.60 Round r68 — the orchestra back with a job, the voice turned down, the record made palatable (2026-09-23)

**Brief, Jack 2026-09-23, again on [1b2aa79c](https://suno.com/song/1b2aa79c-9b06-44e8-b463-63809306060b):**
*"remove the air horns and snarling, the grime voice should be aggressive but not so much so turn it
down, he shouldn't shout. Also we have lost the orchestral elements so add some back and take
another look at this song, and tone down the loud parts and the cheesy parts, make it more
palatable."*

Built on the r67 `answer` atom (§v6.59), which already carries the de-cheesed hook, Duration 185 s
and the grime push. Four things change as constants; the **lane axis is which orchestral element
comes back and what job it does.**

### ✅ The two lifted bans — flagged last round, confirmed this round

`air horns` and `snarling` were flagged at the end of r67 as grime-set signatures still banned by
the "less aggressive" sweep. Jack has now removed them by name. **That is the sixth and seventh ban
found fighting the brief, and the first two caught *before* they cost a round.** Both are out.

### 🔴 "We have lost the orchestral elements" — correct, and here is exactly where they went

The `chorale` lane Jack likes is the **least orchestral of r66's four**. Its only non-D&B instrument
is *"a church organ holds chords at the turns only"* — the piano and the solo violin that open
`1127446d`, the two things he has named as things he likes, are in the `odejoy`, `mars` and `fate`
lanes and **not** in this one. So the diagnosis is exact, and the fix is to put them back **without
repealing Ruling 1**.

🔑 **Ruling 1 stands: the orchestra is a garnish with a JOB, never a bed, never the lead**
(four measurements: a full film-score bed gives the weakest low end, the smallest dynamic range and
the *slowest* rap). So every lane opens on a **felt piano and its own string element**, and that
element then gets a **rhythmic or arrangement job against the break** for the rest of the record.
The bed bans (`orchestral bed`, `symphony orchestra`, `string section`, `sustained string pad`,
`lush pads`, `epic trailer music`) stay in all three lanes.
⚠️ **Which is why lane 2 says "plucked cellos and violas" and not "string section"** — the ban would
have fought the lane, so the lane is worded around it rather than the ban being lifted.

### 🔑 "Aggressive but turned down, he shouldn't shout" — the Flowdan register

The research names the thing precisely: Flowdan's *"distinctive murky low-pitch timbre, several
octaves deeper than anyone else… the personification of dread"*, and a flow built on *"drawing out
and repeating single words with bone-chilling menace"*
([RBMA](https://daily.redbullmusicacademy.com/2018/08/voices-of-pirate-radio-grime/),
[Wikipedia](https://en.wikipedia.org/wiki/Grime_(music_genre))). **That is aggression carried by
pitch and menace instead of volume**, which is exactly the note.

So r43's cast sentence keeps its verbatim core (*"loud and in front"* is a **mix position**, not a
shout) and the tail becomes *"aggressive but held back, low and murky, menace not volume, never
raising their voices, fast and clear."* 🆕 And `shouting, shouted vocals, hollering, bellowing` are
banned for the first time, alongside the `screaming, roaring` that were already there.

### 🔑 "Tone down the loud parts… make it more palatable" — dynamics, not level

🔴 **The trap, stated rather than walked into:** r64 was told to take the aggression out, softened
its production sentence (*"patient rather than violent"*) and **lost the drums entirely**. Turning
this record down the naive way would repeat that exactly.

The research says what "too loud" usually is, and it is not the fader. Harshness lives in the
**2–6 kHz** band and sustained energy there is what produces listening fatigue
([Levels](https://www.levelsmusicproduction.com/blog/why-do-my-high-frequencies-sound-harsh),
[Mastering The Mix](https://www.masteringthemix.com/blogs/learn/understanding-the-different-frequency-ranges)),
and **brickwalling squashes away the dynamic range so everything sounds the same volume**, costing
punch and detail ([iZotope](https://www.izotope.com/community/blog/loud-mix),
[MasteringBOX](https://www.masteringbox.com/learn/dynamic-range-and-loudness)). Our own toolkit
already says Suno's harshness *"sits exactly where D&B lives — brittle cymbals, sizzling hats,
sibilance in 2–6 kHz."*

| Where it was loud | r67 | r68 |
|---|---|---|
| the drop | *"the drums alone and enormous"* | *"whole and controlled rather than louder"* |
| the cycles | *"it empties and **slams back** three more times"* | *"it falls to almost nothing and returns three more times, **the quiet parts really quiet**"* |
| the room | *"a stadium"*, *"barks"*, *"shouted not sung"* | *"low and close, half-spoken in unison, **a pub not a stadium**"* |
| the top end | — | 🆕 *"hats brushed back"* + `sizzling hats, sibilant, harsh, abrasive` banned |
| the master | — | 🆕 *"mixed with headroom, never brickwalled"* + `brickwalled, over-compressed, maximised, loudness war, wall of sound` banned |
| the cheese | `cheesy` | 🆕 `corny, stadium rock, euphoric, football chant` added |

🔑 **The drums are NOT described as quieter anywhere.** `Drums and sub loudest… never in front` is
still in every lane, verbatim. **The loudness comes out of the mastering and the peaks; the drums
keep their place in the balance.** That is the only way to give Jack what he asked for without
buying r64's failure a second time.

✅ **Not one lyric word changed** — asserted byte for byte, 80 lines, and the build fails if
`barking`, `enormous` or `slams back` survive anywhere in the cues.

### The three lanes — identical except which instrument returns and what it does

| Lane | What opens with the piano | Its job for the rest of the record |
|---|---|---|
""")
for k in lanes:
    op={'violin':'a lone violin','pizz':'plucked cellos and violas ticking','cello':'one low cello holding'}[k]
    W(f"| `{k}` | {op} | it {JOB[k]} |\n")
W("""
### Settings

v6 · Style Influence **75** · Variety **Off** · Max Mode off · Vocal Gender Male · Personalize off ·
no Voice · **Duration 185 s** (unchanged — Jack has not commented on r67's pacing yet) · workspace
`camping-Jack` · weirdness **40 and 60**. 6 Creates, 12 takes.

### Generated 2026-09-23 — 6 Creates, 6 clean. Credits 9,200 → 9,140

| Lane | The orchestral job | w40 | w60 |
|---|---|---|---|
""")
for k in lanes: W(f"| `{k}` | {JOB[k]} | {cell(k,0)} | {cell(k,2)} |\n")
W("""
✅ **Six Creates, six clean** — 10 credits each, balance read before and after every one.
✅ **Duration 185 s held again: eight of eight measured takes at 3:03–3:06 against a 3:05 target.**
Across r67 and r68 that is **16/16 within ~2 s**, against two overshoots in sixteen at 175 s.
**185 s is now the settled number for this song.**

⬜ **Not heard.** Four questions, in order:
1. 🔑 **Are the drums still there?** This round deliberately took loudness out of a record that r64
   proved is easy to un-make. If the D&B has gone soft, the culprit is the *mastering* language and
   it comes straight back out — the balance sentence is untouched.
2. **Is the orchestra back, and is it a garnish or a bed?** If any lane sounds like a film score,
   Ruling 1 was broken by the job description, not by the instrument.
3. **Which job reads best** — answering (`violin`) · percussion (`pizz`) · register (`cello`)?
4. **Is the voice aggressive without shouting?** If it now sounds bored rather than menacing, the
   lever is `low and murky, menace not volume` going further, not the cast sentence coming back.

""")
for k in lanes:
    W(f"### r68 {k} atom\n\nStyle:\n\n```\n{S[k]['style']}\n```\n\nExclude styles:\n\n```\n{S[k]['exclude']}\n```\n\n")
W(f"### r68 lyrics (shared — the r67 words, cues turned down)\n\n```lyrics\n{S['violin']['lyrics']}\n```\n\n---\n\n")
src=open(OUT).read(); anchor="## v6.59 Round r67"
assert anchor in src
open(OUT,'w').write(src.replace(anchor, b.getvalue()+anchor, 1))
print("✅ inserted §v6.60")
