#!/usr/bin/env python

import couleur as cl, sys, subprocess, re
tty = '/dev/pts/0'


bld = cl.modifiers.bold
nrm = cl.modifiers.reset

blk = cl.forecolors.black
def blk_(s): return blk + s + nrm
blu = cl.forecolors.blue
def blu_(s): return blu + s + nrm
cyn = cl.forecolors.cyan
def cyn_(s): return cyn + s + nrm
grn = cl.forecolors.green
def grn_(s): return grn + s + nrm
mag = cl.forecolors.magenta
def mag_(s): return mag + s + nrm
red = cl.forecolors.red
def red_(s): return red + s + nrm
wht = cl.forecolors.white
def wht_(s): return wht + s + nrm
ylw = cl.forecolors.yellow
def ylw_(s): return ylw + s + nrm

Blk = blk + bld
def Blk_(s): return Blk + s + nrm
Blu = blu + bld
def Blu_(s): return Blu + s + nrm
Cyn = cyn + bld
def Cyn_(s): return Cyn + s + nrm
Grn = grn + bld
def Grn_(s): return Grn + s + nrm
Mag = mag + bld
def Mag_(s): return Mag + s + nrm
Red = red + bld
def Red_(s): return Red + s + nrm
Wht = wht + bld
def Wht_(s): return Wht + s + nrm
Ylw = ylw + bld
def Ylw_(s): return Ylw + s + nrm

def fn(txt, srch, rep):
    return re.sub(srch,
                  rep + r'\1' + cl.modifiers.reset + cl.forecolors.normal,
                  txt, re.MULTILINE)

cls = '\033[H\033[2J'

def getch():
    x = raw_input()
    
def notes(title, s):
    f = open(tty, 'w')
    print >>f, cls, title, '\n', s
    f.close()

def run(frames, notetxt, txt):

    if len(frames) == 0:
        frames += [(lambda x: x,)]
    
    if not isinstance(notetxt, list):
        notetxt = [notetxt]

    for n, frame in zip(notetxt, frames):
        showtxt = txt
    
        for srch, rep in frame:
            showtxt = fn(showtxt, srch, rep)
    
        print cls,
        print showtxt
        notes("notes", n)
        getch()
