
occour = [{} for i in range(8)]


with open('input') as infile:
    for line  in infile:
        for i,c in enumerate(line[:-1]):
            print i, c
            if c in occour[i]:
                occour[i][c]+=1
            else:
                occour[i][c] = 1


for d in occour:
    a = d.keys()
    b = d.values()
    i = b.index(min(b))
    print a[i]
