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
    if [ -f slides/$1-graph.pdf ] ; then
        evince -s slides/$1-graph.pdf
    fi
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
    demo colorize_clusters
    demo noop
    demo printy
    ./slides/emit_txt.py
    tput clear
    cat emit.py
    read MEH
    tput clear
    ./emit.py
    ./slides/printinput_txt.py
    tput clear
    cat ./printinput.py
    read MEH
    evince -s slides/printinput-graph.pdf
    tput clear
    ./printinput.py
    ./slides/printinput2_txt.py
fi
