hand_map = {"A":0, "B":1, "C":2}

num_map = {v:k for k,v in hand_map.items()}
result_map = {"X": 0, # lose
              "Y": 3, # draw
              "Z": 6} # win

s = 0
with open('input') as infile:
  for other, res in map(str.split, map(str.strip, infile.readlines())):
    val_other = hand_map[other]
    if res == "X":
      val_own = (val_other-1) % 3
    if res == "Y":
      val_own = val_other
    if res == "Z":
      val_own = (val_other+1) % 3
    _s = 0
    _s += val_own + 1
    _s += result_map[res]
    print(other, res, val_other, val_own, _s)
    s+= _s

print(s)

# part 1
# print(other)
# part 2
