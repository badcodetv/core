# The Bank Robbery — Jack's song

Jack's own song (2026-10-20). A scratchpad that sits apart from the film's score, so nothing here
changes the cut, the score sheet or any other file.

## Still to decide (2026-10-21)

Jack is working out the lyrics and the style before anything goes into Suno.

Draft 2 at a glance:
- **Sound:** menacing British art-punk with a 1970s heist-movie funk groove, 120 BPM
- **Instruments:** twitchy distorted funk guitar, bouncing bass, handclaps, swirling psychedelic
  synths on the chorus
- **Voice:** male, flat half-spoken verses that tear into snarled shouts on the chorus, with a gang
  shouting back
- **Shape:** intro → 3 verses → chorus ×3 → spoken monologue → outro, about 3:10

Styles that could fit:
- **Keep it: heist-movie punk.** Tense and sarcastic; suits the Mister Red / Mister Blue story.
- **Grime / UK rap over a heist beat.** The most aggressive, closest to Jack's original verse. Still
  no double-time rap.
- **1970s cop-show funk.** Brass stabs, wah guitar, a narrator talking over it. The most cinematic;
  plays the robbery as a film.
- **Drum & bass.** The BadCode default, but draft 2 bans it on purpose.

Open questions:
- Which lyric lines to keep, cut or make gorier?
- Which style?

## Possible styles

### Maybe: 1970s cop-show funk (2026-10-21)

Jack wants to keep this one as a maybe. Brass stabs, wah guitar, a narrator talking over it: the
most cinematic option, and it plays the robbery as a film. Not tried yet. The Style box below is
written but unheard.

```
Gritty 1970s cop-show funk soundtrack, 104 BPM: stabbing brass section, wah-wah guitar, a fat rumbling bassline, live breakbeat drums with bongos and congas, a breathy low flute stalking the verses, tense string swells on the chorus. Male lead in a hard deadpan spoken narration on the verses that breaks into shouted lines on the chorus, a gang of voices shouting back. Menacing, played completely straight.
```

Exclude Styles (draft 2's list, audited: `orchestral` dropped because this style asks for strings;
the punk lane's sounds added):

```
comedy, novelty, parody, kazoo, cartoon, rap, hip hop, trap, double-time, fast rap, punk, new wave, cheerful, drum and bass, EDM, autotune, choir, gospel, country, power ballad, smooth R&B, disco
```

## Draft 3 (2026-10-21)

Jack's note on draft 2: "Please make it more gritty, gorier, agressive, there is too much of the
story in there."

What changed: the film's story is mostly gone (no Mister Red and Mister Blue, no pallet, no cleaner,
no beach, no town tied to a chair). The song is now a home invasion told straight, with the economics
as hints: printing ("pumping it in"), the pound thinning, rent, wages standing still, whoever gets the
new money first. Jack's own lines are kept word for word. Immigration is still never called fake
("some of what they shout about is real"). Shorter, at 2:50.

Style: still open. Use draft 2's punk Style box or the cop-show funk maybe above; draft 2's Exclude
Styles box carries over. Settings as draft 2 except Duration **2:50**. Unheard, nothing generated.

### Lyrics

```lyrics
[Intro]
They say you can't just walk in and take the money
watch me
(on the floor) on the fucking floor
nobody move

[Verse 1]
Crowbar in the door of the house you never got
missing teeth on the cold tiles, and they're taking the lot
no masks these lot have lost the plot
printing away, bag's full, bloody nails and your bag pulled

empty pockets and got a hole in the lung
coughing up blood by the end of the month
rent letter's red and it's nailed to the door
you worked the whole week and the week's worthless, more or less than before

[Pre-Chorus]
and they're screaming 'bout the boats
(the boats! the boats!)
while the drill's in the wall
and their hand's round your throat

[Chorus]
cash flow, somethings not natural,
board the windows, sweep the glass
this pricks got no fucking mask,
bank roll with punches, bells rung and now you're on crutches

[Verse 2]
Water the wine, bleed the freak's swine
no gun needed, balacava's skeeted
rent seeking? JUST ABOUT EATING!
sorry, did I interrupt your meeting?

[Chorus]
cash flow, somethings not natural,
board the windows, sweep the glass
this pricks got no fucking mask,
bank roll with punches, bells rung and now you're on crutches

[Monologue]
Take a pound off a man and he calls the police. Thin every pound he's got and there's no law for that one.

[Verse 3]
Paris, Lisbon, Brussels, Rome
a whole continent out in the road with no home
they're right to be angry, so look where to aim
it's the bank with the lights on, read the fucking name

[Final Chorus]

cash flow, somethings not natural,
board the windows, sweep the glass
this pricks got no fucking mask,
bank roll with punches, bells rung and now you're on crutches
```

### Round A (2026-10-21): cop-show funk + Jack's draft 3 lyrics

Style and Exclude Styles from "Possible styles" above; lyrics are Jack's own edit of draft 3.
Settings: v6, Variety Normal, Max Mode off, Personalize off, Vocal Gender male, no Voice, style
influence 75, Duration 170 s, workspace `bank-robbery`. 20 credits (10,800 → 10,780). Unheard.

- br-jack-copfunk-A-v6-w30 — https://suno.com/song/358323e1-25c1-4925-8a5e-899eda8373a8
- br-jack-copfunk-A-v6-w30 — https://suno.com/song/e1905c0c-b4dc-4312-ad48-e70e5d64b93a
- br-jack-copfunk-A-v6-w60 — https://suno.com/song/0dc34641-6802-4df7-925b-be86e1b82bcc
- br-jack-copfunk-A-v6-w60 — https://suno.com/song/09b0cacb-0ce7-498a-9963-540e2afcf29a

### Round Y (2026-10-21): Roger Daltrey by name, and the prompt audited

Jack on Round W: the same voice over and over; did the prompt name Roger Daltrey? It did not —
and nor did Round S: Round S's boxes carried translations, not names (the names are only in this
file). So **Y names him literally**, as Jack asked, and **Z** is the translation with every fault
below fixed. Both run on the same fixes.

The audit — what was stopping the voice:
- 🔴 **Variety was Normal in every round since A.** Suno's own v6 FAQ says any Variety above Off
  works by *rewriting your Style box* (`docs/suno-gpt/files/suno-v6.md`, Variety row); the house
  ruling is Off. So every voice description was being rewritten before generation. **Now Off.**
- 🔴 **Exclude banned `punk, new wave`** — the neighbourhood the Who's voice lives in. Round S, the
  round that worked, had them unbanned; Round W put them back. **Removed again.**
- 🟡 **Round S's lyrics had a voice in every section label; Round W's had none.** Back in, one fixed
  label repeated: `raspy English rock tenor`. Jack's words unchanged.
- 🟡 **W put the music first**, which is the funk soundtrack's own male singer. Y and Z put the
  voice first (Round S's order).
- 🟡 Suno reportedly blocks or swaps real artist names on v6 (dev.ua; a Reddit thread) — Y tests it.

#### Y · daltrey-named

```
Roger Daltrey vocals: a 1970s London mod rock frontman, a powerful raspy English tenor with working-class West London vowels, a swaggering blues growl and stuttering snarl on the verses, an ear-splitting primal scream on the chorus. Gritty 1970s cop-show funk soundtrack, 104 BPM: stabbing brass section, wah-wah guitar, a fat rumbling bassline, live breakbeat drums with bongos and congas, a breathy low flute stalking the verses, tense string swells on the chorus. Menacing, played completely straight.
```

#### Z · daltrey-translated

```
A 1970s London mod rock frontman, a powerful raspy English tenor with working-class West London vowels, a swaggering blues growl and stuttering snarl on the verses, an ear-splitting primal scream on the chorus. Gritty 1970s cop-show funk soundtrack, 104 BPM: stabbing brass section, wah-wah guitar, a fat rumbling bassline, live breakbeat drums with bongos and congas, a breathy low flute stalking the verses, tense string swells on the chorus. Menacing, played completely straight.
```

Exclude Styles (both):

```
comedy, novelty, parody, kazoo, cartoon, rap, hip hop, trap, double-time, fast rap, cheerful, drum and bass, EDM, autotune, choir, gospel, country, power ballad, smooth R&B, disco, female vocals
```

Settings: as the liked take except **Variety Off**.

4 Creates, 40 credits (10,320 → 10,280). Suno accepted the named prompt without an error. Unheard.

- br-jack-copfunk-Y-daltrey-named-v6-w30 — 2:50 — https://suno.com/song/4c95489b-1675-403f-845b-6aea1938a4b7
- br-jack-copfunk-Y-daltrey-named-v6-w30 — 2:50 — https://suno.com/song/b810ba97-acf0-47a5-865e-c14e2ea74c22
- br-jack-copfunk-Y-daltrey-named-v6-w60 — 2:50 — https://suno.com/song/af703c90-875d-4a60-bfcd-f3086a902266
- br-jack-copfunk-Y-daltrey-named-v6-w60 — — — https://suno.com/song/5ee254d9-5717-4551-ab16-b666c7441a53
- br-jack-copfunk-Z-daltrey-translated-v6-w30 — — — https://suno.com/song/306f913c-8d32-4bd3-8655-f3713b4774d5
- br-jack-copfunk-Z-daltrey-translated-v6-w30 — — — https://suno.com/song/80c3c9cd-1b0e-471f-ac20-75f343596e78
- br-jack-copfunk-Z-daltrey-translated-v6-w60 — — — https://suno.com/song/5f125536-6563-4ae0-b603-60ce81ff1b5f
- br-jack-copfunk-Z-daltrey-translated-v6-w60 — — — https://suno.com/song/cbdd7ab5-adb9-42de-893a-78a73eaf9708

### Round W (2026-10-21): the liked music + a Roger Daltrey-like voice

Jack on Round S: referencing singers changed the voice (saved to `docs/suno-gpt/suno-voices.md`
§2c and the `suno-prompt` skill), but the style of the liked take (ed6dd946) was lost. Now that
music with Roger Daltrey's voice, or like it. Reference in this file only; the box carries a
translation (sources: Wikipedia, TV Insider, Ultimate Classic Rock — blues growl to scream, the
"My Generation" stutter, working-class West London).

Two placements, to settle §2c's open question: **W** = the liked take's music sentence first,
singer after (the liked take's own order); **X** = singer first, music after (Round S's order).
Lyrics, Exclude Styles and settings as the liked take (Round B), minus `American accent, American`.

#### W · daltrey-music-first

```
Gritty 1970s cop-show funk soundtrack, 104 BPM: stabbing brass section, wah-wah guitar, a fat rumbling bassline, live breakbeat drums with bongos and congas, a breathy low flute stalking the verses, tense string swells on the chorus. Male lead: a 1970s London mod rock frontman, a powerful raspy English tenor with working-class West London vowels, a swaggering blues growl and stuttering snarl on the verses, an ear-splitting primal scream on the chorus. Menacing, played completely straight.
```

#### X · daltrey-voice-first

```
A 1970s London mod rock frontman, a powerful raspy English tenor with working-class West London vowels, a swaggering blues growl and stuttering snarl on the verses, an ear-splitting primal scream on the chorus. Gritty 1970s cop-show funk soundtrack, 104 BPM: stabbing brass section, wah-wah guitar, a fat rumbling bassline, live breakbeat drums with bongos and congas, a breathy low flute stalking the verses, tense string swells on the chorus. Menacing, played completely straight.
```

Exclude Styles (both):

```
comedy, novelty, parody, kazoo, cartoon, rap, hip hop, trap, double-time, fast rap, punk, new wave, cheerful, drum and bass, EDM, autotune, choir, gospel, country, power ballad, smooth R&B, disco
```

4 Creates, 40 credits (10,360 → 10,320). Unheard. 8 of 8 takes listed.

- br-jack-copfunk-W-daltrey-music-first-v6-w30 — 2:48 — https://suno.com/song/ddc03756-486b-4141-ad8e-747da03c0b91
- br-jack-copfunk-W-daltrey-music-first-v6-w30 — 2:49 — https://suno.com/song/8a1c5a92-cd20-472e-82fc-51893d1554dc
- br-jack-copfunk-W-daltrey-music-first-v6-w60 — 2:49 — https://suno.com/song/3815dc3e-2c65-4cd6-8bc5-2d160b4f77c5
- br-jack-copfunk-W-daltrey-music-first-v6-w60 — 2:50 — https://suno.com/song/340725ee-c225-4663-a52a-69fefd546f1f
- br-jack-copfunk-X-daltrey-voice-first-v6-w30 — — — https://suno.com/song/11800fbf-8c39-4d05-a2c5-3502c1d483b3
- br-jack-copfunk-X-daltrey-voice-first-v6-w30 — — — https://suno.com/song/5446e48b-282d-4fca-912d-897726ed7423
- br-jack-copfunk-X-daltrey-voice-first-v6-w60 — — — https://suno.com/song/0d6e0987-3070-431f-8959-635b5eb82925
- br-jack-copfunk-X-daltrey-voice-first-v6-w60 — — — https://suno.com/song/c4869e0a-c996-4a64-a10a-4fcfc4f15e98

### Round S (2026-10-21): English women from English singer references

Jack on Round O: all of them sound like the Karen song's voice, and not English; use English
singers who fit the genre as references.

Why it sounded like Karen: Karen's song (`docs/stories/karen/songs/all-day-to-complain.md`) is the
same music family (spy/heist funk: wah guitar, muted trumpet, baritone sax, Rhodes) with a female
lead, so a woman over this music lands on the same singer. Round O also asked for half-spoken
delivery, which is Karen's.

The references go in this file only, never in a Suno box: Suno rejects or rewrites artist names
(`docs/suno-gpt/files/suno-tag-mechanics.md`), so each one is translated into the English scene she
comes from (placed first, where it is strongest) plus her voice. Music sentence unchanged from the
liked take. Lyrics as Round O. Exclude Styles adds the Karen-pool words.

Exclude Styles (all four):

```
comedy, novelty, parody, kazoo, cartoon, rap, hip hop, trap, double-time, fast rap, cheerful, drum and bass, EDM, autotune, choir, gospel, country, power ballad, smooth R&B, disco, male vocals, male voice, smooth jazz, jazz singer, scat, R&B diva, melodic rap, spoken word
```

#### S · retro-soul (reference: Amy Winehouse)

```
London retro soul, a raw husky contralto woman with a heavy North London accent, swaggering behind-the-beat phrasing, wounded and tough. Gritty 1970s cop-show funk soundtrack, 104 BPM: stabbing brass section, wah-wah guitar, a fat rumbling bassline, live breakbeat drums with bongos and congas, a breathy low flute stalking the verses, tense string swells on the chorus. Menacing, played completely straight.
```

#### T · sixties-soul (reference: Dusty Springfield)

```
1960s British blue-eyed soul, a breathy smoky English mezzo, intimate verses that swell into a big aching chorus. Gritty 1970s cop-show funk soundtrack, 104 BPM: stabbing brass section, wah-wah guitar, a fat rumbling bassline, live breakbeat drums with bongos and congas, a breathy low flute stalking the verses, tense string swells on the chorus. Menacing, played completely straight.
```

#### U · mockney-pop (reference: Lily Allen)

```
British indie pop with a cockney London girl, sweet light voice, sarcastic sing-song verses, broad London vowels. Gritty 1970s cop-show funk soundtrack, 104 BPM: stabbing brass section, wah-wah guitar, a fat rumbling bassline, live breakbeat drums with bongos and congas, a breathy low flute stalking the verses, tense string swells on the chorus. Menacing, played completely straight.
```

#### V · 77-punk (reference: Poly Styrene / Siouxsie Sioux)

```
1977 London punk woman, a piercing yelping English voice, shrieked chorus, sneering and wild. Gritty 1970s cop-show funk soundtrack, 104 BPM: stabbing brass section, wah-wah guitar, a fat rumbling bassline, live breakbeat drums with bongos and congas, a breathy low flute stalking the verses, tense string swells on the chorus. Menacing, played completely straight.
```

8 Creates, 80 credits (10,440 → 10,360). Unheard. 15 of 16 takes listed.

- br-jack-copfunk-S-retro-soul-v6-w30 — 2:50 — https://suno.com/song/ccd3a2c3-22e4-4093-94fb-8ec9b898c5e3
- br-jack-copfunk-S-retro-soul-v6-w60 — 2:49 — https://suno.com/song/80da6f82-1d69-4a4b-b2f1-ce94258029e5
- br-jack-copfunk-S-retro-soul-v6-w60 — 2:50 — https://suno.com/song/43cb54dc-2b15-4ef5-9352-9ffffa9781c1
- br-jack-copfunk-T-sixties-soul-v6-w30 — 2:49 — https://suno.com/song/2bbc25db-77ba-4af0-b143-7cf84b6a0460
- br-jack-copfunk-T-sixties-soul-v6-w30 — 2:49 — https://suno.com/song/763a21c0-c5cd-4893-996d-0289f4547100
- br-jack-copfunk-T-sixties-soul-v6-w60 — 2:49 — https://suno.com/song/ae69ad5f-3233-4e37-896c-1a656e6ed8ab
- br-jack-copfunk-T-sixties-soul-v6-w60 — 2:50 — https://suno.com/song/90c49952-17ce-4dfd-85a0-d290739ad2f9
- br-jack-copfunk-U-mockney-pop-v6-w30 — 2:49 — https://suno.com/song/130608c7-9ca1-4cde-a4d9-5c8dd90fa451
- br-jack-copfunk-U-mockney-pop-v6-w30 — 2:50 — https://suno.com/song/37a17661-c6da-4133-91a8-7659bfc15c00
- br-jack-copfunk-U-mockney-pop-v6-w60 — 2:48 — https://suno.com/song/76dc2787-ec7e-429e-b1cc-6b998be1bcdf
- br-jack-copfunk-U-mockney-pop-v6-w60 — 2:50 — https://suno.com/song/274fecf1-152a-41cb-a184-86cff246da49
- br-jack-copfunk-V-77-punk-v6-w30 — 2:49 — https://suno.com/song/54da795b-20fe-4f0b-8719-958de22ac830
- br-jack-copfunk-V-77-punk-v6-w30 — 2:50 — https://suno.com/song/bc780503-81dd-4906-8a2c-f89740839422
- br-jack-copfunk-V-77-punk-v6-w60 — — — https://suno.com/song/ac041775-251a-406b-aa4d-8a0697de3bf0
- br-jack-copfunk-V-77-punk-v6-w60 — — — https://suno.com/song/b15f19b4-d132-407d-9456-bf037e25d74a

### Round O (2026-10-21): English women, prompts audited

Jack on Round K: the style is there but the voice is not; try English women, and check whether
something in the prompts is causing it.

The audit (rules from `docs/suno-gpt/suno-voices.md` §2a, §4a, §4c):
- **Exclude was banning the English pools.** `punk, new wave` are two of the strongest English
  female-voice families; banning them pushes the singer back to the default, which is American.
  Removed.
- **`American accent, American` named America in the Exclude box.** Bans don't control nationality
  and the words still count as American. Removed.
- **The music sentence is American in genre position** (`1970s cop-show funk soundtrack`, bongos,
  congas). Kept, because Jack likes the style; the voice now has to beat it, so each box opens
  with a place of origin + a performer type, the strongest levers the repo and the web name.
- **Every lyric section had no voice in it**, so each section fell back to the genre's default
  singer. Each section label now carries one fixed cue, `English female vocal`, repeated
  identically (labels only; Jack's words unchanged).
- **Nothing banned male vocals.** Added `male vocals, male voice`; Vocal Gender is female.

Music sentence unchanged from the liked take (ed6dd946). Settings as Round K.

Exclude Styles (all four):

```
comedy, novelty, parody, kazoo, cartoon, rap, hip hop, trap, double-time, fast rap, cheerful, drum and bass, EDM, autotune, choir, gospel, country, power ballad, smooth R&B, disco, male vocals, male voice
```

#### O · london-soul

```
Female vocalist from London, England, singing with natural British pronunciation: a 1960s British soul singer, big raw smoky alto. Gritty 1970s cop-show funk soundtrack, 104 BPM: stabbing brass section, wah-wah guitar, a fat rumbling bassline, live breakbeat drums with bongos and congas, a breathy low flute stalking the verses, tense string swells on the chorus. Menacing, played completely straight.
```

#### P · manc-punk

```
Female vocalist from Manchester, England, singing with natural Northern English pronunciation: a sneering English punk singer, sharp nasal shouted voice. Gritty 1970s cop-show funk soundtrack, 104 BPM: stabbing brass section, wah-wah guitar, a fat rumbling bassline, live breakbeat drums with bongos and congas, a breathy low flute stalking the verses, tense string swells on the chorus. Menacing, played completely straight.
```

#### Q · bristol-hush

```
Female vocalist from Bristol, England, singing with natural British pronunciation: a cool trip hop singer, low hushed breathy voice, close to the mic. Gritty 1970s cop-show funk soundtrack, 104 BPM: stabbing brass section, wah-wah guitar, a fat rumbling bassline, live breakbeat drums with bongos and congas, a breathy low flute stalking the verses, tense string swells on the chorus. Menacing, played completely straight.
```

#### R · london-girl

```
Female vocalist from East London, England, singing with natural British pronunciation: a young London girl, bright light voice, cheeky half-spoken chat on the verses. Gritty 1970s cop-show funk soundtrack, 104 BPM: stabbing brass section, wah-wah guitar, a fat rumbling bassline, live breakbeat drums with bongos and congas, a breathy low flute stalking the verses, tense string swells on the chorus. Menacing, played completely straight.
```

8 Creates, 80 credits (10,520 → 10,440). Unheard. 15 of 16 takes listed.

- br-jack-copfunk-O-london-soul-v6-w30 — 2:50 — https://suno.com/song/8d701070-8a11-4828-88dd-fba1f0261569
- br-jack-copfunk-O-london-soul-v6-w60 — 2:49 — https://suno.com/song/0d465888-1d6f-4409-8bd5-d6f34287aa4b
- br-jack-copfunk-O-london-soul-v6-w60 — 2:50 — https://suno.com/song/d5913c2e-cf02-4aed-b243-4032c884e21f
- br-jack-copfunk-P-manc-punk-v6-w30 — 2:49 — https://suno.com/song/3be4654e-f586-4107-98ec-6ddaf957cfe4
- br-jack-copfunk-P-manc-punk-v6-w30 — 2:50 — https://suno.com/song/bd03430b-9c48-4803-b1e3-e7de0aaad6da
- br-jack-copfunk-P-manc-punk-v6-w60 — 2:49 — https://suno.com/song/1b62f49d-c425-406e-88c8-2d4729820412
- br-jack-copfunk-P-manc-punk-v6-w60 — 2:50 — https://suno.com/song/049824f3-03e9-4012-92c4-2cdc512c4e24
- br-jack-copfunk-Q-bristol-hush-v6-w30 — 2:50 — https://suno.com/song/5b929b11-4b19-4e07-9046-3d224d075276
- br-jack-copfunk-Q-bristol-hush-v6-w30 — 2:50 — https://suno.com/song/c07e7657-48d9-42bc-88f2-e3bc642d23f4
- br-jack-copfunk-Q-bristol-hush-v6-w60 — — — https://suno.com/song/2bff1fa0-b5c4-429e-a7d1-02024f937c67
- br-jack-copfunk-Q-bristol-hush-v6-w60 — — — https://suno.com/song/61eb1dd2-92ac-40de-a6c6-85b785c330b0
- br-jack-copfunk-R-london-girl-v6-w30 — — — https://suno.com/song/9dc2951e-7692-47f7-9cbc-8daf5a355a58
- br-jack-copfunk-R-london-girl-v6-w30 — — — https://suno.com/song/dbc0dfb3-cf60-41a9-a2a6-74b979c52d53
- br-jack-copfunk-R-london-girl-v6-w60 — — — https://suno.com/song/5795334c-1c19-439f-beb5-ac011edc7d13
- br-jack-copfunk-R-london-girl-v6-w60 — — — https://suno.com/song/a78a1f25-e3c8-40b6-ac59-23ea712d1943

### Round K (2026-10-21): the liked take's music, four different English voices

Jack on Round J: English now, but the voices don't vary enough. Keep the music and genre of the
liked take (ed6dd946), drop its voice. Each box = one English voice line first (pitch, age, texture,
gender: what Suno does render), then the liked take's music sentence unchanged, then a short
delivery line. Lyrics, Exclude Styles and settings as Round J; Vocal Gender matches each voice.

#### K · deep-old (Vocal Gender male)

```
English male vocals, a deep low gravelly old man's voice with a thick English accent. Gritty 1970s cop-show funk soundtrack, 104 BPM: stabbing brass section, wah-wah guitar, a fat rumbling bassline, live breakbeat drums with bongos and congas, a breathy low flute stalking the verses, tense string swells on the chorus. Growled half-spoken verses, a hoarse roared chorus. Menacing, played completely straight.
```

#### L · high-young (Vocal Gender male)

```
English male vocals, a high thin young man's voice with a thick English accent. Gritty 1970s cop-show funk soundtrack, 104 BPM: stabbing brass section, wah-wah guitar, a fat rumbling bassline, live breakbeat drums with bongos and congas, a breathy low flute stalking the verses, tense string swells on the chorus. Jittery yelped verses, a screamed chorus. Menacing, played completely straight.
```

#### M · husky-woman (Vocal Gender female)

```
English female vocals, a husky smoky woman's voice with a thick English accent. Gritty 1970s cop-show funk soundtrack, 104 BPM: stabbing brass section, wah-wah guitar, a fat rumbling bassline, live breakbeat drums with bongos and congas, a breathy low flute stalking the verses, tense string swells on the chorus. Cool sultry spoken verses, a snarled chorus. Menacing, played completely straight.
```

#### N · brassy-woman (Vocal Gender female)

```
English female vocals, a sharp loud brassy woman's voice with a thick English accent. Gritty 1970s cop-show funk soundtrack, 104 BPM: stabbing brass section, wah-wah guitar, a fat rumbling bassline, live breakbeat drums with bongos and congas, a breathy low flute stalking the verses, tense string swells on the chorus. Sung verses, a belted shouted chorus with a gang shouting back. Menacing, played completely straight.
```

8 Creates, 80 credits (10,600 → 10,520). Unheard. 15 of 16 takes listed.

- br-jack-copfunk-K-deep-old-v6-w30 — 2:50 — https://suno.com/song/aaa7abe2-ab22-45fe-91c2-5ec5273f77f7
- br-jack-copfunk-K-deep-old-v6-w60 — 2:49 — https://suno.com/song/06c366b1-0119-4b5b-a7a5-7237ccc58c59
- br-jack-copfunk-K-deep-old-v6-w60 — 2:50 — https://suno.com/song/e758d7d6-ec0c-4745-bcbb-a90f3bbd6df9
- br-jack-copfunk-L-high-young-v6-w30 — 2:49 — https://suno.com/song/3c4662eb-5441-4298-bdc5-574da722886f
- br-jack-copfunk-L-high-young-v6-w30 — 2:49 — https://suno.com/song/5dd5db0a-613d-4ef7-bba7-a0bdbb4b49d9
- br-jack-copfunk-L-high-young-v6-w60 — 2:50 — https://suno.com/song/29b29197-340e-4e50-b23a-f05cc5d40349
- br-jack-copfunk-L-high-young-v6-w60 — 2:50 — https://suno.com/song/5f9560af-2471-4008-8be0-6df5f1c9648b
- br-jack-copfunk-M-husky-woman-v6-w30 — 2:50 — https://suno.com/song/304b0bca-44e7-485b-bf96-7d25bd6cb5ee
- br-jack-copfunk-M-husky-woman-v6-w30 — 2:50 — https://suno.com/song/3229b59d-fe79-4907-a838-837f2471dca0
- br-jack-copfunk-M-husky-woman-v6-w60 — 2:49 — https://suno.com/song/9971310d-458b-4002-baad-59912520f0fe
- br-jack-copfunk-M-husky-woman-v6-w60 — 2:50 — https://suno.com/song/214a1d5d-e919-40fa-a6be-92b82b0865a7
- br-jack-copfunk-N-brassy-woman-v6-w30 — — — https://suno.com/song/4abee9fd-71cc-4a4a-9a5b-c34310ab582e
- br-jack-copfunk-N-brassy-woman-v6-w30 — — — https://suno.com/song/4b1199be-31a2-4937-b730-1113d3daf4b9
- br-jack-copfunk-N-brassy-woman-v6-w60 — — — https://suno.com/song/ca40e3ec-0900-423b-9940-9d33fafea068
- br-jack-copfunk-N-brassy-woman-v6-w60 — — — https://suno.com/song/ed884e7d-dd70-4a23-adfb-d3753c862ca9

### Round J (2026-10-21): back to the South London take, just an English voice

Jack liked https://suno.com/song/ed6dd946-0ebf-422d-a68b-3e205462adc1 (Round B, South London w60) and
found Round C weird and nothing like it. Round J is Round B's South London atom unchanged, with one
sentence added at the front: `English male vocals with a thick English accent.` Lyrics, Exclude
Styles and settings exactly as Round B.

Style:

```
English male vocals with a thick English accent. Gritty 1970s cop-show funk soundtrack, 104 BPM: stabbing brass section, wah-wah guitar, a fat rumbling bassline, live breakbeat drums with bongos and congas, a breathy low flute stalking the verses, tense string swells on the chorus. Male lead, a rough South London geezer with a thick English accent, growling deadpan spoken narration on the verses that breaks into barked shouts on the chorus, a gang of London voices shouting back. Menacing, played completely straight.
```

2 Creates, 20 credits (10,620 → 10,600). Unheard.

- br-jack-copfunk-J-english-v6-w30 — https://suno.com/song/23b882c1-32da-4262-a9b5-b7823cf6cd73
- br-jack-copfunk-J-english-v6-w30 — https://suno.com/song/f94a72ef-47d7-4606-ae94-27b2dbb9df99
- br-jack-copfunk-J-english-v6-w60 — https://suno.com/song/1e695e5d-39eb-4d19-ac0f-c446142ace66
- br-jack-copfunk-J-english-v6-w60 — https://suno.com/song/408a170d-6ab2-4549-8767-3430a8d3bd9b

### Round C (2026-10-21): four voices by performer type, voice first

Built on the Round B diagnosis below: each voice is a performance tradition with its own pitch,
texture, room and delivery, placed first in the Style box. Music, lyrics (Jack's draft 3) and settings
as Round A; workspace `bank-robbery-Jack`. No accent bans. Each Exclude box is its own.

#### F · postpunk

Style:

```
British post-punk ranter, a weathered working-class man in his fifties, low gravelly smoke-worn voice, close and dry in your ear, over gritty 1970s cop-show funk, 104 BPM: stabbing brass, wah-wah guitar, a rumbling bassline, breakbeat drums with bongos, a low flute stalking the verses. He mutters the verses like a threat and barks the chorus hoarse. Menacing, played completely straight.
```

Exclude styles:

```
comedy, novelty, parody, kazoo, cartoon, trap, double-time, fast rap, punk, new wave, cheerful, drum and bass, EDM, autotune, choir, gospel, country, power ballad, smooth R&B, disco, rap, hip hop, grime
```

#### G · britpop

Style:

```
Britpop snarl, a cocky young lad, higher nasal sneering voice with slap-back echo, over gritty 1970s cop-show funk, 104 BPM: stabbing brass, wah-wah guitar, a rumbling bassline, breakbeat drums with bongos, a low flute stalking the verses. Sneered verses that swell into a terrace-chant chorus, a crowd of lads chanting back. Menacing, played completely straight.
```

Exclude styles:

```
comedy, novelty, parody, kazoo, cartoon, trap, double-time, fast rap, punk, new wave, cheerful, drum and bass, EDM, autotune, choir, gospel, country, power ballad, smooth R&B, disco, rap, hip hop, grime
```

#### H · newsreader

Style:

```
BBC newsreader turned villain, a polished upper-class after-dinner speaker, smooth crisp clean baritone in a large wood-panelled hall, over gritty 1970s cop-show funk, 104 BPM: stabbing brass, wah-wah guitar, a rumbling bassline, breakbeat drums with bongos, a low flute stalking the verses. Calm and polite on the verses, coldly furious on the chorus, never raising his voice. Menacing, played completely straight.
```

Exclude styles:

```
comedy, novelty, parody, kazoo, cartoon, trap, double-time, fast rap, punk, new wave, cheerful, drum and bass, EDM, autotune, choir, gospel, country, power ballad, smooth R&B, disco, rap, hip hop, grime, shouting, screaming
```

#### I · grime

Style:

```
UK grime MC, a young London voice, punchy clipped mid-range, laid-back half-time flow sitting behind the beat, over gritty 1970s cop-show funk, 104 BPM: stabbing brass, wah-wah guitar, a rumbling bassline, breakbeat drums with bongos, a low flute stalking the verses. Verses spat slow and heavy, the chorus traded call-and-response with his crew. Menacing, played completely straight.
```

Exclude styles:

```
comedy, novelty, parody, kazoo, cartoon, trap, double-time, fast rap, punk, new wave, cheerful, drum and bass, EDM, autotune, choir, gospel, country, power ballad, smooth R&B, disco, triplet flow, drill, American hip hop
```

8 Creates, 80 credits (10,700 → 10,620). Unheard. 15 of 16 takes listed.

- br-jack-copfunk-F-postpunk-v6-w30 — 2:49 — https://suno.com/song/98cd01aa-e7e2-4f98-ab88-ef30e0bad7fd
- br-jack-copfunk-F-postpunk-v6-w60 — 2:49 — https://suno.com/song/37811970-1704-4359-bc4e-5166ff619dc0
- br-jack-copfunk-F-postpunk-v6-w60 — 2:50 — https://suno.com/song/9ba03240-482e-4122-b4ec-a5da0b2f09b2
- br-jack-copfunk-G-britpop-v6-w30 — 2:49 — https://suno.com/song/17fdd031-7b23-43d1-9435-fecbf08740f6
- br-jack-copfunk-G-britpop-v6-w30 — 2:49 — https://suno.com/song/e6bd53b4-652a-41a9-a747-d72b73df7691
- br-jack-copfunk-G-britpop-v6-w60 — 2:49 — https://suno.com/song/e4c1ce91-722d-4995-b7de-afc2bfecf611
- br-jack-copfunk-G-britpop-v6-w60 — 2:50 — https://suno.com/song/c5b2ba8e-efc4-41de-854b-7eb298038dc7
- br-jack-copfunk-H-newsreader-v6-w30 — 2:49 — https://suno.com/song/5e751105-471e-46a8-974b-8969c40c40e6
- br-jack-copfunk-H-newsreader-v6-w30 — 2:50 — https://suno.com/song/a04d5355-4ac9-4966-bb45-05d1ad3106a0
- br-jack-copfunk-H-newsreader-v6-w60 — 2:48 — https://suno.com/song/ea39c01d-7fdc-4e00-9985-233288d7790e
- br-jack-copfunk-H-newsreader-v6-w60 — 2:50 — https://suno.com/song/a6ce5deb-5787-42b7-bc60-1a8a29bd823f
- br-jack-copfunk-I-grime-v6-w30 — — — https://suno.com/song/25fba2a6-0558-4755-8bf3-362f99deb5b1
- br-jack-copfunk-I-grime-v6-w30 — — — https://suno.com/song/6625318c-bbfb-4f17-9505-4fb1fba0cf2a
- br-jack-copfunk-I-grime-v6-w60 — — — https://suno.com/song/dfcd1624-5574-4901-a842-6d0004311d42
- br-jack-copfunk-I-grime-v6-w60 — — — https://suno.com/song/e9cc3699-3cee-44fe-a4f7-ca7f82a397b8

### Round B (2026-10-21): four English voices, same song

Jack: redo the cop-funk songs with English voices that vary from song to song, in the
`bank-robbery-Jack` workspace. Only the voice sentence changes; the music, the lyrics (Jack's
draft 3) and the settings are Round A's. Exclude Styles is Round A's plus `American accent, American`.

#### B · south-london

Style:

```
Gritty 1970s cop-show funk soundtrack, 104 BPM: stabbing brass section, wah-wah guitar, a fat rumbling bassline, live breakbeat drums with bongos and congas, a breathy low flute stalking the verses, tense string swells on the chorus. Male lead, a rough South London geezer with a thick English accent, growling deadpan spoken narration on the verses that breaks into barked shouts on the chorus, a gang of London voices shouting back. Menacing, played completely straight.
```

#### C · manc

Style:

```
Gritty 1970s cop-show funk soundtrack, 104 BPM: stabbing brass section, wah-wah guitar, a fat rumbling bassline, live breakbeat drums with bongos and congas, a breathy low flute stalking the verses, tense string swells on the chorus. Male lead, a sneering Mancunian with a flat nasal Northern English accent, bored deadpan spoken narration on the verses that breaks into snarled shouts on the chorus, a gang of Northern voices shouting back. Menacing, played completely straight.
```

#### D · scouse

Style:

```
Gritty 1970s cop-show funk soundtrack, 104 BPM: stabbing brass section, wah-wah guitar, a fat rumbling bassline, live breakbeat drums with bongos and congas, a breathy low flute stalking the verses, tense string swells on the chorus. Male lead, a raspy Liverpool docker with a thick Scouse English accent, hoarse deadpan spoken narration on the verses that breaks into roared shouts on the chorus, a gang of Scouse voices shouting back. Menacing, played completely straight.
```

#### E · posh

Style:

```
Gritty 1970s cop-show funk soundtrack, 104 BPM: stabbing brass section, wah-wah guitar, a fat rumbling bassline, live breakbeat drums with bongos and congas, a breathy low flute stalking the verses, tense string swells on the chorus. Male lead, a cold upper-class English villain with a clipped plummy accent, quiet menacing spoken narration on the verses that snaps into contemptuous shouts on the chorus, a gang of rough London voices shouting back. Menacing, played completely straight.
```

Exclude Styles (all four):

```
comedy, novelty, parody, kazoo, cartoon, rap, hip hop, trap, double-time, fast rap, punk, new wave, cheerful, drum and bass, EDM, autotune, choir, gospel, country, power ballad, smooth R&B, disco, American accent, American
```

8 Creates, 80 credits (10,780 → 10,700), workspace `bank-robbery-Jack`. Unheard. 15 of 16 takes
listed; the second South London w30 take did not show in the list.

- br-jack-copfunk-B-south-london-v6-w30 — 2:50 — https://suno.com/song/35778104-b667-4b16-8cd4-f2226c168cb0
- br-jack-copfunk-B-south-london-v6-w60 — 2:49 — https://suno.com/song/93fd522d-684e-4de4-a3f0-1c594f08d498
- br-jack-copfunk-B-south-london-v6-w60 — 2:50 — https://suno.com/song/ed6dd946-0ebf-422d-a68b-3e205462adc1
- br-jack-copfunk-C-manc-v6-w30 — 2:50 — https://suno.com/song/379426c0-3d0c-471f-ab8e-b83ae9ce1f6b
- br-jack-copfunk-C-manc-v6-w30 — 2:50 — https://suno.com/song/f415e6a6-3695-413b-8e59-43dbc269180c
- br-jack-copfunk-C-manc-v6-w60 — 2:50 — https://suno.com/song/646dcfe2-d115-463b-ad79-0304d11ad2cf
- br-jack-copfunk-C-manc-v6-w60 — 2:50 — https://suno.com/song/83a22492-6cfb-424c-8a4b-385f08cffe17
- br-jack-copfunk-D-scouse-v6-w30 — 2:47 — https://suno.com/song/7777d2b8-79d3-4536-944a-f642d8b012b6
- br-jack-copfunk-D-scouse-v6-w30 — 2:50 — https://suno.com/song/11c6b37c-1b09-4ae6-b7f7-0fb728ec990c
- br-jack-copfunk-D-scouse-v6-w60 — 2:49 — https://suno.com/song/b445526a-43eb-4477-88ea-9e22d6802136
- br-jack-copfunk-D-scouse-v6-w60 — — — https://suno.com/song/94b09870-8d68-4d1a-b298-7c996efe1801
- br-jack-copfunk-E-posh-v6-w30 — — — https://suno.com/song/3d4c6ac4-19e6-4d2a-9ce5-785973213af0
- br-jack-copfunk-E-posh-v6-w30 — — — https://suno.com/song/a4b83511-263f-4648-9f09-9000cddb2688
- br-jack-copfunk-E-posh-v6-w60 — — — https://suno.com/song/a2bb0f70-32ee-4d7d-a736-c0537083e695
- br-jack-copfunk-E-posh-v6-w60 — — — https://suno.com/song/f0d10f8c-c2a9-4188-a988-9d787232a521

Why Round B came back as one voice (diagnosis, 2026-10-21; Jack heard "basically the same
English voice over and over"):

1. **The only thing that changed was the accent word, and Suno does not render regional accents.**
   Tested in this repo: a detailed Scouse spec produced no accent at all (`docs/suno-gpt/suno-voices.md`
   §2). South London / Manc / Scouse were dead words; only "posh" had a chance.
2. **The genre picks the singer.** "1970s cop-show funk soundtrack" chooses one pool of voices, and
   weirdness 30/60 only moves around inside that pool (`suno-voices.md` §2b).
3. **The rest of the voice sentence was identical in all four:** deadpan spoken narration → shouts on
   the chorus → a gang shouting back. Same delivery, same arc, same voice. A meek variation
   (`suno-automation` "BOLD, NOT MEEK").
4. **The voice sentence sat last**, after a long instrument list, so it had the least pull.
5. **`American accent, American` in Exclude does nothing for nationality** (failed three rounds on
   Camping) and can be deleted.

Fix: vary on what Suno does render (pitch, texture, delivery, room), name a performance tradition
for each voice instead of a region, and put the voice first.

## Draft 2 (2026-10-21) — superseded by draft 3

Jack's brief, word for word:

> i want to stray away from economic talk, mostly reference it as a bank robbery, through metaphor
> and with economic hints throughout, making it aggressive, gory, sort of like the vibe of making
> people aware that they should be angry about their money being stolen, in the same vein as the
> bank robbery story, as in all this immagration talk is just a distration from the debasement of
> our currency, making it impossible to live and buy a house, this has been stolen from us, evident
> from the current protests across europe at the moment, people are angry about living standerds
> and absurd politcal corruption and mismanagement, these are all ingredients for the soup that is
> this song. please help, Also, research the internet, look through the repo, and use the skills to
> achieve this goal. Thanks.

Jack's brief: less economics talk, tell it as a bank robbery in metaphor with economic hints;
aggressive and gory; make people angry that their money is being stolen; the immigration row is the
distraction from the debasement that makes living and buying a house impossible; the protests across
Europe and the anger about living standards and corruption go in the pot. Same vibe as draft 1
(1970s heist soundtrack, nervy art-punk new wave, psychedelic swirl).

The drama in one sentence: men in rosettes break into the bank to put money in, so every pound you
hold bleeds out, and they start the street screaming about boats so nobody hears the drill; the
keys to your house end up in their bag.

What it is built from:
- **Reservoir Dogs:** Mister Red and Mister Blue (they don't pick their own colours), the town tied
  to a chair in the back with the radio on, and the ear taken so it can't hear the drill.
- **The film's canon:** the one pallet with a left end and a right end, "Thirteen years!" /
  "Fourteen!" (the row with no content), the bag of house keys, "he's not a thief, he's just
  early", "three hundred thousand men got off that beach", "take a pound off a man…", the cleaner
  who counts, "burglars take things", and "it's got BANK written on it".
- **Jack's verse:** the money tree, "rent seeking? JUST ABOUT EATING!" and "sorry, did I interrupt
  your meeting?" are kept word for word.
- **The news (checked 2026-10-21):** cost-of-living and housing protests across France, Belgium,
  Italy and Portugal on 17–18 October, with housing marches in Spain (Euronews, 19 Oct 2026). The
  song names the road, not a riot, and calls nobody to burn anything.
- **The reader's rules:** immigration is never called fake ("some of that's real, it's the size of
  a coin"); Red and Blue get it equally; the anger is aimed at the bank and the men with the keys,
  never at the crowd or at the reader.

Settings: model **v6**, Variety **Normal**, Personalize **off**, Max Mode **off**, Vocal Gender
**male**, Duration **3:10**, style influence **75**, weirdness **30 and 60** (the pair). Unheard,
nothing generated.

### Style

```
Menacing British art-punk new wave with a 1970s heist-movie soul groove, 120 BPM: a twitchy distorted funk guitar, a bouncing snarling bassline, dry punchy drums with handclaps, and phased psychedelic synths that swirl in on the chorus. Male lead in a tense deadpan talk-sing on the verses that tears into snarled shouted yelps on the chorus, a gang of flat voices shouting back. Played completely straight.
```

### Exclude Styles

```
comedy, novelty, parody, kazoo, cartoon, rap, hip hop, trap, double-time, fast rap, pop punk, cheerful, drum and bass, EDM, autotune, orchestral, choir, gospel, country, power ballad, smooth R&B
```

### Lyrics

```lyrics
[Intro]
They say you can't make money from a tree
let's see
nobody move, nobody's taking a thing
(nobody move)
that's how you know it's a robbery

[Verse 1]
Eleven black ties at the café at dawn
Mister Red, Mister Blue, didn't pick what they've got on
no masks on the faces, just a rosette
and the getaway car's on the never-never

the drill's in the boot and the key's in his coat
it's his bank, he's had the key the whole time
the drill's for you, mate, the drill's for show
and the van's backed up to the side door, slow

[Pre-Chorus]
"Thirteen years!" "Fourteen!" scream it at the screen
left end, right end, one pallet, one door
(lift your feet)
and the drill goes in while you're scrapping on the floor

[Chorus]
It's a robbery! Robbery!
they're not taking it out, they're shoving it in
every pound in your pocket's bleeding through the skin
(count it again)
It's a robbery! Robbery!
blood on the carpet and the keys in the bag
(that's your house, that's your house)

[Verse 2]
They tied the town to a chair in the back
radio on, something sweet from the seventies
took off its ear so it can't hear the drill
now it only hears the boats, and it's bleeding still

three hundred thousand men got off that beach
and their grandkids can't get a one-bed
the rent letter's doubled on the draining board
he spends the new money first, before the prices move
he's not a thief, he's just early
and you're just late

rent seeking? JUST ABOUT EATING!
sorry, did I interrupt your meeting?

[Chorus]
It's a robbery! Robbery!
they're not taking it out, they're shoving it in
every pound in your pocket's bleeding through the skin
(count it again)
It's a robbery! Robbery!
blood on the carpet and the keys in the bag
(that's your house, that's your house)

[Monologue]
Take a pound off a man and he calls the police. Thin every pound he's got and there's no law for that one. Our road's changed. Some of that's real. It's the size of a coin. The vault's the size of the town.

[Verse 3]
Paris to Porto, they're out in the road
Milan to Madrid, with the rent that they owe
same suits, same pallet, same drill, same queue
and this time they're screaming at the bank

the cleaner don't shout, she just counts the drawers
mops your blood off the marble, it's yours, it's all yours
every balance the same, not a penny gone
burglars take things
this lot took your home

[Final Chorus]
It's a robbery! Robbery!
they're not taking it out, they're shoving it in
every pound in your pocket's bleeding through the skin
(count it again)
It's a robbery! Robbery!
blood on the carpet and the keys in the bag
(that's your house, that's your house)

[Outro]
I've seen how this ends, I came back to say
look at the bank
it's got BANK written on it
(count it again)
```

## Draft 1 (2026-10-21) — superseded by draft 2

Jack's brief: expand and improve the ten-line verse he pasted, nothing else carried in. The vibe is
a 1970s heist soundtrack, nervy art-punk new wave and a psychedelic swirl. No artist names go in any
box. Unheard, nothing generated.

Settings: model **v6**, Variety **Normal**, Personalize **off**, Max Mode **off**, Vocal Gender
**male**, Duration **2:50**, style influence **75**, weirdness **30 and 60** (the pair).

### Style

```
Nervy British art-punk new wave with a 1970s heist-movie soul groove, 118 BPM: a twitchy choppy funk guitar, a bouncing melodic bassline, dry tight drums with handclaps, and phased psychedelic synths that swirl in on the chorus. Male lead in a tense deadpan talk-sing that cracks into yelps on the chorus, flat group shouts answering. Played completely straight.
```

### Exclude Styles

```
comedy, novelty, parody, kazoo, cartoon, rap, hip hop, trap, double-time, fast rap, drum and bass, EDM, autotune, orchestral, choir, gospel, country, power ballad, smooth R&B
```

### Lyrics

```lyrics
[Verse 1]
They say you can't make money from a tree
let's see, each day, not free, ay
you work and get paid, you're earning that dough
but where does it go? Nobody knows!

living standards bleeding, landlords feeding
quantitative easing, grandma FREEZING!
they own the means of production, you get the reduction
stimulus checks are next, go fetch

rent seeking? JUST ABOUT EATING!
sorry, did I interrupt your meeting?

[Chorus]
It's a robbery, robbery
nobody's taking, they're carrying it in
eight hundred and ninety-five billion
print it, print it, print it again
(count it, count it, count it again)

[Verse 2]
They printed it fresh and they bought what they own
the shares and the houses, the bonds and the loans
the top tenth got three hundred and fifty grand
the bottom tenth got three, and a lecture on the plan

now the bread costs more and so does the rent
they call it inflation, like nobody meant it
your wages stood still while the asset prices flew
funny how the tree only fruits for a few

[Chorus]
It's a robbery, robbery
nobody's taking, they're carrying it in
eight hundred and ninety-five billion
print it, print it, print it again
(count it, count it, count it again)

[Bridge]
Left grabs one end, Right grabs the other
shouting 'bout the boats and blaming each other
(it's the boats!) (it's the bosses!)
same bag, same door, same vault getting fuller
and you're the only one getting poorer

[Verse 3]
Morning comes, nothing missing, every balance the same
the coppers shrug, no break-in, nobody to blame
but burglars take things, and this lot left more
the cleaner counts the drawers, then she counts them once more

I've seen how this ends, I've been there, I'm back
the pound in your pocket's been thinned to a crack
they'll tell you it's the weather, the war or the queue
she's the only one in the building who counts

[Outro]
It's a robbery, robbery
(count it, count it, count it again)
nobody's taking, they're carrying it in
(count it again)
```

## Earlier lyrics

The lyrics below are copied word for word from [`score.md`](./score.md), which still holds the
originals.

## Lyrics (from `score.md` § Lyrics)

```lyrics
They say, ya can't make money from a tree
let's see, each day, not free, ay
work and get paid though, earning that dough
but where does it go? nobody knows!

standards bleeding, land-lords needing
quantitative easing, grandma FREEZING!
means of production, means a reduction
stimulus checks are next, get wrecked

rent seeking? JUST ABOUT EATING!
sorry, did I interrupt your meeting?
```

## Lyrics (from `score.md` § br-sting, the 80s montage)

```lyrics
A modern guide to robbing a Bank.
Step 1. Get yourself a wank tank.
Now you look the part, real classy, good start.
Step 2. This one is especially for you.
"You gotta split the red side away from the blue."
Step 3. And this one ain't free.
Slowly start to debase the currency.
Step 4. Start a war.
This one drives the price up from the floor.
```
