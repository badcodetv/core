import { readFileSync } from 'node:fs'
const rows = readFileSync('m2sl.csv','utf8').trim().split('\n').slice(1)
  .map(l => { const [d,v] = l.split(','); return { d, v: Number(v) } })
  .filter(r => Number.isFinite(r.v))
const last = rows.at(-1), first = rows[0]
const pct = (a,b) => ((b/a - 1) * 100)

// annualised growth over trailing windows
const at = (n) => rows.at(-1-n)
const cagr = (n) => (Math.pow(last.v/at(n).v, 12/n) - 1) * 100
console.log(`series: ${first.d} ${first.v}  ->  ${last.d} ${last.v}  (${rows.length} obs)`)
console.log(`M2 CAGR  1y ${cagr(12).toFixed(2)}%  3y ${cagr(36).toFixed(2)}%  5y ${cagr(60).toFixed(2)}%  10y ${cagr(120).toFixed(2)}%  20y ${cagr(240).toFixed(2)}%  since1959 ${((Math.pow(last.v/first.v, 12/(rows.length-1))-1)*100).toFixed(2)}%`)

// monthly moves
const mom = rows.slice(1).map((r,i) => ({ d: r.d, p: pct(rows[i].v, r.v) }))
const sorted = [...mom].sort((a,b)=>a.p-b.p)
console.log(`monthly move: min ${sorted[0].p.toFixed(2)}% (${sorted[0].d})  max ${sorted.at(-1).p.toFixed(2)}% (${sorted.at(-1).d})  median ${sorted[Math.floor(sorted.length/2)].p.toFixed(3)}%`)
console.log(`negative months: ${mom.filter(m=>m.p<0).length} of ${mom.length} (${(100*mom.filter(m=>m.p<0).length/mom.length).toFixed(1)}%)`)

// the 2022-23 contraction
const peak = rows.reduce((a,b)=> b.v>a.v && b.d < '2023-01-01' && b.d > '2021-06-01' ? b : a, {v:0})
const after = rows.filter(r=>r.d>peak.d)
const trough = after.reduce((a,b)=> b.v<a.v ? b : a, after[0])
console.log(`2022 peak ${peak.d} ${peak.v}  -> trough ${trough.d} ${trough.v}  = ${pct(peak.v,trough.v).toFixed(2)}%  (${(trough.v-peak.v).toFixed(1)}B)`)

// rolling 36-month multiples: what a 3-year ENC asset holder gains, before costs
const win = 36
const mult = []
for (let i=win;i<rows.length;i++) mult.push({ d: rows[i].d, m: rows[i].v/rows[i-win].v })
const ms = [...mult].sort((a,b)=>a.m-b.m)
const q = (p) => ms[Math.floor(p*(ms.length-1))]
console.log(`rolling 3y multiple: min ${q(0).m.toFixed(3)}x (${q(0).d})  p25 ${q(.25).m.toFixed(3)}x  median ${q(.5).m.toFixed(3)}x  p75 ${q(.75).m.toFixed(3)}x  max ${q(1).m.toFixed(3)}x (${q(1).d})`)
console.log(`3y windows with a LOSS (multiple<1): ${mult.filter(x=>x.m<1).length} of ${mult.length}`)
const recent = mult.filter(x=>x.d>='2016-01-01')
console.log(`last 10y of 3y windows: min ${Math.min(...recent.map(x=>x.m)).toFixed(3)}x  max ${Math.max(...recent.map(x=>x.m)).toFixed(3)}x`)

// genesis supply
const k = 1e6, dec = 1e6
console.log(`genesis supply at ${last.d}: ${(last.v*k/dec).toLocaleString('en-US',{maximumFractionDigits:0})} whole ENC`)
