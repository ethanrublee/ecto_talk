#!/usr/bin/env python

"""
This example shows how to capture a Kinect point
cloud and display it to a cloud viewer.
"""

import ecto, ecto_openni
from ecto_pcl import *

plasm = ecto.Plasm()

cap = ecto_openni.Capture()
conv = NiConverter()

passthru = PassThrough()
voxgrid = VoxelGrid("VoxelGrid", leaf_size=0.02)

viewer = CloudViewer("Viewer", window_name="Clouds!")

plasm.connect(cap[:] >> conv[:],
              conv[:] >> passthru[:],
              passthru[:] >> voxgrid[:],
              voxgrid[:] >> viewer[:])

if __name__ == "__main__":
    sched = ecto.schedulers.Threadpool(plasm)
    sched.execute()




