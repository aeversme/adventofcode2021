from ..dec21_01 import deterministic_die_roll


def test_die_roll():
    roll1 = deterministic_die_roll(None)
    roll2 = deterministic_die_roll(3)
    roll3 = deterministic_die_roll(100)
    roll4 = [deterministic_die_roll(i) for i in range(14, 17)]
    roll5 = [deterministic_die_roll(i) for i in range(98, 101)]

    assert roll1 == 1
    assert roll2 == 4
    assert roll3 == 1
    assert roll4 == [15, 16, 17]
    assert roll5 == [99, 100, 1]
