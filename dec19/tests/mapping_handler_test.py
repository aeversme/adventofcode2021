from ..mapping_handler import find_shared_beacons
from ..input_handler import convert_input


def setup():
    with open('test-beacons.txt') as b:
        beacons_raw = b.readlines()
    scanners = convert_input(beacons_raw)
    return scanners


def test_find_shared_beacons():
    scanners = setup()
    diff_int, sum_int = find_shared_beacons(scanners[0], scanners[1])

    assert diff_int == {68, 1133}
    assert sum_int == {864, 1133, 957, 919}

