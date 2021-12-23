from collections import defaultdict
from copy import copy
from part1 import get_data, calc_value, count


def get_outputs(conv_form):
    return {k:(k[0]+v, v+k[1]) for k,v in conv_form.items()}

def count_pairs(inp):
    pair_counts = defaultdict(int)
    n = len(inp)
    for i in range(1, n):
        e1 = inp[n-i-1]
        e2 = inp[n-i]
        pair_counts[e1+e2] += 1
    return pair_counts

def solve(inp, conv_form, nstep):
    out_pairs = get_outputs(conv_form)
    pair_counts = count_pairs(inp)
    letter_counts = count(inp)

    print(pair_counts)
    for i in range(nstep):
        pair_counts, letter_counts = iterate(pair_counts,
                letter_counts, out_pairs, conv_form)

    most = max(letter_counts.values())
    least = min(letter_counts.values())
    return most - least

def iterate(pair_counts, letter_counts, out_pairs, conv_form):
    next_counts = copy(pair_counts)
    print("iterate")
    for k,v in pair_counts.items():
        out_letter = conv_form[k]
        letter_counts[out_letter] += v
        a,b = out_pairs[k]
        print(k, v, a, b)
        next_counts[k] -= v
        next_counts[a] += v
        next_counts[b] += v
    print(next_counts)
    return next_counts, letter_counts



if __name__ == '__main__':
    print(solve(*get_data("input"), nstep=40))
