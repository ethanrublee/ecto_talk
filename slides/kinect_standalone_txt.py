#!/usr/bin/env python

import sys, re

from asciipoint import *
slide = open('kinect_standalone.py').read()

hl = [(('(from ecto_openni.*)', Red),),
      ((r'(capture =.*)', Red),),
      ((r'(verter =.*)', Red),),
      ((r'(highgui\.imshow)+', Red, 2, re.MULTILINE),),
      ]


notetxt = "meh"

run(hl, notetxt, slide)


