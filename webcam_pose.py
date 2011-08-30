#!/usr/bin/env python
# add pose estimation
import ecto
from ecto_opencv import highgui, imgproc, calib

plasm = ecto.Plasm()
video_cap = highgui.VideoCapture(video_device=0)

fps = highgui.FPSDrawer()
rgb2gray = imgproc.cvtColor('rgb -> gray', flag=imgproc.RGB2GRAY)

detect = calib.PatternDetector(rows=5, cols=3,
                               pattern_type=calib.ASYMMETRIC_CIRCLES_GRID,
                               square_size=0.04)

draw = calib.PatternDrawer(rows=5, cols=3)

pose_calc = calib.FiducialPoseFinder('Pose Calc')
pose_draw = calib.PoseDrawer('Pose Draw')
camera_info = calib.CameraIntrinsics('Camera Info', camera_file="camera.yml")

imshow = highgui.imshow(name='Pattern', waitKey=2)

plasm.connect(
    video_cap['image'] >> rgb2gray['input'],
    rgb2gray['out'] >> detect['input'],
    detect['out', 'found'] >> draw['points', 'found'],
    video_cap['image'] >> draw['input'],
    camera_info['K'] >> (pose_calc['K'], pose_draw['K']),
    detect['out', 'ideal', 'found'] >> pose_calc['points', 'ideal', 'found'],
    pose_calc['R', 'T'] >> pose_draw['R', 'T'],
    draw['out'] >> pose_draw['image'],
    pose_draw['output'] >> fps['image'],
    fps['image'] >> imshow['input']
    )

if __name__ == "__main__":
    sched = ecto.schedulers.Threadpool(plasm)
    sched.execute()
