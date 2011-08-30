DEMOS = webcam webcam_fps webcam_grey


slides/%.notes.txt:
	echo "notes for $*" > $@

slides/%.txt:
	ln -s ../$*.py $@


slides/%-graph.pdf:
	./makegraph %* slides

all: $(DEMOS:%=slides/%.txt) $(DEMOS:%=slides/%.notes.txt) $(DEMOS:%:slides/%-graph.pdf)
