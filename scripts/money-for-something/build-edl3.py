#!/usr/bin/env python3
"""Money For Something, cut 3 (cut 2 tightened after watching its render): placements snapped to 1/24 s. Each round is: title card, the host asks, the record
(archive + narrator), the room answers. Room lines are trimmed to the words: in 0.15 s before the first sound
(silencedetect), out 0.25 s after the last word (faster-whisper word times). Writes edl3.json."""
import json,os
F=24; snap=lambda t: round(t*F)/F
E=[]; T=0.0
def put(item,i,o,v=0,a=0,at=None):
    global T; d=snap(o-i); E.append([item,round(snap(T if at is None else at),4),round(snap(i),4),round(d,4),v,a])
    if at is None: T=snap(T+d)
room=lambda n,i,o: put('L-'+n+'.mp4',i,o)
pic=lambda n,d: put(n+'.mp4',0,d)
def narr(n,at,d): put(n+'.wav',0,d,0,1,at); return at+d
M=[]; mark=lambda n: M.append([round(snap(T),4),n])
mark('1 Cold open'); pic('g01-may-quote',3.6); s=T; pic('g01-may-2016',4.7); narr('line-s01-nice-try',s+0.15,4.44)
mark('2 Titles'); room('s02-00-wide',0.2,1.8); room('s02-01-host-title',0.9,5.7)
mark('3 Meet the panel'); room('s03-01-host-card-british',0.85,6.25); room('s03-02-british-silent',0.6,1.7); room('s03-03-host-card-german',0.0,5.05); room('s03-04-german-silent',0.4,1.5); room('s03-05-host-card-politician',0.0,3.75); room('s03-06-politician-silent',1.2,2.5)
mark('4 Round 1'); pic('c-r1',1.0); room('s04-01-host-round-one',0.8,4.15); s=T; pic('g04a-kitchener',3.0); pic('g04b-somme-men-walking',3.0); pic('g04c-trench',3.0); narr('line-s04-nineteen-fourteen',s+0.15,8.64)
room('s04-02-british-duke',1.28,4.25); room('s04-03-german-bosnia',0.82,5.2); room('s04-04-british-france',0.94,2.75); room('s04-05-host-who-paid',0.0,2.9); room('s04-06-host-lives',1.9,3.6); room('s04-07-stare',0.5,2.8); room('s04-08-politician-watch',1.6,3.0)
mark('5 Round 2'); pic('c-r2',1.0); room('s05-01-host-afford',0.88,3.85); s=T; pic('g05a-war-loan-poster',2.2); pic('g05b-shells',2.3); pic('g05c-shell-warehouse',2.2); narr('line-s05-nobody-asked-take3',s+0.15,6.36); room('s05-02-politician-shake',1.0,4.7)
mark('6 Round 3 (PLACEHOLDER pictures)'); pic('c-r3',1.0); room('s06-01-host-homes',0.25,3.55); s=T; pic('g06a-PLACEHOLDER-men-resting',4.3); pic('g06b-PLACEHOLDER-1931-unemployed',4.3); narr('line-s06-despite-the-debt',s+0.15,8.28)
room('s06-02-politician-no-money',0.0,2.2); room('s06-03-british-some-on-it',2.0,3.45); room('s06-04-politician-spoken-for',3.15,4.85)
mark('7 Quick-fire'); pic('c-qf',1.0); room('s07-01-host-quickfire',0.8,6.0); room('s07-02-host-rules',0.0,6.95)
s=T; pic('g07a-berlin-1923',1.9); narr('line-s07a-shake',s+0.25,1.36); room('s07-03-german-wheelbarrows',2.05,5.0)
s=T; pic('g07b-london-1931',2.0); narr('line-s07b-starve-take2',s+0.25,1.52)
mark('7c NEEDS NARRATOR: Then another war. And the money was found. Obviously. (caption stands in)'); pic('g07c-1939-b',2.3)
mark('8 The star prize (narrator still says the old wording; two new lines to render)'); pic('c-sp',1.0); s=T
for n,d in [('g08a-guardsmen-building',4.6),('g08b-new-town-houses-b',5.0),('g08c-hospital-b',5.0),('g08d-houses-b',4.6)]: pic(n,d)
t=narr('line-s08a-nineteen-forty-eight',s+0.15,7.84); t=narr('line-s08b-built-the-houses',t+0.35,6.8); narr('line-s08c-done-once',t+0.35,3.4)
room('s08-01-plant',0.5,3.6)
mark('9 Sound Off (stills stand in for muted news clips)'); pic('c-so',1.0)
for (i,o),g in zip([(0.55,1.75),(3.1,4.3),(4.75,6.0)],['g09a-2008','g09b-2010','g09c-2020']):
    s=T; room('s09-01-host-dubs',i,o); put(g+'.mp4',0,o-i,1,0,s)
room('s09-02-politician-catches',2.6,5.4); room('s09-03-british-what-build',0.9,2.9); room('s09-04-host-house-prices',1.65,3.1); room('s09-05-politician-pockets',2.8,5.0); room('s09-06-host-minds-up',1.25,3.65)
mark('10 Final scores'); pic('c-fs',1.0); s=T; pic('g10a-may-2017',2.0); narr('line-s10-what-happened-next',s+0.15,1.68); pic('g10b-caption-dup',3.0)
room('s09-05-politician-pockets',5.5,6.7); room('s10-01-soldiers-hands',2.5,4.5); room('s10-02-host-next-time',1.3,2.95); room('s10-03-empty-room',0.0,3.0)
put('roomtone.wav',0,T,0,2,0)
H=os.path.dirname(os.path.abspath(__file__)); json.dump(dict(entries=E,markers=M,total=T),open(H+'/edl3.json','w'),indent=0)
print(len(E),'placements',round(T,2),'s'); h=len(E)//2
for b in (E[:h],E[h:]): print(json.dumps(b,separators=(',',':'))); print()
print(json.dumps(M,separators=(',',':')))
