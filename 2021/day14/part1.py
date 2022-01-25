from collections import defaultdict

def get_data(filename):
    with open(filename) as infile:
        inp = infile.readline().strip()
        infile.readline()

        conv_form = {}
        for line in infile.readlines():
            a,b = line.strip().split("->")
            conv_form[a.strip()] = b.strip()
        return inp, conv_form


def solve(inp, conv_form, nstep=10):
    for i in range(nstep):
        inp = iterate(inp, conv_form)
    return calc_value(inp)




def count(inp):
    v = defaultdict(int)
    for s in inp:
        v[s] += 1
    return v

def calc_value(inp):
    counts = count(inp)
    most_common = max(counts, key=counts.get)
    least_common = min(counts, key=counts.get)
    return counts[most_common] - counts[least_common]


def iterate(inp, conv_form):
    inp = list(inp)
    # for e1, e2 in zip(inp[:-1], inp[1:]):
    n = len(inp)
    for i in range(1, n):
        e1 = inp[n-i-1]
        e2 = inp[n-i]
        inp.insert(n-i, conv_form[e1 + e2])
    return "".join(inp)



if __name__ == '__main__':
    print(solve(*get_data("input")))
