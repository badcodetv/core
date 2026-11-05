# Statements

Draft social media posts from the cabinet. **Nothing here posts itself.** Kai or Jack post a
statement by hand, or hand it to the marketing `chief-of-staff` skill (which runs it past the
gatekeeper first).

## Where they go

One file per minister per day:

```
docs/government/statements/YYYY-MM-DD/<post>.md
```

`<post>` is the minister's key: `prime-minister`, `chancellor`, `foreign`, `home`, `education`,
`defence`, `health`, `work-pensions`, `housing`, `energy-climate`. The cabinet writes them on the
rolling PR (`government/rolling`); they reach `main` only when a person merges it.

## The format

```markdown
---
platform: x
status: draft
answers: <news memory id>, <news memory id>
---
The post text, exactly as it would go out.
```

- `platform`: one of `x`, `instagram`, `tiktok`, `youtube`, `any`. `any` means the words work
  anywhere; the person posting fits them to the platform.
- `status`: `draft` when written. Only a person changes it.
- `answers`: the Bob `kind=news` memory ids the statement responds to, comma-separated. Every claim
  about the world in the post must be backed by a source in one of those memories.
- The text: in the minister's voice, short enough to quote. For `x`, at most 280 characters. For
  `youtube` or `tiktok`, a spoken script of at most 120 words. No hashtag walls, no calls to vote,
  donate or sign up.

## Marking one as posted

After posting, edit the file (a normal PR, or a fix pushed to the rolling branch):

```markdown
---
platform: x
status: posted
answers: <ids>
url: https://x.com/…/status/…
---
```

If the posted words differ from the draft, put the words that actually went out in the file. A
statement nobody posts simply stays `draft`; that is fine.
