#!/usr/bin/env python
# add pose estimation
import ecto
from ecto_opencv import highgui

plasm = ecto.Plasm()
video_cap = highgui.VideoCapture(video_device=0)

imshow = highgui.imshow(name='Pattern', waitKey=2)

plasm.connect(video_cap['image'] >> imshow['input'])

if __name__ == "__main__":
    sched = ecto.schedulers.Threadpool(plasm)
    sched.execute()
