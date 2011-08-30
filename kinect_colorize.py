#!/usr/bin/env python

import sys
import ecto, ecto_openni, ecto_opencv
from ecto_pcl import *

plasm = ecto.Plasm()

cap = ecto_openni.Capture()
conv = NiConverter()

voxgrid = VoxelGrid("VoxelGrid", leaf_size=0.05)

normals = NormalEstimation("Normals", k_search=0, radius_search=0.2)

segment = SACSegmentationFromNormals("PlanarSegmentation",
                                     model_type=SACMODEL_NORMAL_PLANE,
                                     eps_angle=0.09, distance_threshold=0.1)

project = ProjectInliers("ProjectInliers",
                         model_type=SACMODEL_NORMAL_PLANE)

conhull = ConvexHull("ConvexHull")

prism = ExtractPolygonalPrismData("ExtractPrism",
                                  height_min=0.01, height_max=0.2)

extract = ExtractIndices("Extract", negative=False)

clusters = EuclideanClusterExtraction("Clusters",
                                      min_cluster_size=150,
                                      cluster_tolerance=0.005)

colorize = ColorizeClusters("Colorize")

merge = MergeClouds("merge")

viewer = CloudViewer()

plasm.connect(cap[:] >> conv[:],
              conv[:] >> voxgrid[:],
              voxgrid[:] >> normals[:],
              voxgrid[:] >> segment["input"],
              normals[:] >> segment["normals"],
              voxgrid[:] >> project["input"],
              segment["model"] >> project["model"],
              project[:] >> conhull[:],
              conv[:] >> prism["input"],
              conhull[:] >> prism["planar_hull"],
              prism[:] >> extract["indices"],
              conv[:] >> extract["input"],

              extract[:] >> clusters[:],
              clusters[:] >> colorize["clusters"],
              extract[:] >> colorize["input"],

              conv[:] >> merge["input"],
              colorize[:] >> merge["input2"],
              merge[:] >> viewer[:]
              )



if __name__ == "__main__":
    ecto.view_plasm(plasm)
    sched = ecto.schedulers.Threadpool(plasm)
    sched.execute()

