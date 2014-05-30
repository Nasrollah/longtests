input: clean
	gmsh -2 -o Subduction_Mesh.msh src/Subduction_Mesh.geo 
	../../bin/gmsh2triangle --2d Subduction_Mesh.msh

clean:
	rm -f  *.ele *.edge *.node *.vtu *.stat *.msh *.detectors

