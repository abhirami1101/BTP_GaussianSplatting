import trimesh
import numpy as np
import sys

filename = sys.argv[1]
mesh = trimesh.load(filename, process=False)
points = mesh.vertices
np.savetxt(filename[:-3] + "xyz", points, fmt="%.6f")
