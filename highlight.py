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

def _(srch, *attrs):
    def impl(txt):
        return re.sub(srch,
                      ''.join([lookups[x] for x in attrs]) + r'\1' + cl.modifiers.reset + cl.forecolors.normal,
                     txt, re.MULTILINE)
    return impl

m = {}
m['_'] = _
for l in lookups:
    m[l.__name__] = l
execfile(sys.argv[1], m)
f = open(m['fname'])
txt = f.read()

if len(m['hl']) == 0:
    m['hl'] += [(lambda x: x,)]

if not type(m['hl']) == list:
    m['hl'] = m['hl']



for frame in m['hl']:
    subprocess.check_call(['tput', 'clear'])
    showtxt = txt

    if 'after' in m:
        srch = re.search(m['after'], showtxt)
        if srch:
            showtxt = showtxt[srch.end():]

    if 'until' in m:
        srch = re.search(m['until'], showtxt)
        if srch:
            showtxt = showtxt[:srch.start()]

    for fn in frame:
        showtxt = fn(showtxt)

    print showtxt
    x = raw_input()
