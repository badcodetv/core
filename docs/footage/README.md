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

## Per-story ledgers

A story's own ledger says *which beat needs what and why*; this file says *what we hold and whether
we may use it*.

- **Magic Money Tree** — [`docs/stories/magic-money-tree/footage.md`](../stories/magic-money-tree/footage.md)

## 🔴 The open question that gates the most material

**BadCode has nowhere to carry a credit.** No credits surface in `@badcode/comic`, no end card, no
tail slate. So every attribution-requiring licence is amber by house rule — including the **Open
Government Licence**, which is otherwise exactly the permission we want and which covers the UK
government documents four Magic Money Tree scenes are built on. **Kai owes a ruling on where a
credit lives.** Don't improvise one: a credit we invent and quietly drop is worse than not using
the material.
