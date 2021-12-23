import pytest
from collections import defaultdict
from part1 import get_data, count
from part2 import solve


@pytest.mark.parametrize("nstep,inp", (
    (1, "NCNBCHB"),
    (2, "NBCCNBBBCBHCB"),
    (3, "NBBBCNCCNBBNBNBBCHBHHBCHB"),
    (4, "NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB")
    ))
def test_solve(nstep, inp):
    # expect = 2188189693529

    val = solve(*get_data("test_input"), nstep)
    expect = count(inp)

    assert val == expect
