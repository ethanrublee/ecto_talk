#!/usr/bin/env python

import sys
from pygments import highlight
from pygments.lexers.agile import PythonLexer
from pygments.formatters.terminal256 import Terminal256Formatter
from pygments.formatters.terminal import TerminalFormatter
from pygments.styles import emacs
from pygments.filters import NameHighlightFilter
from pygments.token import Other
from talkstyle import TalkStyle

fltr = NameHighlightFilter(names=['video_cap'], 
                           tokentype=Other)

from asciipoint import *
slide = open('webcam.py').read()

lex = PythonLexer()
lex.add_filter(fltr)

slide = highlight(slide, lex, 
                  Terminal256Formatter(style=TalkStyle)
                  #TerminalFormatter(bg='dark')
                  )

hl = [(('(import ecto)', inv),),
      ((r'(from ecto_opencv.*)', inv),),
      ((r'(plasm =.*)', inv),),
      ((r'(VideoCapture)', inv),),
      ((r'(highgui\.VideoCapture)', inv),),
      ((r'(imshow)', inv),),
      ]


notetxt = "meh"

run(hl, notetxt, slide)


