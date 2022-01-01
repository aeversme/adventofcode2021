from ..beacon_handler import find_shared_beacons, find_diff_sum_nums
from ..input_handler import convert_input


def setup():
    with open('test-beacons.txt') as b:
        beacons_raw = b.readlines()
    scanners = convert_input(beacons_raw)
    return scanners


def test_find_diff_sum_nums():
    scanners = setup()
    diff_dict, sum_dict = find_diff_sum_nums(scanners[0], scanners[1])

    assert len(diff_dict) == 1271
    assert len(sum_dict) == 1303
    assert sum_dict[68] == 12


def test_find_shared_beacons():
    assert True

