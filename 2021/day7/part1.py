import numpy as np
import matplotlib.pyplot as plt

input_path = "input"
with open(input_path) as infile:
    txt = infile.read()
    data = [int(v) for v in txt.split(",")]


print(int(np.sum(np.abs(data - np.round(np.median(data))))))
