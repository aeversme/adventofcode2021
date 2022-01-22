from ..input_handler import convert_input


def setup():
    with open('test-reboot.txt') as file:
        data_raw = file.readlines()
    return data_raw


def test_convert_input():
    data_raw = setup()
    data = convert_input(data_raw)

    assert len(data) == 4
    assert len(data[1]) == 2
    assert data[0][1][2] == [10, 12]
