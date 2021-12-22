from input_handler import convert_input
from mapping_handler import find_shared_beacons

with open('test-beacons.txt') as b:
    beacons_raw = b.readlines()

scanners = convert_input(beacons_raw)

shared_s1, shared_s2 = find_shared_beacons(scanners[0], scanners[1])

print(f"shared from scanner 1: {shared_s1}")
print(f"s1 shares {len(shared_s1)} beacons")
print(f"shared from scanner 2: {shared_s2}")
print(f"s2 shares {len(shared_s2)} beacons")
# print(f"updating scanner x coordinate: {scanner2}")
# print(f"{shared_s1[0]} from {scanner1} shared with {shared_s1[0].shared_with}")
