filename = "input"
with open(filename) as infile:
    data = [line.strip() for line in infile.readlines()]

points = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4}

open_to_close = {
        "(":")", 
        "{":"}",
        "[":"]",
        "<":">"
}
close_to_open = {v:k for k,v in open_to_close.items()}

incomplete = []
syntax_errors = []

for line in data:
    chunks = []
    try:
        for symb in line:
            if symb in open_to_close:
                chunks.append(symb)
            elif symb in close_to_open:
                if close_to_open[symb] == chunks[-1]:
                    chunks.pop(-1)
                else:
                    raise SyntaxError(symb)
        incomplete.append(chunks)
    except SyntaxError:
        syntax_errors.append(symb)

scores = []
for chunks in incomplete:
    missing = [open_to_close[symb] for symb in chunks]
    score = 0
    for symb in missing[::-1]:
        score *= 5
        score += points[symb]
    
    print(score)
    scores.append(score)

print(sorted(scores)[len(scores)//2])
