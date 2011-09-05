#!/usr/bin/env python


"""
ROS:   tons of drivers for hardware
ecto:  kinect, cameras.
"""

slide_data = dict(
    nomenclature=('nomenclature', """acronym vs greek name,
nodes vs cells
turtles vs slimy things
"""),
    buildsystem=('building', """rosmake vs cmake.   ecto uses no code generation."""),
    languages=('languages', """anything you can write message generator
and nodes for (xml-rpc, etc) vs c++-nodes with python wrappers for
introspection and configuration"""),
    devmodel=('development model', """hybrid vs nonhybrid...  that is,
you don't by design have both python and c++ in the same process all
the time.  roslua perhaps a notable exception.  you could probably
implement a rospy that is a wrapper around roscpp"""),
    transports=('transports', """TCPROS, UDPROS (not really so,
supported).  centrall defined, fundamental to what ROS is.  ROSJAVA
speaks this.  ecto has no inherent notion of transport, but there are
cells that connect graphs across a network that know about transport,
but it is limited to these cells."""),
    sync=('sync', """asynchronous vs synchronous.  in ros you don't
know who is listening to a message... you don't in ecto either.  ros:
queues, ecto: no queues.  in ros you can't block until a receiver gets
your message.  you can wait until a 'gotit' message comes back, but
you can't be sure that it will get to you."""),
    serialization=('protocol/serialization', """ROS: messages generated
for a whaever languages can (de)serialize messages and speak the
network protocol.  in ecto there are cells (in development) that use
boost::serialization to send arbitrary datatypes across the network,
but there is NO INHERENT NOTION OF PROTOCOL.  more flexible than ros
messages, you can send cv::Mat directly, have fine grained control of
serialization, versioning of objects, send objects as pointer-to-base,
boost::variant one of my favorites."""),
    runtime=('master vs scheduler', """executed by XML launchfiles
(specifically nodelets are typically in xml launchfiles and these get
messy) or rosrun vs python scripts.  ros requires always at least two
separate processes, a node and a master.  This master doesn't know at
any given instant exactly what messages are in flow between which
nodes; the ecto scheduler does."""),
    threading=('threading', """necessarily multithreaded vs flexibly threaded, different execution models. """),
    delivery=('delivery', """messages copied in both cases.  can
    by-value copy a shared_ptr<T>, user needs to understand semantics.
    ros has message queues, ecto has none. ros messages delivered
    asynchronously (via callback) and unreliably, ecto messages
    delivered reliably and 'synchronously' (no callback).  If an ecto
    cell inputs a string and two cv::Mats and outputs a pointcloud and
    a pose, the interface ensures that these are all done at the same
    time."""),
    support=('interop', """ros: lots of hardware supported.  ecto:
    opencv, pcl, openni, ROS""")
)
order=['nomenclature', 'buildsystem', 'languages', 'devmodel',
       'transports', 'sync', 'serialization', 'runtime', 
       'threading', 'delivery', 'support']

# 17:29 < fergs> the big thing is this: ros has PR2 drivers, etc, these
#                solve a problem Ecto doesn't care about... however if
#                you want to build a perception system (or any sort of
#                graph-based processing), you either have to A) build
#                the entire thing inside a single node (which probably
#                limits code reuse, and maintainability) or B) build a
#                whole bunch of ecto::cell-sized pieces and connect them
#                with lots of topics (as nodes performance degrades
#                horribly, as nodelets you build a whole bunch of
#                ecto::cell-sized pieces and connect them with lots of
#                topics (as nodes performance degrades horribly, as
#                nodelets you have a headache putting them together in
#                an XML launch file) and I'm sure over time we'll find
#                things to move into besides perception (for instance,
#                arm navigation planning could probably benefit from
#                ecto) grasping analysis as well

from hl import *

print locals()
dent = "   "
title = "\n" + dent + "%(Blu)sROS%(nrm)s vs %(Grn)secto%(nrm)s\n\n" % locals()

print title

frames = [(('((ROS){1,1})', Blu), ('(ecto)', Grn)),
          (('(supports)', Red),)
          ]

totalitems = ""
for slide in order:
    cls()

    print title + totalitems + dent + Wht + slide_data[slide][0] + nrm
    totalitems += dent + slide_data[slide][0] + "\n"
    notes(slide_data[slide][1])
    getch()


