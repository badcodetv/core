#!/bin/bash
# Draws the link-preview picture for badcode.tv/future-proof/live/ (1200x630). It must say SIMULATED.
#   bash scripts/government/sim/preview.sh   (needs ImageMagick 6 and the Liberation fonts)
set -e
out="$(dirname "$0")/../../../apps/site/public/future-proof/live/preview.png"
convert -size 1200x630 xc:'#0f151c' \
  -fill none -stroke '#f07d74' -strokewidth 8 -draw "rectangle 24,24 1176,606" -stroke none \
  -font Liberation-Sans-Bold -fill '#f07d74' -pointsize 120 -draw "rotate -3 text 80,230 'SIMULATED'" \
  -font Liberation-Sans-Bold -fill '#e7ecf2' -pointsize 84 -annotate +80+380 'Future Proof Live' \
  -font Liberation-Sans -fill '#9aa7b6' -pointsize 34 -annotate +80+450 'One real UK news story a day, round the loop.' \
  -annotate +80+500 'AI stand-ins for citizens, drawn by lot. Not real people.' \
  -font Liberation-Mono-Bold -fill '#f0a24a' -pointsize 30 -annotate +80+568 'BADCODE.TV  ·  SIMULATED' \
  "$out"
echo "$out"
