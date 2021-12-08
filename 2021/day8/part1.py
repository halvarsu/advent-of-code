import numpy as np

file = "input"

with open(file) as infile:
    txt = infile.read()
    lines = txt.split("\n")
    words = []
    for line in lines:
        words += line[line.find("|")+1:].split()

print(words)

#words = txt.replace("|", " ").replace("\n", " ").split()

lengths = [len(word) for word in words]
print(lengths)

bc = np.bincount(lengths)

unique = {1:2, 4: 4, 7:3, 8:7}
s = 0
for k,v in unique.items():
    num_count = bc[v]
    print(k, num_count)
    s += num_count
print(s)

