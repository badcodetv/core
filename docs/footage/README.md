# Footage ledger — every real clip we have sourced, and whether we may publish it

**What lives here.** One JSON **receipt** per sourced item — the source API's response, verbatim,
tracked in git — plus this index. Nothing else. **No media.** The repo has never tracked a `.mp4`
and must not start; the bytes live under the Premiere media root (see *Where the bytes are* below).

**Why the receipts exist.** Archives take items down and uploaders delete accounts. On 2026-09-12
the `find-footage` reference's own flagship item, `gov.dod.dimoc.30172`, was found **withdrawn from
archive.org** — 404 on the details page, `{}` from the metadata API — while still appearing in the
search index. If a rights question is ever asked about something we published, the receipt is what
we have. It is the copy of the licence claim that survives the item.

**The procedure is the [`find-footage`](../../.claude/skills/find-footage/SKILL.md) skill; the
reference is [`docs/video-fx/footage-sources.md`](../video-fx/footage-sources.md).** Read rule zero
there before adding a row.

## The ledger

🟢 green = publish it · 🟡 amber = **a human must answer the doubt before it ships** · 🔴 red = don't

| Identifier | Source | Tier | Licence, as verified | Credit owed | Used in | Checked |
| --- | --- | --- | --- | --- | --- | --- |
| `gov.fdr.25.4` | archive.org · FedFlix | 🟢 | `publicdomain/zero/1.0/` (CC0); uploader `carl@media.org`; US War Dept work, 17 USC §105 | none | Magic Money Tree sc.01 (Dunkirk, 03:56–05:20) — **downloaded, md5 matched** | 2026-09-12 |
| `gov.fdr.25.2` | archive.org · FedFlix | 🟢 | CC0, same basis | none | MMT sc.01 context (invasion of France) — candidate | 2026-09-12 |
| `gov.fdr.25.3` | archive.org · FedFlix | 🟢 | CC0, same basis | none | MMT sc.01 context — candidate, **unwatched** | 2026-09-12 |
| `gov.archives.arc.65841` | archive.org · FedFlix | 🟢 | `licenses/publicdomain/`, same basis | none | MMT sc.01/02 (*The Battle for the Beaches*) — candidate, **unwatched** | 2026-09-12 |
| `gov.archives.arc.36070` | archive.org · FedFlix | 🟢 | CC0, same basis | none | MMT sc.02 (*The Battle of Britain*) — candidate, **unwatched** | 2026-09-12 |
| `gov.ntis.ava06858vnb1` | archive.org · FedFlix | 🟢 | `licenses/publicdomain/`, same basis | none | MMT sc.05 (*Know Your Ally: Britain*, 1943) — candidate, **unwatched** | 2026-09-12 |
| `gov.archives.arc.38936` | archive.org · FedFlix | 🟢 | CC0, same basis | none | 🔴 **Rejected for MMT sc.07** — it is an *American* VE Day (Times Square, Truman). Kept as context only | 2026-09-12 |
| `NARA - 531280` (Commons) | Wikimedia Commons · NARA | 🟢 | "Public domain", credit *U.S. National Archives and Records Administration*, `AttributionRequired: false`; US federal work | none | MMT sc.07 — VE Day, English woman with Allied servicemen, 2813×3000. **On disk** | 2026-09-12 |
| `NARA - 541917` (Commons) | Wikimedia Commons · NARA | 🟡 | "Public domain" + NARA credit — **but its own description says *"part of the New York Times Paris Bureau Collection"***. Custody ≠ authorship | unknown | MMT sc.02 — first mass air raid on London, 7 Sep 1940. **Held back** | 2026-09-12 |
| `INF 2/66` (TNA) | nationalarchives.gov.uk | 🟢 | **OGL v3**, stated in the page footer; 1948 Crown publication | ✅ *"Contains public sector information licensed under the Open Government Licence v3.0."* | MMT sc.09 — the NHS launch leaflet, 1837×2302. **On disk.** 🔴 It is the *Scotland* printing | 2026-09-12 |
| `MH 55/965` (TNA) | nationalarchives.gov.uk | 🟢 | **OGL v3**, same footer | ✅ same OGL line | MMT sc.12 — the "no fairy wand was waved" pamphlet. 🔴 Published image is only ~900 px | 2026-09-12 |
| IWM-sourced `PD-UKGov` stills (Commons) | Wikimedia Commons · **files uploaded from `media.iwm.org.uk`** | 🟡 | Commons says "Public domain" (Crown copyright expired 50 yrs from creation). **The file came off IWM's server, and IWM's free tier bans campaigning use** | none claimed | MMT sc.02, 07 **and** 10 — VE Day London, air-raid damage, prefab housing. 🔴 **One Kai ruling covers the class** | 2026-09-12 |

🔴 **Two traps this table already caught.** *"NARA"* in a credit is **not** automatically a US
federal work — `541917` is a donated *New York Times* photograph in NARA custody, and custody is not
authorship. And Commons' *"Public domain"* is a **US-law** finding: for a British subject read the
photographer's death date, not the tag (a Howard Coster portrait tagged PD there runs to 2029).

🔴 **Green here clears copyright and nothing else.** Every one of these films contains identifiable
real people. Recutting them to carry an argument the original did not is defamation by false
implication, and no licence closes it. And a Capra *Why We Fight* compilation mixes actuality with
dramatised inserts — **free to publish is not the same as true**, so a human looks at each shot.

## Where the bytes are

```
/mnt/d/badcode-videos/<story>/clips/<scene>/       # WSL
D:\badcode-videos\<story>\clips\<scene>\           # Windows — what Premiere opens
```

`mediaRoot` comes from `premiere_status()` (recorded in `badcode.local.json`). Keep the source
identifier **verbatim** in the filename: it is the only durable link back to the receipt.

| Story | Scene | File | Bytes | sha256 |
| --- | --- | --- | --- | --- |
| magic-money-tree | `s01-dunkirk` | `gov.fdr.25.4.mpeg` | 369,576,027 | `048f57d06d8267265f28b9ed6c33a5530083f98c74081689de668f91104a2a1f` |
| magic-money-tree | `s07-victory` | `NARA-531280-ve-day.tif` | 8,439,281 | `c327a0276228814e407c8a3f35fc94f24a69ef65ddbd22aeaccfade87743fbb8` |
| magic-money-tree | `s09-nhs-opens` | `INF-2-66-02-NHS-diagram-leaflet.jpg` | 999,844 | `e3bc369b9d3d08f7f3c837f33765683c25df01fa90a8cacd85d104312bab011d` |

## Per-story ledgers

A story's own ledger says *which beat needs what and why*; this file says *what we hold and whether
we may use it*.

- **Magic Money Tree** — [`docs/stories/magic-money-tree/footage.md`](../stories/magic-money-tree/footage.md)

## ✅ Credits — settled 2026-09-12

Kai: *"If we need to add a credit into the video in order to then use footage, of course — where we
can put that is in various places in the video, because we very happily put credits in."*

**So an attribution requirement is a cost we pay, not a blocker.** This un-blocks the **Open
Government Licence** (the whole UK government-document route), Commons CC-BY files, Europeana CC-BY,
LoC and CERN.

**Two obligations come with it.** Put the licence's **exact** credit string in the *Credit owed*
column above and in the story's ledger — OGL's is fixed (*"Contains public sector information
licensed under the Open Government Licence v3.0."*), CC-BY's is per-file, so read
`extmetadata.Artist`/`Credit` rather than composing one. And **never ship the clip without it**: a
credit we promised and dropped is worse than not using the material.

🔴 **Video only.** `@badcode/comic` still has no credits surface, so a CC-BY *still in a scroll
comic* remains open. And no credit cures ShareAlike, a non-commercial licence, or a political-use bar.

## 💷 The budget — £100, hard stretch £200, per film

Ruled 2026-09-12. **Not per clip.** It does **not** reach the UK archive houses: BFI's cheapest
published tier is **£840 + £14/sec**, and Pathé, IWM and BBC Motion Gallery quote at broadcast
scale. Best use is a **per-image still licence**; worst use is paying a PD reseller for NARA or LoC
material that is free at source. **Every spend is a stop gate** — price it, say what it buys that
free cannot, and wait for Kai. Log any committed spend in the ledger row before agreeing to it.
