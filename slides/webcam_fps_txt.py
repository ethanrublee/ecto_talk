#!/usr/bin/env python

import sys

from asciipoint import *
slide = open('webcam_fps.py').read()

hl = [(('(^.*import highgui.*$)', Red),),
      ((r'(^fps =.*$)', Red),),
      ((r'(video_.*\'\])', Red),),
      ((r'(fps.*t\'])', Red),),
      ]


notetxt = "meh"

run(hl, notetxt, slide)


