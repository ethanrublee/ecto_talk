#!/usr/bin/env python

import sys, ecto, ectotalk

plasm = ecto.Plasm()
printy = ectotalk.Printy(what="***THIS***");

plasm.insert(printy)

if __name__ == "__main__":
    sched = ecto.schedulers.Threadpool(plasm)
    sched.execute(niter=10)

