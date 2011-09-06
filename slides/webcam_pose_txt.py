#!/usr/bin/env python

import sys

from asciipoint import *
slide = open('webcam_pose.py').read()

hl = [(('(pose_calc)', Red),),
      (('(pose_draw)', Red),),
      (('(camera_info)', Red),),
      ]


notetxt = """so here it is easy to see that the drawer takes a vector
 of image points and it draws it on an image that is different than
 the one it found them, albeit only that the image has now had an fps
 legend drawn on it.
"""

run(hl, notetxt, slide)


