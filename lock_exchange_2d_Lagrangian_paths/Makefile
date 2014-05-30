input: clean
	gmsh -2 ./src/lock_exchange_2d.geo
	../../bin/gmsh2triangle --2d ./src/lock_exchange_2d.msh

clean: 
	rm -f ./src/*.msh *.ele *.edge *.node *.face *.poly *.vtu *.s  *.stat *.log* *.err-0 matrixdump* *checkpoint*
