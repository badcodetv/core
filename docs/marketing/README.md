# BadCode marketing — the plan

**Status:** v1, drafted 2026-07-16 (Kai + Jack decision: continuous release, automate the marketing).
**Companion docs:** [`platform-playbooks.md`](./platform-playbooks.md) (research-grounded growth
mechanics per platform) · [`agent-orange.md`](./agent-orange.md) (how this plan runs as an
Agent Orange worker fleet) · [`marketing-manager-prompt.md`](./marketing-manager-prompt.md)
(the seed system prompt) · [`badcode-image.md`](./badcode-image.md) (the BadCode worker image spec).

---

## 1. Posture: continuous release

The album-drop model is dead. We do not hoard content for a big-bang launch; we release each
piece as it finishes and keep a continuous stream of small satellite content flowing between
core releases. The algorithm feeds accounts that post consistently; audiences bond with
presences, not archives.

Operating rules:

1. **Ship the moment a core is done.** Camping's comic, track, and music video release as each
   crosses the line — not held for each other beyond a short deliberate sequence (§5).
2. **Every core spawns satellites immediately.** A finished comic is also 20 panel posts, 5
   shorts, 3 lyric cards, and a making-of reel. The core is the reservoir; satellites are the
   drip.
3. **Cadence beats polish for satellites.** Cores get the full BadCode production bar.
   Satellites need to be *in voice and on brand* — not perfect. A good tweet today beats a
   great one next month.
4. **Everything funnels down.** Satellite → core → badcode.tv. No dead-end content.

## 2. The content universe model

Each story is a **core** orbited by **satellites**:

```
                        badcode.tv  (the terminus — every path ends here)
                            ▲
        ┌───────────────────┼──────────────────────┐
        │                CORE (per story)          │
        │  scroll comic (badcode.tv)               │
        │  narrated comic video (YouTube)          │
        │  track (Spotify / SoundCloud / YT)       │
        │  music video (YouTube)                   │
        └───────────────────▲──────────────────────┘
                            │
   SATELLITES (continuous): panel carousels · shorts/clips · lyric cards ·
   funnel posts (news-reactive) · narrator transmissions · making-of reels ·
   replies/duets/stitches
```

- Every satellite links to exactly one core (usually the story it orbits).
- Every core links to badcode.tv and to the other cores of the same story.
- Links carry UTM tags (`utm_source=<platform>&utm_campaign=<story>`) so the analyst worker can
  attribute funnel clicks.

**The moral core.** Every story gets one sentence identifying its moral center — this is what
satellites hook into current events with. Recorded per story in `docs/<story>/`:

| Story | Moral core |
| --- | --- |
| Camping | Don't be so quick to judge the homeless — homelessness is a symptom of the wealth gap, and the distance between the smug man and the broken man is five years. |
| Magic Money Tree | "We can't afford it" is a fiction — money is created, not found. |
| Karen | The people dismissed as ridiculous are often the ones who move first. |
| Emperor's New Coin | Value backed by nothing but confidence ends the way it always has. |

## 3. The strategy portfolio

Each strategy: what it is, format, cadence, effort, and which Agent Orange worker owns it
(roster in [`agent-orange.md`](./agent-orange.md)).

### 3.1 Funnel strategy — news-reactive commentary *(the founding idea)*

Identify each active story's moral core, continuously scout news / current affairs / public
debate on that theme, and publish short reactive pieces — a tweet thread, a single image with
narrator caption, a react-style video that meaningfully edits third-party material with our
commentary — each ending with the funnel line: *"…if this caught you, we made a whole story
about it. It's called Camping. → link"*.

- **Format:** text post, quote-post, image + caption, or short react video (see fair-use rules §8).
- **Cadence:** weekly per active theme (starts with homelessness for Camping).
- **Workers:** `trend-scout` finds the angle → `copywriter` writes it → `publisher` posts it.
- **Why it works:** rides existing attention (news gets algorithmic distribution we can't buy),
  demonstrates the voice, and gives every story an evergreen acquisition channel.

### 3.2 Slice strategy — cut the cores into platform-native satellites

Existing finished content re-cut per platform: comic panel runs as Instagram carousels, the
strongest single panels as image posts, 15–30s song sections as Shorts/Reels/TikToks over comic
art, music-video teaser cuts, lyric cards (one couplet + one panel).

- **Cadence:** 2–3 slices/week while a core is fresh; 1/week evergreen after.
- **Workers:** `clip-maker` (video) + `image-maker` (stills) + `copywriter` (captions).
- **Zero new creative cost** — the reservoir already exists; this is editing, not creating.

### 3.3 Serialization strategy — release the comic as a series

A comic drops act-by-act (or 4–6 panel runs) as a scheduled series on Instagram/X/TikTok
(panels as swipe/scroll posts), each installment cut on a cliffhanger, final installment links
the full scroll comic on badcode.tv. Turns one core into weeks of scheduled presence and
trains the audience to come back.

- **Cadence:** 2 installments/week per serialized story.
- **Workers:** `copywriter` (cut points + captions from the comic's page list) + `publisher`.

### 3.4 Narrator-in-residence strategy — the account IS the superintelligence

The social accounts don't post *about* BadCode; they post *as* the narrator — a
superintelligence from a future that already went wrong, commenting on today's news as
received history. Short "transmissions from the bad branch": *"Day 14,203 until the fork.
You're still arguing about whether you can afford things you can already build."*

- **Format:** short text posts, occasionally over a brand image (monolith register).
- **Cadence:** daily (morning transmission); this is the account's heartbeat between satellites.
- **Workers:** `copywriter` on a daily schedule.
- **Why it works:** persona accounts compound — people follow characters, not brands. The
  voice guide (`docs/voice.md`) is the entire content strategy here.

### 3.5 Making-of strategy — the AI collective shows its hands

Behind-the-scenes of a superintelligence making comics with AI: prompt→image evolution reels,
panel revision timelapses (we keep every prompt + revision log in the panel records — this is
free material), "how a panel gets made" shorts, Flow/Suno workflow peeks.

- **Cadence:** 1/week.
- **Workers:** `clip-maker` + `copywriter`; raw material comes straight from
  `docs/<story>/storyboard/` revision logs.
- **Why it works:** the AI-makes-art process is itself high-curiosity content in 2026, and it's
  honest about what we are — leaning into AI authorship instead of hiding it.

### 3.6 Music-first strategy — the DnB channel

The music has its own scene with its own distribution: SoundCloud (DnB community, reposts),
Spotify (editorial + algorithmic playlist pitching via Spotify for Artists, pre-save
campaigns), full tracks on YouTube with comic-art visualizers, genre communities (UKF-adjacent,
r/DnB, DnB TikTok). Tracks credit the story: every upload description carries the story link.

Two verified 2026 constraints (details in the playbooks §4–5): **SoundCloud will not
distribute/monetize Suno-made tracks** (Suno isn't an approved AI partner — SoundCloud is
hosting + community only; Spotify-and-co distribution goes via a DDEX-supporting distributor,
DistroKid first among them), and **Spotify's spam filter de-recommends mass-uploaders** —
release deliberately, full-length tracks only, and declare AI use via the distributor's DDEX
AI credits on every release.

- **Cadence:** per release + weekly community engagement.
- **Workers:** `publisher` (uploads + pitching are mostly manual/human-attended at first) +
  `trend-scout` (playlist/community targets).

### 3.7 Engagement strategy — go where the conversation already is

Reply, quote, duet, and stitch in threads and videos adjacent to each story's theme — in
voice, adding a real point, never punching down, never spamming links (link only when someone
asks or the reply genuinely lands). Early-account growth is disproportionately driven by
showing up in other people's comment sections with the best reply.

- **Cadence:** small daily allotment (e.g. 3–5 quality replies/day).
- **Workers:** `trend-scout` surfaces threads → `copywriter` drafts replies → human approves
  (stage 1) → `publisher`.

### 3.8 Owned-channel strategy — badcode.tv as the terminus

Everything funnels to ground we own: an email list ("Transmissions" — release announcements in
narrator voice), release notes per core, canonical URLs for every story. The email list is the
only audience asset no algorithm can take away.

- **Cadence:** email on every core release + monthly digest.
- **Workers:** `copywriter` + `secretary` (list management, replies).

### 3.9 Collab strategy — borrowed audiences

Targeted collaborations: DnB producers/labels (track feedback, reposts, remix stems), political
commentary creators (react to our comics), AI-art creators (process exchanges). One genuine
collab beats a month of cold posting.

- **Cadence:** 1 outreach/week, human-approved.
- **Workers:** `trend-scout` (targets) + `secretary` (outreach drafts, human-gated).

### 3.10 Evergreen search strategy — "explained by an AI from the future"

YouTube/Google reward search-shaped content long after posting: "The Magic Money Tree,
explained by a superintelligence", "Why automation comes for the financier too". Narrated
comic videos double as this if titled/described for search. Low volume, long tail.

- **Cadence:** riding the narrated-video releases; titles/descriptions owned by `copywriter`.

## 4. Platforms

Per-platform mechanics (algorithm behavior, cadence, format specs, cold-start tactics, AI
disclosure rules) live in [`platform-playbooks.md`](./platform-playbooks.md) — research-grounded
and re-checked monthly by `trend-scout`. Summary of intent:

| Platform | Role | Primary strategies |
| --- | --- | --- |
| YouTube | Core home: narrated comics, music videos, visualizers + Shorts | 3.2, 3.5, 3.6, 3.10 |
| TikTok | Discovery engine: shorts, react edits, duets | 3.1, 3.2, 3.5, 3.7 |
| Instagram | Visual home: carousels, serialized panels, Reels | 3.2, 3.3, 3.4 |
| X/Twitter | The narrator's voice + news reaction | 3.1, 3.4, 3.7 |
| SoundCloud | DnB scene credibility | 3.6 |
| Spotify | Music distribution + playlists | 3.6 |
| Facebook | Low-effort mirror of IG/YT content | 3.2 |
| LinkedIn | Occasional: the economics/automation angle, making-of | 3.5, 3.10 |
| badcode.tv + email | Terminus | 3.8 |

**Priority order for effort:** TikTok + YouTube (discovery) → Instagram + X (home base + voice)
→ SoundCloud/Spotify (scene) → Facebook/LinkedIn (mirrors, near-zero marginal effort).

## 5. Campaign #1: Camping launch

The first concrete run — also the shakedown cruise for the whole machine.

**Prerequisites (human):** finish the comic edits (Kai), finish the song tweaks (Kai), finish
the music video (Jack), register the accounts (§7 checklist).

**Release sequence (~2 weeks, order chosen so each release promotes the next):**

1. **T-7 → T-1: seeding.** Narrator transmissions begin on X/IG/TikTok (§3.4) — the account
   exists and is in voice before anything drops. 2–3 making-of teasers (§3.5).
2. **T0: the track.** Spotify + SoundCloud + YouTube visualizer. Satellites: 15s hook clips.
3. **T+3: the comic.** Live on badcode.tv + narrated video on YouTube. Satellites: serialized
   panel run starts (§3.3), best-panel posts.
4. **T+10: the music video.** YouTube. Satellites: teaser cuts, duet/stitch invitations.
5. **T+14 onward: the funnel.** Weekly homelessness/wealth-gap angle (§3.1) becomes the
   standing drumbeat, all pointing at Camping.

## 6. Cadence calendar (starting rhythm — the manager owns tuning it)

Deliberately modest; consistency over volume. All times UK.

| When | What | Strategy | Worker |
| --- | --- | --- | --- |
| Daily 09:00 | Morning transmission (X, mirrored IG/TikTok text) | 3.4 | copywriter |
| Daily 14:00 | 3–5 engagement replies | 3.7 | trend-scout → copywriter |
| Mon 10:00 | Funnel piece: this week's angle on the active theme | 3.1 | trend-scout → copywriter → publisher |
| Tue + Fri 17:00 | Slice or serialization installment | 3.2 / 3.3 | clip-maker / copywriter |
| Wed 12:00 | Making-of piece | 3.5 | clip-maker |
| Thu | Music/community touch (SoundCloud reposts, playlist pitch, collab outreach) | 3.6 / 3.9 | trend-scout / secretary |
| Every 2h | Inbox check + replies | — | secretary |
| Sun 18:00 | Analyst weekly report → memory | §9 | analyst |
| Sun 19:00 | Manager self-critique + strategy review | §9 | marketing-manager |
| Daily 08:00 | Manager workforce reconcile | — | marketing-manager |

## 7. Account setup checklist (manual, human — one-time)

Register as **BadCode** everywhere (fallbacks: `badcodetv`, `badcode_tv` — pick ONE fallback
and use it identically on every platform where `badcode` is taken):

- [ ] YouTube channel (+ enable Shorts, upload defaults with badcode.tv link)
- [ ] TikTok
- [ ] Instagram (creator account)
- [ ] X/Twitter (+ API tier for posting — see [`badcode-image.md`](./badcode-image.md) §MCP)
- [ ] Facebook page (via Meta Business Suite — also unlocks IG API)
- [ ] LinkedIn page
- [ ] SoundCloud
- [ ] Spotify for Artists (requires a distributor — DistroKid was first to implement the DDEX
      AI-credits disclosure Spotify displays; verify AI-content terms at signup)
- [ ] Email list provider (Buttondown/Mailchimp/etc.) wired to badcode.tv

Conventions: avatar = brand monolith register (`docs/images/`), bio = one-line narrator intro +
badcode.tv link, pinned post = current core. Handles, passwords, and API credentials go in the
operator's env config (never in this repo — see Agent Orange credential rules).

## 8. Fair-use / react-content rules (binding for all workers)

The funnel strategy uses third-party material (news clips, posts). Rules:

1. **Transform, never re-host.** Our commentary/edit must be the point of the piece; the
   borrowed material is the object being commented on. Use the minimum needed to make the point.
2. **Platform asymmetry:** X quote-posts and TikTok duets/stitches are platform-sanctioned
   reaction mechanisms — prefer them. YouTube is the hostile surface: Content ID matches
   clips of just a few seconds and rightsholders auto-monetize ~90% of claims — on YouTube,
   react content must be heavily transformed (our narration dominant, clips under ~5–10s,
   criticism/commentary explicit). A monetization claim is a cost of doing business; a
   dispute escalation is not — **never escalate past an initial Studio dispute without
   Kai/Jack sign-off** (that's where DMCA strikes and channel-termination risk live).
3. **Music is ours** — always prefer scoring react pieces with our own tracks (free rights +
   it markets the music).
4. **Never target private individuals.** Comment on institutions, policies, public statements
   by public figures. Punching down is a voice violation *and* a risk.
5. **AI disclosure:** follow each platform's synthetic-media labeling rules (per-platform
   detail in the playbooks — YouTube now auto-labels detected AI content anyway; Spotify
   wants DDEX AI credits). We lean into being AI-made — disclosure is on-brand, not a cost.
6. **UK caveat:** the verified fair-use analysis is US doctrine; the UK's fair dealing regime
   is narrower (playbooks §10). Until that's resolved, react content stays stage-1
   human-approved regardless of autonomy graduation elsewhere.
7. When in doubt → `request_human_attention`.

## 9. Measurement & the learning loop

Success metric hierarchy (in order — the consultant optimizes for the top, not the bottom):

1. **Funnel clicks to badcode.tv** (UTM-attributed) and email signups — the only numbers that
   are truly ours.
2. **Follower growth per platform** (compounding reach).
3. **Engagement rate** (is the voice landing?).
4. Views/impressions (vanity — context only).

The loop: `analyst` sweeps platform metrics weekly into Agent Orange memory
(`kind=metric, platform=…, week=…`) → `consultant` reads results against what was posted →
rewrites worker prompts (`worker_prompt_write`) with concrete lessons ("threads outperform
single tweets 4:1 — default to threads") → `marketing-manager` weekly self-critique adjusts
strategy/schedules. Every strategy change lands in memory with reasoning, so the strategy's own
revision history is minable.

Kill criteria: any standing satellite format that shows no funnel contribution after 8 weeks
gets its cadence cut or killed by the manager — the plan sheds losers by default.

## 10. Voice guardrails for marketing (non-negotiable)

Everything public follows [`docs/voice.md`](../voice.md). The marketing-specific distillation:

- The narrator has **seen the ending** — certainty, dark humor, no hedging, no corporate voice.
- Contempt for the **mistake**, never the people. Never punch down (the homeless man is
  sympathetic; the system is the target).
- **Story over sermon** — even a tweet leads with image/metaphor, politics arrives through it.
- The two-step: brutal truth, then care. *"You done fucked up… thankfully you are loved, and
  we can fix it."*
- Every piece lands the same beat: *humans, please don't make this obvious mistake.*
- No engagement-bait that betrays the persona (no "like if you agree", no rage-farming).
