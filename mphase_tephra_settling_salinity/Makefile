preprocess:
	@echo **********Converting 2D .msh file to triangle format
	gmsh -2 -o mphase_tephra_settling_salinity.msh src/mphase_tephra_settling_salinity.geo
	../../bin/gmsh2triangle --2d mphase_tephra_settling_salinity.msh

run:
	@echo **********Running simulation
	mpiexec -n 8 ../../bin/flredecomp -i 1 -o  -v -l mphase_tephra_settling_salinity mphase_tephra_settling_salinity_flredecomp
	mpiexec -n 8 ../../bin/fluidity mphase_tephra_settling_salinity_flredecomp.flml

input: clean preprocess

clean:
	rm -f *.stat *.steady_state*
	rm -f *.d.* *.vtu
	rm -f *.msh *.ele *.edge *.node *.poly
	rm -f matrixdump* *.log* *.err*
	rm -rf mphase_tephra_settling_salinity_*
	rm -rf *flredecomp*
