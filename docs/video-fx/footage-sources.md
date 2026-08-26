# footage-sources — where real footage comes from, and whether we may publish it

**The fifth lane.** [`README.md`](./README.md) lists five: **Flow** invents it, **ffmpeg**
transforms it, **Premiere** cuts it, **After Effects** is not installed — and **sourcing** is this
one: footage that *already exists* and is *free to use*. Reach for it when the shot is a real thing
that really happened — an Apollo launch, a 1950s factory floor, a glacier calving, the fall of
France — and inventing it in Flow would be both worse and a lie.

> **This page is the reference. The operating procedure is the [`find-footage`](../../.claude/skills/find-footage/SKILL.md)
> skill** — the trigger, the licence gate, the three search recipes, the download-and-verify loop
> and the handoff to `premiere_import`. Reach for the skill to *do* the job; come here to look
> something up.

The lane rule is the same shape as the others: **if the thing is real and already filmed, source
it; if it never existed, invent it in Flow.** Sourced footage still goes through the other lanes —
ffmpeg to conform it, Premiere to cut it.

> **🔴 The standing ruling still holds: NO PAID PLUGINS, NO PAID FOOTAGE.**
> Same posture as the README. Of the 68 sources catalogued, **34 are paid-only or licence-blocked**.
> They get one reference table at the bottom saying what we don't use and the free route instead.
> **Never end at "licence it from Pathé."**

> **🔴 The global audio rule: strip the audio from every sourced clip by default.**
> The visuals and the soundtrack of an archive item have **different licences**, and the trap
> recurs on NASA, NASA SVS, ESO, Pond5, NOAA and every "multilayered work" a PD reseller warns
> about: a PD film with a licensed music bed, a narration track someone still owns. `-an` costs
> nothing and we make our own music anyway (`suno-prompt`). Keep native audio only when you have
> read that specific item's credits and the sound is the point.

---

## Contents

| § | What |
| --- | --- |
| [The licence rule](#-the-licence-rule--read-this-before-you-download-anything) | The two questions, the tiers, the check, the risk no licence closes |
| [Find footage — start here](#find-footage-of-a-historical-event--start-here) | The ordered path, the subject map, the worked example end to end |
| [The catalogue: 🟢 green](#-green--publish-it) | 7 sources, verified, publish-it |
| [The catalogue: 🟡 amber](#-amber--usable-with-a-per-item-check) | 27 sources, per-item check required |
| [The catalogue: 🔴 red](#-red--do-not-use) | 34 sources, don't |
| [Download mechanics](#download-mechanics) | Search → metadata → bytes → verify → conform → where it lands |
| [What we deliberately don't use](#what-we-deliberately-dont-use) | And the free route instead |
| [Verification status](#verification-status) | 🔴 What was proven live vs only read. Load-bearing |
| [Known gaps](#known-gaps--nobody-covered-these) | Territories nobody surveyed. Read before promising a subject |

---

## 🔴 The licence rule — read this before you download anything

**Two questions, and they have different answers.** Almost every trap on this page is the gap
between them:

1. **Is the underlying footage's copyright expired or waived?**
2. **Is *this file*, from *this source*, clear for *us* to publish?**

A 1940 Ministry of Information reel answers **probably NOT** to (1) — 🔴 **corrected 2026-08-25,
read off legislation.gov.uk:** UK copyright in a *film* runs under CDPA 1988 **s.13B** — 70 years
from the end of the year of death of the last to die of the principal director, screenplay author,
dialogue author and composer — and s.13B "contains no special provisions for works created by the
Crown"; the 125-years / 50-from-publication Crown rule in **s.163** is expressly limited to
"a literary, dramatic, musical or artistic work" and does not reach films. So *Listen to Britain*
(McAllister d.1962) may be in copyright to end-**2032** and *London Can Take It!* (Watt d.1987) to
end-**2057**; only a Jennings-solo film (d.1950) is plausibly expired. The old line here ("pre-June-1957
Crown material generally expired") was search-snippet folklore and is withdrawn. A NARA/FedFlix
"public domain" tag on a British MOI film reflects the **US** position (non-renewal), not UK
clearance — and BadCode publishes from the UK. Evidence and the per-title workings:
[`../stories/magic-money-tree/research/documentary-research-2026-08-25.md`](../stories/magic-money-tree/research/documentary-research-2026-08-25.md) §1.
And still **no** to (2) if you pull it from IWM,
because IWM licenses its own print under its own terms regardless.

### The single most dangerous misconception

> **"It's old" is not a licence. "It's on the Internet Archive" is not a licence. "It's on
> YouTube" is not a licence. "Royalty-free" is not a licence.**

- **archive.org's `licenseurl` field is *uploader-asserted*.** IA's own rights page says it
  "does not make guarantees as to the copyright status of items on archive.org and cannot
  guarantee information posted on item details or collection pages regarding copyright." A
  measured example: `identifier:youtube-*` alone matches **2,059,500 items** — the site is
  saturated with mirrors uploaded by people with no rights to them.
- **"Old" is per-title, not per-decade.** A 1935 US film is public domain only if it was never
  renewed in its 28th year (1929–1963 works). Plenty of majors renewed everything. Conversely a
  clip shot by a federal employee last week is PD on day one under 17 USC §105.
- **"Royalty-free" is a *pricing* model** — pay once instead of per-use. It says nothing about
  what you may do. RF stock EULAs routinely carry editorial-only and no-political-use clauses,
  which is precisely our use case.

### The tiers

| Tier | What it means | Examples |
| --- | --- | --- |
| 🟢 **Green** | Publish it. US federal work (17 USC §105), an institutional PD dedication, or CC0 — **and we made the call live ourselves.** No credit obligation, no clause to weigh | `gov.archives.arc.*`, `collection:nasa`, `gov.dod.dimoc.*`, `universal_newsreels`, images-api.nasa.gov, NASA SVS, Wikimedia Commons *(CC0/PDM subset only)* |
| 🟡 **Amber** | Usable, but **per-item check required** before it ships. A mixed collection, an inferred licence, a credit or ShareAlike obligation, a clause that might bite, or a source we never authenticated against | Prelinger, Library of Congress, ESO, NPS, DVIDS, NARA v2, Adobe Stock Free, Europeana `reusability=open`, Pexels, Pixabay, CERN, ESA's CC subset, C-SPAN, OGL/OPL leads |
| 🔴 **Red** | Do not use without a paid licence or a legal call. Paid houses, non-commercial licences, embed-only channels, dead domains | IWM, BFI, British Pathé, AP, Reuters/ITN, Getty Embed, Storyblocks, `collection:feature_films`, YouTube's CC-BY filter, anything CC-BY-**NC** |

**🔴 Two rules that changed the tier list on 2026-08-22, and are the reason it is shorter than it
was:**

1. **Green means *verified by us*, not *ought to be fine*.** DVIDS, NARA v2 and Adobe Stock Free
   were rated green on documentation alone — no authenticated call was ever made to any of them.
   They are amber until someone makes one.
2. **Green means no obligation we cannot discharge.** "CC-BY where we will actually carry the
   credit" used to be a green criterion. **We have nowhere to carry a credit.** There is no credits
   surface in `@badcode/comic`, no end-card convention, nothing. Until one exists and Kai rules on
   where it lives, **every CC-BY and CC-BY-SA source is amber** — that alone moved ESO out of green.
   See [Naming and disk layout](#naming-and-disk-layout) for the receipt convention and the open
   question.

**🔴 Every green source can still contain an identifiable real person**, and no licence on this page
clears what our cut implies about them. NASA, DVIDS, NPS, ESO, LoC and C-SPAN are *full* of named
people. Read [the one risk a licence check cannot close](#-the-one-risk-a-licence-check-cannot-close)
before any of them goes near a political argument.

### 🔴 CC-BY-NC is a hard kill for BadCode

NonCommercial is defined in the CC 4.0 legalcode as "not primarily intended for or directed
towards commercial advantage or monetary compensation." **We sell music.** That is judged at the
release/entity level in practice, not per transaction — "we didn't charge for this comic" does not
cure NC footage inside a commercial collective's output. If you see `by-nc` or `by-nd` anywhere in
a `licenseurl`, stop.

**CC-BY-SA is a different problem:** ShareAlike is not a commercial-use bar, but it forces the
*finished piece* to be relicensed CC-BY-SA. Editing a clip into a comic is an adaptation. Treat SA
as amber and get a human call before it goes in.

### The clearance check — two halves, and only one of them is fast

🔴 **This was called "the 60-second check" and that was a lie.** The first half is scriptable and
genuinely takes seconds. The second half is a judgement call a human has to make, and pretending
otherwise is how a clause gets missed.

**Half A — the machine check (seconds, scriptable, do it every time):**

1. **Provenance.** Is this a federal-agency work, an institutional PD dedication, or an explicit
   CC0 from the actual rights-holder — not an uploader's assertion? *(On archive.org: is the
   identifier prefix or collection one of the green ones below? An `@nasa.gov` / DIMOC / NARA
   uploader counts; a personal gmail address does not.)*
2. **Licence string.** Read the exact code, not the substring. `creativecommons.org` also matches
   `by-nc-nd`. **BY / BY-SA / CC0 / PDM are different answers.** On Commons, read
   `extmetadata.LicenseShortName` — do not eyeball the page.
3. **Obligation.** Does it require attribution or ShareAlike? If yes it is **amber, not green** —
   we have no credits surface yet (see above).

**Half B — the human check (minutes, not seconds, and it cannot be automated):**

4. **The host's own terms.** Is the hosting institution asserting a *separate* fee/permission gate
   over its print or scan, on top of the underlying copyright? (IWM, BFI, Pathé, CERN: yes.)
   *Worked instance: CERN's `license` field reads the bare string `"CERN"` — which looks like an
   unset placeholder and is in fact a bespoke licence barring use "in advertising or promotion."*
5. **Restoration.** If UK-sourced: is this a modern restoration/rescan an institution claims fresh
   skill-and-labour copyright in? Under UK law it may genuinely have one, even over PD source.
   *Worked instance: a BFI 4K rescan of a 1920s PD title is not a PD file.*
6. **Political and endorsement clauses.** Almost every stock and agency licence on this page has
   one — Pexels and Pixabay bar political context by name, Adobe bars "implied or stated
   endorsements of political parties," NASA and DVIDS bar implied endorsement, DVIDS bars implying
   endorsement of "any political party or candidate." **BadCode's entire output is political
   argument.** *Worked instance: ambient clouds behind a song is not the same act as a stock clip
   of a recognisable person under a line attacking a party — the first is arguable, the second is
   the clause.*
7. **People in frame.** Will our cut put an identifiable real person in a context the original
   footage didn't support? **No licence clears that** — see the note below.

**The gate:** Half A failing kills the clip on the spot. Half B is what "amber needs a per-item
check" actually means, and **nothing amber ships without a human having answered 4–7 out loud.**

### 🔴 The one risk a licence check cannot close

Recutting genuine, cleanly-licensed archive footage of a real, identifiable person to build a
political argument the original context did not carry is a **defamation-by-false-implication**
risk. It lives in the juxtaposition, not the clip. It survives a perfect clearance pass. It scales
with exactly what BadCode does. **This needs a human read on the finished cut, every time** — it is
not a sourcing decision.

---

## Find footage of a historical event — start here

The ordered path. Stop at the first hit.

**1. Is it a US federal government subject?** (space, military, agriculture, public health,
national parks, government-made propaganda, government-commissioned industrial film)
→ **`identifier:gov.archives.arc.*`**, **`collection:nasa`**, **`gov.dod.dimoc.*`** on
archive.org. 17 USC §105. Green, no further licence check — but still read Half B question 7 if a
named person is on screen.

**2. Is it a 20th-century American ephemeral/industrial/educational subject?**
→ **Prelinger, filtered to `licenseurl:*`.** 1,913 of 10,459 items self-declare PD. Green for that
subset. The other 82% need a per-item look at the sponsor/production company.

**3. Is it a mid-century news event?**
→ **`collection:universal_newsreels`** (PD by NARA's 1976 dedication — the single cleanest licence
position in this whole survey). 🔴 **Trap: only 611 items are digitised** and coverage is patchy —
a May–July 1940 date-range query returns **zero** hits. It answers "browse what's online," not
"find this specific event."

**4. Was it filmed by a foreign government or an enemy, and compiled by the US?**
→ Search for the **US War Department / DoD compilation**. Captured German film reissued as a War
Department bulletin is a US federal work. The Dunkirk worked example below is exactly this.

**5. Is it UK government or Parliament?** → **the open-licence route, not the film archives.**
OGL v3 and the Open Parliament Licence both permit commercial exploitation with attribution. 🟡
Amber and **untested for AV** — see [Open licences (UK)](#open-licences-uk--ogl-v3-and-opl-v3).
Worth twenty minutes before you conclude "UK is all paid," because for *political* footage —
which is what we mostly want — it is the only free route that exists.

**6. Nothing yet? Widen to Wikimedia Commons.**
→ Every file carries a machine-readable licence in `extmetadata`. 🔴 **But most of them are
CC-BY-SA, which is amber by our own ShareAlike rule** — the doc's own demo query returns 6 BY-SA,
1 BY, 1 CC0 out of 8. **Filter on `LicenseShortName` for CC0 / Public Domain Mark / a §105 source,
or you are not in the green tier.** Formats are `.webm`/`.ogv` — budget a transcode.

**7. Europe-specific? Europeana with `reusability=open`.**
→ Real, working filter. But only ~12,972 of 389,151 video items are "open" (~3%), and the file
usually lives on the *provider's* server, not Europeana's.

**8. Would a still do the job?** 🔴 **Ask this earlier than feels natural.** A slow push-in on a
1,000-pixel-wide PD photograph, cut on the beat, reads as archive and costs a fraction of the hunt.
**LoC, Commons, NARA and Smithsonian stills are orders of magnitude richer than their video** —
Smithsonian Open Access is a dead end for footage and a real CC0 source for images. Premiere does
the move (`premiere-automation`, Motion Scale/Position keyframes); ffmpeg does it headless
(`zoompan`, brief 16). Note the same licence rules apply to a still as to a clip.

**9. Still nothing? Ask whether Flow should invent it instead.**
→ Before you go near IWM/Pathé/BFI. For a war scene, a factory floor, a crowd — Flow is free at the
margin and carries no rights question. **Sourcing exists for footage whose *being real* is the
point.** If it isn't, invent it.

**10. Step 10 is the trap, not a step: the obvious specialist.** British Pathé, IWM, BFI, AP,
Reuters/ITN, Huntley, Hearst, March of Time, NFB, NFSA — **all red, all paid.** Their whole business
model is licensing the footage. Being the specialist is exactly why they are the wrong tool for us.
If you have got this far, the answer is Flow or a still, not a quote request.

### Subject map — where BadCode's actual subjects live

The path above is chronological-and-jurisdictional. This table is the shortcut for the handful of
subjects our stories keep asking for. 🔴 **Entries marked *unsurveyed* are honest gaps** — nobody
has run these queries; treat them as leads, not as promises.

| Subject | First stop | Notes |
| --- | --- | --- |
| **Space, flight, launches** | `collection:nasa`, images-api.nasa.gov, NASA SVS | The best-covered territory on the page by a distance |
| **Military, war, the fall of France** | `gov.dod.dimoc.*`, `gov.archives.arc.*`, `universal_newsreels` | US federal compilations of European events — accept it won't carry a British uniform |
| **Factory floors, industry, machinery** | Prelinger (`licenseurl:*`) sponsored industrials; CERN's `type=FOOTAGE` (36 items, 🟡 licence) | 🔴 **The weakest territory we have.** See [Known gaps](#known-gaps--nobody-covered-these) |
| **Protest, strikes, picket lines, labour, crowds** | *Unsurveyed.* Leads: Prelinger's sponsored-film and newsreel material; Commons `Category:Demonstrations`, `Category:Strikes`; `universal_newsreels` | 🔴 **For a collective whose subject is the ownership of the means of production, this is the most embarrassing gap on the page.** Nobody has run a single query. Run them and write the results back |
| **Money, markets, trading floors, banks, budgets** | *Unsurveyed.* Leads: Prelinger sponsored finance/insurance films; `universal_newsreels` for crash/budget coverage; C-SPAN 🟡 for hearings | 🔴 Magic Money Tree and Emperor's New Coin both need this and it does not exist here yet |
| **Named decision-makers speaking** (the house rule: *name the decision-maker*) | 🟡 C-SPAN for US hearings and floor; 🟡 OGL/OPL for UK ministers and Parliament | **Both amber, both with real clauses.** This is the territory where the licence gate bites hardest, because the whole point is a real identifiable person |
| **Nature, climate, ice, ocean** | NASA SVS, NOAA (🟡 — NOAA's *videos* are its one non-PD exception) | SVS hands you the mp4 URL directly |
| **Modern ambient b-roll** (skylines, hands, screens) | 🟡 Pexels / Pixabay / Coverr — or **just make it in Flow** | The political-context clause makes stock a worse fit than Flow for anything pointed |
| **A still instead** | LoC, Commons, NARA, Smithsonian Open Access (CC0, images only) | See step 8. Usually the right answer and usually skipped |

### Worked example — "find Dunkirk footage", end to end

Three candidates the search turns up. **Only two of them are green, and the difference is the
whole lesson.**

| Item | What it is | Verdict |
| --- | --- | --- |
| **`gov.dod.dimoc.30172`** — *Army in Action, Ep. III: Flames on the Horizon* | Covers the Fall of France, May–June 1940 | 🟢 **Green.** `licenseurl` = **CC0**, `collection: FedFlix / usgovfilms`. 🔴 **Correction, 2026-08-22:** this page used to say "posted by DoD's own DIMOC account" — it is not. The uploader is `carl@media.org` (Public.Resource.Org, the FedFlix operator). The identifier encodes DIMOC's record number; the *account* is FedFlix. Still green — trusted prefix, trusted operator, explicit CC0 — but the reason is FedFlix, not DIMOC |
| **`Dividean1943_2`** — Frank Capra, *Divide and Conquer* (Why We Fight #3), Part II | Description states it covers *"the evacuation of the British forces at Dunkirk"* | 🟢 **Green.** `collection: prelinger`, US War Department production, textbook §105, `licenseurl` = `licenses/publicdomain/`. 🔴 **Name trap: three differently-named files on one item** — `_512kb.mp4` (55,557,824 B), `.mp4` (82,009,431 B), `_edit.mp4` (285,508,616 B) |
| **`FB-56`** — War Department Film Bulletin 56, *The Western Battle Front, May–June 1940* | Captured German film compiled by the US Signal Corps. NARA description: *"Shows the Dunkirk evacuation; wreckage; and British POWs."* | 🟡 **Amber — and it was rated green here until 2026-08-22, which was wrong.** See below |

#### 🔴 Why FB-56 is amber: the flagship example failed our own check

Re-run live 2026-08-22, `curl -s https://archive.org/metadata/FB-56`:

```
uploader   : jilly@poetryhut.com
collection : ['wwIIarchive', 'folkscanomy_history', 'folkscanomy']
licenseurl : http://creativecommons.org/publicdomain/mark/1.0/
rights     : None      source : None
```

A **private individual**, in **community collections**, with an **uploader-asserted PD Mark**. That
fails Half A question 1, it fails the `collection:` filter rule below, and it is precisely the
"PDM is uploader-asserted" warning at the top of this page. The *underlying* War Department
bulletin is very probably genuinely PD — but **the chain shown is the one we tell you never to
trust**, and "it's obviously a War Department film" is not a check, it is a vibe.

**Curing it — required whenever the identifier is not on a trusted prefix:**

1. Find the same work on a trusted prefix first. `identifier:gov.archives.arc.*` + a title search
   is one query, and if it hits you are done — take that copy instead. *(Ran it for "film
   bulletin": `numFound: 0`. Not cured this way.)*
2. Failing that, pin the record at NARA. FB-56's description cites **NARA ARC 24464**; look it up
   in the NARA catalog and read the use-restriction field. That is the rights-holder's own
   statement about the work, which is what the uploader's PDM was standing in for.
3. Record the answer in the receipt JSON (see [Naming and disk layout](#naming-and-disk-layout))
   with the URL you read it from. **If you cannot cure it, it stays amber and needs Kai's call** —
   don't launder it by calling it green.

#### The whole path, one block

🔴 **This is the only end-to-end sequence on the page. Everything else is a fragment.** It runs
query → metadata → largest original → download → md5 → duration → conform → ready for
`premiere_import`, on the green `gov.dod.dimoc.30172` item.

```bash
set -euo pipefail
ID=gov.dod.dimoc.30172
DEST="$MEDIA_ROOT/footage/archive.org/$ID"      # MEDIA_ROOT = premiere_status().mediaRoot, WSL form
mkdir -p "$DEST"

# 1. SEARCH — always scoped to a trusted collection/identifier prefix
curl -s 'https://archive.org/advancedsearch.php?q=identifier%3Agov.dod.dimoc.*+AND+mediatype%3A(movies)+AND+%22fall+of+france%22&fl[]=identifier&fl[]=title&fl[]=licenseurl&rows=10&output=json' \
  | jq -r '.response.docs[] | [.identifier, .licenseurl, .title] | @tsv'

# 2. METADATA — the receipt AND the only authoritative filename list
curl -s "https://archive.org/metadata/$ID" > "$DEST/source-metadata.json"
jq -r '.metadata | {identifier,uploader,licenseurl,collection}' "$DEST/source-metadata.json"   # ← Half A runs on this

# 3. PICK the largest true original (never guess a filename)
read -r NAME MD5 SIZE < <(jq -r '[.files[] | select(.source=="original") | select(.name|test("\\.(mp4|mov|mpeg|mpg|avi|ogv|webm)$";"i"))]
  | sort_by(.size|tonumber) | last | [.name, .md5, .size] | @tsv' "$DEST/source-metadata.json")
echo "picked: $NAME  ($SIZE bytes, md5 $MD5)"

# 4. DOWNLOAD — -L is mandatory; a bare HEAD on archive.org is always a 302
curl -sL -C - -o "$DEST/raw.${NAME##*.}" "https://archive.org/download/$ID/$NAME"

# 5. VERIFY — byte count is not enough; diff the hash against the declared one
test "$(stat -c%s "$DEST/raw.${NAME##*.}")" = "$SIZE" && echo "size ok"
echo "$MD5  $DEST/raw.${NAME##*.}" | md5sum -c -

# 6. DURATION — ffprobe exit 0 does NOT mean whole file. Compare against the declared length
jq -r --arg n "$NAME" '.files[] | select(.name==$n) | .length' "$DEST/source-metadata.json"
ffprobe -v error -show_entries format=duration -of csv=p=0 "$DEST/raw.${NAME##*.}"

# 7. CONFORM for the timeline — -an because the audio has its own licence
ffprobe -v error -show_entries stream=field_order -of csv=p=0 "$DEST/raw.${NAME##*.}"   # deinterlace only if tt/bb
ffmpeg -y -i "$DEST/raw.${NAME##*.}" -an -c:v prores_ks -profile:v 3 -vendor apl0 \
  -pix_fmt yuv422p10le "$DEST/conform-prores.mov"

# 8. HAND OFF — the path is under mediaRoot, so Premiere can see it
echo "premiere_import({ paths: [\"$DEST/conform-prores.mov\"] })"
```

And the trap the same search finds: `10904germannewsreelbattlefordunkerquemosvwr` — a Periscope
Film upload titled *BATTLE OF DUNKIRK & FALL OF FRANCE 1940 GERMAN BLITZKRIEG NEWSREEL*, freely
downloadable, `licenseurl` = **`by-nc-nd/4.0`**. Free to fetch, illegal for us to publish.

---

## The catalogue

### 🟢 Green — publish it

**7 sources.** 🔴 **This tier lost five members on 2026-08-22** — ESO, NPS, DVIDS, NARA v2 and
Adobe Stock Free all moved to amber. Three of them (DVIDS, NARA, Adobe) had never been
authenticated against at all, and green now means *we made the call ourselves*; the other two carry
obligations or clauses we cannot discharge. They are all still perfectly usable; they are just not
"publish it without looking."

| Source | Holdings *(counts 2026-08-22)* | API | Key | Licence basis |
| --- | --- | --- | --- | --- |
| **archive.org `gov.archives.arc.*`** (FedFlix/NARA) | **2,107** movies — NARA-digitised federal film (2,106 with a `licenseurl`) | ✅ | — | 17 USC §105 + explicit CC0 |
| **archive.org `collection:nasa`** | 13,733 movies — mission footage, NASA TV | ✅ | — | 17 USC §105 (expect **no** `licenseurl`) |
| **archive.org `collection:universal_newsreels`** | 611 digitised reels, 1932–1967 | ✅ | — | NARA PD dedication, 1976 |
| **archive.org `gov.dod.dimoc.*`** | DIMOC-numbered records, uploaded by FedFlix | ✅ | — | 17 USC §105 + CC0 |
| **images-api.nasa.gov** | Every NASA centre's photo/video/audio | ✅ | ❌ none | 17 USC §105 |
| **NASA SVS** (svs.gsfc.nasa.gov/api) | Climate/ocean/orbital data-viz + produced video | ✅ | ❌ none | 17 USC §105 |
| **Wikimedia Commons — CC0 / PDM subset only** | 70M+ files; **the free-licence majority is CC-BY-SA, which is amber** | ✅ | ❌ none | Per-file licence in `extmetadata`, **checked per file, every time** |

🔴 **All seven still carry the endorsement / right-of-publicity / false-implication problem** on any
identifiable person in frame. §105 waives *copyright*. It waives nothing else.

#### The green tier, machine-readable

For a session that wants to filter candidates programmatically rather than read a table. **Kept in
sync by hand — if you change a tier above, change it here.**

```json
[
  {"id":"ia-fedflix",      "tier":"green","endpoint":"https://archive.org/advancedsearch.php","scope":"identifier:gov.archives.arc.*","auth":"none","licence":"US-17USC105 + CC0","count":2107,"asof":"2026-08-22"},
  {"id":"ia-nasa",         "tier":"green","endpoint":"https://archive.org/advancedsearch.php","scope":"collection:nasa","auth":"none","licence":"US-17USC105","count":13733,"asof":"2026-08-22"},
  {"id":"ia-newsreels",    "tier":"green","endpoint":"https://archive.org/advancedsearch.php","scope":"collection:universal_newsreels","auth":"none","licence":"PD-dedication-NARA-1976","count":611,"asof":"2026-08-22"},
  {"id":"ia-dimoc",        "tier":"green","endpoint":"https://archive.org/advancedsearch.php","scope":"identifier:gov.dod.dimoc.*","auth":"none","licence":"US-17USC105 + CC0","count":null,"asof":"2026-08-22"},
  {"id":"nasa-images",     "tier":"green","endpoint":"https://images-api.nasa.gov/search","scope":"media_type=video","auth":"none","licence":"US-17USC105","note":"rejects api_key with HTTP 400"},
  {"id":"nasa-svs",        "tier":"green","endpoint":"https://svs.gsfc.nasa.gov/api/search/","scope":"q=","auth":"none","licence":"US-17USC105","note":"hands you the literal mp4 url"},
  {"id":"commons-cc0",     "tier":"green","endpoint":"https://commons.wikimedia.org/w/api.php","scope":"extmetadata.LicenseShortName in [CC0, Public domain, PDM]","auth":"none","licence":"CC0/PDM","note":"any other LicenseShortName is amber"}
]
```

**The one-line filter that keeps you in the green tier on archive.org:** never issue a query
without `identifier:` or `collection:` pinned to one of the four scopes above.

---

#### archive.org — the query API (the mechanism behind four green tiers)

The search surface is `advancedsearch.php`. **The API itself is safe; an unscoped query is not.**
A bare `title:"dunkirk" AND mediatype:(movies)` surfaces community-media local-news mirrors with
zero `licenseurl` before any curated result. **Always add a `collection:` or `identifier:` filter
to a trusted tier.**

Verified query syntax:

- `q=` takes Lucene boolean: `AND`/`OR`, `field:value`, `identifier:X*` wildcard,
  `year:[1965 TO 1972]` range, `licenseurl:*` existence check, `title:"exact phrase"`
- `fl[]=field` — repeat per field: `fl[]=identifier&fl[]=title&fl[]=licenseurl&fl[]=year`
- `sort[]=downloads+desc`
- `rows=` / `page=` for pagination (verified: `page=2&rows=3` returns `start=3`)
- **`rows=0` is a free count-only query** — use it to size a collection without pulling docs
- `output=json` required

```bash
curl -s 'https://archive.org/advancedsearch.php?q=collection%3Aprelinger+AND+mediatype%3A%28movies%29+AND+licenseurl%3A*&fl[]=identifier&fl[]=title&fl[]=licenseurl&fl[]=year&sort[]=downloads+desc&rows=20&page=1&output=json'
```

**Bulk listing** is a different endpoint — `https://archive.org/services/search/v1/scrape?q=...&fields=...&count=N`.
`count` has a **hard minimum of 100** (`count=5` → HTTP 400 "count is too small"); it returns a
base64 cursor for paging past the ~10k row limit `advancedsearch` pagination hits.

**The `ia` CLI** is real and free: `pip install internetarchive` (v5.11.1, Python ≥3.10). `ia search
'<query>' --itemlist` and `ia metadata <id>` both work and beat hand-rolled curl+jq for exploration.
⚠️ Agents disagree on `ia download`: one hit read-timeouts (12s default) in a sandboxed session and
recommended direct `curl -L` for media pulls; another used `ia metadata` cleanly without comment.
**Use `ia` for search/metadata, curl for bytes.**

🔴 **The `fav-<username>` contamination trap.** Almost every item's `collection` array also lists
dozens of personal-favourites pseudo-collections. A long collection array is **not** institutional
backing. Look for the real names among the clutter.

**Rate limits:** 8 rapid sequential requests (~0.7s each) drew no throttling and no 429. That is not
proof none exists at volume. IA's docs document 429 with an `X-Accept-Reduced-Priority` opt-in. Be a
good citizen: sequential, 1–2s between calls, back off on 429.

---

#### archive.org `gov.archives.arc.*` — FedFlix / National Archives

**2,107 items** (re-counted live 2026-08-22; 2,106 of them carry a `licenseurl`). 🔴 **This page
said 2,218 and that was stale — date-stamp every collection count you write here, because they
move.** Collections: `FedFlix`, `usgovfilms`, `newsandpublicaffairs`.
This is a level above a generic "gov" claim: **the identifier itself encodes the NARA ARC catalog
number**, and the uploader is `carl@media.org` — Public.Resource.Org, the named FedFlix operator,
not an anonymous account.

```bash
curl -s 'https://archive.org/advancedsearch.php?q=identifier%3Agov.archives.arc.*+AND+mediatype%3A%28movies%29&fl[]=identifier&fl[]=title&fl[]=collection&rows=20&output=json'
```

Verified sample `gov.archives.arc.13496` (*Tahtonka*, USDA Forest Service): `licenseurl` = **CC0**.
File ladder: `.mpeg` original MPEG2 at 1,362,977,061 bytes (the master), `_512kb.mp4` at
121,791,529 B and `.ogv` at 141,034,116 B (auto-derivatives). For a 1.3GB source the `_512kb.mp4`
is the practical "just works" pick.

#### archive.org `collection:nasa`

**13,733 items** (verified). 🔴 **`collection:NASAarchive` returns zero** — the identifier is just
`nasa`, and that had to be discovered, not assumed.

🔴 **Do not apply the "no `licenseurl` = suspicious" heuristic here.** Sampled item
`Hq-194_apollo11TheEagleHasLanded2.wmv` has `licenseurl=None` and `rights=None`, because federal
works have no copyright *to* licence. The trust signal is the uploader: `maura.white-1@nasa.gov`.
An `@nasa.gov` address is as strong as CC0 metadata.

That item has **no mp4 derivative at all** — only the `.wmv` original (1,090,992,983 B) and a
low-res `.ogv` (143,414,853 B). Enumerate `files[]`, take the largest `source:"original"`,
transcode locally.

#### archive.org `collection:universal_newsreels`

Universal City Studios' newsreels 1929–1967, **donated to NARA and placed in the public domain in
1976**. NARA holds ~6,000 edited reels + 8,500 of outtakes; **only 611 are digitised on IA**
(verified count, earliest 1932).

```bash
curl -s 'https://archive.org/advancedsearch.php?q=collection%3A(universal_newsreels)+AND+date%3A[1940-05-01+TO+1940-07-15]&fl[]=identifier&fl[]=title&fl[]=licenseurl&rows=50&output=json'
```

🔴 **That exact query returns `numFound: 0`.** Best licence position in the territory, thin
coverage. Browse it; don't rely on it for a named event.

#### archive.org `gov.dod.dimoc.*` — DoD DIMOC records, via FedFlix

Defense Imagery Management Operations Center records. Verified item `gov.dod.dimoc.30172` carries
`licenseurl` = **CC0**.

🔴 **Corrected 2026-08-22.** This entry previously claimed the items were posted by "DoD's own
institutional account." **They are not.** Re-run live, `gov.dod.dimoc.30172`'s uploader is
`carl@media.org` and its collections are `FedFlix / usgovfilms / newsandpublicaffairs` — the same
Public.Resource.Org operation behind `gov.archives.arc.*`. The identifier encodes DIMOC's own
record number, which is why the prefix is trustworthy; the *account* is FedFlix. Green on the same
basis as FedFlix — named operator, gov-numbered identifier, explicit CC0 — **not** on the basis of
being an agency account. If you were relying on "the agency posted it themselves," you were
relying on something that is not true.

🟡 **File-size note.** The largest `source: "original"` on that item is a **949,987,612-byte
MPEG-2** (`.mpeg`, declared length 1732.73s); the `_512kb.mp4` at 125,430,767 B is the practical
pick for anything but a hero shot. The runbook above takes the largest original by design — override
step 3 when you want the derivative.

```bash
curl -s 'https://archive.org/advancedsearch.php?q=(%22fall+of+france%22+OR+%22british+expeditionary+force%22)+AND+mediatype%3A(movies)+AND+licenseurl%3A(*publicdomain*)&fl[]=identifier&fl[]=title&fl[]=licenseurl&fl[]=collection&rows=30&output=json'
```

#### NASA — images-api.nasa.gov

Fully open, **no auth of any kind**. Passing `api_key=DEMO_KEY` to this endpoint returns **HTTP
400** — it does not accept the param at all, unlike other `api.nasa.gov` data APIs. Do not assume
one auth scheme across `*.nasa.gov`.

```bash
curl -s 'https://images-api.nasa.gov/search?q=apollo&media_type=video&center=JPL'
```

**Three-step indirection.** Search returns `collection.items[]`, each with an `href` pointing at a
per-asset `collection.json` manifest — *not* at a video. Fetch the manifest, then take a file URL.

🔴 **Two traps, both hit live.** (1) The returned URLs contain **literal unencoded spaces** and are
`http://` — percent-encode and force https yourself. (2) Variants are **tilde-suffixed**:
`~orig.mp4`, `~large.mp4`, `~medium.mp4`, `~small.mp4`, `~mobile.mp4`, `~preview.mp4`.

⚠️ **Agents disagree on which suffixes exist.** One verified `~medium.mp4` at HTTP 200 (65,068,407 B)
while `~large.mp4` and `~orig.mp4` **403'd** on that item, concluding orig is a `.mov`; another
verified a `~large.mp4` at HTTP 200 (183,473,399 B) on a different item. **Resolution: the manifest
is the authority. Parse it, don't generalise the ladder across items.**

🟡 **The music trap.** NASA *produced* videos (intro graphics, narration) sometimes carry a licensed
stock-music bed — one credited *"Music: 'Smart Future' from Universal Production Music"*. The
visuals are PD; the audio may not be. **Check the credits field before keeping native audio; mute
and replace by default** (the global audio rule at the top of this page).

🔴 **§105 waives copyright and nothing else. NASA's media guidelines carry three further
restrictions this page used to omit, and every one of them lands on BadCode's use case:**

> *"If the NASA material is to be used for commercial purposes, including advertisements, it must
> not explicitly or implicitly convey NASA's endorsement"*

> current employees and astronauts *"cannot have their names, **likenesses** or other personality
> traits displayed… on any commercial products, advertisements, promotional material"*

> where images include identifiable individuals, *"using the media for commercial purposes may
> infringe that person's **right of privacy or publicity**"*

**Read that against what we do.** Apollo footage of a named astronaut, recut under a line about
who owns the future, is a commercial use of an identifiable person's likeness in a persuasive
piece. The clip is free; the *cut* is the exposure. This is the same problem as
[the risk a licence check cannot close](#-the-one-risk-a-licence-check-cannot-close) — and it is
why "green" on this page never meant "no thinking required." Crowds, hardware, launches, Earth
views: fine. A named person's face carrying an argument: human call, every time.

NASA's insignia has its own separate restriction — don't use the meatball as branding.

#### NASA SVS (Scientific Visualization Studio)

A **separate, better-shaped API** from images-api. Climate/ocean/ice/hurricane visualisation and
produced explainers — the science-and-machines register.

```bash
curl -s 'https://svs.gsfc.nasa.gov/api/search/?q=glacier'          # verified: count 10556
curl -s 'https://svs.gsfc.nasa.gov/api/13660/' | jq -r '.main_video.url'
```

**It hands you the literal mp4 URL** — no filename guessing. Verified:
`.../a013660/OIB_Alaska_Final_Export_8.mp4`, 1920×1080, 407,598,044 bytes, `Accept-Ranges: bytes`.

🔴 The human-facing `/13660` URL is not the API — you need `/api/<id>/`. Same music-bed caveat as
above, and it bites more often here because SVS produced-video items are edited pieces.

#### Wikimedia Commons — 🟢 green **only** for the CC0 / PDM subset

**The most reliably machine-checkable rights signal in the entire survey** — and, until
2026-08-22, mis-tiered because of it. Every file must carry a *free* licence to be hosted at all,
and it is exposed as structured `extmetadata` (`LicenseShortName`, `LicenseUrl`, `Copyrighted`,
`AttributionRequired`). But **"free" in Commons' sense includes CC-BY-SA, and this page's own rule
puts ShareAlike in amber** — editing a clip into a comic is an adaptation, which would force the
finished piece out under CC-BY-SA.

🔴 **How badly does that bite? Re-ran this entry's own example query live on 2026-08-22.** Of the
8 results:

| `LicenseShortName` | Count |
| --- | --- |
| CC BY-SA 3.0 / 4.0 | **6** |
| CC BY 3.0 | 1 |
| CC0 | 1 |

**Amber is the majority case, by a lot** — six of eight — and the green subset was one file. Worse,
zero of the eight were WWII footage: the query returned a handball match, four cycling stages, an
aerial beach shot and a Spitfire experience, all in Dunkerque, France. **Commons search matches the
place name, not the event.** Budget for that: name the event, the year and the belligerents, or
traverse a category instead of searching.

**So the rule is mechanical, not advisory: read `LicenseShortName` on every single file. CC0 or
Public Domain Mark → green. Anything else → amber, and BY-SA needs Kai's call.**

```bash
# search
curl -s 'https://commons.wikimedia.org/w/api.php?action=query&format=json&generator=search&gsrsearch=filetype:video%20dunkirk&gsrnamespace=6&gsrlimit=5&prop=imageinfo&iiprop=url|size|mime|extmetadata'
# category traversal
curl -s 'https://commons.wikimedia.org/w/api.php?action=query&format=json&generator=categorymembers&gcmtitle=Category:Videos%20from%20NASA&gcmtype=file&gcmlimit=50&prop=imageinfo&iiprop=url|size|mime|extmetadata'
```

`imageinfo.url` **is** the direct file URL, no auth, `Accept-Ranges: bytes`. Verified: a Commons
WWII reel at `Content-Length: 1,689,032,627` (1.69GB), and a smaller `.webm` at 32,236,320 B.

🔴 **Never construct an `upload.wikimedia.org` path by hand.** The directory is not alphabetical —
it is the first hex char and first two hex chars of `md5(underscored_filename)`. Verified:
`md5('Czechoslovak_arms_factories_1938_newsreel.webm') = 24ed9ab3…` → bucket `2/24`. Hitting `1/24`
returns a clean 404. Take the URL from `videoinfo.url`.

Other traps: `filetype:video` in `gsrsearch` is a **hint, not a hard filter** — verify `mime` in the
response. Files are enormous and in `.webm`/`.ogv` (Commons rejects mp4 uploads), so budget a
transcode. Category names are inconsistent free text — traverse several. And a file being on
Commons is not proof it was legitimately uploaded: **cross-check the stated source** (e.g. "Library
of Congress — no known copyright restrictions") for anything load-bearing.

The `videoinfo` call returns codec, resolution, fps, duration and bitrate inline — **read that
before deciding whether to pull 81MB.** It is your pre-flight ffprobe.

---

### 🟡 Amber — usable with a per-item check

**27 sources.** 🔴 **Amber is not "probably fine."** It means a human answers Half B questions 4–7
on *this item* before it ships — and for the political-clause sources (Adobe, Pexels, Pixabay,
DVIDS, C-SPAN) that answer has to be written down, because our whole output is political argument.

| Source | Why amber | API | Key |
| --- | --- | --- | --- |
| **archive.org `advancedsearch`** (mechanism) | Safe to call; an unscoped query is dangerous | ✅ | — |
| **archive.org Prelinger** | Only 18% carry a `licenseurl`; the rest need a sponsor check | ✅ | — |
| **Library of Congress** | "No known copyright" is LoC's *opinion*, not statutory PD | ✅ | ❌ |
| **Europeana** | `reusability=open` is only ~3%; file usually lives off-platform | ✅ | ✅ free |
| **Open Beelden** (NL) | Real downloadable mp4s, but Atom-feed-only and per-item licence varies | 🟡 feeds | ❌ |
| **Deutsche Digitale Bibliothek** | CC0 covers the **metadata only**, never the media | ✅ | ✅ free |
| **Pexels** | 🔴 explicit **political-context exclusion** | ✅ | ✅ free |
| **Pixabay** | Same political exclusion; only pre-2019 uploads are true CC0 | ✅ | ✅ free |
| **Coverr** | No political clause found — possibly our safest stock tier — but thinly verified | ✅ | ✅ free |
| **Mixkit** | Free-License and **Restricted-License** clips mixed in one result set | ❌ | — |
| **Pond5 Public Domain Project** | Pond5 **disclaims** PD warranty and pushes risk to you | ❌ | — |
| **Shutterstock free tier** | Real licence, tiny pool (~40 videos) | ❌ | — |
| **CERN CDS Videos** | Great open API, restrictive bespoke licence | ✅ | ❌ |
| **ESA** | Only an ~86-video **CC-BY-SA 3.0 IGO** subset is safe | ❌ | — |
| **NOAA Photo Library** | NOAA itself flags **video** as its one non-PD exception | ❌ | — |
| **NOAA Ocean Exploration** | PD in principle; basket-and-email ordering, not scriptable | ❌ | — |
| **USGS Multimedia** | Federal PD in principle; **WAF-blocked**, and agents disagree on the colour | ❌ | — |
| **PD movie aggregators** | Whole features, no metadata trail, wrong shape for clips | ❌ | — |
| **ESO** *(was green)* | CC-**BY**, plus a commercial bar on identifiable people and a music carve-out | ❌ HTML | — |
| **NPS Multimedia API** *(was green)* | **24 of 30 records carry a named non-NPS credit** — the check is the norm, not the edge case | ✅ | ✅ free |
| **DVIDS** *(was green)* | Never authenticated; policy restricts commercial use and bars implying political endorsement | ✅ | ✅ free signup |
| **NARA Catalog API v2** *(was green)* | Never authenticated — no key was ever obtained | ✅ | ✅ free, by email |
| **Adobe Stock Free** *(was green)* | 🔴 Explicit **political-endorsement prohibition** in Adobe's Additional Terms | ❌ browser | Free Adobe ID |
| **C-SPAN** *(new)* | Congressional floor coverage has a genuine PD basis; **C-SPAN's live page bars unlicensed commercial use of its programming** | ❌ | — |
| **American Archive of Public Broadcasting** *(new)* | Rights assessment is pushed onto the user, and the site is **US-IP-restricted** | 🟡 | — |
| **OGL v3 — UK government AV** *(new)* | Commercial exploitation permitted with attribution; **whether it reaches AV is untested** | — | — |
| **Open Parliament Licence v3** *(new)* | Same shape; 🔴 parliamentlive.tv's own T&Cs are *more* restrictive | — | — |

---

#### Prelinger Archives

~10,459 movies (verified): US ephemeral film 1927–1987 — industrial, educational, advertising,
government, home movies. **The canonical American ephemeral-film archive**, curated by Rick
Prelinger himself.

🔴 **Only 1,913 of 10,459 items (18%) carry an explicit `licenseurl`** (verified via `rows=0`
count). Where present it is typically `creativecommons.org/licenses/publicdomain/`. **The other 82%
assert nothing.** Prelinger's own stated position: items without a CC licence on the page "may not
be reproduced for commercial purposes of any kind without permission" (`prelingerclips@gmail.com`).
Collection membership is strong provenance; it is not a machine-checkable grant.

**House answer: filter to `licenseurl:*` and treat that 1,913-item subset as green.** For anything
outside it, check the item description for sponsor/production company first.

Verified sample `AboutBan1935` (United Fruit Company, 1935): `licenseurl` =
`creativecommons.org/licenses/publicdomain/`. Its 47-file ladder — masters are `.mpeg` (306,617,225
B) and `_edit.mp4` ("HiRes MPEG4", 211,573,767 B, **bigger and better than the auto-derivative**);
derivatives are `.mp4` (68,512,128 B), `_512kb.mp4` (45,941,165 B), `.ogv` (46,417,991 B).

#### Library of Congress

**The opposite case to NASA: a green-looking API over amber content.** The National Screening Room
and film-and-video holdings are dominated by **donated** collections — Prelinger, and commercial
newsreel houses like Castle Films (confirmed on a record actually pulled: *News Parade of the Year
1945*).

LoC's blanket statement is *"not aware of any U.S. copyright or other restrictions in the vast
majority"* — a **no-known-copyright opinion**, not a §105 claim, and LoC says so in the same
paragraph. **Green only when the item's creator field names an actual federal office** (Signal
Corps, OWI, USIA). **The `rights` field is prose HTML, not a boolean** — you must read it per item.

```bash
curl -sL 'https://www.loc.gov/collections/national-screening-room/?fo=json&c=5&q=world+war'
curl -sL 'https://www.loc.gov/item/2015600171/?fo=json'
```

Every loc.gov page accepts `&fo=json`. Verified: item 2015600171's mp4 at
`https://tile.loc.gov/storage-services/service/mbrs/ntscrm/00056155/00056155.mp4`, metadata size
366,773,204 bytes — **byte-exact match** on a HEAD. A `.mov` preservation master (1.2GB), `.vtt`
captions and poster frames sit alongside.

🔴 Traps: many catalog records aren't digitised and return `resources: []` (verified on item
91482338). Search results carry `http://` URLs that need `-L`. **The video URL is inside a deeply
nested `files[][]` array whose shape differs by collection — don't hardcode indices.**

#### Europeana

389,151 VIDEO-typed items from 3,000+ European institutions. Strong on continental Europe, **thin
on the UK: 494 video items total, only 247 of them "open."**

Reusability facet (verified, sums exactly to total): **open 12,972 / restricted 42,419 / permission
333,760.** Only "open" (~3%) is commercially safe.

```bash
curl -s "https://api.europeana.eu/record/v2/search.json?wskey=api2demo&query=*:*&qf=TYPE:VIDEO&reusability=open&rows=10&profile=rich"
```

🔴 **`reusability` is a top-level param, not a `qf=` filter.** `qf=REUSABILITY:open` **silently
returns 0** with no error — verified across 4–5 syntax variants. Same for `qf=RIGHTS_OPEN:true`.

🔴 **Europeana is a discovery layer, not reliably a hosting layer.** `edmIsShownBy` on an "open"
record frequently points at the *provider's* player — verified `https://vimeo.com/438840139` on one
CC-cleared item. Others are real direct files (verified `.mp4` links on filmportal.de and
openbeelden.nl, rights = PublicDomainMark 1.0). Check the URL shape before assuming curl fetches
bytes.

🔴 Naive substring-matching `creativecommons.org` in the `rights` field also catches **CC-BY-NC**
(46,396 items). Use the exact licence code, or lean on `reusability` as the coarse filter.

Free key at `apikey.europeana.eu`. `api2demo` works for testing, rate-limited, not for production.

#### Open Beelden (Netherlands Institute for Sound & Vision)

~7,000+ items of Dutch AV heritage, 1920s–2000s, released specifically to seed CC reuse. **Genuinely
downloadable mp4s with `Content-Disposition: attachment`** — rare in this territory.

```bash
curl -s 'https://www.openbeelden.nl/feeds/atom/?q=oorlog'   # oorlog = war
```

Parse the mp4 URL out of the Atom entry's HTML content field (pattern
`https://www.openbeelden.nl/files/NN/NN/<id>.mp4`), then curl it. Verified: an 11,877,942-byte
`video/mp4` at HTTP 200.

🔴 No JSON REST API — this is a legacy CMS with Atom/RSS feeds; `format=json` is silently ignored
and returns HTML. 🟡 The feed-level `<rights>` tag says CC-BY 3.0 but that is a **platform default**
— at least one item is actually tagged Public Domain Mark. Grep the item page for the real licence.
Dutch-only content; no UK relevance beyond general European B-roll.

#### Deutsche Digitale Bibliothek

**⚠️ Largely unverified.** The key requirement was confirmed live (an unauthenticated call returns
HTTP 403 `NotAuthorizedException`); nothing else was.

🔴 **The advertised CC0 covers the *search metadata* only.** The media files carry each contributing
institution's own `dcterms:rights` statement — likely the same InC/CC mix as Europeana, since DDB
feeds Europeana. Do not extrapolate.

Free key via a "Meine DDB" account. The auth header format (`Authorization: OAuth <key>`) should be
confirmed against DDB's OpenAPI once you have one — **not verified here.**

#### Pexels

Broad modern stock: nature, people, urban, abstract loops. High production value, **not archival**.
Free commercial use, no attribution required.

🔴 **The clause that matters to us:** *"You cannot use Content in a political context (such as the
promotion, advertisement or endorsement of any party, candidate, or elected official…)"* and content
"featuring a recognisable person" cannot imply endorsement.

**How to read that for BadCode:** ambient b-roll — clouds, skylines, hands typing — as texture
behind original comic/song content is a different thing from using stock footage to promote or
attack a party or candidate. **But no Pexels clip is blanket-cleared for whatever the finished piece
does.** Anything with a recognisable person in overtly political content needs a manual call.

```bash
curl -H 'Authorization: YOUR_API_KEY' 'https://api.pexels.com/videos/search?query=nature&per_page=15&size=large'
```

Free key, instant, from pexels.com/api. **200 req/hour, 20,000/month** (documented, not load-tested).
`video_files[]` gives `{quality, width, height, fps, link, size}` — **take the exact `link`, the
frame-rate suffix in the filename varies per clip.** The CDN itself needs no key once you have the
link (verified: a 14,157,772-byte mp4 at HTTP 200).

🔴 **The cache trap — a genuinely novel finding, twice, independently.** An unauthenticated call to a
common query returned **HTTP 200 with a full valid result** — because Cloudflare replayed someone
else's authenticated response (`cf-cache-status: HIT`, `age: ~946525`s ≈ 11 days). A cache-busted
call with a nonce query immediately returned the correct **401 "Missing API key."**
**Never test "does this need a key?" with a plausible query. Always append a nonce.** And do not
report Pexels as keyless.

#### Pixabay

Same shape as Pexels, huge volume, mixed quality.

🔴 **Two-tier licence:** content published **before 2019-01-09 is CC0**; everything since is
Pixabay's own custom Content License. "Pixabay = CC0" is a stale reputation — most current results
are the newer tier.

🔴 **Same political-context exclusion** as Pexels, near-identically worded.

```bash
curl 'https://pixabay.com/api/videos/?key=YOUR_KEY&q=nature&per_page=20'
```

Key in the **query string** (verified: no key → HTTP 400 `[ERROR 400] Invalid or missing API key`).
100 requests per 60 seconds. Four tiers per video: `tiny` / `small` / `medium` / `large`, each with a
direct CDN url in the search response — no second call needed.

🟡 **Ops hygiene:** query-string keys land in shell history, proxy logs and `curl -v` output. Header
keys don't. Scrub or inject via `curl --config`.

#### Coverr

Smaller, curated, boutique. **No political-use clause was found in the licence text fetched** —
which may make it our *safest* stock tier for anything pointed. Irrevocable, worldwide, free,
commercial use included.

🔴 Its standout clause is an **AI-training prohibition**: *"Our videos and music must not be used to
train AI algorithms, develop AI models, or serve as part of any dataset for such purposes."*
Irrelevant to publishing; relevant if anything downstream ever trains on our assets. Resale as a
standalone product is banned.

```bash
curl -H 'api_key: YOUR_KEY' 'https://api.coverr.co/videos?query=nature&sort=popularity'
```

Verified live: no key → HTTP 401 `{"message":"Invalid API_KEY"}`. **No authenticated response
observed** — the video-file URL field and resolutions are undocumented from our side.

⚠️ **Rate limits contradictory and unresolved:** one doc page says free/staging = **1000 calls per
month**, another source says **50 calls/hour**; production is quoted as both "2,000/hour" and
"500/min". **Check your own dashboard.** Amber rather than green pending a closer read of
coverr.co/terms.

#### Mixkit (Envato)

Polished modern b-roll, browse-and-download only. **No API** — a guessed `/api/videos` path returns
HTTP 301, confirming none exists.

🔴 **The trap:** two licence tiers live in the **same search results**, distinguished only by a badge
on the item page — **"Free License"** (free commercial, no attribution) and **"Restricted License"**
(non-commercial only). Grab the wrong one in a fast pipeline and you have published something
non-commercial-only. **Check the badge on every clip.**

As an Envato property it inherits Envato's Acceptable Use Policy, which prohibits "untruthful or
defamatory material about a person that would have the likely tendency to lower their estimation in
the eyes of others." Not a political-content ban — but our satire has to stay factually groundable.

#### Pond5 Public Domain Project

Live counts (Dec 2025 snapshot): **Footage 1,000 files**, Audio 2,754, Images 63,824, 3D 121. 🔴 The
widely-cited "80,000 free clips / 10,000 video" figure is from the **2015 launch PR** — do not quote
it as current.

Pond5's grant: *"provided by Pond5, free of charge for unlimited use,"* royalty-free lifetime
worldwide. 🔴 **But a separate legal page disclaims warranty of PD status entirely** and shifts
verification onto you — naming the exact traps: multilayered works (a PD film with a non-PD
soundtrack), background IP in frame, and depicted-people privacy/publicity rights without a model
release, recommending such content be treated as **editorial use only**. Same uploader-asserted
problem as archive.org, just with a brand on it.

No API. pond5.com bot-blocks curl (403). Requires a free account and the web UI.

#### Shutterstock free tier

~3 free photos + **~40 curated free videos** + 2 AI generations per free account. The old
"10 free images" trial ended **March 1, 2024**. The specific free-tagged items carry a real Standard
License — commercial use, 500,000 reproductions, $10,000 indemnification. **The pool is hand-picked
and tiny; it is an occasional freebie, not a source.** No API to the free subset.

*(Detail via a secondary source — shutterstock.com bot-blocks. See verification table.)*

#### CERN CDS Videos

🔴 **The clearest example in this whole survey that an open API is not an open licence.**

Genuinely excellent API — Invenio, keyless, no rate-limit friction, direct file downloads. And a
dedicated **`type=FOOTAGE`** facet (36 items) of raw accelerator-tunnel, detector-assembly and
lab-infrastructure b-roll — exactly the monumental-machine register.

```bash
curl -s 'https://videos.cern.ch/api/records/?q=collider&size=10&type=FOOTAGE'
# then: .metadata._files[0].links.self  →  a direct api/files/<bucket>/<name>.mp4
```

Verified: aggregations VIDEO 1955 / FOOTAGE 36; a real file at 478,006,191 bytes, HTTP 200, no auth.

🔴 The licence is a bespoke **"General CERN Licence"** — the record's `license` field just reads the
string `"CERN"`, which looks like an unset placeholder and **is not**. CERN's Terms of Use: free for
"educational and informational use" only; CERN retains copyright; material "may not be used in a
misleading, inappropriate or offensive manner, in a military context, **in advertising or
promotion**"; and "may not be sold, distributed or otherwise made available for use by third
parties."

**Our read:** commercially-sold, persuasive political comics sit closer to "advertising or
promotion" than to "educational," and the no-redistribution clause is in tension with publishing
footage inside a distributed work. **Usable for genuinely explanatory framing with a clear ©CERN
credit. Not cleared for music-video b-roll or merch.** Get a human call.

*(`cds.cern.ch`, the older Document Server, sits behind an Anubis bot-challenge and is not
curl-accessible at all.)*

#### ESA — European Space Agency

🔴 **The central trap of the space territory: ESA is not blanket CC.**

**Two regimes on one site.** (1) The **site-wide default** is a bespoke free-but-restricted licence:
usable without fee for "educational, editorial or informational" purposes with mandatory ©ESA
credit, but explicitly *"shall not be used for a commercial purpose, such as but not limited to,
entertainment, advertisement, merchandising"* without written ESA authorisation. (2) A separate,
**explicitly tagged subset** is **CC BY-SA 3.0 IGO** — and it is **BY-SA, not BY**.

The safe subset is reachable at a filter URL (verified — the page literally reads "Search 86 Results
for Description: 'Creative Commons' in Videos"):

```
https://www.esa.int/ESA_Multimedia/Keywords/Description/Creative_Commons/(result_type)/videos
```

Then parse the video page for `https://dlmultimedia.esa.int/download/public/videos/...mp4` (an
`orig-` prefixed master is usually offered too). Verified one at HTTP 200, `video/mp4`.

🟡 **ShareAlike rides along even on the safe subset** — anything we build with it must itself go out
CC BY-SA 3.0 IGO, and it's the **IGO port**, so link `creativecommons.org/licenses/by-sa/3.0/igo/`.
Everything outside those 86 videos needs written permission from `spaceinvideos@esa.int`.

#### NOAA Photo Library

🔴 **NOAA itself singles out video as its one exception**, and this is NOAA's own wording, not our
speculation: images "are in the 'public domain' and cannot be copyrighted… you may use it without
express permission," but — *"The one exception is our videos, as they often use third-party
copyrighted footage."*

An agent that treats "NOAA = government = PD" uniformly across media types **will get this wrong.**
Check every video's caption/credit for a named non-NOAA rights holder.

No JSON API found — `/noaa-collections/search/photo-library?query=<term>` is a JS-rendered UI that
returns HTML even with `Accept: application/json`. Browser click-path only.

#### NOAA Ocean Exploration Video Portal (NCEI)

Deep-sea ROV and expedition footage, searchable by expedition ID / location / keyword / depth /
dates. **No API, by design** — confirmed from the portal's own help page.

The click-path: check "Web streaming" boxes → **"Get File(s)"** returns a ZIP of preview-quality
clips immediately. For **full-resolution ProRes masters**, check "Full-resolution," enter an email,
submit — NOAA runs an **async retrieval-from-deep-storage job** and emails a link. Genuinely high
quality, genuinely not scriptable.

🔴 It looks like it should have an API. It does not. Don't burn time reverse-engineering one.

#### USGS Multimedia — ⚠️ contested, unresolved

Geology, mining, hydrology, volcanoes, earthquakes, Landsat/EROS, field footage. Federal, so §105
PD in principle.

🔴 **The whole domain is behind an AWS WAF JS-challenge.** `curl` to `/media/videos` returned **403**
(919-byte block page); `/multimedia-gallery` with a browser UA returned **HTTP 202 with a zero-byte
body** and `x-amzn-waf-action: challenge`. Both agents hit this independently. **A 202-empty
response looks superficially like success** — a naive pipeline will record a working source that
isn't.

⚠️ **Agents disagree on the colour.** One marked it **red** ("operationally unreachable, nothing
here should be asserted as fact yet"); the other marked it **amber** ("licence basis is solid, mark
amber for 'verify before shipping,' not because the licence is suspect"). **We have filed it amber
and flagged the disagreement.** The PD-by-policy claim itself was never read off usgs.gov — it comes
from a search summary. Needs a real browser session before we rely on it.

#### Public-domain movie aggregators

`publicdomaintorrents.info`, `publicdomainmovies.net`, PD Info. **Whole PD feature films** — classic
B-movies, horror, sci-fi. PD status is the site's own per-title claim with no metadata trail like
archive.org's provenance signals.

🔴 **Structurally the wrong tool** for sourcing a specific historical-event clip. Included so nobody
wastes an hour finding that out. **Unverified — not fetched.**

#### ESO — European Southern Observatory — 🟡 **demoted from green 2026-08-22**

**CC BY 4.0 by default**, confirmed on ESO's own copyright page: *"the images, videos, and music
distributed on the public ESO website … are licensed under a Creative Commons Attribution 4.0
International License."* That part is true and was verified live.

🔴 **What this page used to say was false.** It read: *"Commercial use and adaptation included;
only a visible, unaltered credit is required."* Three clauses on the same ESO page say otherwise:

> **"If an image includes a picture of an identifiable person, using that image for commercial
> purposes is not permitted."**

> "ESO materials, images and videos may not be used to state or imply the endorsement by ESO or any
> ESO employee of a commercial product or service"

> "note that **music**, scientific papers, code, and text other than press releases… **are not
> released under the Creative Commons Attribution 4.0 International License**"

**Why each one lands on us specifically.** We recommended ESO for *"Paranal/ALMA/ELT, telescope
machinery"* — the shots that most often have a technician in frame, and technicians are
identifiable people. **BadCode sells music**, so "commercial purposes" is us, not somebody else.
And ESO videos ship with **ESO's own music bed, explicitly outside the CC BY grant** — the same
trap as NASA and SVS, which is why the audio rule at the top of this page is global.

**House answer: strip the audio, prefer plates with no people in them, carry the ©ESO credit — and
if a person is identifiable, it needs Kai's call, not a licence check.** Plus the standing CC-BY
problem: we have no credits surface, so even a clean ESO plate is amber until we do.

No API. HTML only, but the CDN paths are predictable:

```bash
curl -s 'https://www.eso.org/public/videos/eso2612a/' \
  | grep -oE 'https://cdn2?\.eso\.org/videos/[a-z_0-9]+/eso2612a\.mp4'
```

Renditions: `ultra_hd`, `ultra_hd_h265`, `hd_1080p25_screen`, `medium_podcast`. Verified
`hd_1080p25_screen/eso2612a.mp4` at 983,696,048 bytes. "Unless specifically noted" means checking
the detail page for a named non-ESO photographer to credit instead.

#### NPS Multimedia API — 🟡 **demoted from green 2026-08-22**

**10,634 videos** (verified count). Federal, DOI agency, §105 — **the licence basis is not in
doubt.** What is in doubt is who actually shot each one.

```bash
curl -s 'https://developer.nps.gov/api/v1/multimedia/videos?limit=3&api_key=DEMO_KEY'
```

🔴 **The third-party credit is the default case, not an edge case.** This page filed it as a 🟡
spot-check under a green rating. Pull 30 records and **24 of them carry a named non-NPS credit** —
outside companies (`Ploeger ASL Interpreting, LLC/NPS`) and bare personal names (`Kevin Bryant`,
`Tom Bartels`). **A check required on 80% of items is the definition of amber.** The `credit` field
is free text and is not a rights flag: it does not tell you whether the named party was a
contractor-for-hire (work made for hire, NPS owns it, §105 applies) or a donor who licensed it in
(they still own it). You have to establish which.

Each item's `versions[]` holds a direct CDN mp4 on nps.gov. Verified a 360p file at 98,682,801
bytes, HTTP 200. Only one version was populated on that record — **check the array length, don't
assume HD exists.**

🔴 `DEMO_KEY` is a **shared api.data.gov-wide** key — fine for a one-off, useless in production (the
same key hit `OVER_RATE_LIMIT` against Smithsonian in the same session). Get a free real one at
api.data.gov/signup.

#### DVIDS — 🟡 **demoted from green 2026-08-22**

1.8M+ items of US military-produced news/photo/video/audio. Free registration at
dvidshub.net/member/registration; keys look like `key-XXXXXXXXXXXXX`.

```bash
curl -s 'https://api.dvidshub.net/search?q=tank&type=video&api_key=key-XXXXXXXXXXXXX'
```

**Demoted for two independent reasons, either of which is sufficient.**

🔴 **(1) The licence is not the flat §105 grant this page implied.** From dvidshub.net's own
copyright page:

> "DoW VI may be distributed, copied, and used, **for non-commercial, personal use**, as well as
> historical and newsworthy purposes"

> commercial use "for advertisements, marketing, promotion, solicitation, or fundraising purposes"
> **requires a non-endorsement disclaimer**

> material "may not be used in a manner that could imply endorsement of… **any political party or
> candidate**"

> "Some VI… may be subject to copyright or other intellectual property rights owned by non-DoW
> parties"

The underlying federal works are still PD — but DVIDS is a *distribution service* carrying more
than federal works, and the political-endorsement clause is aimed squarely at what we make.

⚠️ **(2) No authenticated call was ever made.** A placeholder key returned HTTP 200 with
`{"errors":["Unauthorized - Provided API key is not authorized"]}` — proving the endpoint, params
and error shape are real, and nothing else. The documented video-record shape (a `files[]` array of
mp4 tiers from 486×274@300kbps up to 1280×720@9173kbps, plus `hls_url` and `closed_caption_urls`)
is **from DVIDS' docs, not observed.**

🔴 The 403 error text mentions origin-locking to a key's associated domain — **may not work
server-side from WSL.** Confirm with DVIDS before building on it. Also: a search result's `url`
field points at the *webpage*, not a file; the Asset API is a separate call.

**To promote it back to green:** get a key, make one authenticated call from WSL, and resolve the
non-commercial clause against a specific piece of BadCode output. Two of those are ten minutes; the
third is Kai's.

#### NARA Catalog API v2 — 🟡 **demoted from green 2026-08-22**

The primary source behind archive.org's `gov.archives.*` mirror, and the place you go to **cure**
an uploader-asserted PD claim (see the FB-56 example). Key is **free but human-issued**: email
`Catalog_API@nara.gov`.

```bash
curl --location 'https://catalog.archives.gov/api/v2/records/search?q=constitution' \
  --header 'x-api-key: YOUR_API_KEY'
```

⚠️ **Demoted purely for verification, not for licence risk.** NARA's PD-as-federal-work position is
sound; **no key was ever obtained, so no response was ever seen.** 10,000 queries/month per key,
resetting on the 1st, is from NARA's own README (which *was* fetched successfully). The
digital-object field names are from docs, **not observed** — flag this gap to whoever requests the
key, and promote this entry the day someone makes a real call.

🔴 **Calling without a key does not error.** It returns **HTTP 200 serving the catalog's HTML
single-page app** — which looks like success in a naive integration test and contains no data.
Check content-type/JSON-parseability, never just the status code. The Swagger docs render
client-side; `swagger.json`/`openapi.json` all return the same wrapper HTML.

#### Adobe Stock Free collection — 🟡 **demoted from green 2026-08-22**

1.1M+ free assets including video, carved out of Adobe's 590M paid library. Adobe's page copy:
*"Free to download, cleared for commercial-use, royalty-free, no credit card required."*

🔴 **This page called it "the only genuine free, commercial-safe find in the whole commercial-houses
territory." That was wrong, and it was wrong in a way that contradicted this page's own rules.**
Free-collection assets download under the same Standard License and are governed by Adobe Stock's
Additional Terms, §3.1 of which prohibits:

> "(E) use the Stock Assets in a manner, or in connection with a subject, that a reasonable person
> could consider unflattering, immoral, offensive, obscene, or controversial… examples of which
> could include… **implied or stated endorsements of political parties or other opinion-based
> movements**; or implying mental or physical impairment"

> "(D) use the Stock Assets in a manner that is pornographic or **defamatory**"

**That is the same clause family we ambered Pexels and Pixabay for** — so rating Adobe green while
ambering them was a straight internal contradiction, sitting on the source this page recommended
most enthusiastically. There is also an unmentioned **500,000-reproduction cap** on the Standard
License; irrelevant at our scale today, relevant if anything ever travels.

🔴 **Read it against BadCode plainly:** we publish opinion-based political argument. Clause (E) does
not ban that outright — it bans doing it *with Adobe's assets in a way that reads as endorsement or
as controversial subject matter*. Where the line is, is a human call. Ambient texture behind a song
is arguable; a stock face under a line about a party is the clause. **Nothing from Adobe Free ships
without that call being made and recorded.**

🟢 **It is not a Creative Cloud perk.** Open to anyone with a free Adobe ID; our CC subscription
unlocks nothing extra here.

Browser only: `stock.adobe.com/free`, or filter any search — `stock.adobe.com/search/video?k=free`.
🔴 stock.adobe.com **hard bot-blocks** unauthenticated non-browser requests (403), so there is no
curl path; an authenticated browser session is required. ⚠️ The page copy itself was only ever read
via a **web.archive.org snapshot** — a third reason this is amber. Adobe has an official Stock API
supporting a free-content filter — **untested, treat as unverified.**

⚠️ This applies **only to the "Free"-badged subset.** The wider paid library is red like any other
stock house.

#### C-SPAN — 🟡 **new 2026-08-22, and it is not the green source it looks like**

**Why it is here at all:** hearings and floor debate are where *named decision-makers* say the
thing on the record, and `docs/marketing/the-reader.md` rule is **name the decision-maker, never
the technology**. There is no other free source for this at all. It was missing from a 61-source
survey and that was a real gap.

**The genuine PD basis:** video of proceedings originating from the House and Senate chambers is
recorded by the chambers' own recording studios — federal employees — so the *underlying* feed is
a US government work with no copyright to license.

🔴 **But C-SPAN's live copyright page, fetched 2026-08-22, reads:**

> "C-SPAN does **NOT** permit unlicensed commercial use of any of its audio or video programming
> (including coverage of federal government events) whether or not C-SPAN is attributed as the
> source."

> a licence is required for "Documentaries, films, television programs or podcasts… Any use that
> relies substantially on C-SPAN content to generate revenue."

> a licence is "generally not required to post a recording of C-SPAN's… coverage of federal
> government events online **for non-commercial purposes** so long as C-SPAN is attributed"

**So: PD underlying feed, restrictive distributor.** The widely-repeated line that C-SPAN floor
coverage "may be used without restriction or attribution" did **not** appear anywhere on the page
we actually fetched — do not quote it. Non-floor, C-SPAN-*produced* programming (*Washington
Journal*, studio forums) is plainly not PD, and licensing for those is $100/programme/year,
**streaming only, no downloading**, which is useless to an edit.

**House answer:** treat C-SPAN's own player as a discovery tool, then **go and get the same
proceeding from the chamber's own feed or from a federal source** rather than from C-SPAN's file —
that is where the PD claim actually lives. If only C-SPAN has it, it is a human call, and the
honest framing is that we would be relying on the underlying-work argument against the
distributor's stated position. 🔴 **Untested from our side: nobody has yet found and pulled a
chamber-original file.** That is the next twenty minutes of work in this territory.

#### American Archive of Public Broadcasting — 🟡 **new 2026-08-22**

**The answer to "what about TV news after the newsreel era?"**, which this page previously
dead-ended at "all red." AAPB is a Library of Congress + GBH partnership holding decades of US
public radio and television — 1960s through 2000s, exactly the gap between `universal_newsreels`
(stops 1967) and the paid wire archives.

🔴 **Two facts a session needs before spending time here:**

1. **Rights assessment is pushed onto the user.** AAPB is a preservation and access programme, not
   a licensor: it makes material available for research and does not clear it for reuse. Every item
   needs its own rights conversation with the contributing station. It is a *finding aid*, not a
   source of publishable files.
2. **The site is US-IP-restricted** for much of its content — which matters from WSL, because our
   whole toolchain is a curl on a UK connection. Expect to be blocked before you expect to be
   licensed.

⚠️ **Unverified from here** — listed because its absence was a real gap, not because we have used
it. If you do try it, write down what actually happened.

#### Open licences (UK) — OGL v3 and OPL v3

🟡 **New 2026-08-22.** 🔴 **This page used to say UK free-and-clear footage is "essentially none." That is true of the UK
archival film *houses* — Pathé, IWM, BFI, Huntley are correctly red — and it was never tested
against the UK's open-licensing regime at all.** Given the target reader is British and the house
rule is *name the decision-maker*, **UK government and parliamentary footage is the most
load-bearing under-explored territory on this page.**

**Open Government Licence v3.0** — fetched verbatim from nationalarchives.gov.uk, 2026-08-22:

> "You are free to: **copy, publish, distribute and transmit the Information**; **adapt the
> Information**; **exploit the Information commercially** and non-commercially"

Attribution only: *"Contains public sector information licensed under the Open Government Licence
v3.0."* Its exemption list is explicit and matters to us: **personal data; departmental logos,
crests and the Royal Arms; military insignia; third-party rights the Information Provider is not
authorised to license.**

**Open Parliament Licence v3.0** — same shape, same commercial permission, attribution
*"Contains Parliamentary information licensed under the Open Parliament Licence v3.0."*
⚠️ **Not verified live here: parliament.uk sits behind a Cloudflare JS challenge** (confirmed
2026-08-22 — a direct fetch returns "Enable JavaScript and cookies to continue"). Read it in a
browser before relying on the wording.

🔴 **The trap, and it is a textbook instance of this page's two-questions split:**
**parliamentlive.tv has its own Downloading & Sharing terms, and they are *more* restrictive than
OPL** — barring use for "advertising, promotion… or financial gain." So a debate can be OPL-licensed
as *information* and still be barred as *this file from this host*. ⚠️ Those terms were **not
readable live either** — `/Guidance`, `/Help` and `/Home/Copyright` all returned the site's 404
page on 2026-08-22. Find the current URL in a browser.

**Amber, and honestly amber: nobody has established that OGL reaches moving-image material at all.**
Departmental video may be OGL, may be Crown copyright with separate terms, may be third-party
production. **The next step is concrete and small** — pick one gov.uk or departmental video, find
its stated licence, and write the answer here. Until someone does, this is a lead, not a source.

---

### 🔴 Red — do not use

**34 sources.** Paid, non-commercial-only, embed-only, or dead. Grouped by why.

#### Paid archive houses (the "obvious" specialists)

| Source | The position | Price |
| --- | --- | --- |
| **British Pathé** | 85,000+ newsreels, all on YouTube. Asserts copyright over its **entire collection**, states **none of it is public domain**. YouTube embed is free; extraction or editing needs a paid per-second licence — *"this requirement applies irrespective of whether we supply the material to you ourselves or you have obtained it from another source."* Preview downloads are watermarked. **Downloading from YouTube does not launder the rights.** | Per-second, 60s minimum. A ~$2,500+/minute figure appeared in search snippets — **unconfirmed**, no live vendor page fetched |
| **IWM** | The definitive UK WWI/WWII official archive. Two tiers: a **free Non-Commercial Licence** and paid commercial licensing. 🔴 The free tier **expressly excludes** use "intended for or directed toward commercial advantage," commercial-organisation websites, **and "fundraising or campaigning on behalf of organisations."** BadCode fails on both the commercial *and* the campaigning ground. Sensitive-subject footage additionally requires submitting a full script before release | Quote-based; "fee… based on the rights, territories and duration required" |
| **BFI** | UK National Archive footage sales | **Live rate card, verified:** £840 + £14/sec single-country TV 5yr; £3,300 + £55/sec worldwide TV 10yr; **£8,580 + £143/sec worldwide all-media perpetuity**; £4,320 + £72/sec documentary rate. **No free tier exists anywhere on the card.** 🔴 BFI Player (streaming) is a different product from Archive Footage Sales |
| **Footage Farm** | ~25,000 reels of genuinely-PD US government material — but charges a **one-time buy-out fee** for research/mastering/delivery. Low licence risk, real cost | Quote-based, no price list. A ~£200/reel trade-press figure is **unconfirmed** |
| **CriticalPast** | 59,000+ clips 1890s–1990s, largely US government sources. "Royalty-free, worldwide, in perpetuity" — meaning **no further fee after a paid purchase** | ~$125/clip starting, ~$200 for a 2-min HD clip — **unconfirmed secondary source** |
| **Periscope Film** | Large military/aviation library. Posts previews to archive.org **under CC BY-NC-ND 4.0** — free to download, illegal for us to publish | Per-clip, quote-based |
| **Huntley Film Archives** | 80,000 titles of British social history 1895–1980s. Per-clip commercial licensing, no free tier | **Unverified** — browse/contact only |
| **Hearst Metrotone News** | 27M+ feet, 1914–1968, at UCLA / Packard Humanities. Rights-managed, **no PD dedication** comparable to Universal Newsreel's | **Unverified** |
| **March of Time** | Release library acquired by **HBO Archives**, licensed commercially. A narrow subset of outtakes in NARA/USHMM custody may be PD — easy to get wrong | **Unverified** |
| **NFB Canada** | 50,200+ shots from 13,000+ productions. Operates its archive as a paid stock business | Pricing calculator, **unverified** |
| **NFSA Australia** | Default is "All Rights, All Media, Worldwide, In Perpetuity" paid. Its **Zero Fee Licence** is scoped to *Australian independent documentary makers*, 3-minute cap, mandatory credit — not us | **Unverified** |
| **INA (France)** | Full French national broadcast archive. Preview streaming only; reuse sold through mediaclip | **Unverified** — search snippets only |
| **Artgrid** | Subscription-only cinematic stock, no free tier | ~$19.99–$49.92/mo tiers — **unconfirmed**, the pricing page is a JS shell |
| **Filmsupply** | Per-clip premium footage | **Live page, verified:** Internal from **$109/clip**, Web/Social from **$219/clip**, Extended Use quote-only |
| **Musicbed** | Music sync, sister brand (FM LLC) | ~$29.99 personal / ~$99.99 commercial per month — **unconfirmed**, JS shell |
| **Storyblocks** | 7M+ assets, subscription | **Live page, verified:** Essentials £16/mo, Unlimited £23/mo, Small Business £35/mo, all billed annually. 🔴 **The 7-day free trial page now returns HTTP 410 Gone** — the offer is withdrawn |

#### Embed-only news wires

| Source | The position |
| --- | --- |
| **AP Archive** | Publishes to YouTube under the **Standard YouTube License** specifically to retain ownership. Embed yes, download/re-edit no |
| **Reuters via ScreenOcean** | Its **free "Corporate Use" tier** exists but excludes distribution or display *"to the general public"* — scoped to internal/staff/invited audiences. Our releases are public, so even the free tier doesn't reach. **Unverified — search snippets only** |
| **Getty Images Embed** | 🔴 Not footage at all. An **iframe widget**: *"Embedded Getty Images Content may not be used: (a) for any commercial purpose… or (d) outside of the context of the Embedded Viewer."* No file is ever obtained, so **there is nothing to composite**. Getty may put ads in the viewer and may revoke any image at will. Easily mistaken for "free footage" by name alone |

#### Streaming showcases that read as open and are not

| Source | The position |
| --- | --- |
| **filmarkivet.se** (Swedish Film Institute) | ~2,000 Swedish archival films, free to stream. Own policy: downloading is not allowed "for copyright reasons." **Unverified — search snippets only** |
| **Stumfilm.dk** (Danish Film Institute) | Full Danish silent-film heritage 1903–1928, streaming showcase, no reuse licence found. **Unverified** |
| **RTVE (Spain)** | 🔴 **The clearest open-API-≠-open-licence case after CERN.** `curl 'https://api.rtve.es/api/programas.json'` works with no key and returns real JSON — and grants nothing. It is a catalogue API for their streaming platform; using clips is ordinary broadcast infringement |

#### Dead or absorbed

| Source | What happened |
| --- | --- |
| **Videvo** | `curl -I` → **HTTP 301 to freepik.com/videos**. The old three-tier system (Royalty-Free / Attribution / CC 3.0) **no longer governs anything.** Any blog post describing it is stale |
| **Mazwai** | Same **301 to freepik.com/videos**. The old CC-BY-3.0 claim cannot be verified against a live source |
| **Freepik** (their successor) | Real API, key-gated (verified 401). Free tier **requires attribution** and reportedly withholds full commercial rights. This is the commercial product, not free stock |
| **Life of Vids** | 🔴 Domain does not resolve — `curl` error 28, connection timed out after 10s. Not moved: **dead.** Survives only as a mirrored catalogue on Pixabay, inheriting **Pixabay's** licence, not an old CC0 claim |
| **EPA multimedia** | 🔴 A textbook "looks alive, isn't." `www.epa.gov/multimedia` → **404**. The only reachable content is a frozen Flash-era Region 2 stock-footage microsite whose listing page **loads convincingly, lists real clip names, and whose every download link 404s** (both `welsbach_bulldozing.zip` and `hudsonriver_dredging.zip` tested). A pipeline checking only "did the listing load" records a working source that is not |

#### Query surfaces we do not trust

| Source | The position |
| --- | --- |
| **archive.org `collection:feature_films`** | 28,415 items; **only 9,046 (32%) carry any `licenseurl` at all**. Popularity does not correlate with rights clarity — top-by-downloads results include titles with no licence claim. 🔴 Query-shape trap: without `mediatype:(movies)` the top hits are sub-collection *folders*, not films. **Uploader-asserted PD on Hollywood-era features is the single riskiest claim type on all of IA** |
| **archive.org `collection:computerchronicles`** | 634 items of 1980s/90s tech-history TV. A bare collection query surfaced `fr_cc192_smart_tv` at **`by-nc-nd/2.0`** alongside unlicensed items. Per-item-check-required, not a safe tier |
| **Smithsonian Open Access** | Real API, real CC0 — **for 2D/3D images and datasets.** For video it is a dead end: `q=online_media_type:Videos` and `q=object_type:"Videos"` both returned **rowCount 0** against live data. A naive `q=video` returns 5.25M hits that are library records *about* film. Don't mistake result count for footage |
| **Openverse** | 🔴 **Does not index video at all.** `/v1/videos/` → 404; the OpenAPI schema lists only `/v1/images/`, `/v1/audio/`, `/v1/thumbs/`. Video is a roadmap item, not shipped. Its frontend "External Sources" links are a UI convenience, not an API capability. **Listing it as a video source would be a factual error** |
| **Google Images usage-rights filter** | 🔴 Unscriptable — `tbs=sur:fmc` returns a **262-byte 302 stub** redirecting to a JS-rendered SPA. Google itself says it cannot guarantee the label's accuracy. And **there is no equivalent filter on Google Video** |
| **YouTube's Creative Commons filter** | 🔴 **The single most tempting shortcut a session will reach for, and it is red.** YouTube's `Filters ▸ Creative Commons` marks videos an *uploader* ticked CC-BY on — the same uploader-asserted problem as archive.org's `licenseurl`, with none of archive.org's provenance signals (no collection, no institutional account, no metadata trail), on a platform saturated with re-uploads. **A CC-BY tick by someone who did not shoot the footage grants nothing.** There is also no supported way to obtain the file: yt-dlp against YouTube is against its ToS, and "it was CC on YouTube" is not a defence anyone has ever won with. British Pathé's own position makes the point — 85,000 newsreels are on YouTube and **"downloading from YouTube does not launder the rights."** If a YouTube result is the only hit, go and find the same work at its institutional source, or invent it in Flow |
| **Bing Images usage-rights filter** | 🔴 **Caught mislabelling within the first query tested:** a search filtered to "free to share and use commercially" (`license-L2_L3_L4`) surfaced an **Alamy stock photo** — a paid rights-managed library. Also: the structured **Bing Search API was fully retired 11 Aug 2025**; keys decommissioned, no new signups, and the replacement ("Grounding with Bing Search") only feeds an LLM's context and returns nothing a script can filter. **Not a fallback** |

---

## Download mechanics

### The universal pattern

**search API → item/metadata endpoint → real file URL.** Every source wears the same shape in
different clothes — archive.org's `files[]`, Wikimedia's `videoinfo.url`, NASA's `collection.json`,
Pexels' `video_files[]`. **The middle step is skippable on almost none of them.**

🔴 **Never guess a filename.** Proven twice, independently:
- archive.org, invented-but-plausible `<id>_512kb.ogv` → **302 → 404**. And a bare `curl -I` on an
  archive.org URL **always** shows 302 regardless of whether the target exists — **you must
  `curl -L`** to see the real status.
- Wikimedia, wrong md5 hash-bucket → clean 404.

**There is no fixed ladder.** One Prelinger item carried all three derivative tiers; a NASA item had
only `.ogv` and **no mp4 at all**; one archive.org item mixes `<id>.mp4`, `<id>_512kb.mp4` and
`<id>_edit.mp4` — where the `_edit.mp4` is *bigger and better* than the plain `.mp4`. Fetch
`/metadata/<id>`, filter `files[]` for `source == "original"`, take the largest.

🔴 **The runnable version of all of this is
[The whole path, one block](#the-whole-path-one-block)** — query → metadata → largest original →
download → md5 → duration → conform → `premiere_import`, on one real identifier, verified live
2026-08-22. **Use that; this section explains why each step is there.** The three-line sketch below
is the shape, not a script — note that steps 2 and 3 must use the identifier step 1 returned, which
is exactly the mistake the earlier version of this page made:

```bash
ID=<the identifier step 1 actually returned>
# 1. search — always scoped to a trusted collection/identifier prefix
curl -s 'https://archive.org/advancedsearch.php?q=…&output=json'
# 2. metadata — the ONLY authoritative filename list (27 real filenames on one verified item)
curl -s "https://archive.org/metadata/$ID"
# 3. file — name taken from files[], never guessed; -L because a bare HEAD is always a 302
curl -L -o out.mp4 "https://archive.org/download/$ID/<name from files[]>"
```

The metadata record also carries per-file **md5 / sha1 / crc32 / width / height / length** — **it is
your pre-flight ffprobe.** No download needed to know resolution, duration and codec.

### Auth patterns — all four seen live

| Pattern | Sources | Test |
| --- | --- | --- |
| None | archive.org, Wikimedia Commons, images-api.nasa.gov, NASA SVS, LoC, CERN, RTVE | Real 200s |
| Key in query string, **enforced** | Pixabay, NPS, Smithsonian, DVIDS | Missing key → 400/401 |
| Key in query string, **optional rate booster** | general `api.nasa.gov` pattern (30/hr unregistered → 1000/hr registered) | 🔴 **Not** images-api.nasa.gov, which rejects `api_key` with a 400 |
| Key in an **Authorization header** | Pexels (bare key, **not** `Bearer`), Coverr (`api_key:` header), NARA (`x-api-key:`) | Missing → 401 |

🔴 **Cache-bust when probing auth.** See the Pexels entry — a "keyless 200" was an 11-day-old
Cloudflare cache hit. Append `?q=zzz_nonce_$(date +%s%N)`.

### Verifying what you got

**Content-Length is not enough.** A resume bug can produce a byte-count match on a corrupt file.

```bash
# ranged / resumable — verified 206 with correct Content-Range on archive.org
curl -sL -C - -o out.mp4 'URL'
curl -sL -r 0-4999999 -o part.mp4 'URL'
wget -c 'URL' -O out.mp4          # verified byte-exact against declared filesize
curl -sI 'URL'                    # size + content-type + accept-ranges, no download
```

**Then diff the hash** against the archive's declared md5 from the metadata step. Proven: a
deliberately truncated download produced md5 `92817432…` against a declared `d0a14394…` on a
39,706,987-byte file where only 1,982,014 bytes landed. **Both diverged correctly.**

🔴 **`ffprobe` exit code alone is not sufficient.** A deliberately truncated Ogg **conformed cleanly
through ffmpeg (exit 0, playable output)** despite `Broken file, keyframe not correctly marked` on
stderr — ffmpeg happily produced a short-but-valid file rather than failing loud. **Compare the
output's duration against the expected duration from the metadata record.** (30.9s of playable
footage was recovered from a file whose source is 555s.)

### Pre-flight without committing to a full download

Two techniques, **different guarantees, do not conflate them:**

**(A) Point ffprobe at the remote URL.** Works when the server advertises `accept-ranges: bytes`,
because ffmpeg's demuxers seek to the tail for the duration index.

```bash
ffprobe -v error -probesize 2000000 -analyzeduration 2000000 \
  -show_entries stream=codec_name,width,height,r_frame_rate \
  -show_entries format=duration,size -of default=noprint_wrappers=1 'URL'
```

Verified: correct **full** duration (555.49s) returned in ~10s of wall time on a link moving ~17KB/s
— nowhere near enough bytes to have fetched the 39MB file. Cross-confirmed on Wikimedia (486.147s,
640×480, 30000/1001, vp8/vorbis — exactly matching the API's own self-reported metadata).

**(B) Range-fetch a fragment locally, then probe it.** Gives accurate codec / resolution / pix_fmt /
fps immediately (theora/vorbis/400×300/29.97 from a 512KB fragment) — 🔴 **but the duration is only
the duration of what you saved.** Do not report it as the source duration.

**Best of all: use the archive's own metadata `length`/`duration` field.** Wikimedia and archive.org
both give it away free, no probing.

### Conforming an archive file to a Premiere timeline

Both run for real on a genuine Theora/Vorbis Ogg (400×300, 29.97) and verified with ffprobe on the
output:

```bash
# fast delivery / proxy
ffmpeg -i in.ogv -c:v libx264 -pix_fmt yuv420p -profile:v high -crf 18 -c:a aac -b:a 192k out.mp4

# editing-grade ProRes — avoids Premiere's background-transcode stall on import
ffmpeg -i in.ogv -c:v prores_ks -profile:v 3 -vendor apl0 -pix_fmt yuv422p10le -c:a pcm_s16le out.mov
```

**For the archive-specific traps:**

- **Deinterlace** with `-vf yadif=1` (or `bwdif=1` for sharper) **before** any scale or fps filter.
  🔴 **Check `field_order` in ffprobe first** — progressive vs `tt`/`bb`. Never deinterlace blind.
- **Frame rate.** `-vf "minterpolate=fps=25:mi_mode=mci"` preserves motion; plain `fps=25` just
  drops/duplicates and judders on anything moving. **Better: build the Premiere sequence at the
  source frame rate** and skip the conversion — mixed-rate timelines are what sequence settings are
  for.
- **Upscale SD** with `scale=1920:-2:flags=lanczos`. It will look like upscaled SD, because it is.
  Don't oversell it.
- **4:3 sources: don't force-pillarbox in ffmpeg.** Leave native aspect and let the Premiere
  sequence place it, so crop / pillarbox / scale-fill stays an edit-time choice, not baked in.

### Naming and disk layout

🔴 **Where the file actually goes — this used to be unstated, which made every other instruction on
this page unactionable.** Two homes, and they are deliberately different, because one of these
things is 950MB of MPEG-2 and the other is 4KB that has to survive forever.

**1. The bytes → under the Premiere media root.** `premiere_status()` returns `mediaRoot` (e.g.
`D:\badcode-videos`, which the bridge translates to `/mnt/d/badcode-videos` in WSL — it handles
`/mnt/d` ⇄ `D:\` both ways). Downloading anywhere else means Premiere cannot see the file and
`premiere_import` fails on a path that exists.

```
<mediaRoot>/footage/<source>/<identifier>/raw.<ext>
<mediaRoot>/footage/<source>/<identifier>/conform-<preset>.mov
<mediaRoot>/footage/<source>/<identifier>/source-metadata.json
```

Keep the archive identifier **verbatim** in the path — it is the only durable link back to the
metadata record and the licence claim. Keep raw and conformed as separate artifacts; never
overwrite. **The repo has never tracked a `.mp4` and must not start** (see `.gitignore`: a single
scene's takes are ~155MB and git keeps every byte forever).

**2. The receipt → in the repo, tracked, small.**

```
docs/footage/<source>--<identifier>.json    ← the API response verbatim
docs/footage/README.md                      ← the ledger: one row per sourced clip
```

**That JSON is the licence receipt.** Archives do take items down; uploaders delete accounts. If a
rights question ever comes up, it is what we have — and it is worthless on a drive that isn't
backed up, which is why it lives in git and the video does not. The ledger row carries: identifier,
source, tier, exact licence code, the credit line if one is owed, the Half B answers if it was
amber, and which piece it went into.

🔴 **Neither directory exists yet.** The first session to source a clip creates them and writes the
ledger's header. Don't skip it and don't invent a different layout.

#### 🔴 The credit surface — an open question, and it is why CC-BY is amber

Green used to include *"CC-BY where we will actually carry the credit."* **There is nowhere to carry
a credit.** `@badcode/comic` has no credits surface, there is no end-card convention, the shorts
have no tail slate, and no comic page has ever displayed an attribution line. Every other BadCode
artifact has a home; this one has never been designed.

Until Kai rules on where a credit goes, **every attribution-requiring source on this page is amber**
— ESO, Commons' CC-BY/BY-SA majority, Europeana's CC-BY records, OGL/OPL material, CERN. The
candidates worth ruling between are: a credits page on the site; a per-comic end card; a
`## Credits` block in the story canon that renders; or a tail slate on video. **Ask, don't
improvise** — a credit we invent and then quietly drop is worse than not using the clip.

### Politeness

No source in the research sweep showed rate-limit friction, but nothing was probed at volume either.
Published limits: archive.org documents 429 with an `X-Accept-Reduced-Priority` opt-in; Pexels 200/hr
and 20,000/month; Pixabay 100 per 60s; NARA 10,000/month per key; Europeana's `api2demo` is shared
and throttled; api.data.gov's `DEMO_KEY` is shared **across every tool on the internet** and will
rate-limit against strangers.

**House rule:** single-threaded sequential fetches, 1–2s between search/metadata calls, **no parallel
download workers against one host**, and treat 429/503 as *stop for a few minutes*, not *retry now*.
🔴 web.archive.org specifically throttles to roughly one request per 10–15s — back off, don't hammer.

---

## What we deliberately don't use

| Not used | Why | The free route we take instead |
| --- | --- | --- |
| **British Pathé, IWM, BFI** (UK archival) | Paid per-second; IWM's only free tier bans campaigning use **by name** | **US federal compilations of the same events** on archive.org (`gov.archives.arc.*`, War Dept bulletins, Capra's *Why We Fight*) — accept it won't carry a British uniform |
| **AP, Reuters/ITN, Getty Embed** (news wires) | Embed-only or internal-audience-only; nothing extractable | Wikimedia Commons for PD news film; Flow for anything that only needs to *look* like news |
| **Footage Farm, CriticalPast, Periscope Film** (PD resellers) | They sell research and delivery on top of genuinely-PD material | **Go to the underlying source.** All three draw largely on NARA / LoC — which are free |
| **Storyblocks, Artgrid, Filmsupply, Shutterstock bulk, Adobe Stock paid** (subscription/per-clip) | Paid, no usable free tier | 🟡 **Adobe Stock Free** (1.1M+, free Adobe ID — but its terms bar implied political endorsement, so it is amber, not "commercial-cleared"), Pexels/Pixabay/Coverr within their clauses. For anything pointed, **Flow is the cleaner answer than any stock house** |
| **Freepik / Videvo / Mazwai** | Consolidated into a plan-gated product; free tier needs attribution and reportedly withholds commercial rights | Pexels or Coverr |
| **Musicbed** (music) | ~$99.99/mo for the tier we'd need | **Suno** — see the `suno-prompt` skill. We make our own music |
| **YouTube's Creative Commons filter** | Uploader-asserted, no provenance trail, no supported way to get the file — and "downloading from YouTube does not launder the rights" | The same work at its institutional source (`gov.archives.arc.*`, Commons, LoC), or Flow |
| **Google / Bing "usage rights" filters** | One unscriptable, the other caught mislabelling paid Alamy stock as free-to-use-commercially in the first query tested | **Wikimedia Commons `extmetadata`** — structured, per-file, enforced at upload |
| **Openverse** | Indexes images and audio only; no video | Wikimedia Commons + Europeana `reusability=open` |
| **Anything CC-BY-NC / BY-ND** | We sell music. NC is judged at the entity level | Find the same subject in a §105 federal source, or invent it in Flow |
| **Paid footage of a thing that never happened** | It's a rendering job, not an archive job | **Flow.** Sourcing is for footage whose *being real* is the point |

---

## Verification status

🔴 **This table is load-bearing. A future session must know what to trust.** "Verified live" means
someone actually made the call in the research sweep and read the response.

### Verified live — trust these

| Claim | How it was proven |
| --- | --- |
| archive.org query syntax (`fl[]`, `sort[]`, `rows=0`, wildcards, ranges, pagination) | 15+ distinct calls, all HTTP 200; `page=2&rows=3` → `start=3` |
| Collection counts **as of 2026-08-22**: Prelinger 10,459 / 1,913 with licence; **FedFlix 2,107 / 2,106 with licence**; nasa 13,733; feature_films 28,415 / 9,046; computerchronicles 634; universal_newsreels 611; `youtube-*` 2,059,500 | `rows=0` count queries. 🔴 **FedFlix was written here as 2,218 and had drifted to 2,107 — date-stamp every count** |
| `collection:NASAarchive` returns **zero** | Live query |
| Universal Newsreel has **no** May–July 1940 item | Live date-range query, `numFound: 0` |
| The Dunkirk items are real files (FB-56, Dividean1943_2, gov.dod.dimoc.30172) | Full `/metadata/` fetch + range GET → HTTP 206 + `file` confirmed genuine ISO Media MP4. 🔴 **"All three are green" was the claim and it was wrong — see the 2026-08-22 corrections below** |
| Periscope Film's archive.org previews are **CC BY-NC-ND 4.0** | `licenseurl` read from raw JSON |
| archive.org guessed-filename → 302→404; real file → 302→200 with exact byte match | `curl -sIL` |
| Resume/integrity: 206 + Content-Range; truncated file's md5 ≠ declared md5 | Executed end to end |
| `ffprobe` on a remote URL returns correct **full** duration via range-seeking | 555.49s in ~10s on a ~17KB/s link |
| Both ffmpeg conform commands (H.264 and ProRes) | Exit 0, output ffprobed |
| images-api.nasa.gov keyless; **rejects `api_key` with 400** | Live comparison |
| NASA SVS: `count: 10556` for glacier; direct mp4 at 407,598,044 B | Live |
| NASA filename ladder is tilde-suffixed; literal spaces in URLs | Live 200s and 403s |
| Wikimedia: `extmetadata` licences, direct URL at 1,689,032,627 B, md5-bucket path rule, wrong bucket → 404 | Live, md5 computed by hand |
| LoC: item 2015600171 mp4 at 366,773,204 B, **byte-exact** to metadata; item 91482338 → `resources: []` | Live |
| NPS: `total: 10634`, direct 360p mp4 at 98,682,801 B | Live with DEMO_KEY |
| Europeana facets (12,972/42,419/333,760, sums exactly); UK+open = 247; `qf=REUSABILITY:open` silently returns 0 | 12+ live calls |
| Europeana `edmIsShownBy` = a **vimeo.com** link on a CC-cleared item | Full EDM record fetched (49,904 B) |
| Open Beelden: Atom feed + direct mp4 at 11,877,942 B, `Content-Disposition: attachment` | Live |
| CERN: FOOTAGE facet = 36; file at 478,006,191 B, no auth; licence string is `"CERN"` | Live API + copyright.web.cern.ch fetched |
| ESO CC BY 4.0 (exact wording); mp4 at 983,696,048 B | Live copyright page + CDN HEAD |
| ESA: "86 Results" on the CC filter page; site-wide-default vs CC-BY-SA-IGO split | Live filter page + Copyright_Notice_Images fetched |
| NOAA's own images-PD / **videos-exception** wording | Read verbatim off the photo-library page |
| NOAA Ocean Exploration has no API (basket + async email) | Its own help page fetched |
| Pexels: **stale-cache 200**, then cache-busted **401**; CDN file at 14,157,772 B | Live, both legs |
| Pixabay missing key → 400; Coverr missing key → 401; Freepik missing key → 401; DDB missing key → 403; DVIDS bad key → 200 + JSON error; NARA no key → **200 with HTML** | Live auth probes |
| Smithsonian: `Videos` queries → rowCount 0; DEMO_KEY hit `OVER_RATE_LIMIT` | Live |
| Openverse `/v1/videos/` → 404; schema lists no video path | Live + 114KB OpenAPI doc grepped |
| Google `tbs=sur:fmc` → 262-byte 302 stub | Live |
| Bing "free commercially" filter → **Alamy** result | Live, parsed from the result page |
| Videvo → 301 freepik; Mazwai → 301 freepik; lifeofvids.com → **connection timeout** | `curl -I` |
| EPA: `/multimedia` 404; archived listing loads; **both zip links 404** | Live |
| USGS: 403 and **202-empty with `x-amzn-waf-action: challenge`** | Live, two agents independently |
| BFI rate card (all figures) | Live page fetched |
| Filmsupply $109 / $219 / quote | Live page fetched |
| Storyblocks £16/£23/£35 and the trial page → **HTTP 410 Gone** | Live page fetched |
| IWM's non-commercial licence exclusions + Delegated Authority | Both IWM policy pages fetched |
| Getty Embed terms (verbatim) | gettyimages.co.uk/company/terms fetched |
| Legal: 17 USC §105; CDPA ss.13B/77/87/163; CC0 and CC-BY-NC legalcode; EU Database Directive Arts.7/10; **Bridgeman v. Corel**; IA's own rights page | Direct primary-source fetches, all 200 |

### Re-verified and corrected — 2026-08-22 critic pass

🔴 **These are the claims that failed on re-run.** Every one had been stated on this page as fact.

| Claim as it stood | What the live re-run returned | What changed |
| --- | --- | --- |
| FedFlix = **2,218** items | `numFound: 2107` (2,106 with `licenseurl`) | Count corrected + date-stamped; rule added to date-stamp all counts |
| `FB-56` is **green**, "US federal work" | `uploader: jilly@poetryhut.com`, `collection: [wwIIarchive, folkscanomy_history, folkscanomy]`, `licenseurl` = uploader-asserted **PDM**, `rights: None`, `source: None` | **Demoted to amber.** It failed this page's own Half A check. Curing procedure added |
| `gov.dod.dimoc.*` is **"DoD's own institutional account"** | `uploader: carl@media.org`, `collection: [FedFlix, usgovfilms, newsandpublicaffairs]` | **Claim corrected.** Still green — but on the FedFlix basis, not an agency-account basis |
| **Wikimedia Commons** is green; the demo query is the proof | Same query, 8 results: **6 × CC BY-SA**, 1 × CC BY, 1 × CC0 — and **zero WWII footage** (handball, four cycling stages, a beach drone shot, a Spitfire experience) | **Green scoped to the CC0/PDM subset only**; `LicenseShortName` check made mandatory; place-name-vs-event trap documented |
| **C-SPAN** floor coverage "may be used without restriction or attribution" *(proposed as a new green source)* | c-span.org/about/copyrightsAndLicensing fetched live: *"C-SPAN does **NOT** permit unlicensed commercial use of any of its audio or video programming (including coverage of federal government events)"* | **Filed amber, not green.** The quoted "without restriction" line does not appear on the live page — **do not quote it** |
| **Adobe Stock Free** = "the only genuine free, commercial-safe find" | Adobe Stock Additional Terms §3.1(E) prohibits *"implied or stated endorsements of political parties or other opinion-based movements"* | **Demoted to amber.** Framing deleted; 500,000-reproduction cap noted |
| **ESO**: "only a visible, unaltered credit is required" | eso.org/public/copyright: no commercial use of images with **identifiable people**; no implied ESO endorsement; **music is outside the CC BY grant** | **Demoted to amber**, all three clauses quoted |
| **NPS**: third-party credit is a spot-check | 30 records pulled: **24 carry a named non-NPS credit** | **Demoted to amber.** 80% is not a spot-check |
| **DVIDS / NARA v2 / Adobe** are green | **No authenticated call has ever been made to any of the three** | **All demoted.** Green now means *verified by us* |
| The page is discoverable | `grep -rn "footage-sources" --include=*.md` returned **only this file** | `docs/video-fx/README.md`, `CLAUDE.md` and the `find-footage` skill now link here |
| **OGL v3** was never surveyed | nationalarchives.gov.uk fetched verbatim: *"exploit the Information commercially"*, attribution-only, exemption list read | New amber entry; UK Known-gaps conclusion softened |
| The end-to-end command block | Steps 1–3 + the metadata/duration steps of [The whole path](#the-whole-path-one-block) **executed live on `gov.dod.dimoc.30172`** — search returned the item, `jq` picked `gov.dod.dimoc.30172.mpeg` (949,987,612 B, md5 `114bfc74…`), declared length 1732.73s | Replaced the old block, which did not chain: its step 1 was elided and its steps 2–3 hardcoded an unrelated identifier |

⚠️ **Read but not re-verified in this pass:** the Open Parliament Licence wording and
parliamentlive.tv's Downloading & Sharing terms. **parliament.uk returned a Cloudflare JS challenge
and parliamentlive.tv's `/Guidance`, `/Help` and `/Home/Copyright` all 404'd**, both on 2026-08-22.
The OPL entry says so in place.

### Read but not verified — treat with care

| Claim | Status |
| --- | --- |
| **NARA API v2** record schema, digital-object field names, video filter | ⚠️ **No key obtained.** Endpoint reachable; the schema is from NARA's README. Flag this gap to whoever requests the key |
| **DVIDS** `files[]` / `hls_url` / caption shape, and whether keys are origin-locked | ⚠️ **No key obtained.** Auth-failure shape confirmed; no success response ever seen. **Origin-locking may break server-side use from WSL** |
| **DDB** everything beyond the 403 | ⚠️ Key requirement confirmed; auth header format, record shape and video coverage all unverified |
| **Pexels / Pixabay / Coverr / Freepik** authenticated response shapes and resolutions | ⚠️ No accounts created. Endpoints proven live via documented error shapes; JSON shapes are from vendor docs |
| **Adobe Stock Free** | 🟡 Page copy verified via a **web.archive.org snapshot** (stock.adobe.com 403s) + an Adobe Community answer. The **Adobe Stock API path is untested.** The Additional Terms §3.1 clauses were decoded from Adobe's own PDF — those *are* verbatim |
| **Shutterstock free tier** (~3 photos, ~40 videos, ended-trial date) | ⚠️ Via a **secondary source** (photutorial.com); shutterstock.com 403s |
| **Pond5** counts and disclaimer | 🟡 Via **web.archive.org snapshots** (pond5.com 403s) — the snapshots themselves returned 200 and the text was read verbatim |
| **CriticalPast** FAQ | 🟡 Fetched by declaring a **Googlebot UA** (a normal browser UA 403'd). The **$125 price is a secondary source, unconfirmed** |
| **British Pathé** copyright claim | ⚠️ britishpathe.com **403s / Cloudflare-challenges** direct fetch. The quote *"retains the copyright to its entire collection, none of which is in the public domain"* is **search-snippet-sourced**. 🔴 **Worth a retry with a browser before quoting verbatim in public BadCode copy** |
| **Reuters/ScreenOcean** licence-tier wording | ⚠️ Search snippets only, never fetched |
| **INA, filmarkivet.se, stumfilm.dk, Huntley, Hearst, March of Time, NFB, NFSA** | ⚠️ Search snippets only. Flagged red as a **caution**, not from a verified rate card |
| **Artgrid, Musicbed** prices | ⚠️ Both pricing pages are **JS shells**; figures from 2026-dated secondary sources. **Unconfirmed** |
| **Footage Farm** ~£200/reel | ⚠️ Trade press. The **buy-out model itself** is verified from their own FAQ |
| **USGS** PD-by-policy wording | ⚠️ Never read off usgs.gov — WAF-blocked. From a search summary |
| **PD movie aggregators** | ⚠️ Never fetched at all |
| **CDPA Schedule 1** pre-1957 film mechanics | ⚠️ National Archives page **404'd**; the "Crown copyright in pre-1-June-1957 material has universally expired" line is a **search-engine snippet of NARA's own text**. The statutory sections (13B, 163, 77, 87) *were* fetched directly |
| **Antiquesportfolio.com v Rodney Fitch** (UK new-copyright-in-a-skilled-reproduction) | ⚠️ Confirmed via **multiple converging legal summaries**, not a primary case report |
| **Stock EULA "editorial only" clause wording** | ⚠️ A well-established **pattern description**, not a verbatim quote from a specific EULA. Read the actual EULA per clip |
| **US right-of-publicity** state exemptions | ⚠️ Secondary summaries. Jurisdiction-specific follow-up needed before relying on it |
| **archive.org rate limits** | ⚠️ From IA's docs; deliberately **not load-tested** |

### Where the agents disagreed — unresolved

| Question | The disagreement | Where it stands |
| --- | --- | --- |
| **USGS colour** | One agent: **red** ("operationally unreachable, assert nothing"). Another: **amber** ("licence basis is solid, it's a fetch problem"). Both agree on the WAF block | **Filed amber**, flagged here. Needs a browser session |
| **NASA mp4 ladder** | One verified `~medium.mp4` 200 while `~large`/`~orig` **403'd**; another verified `~large.mp4` 200 on a different item | **Not a contradiction — per-item variance.** The manifest is the authority; never generalise the ladder |
| **Coverr rate limits** | Docs say **1000 calls/month** (staging); another source says **50/hour**. Production quoted as both "2,000/hour" and "500/min" | **Unresolved.** Check your own dashboard |
| **`ia download`** | One agent hit read-timeouts (12s default) and recommended curl; another used `ia metadata` without trouble | **House answer: `ia` for search/metadata, curl for bytes** |
| **British Pathé pricing shape** | One brief: per-second with a 60s minimum. Another: ~$2,500+/min for perpetual worldwide online | **Both unconfirmed** (no live page fetched). Quote neither as a number |

### Known gaps — nobody covered these

🔴 **Read this before you promise anyone a subject.** The green tier is deep on space and US
federal film and shallow-to-empty on most of what BadCode's stories are actually about.

**Subjects with no source and no query run — the ones that matter most:**

- **Protest, strikes, picket lines, labour organising, crowds.** **Zero sources, zero search
  recipes, in a survey written for a collective whose subject is the ownership of the means of
  production.** Prelinger and Commons both hold this material and neither entry points at it.
  Leads: Prelinger sponsored/newsreel film, `collection:universal_newsreels`, Commons
  `Category:Demonstrations` / `Category:Strikes`, and — for named speakers — the UK OGL/OPL route.
  **This is the highest-value hour anyone can spend on this page.**
- **Financial markets, trading floors, banks, budgets, economic policy.** Zero. **The Magic Money
  Tree and Emperor's New Coin both need it.** Leads: Prelinger's sponsored finance and insurance
  films, newsreel crash/budget coverage, C-SPAN 🟡 for hearings.
- **Heavy industry, manufacturing, mining, energy, ports, automation.** The only real factory-floor
  or machinery material found is **CERN's 36-item FOOTAGE facet** (amber licence) and the **dead**
  EPA Region 2 clips. Everything else in the science territory skews space and earth-science.
  **NREL timed out, USACE was Akamai-blocked, USBR's `/multimedia/` 404'd.**

**Territories only partially opened:**

- **UK.** 🔴 **Corrected 2026-08-22 — the old conclusion here was over-broad.** It read "UK-specific
  archival footage that is both free and clear: there is essentially none." The accurate statement
  is: **UK archival *film* is a paid line item** (Pathé, IWM, BFI, Huntley — all correctly red, and
  IWM's only free tier bans campaigning use by name), **but UK *government and parliamentary*
  footage has an open-licence route that has never been tested** — OGL v3 and OPL v3 both permit
  commercial exploitation with attribution. See [Open licences (UK)](#open-licences-uk--ogl-v3-and-opl-v3).
  Whether either reaches moving-image material is the open question, and it is answerable in an
  afternoon.
- **Archival TV news, 1960s–2000s.** The gap between `universal_newsreels` (stops 1967) and the paid
  wires. **American Archive of Public Broadcasting** is now listed 🟡 — but it is a finding aid with
  user-borne rights assessment and US-IP restrictions, not a source of publishable files.
- **Non-US, non-European regions.** Nothing at all on **Canada** beyond the paid NFB (Library and
  Archives Canada is unlisted and unexamined), **Australia** beyond NFSA, **Ireland**, and the whole
  of **Asia, Latin America and Africa**. "Europe-specific? Europeana" is the only non-US route this
  page offers.
- **Stills.** Now named as a strategy in [step 8](#find-footage-of-a-historical-event--start-here),
  but no stills source has been surveyed to the depth the video sources have. LoC, NARA, Commons and
  Smithsonian Open Access (real CC0, images only) are all orders of magnitude richer for stills than
  for footage, and a push-in on a PD photograph is usually cheaper than the hunt for a clip.

**Verification gaps:**

- **No authenticated call has ever been made** to NARA v2, DVIDS or DDB. All three are amber for
  exactly that reason.
- **No chamber-original congressional feed has been located or pulled** — the C-SPAN entry's
  recommended route is untested.

---

## The procedure

Same shape as the README's. **The step-by-step operating version is the
[`find-footage`](../../.claude/skills/find-footage/SKILL.md) skill** — this is the reference behind
it.

1. **Check this page first.** The green tier answers most requests, and the red tier saves you the
   hour you were about to spend on British Pathé.
2. **Run the clearance check** — Half A before anything is downloaded, Half B before anything is
   cut, and **never let amber ship without Half B answered out loud.**
3. **Save the metadata JSON as the receipt** — `docs/footage/<source>--<identifier>.json`, tracked,
   plus a ledger row. The bytes go under `mediaRoot`. See
   [Naming and disk layout](#naming-and-disk-layout).
4. **When you find something new, write it back here** — dated, with the exact command and what the
   response actually was, so the next session doesn't pay again.
5. **Mark what you verified and what you only read.** The verification table above is only worth
   anything if it stays honest.
6. **Never end at "licence it."** State the free route — a §105 equivalent, Commons, or Flow. If
   there genuinely isn't one, say so plainly and let Kai decide.

**On prices:** a price without a live vendor page is quoted as *unconfirmed*, never as a number.
Four figures on this page are live-verified (BFI, Filmsupply, Storyblocks, and Adobe's free-tier
copy). Everything else in the red table is unconfirmed and marked as such.

---

## Status

🟡 **Written 2026-08-22 from a multi-agent research sweep, and revised the same day after a critic
pass re-ran every command and licence claim live.**

**68 sources as of 2026-08-22: 7 green, 27 amber, 34 red.** 🔴 **The green tier went from 12 to 7
in that revision** — see [Re-verified and corrected](#re-verified-and-corrected--2026-08-22-critic-pass)
for exactly which claims failed and why. The counts and the tiers are stated *as of a date* on
purpose; both move. *(The previously advertised total, "61 sources: 12 green, 18 amber, 31 red",
was itself a miscount — the red table has always held 33 rows. Counts here are now taken by
counting table rows, not by memory.)*

**The failures clustered in licence interpretation, not in mechanics.** The download, verify and
conform layer was re-run against the sources and came back exact — byte counts, md5s, HTTP codes,
facet totals — and [the end-to-end runbook](#the-whole-path-one-block) had its search, metadata,
file-selection and duration legs executed live on `gov.dod.dimoc.30172`. **The ffmpeg conform
commands were not re-executed in this pass**; they were verified in the original sweep and are
unchanged. What did not survive was the optimism: three green sources had never been called at all, two carried clauses aimed directly at
political publishing, and the flagship worked example failed this page's own provenance check.

**The operating procedure is the [`find-footage`](../../.claude/skills/find-footage/SKILL.md)
skill.** Come here for the reference; use `premiere-automation` for the edit and `flow-prompt` for
anything that has to be invented instead.

Lane choice between Flow, ffmpeg, Premiere and sourcing: [`README.md`](./README.md).
