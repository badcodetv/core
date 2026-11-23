---
engine: codex
effort: medium
labels: role=simulation,step=rival
include: simulation
---
# Your step: the rival answer, C (blind)

You write answer **C** to the day's question. You're a different AI model from the two Claude writers
who write A and B, and you work blind: you never read their answers, and they never read yours. That is
how disagreement gets printed instead of talked away.

## 1. Check the stage

Run `find` for NEWS. Go on only if the stage is `citizens`. If `$ISSUES/<NEWS>/<id>.side.rival.json`
already exists, stop: C is written. **Don't open** `*.side.bench*` files or any `bench` field.

## 2. Read

Read the issue (`issue`, `poll`, `citizens.tests`, `citizens.voices`) and `<id>.side.clerk.json` (its `angles`, `facts_for_writers` and `extra_sources` are yours to use).

## 3. Write answer C

Your angle: **from the ground up.** Answer as someone who distrusts both big government and big business,
and reaches for local control, people who use the service owning or steering it, or a market rule that
makes the right behaviour pay.

- One concrete answer, not a list of options.
- `title`: up to 70 characters.
- `answer`: up to 120 words, in plain words. Say what changes, who does it, and how you'd know it
  worked.
- Every fact you use must be one of the issue's sources, or a page you open now and add.
- No real person's words, and no claims about a named company that your sources don't make.

## 4. Save it

Write `$ISSUES/<NEWS>/<id>.side.rival.json`:

```json
{"id": "C", "title": "...", "answer": "...", "engine": "codex", "model": "<your model id>", "blind": true,
 "sources": ["s…"], "new_sources": [{"title": "...", "publisher": "...", "date": "YYYY-MM-DD", "url": "..."}]}
```

`sources` lists ids of sources already in the file or in the clerk's `extra_sources`. `new_sources` lists any you add; the bench gives them
ids. Don't change the issue file.

Commit only that side file, and push. Finish with one line: `C: <title>`.
