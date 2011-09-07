#!/usr/bin/env python

import sys, re

from asciipoint import *
slide = open('kinect_voxelgrid.py').read()

hl = [(('(voxgrid =.*)', Red),),
      ((r'(voxgrid\[:\])+', Red),),
      ]


notetxt = "meh"

run(hl, notetxt, slide)


