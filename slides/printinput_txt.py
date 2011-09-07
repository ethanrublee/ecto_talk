#!/usr/bin/env python

import sys

from asciipoint import *
slide = open('src/printinput.cpp').read()
#slide += '///////////////////////////////////////////\n'
#slide += open('emit.py').read()

hl = [(('(declare_io)', Red),),
      (('(i\.declare<std::string>)', Red),),
      (('(\"input\")', Red, 1),),
      (('(i.get<.*\))', Red),),
      ]

notetxt = ""
run(hl, notetxt, slide)


