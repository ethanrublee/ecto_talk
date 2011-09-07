#!/usr/bin/env python

import sys

from asciipoint import *
slide = open('src/printy.cpp').read()
slide += '///////////////////////////////////////////\n'
slide += open('printy.py').read()

hl = [(('(declare_params)', Red),),
      (('(static)', Red),),
      (('(tendrils& p)', Red, 1),),
      (('(declare<std::string>)', Red),),
      (('(\"what\")', Red),),
      (('(get<std::string>)', Red),),
      (('(what = .*|std::string what)', Red),),
      (('(<< what <<)', Red),),
      (('("what"|what=)', Ylw),), 
      ]


notetxt = "meh"

run(hl, notetxt, slide)


