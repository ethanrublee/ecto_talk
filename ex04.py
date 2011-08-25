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

normals = ecto_pcl.NormalEstimation("Normals", k_search=0, radius_search=0.2)

# segment, find hull
# find best fit plane using ransac
# alt here:  SACSegmentation.  (no normals)
segment = ecto_pcl.SACSegmentationFromNormals("PlanarSegmentation",
                                     model_type=ecto_pcl.SACMODEL_NORMAL_PLANE,
                                     eps_angle=0.09, distance_threshold=0.1)


# put the points on the plane actually on the plane... a.k.a. remove
# noise tangent to plane defined by model, for the points that the
# model fits
project = ecto_pcl.ProjectInliers("ProjectInliers",
                         model_type=ecto_pcl.SACMODEL_NORMAL_PLANE)

# finds the convex hull of the *perimeter* of the plane
conhull = ecto_pcl.ConvexHull("ConvexHull")

# prism:  take the hidensity orig. cloud, the hull-perimeter, and extract
# what is closer to the sensor (i.e. "higher" or "above" the hull)
prism = ecto_pcl.ExtractPolygonalPrismData("ExtractPrism", height_min=0.01, height_max=0.2)

# given orig. cloud and indices from prism above, make smaller cloud:
# now we've got highdensity, only above table
extract = ecto_pcl.ExtractIndices("Extract", negative=False)



viewer = ecto_pcl.CloudViewer()

plasm.connect(cap[:] >> conv[:],
              conv[:] >> voxgrid[:],
              voxgrid[:] >> normals[:],
              voxgrid[:] >> segment["input"],
              normals[:] >> segment["normals"],
              # project inliers, find convex hull
              voxgrid[:] >> project["input"],
              segment["model"] >> project["model"],
              project[:] >> conhull[:],

              # extract stuff on table from original high-res cloud
              conv[:] >> prism["input"],
              conhull[:] >> prism["planar_hull"],
              prism[:] >> extract["indices"],
              conv[:] >> extract["input"],

              extract[:] >> viewer[:])

f = open(sys.argv[0] + ".dot", "w")
print >>f, plasm.viz()
f.close()
subprocess.check_call(["dot", "-Tpdf", "-O", sys.argv[0] + ".dot"])
sched = ecto.schedulers.Threadpool(plasm)
sched.execute()

