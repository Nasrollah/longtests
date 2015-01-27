MODEL=vanKekenTwoB

default: input

input:  clean
	gmsh -2 -optimize src/Subduction_Mesh.geo
	cp src/Subduction_Mesh.msh .

clean:
	rm -f  *.ele *.edge *.node *.vtu *.stat *.msh *.detectors fluidity.* *.dat *Parallel* *.pyc
	rm -R -f $(MODEL)_*

