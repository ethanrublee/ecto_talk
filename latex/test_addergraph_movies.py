#!/usr/bin/env python
import ecto
import ecto_test
import sys

def build_addergraph(nlevels):
    
    plasm = ecto.Plasm()

    prevlevel = [ecto_test.Add("Add_%u" % x) for x in range(2**(nlevels-1))]
    ncell = 2**(nlevels-1)
    for adder in prevlevel:
        plasm.connect(
                      ecto_test.Generate("Generate_%u" % ncell, step=1.0, start=1.0)["out"] >> adder["left"],
                      ecto_test.Generate("Generate_%u" % (ncell+1), step=1.0, start=1.0)["out"] >> adder["right"]
                      )
        ncell += 2                      
                      
                      
    print "prev has", len(prevlevel)

    ncell = 0
    for k in range(nlevels-2, -1, -1):
        print "****** k=", k, " ***********"
        thislevel = [ecto_test.Add("Add_%u" % ncell) for x in range(2**k)]
        ncell += 1
        print "prevlevel=", prevlevel
        print "thislevel=", thislevel
        index = 0
        print "for...", range(2**k)
        for r in range(2**k):
            print "prev[%u] => cur[%u]" % (index, r)
            plasm.connect(prevlevel[index]["out"] >> thislevel[r]["left"])
            index += 1
            print "prev[%u] => cur[%u]" % (index, r)
            plasm.connect(prevlevel[index]["out"]>>thislevel[r]["right"])
            index += 1
        prevlevel = thislevel

    assert len(prevlevel) == 1
    final_adder = prevlevel[0]
    printer = ecto_test.Printer("printy!")
    #plasm.connect(final_adder, "out", printer, "in")

    return (plasm, final_adder)

def test_plasm(nlevels, nthreads, niter):
    (plasm, outnode) = build_addergraph(nlevels)

    #o = open('graph.dot', 'w')
    #print >>o, plasm.viz()
    #o.close()
    ecto.view_plasm(plasm)
    sched = ecto.schedulers.Singlethreaded(plasm)
    sched.execute(niter)

    print "RESULT:", outnode.outputs.out
    shouldbe = float(2**nlevels * niter)
    print "expected:", shouldbe
    assert outnode.outputs.out == shouldbe

if __name__ == '__main__':
    #test_plasm(1, 1, 1)
    #test_plasm(1, 1, 2)
    #test_plasm(5, 1, 1)
    #test_plasm(5, 2, 1)
    #test_plasm(5, 5, 5)
    test_plasm(6, 6, 100)
#    test_plasm(8, 1, 5)
#    test_plasm(9, 64, 100)
#    test_plasm(10, 8, 10)
#    test_plasm(11, 8, 10)




