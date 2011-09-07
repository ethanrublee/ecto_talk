#!/usr/bin/env python

import sys, ecto, ectotalk

plasm = ecto.Plasm()
nada = ectotalk.NoOp();

plasm.insert(nada)

if __name__ == "__main__":
    sched = ecto.schedulers.Threadpool(plasm)
    sched.execute(niter=10)

