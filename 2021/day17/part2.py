import numpy as np

filename = "input"
with open(filename) as infile:
    txt = infile.read()

(x0, xm), (y0, ym) = [[int(val.replace(",",""))
                      for val in word.split("=")[1].split("..")]
                      for word in txt.split()[-2:]]
# y0 = abs(int(.split("=")[-1]))

max_steps = max(2*abs(y0) + 1, int((np.sqrt(1+8*xm)-1)/2))
vx_max = xm + 1
vx_min = int((np.sqrt(1 + 8*x0) - 1)/2)
nvx = vx_max - vx_min

assert y0 < 0
vy_max = - y0
vy_min = y0
ny = vy_max + vy_min + 1
vy0 = np.arange(vy_min, vy_max+1)
vx0 = np.arange(vx_min, vx_max+1)

in_box = np.zeros((max_steps, vy0.shape[0], vx0.shape[0]), dtype=bool)

vx, vy = np.meshgrid(vx0, vy0)
x = np.zeros_like(vx)
y = np.zeros_like(vx)

def is_in_box(x,y,x0,xm,y0,ym):
    return np.logical_and(
            np.logical_and(x0 <= x, x <= xm),
            np.logical_and(y0 <= y, y <= ym))

already_counted = np.zeros_like(vx, dtype=bool)

for i in range(max_steps):
    x += vx
    y += vy
    vx[vx > 0] -= 1
    vy -= 1
    mask = is_in_box(x,y,x0,xm,y0,ym)
    mask[already_counted] = 0
    already_counted[mask] = 1
    in_box[i][mask] = 1
    print(x[8,6],y[8,6], already_counted[8, 6])

print(np.sum(in_box))
