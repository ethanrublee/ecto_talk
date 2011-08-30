#!/usr/bin/env python
# add pose estimation
import ecto
from ecto_opencv import highgui, imgproc

plasm = ecto.Plasm()
video_cap = highgui.VideoCapture(video_device=0)

fps = highgui.FPSDrawer()
rgb2gray = imgproc.cvtColor('rgb -> gray', flag=imgproc.RGB2GRAY)

imshow = highgui.imshow(name='Pattern', waitKey=2, maximize=True)

plasm.connect(video_cap['image'] >> fps['image'],
              fps['image'] >> rgb2gray['input'],
              rgb2gray['out'] >> imshow['input']
              )

if __name__ == "__main__":
    sched = ecto.schedulers.Singlethreaded(plasm)
    sched.execute()
