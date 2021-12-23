from part1 import iterate, get_data, calc_value, count

def test_iterate():
    expect = ["NNCB",
            "NCNBCHB",
            "NBCCNBBBCBHCB",
            "NBBBCNCCNBBNBNBBCHBHHBCHB",
            "NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB"]

    inp, conv_form = get_data("test_input")
    assert expect[0] == inp, f"failed at step {i}, "
    for i, expect_val in enumerate(expect[1:]):
        inp = iterate(inp, conv_form)
        assert expect_val == inp, f"failed at step {i}, "


def test_count():
    inp = "NBCCNBBBCBHCB"
    expect = {"C":4, "B":6, "N":2, "H":1}
    counts = count(inp)
    assert counts == expect


def test_calc_value():
    expect = 1588
    inp, conv_form = get_data("test_input")

    for i in range(10):
        inp = iterate(inp, conv_form)
    assert calc_value(inp) == expect





