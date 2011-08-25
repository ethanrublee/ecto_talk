#!/usr/bin/env python

import sys, re

processfname = sys.argv[1]
dotfname = sys.argv[2]

process = open(processfname).read()
dot = open(dotfname).read()

print len(process), len(dot)

data = []

onoff = set()

for l in process.splitlines():
    # print l
    (gah, modname, time, tick, on) = l.split(' ', 5)
    data += [(modname, int(time), int(tick), int(on))]
    
import re


def update():
    newdot = dot
    def subber(p):
        print "SUPPER!", p.groups()

    for active in onoff:
        print "subbing for", active
        # re.sub(r"^\d+\[label[^\]]+(" + active + ").*\];", subber, newdot, 1, re.MULTILINE)
        re.sub("(^\d+.*)(" + active + r')(.*)', subber, newdot, 1, re.MULTILINE)
        
        # print newdot
    
print data[:100]


prevtime = data[0][1]
maxsize = 0

for modname, time, tick, on in data[:4]:
    print time - prevtime
    prevtime = time
    if on:
        onoff.add(modname)
        if len(onoff) > maxsize:
            maxsize = len(onoff)
    else:
        onoff.remove(modname)

    update()
        

elapsed = data[-1][1] - data[0][1]
duration = 120
fps = 24
totalframes = duration*fps
frame_duration = elapsed/totalframes

print "maxsize =", maxsize
print "time = ", elapsed
print "time/frame = ", frame_duration

update
