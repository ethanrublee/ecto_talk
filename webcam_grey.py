#!/usr/bin/env python
# add pose estimation
import ecto
from ecto_opencv import highgui, imgproc

plasm = ecto.Plasm()
video_cap = highgui.VideoCapture(video_device=0)

fps = highgui.FPSDrawer()
rgb2gray = imgproc.cvtColor('rgb -> gray', flag=imgproc.RGB2GRAY)

imshow = highgui.imshow(name='Pattern', waitKey=2)

plasm.connect(video_cap['image'] >> rgb2gray['input'],
              rgb2gray['out'] >> fps['image'],
              fps['image'] >> imshow['input']
              )

if __name__ == "__main__":
    sched = ecto.schedulers.Threadpool(plasm)
    sched.execute()
