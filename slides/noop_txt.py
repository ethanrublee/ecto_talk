#!/usr/bin/env python

import sys

from asciipoint import *
slide = open('src/noop.cpp').read()
slide += '///////////////////////////////////////////\n'
slide += open('noop.py').read()

hl = [(('(struct NoOp)', Red),),
      ((r'(int process.*)', Red),),
      ((r'(const tendrils& i)', Red),),
      ((r'(const tendrils& o)', Red),),
      ((r'(std.*)',Red),),
      ((r'(ECTO_CELL)', Red),),
      ((r'(ectotalk)', Red),),
      ((r'(NoOp)+', Red, 2),),
      ((r'(\"NoOp\")', Red, 1),(r'(?:ectotalk\.(NoOp))', Red)),
      ((r'(\"The.*\")', Red),)
      ]


notetxt = "meh"

run(hl, notetxt, slide)


