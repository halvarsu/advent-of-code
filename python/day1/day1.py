def part1():
    s = 0
    with open('input') as infile:
        for line in infile:
            s+= int(line)
    return s

## part 2

def part2():
    freqs = set([])
    df = []
    s = 0
    with open('input') as infile:
        delta_freqs = [line for line in infile]
        while True:
            for df in delta_freqs:
                s+= int(df)
                if s in freqs:
                    return s
                freqs.add(s)


print(part1())
print(part2())

