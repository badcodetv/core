import json, re, pathlib
REPO = pathlib.Path('/home/jackt/projects/badcode/badcode')
SHEET = REPO / 'docs/stories/camping/songs/camping.md'
OUT = REPO / 'scripts/suno/.tmp/r53'
src = SHEET.read_text()
start = src.index('### r52 sinogrime atom'); end = src.index('### r52 bleep atom')
lyrics = re.findall(r'\n```[a-z]*\n(.*?)\n```\n', src[start:end], re.S)[2]
assert '[gruff MC]' in lyrics and lyrics.count('I can\'t live like this forever') >= 8

STYLE = (
 # 1. genre + BPM in the first tokens (weighted heaviest)
 "Dark UK drum and bass at 174 BPM, grime over it, minor key. "
 # 2. gear one — the opening, three lines only
 "It opens with no drums: a lone sad piano and a solo violin, the first MC quiet and emotional over them, "
 "but only for three lines. "
 # 3. gear two — the drop, everything arriving at once
 "Then the drop: the full beat slams in at once, chopped amen breaks and tears at every turn, skippy two-step "
 "shuffles in the roll, a dark Reese sub growing meaner every section. "
 # 4. the garnish, explicitly scoped so it cannot become the bed
 "Cheap synth strings stay at the edges as colour only, never a film score, never the bed. "
 # 5. balance — the fix for 'not enough drum and bass'
 "The drums and the sub are the loudest thing in the mix throughout. "
 # 6. unity + continuity
 "The strings and the breaks are one piece of music, not a remix, and the breaks never stop, not one bar. "
 # 7. the hook Suno invented and Jack kept
 "A big sung chorus hook returns three times, the only sung thing. "
 # 8. production
 "Night-bus melancholy, cold and grimy, dry close vocals, unpolished. "
 # 9. cast — the standing grime rule
 "Two English grime MCs trade the verses, loud and in front, one gruff and raw, one clipped and cold, both "
 "spitting fast, furious and emotional, voices close to cracking, rapid-fire on the 174 grid and never slowing "
 "for a punchline.")

EXCLUDE = (
 # nationality — the r19 list's strongest, kept whole
 "American accent, American vocal, Southern drawl, country vocal, twang, americana, US rap, American rap, trap, "
 "boom bap, blues, Delta blues, gospel, soul singer, "
 # voice faults
 "teenage voice, boyish voice, falsetto, autotune, female vocal, choir, "
 # 🔑 the delivery Jack disliked, attacked as DELIVERY - never as tempo
 "laid-back, chill, mumbled, lazy flow, steady rap pace, measured delivery, spoken word, "
 # genre faults
 "jump up, wobble bass, dubstep, EDM drops, neurofunk, happy, uplifting, major key, comedic, novelty, parody, "
 # classical BED only - never the bare word violin, piano or classical
 "orchestral film score, epic trailer music, brass braams, war drums, full orchestra, symphony orchestra, "
 "string section, lush strings, chamber music, baroque, concerto, orchestral bed, "
 # mix
 "mono mix, muddy mix, crowd noise, audience, applause, glossy production, radio pop")

spec = {"style": STYLE, "exclude": EXCLUDE, "lyrics": lyrics,
        "model": "v6", "title": "camping-r53-optimised", "workspace": "camping-Jack",
        "styleInfluence": 80, "weirdness": [30, 60], "durationSec": 195,
        "variety": "off", "maxMode": False, "vocalGender": "male", "personalize": False}
(OUT / "optimised.json").write_text(json.dumps(spec, indent=2))
print('style', len(STYLE), 'exclude', len(EXCLUDE), 'lyrics', len(lyrics))
assert len(STYLE) <= 1000, len(STYLE)

SECTION = f"""## v6.45 Round r53 — `1127446d` optimised, read off its own page (2026-09-19)

**Brief, Jack 2026-09-19:** *"please go to this
[song](https://suno.com/song/1127446d-abe8-4079-9bbe-6b281e12aa74), look at all the prompts and
optimise it as much as possible."*

### ✅ Read live off the song page, not off this sheet

Scraped from `suno.com/song/1127446d-…` on 2026-09-19 with the create tab's own browser. **Two
things are now confirmed that the sheet only claimed:**

1. **Its Style and Exclude boxes are the r19 `reese` boxes, byte for byte** — including `-piano`,
   `-slow tempo`, `-half time`, `-tempo change`. ✅ The repo's claim was right.
2. 🔑 **Its Lyrics box has NO CHORUS, and its `[Intro]` cue reads *"a solid, full drum and bass beat
   and heavy sub bass from the very first second, no vocal yet"*.** So **both** of the things Jack
   likes most — the slow piano opening and the sung chorus — are **inventions by Suno at weirdness
   60, against an instruction that said the opposite.** §v6.39 inferred this from the boxes; this is
   the direct confirmation, off the take's own page.

### 🔑 The pivot this round makes

While the prompt was wrong, **low adherence and high weirdness were doing the work** — every liked
feature was drift. Now that the prompt *contains* those features, adherence stops being the enemy
and becomes the tool. So the optimisation is not only better words, it is a **different slider
posture**: Style Influence **70 → 80**, and a proper pair at weirdness **30 and 60** to measure
whether the drift is still needed. Practitioner consensus for v6 is Style Influence **75-85** when
you want to be obeyed, and Variety **0** so the box is not rewritten
([Jack Righteous](https://jackrighteous.com/en-us/blogs/guides-using-suno-ai-music-creation/how-to-use-suno-s-advanced-sliders-weirdness-style-audio-influence),
[Suno help](https://help.suno.com/en/articles/6141377),
[sunostyles](https://sunostyles.com/blog/suno-v6-settings)).

### Every change, and why

| Change | From → to | Why |
|---|---|---|
| **`piano` un-banned** | exclude → gone | 🔴 The single most self-defeating word in the original. The piano he loves arrived *despite* a ban on it |
| **`slow tempo`, `half time`, `tempo change` un-banned** | exclude → gone | They fight the three-line emotional opening and the build-then-drop shape he described |
| **The slow delivery** | `steady rap pace, not double time and not half time` (Style) → `rapid-fire on the 174 grid and never slowing for a punchline` | The one thing he disliked is the one thing the old prompt **asked for**. Attacked as a positive, never as a tempo ban |
| **Slowness banned as delivery instead** | added `laid-back, chill, mumbled, lazy flow, steady rap pace, measured delivery` | The safe place to put it — delivery words cannot strangle the opening |
| **Cast** | storyteller + BBC newsreader → **the r43 grime MCs** | Jack's standing rule, 2026-09-19 |
| **The opening written in** | nothing → `no drums: a lone sad piano and a solo violin… only for three lines` | Was drift; now instruction |
| **The chorus written in** | no chorus in the box → `[Chorus]` x3 in the lyrics + `a big sung chorus hook returns three times` | Was drift; now instruction |
| **Strings scoped** | `cheap synth strings` floating → `stay at the edges as colour only, never a film score, never the bed` | His classical ruling. `cheap synth strings` is kept because it is the layer he liked (r43) |
| **Balance stated** | nothing → `the drums and the sub are the loudest thing in the mix throughout` | "not enough drum and bass" is a **balance** complaint; no previous round stated balance |
| **Continuity stated** | nothing → `the breaks never stop, not one bar` | r49 measured 12-14 s holes in lanes that did not say it |
| **Structure** | one 900-char run-on sentence | rebuilt as genre → gear one → gear two → garnish → balance → unity → hook → production → cast. Suno weights the first tokens hardest |

### Settings

v6 · Style Influence **80** · Variety **Off** · Max Mode off · Vocal Gender **Male** · Personalize
off · no Voice · **Duration 195 s** · workspace `camping-Jack` · **Weirdness 30 and 60 — a real
pair**, because whether the prompt still needs drift is exactly the open question.

### Generated 2026-09-19 — 2 Creates, 4 takes. Credits 10,620 → 10,600

| Cell | Takes |
|---|---|
| **w30** — obey the new box | [cd5390c4](https://suno.com/song/cd5390c4-e16f-413c-9a6b-d650d7b6c28a) · [b1d92d95](https://suno.com/song/b1d92d95-73ee-4396-a907-42271d49d0b3) |
| **w60** — the reference's own setting | [cfcb9195](https://suno.com/song/cfcb9195-8f53-488d-95d7-1295483115da) · [d0bbb0a3](https://suno.com/song/d0bbb0a3-e513-4468-87bd-d135665c7d31) |

🔑 **This pair answers a question no other round can:** if **w30 wins**, the prompt is now correct and
every future round can stop gambling on drift. If **w60 still wins**, something Jack likes is *still*
not written down, and the next job is to find out what.

### r53 optimised atom

Style:

```
{STYLE}
```

Exclude styles:

```
{EXCLUDE}
```

Lyrics:

```lyrics
{lyrics}
```

---

"""
i = src.index('## v6.44 Round r52')
s2 = src[:i] + SECTION + src[i:]
s2 = s2.replace("RESUME HERE — rounds r51 (§v6.43, the grime cast, no classical lane) and r52 (§v6.44, six researched fusions with a real lineage to 174) are both generated, 24 takes, 2026-09-19, waiting on Jack's ear; r49's takes are also unheard and r50 is superseded.",
 "RESUME HERE — r53 (§v6.45) is the optimised `1127446d` atom, generated as a real w30/w60 pair on 2026-09-19 and the most important thing to listen to; r51 and r52 (12 takes each) and r49 are also unheard, and r50 is superseded.")
SHEET.write_text(s2)
print('sheet: r53 inserted')
