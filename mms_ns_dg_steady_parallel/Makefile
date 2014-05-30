input:	clean
	../../bin/gmsh2triangle --2d src/MMS_A.msh
	../../bin/gmsh2triangle --2d src/MMS_B.msh
	../../bin/gmsh2triangle --2d src/MMS_C.msh
	../../bin/gmsh2triangle --2d src/MMS_D.msh

clean:
	rm -rf *.pvtu *.stat *.s *.log-? *.err-? *.halo *.node *.ele *.edge *checkpoint*
	rm -rf MMS_?_?
	rm -rf *flredecomp*
