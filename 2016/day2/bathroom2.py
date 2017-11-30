import numpy as np

with open('input') as infile:
    data = [s.replace('\n','') for s in infile.readlines()]

def sgn(x):
    return 0 if x < 0 else 1


instructions = {l:i for i,l in enumerate('URDL')}
buttons = []
x = 0
y = 0
print data
pos = [x,y]
for line in data:
    for l in line:
        dist = abs(x) + abs(y)
        i = instructions[l]

        sign = 1 if i/2 else -1
        direction = i%2
        pos1 = pos[direction]
        pos2 = pos[not direction]
        dist = abs(x) + abs(y)
        if dist < 2:

            
        elif abs(pos1)==2 and sgn(pos1) == sgn(s):
            continue
    print x, y
