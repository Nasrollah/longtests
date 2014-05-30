input: clean
	../../bin/gmsh2triangle --2d src/drainage_a.msh
	../../bin/gmsh2triangle --2d src/drainage_b.msh
	../../bin/gmsh2triangle --2d src/drainage_c.msh
	../../bin/gmsh2triangle --2d src/drainage_d.msh

clean:
	rm -rf *.stat *.vtu *.node *.edge *.ele *.log-0 *.err-0
	rm -rf matrixdump*
