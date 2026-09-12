---
id: magic-money-tree
title: "Footage ledger — The Future He Never Saw"
status: in-progress
updated: 2026-09-12
pass: 1 — war family verified; UK / NHS / austerity families still open
---

# Footage ledger — *The Magic Money Tree: The Future He Never Saw*

**What this file is.** One row per beat in [`storyboard.md`](./storyboard.md) that shows something
that really happened, with the source we may publish it from, the licence **as verified in a
session** (not as asserted by an uploader), the file on disk, and the fallback when nothing free
exists. It is the sourcing half of the film. It does not choose shots and it does not write prompts.

**It supersedes nothing.** The [2026-09-11 investigation's rights ledger](./research/documentary-austerity-emergency-investigation-2026-09-11.md#footage-and-rights-ledger)
still holds for documents, charts and the modern-politics beats. This file re-runs its *archive
footage candidates* against the live archive and records what actually answered.

**How to read a tier** (house rule, from [`docs/video-fx/footage-sources.md`](../../video-fx/footage-sources.md)):

| Tier | Means |
| --- | --- |
| 🟢 Green | US federal work, an institutional PD dedication, CC0, **or an attribution-only licence whose credit we record** — and someone opened the licence in a session and said so |
| 🟡 Amber | Usable only after a **per-item human check**. Inferred licence, uploader-asserted PD, a **ShareAlike** obligation, or a host charging for its own print |
| 🔴 Red | Paid house, non-commercial licence, live copyright, or a clause that bars political use |

**Two rulings from Kai, 2026-09-12, that set the shape of this film's sourcing.**

✅ **1. Credits go in the video.** *"If we need to add a credit into the video in order to then use
footage, of course — where we can put that is in various places in the video, because we very
happily put credits in."* This **unblocks the Open Government Licence**, and with it scenes 06, 09,
10 and 12 — the NHS leaflet, the 1944 White Paper, the 1948 pamphlet. The obligation it creates:
record each licence's **exact** credit string here, and never ship the clip without it.

💷 **2. There is a budget: £100 for the whole film, £200 at an absolute push.** *"I'd rather not
if we can get away with it… we have to be very very price sensitive."* Not per clip.
🔴 **It does not reach the UK archive houses** — BFI's cheapest tier is £840 + £14/sec before a
second is counted, and Pathé, IWM and BBC Motion Gallery are all quote-based at broadcast scale. So
the plan below does not change: free sources first, a **per-image still licence** as the one
category that fits, and every spend a stop gate that waits for Kai.

🔴 **And the rule that did not change: "royalty-free" is a pricing model, not a permission.**
Stock EULAs routinely bar political use. This film is political argument end to end — so paying a
stock house can leave us *less* free to publish than a PD reel we got for nothing.

---

## 1. The beat inventory — which scenes need real footage, and from where

Fourteen scenes. Six need genuine actuality, four need a real *document* or a real *photograph*,
four need nothing real at all and belong to Flow.

| # | Scene | What really happened in it | Needs | Source family |
| --- | --- | --- | --- | --- |
| 01 | Get them off the beach | Operation Dynamo, Dunkirk, 26 May – 4 Jun 1940 | **Actuality** | 🇺🇸 **US federal film** — War Department compilations of European events |
| 02 | Home to what? | The coming peace; bomb damage; the debt figure; Keynes introduced | Actuality + a still + a figure card | US federal film · Commons stills 🟡 · OBR figure (typeset) |
| 03 | The unemployed builder and the unbuilt house | **Nothing.** An explicitly labelled illustration | Invented | **Flow** — the storyboard says it must stay recognisable as an example |
| 04 | The word "actually" | Bricks, training, capacity; the 1942 Keynes quotation | Generic industry + a text card | Prelinger industrials 🟡 · **Flow** · typography |
| 05 | Britain did pay for the war | Rationing, war production, taxation, savings, convoys, Lend-Lease | **Actuality** | 🇺🇸 **US federal film** (a US film *about* Britain) + TNA documents |
| 06 | A job after the uniform | 1944 Employment Policy White Paper; Bevin presenting it 21 Jun 1944; Beveridge | A document + a still | 🇬🇧 **UK Crown / Hansard** — 🔴 **no free moving image exists** |
| 07 | Victory does not come with a roof | VE Day in Britain; the 1945 election; Keynes on the American loan in the Lords | **Actuality (British)** + a still | 🔴 **Open** — see §3. US VE-Day film is American and must not stand in |
| 08 | 21 April 1946 | Keynes's death | **One still, held** | Commons / library PD portrait 🟡 |
| 09 | The promise gets a working day | The NHS opens, 5 Jul 1948; the launch leaflet | A document + stills | 🇬🇧 **TNA, OGL** (leaflet `INF 2/66`) — ✅ **unblocked by the credits ruling**; 🔴 still no free moving image |
| 10 | The key in the door | Post-war council building into the 1950s | Actuality or stills | 🇬🇧 **Open** — Commons stills 🟡; no free film found yet |
| 11 | The promise requires another shift | June 2010 Budget; nurses on *Question Time*, 2 Jun 2017 | Broadcast + Parliament AV | 🔴 **Red both ways.** BBC owns the programme; Parliament's AV terms bar our use. → subtitle cards + a silent timeline |
| 12 | They knew about the magic | The September 1948 NHS pamphlet, TNA `MH 55/965` | A document | 🇬🇧 **TNA, OGL** — ✅ **unblocked by the credits ruling** |
| 13 | What is actually missing? | Nothing specific — present-day hospital, training, building | Invented / generic | **Flow** |
| 14 | A life to get back to | Nothing specific — an ordinary act of care | Invented | **Flow** (the storyboard forbids a falsely identified real patient) |

**Reading of that table.** Only scenes 01, 02, 05 and 07 want war actuality, and only 01, 02 and 05
can get it free. Everything British and post-war is **documents and photographs, not film** — which
is not a defeat, because a slow push-in on a 5,000-pixel photograph cut on the beat reads as archive
and costs nothing.

---

## 2. The war family — verified 2026-09-12

Every row below was checked in this session with `curl -s https://archive.org/metadata/<id>` and, for
the dead ones, `curl -sL -o /dev/null -w '%{http_code}' https://archive.org/details/<id>`.

### 2a. 🟢 Green — trusted prefix, trusted operator, explicit PD or CC0

All of these are **FedFlix** items: uploader `carl@media.org` (Public.Resource.Org, the FedFlix
operator), collections `FedFlix, usgovfilms, newsandpublicaffairs`. The underlying films are US War
Department / US government works — 17 USC §105, no copyright — and the item carries an explicit
public-domain `licenseurl`. That is the green criterion, met and checked.

| Beat | Identifier | Title | Licence URL (verbatim) | Original file | Bytes | Duration | md5 (declared) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **01 Dunkirk** ⭐ | `gov.fdr.25.4` | *Divide and Conquer* (Part 4) | `publicdomain/zero/1.0/` | `gov.fdr.25.4.mpeg` | 369,576,027 | 809.01 s | `95f87bb33a241c239e10b59b5415eb75` |
| 01 context | `gov.fdr.25.2` | *Divide and Conquer* (Part 2) | `publicdomain/zero/1.0/` | `gov.fdr.25.2.mpeg` | 360,530,997 | 789.32 s | `9f32c3995274923dc55159f91d1270f3` |
| 01 context | `gov.fdr.25.3` | *Divide and Conquer* (Part 3) | `publicdomain/zero/1.0/` | `gov.fdr.25.3.mpeg` | 606,947,871 | 918.66 s | `690de18d33b8337487d789632cbd40d2` |
| 01 / 02 | `gov.archives.arc.65841` | *The Battle for the Beaches* (342-USAF-19152) | `licenses/publicdomain/` | `gov.archives.arc.65841.mpeg` | 1,046,524,402 | 1286.63 s | `d9ff99d56f596dfd71f3d9ba5aea752b` |
| 02 Blitz | `gov.archives.arc.36070` | *The Battle of Britain* (Capra, Why We Fight #4) | `publicdomain/zero/1.0/` | `gov.archives.arc.36070.mpeg` | 2,598,037,291 | 3194.27 s | `4d57ed3c43241fe5d22aa0ea603e013e` |
| **05 home front** ⭐ | `gov.ntis.ava06858vnb1` | *Know Your Ally: Britain* (1943) | `licenses/publicdomain/` | `ava06858vnb1.mpeg` | 1,540,064,187 | 2525.56 s | `37fe8905ad76f2bacf57ce4e9e09246b` |
| (context only) | `gov.archives.arc.38936` | *The War Ends in Europe* (United News) | `publicdomain/zero/1.0/` | `gov.archives.arc.38936.mpeg` | 228,617,773 | 281.14 s | `10d8b9916e434a5fffae91de0b083dad` |
| (context only) | `gov.fdr.44` | *Why We Fight: Prelude to War* | `publicdomain/zero/1.0/` | — | — | — | — |
| (context only) | `gov.archives.arc.36068` | *The Nazis Strike* | `publicdomain/zero/1.0/` | — | — | — | — |
| (Bretton Woods) | `gov.archives.arc.39018` | *Last Liberty Ship Launched [etc.]* — **Part 3 is Morgenthau opening the UN Monetary Conference at Bretton Woods** | `publicdomain/zero/1.0/` | — | — | — | — |

The same four *Divide and Conquer* reels also exist on **Prelinger** as `Dividean1943_2/_3/_4`
(`licenses/publicdomain/`, no uploader field). Same film, same licence basis, worse provenance
signal — prefer the `gov.fdr.*` copies.

### 2b. The Dunkirk shot actually exists, and here is where it is

`gov.fdr.25.4` downloaded, md5 matched the declared value, and its frames were scrubbed at 8-second
intervals across 3:40–6:50. **The evacuation block runs ≈ 03:56 – 05:20 (about 84 seconds).**

| Time | What is on screen |
| --- | --- |
| 3:40–3:50 | Animated map, "DUNKIRK" legible top-left |
| 3:56 | Dive-bomber over a burning shoreline |
| 4:04 | Destroyers under way, line astern |
| 4:12 | A single exhausted soldier, balaclava, in profile |
| 4:36 | Burning wreckage along a shore |
| 4:44 | Troops packed on a deck, boarding from the water |
| **4:52** | **A small vessel seen from above, completely filled with troops** |
| **5:00** | **British troops in Brodie helmets crowded on deck, faces to camera** |
| 5:08–5:20 | More crowded decks; troops disembarking among civilians |

Scene 01 has a 35-second allowance. 4:44–5:20 alone is 36 seconds of it.

🔴 **The one caveat that matters, and it is the storyboard's own rule.** Scene 01 says: *"No scenes
from a feature film passed off as actuality."* *Divide and Conquer* is a Frank Capra **compilation** —
the War Department assembled it from newsreel, captured enemy film and, in places, dramatised
material. The item is unambiguously free to publish; what is **not** established is that any given
shot inside it is actuality rather than a staged or feature-film insert. **Before a shot is cut in,
a human must look at it and decide.** That check is not automatable and has not been done.

### 2c. ⛔ Seven candidate identifiers from the prior sweep are **dead**, and the search index still lists them

This is the finding with the widest blast radius. `https://archive.org/metadata/<id>` returns
`{}` with **HTTP 200**, and `/details/<id>` returns **404 "Item cannot be found"** — while
`advancedsearch.php` still returns the identifier as a hit.

| Dead identifier | What it was supposed to be | Where it came from |
| --- | --- | --- |
| `gov.dod.dimoc.30172` | *Army in Action, Ep. III: Flames on the Horizon* | 🔴 **the flagship green example and the only end-to-end code block in `footage-sources.md`** |
| `111-of-16-r1-5` | *Know Your Ally: Britain* | prior MMT sweep |
| `gov.archives.arc.36080` | *Know Your Ally: Britain* (the other copy) | this session's own search |
| `gov.archives.arc.39190` | *War Pictorial News No. 133* (Churchill on camera) | prior MMT sweep |
| `111-adc-4267` | VE Day / Piccadilly | prior MMT sweep |
| `gov.archives.arc.39139` | *Return to Dunkirk* | this session's own search |
| `gov.fdr.25.1` | *Divide and Conquer* (Part 1) | prior MMT sweep |
| `Dividean1943` | *Divide and Conquer* (the whole-film Prelinger item) | this session's own search |

**Liveness sampling, run this session:** 12 random `gov.archives.arc.*` movie items → **3 dead**
(25%). 10 random `gov.dod.dimoc.*` movie items → **4 dead** (40%). The search index reports
2,108 / 917 / 611 / 154 items for `gov.archives.arc.*` / `gov.dod.dimoc.*` / `universal_newsreels` /
`gov.fdr.*` respectively; a meaningful fraction of the first two is unreachable.

🔴 **New house rule this produces: a search hit is not an item.** Always fetch
`/metadata/<id>` and treat `{}` as *gone*, not as *empty*. Two of the recoveries above
(*Know Your Ally: Britain*, *Divide and Conquer*) were only found because the dead identifier was
re-searched by **title** across `collection:usgovfilms` and `collection:prelinger`.

### 2d. 🟡 Amber in the war family

| Item | Why amber | The specific doubt a human must answer |
| --- | --- | --- |
| `1942_Dover` (*Dover*, Universal Newsreel) | Uploader is **`skipe@mindspring.com`**, a personal address | The collection-level basis is sound (see below) but the prior sweep also flagged **embedded Ed Murrow audio**. Strip audio and check every insert |
| `collection:universal_newsreels` generally | Every item's uploader is that same personal address | The rights basis is **collection-level, not uploader-level**, and it reads well. IA's collection record states verbatim: *"Universal City Studios gifted Universal Newsreel to the American people, put the newsreels into the public domain, and gave film materials to the National Archives in 1976."* 🔴 That sentence was read **on archive.org**, not on a NARA page. Someone should pin it at NARA |

---

## 3. 🔴 Scene 07 has no British victory footage, and the obvious substitute is a lie

`gov.archives.arc.38936` (*The War Ends in Europe*) is green, cheap and wrong. Its frames were
scrubbed this session at 15-second intervals: **Times Square crowds, Truman announcing the surrender
at his desk, US and Soviet troops at the Elbe, Nuremberg.** It is an American VE Day.

Scene 07 is *"In 1945 Britain wins. Voters elect Attlee's Labour government."* Cutting an American
crowd under that line is a factual misrepresentation, and it is exactly the kind our own storyboard
bans. **Do not use it for scene 07.** It remains fine as context if the narration says what it is.

**What exists instead — British VE Day, as stills.** Wikimedia Commons, queried and licence-filtered
this session, has a deep set. Pick of the crop by size:

| File | Pixels | Commons licence | 🔴 The catch |
| --- | --- | --- | --- |
| `Ve_Day_in_London,_8_May_1945_HU49414.jpg` | 5335×3941 | "Public domain", `AttributionRequired: false` | **Source URL is `media.iwm.org.uk`** |
| `Ve_Day_Celebrations_in_London,_8_May_1945_HU41808.jpg` | 2480×1768 | same | same |
| `Air_Raid_Damage_in_Britain_…_HU36188.jpg` | 5163×4071 | same | same |
| `Bomb_Damage_in_London_…_HU36157.jpg` | 1300×950 | same | same |

🟡 **Why these are amber and not green.** The *copyright* argument is strong: a 1945 photograph by
an official UK government photographer is Crown copyright, which expires 50 years from creation, so
it genuinely is out of copyright — that is what Commons' `PD-UKGov` tag asserts. But the Commons
`Credit` field shows the file was **lifted from IWM's own media server**, and IWM is red on our
catalogue: its free tier expressly excludes *"fundraising or campaigning on behalf of
organisations."* That is the two-questions split in its purest form — *is the work free?* probably
yes; *is this file, from this host, clear for us?* unanswered. **Per-item human call. Do not launder
it to green.**

---

## 4. 🔴 Two portrait stills that look free and are not

Found and rejected this session, both of which a careless pass would have shipped.

| File | Commons says | What is actually true |
| --- | --- | --- |
| `Aneurin_Bevan_(1943).jpg` | "Public domain" | Photographer **Howard Coster, died 1959**. UK copyright is life + 70 → **in copyright until 2029.** Commons itself carries a warning on the file that *"one or more third parties have made copyright claims… use of this image in the jurisdiction of the claimant… may be regarded as copyright infringement."* 🔴 **Red for a UK audience** |
| `Person_attlee2.jpg` | "Public domain", 1559×2048 | Artist field reads **"Presumably Yousuf Karsh"** and the credit is a fan site (`ww2db.com`). Karsh died 2002 — if the attribution is right, this is firmly in copyright, and "presumably" is not a chain of title. 🔴 **Red** |

**Safe by comparison:**

| File | Pixels | Licence | Basis |
| --- | --- | --- | --- |
| `Clement_Attlee.jpg` | 1712×2445 | 🟢 **CC0** | Dutch Nationaal Archief (`proxy.handle.net/10648/…`), dated 1950-02-23. Genuinely CC0, no obligation. Attlee in 1950, not 1945 — a portrait, not an election shot |
| `Keynes_Martin.jpg` | 1348×1470 | 🟡 "Public domain", credit *Harvard University library*, author unknown | Best Keynes candidate found. Institutional credit, no competing claim on the file page. Still needs the per-item look |
| `John_Maynard_Keynes_1929.jpg` | 2048×1591 | 🟡 "Public domain" — **credit is a WordPress blog** | Bigger and better looking, far weaker chain of title. Prefer `Keynes_Martin.jpg` |
| `Aneurin_Bevan.jpg` (Geoff Charles, 1952) | 539×772 | 🟡 "No restrictions" | National Library of Wales' Geoff Charles collection. Promising, unverified at NLW; small |

---

## 5. The UK documents route — and the credit problem that blocks it

Verified live this session:

- **Open Government Licence v3.0**, fetched from `nationalarchives.gov.uk/doc/open-government-licence/version/3/`.
  You are free to *"copy, publish, distribute and transmit the Information"*, *"adapt the
  Information"*, and *"exploit the Information commercially and non-commercially."* Attribution
  required: *"Contains public sector information licensed under the Open Government Licence v3.0."*
  Exclusions that matter to us: **personal data; departmental logos, crests and the Royal Arms;
  military insignia; third-party rights the Information Provider is not authorised to license.**
- **TNA's "Birth of the NHS 1948" page** carries in its footer, verbatim: *"All content is available
  under the Open Government Licence v3.0, except where otherwise stated."* The NHS launch leaflet on
  that page is catalogue reference **`INF 2/66`, page 15** — the document scene 09 wants.

✅ **Settled 2026-09-12 — this route is open.** It was amber for one reason: OGL asks for a credit
line and BadCode had nowhere to put one. Kai has ruled that credits go in the video. So scenes 06,
09, 10 and 12 — all documents, all OGL — are usable.

**The credit this film owes, verbatim, once for all OGL material:**

> Contains public sector information licensed under the Open Government Licence v3.0.

🔴 **Two things still to watch.** OGL exempts **departmental logos, crests and the Royal Arms**
except where they form an integral part of the document — a 1948 leaflet's own masthead is integral,
a bolted-on crest is not. And TNA's footer says *"except where otherwise stated"*: check each item's
own notice, not just the page.

---

## 6. Still red, and no free route exists

| Beat | Why | What we do instead |
| --- | --- | --- |
| **Scene 11 — nurses on *Question Time*, 2 Jun 2017** | BBC copyright. BBC Studios licenses clips commercially; availability and cost unknown | The storyboard already plans for this: **exact subtitle cards plus a silent timeline, no imitation of the speaker.** The working narration is complete without a clip |
| **Scene 11 — Osborne's June 2010 Budget statement** | parliamentlive.tv's own terms bar *"advertising, promotion… or financial gain"* and are **more restrictive than the Open Parliament Licence**. OPL does not cover live or archived AV at all | Hansard text under OPL, typeset over dated Red Book pages |
| **Any UK archival film house** | IWM, BFI, British Pathé, Huntley: all paid, no free tier. IWM's free tier bans campaigning use by name | Stills, OGL documents, or Flow |

💷 **Would the budget change any of these? No.** BFI's cheapest published tier is **£840 + £14
per second** — four times the absolute ceiling before a single second is counted — and Pathé, IWM
and BBC Motion Gallery publish no floor at all and quote at broadcast scale. **£200 does not buy one
second of British archive film.** Where the free route does not exist, the answer above *is* the
answer, and the budget is better spent on a **still licence** for a beat that has no free
photograph — see §8.

---

## 7. On disk

Media lives **outside the repo**, under the Premiere media root so the bridge can open it.

```
/mnt/d/badcode-videos/magic-money-tree/clips/<scene>/     # WSL
D:\badcode-videos\magic-money-tree\clips\<scene>\         # Windows, what Premiere sees
```

*(The thread brief said `clips/mmt/<beat>/`; this is that, placed under the existing house
convention `<mediaRoot>/<story>/clips/<scene>/` — the same shape as `gitpush-origin-master` and
`camping-music` — so `premiere_import` can see it. Say so if you want the literal path instead.)*

| Beat | File | Bytes | sha256 |
| --- | --- | --- | --- |
| `s01-dunkirk` | `gov.fdr.25.4.mpeg` | 369,576,027 | `048f57d06d8267265f28b9ed6c33a5530083f98c74081689de668f91104a2a1f` |

**The command that fetched it, verbatim:**

```bash
mkdir -p /mnt/d/badcode-videos/magic-money-tree/clips/s01-dunkirk
cd       /mnt/d/badcode-videos/magic-money-tree/clips/s01-dunkirk
curl -sL -C - -o gov.fdr.25.4.mpeg \
  "https://archive.org/download/gov.fdr.25.4/gov.fdr.25.4.mpeg"
md5sum gov.fdr.25.4.mpeg     # → 95f87bb33a241c239e10b59b5415eb75, matches the metadata record
sha256sum gov.fdr.25.4.mpeg  # → 048f57d0…
```

**What `ffprobe` says, and it is not what the metadata claims:**

```
codec_name=mpeg2video   width=368   height=480
sample_aspect_ratio=40:23   display_aspect_ratio=4:3
field_order=tt   r_frame_rate=30000/1001   bit_rate=3500000
duration=809.009011      # matches the declared length of 809.01
```

🔴 **Three practical consequences.**
1. **The coded picture is 368×480, not the 640×480 the archive metadata advertises.** 640×480 is the
   *display* size after the 40:23 pixel aspect. Horizontal detail is genuinely that low. Everything
   in this family is standard-definition NTSC telecine and will be soft at 1080p. That is a look, not
   a defect — but nobody should be surprised at the grade.
2. **`field_order=tt` — it is interlaced.** Deinterlace with `-vf yadif=1`. Never blind, but here the
   probe says yes.
3. **Conform to ProRes before import**, or Premiere stalls on background transcode:
   `ffmpeg -i raw.mpeg -an -vf yadif=1 -c:v prores_ks -profile:v 3 -pix_fmt yuv422p10le conform-prores.mov`
   — `-an` because the soundtrack has its own licence and we make our own music anyway.

---

## 8. What is still open

| # | Open item | Who answers |
| --- | --- | --- |
| 1 | ~~Where does a credit line live?~~ | ✅ **Answered 2026-09-12 — in the video. OGL route open** |
| 2 | Is a `PD-UKGov` photograph pulled from IWM's own media server clear for us? — **now the biggest single blocker**, because it gates the British picture in scenes 02, 07 and 10 | 🔴 **Kai**, one ruling covers the class |
| 2b | 💷 Would **£100–200 on a per-image still licence** buy scene 07 or 10 something Commons cannot? Unpriced — needs a live check of a per-image library's terms *and* its political-use clause | Next pass, then 🔴 **Kai** approves the spend |
| 3 | Is each chosen *Divide and Conquer* shot actuality or a dramatised insert? | A human watching it |
| 4 | Scene 07 — British victory. Stills only, or is there a US-federal film containing British VE-Day material nobody has found? | Next pass |
| 5 | Scene 10 — post-war council housing. Nothing searched yet | Next pass |
| 6 | *Know Your Ally: Britain* (`gov.ntis.ava06858vnb1`) — 42 minutes, unwatched. The likeliest single source for scene 05 | Next pass |
| 7 | Pin Universal Newsreel's 1976 dedication at NARA rather than on archive.org | Next pass |

---

## 9. Provenance of this file

Pass 1, 2026-09-12. Every licence statement above was fetched in that session; every "dead" was
confirmed with both `/metadata/` and `/details/`. Corrections owed to
[`docs/video-fx/footage-sources.md`](../../video-fx/footage-sources.md) are listed in §2c and §3 and
have been written back there.
