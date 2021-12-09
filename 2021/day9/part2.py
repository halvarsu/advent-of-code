import numpy as np
from scipy.ndimage import label

filename = "input"
with open(filename) as infile:
    a = np.array([[int(v) for v in line.strip()] for line in infile.readlines()])

labels, num_basins = label(a < 9)
basin_sizes = [np.sum(labels == i+1) for i in range(num_basins)]
print(np.prod(sorted(basin_sizes)[-3:]))


