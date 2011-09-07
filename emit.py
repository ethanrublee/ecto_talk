#!/usr/bin/env python

import sys, ecto, ectotalk

plasm = ecto.Plasm()
emitter = ectotalk.Emit(what="***THIS***");

plasm.insert(emitter)

if __name__ == "__main__":
    sched = ecto.schedulers.Threadpool(plasm)
    sched.execute(niter=10)

