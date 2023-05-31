other_map = {"A":1, "B":2, "C":3}
own_map = {"X": 1, "Y": 2, "Z": 3}

s = 0
with open('input') as infile:
  for other, own in map(str.split, map(str.strip, infile.readlines())):
    val_other = other_map[other]
    val_own = own_map[own]
    diff = (val_own - val_other) % 3
    s += val_own
    # loss
    if diff == 2:
      s+=0
    # draw
    if diff == 0:
      s+=3
    # win
    if diff == 1:
      s+=6
print(s)

# part 1
# print(other)
# part 2
