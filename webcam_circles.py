#!/usr/bin/env python
# add pose estimation
import ecto
from ecto_opencv import highgui, imgproc, calib

plasm = ecto.Plasm()
video_cap = highgui.VideoCapture(video_device=0)

fps = highgui.FPSDrawer()
rgb2gray = imgproc.cvtColor('rgb -> gray', flag=imgproc.RGB2GRAY)

detect = calib.PatternDetector(rows=5, cols=3,
                               pattern_type=calib.ASYMMETRIC_CIRCLES_GRID,
                               square_size=0.04)

draw = calib.PatternDrawer(rows=5, cols=3)

imshow = highgui.imshow(name='Pattern', waitKey=2, maximize=True)

plasm.connect(video_cap['image'] >> fps['image'],
              fps['image'] >> rgb2gray['input'],
              rgb2gray['out'] >> detect['input'],
              detect['out', 'found'] >> draw['points', 'found'],
              video_cap['image'] >> draw['input'],

              draw[:] >> imshow[:])

if __name__ == "__main__":
    sched = ecto.schedulers.Singlethreaded(plasm)
    sched.execute()
