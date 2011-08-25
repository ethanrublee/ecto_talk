#!/usr/bin/env python

import time, ecto
from ecto_opencv import highgui,calib,imgproc, cv_bp as opencv

plasm = ecto.Plasm()

def make_calib(images, plasm, calibfname):
    rgb2gray = imgproc.cvtColor(flag=imgproc.RGB2GRAY)
    plasm.connect(images["image"] >> rgb2gray[:])

    detect = calib.PatternDetector(rows=5, cols=3,
                                   pattern_type=calib.ASYMMETRIC_CIRCLES_GRID,
                                   square_size=0.04)
    plasm.connect(rgb2gray["out"] >> detect["input"])

    draw = calib.PatternDrawer(rows=5, cols=3)
    plasm.connect(detect["out"] >> draw["points"],
                  detect["found"] >> draw["found"],
                  images["image"] >> draw["input"])

    fps = highgui.FPSDrawer()
    plasm.connect(draw[:] >> fps[:])

    calibcell = calib.CameraCalibrator(output_file_name=calibfname + '.yml',
                                       n_obs=75,
                                       quit_when_calibrated=False)

    plasm.connect(detect["ideal"] >> calibcell["ideal"],
                  detect["out"] >> calibcell["points"],
                  detect["found"] >> calibcell["found"],
                  images["image"] >> calibcell["image"])
    pattern_show = highgui.imshow(name=calibfname, waitKey=10)
    plasm.connect(fps[:] >> pattern_show["input"])



import ecto_openni
kinect_device = ecto_openni.Capture()
kinect_images = highgui.NiConverter()
plasm.connect(kinect_device[:] >> kinect_images[:])
make_calib(kinect_images, plasm, "kinect")

webcam_device = highgui.VideoCapture(video_device=0)#, width=800, height=600)
make_calib(webcam_device, plasm, "webcam")

if __name__ == '__main__':

    ecto.view_plasm(plasm)
    sched = ecto.schedulers.Threadpool(plasm)
    sched.execute()
