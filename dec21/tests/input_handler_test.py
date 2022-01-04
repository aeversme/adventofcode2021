from ..input_handler import convert_input


def setup():
    with open('test-dirac.txt') as d:
        start_raw = d.readlines()
    return start_raw


def test_convert_input():
    start = convert_input(setup())

    assert start == {
        'Player 1': 4,
        'Player 2': 8
    }
