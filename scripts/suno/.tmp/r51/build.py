import json, re, pathlib

REPO = pathlib.Path('/home/jackt/projects/badcode/badcode')
SHEET = REPO / 'docs/stories/camping/songs/camping.md'
OUT = REPO / 'scripts/suno/.tmp/r51'
src = SHEET.read_text()

# lyrics: identical to r50's (pull from the r50 liquid atom so they cannot drift)
start = src.index('### r50 liquid atom'); end = src.index('### r50 techstep atom')
lyrics = re.findall(r'\n```[a-z]*\n(.*?)\n```\n', src[start:end], re.S)[2]
assert '[gruff MC]' in lyrics and 'the whole arrangement arrives with them' in lyrics

# 🔑 the proven grime cast (r43 §v6.35), now a standing rule (Jack 2026-09-19)
CAST = ("Two English grime MCs trade the verses, loud and in front, one gruff and raw, one clipped and cold, "
        "both spitting fast, furious and emotional, voices close to cracking, rapid-fire on the 174 grid and "
        "never slowing for a punchline.")
OPEN = ("It opens with no drums - a lone sad piano and a solo violin - the first MC quiet and emotional over "
        "them, but only for three lines.")
def DOM(x):
    return f"The drums and the sub are the loudest thing in the mix throughout; the {x} sits under them, never in front."

BASE_EX = ("American accent, American vocal, Southern drawl, country vocal, twang, americana, US rap, American rap, "
 "trap, boom bap, teenage voice, boyish voice, autotune, female vocal, laid-back, chill, mumbled, lazy flow, "
 "spoken word, happy, uplifting, major key, comedic, novelty, parody, mono mix, muddy mix, crowd noise, applause, "
 "jump up, wobble bass, dubstep, EDM drops, glossy production, radio pop, "
 # 🔴 classical BED words only — never the bare `violin` or `classical`, which would kill the opening Jack likes
 "orchestral film score, epic trailer music, brass braams, war drums, full orchestra, symphony orchestra, "
 "string section, lush strings, chamber music, classical arrangement, baroque, concerto, orchestral bed")

LANES = [
 dict(key='liquid', fam='Rhodes',
  style=("Liquid drum and bass led by a warm Rhodes electric piano. " + OPEN +
   " Then the drop: 174 BPM UK drum and bass at full weight, chopped amen breaks, skippy two-step shuffles folded "
   "into the roll, a deep rolling sub. The Rhodes plays on through every verse and over every "
   "drop; the Rhodes and the breaks are one piece of music, not a remix, and the breaks never stop, not for one bar. "
   + DOM('Rhodes') + " Warm and soulful under bleak words, night-bus melancholy, raw and never glossy. "
   "The sung chorus hook comes back three times. " + CAST),
  ex="soul diva, R&B vocal, smooth male singer, crooner, sung verses, melodic rap, liquid vocal hook, "
     "harmonica, slide guitar, industrial percussion, post-punk guitar, chorused guitar, Moog arpeggio, "
     "analogue synth lead, Motown horns, tambourine, brass band"),
 dict(key='techstep', fam='metal',
  style=("Techstep drum and bass, 1997 cold: metallic industrial percussion, detuned machine stabs, a growling "
   "Reese bass. " + OPEN +
   " Then the drop: hard 174 BPM breakbeats chopped to splinters, two-step shuffles in the roll, sub "
   "pressure that never lifts. The machine stabs hammer through every verse and over every drop - the metal and "
   "the breaks are one piece of music, not a remix - and the breaks never stop, not for one bar. " + DOM('metal') +
   " Hostile, claustrophobic, bone dry, corroded. A sung chorus hook returns three times. " + CAST),
  ex="robot vocal, vocoder, sci-fi spoken sample, MC hype chants, ragga toaster, rave stabs, "
     "Rhodes piano, harmonica, slide guitar, post-punk guitar, Moog arpeggio, Motown horns, tambourine, "
     "soul sample, brass band"),
 dict(key='bluesharp', fam='harmonica',
  style=("British blues-boom harmonica over drum and bass: one cracked amplified harmonica riff, a dirty slide "
   "guitar answering, 1966 Soho basement. " + OPEN +
   " Then the drop: 174 BPM UK drum and bass at full weight, chopped amen breaks, two-step shuffles, heavy "
   "rolling sub. The harmonica wails through every verse and across every drop - the harp and the "
   "breaks are one piece of music, not a remix - and the breaks never stop, not for one bar. " + DOM('harmonica') +
   " Filthy and hungover, valve-amp dirt against cold drums. The sung hook returns three times. " + CAST),
  ex="blues singer, howling vocal, Delta blues, twelve-bar, jug band, folk vocal, skiffle, "
     "Rhodes piano, industrial percussion, post-punk guitar, chorused guitar, Moog arpeggio, analogue synth lead, "
     "Motown horns, tambourine, brass band"),
 dict(key='postpunk', fam='guitar',
  style=("Bleak English post-punk guitar over drum and bass: one scraping chorused guitar figure, a high melodic "
   "bass line, a grey northern room. " + OPEN +
   " Then the drop: 174 BPM UK drum and bass at full weight, rolling amen breaks, two-step shuffles, heavy "
   "sub. The guitar figure repeats under every verse and rings out across every drop - the guitar "
   "and the breaks are one piece of music, not a remix - and the breaks never stop, not for one bar. " + DOM('guitar')
   + " Overcast, severe, tape-flat, nothing polished. The sung hook returns three times. " + CAST),
  ex="indie sung vocal, post-punk singing, baritone crooner, shoegaze vocal, goth vocal, "
     "Rhodes piano, harmonica, slide guitar, industrial percussion, Moog arpeggio, analogue synth lead, "
     "Motown horns, tambourine, brass band"),
 dict(key='analogue', fam='arpeggio',
  style=("Analogue 1980s synth hardware driving drum and bass: a Moog bass arpeggio in sixteenths, cold Juno pads and tape delay. " + OPEN +
   " Then the drop: 174 BPM UK drum and bass at full weight, chopped amen breaks, two-step shuffles, a "
   "growling sub under the arpeggio. The arpeggio runs unbroken beneath every verse and straight through every drop "
   "- the synths and the breaks are one piece of music, not a remix - and the breaks never stop, not for one bar. "
   + DOM('arpeggio') + " Airless and mechanical. A sung chorus hook comes round three times. " + CAST),
  ex="synthpop vocal, vocoder, robot vocal, 80s pop singer, new romantic croon, "
     "Rhodes piano, harmonica, slide guitar, post-punk guitar, chorused guitar, industrial percussion, "
     "Motown horns, tambourine, brass band"),
 dict(key='motown', fam='horn stabs',
  style=("Chopped 1960s soul records over drum and bass: cracked horn stabs, upright piano vamp, tambourine, "
   "vinyl crackle, cut like a 1995 jungle plate. " + OPEN +
   " Then the drop: 174 BPM UK drum and bass at full weight, amen breaks torn across the turns, two-step "
   "shuffles, deep rolling sub. The horn stabs punch through every verse and across every drop - the samples and "
   "the breaks are one piece of music, not a remix - and the breaks never stop, not one bar. " + DOM('horn stabs')
   + " Dusty, cracked, sampler-crunched. The sung chorus hook lands three times. " + CAST),
  ex="soul singer, gospel vocal, diva, doo-wop harmony, backing singers, female soul vocal, Motown singing, "
     "Rhodes piano, harmonica, slide guitar, post-punk guitar, chorused guitar, Moog arpeggio, analogue synth lead, "
     "industrial percussion"),
]

over=[]
for L in LANES:
    over.append((L['key'], len(L['style']))) if len(L['style'])>1000 else None
    spec = {"style": L['style'], "exclude": BASE_EX + ", " + L['ex'], "lyrics": lyrics,
            "model": "v6", "title": f"camping-r51-{L['key']}", "workspace": "camping-Jack",
            "styleInfluence": 75, "weirdness": [60], "durationSec": 195,
            "variety": "off", "maxMode": False, "vocalGender": "male", "personalize": False}
    (OUT / f"{L['key']}.json").write_text(json.dumps(spec, indent=2))
    print(f"{L['key']:10s} style={len(L['style']):4d} exclude={len(spec['exclude']):4d}")
print('grime cast chars:', len(CAST))
print('OVER CAP:', over)

GROUND = {
 'liquid':   ('warm Rhodes electric piano', 'the melancholy end of D&B itself — warm colour with the 174 spine untouched'),
 'techstep': ('metallic industrial percussion, machine stabs', '1997 techstep is the coldest, most hostile D&B there is — maximum contrast with the sad piano'),
 'bluesharp':('cracked amplified harmonica, slide guitar', '**replaces r50 `quartet`** — the British blues boom is filthy, bleak and completely un-classical'),
 'postpunk': ('scraping chorused electric guitar', 'the bleak English guitar tradition; the original Camping candidate&rsquo;s palm-muted figure, never tried over these words'),
 'analogue': ('Moog bass arpeggio, Juno pads', 'analogue hardware is a different way of making sound, not just a different genre'),
 'motown':   ('chopped soul horn stabs, upright piano', 'chopping old soul records IS how jungle was built — the fusion needs no defending'),
}
TAKES = {
 'liquid': ('4d396e56-b5f8-4608-a1f6-1566ca1216f9','382e8119-e63a-44c6-839b-7ea0c11ab0f2'),
 'techstep': ('8c196a2d-200b-4334-9ced-c5b233f2f0c1','c1008398-316e-46ba-92ed-943fa37c99e4'),
 'bluesharp': ('76cc57c8-cf55-403f-ad6a-dbd9db8167b9','fb2fb764-b20c-422e-8d68-d7860e3d0c0d'),
 'postpunk': ('ffbfd602-28be-40cd-81f2-e4b913fee69e','168d90df-f4ab-46fa-8552-b98daac70c17'),
 'analogue': ('dd5f5b66-bcd2-4f13-a257-374a39c1b437','3162bd05-b87e-452a-822e-0614e65f9280'),
 'motown': ('7120ef8f-ffbb-4601-ab51-1fac9f9f8f2f','72d43179-c7e7-40eb-a1e4-272f13f23a4f'),
}
rows = '\n'.join(f"| **`{L['key']}`** | {GROUND[L['key']][0]} | {GROUND[L['key']][1]} |" for L in LANES)
takerows = '\n'.join(
  f"| `{k}` | [{a[:8]}](https://suno.com/song/{a}) · [{b[:8]}](https://suno.com/song/{b}) |"
  for k, (a, b) in TAKES.items())
atoms = ''
for L in LANES:
    atoms += (f"### r51 {L['key']} atom\n\nStyle:\n\n```\n{L['style']}\n```\n\nExclude styles:\n\n```\n"
              f"{BASE_EX + ', ' + L['ex']}\n```\n\nLyrics:\n\n```lyrics\n{lyrics}\n```\n\n")

SECTION = f"""## v6.43 Round r51 — the grime cast, and no classical lane (2026-09-19)

**Two rulings, Jack 2026-09-19:** *"anytime there has been elements of classical, it has been too
much classical and not enough drum and bass, also always have the grime voice."*

### 🔴 Both rulings invalidated r50's Style boxes, so the round was re-run

r50 (§v6.42) was one hour old and wrong on both counts. It is kept as history — **its takes were
never heard and its cast is now out of policy** — and this round is r50's six lanes with the two
rulings applied. The lyrics, the settings and the spine are byte-identical to r50, so **the cast
sentence, the `quartet` lane and the mix instruction are the only things that moved.**

### Ruling 1 — classical is a garnish or it is nothing

This is the **fourth** confirmation of the same finding (r43's Zimmer rounds, r47 `cinematic`, r48
`grimescore`, now Jack's ear on the whole corpus), and the widest: it is not only film scores.

- 🔴 **The `quartet` lane is dropped.** A string quartet leading the Style box is the exact failure
  he named. It is replaced by **`bluesharp`** — British blues-boom harmonica and slide guitar, which
  is bleak and filthy without a bow anywhere near it.
- ✅ **What survives:** the **solo violin and piano in the three-line opening only** — he named "the
  violins and stuff" as a thing he likes about `1127446d`. Garnish at the edge, never the bed.
- 🔑 **The bans are at bed scale and never on the bare words `violin` or `classical`** — `full
  orchestra, symphony orchestra, string section, lush strings, chamber music, classical arrangement,
  baroque, concerto, orchestral bed`. Banning the instrument itself would kill the opening he likes:
  that is the documented stale-ban failure, where the Style box merely *looks* ignored.
- 🔑 **New in every lane, and the direct answer to "not enough drum and bass":** a positive mix
  instruction — *"The drums and the sub are the loudest thing in the mix throughout; the X sits under
  them, never in front."* Previous rounds only ever said the guest instrument plays *throughout*,
  which is a presence instruction, not a **balance** one. This is the first round to state the
  balance.

### Ruling 2 — always the grime voice

Standing from now on, not a per-round ask. Every lane carries **r43's proven cast sentence verbatim**
(§v6.35): *"Two English grime MCs trade the verses, loud and in front, one gruff and raw, one clipped
and cold, both spitting fast, furious and emotional, voices close to cracking, rapid-fire on the 174
grid and never slowing for a punchline."*

🔴 **r50 used the `1127446d` cast instead** — "a gravelly raspy older English storyteller… a clipped
BBC newsreader" — on the reasoning that the reference take should be copied whole. Wrong: the spine
to copy is the *arrangement*, and the voice is a separate, now-fixed decision. Lyric labels stay
`[gruff MC]` / `[cold MC]`.

### The six lanes

| Lane | Instrument family | Why this one |
|---|---|---|
{rows}

### Settings

v6 · Style Influence **75** · Variety **Off** · Max Mode off · Vocal Gender **Male** · Personalize
off · no Voice · **Duration 195 s** · workspace `camping-Jack` · Weirdness **60**. Titles
`camping-r51-<lane>-v6-w60`. Held byte-identical to r50 so the two rounds are directly comparable.

### Generated 2026-09-19 — 6 Creates, 12 takes, workspace `camping-Jack`

**Credits 10,740 → 10,680 — 10 per Create, 60 for the round.**

| Lane | Takes |
|---|---|
{takerows}

⚠️ **The balance moved by 80 credits between r50 and r51 with no Create of ours in between**
(10,820 → 10,740). Eight Creates happened from somewhere else — almost certainly Jack generating by
hand in the same account. Recorded because a mid-session balance drop is the documented tell for a
second session on the one create form.

⬜ **Not measured and not heard.** The r49 pass (breaks-present %, longest gap, pairwise timbre
distance) would now answer the exact complaint — **does the kit stay louder than the guest
instrument** — and it spends no download allowance.

{atoms}---

"""
marker = '## v6.42 Round r50'
i = src.index(marker)
s2 = src[:i] + SECTION + src[i:]
s2 = s2.replace("## v6.42 Round r50 — six instrument families on the `1127446d` spine (2026-09-19)",
 "## v6.42 Round r50 — six instrument families on the `1127446d` spine (2026-09-19) 🔴 SUPERSEDED BY r51\n\n"
 "> 🔴 **Out of policy within the hour.** Jack ruled on 2026-09-19 that **classical elements always\n"
 "> come out too classical and not enough drum and bass**, and that the **grime voice is standing**.\n"
 "> This round's `quartet` lane leads on a string quartet and all six lanes carry the `1127446d`\n"
 "> storyteller/newsreader cast, so every Style box here is superseded by §v6.43 r51. The twelve\n"
 "> takes were never heard. Kept for the reasoning and for the r51 diff — **do not re-run these boxes.**", 1)
s2 = s2.replace("RESUME HERE — round r50 (§v6.42, six instrument families on the 1127446d spine, 12 takes, 2026-09-19) is generated and waiting on Jack's ear; r49's twelve takes are also still unheard.",
 "RESUME HERE — round r51 (§v6.43, the grime cast and no classical lane, 12 takes, 2026-09-19) is generated and waiting on Jack's ear; r49's and r50's takes are also unheard, and r50 is superseded.")
SHEET.write_text(s2)
print('sheet: r51 inserted, r50 marked superseded')
