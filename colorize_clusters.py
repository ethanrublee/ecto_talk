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

import sys
import ecto, ecto_openni, ecto_opencv # ecto_sensor_msgs,
from ecto_pcl import *
plasm = ecto.Plasm()

# video_cap = ecto_openv.highgui.VideoCapture(video_device=0, width = 1600, height = 1200)

cap = ecto_openni.Capture()
conv = NiConverter()

voxgrid = VoxelGrid("VoxelGrid", leaf_size=0.05)

normals = NormalEstimation("Normals", k_search=0, radius_search=0.2)

# segment, find hull
# find best fit plane using ransac
# alt here:  SACSegmentation.  (no normals)
segment = SACSegmentationFromNormals("PlanarSegmentation",
                                     model_type=SACMODEL_NORMAL_PLANE,
                                     eps_angle=0.09, distance_threshold=0.1)


# put the points on the plane actually on the plane... a.k.a. remove
# noise tangent to plane defined by model, for the points that the
# model fits
project = ProjectInliers("ProjectInliers",
                         model_type=SACMODEL_NORMAL_PLANE)

# finds the convex hull of the *perimeter* of the plane
conhull = ConvexHull("ConvexHull")

# prism:  take the hidensity orig. cloud, the hull-perimeter, and extract
# what is closer to the sensor (i.e. "higher" or "above" the hull)
prism = ExtractPolygonalPrismData("ExtractPrism", height_min=0.01, height_max=0.2)

# given orig. cloud and indices from prism above, make smaller cloud:
# now we've got highdensity, only above table
extract = ExtractIndices("Extract", negative=False)

# get clusters of objects above table: vector of (lists of indices)

clusters = EuclideanClusterExtraction("Clusters", min_cluster_size=50, cluster_tolerance=0.005)

# for each one, colorize
colorize = ColorizeClusters("Colorize")

# extract plane, merge with clusters
# extract2 = ExtractIndices("Extract2", negative=False)
merge = MergeClouds("merge")

viewer = CloudViewer()

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

              extract[:] >> clusters[:],
              clusters[:] >> colorize["clusters"],
              extract[:] >> colorize["input"],

              conv[:] >> merge["input"],
              colorize[:] >> merge["input2"],

              # publish to ROS, or
              # merge[:] >> pcl2msg[:],
              # pcl2msg[:] >> pub[:]

              # pop up in cloud viewer
              merge[:] >> viewer[:]
              #conhull[:] >> viewer[:]
              )



if __name__ == "__main__":
    ecto.view_plasm(plasm)
    # ecto_ros.init(sys.argv, "colorize_clusters")
    sched = ecto.schedulers.Threadpool(plasm)
    sched.execute_async()

    from IPython.Shell import IPShellEmbed
    ipshell = IPShellEmbed()
    ipshell()

