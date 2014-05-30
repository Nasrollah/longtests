preprocess:
	@echo **********Creating 3D mesh
	gmsh -3 -o mphase_tephra_settling_3d.msh src/mphase_tephra_settling_3d.geo
	../../bin/gmsh2triangle mphase_tephra_settling_3d.msh

run:
	@echo **********Running simulation
	mpiexec -n 8 ../../bin/flredecomp -i 1 -o 8 -v -l mphase_tephra_settling_3d mphase_tephra_settling_3d_flredecomp
	mpiexec -n 8 ../../bin/fluidity -v2 -l mphase_tephra_settling_3d_flredecomp.flml

input: clean preprocess

clean:
	rm -f *.stat *.steady_state*
	rm -f *.d.* *.vtu
	rm -f *.msh
	rm -f *.ele *.edge *.node *.poly *.face *.halo
	rm -f matrixdump* *.log* *.err*
	rm -rf mphase_tephra_settling_3d_*
	rm -rf *flredecomp*
