DEMOS = webcam webcam_fps webcam_grey webcam_circles webcam_pose \
	kinect_view


slides/%.notes.txt:
	echo "notes for $*" > $@

slides/%.txt:
	ln -s ../$*.py $@

slides/%.py:
	echo "fname = '$*.txt'" > $@
	echo "hl = []" >> $@



slides/%-graph.pdf:
	./makegraph.py $* slides

all: $(DEMOS:%=slides/%.txt) \
	$(DEMOS:%=slides/%.notes.txt) \
	$(DEMOS:%=slides/%-graph.pdf) \
	$(DEMOS:%=slides/%.py)

