input:	clean
	gmsh -3 src/inletslice.geo
	../../bin/gmsh2triangle src/inletslice.msh


clean:
	rm -f *.vtu *.stat *.log* *.err* *.msh *.halo *.node *.ele *.face *_checkpoint* *.convergence *.pvtu matrixdump*
