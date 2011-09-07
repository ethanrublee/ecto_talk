#!/usr/bin/env python

import sys

from asciipoint import *
slide = open('src/PrintInput2.cpp').read()

hl = [(('(declare_io)', Red),),
      (('(i\.declare<std::string>.*)', Red),),
      (('(spore)', Red, 1),),
      (('(spore<std::string>)', Red, 1),),
      (('(in =.*)', Red, 1),),
      (('(\*in)', Red),),
      ]

notetxt = ""
run(hl, notetxt, slide)


