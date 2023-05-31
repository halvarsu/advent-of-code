with open('input') as infile:
  elves = []
  curr = []
  for line in map(str.strip, infile.readlines()):
    if not line:
      elves.append(curr)
      curr = []
    else:
      curr.append(int(line))
tots = [sum(elf) for elf in elves]
# part 1
print(max(tots))
# part 2
print(sum(sorted(tots)[-3:]))
