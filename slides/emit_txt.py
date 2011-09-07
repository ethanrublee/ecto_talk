#!/usr/bin/env python

import sys

from asciipoint import *
slide = open('src/emit.cpp').read()
#slide += '///////////////////////////////////////////\n'
#slide += open('emit.py').read()

hl = [(('(static void declare_io)', Red),),
      (('(const tendrils& p)', Red, 1),),
      (('(tendrils& i, tendrils& o)', Red),),
      (('(o\.declare<std::string>)', Red),),
      (('(\"output\")', Red),),
      (('(std::string emitted.*)', Red),),
      (('(o.get<.*)', Red),),
      ]

notetxt = ""
run(hl, notetxt, slide)


