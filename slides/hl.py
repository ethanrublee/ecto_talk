#!/usr/bin/env python

import couleur as cl, sys, subprocess, re
tty = '/dev/pts/0'


blk = cl.forecolors.black
blu = cl.forecolors.blue
cyn = cl.forecolors.cyan
grn = cl.forecolors.green
mag = cl.forecolors.magenta
red = cl.forecolors.red
wht = cl.forecolors.white
ylw = cl.forecolors.yellow

bld = cl.modifiers.bold
nrm = cl.modifiers.reset

Blk = blk + bld
Blu = blu + bld
Cyn = cyn + bld
Grn = grn + bld
Mag = mag + bld
Red = red + bld
Wht = wht + bld
Ylw = ylw + bld

def fn(txt, srch, rep):
    return re.sub(srch,
                  rep + r'\1' + cl.modifiers.reset + cl.forecolors.normal,
                  txt, re.MULTILINE)

def cls():
    subprocess.check_call(['tput', 'clear'])

def getch():
    x = raw_input()
    
def notes(s):
    f = open(tty, 'w')
    print >>f, '\033[H\033[2J'
    print >>f, s
    f.close()

def run(frames, notes, txt):

    if len(frames) == 0:
        frames += [(lambda x: x,)]
    
    for frame in frames:
        showtxt = txt
    
        for srch, rep in frame:
            showtxt = fn(showtxt, srch, rep)
    
        cls()
        print showtxt
        getch()
