import numpy as np
import matplotlib.pyplot as plt

input_path = "input"
with open(input_path) as infile:
    txt = infile.read()
    lines = txt.split("\n")
    paths = []
    for line in lines:
        if not line:
            continue
        line = line.split(" -> ")
        x0,y0 = map(int, line[0].split(","))
        x1,y1 = map(int, line[1].split(","))
        paths.append(((x0,y0),(x1,y1)))

paths = np.array(paths, dtype=int)
# ensure smallest number first
# paths = np.sort(paths, axis=1)
is_non_diag = np.any((np.diff(paths, axis=1) == 0)[:,0],axis=1)
non_diag_paths = paths[is_non_diag]

board1 = np.zeros((np.max(paths[:,:,0])+1, np.max(paths[:,:,1])+1))
board2 = np.zeros((np.max(paths[:,:,0])+1, np.max(paths[:,:,1])+1))

for ((x0,y0), (x1,y1)) in paths:
    # slice arrays
    xdir = 1-2*(x0 > x1)
    ydir = 1-2*(y0 > y1)
    sx = np.r_[x0:x1+xdir:xdir]
    sy = np.r_[y0:y1+ydir:ydir]
    board2[sx,sy] += 1
    if x0 != x1 and y0 != y1:
        continue
    board1[sx,sy] += 1

def print_board(board):
    for line in board:
        for val in line:
            print(int(val) if val else '.', end='')
        print()
# print_board(board1.T)
print()
# print_board(board2.T)
print()

print(np.sum(board1 > 1))
print(np.sum(board2 > 1))

plt.imshow(board2)
plt.show()
