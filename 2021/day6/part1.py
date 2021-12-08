import numpy as np
import matplotlib.pyplot as plt

input_path = "test_input"
with open(input_path) as infile:
    txt = infile.read()
    data = [int(v) for v in txt.split(",")]

print(data)
ndays = 80
t=0
print(t, len(data))
for t in range(1, ndays+1):
    for i in range(len(data)):
        if data[i] == 0:
            data[i] = 6
            data.append(8)
        else:
            data[i] -= 1
    if t % 40 == 0:
        print(t, len(data))

print(len(data))

