import numpy as np
import matplotlib.pyplot as plt

input_path = "input"
with open(input_path) as infile:
    txt = infile.read()
    data = np.array([int(v) for v in txt.split(",")])



def get_fuel(pos, data):
    n = np.abs(data - pos)
    return (int(np.sum((n*(n+1))/2)))


# brute force check all
fuel_use = [get_fuel(i, data) for i in range(min(data), max(data)+1)]
print(np.min(fuel_use))

