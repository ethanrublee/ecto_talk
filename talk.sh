#!/bin/bash -e

NOTESTTY=/dev/pts/0

#exec 2>$NOTESTTY

# CACA_DRIVER=ncurses cacaview willowgarage.jpg

slide () {
    #tput clear > $NOTESTTY
    #tput reset > $NOTESTTY
    pushd slides > /dev/null
    echo $1 > $NOTESTTY
    cat `basename $1 .txt`.notes.txt > $NOTESTTY
    echo > $NOTESTTY
    ../highlight.py $1.py
    popd > /dev/null
}

demo () {
    ./slides/$1_txt.py
    evince -s slides/$1-graph.pdf
    ./$1.py
}

if [ -n "" ] ; then
    ./slides/splash.py
    ./slides/contact.py
    ./slides/comparison.py
    ./slides/poseestimator.py
    demo webcam
    demo webcam_fps
    demo webcam_grey
    demo webcam_circles
    demo webcam_pose
    demo kinect_standalone        # kinect -> pointcloud
    demo kinect_view        # kinect -> pointcloud
    demo kinect_voxelgrid  # kinect -> cv::Mat
fi

# work your way up to colorize_clusters
