#!/bin/bash -e

NOTESTTY=/dev/null

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
    slide $1
    evince -s slides/$1-graph.pdf
    ./$1.py
}

./slides/splash.py
slide contact
./slides/comparison.py
slide poseestimator
#demo webcam
#demo webcam_fps
#demo webcam_grey
#demo webcam_circles
#demo webcam_pose

#demo kinect_view        # kinect -> pointcloud
#demo kinect_standalone  # kinect -> cv::Mat
# work your way up to colorize_clusters
