from ..input_handler import convert_input


def setup():
    with open('test-dirac.txt') as d:
        player_list = d.readlines()
    return player_list


def test_convert_input():
    player_list = convert_input(setup())

    assert player_list == [['Player 1', 4], ['Player 2', 8]]
