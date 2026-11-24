---
engine: claude
model: claude-sonnet-5-5
effort: high
labels: role=demo,step=clerk
include: demo
---
# Your step: the clerk (stage `case`)

You set up the day: a real topic from the news, and a made-up case built so the day's chosen ending can
be reached honestly.

## 1. Stop if the day has started

Run `$DEMO find $DAYS $NEWS`. If a file exists, say so in one line and stop. Run `$DEMO plan $NEWS` for
AREA and ENDING.

## 2. Find the real topic

- `memory_search` with `label_selector: "kind=news-digest,date=<NEWS>"`, then `memory_get` it.
- Pick the UK item that best fits AREA (housing, health, education, work, energy, transport, crime). Use
  `memory_get` on the item for its sources. Prefer a big, familiar topic people care about.
- Open the source URL. Use only what the page says. A page that won't open is not a source.
- No fitting item that day: take the closest UK item and say why in `case.in_the_news.why`.

## 3. Make up the case

Invent one place and one concrete choice it faces that plays out the real topic. Examples: a made-up
town, a made-up hospital trust, a made-up bus company or a made-up school. Mark the place as made up,
e.g. `Fernbridge (made up)`. Name no real person or company. Use invented numbers, except for up to four
real figures in `case.facts`, each with its source.

Build the case for ENDING. This is the fixture: write it so the honest marks can land there.

- **accepted:** a choice where a careful plan can meet everything people will ask for. There is enough
  money, the trade-offs are mild, and there is a known way to do it.
- **partly:** there is a real tension, so a good plan can keep within the red lines but can't promise
  everything, such as speed against cost, or one group's gain against another's wait. Build it in as hard numbers in the
  story (e.g. the fund covers 1,200 of the 1,500 homes at the level they need), and put in `tests_hint`
  one thing people will rightly ask for that those numbers rule out inside the red lines ("every one of
  the 1,500 homes gets the full amount"). A careful answer keeps every limit and misses that test.
- **rejected:** a hard bind. Every obvious route crosses something people won't accept, such as a fixed
  budget where saving money means a closure and keeping it open means a tax rise. The story says so
  plainly. Put the bind itself in `tests_hint` as a red line ("the books must balance"), next to the
  red lines each route crosses, so no answer can keep every limit by leaving the bind unsolved.

## 4. Write the file

Path: `$DAYS/<NEWS>/<NEWS>-<slug>.json` (slug: 2 to 4 lowercase words). Fill:

- `schema: "fp-demo/1"`, `id`, `stage: "case"`.
- `run`: `{mode: "daily"|"backfill", run_date: RUN, news_date: NEWS}`.
- `plan`: `{area: AREA, ending: ENDING}`.
- `case`:
  - `title`: up to 80 characters;
  - `short`: up to 22 characters, CAPITALS;
  - `question`: the one choice, in plain words;
  - `place`;
  - `story`: 3 to 5 sentences, up to 900 characters, saying what the place faces;
  - `in_the_news`: `{headline, why, memory_id, sources}`, where `why` is one sentence linking the case to
    the real story;
  - `facts`.
- `sources`: `s1`, `s2`, …, each with `title`, `publisher`, `date` and `url`.
- `made_by`: `{workers: ["demo-clerk"]}`.

Also write `<id>.side.clerk.json`, the design notes that only the citizens, the bench and `demo-redo`
read, never the gate:

- `design`: two or three sentences on how the case is built to reach ENDING;
- `tests_hint`: the kinds of tests and red lines citizens in that place would set;
- `angles`: three different directions for answers A, B and C, each up to 60 characters.

## 5. Validate, commit, push

Finish with one line: `<id>: <short> (<AREA>, <ENDING>)`.
