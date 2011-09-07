DEMOS = webcam webcam_fps webcam_grey webcam_circles webcam_pose \
	kinect_standalone kinect_view kinect_voxelgrid colorize_clusters


slides/%.notes.txt:
	echo "notes for $*" > $@

slides/%.txt:
	ln -s ../$*.py $@

slides/%.py:
	echo "fname = '$*.txt'" > $@
	echo "hl = []" >> $@



slides/%-graph.pdf:
	./makegraph.py $* slides

all: $(DEMOS:%=slides/%-graph.pdf)


