#!/usr/bin/env python

"""
This example shows how to extract points corresponding to objects on a table,
    cluster them, colorize the clusters, and republish as a single cloud.

  1) The example downsamples using a VoxelGrid before estimating
     normals for the downsampled cloud.
  2) These normals are then used for segmentation using RANSAC.
  3) Segmentation produces a planar model to which all inliers are
     projected so that a 2D convex hull can be created.
  4) We then extract the indices of all points that are above the
     plane formed by the convex hull.
  5) This cloud is then clustered
  6) The clusters are concatenated, with each having a unique color.

"""

import sys, subprocess
import ecto, ecto_openni, ecto_pcl

plasm = ecto.Plasm()

cap = ecto_openni.Capture()

conv = ecto_pcl.NiConverter()

voxgrid = ecto_pcl.VoxelGrid("VoxelGrid", leaf_size=0.05)

viewer = ecto_pcl.CloudViewer()

plasm.connect(cap[:] >> conv[:],
              conv[:] >> voxgrid[:],
              voxgrid[:] >> viewer[:])

f = open(sys.argv[0] + ".dot", "w")
print >>f, plasm.viz()
f.close()
subprocess.check_call(["dot", "-Tpdf", "-O", sys.argv[0] + ".dot"])
sched = ecto.schedulers.Threadpool(plasm)
sched.execute()

