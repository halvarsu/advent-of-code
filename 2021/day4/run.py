import numpy as np
import matplotlib.pyplot as plt

# input_path = "test_input"
input_path = "input"
with open(input_path) as infile:
    txt = infile.read()
    lines = txt.split("\n")
    numbers = [int(v) for v in lines[0].split(",")]

    nboards = len(lines[1:]) // 6
    boards = np.zeros((nboards, 5,5))
    j = 0
    for i in range(2, len(lines[1:]), 6):
        board_lines = lines[i:i+5]
        board = np.array([line.split() for line in board_lines], dtype=int)
        boards[j] = board
        j+=1


def check_won(marked):
    won_col = np.any(np.all(marked, axis=1), axis=1)
    won_row = np.any(np.all(marked, axis=2), axis=1)
    return np.where(np.logical_or(won_col, won_row))[0]

marked = np.zeros_like(boards, dtype=bool)
has_won = np.zeros(boards.shape[0])

winners = []
for i, num in enumerate(numbers):
    print(i, num)
    marked[boards == num] = 1
    for ind in check_won(marked):
        if not has_won[ind]:
            value = num * np.sum(boards[ind][~marked[ind]])
            winners.append((i,num,ind, int(value)))
            has_won[ind] = True

print(winners)
