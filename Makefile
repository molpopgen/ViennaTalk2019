IMAGES:=tajd.png tree1.png tree2.png

all: Thornton.pdf

clean:
	rm -f Thornton.pdf

Thornton.pdf: Thornton.Rmd render.R $(IMAGES)
	r render.R

tajd.png: tajd.py
	python3 tajd.py

tree1.svg: simtrees.py
	python3 simtrees.py

tree2.svg: simtrees.py
	python3 simtrees.py

tree1.png: tree1.svg
	convert -density 300 tree1.svg tree1.png

tree2.png: tree2.svg
	convert -density 300 tree2.svg tree2.png
