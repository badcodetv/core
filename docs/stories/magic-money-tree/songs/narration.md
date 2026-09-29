---
title: Magic Money Tree narration — the live sheet
status: 🟡 FIRST DRAFT, 2026-09-29. Words not locked; nothing generated. Kai edits the words, then round 1 is the style test in section 4.
kind: scored spoken narration for the documentary (voice and score in one Suno take), not a song
model: v6
workspace: mmt-narration (create it; one workspace per arc)
source_words: ../storyboard.md, working narration as rebuilt 2026-09-28
sibling: ./magic-money-tree.md (the jump-up song; a separate piece, not the film's score)
---

# Magic Money Tree narration — the live sheet

**What this is.** The film's narration as Suno lyrics, split into parts Suno can read in one take,
with the boxes to paste. It follows the method GitPush Origin Master proved
([`../../gitpush-origin-master/songs/narration.md`](../../gitpush-origin-master/songs/narration.md)):
one calm British voice, a quiet score underneath, generated together, one part per take, cut
together in Premiere.

**What is different here, by Kai's brief (29 September).** GPOM is dramatic. This film is a
documentary: **the music is minimal and matters**, the voice is an **English narrator**, and the
score sits under the words the way a good documentary's does, never announcing itself.

**Where the words come from.** Every line below is the storyboard's working narration, verbatim,
except for three kinds of change made only so Suno says it right: **numbers and dates written out as
spoken**, **"..." where a documentary narrator would breathe**, and **one sentence per line**.
The storyboard stays the source of truth for meaning. **Kai edits the words here next**; when a line
changes, change it in the storyboard too.

**Nothing has been generated.** Section 4 is the first round.

---

## 1. Length, and why it is ten parts

- **The draft is about 1,570 words.** At a documentary pace that is roughly **13 to 15 minutes** of
  voice. Kai wants the film shorter; section 6 lists what could go.
- **Suno's ceiling is 8 minutes a take** (v6, all models), but GPOM's picked takes are all **under
  1:40**, and long takes are where lines get skipped or garbled. Nobody has tested a 5-minute read.
- **So the film is cut into ten parts of 25 seconds to 2 minutes**, each ending on a natural break in
  the story, so a seam between takes falls where the picture changes anyway. This is the GPOM model.
- **Rule inherited from GPOM:** a take **20 seconds or more shorter than its twin** has probably
  skipped lines. Check it says every line before judging it.

| Part | Scenes | Movement | Words | Target | Set Duration to |
| --- | --- | --- | --- | --- | --- |
| **P1 Pride** | 01, 02 | 1 Pride | 136 | ≈1:20 | 65 |
| **P2 Shake and starve** | 02a, 03 | 2 The Craftsman | 187 | ≈1:50 | 95 |
| **P3 The rule** | 04 | 2 The Craftsman | 110 | ≈1:05 | 50 |
| **P4 Paying for the war** | 05, 06 | 3 The Build | 169 | ≈1:40 | 85 |
| **P5 Victory, and a death** | 07, 08 | 3 The Build | 143 | ≈1:30 | 75 |
| **P6 The build** | 09, 10, 10b | 3 The Build | 215 | ≈2:05 | 110 |
| **P7 New money, same nurse** | 10a, 11 | 4 The Misuse | 213 | ≈2:05 | 110 |
| **P8 Money was found** | 11a | 4 The Misuse | 170 | ≈1:40 | 85 |
| **P9 The statement** | 12, 13, 14 | 5 The Statement | 187 | ≈1:55 | 100 |
| **P10 One more thing** | 15 | coda | 37 | ≈0:25 | 20 |

Duration is set about 15 seconds under the target, because Suno overshoots (GPOM: 60 → 1:15,
70 → 1:29 to 1:35). P6 and P7 are the longest; if either garbles, split it at the scene boundary
(P6 after scene 10; P7 after scene 10a) before changing anything else.

## 2. House settings (proposed; nothing measured on this film yet)

Starting point is GPOM's house, which is the only narration setting we have evidence for.

| Control | Value | Note |
| --- | --- | --- |
| Model | **v6** | |
| Voice | **Test both** in round 1: `badcode newsreader` (GPOM's saved Voice) and **no Voice** | The storyboard says the narrator is BadCode's voice, which argues for the same Voice as GPOM. But Kai asked for an *English documentary narrator*, which may want a different, older, warmer voice. Round 1 decides |
| Style Influence | **50** | GPOM: dropping from 75 fixed a muffled voice |
| Audio Influence | **65** with the Voice; n/a without | |
| Weirdness | **25** | GPOM: 35 garbled words |
| Variety · Max Mode · Personalize | **Off** · **Off** · **Off** | |
| Vocal Gender | unset with the Voice; **Male** without it | |
| Duration | per part, table above | |

**House rules carried over:** generate verbatim from the block; words change only with Kai;
**record only when Kai says "record"**; **listen (Gemini) only when Kai asks**; one copy of each
part, in this file only.

## 3. House style — one template, three palettes to try

The Style box is one sentence frame for every part, so the ten takes sound like one film. Only the
blanks change per part: `{{PALETTE}}` is fixed for the whole film once round 1 picks it; `{{ARC}}`
and `{{ENDING}}` change per part.

```template
Spoken word narration for a British documentary. One calm English male narrator, warm, dry and unhurried, reading slowly with natural pauses, always clearly on top of the music. Underneath him, a minimal documentary score, mixed far back and low: {{PALETTE}}. His delivery follows the story: {{ARC}}. Close-mic'd and dry, his voice loud and right at the front of the mix, the music always well behind him and never rising over a word. Sparse, quiet, patient, never dramatic, never busy. {{ENDING}} He speaks only the words written.
```

**The three palettes for round 1** (Kai: minimal, documentary, not GPOM's drama):

| Name | `{{PALETTE}}` | Why it might be right | The risk |
| --- | --- | --- | --- |
| **A · Felt piano** | a single soft felt piano playing slow, sparse notes with long gaps, and a low sustained string note far underneath | The modern documentary default; the least likely to fight the voice | Can sound like every documentary; the "stock" risk |
| **B · English pastoral** | a slow string quartet, English pastoral and hymn-like, a solo cello carrying a simple line, very quiet and very sparse | Sounds like the country the film is about; sincere for the patriotic viewer | A melody under him can pull the voice toward singing (GPOM got away with a solo cello) |
| **C · Colliery band** | a distant brass band playing a slow hymn-like chorale, a soft flugelhorn and a tenor horn, as if heard from across a town square | Working-class, northern, 1940s: the film's own reader, and its nostalgia, in one sound | The most characterful and the most likely to go sentimental or loud |

A thought for after round 1, not before: the palette could **change by movement** (brass for Pride
and the Statement, piano alone for the Misuse), which would let the music tell the film's turn
without a word. Test one palette across the whole film first.

**The two endings, verbatim:**

- **hollow:** `No drums at all. It ends hollow, the last note fading to nothing.`
- **resolve:** `No drums at all. The music resolves quietly on his last line and rings out.`

**The Exclude box, the same for every part** (GPOM's, plus the documentary-specific bans):

```
singing, sung vocals, humming, chanting, choir, rap, autotune, female vocals, synth, electronic, drum kit, drum machine, percussion, breakbeat, beat, groove, steady pulse, epic, cinematic trailer, bombastic, loud orchestra, dense orchestration, swelling climax, robotic voice, text to speech, laughing, ad-lib, comedic, novelty, music louder than the voice, music over the vocal
```

**Pronunciations to listen for** (respell only if a take gets one wrong; hyphens stretch a word, so
respell without them): Keynes (rhymes with *rains*; fallback `Kaynes`) · Ruhr (`Roor`) · Aneurin
Bevan (`Anyeyerin Bevan`) · Mone (`Moan`) · Beveridge · Macmillan · reparations.

---

## 4. Round 1 — the style test (run before anything else)

**Generate P1 only**, six ways: palettes **A, B, C** × **with and without** `badcode newsreader`.
Same words, same settings otherwise. Kai picks the palette and the voice by ear; that pick becomes
the house for P2 to P10. Six P1 takes cost less than one wrong full film.

If none of the six sounds like an English documentary narrator, the next lever is **the voice, not
the palette** (skill: "Getting a specific voice"): probe-farm a narrator in his home genre, then
save a new Voice for this film.

---

## 5. The parts

Each part's Style box is the template with its blanks filled. Round 1 fills `{{PALETTE}}`; the
`{{ARC}}` and `{{ENDING}}` for each part are given here. Paste order: **Style, Exclude, Lyrics**,
every round, every box.

### P1 · Pride · scenes 01, 02

`{{ARC}}`: quietly proud and warm about the rescue, then thoughtful as he looks ahead, and gentle on the last line
`{{ENDING}}`: hollow

```lyrics
[Monologue, a calm English documentary narrator, a quiet score far underneath]
Dunkirk... nineteen forty.
More than three hundred and thirty-eight thousand British and Allied troops evacuated from the beaches and harbour.
Naval ships. Merchant crews. Little boats.
People helping people get out alive.
A defeat... and an extraordinary rescue.
Britain remembers the getting-home part.
This is about what came after.

When the war ends, there will still be homes to rebuild, work to find, people getting ill.
Britain will owe about two and a half times what it earns in a year.
In nineteen forty-eight it will open the NHS anyway.
Almost seventy years later, a nurse will ask about her pay... and hear that there is no magic money tree.
Both of those things happened in the same country.
One economist helped explain the first.
He did not live to see it.
John Maynard Keynes.
This is the future he never saw.
```

### P2 · Shake and starve · scenes 02a, 03

`{{ARC}}`: grave and plain about Germany, then drily amused by the builder who cannot build, and matter of fact at the end
`{{ENDING}}`: hollow

```lyrics
[Monologue, a calm English documentary narrator, a quiet score far underneath]
Germany... nineteen twenty-three.
Seventeen years before Dunkirk.
War debts, reparations and a political crisis have strained the state.
It borrows from its central bank, which creates the money.
Then the Ruhr is occupied, and production stalls.
The state pays the workers anyway.
More notes. Fewer goods.
In some places people are paid daily, and hurry to spend it before the prices change.
The currency collapses.
That is one thing you can do with a money tree.
You can shake it.
The money falls.
There is nothing underneath it to buy.

The early nineteen thirties bring the opposite disaster.
Falling prices. Closed works. Queues for a job.
Picture it small.
An unemployed builder. A family needing a house.
The materials, for this example, in the yard.
The builder can build. The family needs a home.
Nothing happens.
Need isn't a paying order.
That is the second thing you can do.
You can starve it.
Keynes challenged the idea that an economy would reliably put everyone to work by itself.
When private spending falls short, government can commission useful work.
The builder hasn't suddenly acquired moral character.
He's acquired a customer.
```

### P3 · The rule · scene 04

`{{ARC}}`: careful and fair-minded, then quietly delighted by the word "actually", and certain on the last line
`{{ENDING}}`: hollow

```lyrics
[Monologue, a calm English documentary narrator, a quiet score far underneath]
That doesn't mean ordering a million houses makes them appear.
If the bricks are missing, make bricks.
If the skills are missing, train people.
Those take time too.
And if everyone is already busy, more money doesn't build more homes.
It bids up the price of the ones there are.
Keynes named that limit himself.
Demand beyond what the country can physically supply is, he said, "the proper meaning of inflation".
Inside that limit...
"Anything we can actually do we can afford."
"Actually" is carrying quite a lot of the sentence.
That is the third thing you can do.
You can plant it.
In work that can actually be done.
```

### P4 · Paying for the war · scenes 05, 06

`{{ARC}}`: sober and respectful about what the war cost, a flicker of dry wit at the tax rates, then hopeful about the peace
`{{ENDING}}`: hollow

```lyrics
[Monologue, a calm English documentary narrator, a quiet score far underneath]
Britain didn't fight the war by discovering a cupboard of free money.
It taxed. Borrowed. Directed production. Rationed goods.
Relied on overseas supplies and support.
People paid in work, in foregone comforts, and in losses no budget can measure.
Keynes worked on the finances.
He proposed taxes and deferred pay to hold spending down while production went to war.
Inflation was the thing he was trying to prevent.
An American army film of the time put Britain's tax rates on the screen.
The highest went to the people with the most.
Winning would leave another job...
organising the peace.

Before victory, Churchill's coalition accepted responsibility for maintaining "a high and stable level of employment" after the war.
Not just finding people something to do in uniform.
Making civilian work a public responsibility.
Beveridge's proposals, and plans for a national health service, were part of the argument about the peace too.
Keynes wasn't building this future alone.
And a promise on paper still needed a government to carry it out.
```

### P5 · Victory, and a death · scenes 07, 08

`{{ARC}}`: brisk and plain about the victory and the debt, warmly amused at Keynes's joke, then slow and very quiet for his death
`{{ENDING}}`: `The music stops completely before his last three sentences, which he reads over silence.` *(if Suno will not stop, use hollow, and the edit takes the music out under scene 08: the plan wants that scene silent)*

```lyrics
[Monologue, a calm English documentary narrator, a quiet score far underneath]
In nineteen forty-five, Britain wins.
Voters elect Attlee's Labour government.
The celebration does not come with a roof.
Debt is enormous. Supplies are short. Rationing continues.
But the war's end releases people and production for civilian work.
Taxes and borrowing remain part of the answer...
so do external finance, and the difficult business of paying for imports.
Keynes negotiates an American loan, then defends it in Parliament.
Still finding time to tell a fellow peer: "I have never heard statistics so funny."
The country doesn't wait to clear its entire debt before rebuilding.
Debt is a burden.
It isn't a veto.

Keynes died on the twenty-first of April, nineteen forty-six.
The NHS would open more than two years later.
He had seen victory.
He would not see this.
We don't know what he would have made of everything that followed.
Other people had the work to do.
```

### P6 · The build · scenes 09, 10, 10b

`{{ARC}}`: warm and quietly proud as the NHS and the homes are built, drily pleased at the patriotism line, then satisfied and certain as the debt is outgrown
`{{ENDING}}`: resolve

```lyrics
[Monologue, a calm English documentary narrator, a quiet score far underneath]
Attlee's government, with Aneurin Bevan as Health Minister, established the NHS.
It took legislation, negotiation, and people turning up to work.
On the fifth of July, nineteen forty-eight, existing hospitals and services became part of a new settlement...
care available to everyone, free at the point of use.
Not free to provide.
The staff and suppliers still had to be paid.
Public funding changed who faced the bill.
A nurse could get on with the work.
A patient could get on with getting better.

Councils commissioned homes. Builders built them. Families moved in.
Not everyone got a home. Not overnight.
But the building continued.
Under the Conservatives, Harold Macmillan made housing a major priority too.
They disagreed about plenty.
Large-scale council building wasn't confined to one party.
A key in a front door is a fairly practical sort of patriotism.

And the debt?
It was never cleared.
In pounds, it kept rising.
The economy rose faster.
People were housed, treated, and in work.
For twenty years, unemployment averaged under two in a hundred.
For twenty-seven years running, the debt shrank against the size of the country.
Not by magic.
Budgets were tight.
Interest was held below inflation, so lenders and savers carried part of the bill.
Quietly.
Britain did not shrink to fit its debt.
It outgrew it.
```

### P7 · New money, same nurse · scenes 10a, 11

`{{ARC}}`: cooler and more clipped now, the present day, fair to the household argument, dry and pointed at "good news, if you owned some", then very quiet and plain for the nurse
`{{ENDING}}`: hollow

```lyrics
[Monologue, a calm English documentary narrator, a quiet score far underneath]
Two thousand and eight.
The banking system is failing.
Government buys bank shares, makes loans, and gives guarantees to keep it standing.
In March two thousand and nine, the Bank of England does something else.
It creates new money, electronically, and uses it to buy bonds.
This is new money. The Bank says so itself.
Most money, in fact, is made by ordinary banks when they lend.
There was never a fixed national pot.
The Bank's new money probably prevented a worse slump.
It also lifted the price of things people already owned.
Good news... if you owned some.

Twenty ten.
Borrowing is very high.
The case for cutting is one every household understands...
you can't keep spending money you haven't got.
The Coalition chooses tax rises and spending restraint.
Mostly restraint.
Public-sector pay is frozen for two years, then held to about one per cent.
So the Bank is creating money while the Treasury is holding it back.
Same country. Same years.
Twenty seventeen. Question Time.
Nurses ask the Prime Minister about pay.
One says her payslip matches the one she had in two thousand and nine.
Theresa May says she recognises the job they do.
Then she says there isn't a magic money tree that we can shake.
You can print the money.
You can't print the nurse.
She was already there.
```

### P8 · Money was found · scene 11a

🔴 **Legal guardrails apply (storyboard §3, scene 11a). Do not generate this part until the scene has
had its legal read and fact re-check; a take recorded before that may have to be thrown away.**

`{{ARC}}`: brisk and factual, fair about the furlough, then scrupulously neutral through the company's story, reading the dates without comment, and finally dry and quietly damning on the last three lines
`{{ENDING}}`: hollow

```lyrics
[Monologue, a calm English documentary narrator, a quiet score far underneath]
Twenty twenty. Covid.
Money is found. In days.
The Treasury borrows hundreds of billions.
The Bank creates hundreds of billions more.
Some of what government spends keeps wages paid.
That part is planted.
Some goes down a priority lane, for suppliers recommended by ministers, MPs and peers.
One company is a few weeks old.
It wins contracts worth two hundred and three million pounds.
The gowns can't be used.
A court orders a hundred and twenty-two million repaid.
The company goes into administration the day before the judgment.
Baroness Mone had told the government she would not benefit.
She later said on television that she stood to benefit from about sixty million.
She denies any wrongdoing.
The following spring, a company run by the supplier's owner of record bought a yacht.
No court has connected those facts.
We are only reading the dates.
In the nineteen forties, the people with the most paid the most.
In the twenty-tens, the nurse paid.
In twenty twenty, some of the people with the most got paid.
```

### P9 · The statement · scenes 12, 13, 14

`{{ARC}}`: warm and a little amused at the 1948 pamphlet, then firm and certain as he makes the statement, and finally very quiet and tender at the end
`{{ENDING}}`: resolve

```lyrics
[Monologue, a calm English documentary narrator, a quiet score far underneath]
Go back to nineteen forty-eight.
Two months after the NHS opened, its own pamphlet told the public...
"no fairy wand was waved on July the fifth".
New hospitals, doctors and nurses had not appeared overnight.
They knew there was no magic.
They built it anyway.
The absence of magic wasn't the end of the discussion.
It was the beginning of a job list.

So.
She was right.
You can't shake it.
People have tried.
You can't starve it either.
That has been tried too.
A household can't create money, or raise a tax.
A country can.
So a country can do the third thing.
You plant it.
There is a magic money tree.
Keynes knew how to use it.
You plant it in work.
Britain did, owing more than it ever had.
Then it outgrew the debt.
"Anything we can actually do we can afford."

Keynes never saw the NHS open.
Other people did.
And every day after that, other people made it work.
We began with getting people home.
A country worth coming home to still needs building.
There should be a life to get back to.
```

### P10 · One more thing · scene 15 (the coda, after the film has ended)

`{{ARC}}`: casual and knowing, as if leaning back in after the credits, then certain on the last three words
`{{ENDING}}`: hollow

```lyrics
[Monologue, a calm English documentary narrator, a quiet score far underneath]
One more thing.
The limit was what we can actually do.
Machines are about to move it.
Borrowing to build was a good bet in nineteen forty-five.
It is a better one now.
Not shaken. Not starved. Planted.
```

*(Kai's open option: add `I would know.` after "Machines are about to move it.")*

---

## 6. Cutting it shorter — candidates for Kai, not applied

Kai wants the film shorter. These are the cuts that lose least, largest first. Word counts are
approximate; at the film's pace about 100 words is a minute.

| Cut | Saves | What it costs |
| --- | --- | --- |
| Scene 06 folded into one sentence in scene 05 ("Before victory, the coalition promised a high and stable level of employment after the war.") | ≈55 words | Beveridge and the "not alone" credit; some cross-party warmth |
| Scene 10a: drop "Most money, in fact, is made by ordinary banks… fixed national pot." | ≈20 | A true, useful aside; the film does not need it to make its point |
| Scene 07: drop "Taxes and borrowing remain… paying for imports." | ≈20 | A fairness caveat; the scene 05 tax beat already carries it |
| Scene 02a: drop "Seventeen years before Dunkirk." and "In some places people are paid daily…" | ≈25 | Some texture; the banknote pictures carry it |
| Scene 03: drop "Keynes challenged the idea… by itself." | ≈15 | The explicit link to Keynes; "commission useful work" still carries it |
| Scene 11: drop "The Coalition chooses tax rises and spending restraint. Mostly restraint." | ≈10 | A good dry line |
| Scene 11a: drop "The Treasury borrows… hundreds of billions more." | ≈15 | Scale; the "in days" line keeps the point |

Taking all of them saves about **160 words, roughly a minute and a half**, and leaves every argument
and every verb beat standing. A deeper cut means losing a scene: the storyboard's own advice is
**02a and 10a first**, because the verbs survive on the cards.

## 7. Round log

Rounds go at the top of `narration-history.md` in this folder once there is one. None yet.
