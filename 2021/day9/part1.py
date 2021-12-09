import numpy as np

filename = "input"
with open(filename) as infile:
    a = np.array([[int(v) for v in line.strip()] for line in infile.readlines()])

x = np.pad(a, 1, constant_values =np.max(a) + 1)
dx = np.logical_and(x[1:-1,1:-1] < x[:-2,1:-1], x[1:-1,1:-1] < x[2:,1:-1])
dy = np.logical_and(x[1:-1,1:-1] < x[1:-1,:-2], x[1:-1,1:-1] < x[1:-1,2:])
dxy = np.logical_and(dx, dy)
print(np.sum(a[dxy]+1))
