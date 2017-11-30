import numpy as np
import re

with open('input') as infile:
    lines = infile.readlines()
min_length = 200
s = 0

def test_line(line):
    sline = re.split(r'[-\[]',line.strip(']\r\n'))
    name = ''.join(sline[:-2])
    number = int(sline[-2])
    checksum = sline[-1]

    letters = np.array(sorted(set(name)))[::-1]
    lcount = [name.count(l) for l in letters]
    countsort = np.argsort(lcount)[::-1]
    code = ''.join(letters[countsort])[:5]
    if code == checksum:
        return number
    else:
        return 0


for line in lines:
    s+=test_line(line)

print (s)

