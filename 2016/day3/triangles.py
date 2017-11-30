import numpy as np

def check_tri():
    return

valid = 0
with open('input') as infile:
    for line in infile.readlines():
        tri = sorted([int(i) for i in line.split()])
        if (tri[0] + tri[1] )> tri[2]:
            valid+=1

print valid


