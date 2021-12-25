from input_handler import convert_input
from beacon_handler import find_shared_beacons

with open('test-beacons.txt') as b:
    beacons_raw = b.readlines()

scanners = convert_input(beacons_raw)

shared_s1, shared_s2 = find_shared_beacons(scanners[0], scanners[1])
if shared_s1:
    print(f"shared from scanner 1: {shared_s1}")
    print(f"shared from scanner 2: {shared_s2}")
    print(f"s2 shares {len(shared_s2)} beacons with s1")
    print(f"{shared_s1[0]} from {scanners[0]} shared with {shared_s1[0].shared_with}")

print("Unshared beacons:")
for beacon in scanners[1].beacons:
    if beacon.shared_with is None:
        print(beacon)
