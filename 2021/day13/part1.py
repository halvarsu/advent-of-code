import numpy as np

filename = 'input'

with open(filename) as infile:
    coords = []

    # read coordinates
    while (line := infile.readline()):
        try:
            coords.append(tuple(map(int, line.strip().split(","))))
        except ValueError:
            break

    folds = []
    while (line := infile.readline()):
        axis, value = line.split()[-1].split("=")
        folds.append((axis,int(value)))


coords = np.array(coords)[:,::-1]
if filename == 'input':
    shape = (895, 1311)
else:
    shape = np.apply_along_axis(np.max, 0, coords)+1
dots = np.zeros(shape, dtype=bool)
print(np.apply_along_axis(np.max, 0, coords))
print(np.apply_along_axis(np.min, 0, coords))
dots[coords[:,0],coords[:,1]] = 1

def print_dots(dots):
    for line in dots:
        for val in line:
            print("▀" if val else " ", end='')
        print()
print(dots.shape)

prev_axis = 'y'
for axis, line_value in folds:
    print(axis, np.sum(dots),dots.shape)
    if axis != prev_axis:
        dots = dots.T
    prev_axis = axis
    shape = (np.floor(dots.shape[0]//2).astype(int), dots.shape[1])

    new_dots = np.zeros(shape, dtype=bool)
    plus = dots.shape[0] % 2

    print(dots.shape, line_value, np.sum(dots[line_value+plus]))
    new_dots += dots[:line_value]
    new_dots += dots[line_value+plus:][::-1]
    dots = new_dots
    # print_dots(dots)

if prev_axis == 'x':
    dots = dots.T
print_dots(dots)
# print(dots.astype(int))
