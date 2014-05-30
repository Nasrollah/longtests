input: clean
	gmsh -3 -o nemo_layers_1000m.msh nemo_layers_1000m.geo
	../../bin/gmsh2triangle nemo_layers_1000m.msh

clean: 
	rm -f  *.ele *.edge *.node *.face *.poly *.vtu *.s  *.stat *.log-0 *.err-0 matrixdump* *log *err
