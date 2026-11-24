#!/bin/bash
# Draws the link-preview picture for badcode.tv/demo/ (1200x630). It says "THIS IS A DEMO".
#   bash scripts/demo/preview.sh   (needs ImageMagick 6 and the Liberation fonts)
set -e
out="$(dirname "$0")/../../apps/site/public/demo/preview.png"
mkdir -p "$(dirname "$out")"
convert -size 1200x630 xc:'#0f151c' \
  -fill none -stroke '#f0a24a' -strokewidth 8 -draw "rectangle 24,24 1176,606" -stroke none \
  -font Liberation-Mono-Bold -fill '#f0a24a' -pointsize 44 -annotate +80+130 'THIS IS A DEMO' \
  -font Liberation-Sans-Bold -fill '#e7ecf2' -pointsize 96 -annotate +80+260 'Future Proof Demo' \
  -font Liberation-Sans -fill '#9aa7b6' -pointsize 36 -annotate +80+340 'A made-up case on a real news topic, every day.' \
  -annotate +80+392 'Made-up citizens set the tests. AI answers are marked.' \
  -fill '#7cc49a' -font Liberation-Sans-Bold -annotate +80+470 'Accepted' -fill '#f0a24a' -annotate +300+470 'A trial' -fill '#f07d74' -annotate +480+470 'Sent back' \
  -font Liberation-Mono-Bold -fill '#9aa7b6' -pointsize 28 -annotate +80+568 'BADCODE.TV/DEMO  ·  A GOVERNMENT BUILT FROM THE BOTTOM UP' \
  "$out"
echo "$out"
