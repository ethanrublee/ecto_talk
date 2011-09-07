#!/usr/bin/env python

import sys, ecto, ecto_openni
from ecto_pcl import *
plasm = ecto.Plasm()

cap = ecto_openni.Capture()
conv = NiConverter()
passthru = PassThrough()
viewer = CloudViewer()

plasm.connect(cap[:] >> conv[:],
              conv[:] >> passthru[:],
              passthru[:] >> viewer[:]
              )

if __name__ == "__main__":
    sched = ecto.schedulers.Singlethreaded(plasm)
    sched.execute()

