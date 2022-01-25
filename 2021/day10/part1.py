import numpy as np

filename = "input"
with open(filename) as infile:
    data = [line.strip() for line in infile.readlines()]

points = {")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137}

open_to_close = {
        "(":")", 
        "{":"}",
        "[":"]",
        "<":">"
}
close_to_open = {v:k for k,v in open_to_close.items()}

chunks = []
syntax_errors = []

for line in data:
    for symb in line:
        if symb in open_to_close:
            chunks.append(symb)
        elif symb in close_to_open:
            if close_to_open[symb] == chunks[-1]:
                chunks.pop(-1)
            else:
                syntax_errors.append(symb)
                break


score = sum(points[symb] for symb in syntax_errors)
print(score)
