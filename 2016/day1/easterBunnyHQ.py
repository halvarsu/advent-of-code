import numpy as np
import matplotlib.pyplot as plt

with open('input') as infile:
    data = infile.readline().replace(' ','').replace('\n','').split(',')

x = 0
y = 0
heading = 0

positions = np.zeros((len(data),2))
for i,c in enumerate(data):
    if c[0] == 'R':
        heading = (heading + 1)%4
    elif c[0] == 'L':
        heading = (heading - 1)%4
    if (heading%2):
        y+=int(c[1:]) if heading/2 == 0 else -int(c[1:])
    else:
        x+=int(c[1:]) if heading/2 == 0 else -int(c[1:])
    positions[i] = (x,y)

print x, y
print abs(x)+abs(y)
plt.plot(positions[:,0],positions[:,1])
plt.scatter(positions[0,0],positions[0,1])
plt.show()
