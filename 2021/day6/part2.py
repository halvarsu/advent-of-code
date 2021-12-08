import numpy as np
import matplotlib.pyplot as plt

input_path = "input"
with open(input_path) as infile:
    txt = infile.read()
    data = [int(v) for v in txt.split(",")]


def get_num_children(days_left):
    if days_left < 7:
        return 1
    else:
        a = get_num_children(days_left - 7)
        b = get_num_children(days_left - 9)
        return a + b

def get_num_children_stored(days_left, prev={1:1}):
    """Passes through a dict for fast route for earlier explored alternatives"""
    if days_left in prev:
        pass
    elif days_left < 7:
        prev[days_left] = 1
    else:
        a, prev = get_num_children_stored(days_left - 7, prev=prev)
        b, prev = get_num_children_stored(days_left - 9, prev=prev)
        prev[days_left] = a + b
    return prev[days_left], prev


ndays = 256
s = 0

prev = {1:1}
for i in range(ndays+6):
    num, prev = get_num_children_stored(i, prev)
    print(num)


for fish in data:
    out = prev[ndays + 6 - fish]#get_num_children(ndays + 6 - fish)
    print("Fish:", out)
    s+=out

print(s)
