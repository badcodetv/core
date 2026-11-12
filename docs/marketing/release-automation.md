# Release automation: one post, every platform, wired into Claude

Kai, 2026-11-12: "it's really, really useful how we've automated YouTube … if we were able to kind of, say,
make a post, that that means publish it on YouTube and Instagram and everything else, TikTok … and with the
music, SoundCloud, Spotify … it feels like we have more flexibility over such tools if we wire them directly
into you."

Status: **parked by Kai, 2026-11-12. YouTube first.** Researched 2026-11-12 (two marketing-researcher passes,
about 25 searches); nothing built.

## Kai's ruling (2026-11-12)

"Let's stick to YouTube for the moment … once we come to it, we will build a release tool that will combine
automatic APIs with then manual instructions … I'll come back to this thread once we've got all the actual
content onto YouTube. And then from there, we can use that as a reference for what we're actually publishing
elsewhere."

- **Now:** get all the content onto YouTube, through the `youtube` MCP and the `youtube-channel` skill.
- **Later:** one **release tool** that, per platform, either posts through the official API (where this page
  says it can) or writes the exact manual steps for a person to follow (TikTok, the distributor, Spotify's
  pitch). Built once the YouTube channel is full.
- **YouTube is the reference:** what's on the channel (`docs/youtube/channel.json`) is the list of what gets
  published elsewhere, and its titles, descriptions and AI line are the starting words for each platform.
- Re-check this page's facts when the work restarts: platform rules move fast (TikTok's rules were updated
  2026-10-27; X's pricing changed in April 2026).
Tags: **confirmed** = read on the official page; **reported** = vendor or secondary page; **unclear**.

## The answer per platform

| Platform | How Claude posts | Human yes | AI label via API | Cost | Verdict |
| --- | --- | --- | --- | --- | --- |
| YouTube | our `youtube` MCP (official API) | uploads private, a human goes public | `containsSyntheticMedia` | free | ✅ done 2026-11-11 |
| Facebook Page | Meta Graph API, Reels `/{page-id}/video_reels` | `video_state` = `DRAFT` or `SCHEDULED` (10 min to 29 days ahead) (confirmed) | `is_ai_generated` (confirmed) | free | **wire it** (one Meta app) |
| Instagram `@badcode.tv` | Graph API content publishing: Reels, images, carousels, stories, trial reels (confirmed) | no draft state: Claude asks before the publish call | `is_ai_generated` (confirmed) | free | **wire it**, same Meta app |
| Threads | Threads API (confirmed) | Claude asks first | `is_made_with_ai` (confirmed) | free | wire after Instagram |
| TikTok | Content Posting API | inbox upload = a draft a human finishes in the app | `is_aigc` on Direct Post only (confirmed) | free | **manual now** (see below) |
| X `@badcode.tv` | X API v2, pay per use | Claude asks first | none found | $0.015 a post, **$0.20 with a link** (confirmed) | parked (plan says not now) |
| Bluesky | AT Protocol, app password | Claude asks first | none found | free | optional, an afternoon |
| Spotify, Apple Music… | **no upload API exists** (confirmed); only via a distributor | a human submits | DDEX AI credits on the distributor's form | DistroKid yearly fee | **Claude prepares, human submits** |
| SoundCloud | self-serve upload API since mid-2026, **needs Artist Pro** (reported) | Claude asks first | none found | Artist Pro subscription | later; it won't monetise Suno tracks anyway (reported) |

### TikTok is the hard one (confirmed, developers.tiktok.com content-sharing guidelines)

- An unaudited app can only post **privately**, and only to a private account.
- The audit **rejects exactly what we'd build**: "a utility tool to help upload contents to the account(s) you
  or your team manages" is listed as not acceptable.
- The draft route (`video.upload` → the TikTok inbox, a human posts in the app) still needs a review; whether a
  team-only tool passes it is unclear.
- So the options are: post by hand in TikTok Studio, or post through a tool that already holds an audited app
  (Upload-Post from about $16–24 a month, Postiz hosted about $23–31 a month, Ayrshare $149; reported, vendor pages).

### Music (reported unless marked)

- Spotify has no upload API (confirmed, developer.spotify.com). Releases go through a distributor.
- DistroKid has no official API; it takes AI music if declared, rights held, no voice cloning. LabelGrid
  ($139/month) and Revelator ($249/month) have APIs; too dear for us.
- TuneCore and CD Baby: sources contradict on Suno. Suno v6 is licensed (Warner, BMG; 2026-09-09), so old
  "blocks Suno" notes may be stale. Ask each distributor before relying on it.
- Suno: commercial rights only for songs made **on a paid plan**, and that is a licence, not ownership. Keep
  proof of the plan per track; the distributor makes a person warrant the rights.
- Spotify editorial pitch: at least 7 days before release, 2–4 weeks advised, one song at a time, a form with
  no API.
- **What a person must do:** accept terms and pay, sign the rights and AI declaration, approve the artwork,
  pitch in Spotify for Artists, click submit. **What Claude can do:** the release pack (WAV master, 3000×3000
  artwork, metadata with AI credits, release date 2–4 weeks out, pitch text) and fill the form in a browser
  for you to check.

## Own wiring or a tool?

**Hybrid.** Own wiring wherever an official free API lets our own app post to our own accounts (YouTube, the
Meta three, Bluesky). That keeps our habits: private or draft first, the AI flag always on, every post in a
log, a human yes. A paid tool only for what our own app can't get (TikTok's audit), and only if posting by
hand turns out to be the bottleneck.

## Automation shape

- **Trigger:** Kai or Jack says "release <thing>" (a finished cut or song).
- **Steps:** delivery QC → words drafted and gatekept (the `youtube-channel` loop, per platform) → each
  platform gets the native file, caption and AI flag, as a **draft / scheduled / held** post → one page
  listing every held post → a person says yes → Claude publishes the held ones and logs the links.
- **Human gate:** always (chief-of-staff rule 3). Facebook keeps it natively (`DRAFT`); Instagram and Threads
  hold on our side; TikTok and the distributor are a human tap by design.

## Before the Meta tool can work

- The Facebook Page runs from Jack's personal profile, so **Jack must be a developer on the Meta app, or add
  Kai as a Page admin**, before a Page token can be issued (inference from Meta's Page-token rule).
- Instagram must be a Business or Creator account, added to the app as a tester.
- Instagram fetches the video from a **public URL**, so we need a short-lived link (e.g. Cloudflare).
- Facebook Reels are **3–90 seconds**; longer shorts need another route.

## Corrections to older docs

- `platform-playbooks.md` §6–8: the Meta APIs are free (it said "nothing verified" / "write access is paid");
  X is pay per use at the prices above.
- `shorts-release.md` §3: trial reels and the AI flag are in the Instagram API; Facebook collaborator invites
  are in the Reels API. Its "posting tool" question is answered here.

## Open questions

- Does Meta really need no app review for our own Page and account? Vendor claim only; try in development mode.
- Meta and TikTok token lifetimes; Instagram reel length, cover frame and scheduling through the API.
- Would TikTok accept a team-only `video.upload` (inbox) app?
- Do the cross-post tools post natively, and does their AI flag actually show? Test one before paying.
- Which distributors accept Suno v6 today, in their own words.
