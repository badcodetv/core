# The demo step's common ground

You are one step of the Future Proof Demo (`docs/demo/README.md`), not the cabinet and not the
simulation. Ignore the cabinet's daily procedure above. Its voice and honesty rules still apply.

## Setup (same for every demo step)

```bash
git -C /project/work/core show origin/main:scripts/demo/bob-setup.sh | bash
MAIN=/project/work/.demo/main; LIVE=/project/work/.demo/live; DAYS=$LIVE/docs/demo/days
DEMO="node $MAIN/scripts/demo/demo.mjs"
```

Read `$MAIN/docs/demo/README.md` in full.

- **Dates:** the message that started you says either `Backfill: news_date=… run_date=…`, or nothing,
  in which case NEWS and RUN are both today (`TZ=Europe/London date +%F`).
- **Today's plan:** `$DEMO plan $NEWS` gives the area and the ending.
- **Today's file:** `$DEMO find $DAYS $NEWS` gives its path and stage.
