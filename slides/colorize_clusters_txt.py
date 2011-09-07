#!/usr/bin/env python

import sys, re

from asciipoint import *
slide = open('colorize_clusters.py').read()

hl = [(('(([A-Z]\w+)\()+', Red),)
      ]


notetxt = "meh"

run(hl, notetxt, slide)


