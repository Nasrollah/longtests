input: clean
	../../bin/gmsh2triangle --2d src/2d_square.msh

clean:
	rm -rf *.stat *.vtu *.node *.ele *.edge *checkpoint* *convergence* *.log

merged_mesh:
	mpiexec unifiedmesh explicit-hyperc-shear-conservative_CoordinateMesh_0_checkpoint explicit-hyperc-shear-conservative_checkpoint_CoordinateMesh_16_checkpoint merged_mesh
