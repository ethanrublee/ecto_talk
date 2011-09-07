#!/usr/bin/env python

import sys, re

from asciipoint import *
slide = open('kinect_view.py').read()

hl = [(('(cap =.*)', Red),),
      ((r'(conv =.*)', Red),),
      ((r'(passthru =.*)', Red),),
      ((r'(viewer =.*)', Red),),
      ]


notetxt = "meh"

run(hl, notetxt, slide)


