#!/bin/sh -e

NOTESTTY=/dev/pts/28

exec 2>/dev/pts/28

# CACA_DRIVER=ncurses cacaview willowgarage.jpg

function slide {
    #tput clear > $NOTESTTY
    #tput reset > $NOTESTTY
    pushd slides > /dev/null
    echo $1 > $NOTESTTY
    cat `basename $1 .txt`.notes.txt > $NOTESTTY
    echo > $NOTESTTY
    ../highlight.py $1.py
    popd > /dev/null
}

function demo {
    slide $1
    evince -s slides/$1-graph.pdf
    ./$1.py
}

#slide splash
#slide contact
#slide poseestimator
#demo webcam
#demo webcam_fps
#demo webcam_grey
#demo webcam_circles
#demo webcam_pose

demo kinect_view        # kinect -> pointcloud
demo kinect_standalone  # kinect -> cv::Mat

