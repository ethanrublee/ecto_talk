#!/usr/bin/env python

import sys, subprocess

s, outdir = sys.argv[1], sys.argv[2]
l = {}
m = __import__(s, globals=globals(), locals=l)

f = open(s + '.dot', 'w')
print >>f, m.__dict__['plasm'].viz()
f.close()
subprocess.check_call(['dot', '-Tpdf',
                       s + '.dot',
                       '-o', outdir + '/' + s + '-graph.pdf'])
