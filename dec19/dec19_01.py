from input_handler import convert_input
from mapping_handler import find_shared_beacons

with open('test-beacons.txt') as b:
    beacons_raw = b.readlines()

scanners = convert_input(beacons_raw)

diff_int, sum_int = find_shared_beacons(scanners[0], scanners[1])
print(diff_int)
print(sum_int)
