from ..dec21_01 import deterministic_die_roll, game_turn
from ..player_handler import Player


def setup():
    with open('test-dirac.txt') as d:
        dirac_raw = d.readlines()
    dirac_strip = [i.strip('\n') for i in dirac_raw]
    player_list = []
    for player in dirac_strip:
        player_list.append([player[:8], int(player[-1])])
    players = [Player(player[0], player[1]) for player in player_list]
    return players


def test_die_roll():
    roll1 = deterministic_die_roll(0)
    roll2 = deterministic_die_roll(3)
    roll3 = deterministic_die_roll(100)
    roll4 = [deterministic_die_roll(i) for i in range(14, 17)]
    roll5 = [deterministic_die_roll(i) for i in range(98, 101)]

    assert roll1 == 1
    assert roll2 == 4
    assert roll3 == 1
    assert roll4 == [15, 16, 17]
    assert roll5 == [99, 100, 1]


def test_game_turn():
    players = setup()
    last_roll = 0
    roll_count = 0
    next_player = players[0]
    for _ in range(5):
        last_roll, next_player = game_turn(next_player, players, last_roll, roll_count)

    assert last_roll == 15
    assert players[1].space == 6
    assert players[0].score == 20
    assert next_player == players[1]
