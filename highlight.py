#!/usr/bin/env python

import couleur as cl, sys, subprocess, re

class blue: pass
class cyan: pass
class green: pass
class magenta: pass
class normal: pass
class red: pass
class white: pass
class yellow: pass
class bold: pass

lookups = {blue : cl.forecolors.blue,
           cyan : cl.forecolors.cyan,
           red : cl.forecolors.red,
           green : cl.forecolors.green,
           yellow : cl.forecolors.yellow,
           white : cl.forecolors.white,
           bold : cl.modifiers.bold,
           }

def _(s, *attrs):
    def impl(txt):
        txt = re.sub(s, ''.join([lookups[x] for x in attrs]) + r'\1' + cl.modifiers.reset + cl.forecolors.normal,
                     txt, re.MULTILINE)
        return txt
    return impl

execfile(sys.argv[1])
f = open(fname)
txt = f.read()

if not type(hl) == list:
    hl = [hl]

for frame in hl:
    subprocess.check_call(['tput', 'clear'])
    showtxt = txt
    for fn in frame:
        showtxt = fn(showtxt)

    print showtxt
    x = raw_input()
