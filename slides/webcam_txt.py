#!/usr/bin/env python

import sys

from asciipoint import *
slide = open('webcam.py').read()

hl = [(('(import ecto)', Red),),
      ((r'(from ecto_opencv.*)', Red),),
      ((r'(plasm =.*)', Red),),
      ((r'(VideoCapture)', Red),),
      ((r'(highgui\.VideoCapture)', Red),),
      ((r'(video_device=0)', Red),),
      ((r'(video_cap)', Red, 1),),
      ((r'(highgui\.imshow)', Red),),
      ((r'(name.*2)', Red),),
      ((r'(imshow)', Red, 1),),
      ]


notetxt = "meh"

run(hl, notetxt, slide)


