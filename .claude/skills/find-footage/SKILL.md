---
name: find-footage
description: Use when looking for real footage that already exists and is free for BadCode to publish — archive film, newsreel, government and space footage, stock b-roll — and when checking whether a clip we already have is safe to use. Triggers on "is there a royalty-free clip of", "find footage of", "find stock footage", "search the Internet Archive", "can we get archive footage of", "is this clip safe to use", "what's the licence on this", "find archive footage", "is this public domain". Sourcing and clearance only — WHICH effect to reach for belongs to video-fx, inventing footage that never existed belongs to flow-prompt, and putting it on a timeline belongs to premiere-automation.
---

# Find Footage

**The sourcing lane.** Footage that *already exists* and is *free to use* — find it, prove we may
publish it, get it onto disk in a state Premiere can open.

The lane rule: **if the thing is real and already filmed, source it; if it never existed, invent it
in Flow.** Sourcing exists for footage whose *being real* is the point — an Apollo launch, a 1950s
factory floor, the fall of France. For a war scene, a crowd, a burning building, Flow is free at
the margin and carries no rights question at all.

## What this is not

| Job | Skill | Question it answers |
| --- | --- | --- |
| **Finding and clearing real footage** | **this skill** | Does it exist? May we publish it? Where is the file? |
| **Choosing the effect** | `video-fx` | Fire, film look, map zoom — which lane, what does it cost? |
| **Inventing footage that doesn't exist** | `flow-prompt` | How do I write the prompt so Veo makes it? |
| **Putting it on the timeline** | `premiere-automation` | Import, cut, trim, grade, export |
| **The BadCode look** | `badcode-art-direction` · `new-image` | What should it look like? |

**The reference this skill runs on:**
[`docs/video-fx/footage-sources.md`](../../../docs/video-fx/footage-sources.md) — 68 sources with
every count, command, trap and licence quote. **This file is the procedure; that file is the
lookup.** Anything not answered here is answered there.

---

## 🔴 Rule zero — the licence gate. Nothing gets past this.

**Two questions, and they have different answers:**

1. Is the underlying footage's copyright expired or waived?
2. Is **this file, from this source, clear for *us* to publish?**

Almost every trap is the gap between them. A 1940 Ministry of Information reel answers *probably
yes* to (1) and **no** to (2) if you pull it from IWM, because IWM licenses its own print under its
own terms regardless.

> **"It's old" is not a licence. "It's on the Internet Archive" is not a licence. "It's on YouTube"
> is not a licence. "Royalty-free" is not a licence** — royalty-free is a *pricing* model and RF
> EULAs routinely carry editorial-only and no-political-use clauses, which is exactly our use case.

### The tiers

| Tier | What it means | Do |
| --- | --- | --- |
| 🟢 **Green** | US federal work (17 USC §105), an institutional PD dedication, or CC0 — **and we verified it ourselves.** No credit owed, no clause to weigh | Download it. Still read the people-in-frame rule below |
| 🟡 **Amber** | Mixed collection, inferred licence, attribution or ShareAlike obligation, a clause that might bite, or a source nobody ever authenticated against | 🔴 **Per-item check, and it does not ship until a human has answered.** See the hard stop |
| 🔴 **Red** | Paid house, non-commercial licence, embed-only, dead domain | Don't. Say so, name the free route, move on |

**The seven green sources — memorise these, they answer most requests:**

| Green source | For |
| --- | --- |
| `identifier:gov.archives.arc.*` (FedFlix/NARA) | US federal film, 2,107 items |
| `collection:nasa` | Mission footage, NASA TV, 13,733 items |
| `identifier:gov.dod.dimoc.*` | US military, DIMOC-numbered, CC0 |
| `collection:universal_newsreels` | Newsreel 1932–1967 — cleanest licence on the page, only 611 digitised |
| `images-api.nasa.gov` | Every NASA centre. Keyless — and it **rejects `api_key` with HTTP 400** |
| `svs.gsfc.nasa.gov/api` | Climate/ocean/ice viz. Hands you the literal mp4 URL |
| Wikimedia Commons — **CC0 / PDM files only** | Everything else. 🔴 The BY-SA majority is amber |

Everything else is amber or red. **Prelinger is amber except the `licenseurl:*` subset** (1,913 of
10,459), which is green.

### 🔴 The hard stop — nothing amber gets published without a per-item check

**This is not a formality and it is not automatable.** Say it to the user in these words when it
applies:

> *"That source is amber. I can download it, but it needs a per-item licence check before it goes
> into anything we publish."*

**Why, concretely:** archive.org's `licenseurl` field is **uploader-asserted**. IA's own rights page
says it "cannot guarantee information posted on item details or collection pages regarding
copyright." A private individual can tick "Public Domain Mark" on a file they have no rights to,
and it looks identical in the API to a genuine agency CC0. **This page's own flagship Dunkirk
example, `FB-56`, was rated green for months and is uploaded by a personal Gmail address into
community collections with an uploader-asserted PD Mark.** That is what amber protects against.

**The check, in two halves. Half A is scriptable. Half B is not.**

**Half A — run it every time, takes seconds:**

| # | Check | Fail = stop |
| --- | --- | --- |
| 1 | **Provenance.** Trusted identifier prefix or collection? An `@nasa.gov` / FedFlix (`carl@media.org`) / DIMOC uploader counts. **A personal email address does not** | Yes |
| 2 | **Exact licence code**, not a substring. `creativecommons.org` also matches `by-nc-nd`. **BY / BY-SA / CC0 / PDM are four different answers** | Yes |
| 3 | **Obligation.** Attribution or ShareAlike required? → **amber, not green** — we have no credits surface (see below) | Downgrade |

**Half B — a human answers these, out loud, before it ships:**

| # | Check |
| --- | --- |
| 4 | **The host's own terms.** Is the institution charging for *its print*, on top of the underlying copyright? (IWM, BFI, Pathé, CERN: yes) |
| 5 | **Restoration.** UK source — is this a modern rescan an institution claims fresh copyright in? Under UK law it may genuinely have one, over PD source |
| 6 | **Political and endorsement clauses.** Adobe bars *"implied or stated endorsements of political parties"*; Pexels and Pixabay bar political context by name; DVIDS bars implying endorsement of *"any political party or candidate"*; NASA and ESO bar implied endorsement. **BadCode's entire output is political argument** |
| 7 | **People in frame.** Will our cut put an identifiable real person in a context the original didn't support? |

### 🔴 The one risk no licence clears

Recutting genuine, cleanly-licensed archive footage of a **real, identifiable person** to build a
political argument the original context did not carry is **defamation by false implication**. It
lives in the juxtaposition, not the clip. It survives a perfect clearance pass. It scales with
exactly what BadCode does.

**Every green source is full of identifiable people** — NASA, DVIDS, NPS, ESO, LoC, C-SPAN. §105
waives *copyright* and nothing else: NASA's own guidelines separately bar use of astronauts'
**likenesses** in commercial or promotional material and warn about right of privacy/publicity.
**Hardware, crowds, landscapes, launches: fine. A named person's face carrying an argument: Kai's
call, every time.**

### 🔴 CC-BY-NC is a hard kill · CC-BY needs a home we don't have

- **NC:** "not primarily intended for commercial advantage." **We sell music.** Judged at the
  entity level — "we didn't charge for this comic" does not cure it. See `by-nc` or `by-nd` in a
  `licenseurl`, stop.
- **SA:** not a commercial bar, but it forces the *finished piece* to be relicensed CC-BY-SA.
  Editing a clip into a comic is an adaptation. Amber, human call.
- **BY:** 🔴 **There is nowhere in BadCode to carry a credit.** No credits surface in
  `@badcode/comic`, no end card, no tail slate. **Every attribution-requiring source is amber until
  Kai rules on where a credit goes.** Don't improvise one — a credit we invent and quietly drop is
  worse than not using the clip.

### 🔴 Strip the audio by default

The visuals and the soundtrack have **different licences**. A PD film with a licensed music bed is
the single most recurrent trap on the reference page (NASA, NASA SVS, ESO, Pond5, NOAA). `-an`
costs nothing and we make our own music anyway (`suno-prompt`). Keep native audio only after
reading that item's credits.

---

## The three recipes that answer most requests

Run these before opening the reference. **Always scope an archive.org query with `collection:` or
`identifier:`** — a bare `title:"dunkirk" AND mediatype:(movies)` surfaces community mirrors with
no licence claim before any curated result.

**1. The green federal sweep — first thing to try for any historical or institutional subject:**

```bash
Q='%22fall+of+france%22'   # url-encoded phrase, or just a keyword
for SCOPE in 'identifier%3Agov.archives.arc.*' 'identifier%3Agov.dod.dimoc.*' \
             'collection%3Anasa' 'collection%3Auniversal_newsreels'; do
  curl -s "https://archive.org/advancedsearch.php?q=$SCOPE+AND+mediatype%3A(movies)+AND+$Q&fl[]=identifier&fl[]=title&fl[]=licenseurl&fl[]=year&sort[]=downloads+desc&rows=10&output=json" \
    | jq -r '.response.docs[]? | [.identifier, (.licenseurl // "-"), .title] | @tsv'
done
```

**2. Prelinger, filtered to the green subset** — 20th-century American ephemeral, industrial,
educational, advertising and sponsored film. The right first stop for factory floors, offices,
finance, consumer life:

```bash
curl -s 'https://archive.org/advancedsearch.php?q=collection%3Aprelinger+AND+mediatype%3A(movies)+AND+licenseurl%3A*+AND+factory&fl[]=identifier&fl[]=title&fl[]=licenseurl&fl[]=year&sort[]=downloads+desc&rows=20&output=json' \
  | jq -r '.response.docs[] | [.identifier, .year, .title] | @tsv'
```

**3. Wikimedia Commons, licence-filtered in the same call** — the widest net, and the only source
with a genuinely machine-readable per-file licence. 🔴 **The filter is mandatory: the free-licence
majority on Commons is CC-BY-SA, which is amber by our own rule.**

```bash
curl -s 'https://commons.wikimedia.org/w/api.php?action=query&format=json&generator=search&gsrsearch=filetype:video%20apollo&gsrnamespace=6&gsrlimit=20&prop=imageinfo&iiprop=url|size|mime|extmetadata' \
  | jq -r '.query.pages[] | .imageinfo[0] as $i
           | [$i.extmetadata.LicenseShortName.value, ($i.size|tostring), $i.url] | @tsv' \
  | grep -E '^(CC0|Public domain|PDM)'      # ← drop this grep and you have left the green tier
```

🔴 **Commons search matches place names, not events.** A "dunkirk" search returns a handball match
and four cycling stages in Dunkerque and zero WWII footage. Name the event, the year and the
belligerents, or traverse a category instead.

**One more worth knowing:** NASA SVS hands you the mp4 URL directly, no filename guessing —
`curl -s 'https://svs.gsfc.nasa.gov/api/search/?q=glacier'` then
`curl -s 'https://svs.gsfc.nasa.gov/api/<id>/' | jq -r '.main_video.url'`.

**Nothing hit?** In order: try a **still** instead (a slow push-in on a PD photograph reads as
archive and LoC/Commons/NARA stills are far richer than their video) → try **Flow** → and only then
tell the user the honest answer, which is that this subject may not exist free. 🔴 **Never end at
"licence it from Pathé."** The specialists — Pathé, IWM, BFI, AP, Reuters, Huntley, NFB, NFSA — are
all red and all paid. Being the specialist is exactly why they are the wrong tool for us.

---

## Download and verify

🔴 **Three rules, each learned the hard way:**

1. **Never guess a filename.** There is no fixed derivative ladder. Fetch `/metadata/<id>`, filter
   `files[]` for `source == "original"`, take the largest. One NASA item had **no mp4 at all**.
2. **`curl -L` always.** A bare `curl -I` on archive.org shows 302 whether or not the target exists.
3. **`ffprobe` exit 0 does not mean you got the whole file.** A truncated Ogg conformed cleanly
   through ffmpeg and produced 30.9s of playable footage from a 555s source. **Compare duration
   against the metadata's declared `length`.**

The full runnable loop, verified live:

```bash
set -euo pipefail
ID=gov.dod.dimoc.30172
DEST="$MEDIA_ROOT/footage/archive.org/$ID"      # MEDIA_ROOT = premiere_status().mediaRoot, WSL form
mkdir -p "$DEST"

curl -s "https://archive.org/metadata/$ID" > "$DEST/source-metadata.json"
jq -r '.metadata | {identifier,uploader,licenseurl,collection}' "$DEST/source-metadata.json"   # ← Half A

read -r NAME MD5 SIZE < <(jq -r '[.files[] | select(.source=="original") | select(.name|test("\\.(mp4|mov|mpeg|mpg|avi|ogv|webm)$";"i"))]
  | sort_by(.size|tonumber) | last | [.name, .md5, .size] | @tsv' "$DEST/source-metadata.json")

curl -sL -C - -o "$DEST/raw.${NAME##*.}" "https://archive.org/download/$ID/$NAME"
echo "$MD5  $DEST/raw.${NAME##*.}" | md5sum -c -                                    # integrity
jq -r --arg n "$NAME" '.files[]|select(.name==$n)|.length' "$DEST/source-metadata.json"   # expected
ffprobe -v error -show_entries format=duration -of csv=p=0 "$DEST/raw.${NAME##*.}"        # actual

ffprobe -v error -show_entries stream=field_order -of csv=p=0 "$DEST/raw.${NAME##*.}"     # tt/bb → deinterlace
ffmpeg -y -i "$DEST/raw.${NAME##*.}" -an -c:v prores_ks -profile:v 3 -vendor apl0 \
  -pix_fmt yuv422p10le "$DEST/conform-prores.mov"
```

**Pre-flight without downloading:** the metadata record carries per-file md5, width, height and
`length` — **it is your free ffprobe.** Read it before deciding whether to pull 950MB. Commons'
`videoinfo` does the same.

**Conform notes:** ProRes avoids Premiere's background-transcode stall on import. Deinterlace with
`-vf yadif=1` **only** if `field_order` says `tt`/`bb` — never blind. Don't force-pillarbox 4:3 in
ffmpeg; leave it native and let the sequence place it. Build the sequence at the **source** frame
rate rather than converting.

**Politeness:** sequential fetches, 1–2s between calls, **no parallel workers against one host**,
treat 429/503 as *stop for a few minutes*.

---

## Where it lands, and the handoff

| What | Where | Why |
| --- | --- | --- |
| **The bytes** | `<mediaRoot>/footage/<source>/<identifier>/raw.<ext>` and `conform-<preset>.mov` | `mediaRoot` comes from `premiere_status()` (e.g. `D:\badcode-videos` ⇄ `/mnt/d/badcode-videos`). **Download anywhere else and Premiere cannot see the file.** The repo has never tracked a `.mp4` and must not start |
| **The receipt** | `docs/footage/<source>--<identifier>.json` — the API response verbatim, tracked in git | Archives take items down and uploaders delete accounts. If a rights question ever comes up, this is what we have |
| **The ledger row** | `docs/footage/README.md` | identifier, source, tier, exact licence code, credit line if owed, the Half B answers if amber, and which piece it went into |

🔴 **Neither `docs/footage/` directory nor the ledger exists yet** — the first session to source a
clip creates them. Don't invent a different layout.

**Then hand to `premiere-automation`:**

```
premiere_status()                                            # → mediaRoot, and is the bridge up
premiere_import({ paths: ["/mnt/d/badcode-videos/footage/archive.org/<id>/conform-prores.mov"] })
```

Keep the archive identifier **verbatim** in the path — it is the only durable link back to the
metadata record and the licence claim.

---

## Reporting back to the user

**Always say the tier and the reason, not just the link.** A bare "found it, here's the URL" hides
the only thing that matters.

| Situation | Say |
| --- | --- |
| Green hit | *"`gov.dod.dimoc.30172`, CC0, FedFlix — green, safe to publish. Downloaded and conformed to `<path>`."* |
| Amber hit | *"Found it on Prelinger but it has no `licenseurl` — amber. I can pull it; it needs a per-item check on the sponsor before it ships."* |
| Only red exists | *"The only source is British Pathé, which is paid per-second and states none of its collection is PD. Free routes: a US federal compilation of the same event, or invent it in Flow."* |
| Nothing exists free | Say so plainly and let Kai decide. **Never end at "buy it."** |

🔴 **Never launder a tier.** If you could not cure an uploader-asserted claim, it stays amber. "It's
obviously a War Department film" is a vibe, not a check.

---

## Write back what you learn

Everything new goes into
[`docs/video-fx/footage-sources.md`](../../../docs/video-fx/footage-sources.md), **dated, with the
exact command and what the response actually was.** That page is only worth anything if it stays
honest — it carries a verification table separating what was proven live from what was merely read,
and a corrections log of claims that failed re-run.

| You learned | Where it goes |
| --- | --- |
| A new source, or a tier that was wrong | The catalogue + the tier tables + the status counts |
| A count that had drifted | The entry **and** the verification table, date-stamped |
| A command that failed or a trap | The relevant entry, with the literal response |
| A licence clause nobody had read | The entry, **quoted verbatim**, with the URL |
| A subject with no source at all | **Known gaps** — protest/labour and finance are both open and both matter |

**Mark what you verified and what you only read.** A confident wrong claim about a licence costs
far more than an honest gap.

---

## Scope

Finding real footage and proving we may publish it: search recipes, licence tiers, the clearance
check, download integrity, conform, disk layout, receipts. **Not** which effect to apply
(`video-fx`), **not** inventing footage that never existed (`flow-prompt`), **not** the timeline
(`premiere-automation`), **not** music (`suno-prompt` — we make our own).
