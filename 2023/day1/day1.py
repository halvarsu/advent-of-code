import regex as re

STRING_NUMBERS = "one,two,three,four,five,six,seven,eight,nine".split(",")
TO_NUM = {s: str(i + 1) for i, s in enumerate(STRING_NUMBERS)}
TO_NUM.update({num: num for num in TO_NUM.values()})
print(TO_NUM)


def test_part2():
    test_inp = """two1nine
  eightwothree
  abcone2threexyz
  xtwone3four
  4nineeightseven2
  zoneight234
  7pqrstsixteen"""

    part2(inp=test_inp)


def test():
    test_inp = """1abc2
  pqr3stu8vwx
  a1b2c3d4e5f
  treb7uchet"""

    part1(inp=test_inp)


def run(inp, pattern=r"\d"):
    s = 0
    for line in inp.split("\n"):
        if not line:
            continue
        matches = re.findall(pattern, line, overlapped=True)
        # print(line)
        # print(matches)
        if matches:
            s += int(TO_NUM[matches[0]] + TO_NUM[matches[-1]])
            print(matches[0], matches[-1])
        else:
            print("err", line)
    print(s)


def part1(inp=None):
    if inp is None:
        inp = load_inp("input")
    run(inp)


def part2(inp=None):
    if inp is None:
        inp = load_inp("input")

    pattern = "(" + "|".join(STRING_NUMBERS) + r"|\d" + ")"
    # print(pattern)
    # print(re.findall(pattern, "one123twofour"))
    print(run(inp, pattern))


def load_inp(filename):
    with open(filename) as infile:
        return infile.read()


if __name__ == "__main__":
    # print("Running test")
    # test()
    # print("Running part 1")
    # part1()
    # print("Running test 2")
    # test_part2()
    print("Running part 2")
    part2()
