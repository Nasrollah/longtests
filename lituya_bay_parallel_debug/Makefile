input:	clean
	gmsh -2 src/inletslice.geo
	../../bin/gmsh2triangle --2d src/inletslice.msh


clean:
	rm -f *.stat *.log* *.err* *.msh *.halo *.face *.node *.ele *.edge *.convergence *.pvtu matrixdump*
	rm -f src/inletslice.msh
	rm -rf *_checkpoint* 
	rm -f landslide_*/*.vtu
	rm -rf landslide_? landslide_??
	rm -rf *flredecomp*
