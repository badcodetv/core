import json, io, os
OUT='/home/jackt/projects/badcode/badcode/docs/stories/camping/songs/camping.md'
lanes=['terrace','answer','raw']
S={k:json.load(open(k+'.json')) for k in lanes}
TAKES={
 'terrace':[('b4276153-b9ea-46a4-b18a-d36deb6b5696','3:04'),('89c1dff6-a2ef-4f36-b2b5-a33d5f642e54','3:04'),
            ('ac657394-07c3-4896-ada3-361f2c7b562e','3:05'),('c3afdf1d-d8f8-4109-8bfa-0f0a21eca907','3:06')],
 'answer': [('545f6755-bfd6-4a13-b43b-91c60d30190f','3:05'),('e5995492-db0c-4092-96f0-dc026cfe8333','3:04'),
            ('50f30fd1-9176-47c9-b7e9-e0f0860cd72c','3:04'),('00c17fdc-6f52-47d3-9418-82d1103ccacf','3:04')],
 'raw':    [('7b91af7f-4e7c-4e63-b8ea-631adef9ac7d','—'),('c6b9e8b0-1c09-4d39-b528-3605606ababe','—'),
            ('9a0c4019-d080-415c-8fa1-ac4c198c3f78','—'),('6da84046-17cf-4246-9e45-35a173005266','—')],
}
SHORT={
 'terrace':'the hook chanted flat on ONE note by a crowd, shouted not sung — nothing left to tune',
 'answer':'no hook melody at all: he says the line, the room barks the last three words back',
 'raw':'the hook still sung, but by ONE man, rough, flat and cracked, nobody behind him',
}
def cell(k,i):
    return ' · '.join(f'[{s[:8]}](https://suno.com/song/{s})'+(f' ({d})' if d!='—' else '') for s,d in TAKES[k][i:i+2])

b=io.StringIO(); W=b.write
W("""## v6.59 Round r67 — the liked take, de-cheesed: kill the autotune hook, slow the rap a notch, push the grime (2026-09-23)

**Brief, Jack 2026-09-23, on [1b2aa79c](https://suno.com/song/1b2aa79c-9b06-44e8-b463-63809306060b)
(= `camping-r66-chorale-v6-w60`):** *"this song is cool i like the vibes, please get rid of the
autotune chorus it is too cheesy, please slow down the rap a bit, but it should stay fast, just not
too fast, we should hear what he says, also add more of a grime voice to it. try a few variations."*

🔑 **This is the round the sheet has been waiting for: the first DEEPENING round.** r49–r66 all
widened. Jack has now named a take, so the spine is `chorale` and nothing else moves except the
three things he asked for.

### 🔴 The finding: `autotune` was ALREADY banned, and it still arrived

`autotune` sat in r66 `chorale`'s exclude box the whole time. The chorus came back autotuned anyway,
because **the Style box asked for it in the positive**:

| What r66 said | What it routes to |
|---|---|
| *"a room of men **singing** the hook line together in **bare block harmony**"* | a tuned, stacked gang vocal — the EDM-chorus centroid |
| *"half **singing** line ends"* (cast tail) | a pitched lead on the hook |
| `[Chorus \| … half sung and half chanted …]` ×3 | the lyric cue voting for the same thing, and cues out-vote the Style box |

🔑 **A ban does not beat a positive instruction; it only removes an option the model was not already
being pushed toward.** Our own knowledge base says the same thing from the other side — *prefer the
positive form and take the instrument risk* — and the practitioner guides say the reliable fix is a
**three-part stack**: a positive Style-box target, matching section tags, and the exclude terms last
([Jack Righteous](https://jackrighteous.com/en-us/blogs/guides-using-suno-ai-music-creation/stop-suno-adding-crowd-vocals-choirs-backing-voices),
[SongSmith](https://songsmith.studio/blog/suno-negative-prompts-guide)). That is what r67 does, and
the lane axis is **which positive form** to use.

### The three levers, one per complaint

| Complaint | Lever | Why this one |
|---|---|---|
| **"autotune chorus, too cheesy"** | every word in the *singing* family deleted from the hook description in **all three boxes**, replaced by a positive un-tunable form (per lane), then the ban list widened to `pitch-corrected vocals, tuned vocals, vocoder, stacked harmonies, layered vocals, vocal doubles, EDM vocal, pop hook, anthemic chorus, singalong, cheesy` | deleting beats adding; the ban is the third line of defence, not the first |
| **"slow the rap a bit, still fast, we should hear what he says"** | 🔑 **Duration 175 → 185 s**, plus `rapid-fire` **removed from the Style box** (and left unbanned) for *"spitting fast but every word clear, never rushing and never slowing for a punchline"*, plus a clarity clause in the mix sentence and `mumbled, buried vocals, drowned in the mix, heavy vocal reverb` banned | Duration is the only pacing lever ever proven obeyed on this song, and 185 s sits inside the settled 175–190 working bracket. 🔑 *"We should hear what he says"* is half a **mix** problem, not only a speed one |
| **"more of a grime voice"** | `UK grime MCs` moved to the **first three tokens** of every Style box; `London pirate-radio energy, bars spat down the mic`; and — the strongest lever — **every lyric label renamed `gruff MC` → `gruff grime MC`, `cold MC` → `cold grime MC`** | Suno weights the opening tokens heavily, and the lyrics box out-votes the Style box on casting (§v6.51). Sixteen grime-labelled cues now vote for the pool every section |

🔴 **Excludes audit — and one deliberate shrink.** The exclude box went **835 → 731 chars**. Our own
rule: *if the Exclude box holds more words from a family than the Style box does, the Style box
loses*. With a round whose whole point is pushing a vocal pool harder, the bloated cross-lane ban
list inherited from r66 was dead weight, so every ban that was only there to keep r66's four lanes
apart came out. What stayed: the pacing guards, the drum-loss guards that r64's failure bought, the
aggression bans Jack has **not** complained about since, and the bed bans.
⚠️ **Noted, not acted on:** `air horns` and `snarling` are grime-set signatures still banned as
aggression. If a lane reads as not-grime-enough, they are the first two to lift.

✅ **Not one lyric word changed** — cues stripped, words compared byte for byte, 80 lines held, and
the build asserts `half sung` / `half chanted` are gone and that ≥12 `grime MC` labels are present.

### The three lanes — all identical except HOW the hook is performed

| Lane | The hook | The risk it tests |
|---|---|---|
| `terrace` | a crowd of men on **one flat note**, shouted not sung, never harmonised | nothing is left to tune — but does it stop being a hook? |
| `answer` | **no melody at all**: he says the line, the room barks the last three words back | pure Hallelujah antiphony, de-pitched — does the chorus still lift? |
| `raw` | still **sung**, but by one man, rough, flat and cracked, nobody behind him | 🔑 the hedge — Jack has liked a sung chorus since `1127446d`; he objected to **autotune**, not to singing |

### Settings

v6 · Style Influence **75** · Variety **Off** · Max Mode off · Vocal Gender Male · Personalize off ·
no Voice · **Duration 185 s** · workspace `camping-Jack` · weirdness **40 and 60**. 6 Creates, 12 takes.

### Generated 2026-09-23 — 6 Creates, 6 clean. Credits 9,260 → 9,200

| Lane | What changed about the hook | w40 | w60 |
|---|---|---|---|
""")
for k in lanes: W(f"| `{k}` | {SHORT[k]} | {cell(k,0)} | {cell(k,2)} |\n")
W("""
✅ **Six Creates, six clean** — 10 credits each, balance read before and after every one.

✅ **And Duration 185 s behaved perfectly: eight of eight measured takes came back 3:04–3:06 against
a 3:05 target.** 🔑 That is worth recording next to r66, where a **175 s** target overshot twice in
sixteen takes. Two rounds now point the same way: **the tighter the target squeezes the same ~60
lines, the likelier Suno treats it as a suggestion.** 185 s is both the pacing Jack asked for and
the more reliable number.

⬜ **Not heard.** Three questions, in order:
1. 🔑 **Is the cheese gone?** If any lane still comes back tuned, the ban was never the problem and
   the next move is the lyric cue, not the exclude box.
2. **Which un-tuned hook still lifts?** `terrace` (a crowd on one note) · `answer` (barked
   response) · `raw` (one cracked voice). If `raw` wins, Jack's sung chorus survives and only the
   *tuning* ever needed to go.
3. **Is the rap now audible without dragging?** 185 s is one notch slower than the take he liked.
   If it drags, the answer is 180, not a rewording.

""")
for k in lanes:
    W(f"### r67 {k} atom\n\nStyle:\n\n```\n{S[k]['style']}\n```\n\nExclude styles:\n\n```\n{S[k]['exclude']}\n```\n\nLyrics:\n\n```lyrics\n{S[k]['lyrics']}\n```\n\n")
W("---\n\n")
src=open(OUT).read()
anchor="## v6.58 Round r66"
assert anchor in src
open(OUT,'w').write(src.replace(anchor, b.getvalue()+anchor, 1))
print("✅ inserted §v6.59")
