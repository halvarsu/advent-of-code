import numpy as np

with open('input') as infile:
    data = [s.replace('\n','') for s in infile.readlines()]

def sgn(x):
    return 0 if x < 0 else 1


instructions = {l:i for i,l in enumerate('RULD')}
buttons = []
for i in range(-2,3):
    for j in range(-2,3):
        if abs(i) + abs(j) < 3:
            buttons.append([i,j])
moves = []
print data
pos = [-2,0]
for line in data:
    pos = [-2,0]
    for l in line:
        i = instructions[l]
        newpos = pos[:]
        newpos[i%2]+= -1 if i//2 else 1
        if newpos in buttons:
            pos = newpos


    print pos

print type(newpos), type(buttons[0])

for  l in 'RULD':
    i = instructions[l]
    print l, i % 2, i // 2
