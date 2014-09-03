#!/usr/bin/env python
f=open("accepted_hits.sam")
nl=0
for line in f:
    if "SRR" in line:
        nl=nl+1
print nl

18417196

f=open("accepted_hits.sam")
nl=0
for line in f:
    if "HI:i:0" in line:
        nl=nl+1
print nl

229352

f=open("accepted_hits.sam")
nl=0
for line in f:
    if "NH:i:1" in line:
        nl=nl+1
print nl

17444398



