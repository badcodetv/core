# Bob configuration

This folder configures a [Bob](https://github.com/badcodetv/bob) project. Bob reads it from
`main`; after pushing a change, press **Sync git** in Bob to pick it up.

```
workers/<name>.md         one file per worker; the file name is the worker's name
skills/<name>/SKILL.md    skills every worker in this project can use (optional)
```

A worker file is YAML front matter, then the worker's system prompt:

```markdown
---
engine: claude            # claude (codex and opencode are coming)
model: claude-sonnet-5    # optional
effort: low               # optional: low, medium, high, xhigh, max
tools: [Read, Grep]       # optional: tools allowed without asking; omit for the default set
---
You are …
```

Never put a secret in this folder. The repository is public.
