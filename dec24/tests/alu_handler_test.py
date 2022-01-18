from ..alu_handler import alu


def test_alu():

    assert alu('add', 1, 2) == 3
    assert alu('mul', 3, 4) == 12
    assert alu('div', 4, 2) == 2
    assert alu('div', 9, 2) == 4
    assert alu('mod', 3, 2) == 1
    assert alu('mod', 7, 4) == 3
    assert alu('eql', 6, 6) == 1
    assert alu('eql', 7, 5) == 0
