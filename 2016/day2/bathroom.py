import numpy as np

with open('input') as infile:
    data = [s.replace('\n','') for s in infile.readlines()]

def sgn(x):
    return 0 if x < 0 else 1

def increment(direc, coord):
    if direc == coord:
        return coord
    else:
        return coord + direc 

inst = {l:i for i,l in enumerate('URDL')}
buttons = []
x = 0
y = 0
print data
for line in data:
    for l in line:
        i = inst[l]
        j = 1 if i/2 else -1
        if i%2:
            x = increment(j,x)
        else:
            y = increment(j,y)

    print x, y




