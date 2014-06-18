#
input: clean
	cp src/mesh.zip .
	unzip mesh.zip

clean: 
	find . -name '*vtu' | xargs -n 10 rm -f
	rm -f *.edge *.node *.face *.ele *.halo *.poly *.s
	rm -rf *checkpoint* 
	rm -f *.msh *.stat *.log-* *.err-* matrixdump* *~
	rm -rf lock_exchange_3d_*[0-9]
	rm -rf *flredecomp*
