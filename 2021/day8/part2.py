import numpy as np

file = "input"

with open(file) as infile:
    txt = infile.read()
    lines = txt.split("\n")
    signals = []
    outputs = []
    for line in lines:
        if not line:
            continue
        delim = line.find("|")

        signals.append(["".join(sorted(word)) for word in line[:delim].split()])
        outputs.append(["".join(sorted(word)) for word in line[delim+1:].split()])

# out_lengths = [len(word) for word in output]
# sig_lengths = [len(word) for word in signal]
# print(out_lengths)


#      0:      1:      2:      3:      4:
#    aaaa    ....    aaaa    aaaa    ....
#   b    c  .    c  .    c  .    c  b    c
#   b    c  .    c  .    c  .    c  b    c
#    ....    ....    dddd    dddd    dddd
#   e    f  .    f  e    .  .    f  .    f
#   e    f  .    f  e    .  .    f  .    f
#    gggg    ....    gggg    gggg    ....
#
#     5:      6:      7:      8:      9:
#    aaaa    aaaa    aaaa    aaaa    aaaa
#   b    .  b    .  .    c  b    c  b    c
#   b    .  b    .  .    c  b    c  b    c
#    dddd    dddd    ....    dddd    dddd
#   .    f  e    f  .    f  e    f  .    f
#   .    f  e    f  .    f  e    f  .    f
#    gggg    gggg    ....    gggg    gggg

# lengths = {_1:2, 2:5, 3:5, _4:4, 5:5, 6:6, _7:3, _8:7, 9:6}


def get_symbols(signal):
    signal = np.array(signal)
    lengths = np.array([len(word) for word in signal])
    symbols = {}
    symbols[1] = signal[np.where(lengths == 2)[0]][0]
    symbols[4] = signal[np.where(lengths == 4)[0]][0]
    symbols[7] = signal[np.where(lengths == 3)[0]][0]
    symbols[8] = signal[np.where(lengths == 7)[0]][0]
    cf = symbols[1]
    # loop through numbers with 6 characters
    for six in signal[np.where(lengths == 6)[0]]:
        has_cf = [int(cf_symb in six) for cf_symb in cf]
        if sum(has_cf) == 1:
            symbols[6] = six
            c = cf[has_cf[0]]
            f = cf[has_cf[1]]
        elif all(four_char in six for four_char in symbols[4]):
            symbols[9] = six
        else:
            symbols[0] = six
    # loop through numbers with 5 characters
    for five in signal[np.where(lengths == 5)[0]]:
        if c in five and f in five:
            symbols[3] = five
        elif c in five:
            symbols[2] = five
        else:
            symbols[5] = five
    return symbols

s = 0
for signal, output in zip(signals, outputs):
    symbs = get_symbols(signal)
    values = {v:k for k,v in symbs.items()}
    readout = sum(values[symb]*10**i for i,symb in enumerate(output[::-1]))
    s += readout
    print(output, readout)
print(s)

