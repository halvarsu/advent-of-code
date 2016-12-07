import numpy as np

def check_tri():
    return

valid = 0
with open('input') as infile:
    indata = infile.readlines()

    for i in range(0,len(indata),3):
        triangles = np.array([l.split() for l in indata[i:i+3]],dtype = int).T
        for tri in triangles:
            tri = sorted(tri)
            if (tri[0] + tri[1])> tri[2]:
                valid+=1

print valid


