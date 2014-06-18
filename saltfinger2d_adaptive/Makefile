input: clean
	cp src/unstructured-2.geo .
	gmsh -2 -algo del2d unstructured-2.geo
	gmsh2triangle -2 unstructured-2.msh

clean:
	rm -fr  *.ele *.face *.node saltfinger-2d_* unstructured-2.* *.edge *.stat *.halo
	rm -rf *flredecomp*
