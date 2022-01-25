from collections import defaultdict
from copy import deepcopy
from part1 import *

def expand_risks(risks, dn, dm):
    n = len(risks)
    m = len(risks[0])

    print_risks(risks)
    large_risks = deepcopy(risks)

    for i in range(dm):
        for k in range(n):
            for v in large_risks[k][n*i:n*(i+1)]:
                large_risks[k].append(v % 9 + 1)

    # print_risks(large_risks)
    for j in range(dn):
        for k in range(n):
            large_risks.append([])
            for v in large_risks[j*n+k]:
                large_risks[-1].append(v % 9 + 1)
    # print_risks(large_risks)
    return large_risks



if __name__ == "__main__":
    risks = expand_risks(get_data("input"),4,4)
    print(solve(risks))
