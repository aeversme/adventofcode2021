from input_handler import convert_input

with open('test-beacons.txt') as b:
    beacons_raw = b.readlines()

beacons, scanners = convert_input(beacons_raw)

print(scanners[1].beacons[3])
