input: clean
	gmsh -3 -o oodc-unstructured.msh oodc-unstructured.geo 
	../../bin/gmsh2triangle oodc-unstructured.msh

clean:
	rm -f *.msh *.ele *.face *.node *.halo *.vtu *.stat matrixdump* *log* *err*
	rm -rf oodc-unstructured-parallel_?*
	rm -rf *flredecomp*
