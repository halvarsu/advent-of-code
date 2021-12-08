# power = gamma rate * epsilon rate ( ? )

# gamma = each bit is the most common bit in column of numbers
# epsilon: least common rate, or rather the inv of gamma

import numpy as np

file = 'input'
with open(file) as infile:
    lines = infile.readlines()
    vals = [[int(v) for v in line.strip()] for line in lines if line]

a = np.array(vals, dtype=bool)

bincounts = [np.bincount(col) for col in a.T]
most_common_bits = [np.argmax(bins) for bins in bincounts]
# np.median(a, axis=0).astype(int)
least_common_bits = [np.argmin(bins) for bins in bincounts]
# 1-most_common_bits

print(most_common_bits)
print(least_common_bits)

def convert_bits_to_int(bits):
    return sum(v*2**i for i,v in enumerate(bits[::-1]))

gamma = convert_bits_to_int(most_common_bits)
epsilon = convert_bits_to_int(least_common_bits)
print(gamma, epsilon, gamma*epsilon)

# part two:
# multiplying the oxygen generator rating by the CO2 scrubber rating.

oxygen = 0
co2 = 0

print(a.shape)


def get_part_two_val(a, get_max=True):
    numbers = a.copy()
    bit_place = 0
    base_target = int(get_max)
    while len(numbers) > 1:
        print(bit_place, len(numbers))
        if len(numbers) == 2:
            numbers = numbers[numbers[:,bit_place] == base_target]
            break
        bins = np.bincount(numbers[:,bit_place])
        if bins[0] == bins[1]:
            target = base_target
        elif get_max:
            target = np.argmax(bins)
        else:
            target = np.argmin(bins)
        numbers = numbers[numbers[:,bit_place] == target]
        bit_place += 1
    return convert_bits_to_int(numbers[0])


def get_oxygen(a):
    return get_part_two_val(a, get_max=True)
def get_co2(a):
    return get_part_two_val(a, get_max=False)
o2 = get_oxygen(a)
co2 = get_co2(a)
print(o2, co2, o2*co2)
