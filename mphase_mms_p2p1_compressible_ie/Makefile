input:	clean
	./copy_script

run:
	@echo **********Running simulations
	mpiexec ../../bin/fluidity MMS_A.flml
	mpiexec ../../bin/fluidity MMS_B.flml
	mpiexec ../../bin/fluidity MMS_C.flml

clean:
	rm -f *.vtu *.stat *.s *.log *_A* *_B* *_C* matrix* *~ mphase_mms_p2p1_compressible_ie.py *.pyc fluidity.*
