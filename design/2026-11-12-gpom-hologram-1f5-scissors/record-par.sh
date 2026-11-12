#!/bin/bash
# record-par.sh <url> <outdir> <frames-dir-name> <jobs> [record.mjs args...]
# Every frame is a pure function of t, so the film splits into <jobs> stretches recorded by separate headless browsers at once,
# each writing its frames under their global numbers into the same folder. Kai, 10 Nov: "parallel rendering sounds like a useful thing".
# 32 cores / ~15 GB free here: 4 jobs is safe. Logs: <outdir>/record-par-<k>.log
set -e
URL=$1; OUT=$2; FR=$3; J=$4; shift 4
D=$(cd "$(dirname "$0")" && pwd)
N=$(node -e "
const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({executablePath:'/usr/bin/google-chrome',headless:true,args:['--use-angle=swiftshader','--enable-unsafe-swiftshader']});
const p=await b.newPage();await p.goto('$URL',{waitUntil:'networkidle'});await p.waitForFunction(()=>window.hologram&&window.hologram.TD>0,null,{timeout:60000});
console.log(Math.ceil((await p.evaluate(()=>window.hologram.TD))*24));await b.close()})()")
echo "frames $N in $J jobs"
for ((k=0; k<J; k++)); do
  A=$(( N*k/J )); Z=$(( N*(k+1)/J ))
  node "$D/record.mjs" "$URL" "$OUT" --frames "$FR" --range $A:$Z "$@" > "$OUT/record-par-$k.log" 2>&1 &
done
wait
C=$(ls "$OUT/$FR" | wc -l); echo "recorded $C of $N"; [ "$C" -ge "$N" ]
