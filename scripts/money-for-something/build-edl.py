#!/usr/bin/env python3
"""Money For Something: the first cut as a list of placements, snapped to 1/24 s. Writes edl.json for the Premiere
eval in the ledger. v/a are 0-based track indices; kind 'a' is an audio-only narrator line."""
import json,os
F=24; snap=lambda t: round(t*F)/F
E=[]; T=0.0
def room(name,i,o):
    global T; d=snap(o-i); E.append(dict(item=name+'.mp4',start=snap(T),inp=snap(i),dur=d,v=0,a=0,kind='v')); T=snap(T+d)
def foot(name,d):
    global T; d=snap(d); E.append(dict(item=name+'.mp4',start=snap(T),inp=0,dur=d,v=0,a=0,kind='v')); T=snap(T+d)
def narr(name,at,d): E.append(dict(item=name+'.wav',start=snap(at),inp=0,dur=d,v=0,a=1,kind='a')); return at+d
def over(name,at,d): E.append(dict(item=name+'.mp4',start=snap(at),inp=0,dur=snap(d),v=1,a=0,kind='v'))
M=[]
def mark(name): M.append((snap(T),name))
mark('1 Cold open'); foot('f01a-may-2017',3.0); s=T; foot('f01b-may-2016',4.7); narr('line-s01-nice-try',s+0.2,4.44)
mark('2 Titles'); room('s02-00-wide',0,3.0); room('s02-01-host-title',0.6,6.0)
mark('3 Meet the panel'); room('s03-01-host-card-british',0.6,6.6); room('s03-02-british-silent',0.5,3.0); room('s03-03-host-card-german',0.0,5.4); room('s03-04-german-silent',0.3,3.0); room('s03-05-host-card-politician',0.0,4.0); room('s03-06-politician-silent',1.0,3.5)
mark('4 How did it start'); s=T; foot('f04a-kitchener',2.2); foot('f04b-britain-needs-you',1.6); foot('f04c-somme-men-walking',2.6); foot('f04d-trench',2.6); narr('line-s04-nineteen-fourteen',s+0.2,8.64)
room('s04-01-host-round-one',0.5,4.4); room('s04-02-british-duke',1.0,4.4); room('s04-03-german-bosnia',0.5,5.5); room('s04-04-british-france',0.6,3.0); room('s04-05-host-who-paid',0.0,2.8); room('s04-06-host-lives',0.8,4.3); room('s04-07-stare',0.5,5.5); room('s04-08-politician-watch',1.0,4.5)
mark('5 Can we afford it'); s=T; foot('f05a-war-loan-poster',2.2); foot('f05b-shells',2.2); foot('f05c-shell-warehouse',2.3); narr('line-s05-nobody-asked-take3',s+0.2,6.36)
room('s05-01-host-afford',0.6,3.9); room('s05-02-politician-shake',0.0,5.0)
mark('6 What happened next (PLACEHOLDER pictures)'); s=T; foot('f06a-PLACEHOLDER-somme-men-resting',3.0); foot('f06b-PLACEHOLDER-1949-queue',2.7); foot('f06c-PLACEHOLDER-1931-unemployed',2.9); narr('line-s06-despite-the-debt',s+0.2,8.28)
room('s06-01-host-homes',0.0,3.9); room('s06-02-politician-no-money',0.0,2.6); room('s06-03-british-some-on-it',1.6,3.5); room('s06-04-politician-spoken-for',2.6,5.0)
mark('7 Shake, Starve or Plant'); room('s07-01-host-quickfire',0.5,4.8); room('s07-02-host-rules',0.0,7.3)
s=T; foot('f07a-berlin-bread-van-1923',2.0); narr('line-s07a-shake',s+0.3,1.36); room('s07-03-german-wheelbarrows',1.2,5.4)
s=T; foot('f07b-london-unemployed-1931',2.0); narr('line-s07b-starve-take2',s+0.3,1.52)
mark('7c NEEDS NARRATOR LINE: Then another war. And the money was found. Obviously.'); foot('f07c-next-war-paratroops',2.8)
mark('8 Plant (two new narrator lines still to render)'); s=T
for n,d in [('f08a-new-town-houses',3.0),('f08b-guardsmen-building',2.6),('f08c-houses-cartoon',3.0),('f08d-new-town-roads',3.0),('f08e-hospital-cartoon',3.0),('f08f-repairing-housing',2.2),('f08g-training',2.4)]: foot(n,d)
t=narr('line-s08a-nineteen-forty-eight',s+0.2,7.84); t=narr('line-s08b-built-the-houses',t+0.35,6.8); narr('line-s08c-done-once',t+0.35,3.4)
room('s08-01-plant',0.0,6.5)
mark('9 Sound Off'); s=T; room('s09-01-host-dubs',0.4,6.3); over('f09a-lehman-2008',s+0.3,2.4); over('f09b-budget-2014',s+2.7,1.7); over('f09c-press-conference-2020',s+4.4,1.25)
room('s09-02-politician-catches',1.5,7.0); room('s09-03-british-what-build',0.0,4.2); room('s09-04-host-house-prices',1.3,3.6); room('s09-05-politician-pockets',2.5,5.5); room('s09-06-host-minds-up',0.9,3.8)
mark('10 Final scores'); s=T; foot('f10a-may-2017',2.2); narr('line-s10-what-happened-next',s+0.25,1.68); foot('f10b-caption-dup',4.0)
room('s09-05-politician-pockets',5.5,7.5); room('s10-01-soldiers-hands',2.0,6.0); room('s10-02-host-next-time',1.0,3.3); room('s10-03-empty-room',0.0,6.0)
H=os.path.dirname(os.path.abspath(__file__))
json.dump(dict(entries=E,markers=M,total=T),open(H+'/edl.json','w'),indent=1)
print(len(E),'placements', round(T,2),'s'); 
