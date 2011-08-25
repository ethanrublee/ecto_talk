#!/usr/bin/env python
import ecto
import ecto_test
import sys

def build_addergraph(nlevels, cellsperlevel):
    
    plasm = ecto.Plasm()

    generators = [ecto_test.Generate("Gen%u" % x) for x in range(cellsperlevel)]

    prevlevel = [ecto_test.LatticeSleep("Sleepy_0_%u"% y, n=cellsperlevel) for y in range(cellsperlevel)]

    for n, gen in enumerate(generators):
        for s in prevlevel:
            plasm.connect(gen["out"] >> s["in%u" % n])

    for k in range(1,nlevels):
        nextlevel = [ecto_test.LatticeSleep("Sleepy_%u_%u" % (k, y), n=cellsperlevel) for y in range(cellsperlevel)]
        for j in range(cellsperlevel):
            for k in range(cellsperlevel):
                print "%u_%u => %u_%u" % (j, j, k, j)
                plasm.connect(prevlevel[j]["out%u" % j] >> nextlevel[k]["in%u" % j])
        prevlevel = nextlevel            

    gather = ecto_test.Gather_double("Gather", n=cellsperlevel)

    for n, lat in enumerate(prevlevel):
        plasm.connect(lat['out%u' % n] >> gather["in_%04u" % n])

    printer = ecto_test.Printer("printy!")
    plasm.connect(gather, "out", printer, "in")

    return plasm

def test_plasm(nlevels, cellsperlevel, niter):
    plasm = build_addergraph(nlevels, cellsperlevel)

    suffix = '%ulvls_%uperlevel_%uiter' %(nlevels, cellsperlevel, niter)
    o = open('graph_%s.dot' %suffix , 'w')
    print >>o, plasm.viz()
    o.close()
    ecto.view_plasm(plasm)
    sched = ecto.schedulers.Threadpool(plasm)
    sched.execute(niter)

if __name__ == '__main__':

    test_plasm(6, 5, 7)




