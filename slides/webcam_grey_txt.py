#!/usr/bin/env python

import sys

from asciipoint import *
slide = open('webcam_grey.py').read()

hl = [(('(imgproc)', Red, 1),),
      ((r'(^rgb2gray =.*$)', Red),),
      ((r'(video_.*\'\])', Red),),
      ((r'(rgb2gray.*e\'])', Red),),
      ]


notetxt = "meh"

run(hl, notetxt, slide)


