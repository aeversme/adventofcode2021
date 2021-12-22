from ..input_handler import convert_input


def test_input_handler():
    data = ['--- scanner 0 ---', '-1,2,3\n', '4,5,-6\n', '', '--- scanner 1 ---', '-7, -8, 9']
    scanners = convert_input(data)

    assert any(s.name == 'scanner 0' for s in scanners)
    assert len(scanners) == 2
    assert len(scanners[0].beacons) == 2
