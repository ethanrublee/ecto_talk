#!/usr/bin/env python

import sys

from asciipoint import *
slide = open('webcam_circles.py').read()

hl = [(('(calib)', Red, 1),),
      ((r'(calib\.PatternDetector)', Red),),
      ((r'(rows.*3)', Red, 1),),
      ((r'(pattern_type.*GRID)', Red, 1),),
      ((r'(square_size.*4)', Red, 1),),
      ((r'(draw.*)', Red, 1),),
      ((r'(rgb2.*>>.*)', Red, 1),),
      ((r'(detect.*>>.*)', Red, 1),),
      ]


notetxt = """so here it is easy to see that the drawer takes a vector
 of image points and it draws it on an image that is different than
 the one it found them, albeit only that the image has now had an fps
 legend drawn on it.
"""

run(hl, notetxt, slide)


