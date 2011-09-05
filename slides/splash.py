#!/usr/bin/env python

from asciipoint import *

slide = """{Grn}
     oooooooooooooooo
     ooooo    o  o  o
     o   o    o  o  o
     oooooooo o  oooo
{nrm}

     A Framework For Perception



     Troy Straszheim
     Ethan Rublee

     Willow Garage, Inc.
""".format(**locals())

print cls
print slide

notetxt = """

Announcing Ecto Amoeba (Beta, August 2011)

Development began in earnest March 11, 2011

  Ecto core:

    7k lines C++
    2.5k lines Python

  Tests:
    1.8k lines C++
    3.3k lines Python

  > 2k lines of handwritten .rst documentation


Across projects ecto, ecto_pcl, ecto_ros, ecto_opencv, ecto_openni:
28k lines C++, 9.5k lines Python
"""


notes("intro", notetxt)

getch()

