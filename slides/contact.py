#!/usr/bin/env python
from asciipoint import *

slide = """

   CODE:           http://github.com/plasmodic/

   IRC:            irc.oftc.net:#ecto

   MAILINGLIST:    http://groups.google.com/a/plasmodic.org/?hl=en

   WWW:            http://plasmodic.org
                   http://ecto.willowgarage.com

"""

notes = ["""

Why plasmodic?  Does it mean anything, no, it is a made-up name.
'ecto' was taken on github.  We'd been up too late coding, plasmodic
was it.

Why ecto?  Originally from the greek 'outside' or 'external'.  Turns
out that 'ecto' was a 1987 album from singer/songwriter Happy Rhodes,
who has a wide enough vocal range that one of her songs was once
mislabeled and put up on napster as a duet between annie lennox and
kate bush.  ecto.org is a fan website run by people who call
themselves 'ectophiles'.  So the name came with its own built-in
quirky subculture and even a "rickroll"
"""]

hl = [(('(IRC:|MAILINGLIST:|WWW:|CODE:)+', Grn),
       ('(http:[^\s]+|irc.*)+', ylw),),
      ]

run(hl, notes, slide)
