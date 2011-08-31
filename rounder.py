#!/usr/bin/env python
# abstract the input.

import sys, ecto, ecto_test
from ecto_opencv import highgui, calib, imgproc, features2d
from ecto_openni import Capture, ResolutionMode

import ecto_ros, ecto_sensor_msgs, ecto_geometry_msgs
import sys

class PoseFromFiducial(ecto.BlackBox):
    def __init__(self, plasm,rows,cols,pattern_type,square_size,debug=True):
        ecto.BlackBox.__init__(self, plasm)
        if debug:
            print self.__class__, "enabling debug nodes"
        self.video_cap = ecto.Passthrough('Image Input')
        self.rgb2gray = imgproc.cvtColor('rgb -> gray', flag=imgproc.RGB2GRAY)
        self.circle_detector = calib.PatternDetector('Dot Detector',
                                                     rows=rows, cols=cols,
                                                     pattern_type=pattern_type,
                                                     square_size=square_size)
        self.pose_calc = calib.FiducialPoseFinder('Pose Calc')
        self.camera_info = calib.CameraIntrinsics('Camera Info',
                                                  camera_file="camera.yml")
        self.trans = imgproc.Translate("trans", x=0.04 * 3)

        self.debug = debug
        if self.debug:
            self.fps = highgui.FPSDrawer()
            self.circle_drawer = calib.PatternDrawer('Circle Draw',
                                                     rows=rows, cols=cols)
            self.pose_draw = calib.PoseDrawer('Pose Draw')

            self.circle_conv = ecto_ros.Mat2Image('Fiducial Pose Converter')
            self.circle_pub = ecto_sensor_msgs.Publisher_Image('Fiducial Image w/ Pose Publisher', topic_name='/ecto/circles')

            self.foundprinter = ecto_test.Printer("printy", print_type='bool')

    def expose_outputs(self):
        return {
                'R': self.pose_calc['R'],
                'T': self.pose_calc['T'],
                'K': self.camera_info['K'],
               }
    def expose_inputs(self):
        return {
                'image': self.video_cap[:],
               }
    def expose_parameters(self):
        return {
                }
    def connections(self):
        graph = [self.video_cap[:] >> self.rgb2gray['input'],
                 self.rgb2gray['out'] >> self.circle_detector['input'],
                 self.camera_info['K'] >> self.pose_calc['K'],
                 self.circle_detector['out', 'ideal', 'found'] >> self.pose_calc['points', 'ideal', 'found'],
                 self.circle_detector['found'] >> self.foundprinter[:]
               ]

        if self.debug:
            graph += [ self.video_cap[:] >> self.circle_drawer['input'],
                       self.circle_drawer['out'] >> self.pose_draw['image'],
                       self.pose_draw['output'] >> self.fps['image'],
                       self.fps['image'] >> self.circle_conv[:],
                       self.circle_conv[:] >> self.circle_pub[:],
                       self.pose_calc['R', 'T'] >> self.pose_draw['R', 'T'],
                       self.circle_detector['out', 'found'] >> self.circle_drawer['points', 'found'],
                       self.camera_info['K'] >> self.pose_draw['K'],
                     ]
        return graph


# ecto_ros.init(sys.argv,"pose_estimator")

plasm = ecto.Plasm()
sched = ecto.schedulers.Threadpool(plasm)

#lil bit of debug On/Off
debug = True
if 'R' in sys.argv:
    debug = False


capture = Capture('ni device', rgb_resolution=ResolutionMode.SXGA_RES)
verter = highgui.NiConverter('verter')




#add our black box to the plasm.
pose_from_fiducial = PoseFromFiducial(plasm,
                                      rows=5, cols=3,
                                      pattern_type=calib.ASYMMETRIC_CIRCLES_GRID,
                                      square_size=0.04, debug=debug)

circle_drawer = calib.PatternDrawer('Circle Draw',
                                    rows=7, cols=3)

udim = 0.04

ppcm = 20
xcm = 7
ycm = 10
srr = calib.SubrectRectifier("extractor",
                             xoffset=-0.135, yoffset=0,
                             xsize_world=xcm*0.01, ysize_world=ycm*0.01,
                             xsize_pixels=xcm*ppcm, ysize_pixels=ycm*ppcm)

im2mat_rgb = ecto_ros.Image2Mat('Image -> cv::Mat')
im2mat_depth = ecto_ros.Image2Mat('Depth -> cv::Mat')

rgb2bgr = imgproc.cvtColor('rgb -> bgr')

training_card_conv = ecto_ros.Mat2Image('Training Card Converter')
training_card_pub = ecto_sensor_msgs.Publisher_Image('Training Card Publisher',
                                                     topic_name = '/ecto/training_card')

pose_from_plane = projector.PlaneFitter()

dewarp_table = calib.SubrectRectifier("tabledewarper",
                                      xoffset=-0.3, yoffset=-0.3,
                                      xsize_world=0.6, ysize_world=0.6,
                                      xsize_pixels=int(ppcm*60), ysize_pixels=int(ppcm*60))

table_rect_conv = ecto_ros.Mat2Image('Rectified Table Converter')
table_rect_pub = ecto_sensor_msgs.Publisher_Image('Rectified Table Publisher',
                                                     topic_name = '/ecto/table_rect')

orb = features2d.ORB(n_levels=3)
fast = features2d.FAST(thresh=5)
orb_test = features2d.ORB(n_levels=3)
fast_test = features2d.FAST(thresh=5)

draw_kpts = features2d.DrawKeypoints()
draw_kpts_test = features2d.DrawKeypoints()

matcher = features2d.Matcher()
hfitter = features2d.MatchRefinement()

match_draw = features2d.DrawMatches()

match_conv = ecto_ros.Mat2Image("Matches")
match_pub =  ecto_sensor_msgs.Publisher_Image("MatchesPub",
                                              topic_name="/ecto/matches")

plasm.connect(sync['image'] >> im2mat_rgb['image'],
              sync['depth'] >> im2mat_depth['image'],
              im2mat_depth['image'] >> pose_from_plane['depth'],
              pose_from_fiducial['K'] >> pose_from_plane['K'],
              im2mat_rgb['image'] >> rgb2bgr[:],
              rgb2bgr[:] >> (pose_from_fiducial['image'], srr['image'],
                             dewarp_table['image']),
              pose_from_fiducial['R', 'T', 'K'] >> srr['R', 'T', 'K'],
              pose_from_plane['R', 'T'] >> dewarp_table['R', 'T'],
              pose_from_fiducial['K'] >> dewarp_table['K'],
              dewarp_table[:] >> (fast['image'],draw_kpts['input'],orb['image']),
              fast['kpts'] >> (draw_kpts['kpts'],orb['kpts']),
              draw_kpts['output'] >> table_rect_conv[:],
              table_rect_conv[:] >> table_rect_pub[:],
              srr[:] >> (fast_test['image'], draw_kpts_test['input'],
                         orb_test['image']),
              fast_test['kpts'] >> (draw_kpts_test['kpts'],orb_test['kpts']),
              draw_kpts_test['output'] >> training_card_conv[:],
              training_card_conv[:] >> training_card_pub[:],
              orb['descriptors'] >> matcher['train'],
              orb_test['descriptors'] >> matcher['test'],
              orb['kpts'] >> (hfitter['train'],match_draw['train']),
              orb_test['kpts'] >> (hfitter['test'],match_draw['test']),
              matcher['matches'] >> hfitter['matches'],
              hfitter['matches'] >> match_draw['matches'],
              srr[:] >> match_draw['test_image'],
              dewarp_table[:] >> match_draw['train_image'],
              match_draw[:] >> match_conv[:],
              match_conv[:] >> match_pub[:]
              )
ecto.view_plasm(plasm)
#sched.execute(niter=0,nthreads=1)
plasm.configure_all()
sched.execute_async()

from IPython.Shell import IPShellEmbed
ipshell = IPShellEmbed()
ipshell()


