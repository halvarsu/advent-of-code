import numpy as np

from part1 import get_data, simulate


expect = get_data("n2")
vals, _ = simulate(get_data("test_input2"), nstep=2)

print("HEU:")
print(expect)
print(vals)
print(expect == vals)
