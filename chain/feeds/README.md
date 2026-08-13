# The M2 feed — and the proof it can't be tampered with

This directory holds the Switchboard job definition that is meant to put the US
money supply on-chain, and the evidence for the claim Emperor's New Coin rests
on.

**Everything below was executed live on 2026-08-10, not taken from documentation.**
Re-run any of it yourself; that is the point.

> **Status, so the present tense above is not read as more than it is (T21,
> 2026-08-13).** The immutability experiment is genuinely done and its result
> genuinely holds. **The feed is not wired to the program.** No feed is stood up
> on devnet (T17), the program's Switchboard read path is a stub that returns
> `OracleUnavailable` and the crate has no Switchboard dependency (T18), and the
> committed job extracts the *value* only — so `Quote.release_date` still has no
> source, which `retire` depends on. Nothing in this directory puts anything
> on-chain today.

## The claim

> We can't change what the coin does, because changing the job doesn't *edit* the
> feed — it creates a different feed our program won't read.

The feed's identity **is** a hash of its job definition. Switchboard's on-chain
account is a PDA derived from `(queue, feed IDs)`, so a different job means a
different hash means a different address. There is no authority field, no edit
operation, and no pause button.

Note what this does **not** claim. Switchboard's queue authority governs which
attested oracles may sign. The honest sentence is *"we removed ourselves from the
loop"* — not *"nobody is in the loop."* See `docs/coins/emperors-new-coin.md`.

## The proof

Three `POST https://crossbar.switchboard.xyz/store` calls, devnet queue
`EYiAmGSdsQTuCw413V5BzaruWuCCSDgTPtBGvLkXHbe7`:

| Job | Change | `feedHash` |
| --- | --- | --- |
| A | `cosd=2026-06-01` | `0xdaaa66fb08a01591f428c42644ede7488e66b165dd545e4a6dde12d83be20fa6` |
| B | `cosd=2026-06-0**2**` — one character | `0xbf8ed1036924c3d4462a5a1ae9cb1829384e1747ea80109e751455124f40dc79` |
| A again | none | `0xdaaa66fb08a01591f428c42644ede7488e66b165dd545e4a6dde12d83be20fa6` |

A single character produces a completely unrelated hash. Re-storing an unchanged
job reproduces its hash exactly. `queueHex` was identical throughout
(`0xc9477bfb…a66ca5b0`), so a different feed hash genuinely lands at a different
PDA rather than overwriting anything.

**The claim holds. It is safe to publish.**

## The production job

`m2sl.job.json` — its stored hash on the devnet queue:

```
0xbb3e9969719177b2e65c7d77c703d9cf351ad64ab979d72deb55708f873b9cfd
```

Keep this file forever. Crossbar pins the definition to IPFS but never documents
pin durability, and the SDK accepts inline job objects — so as long as this JSON
survives in git, the feed is reconstructible from a text file even if every
external service forgets it.

### Why it fetches the whole series

The job is **static forever** — its bytes are its identity, so it can never carry
a rolling date parameter. It therefore pulls the complete M2SL history (~14.5 KB,
811 rows) and extracts the final row.

**The regex is end-anchored, and that is load-bearing.** A naive first-match
pattern returns `286.6` — the money supply in **January 1959**. Pegging the coin
to Eisenhower-era M2 is the kind of bug that ships silently and can never be
undone, because the program is immutable. Verified:

```
[0-9]{4}-[0-9]{2}-[0-9]{2},([0-9.]+)\s*$   ->  23155.2   ✓ (June 2026)
[0-9]{4}-[0-9]{2}-[0-9]{2},([0-9.]+)       ->  286.6     ✗ (January 1959)
```

## The data source

`M2SL` — monthly, **seasonally adjusted**. Do not substitute the weekly series:
it is not seasonally adjusted, so it climbs every December on holiday cash demand,
and the coin would mint on Christmas shopping rather than Fed policy.

Two independent keyless sources agree exactly (2026-08-10, June 2026 observation):

| Source | Value |
| --- | --- |
| `fred.stlouisfed.org/graph/fredgraph.csv?id=M2SL` | 23155.2 |
| `api.db.nomics.world` → `FED/H6_H6_M2/M2.M` | 23155.2 |

Neither needs an API key. That matters more than convenience: Switchboard's hosted
secrets service is gone, and its replacement injects secrets at request time —
meaning a keyed feed can only be cranked by whoever holds the key. Keyless is what
keeps the feed permissionless after we stop paying attention.

Also confirmed live: DBnomics `M2.WM` (weekly, seasonally adjusted) last updated
**2021-W05**, corroborating that the Fed discontinued weekly SA publication in
February 2021. Releases are monthly, fourth Tuesday, 1:00 pm ET.

### Fetching notes

FRED sits behind Akamai bot protection. Blocks appear as **hangs, not errors**, so
a timeout is more likely a block than a network fault. A `python-requests`
User-Agent passes; a spoofed Chrome UA is blocked (its TLS fingerprint doesn't
match the claim). Pin a known-good UA and expect to chase this at least once.

## Still to do

- **Second source for redundancy.** DBnomics is the candidate (JSON, so
  `jsonParseTask` rather than regex), median-aggregated with FRED. Needs the
  JSONPath-to-last-element shape tested — its `observations=1` parameter does
  *not* limit the response to one observation.
- **Mainnet feed.** This hash is against the devnet queue. Mainnet gets its own,
  recorded in `m2sl.mainnet.json` at launch.
