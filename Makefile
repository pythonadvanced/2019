all: strip md

NOTEBOOKS := $(shell git ls-files *.ipynb)
MDS = $(subst .ipynb,.md,$(NOTEBOOKS))

strip:
	nbstripout $(NOTEBOOKS)

md: $(MDS)

%.md: %.ipynb
	jupyter nbconvert --to markdown $*

