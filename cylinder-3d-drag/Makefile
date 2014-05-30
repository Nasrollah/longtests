input: clean
	../../bin/gmsh2triangle src/cylinder.msh

clean:
	rm -f *.ele *.edge *.face *.node *.poly *.s *.d.* *.stat *.s *.log-0 *.err-0
	find . -name '*.vtu' | xargs -n 20 rm -f
