from input_handler import convert_input

with open('test-beacons.txt') as b:
    beacons_raw = b.readlines()

scanners = convert_input(beacons_raw)
print(f"There are {len(scanners)} scanners.")

scanners_copy = scanners.copy()
scanners[0].discover_scanner_relationships(scanners_copy)

print("\n")

for scanner in scanners:
    if scanner.child_scanners:
        print(f"*** {scanner.name} child scanner(s):")
        for child in scanner.child_scanners:
            print(f"{child}")

print("\n")

abs_coords_1 = scanners[1].calc_scanner_absolute_coordinates()
print(f"{scanners[1].name} absolute coordinates: {abs_coords_1}")

abs_coords_4 = scanners[4].calc_scanner_absolute_coordinates()
print(f"{scanners[4].name} absolute coordinates: {abs_coords_4}")

abs_coords_3 = scanners[3].calc_scanner_absolute_coordinates()
print(f"{scanners[3].name} absolute coordinates: {abs_coords_3}")

abs_coords_2 = scanners[2].calc_scanner_absolute_coordinates()
print(f"{scanners[2].name} absolute coordinates: {abs_coords_2}")

coordinates = scanners[0].transform_beacon_coordinates()
print(f"number of total coordinates: {len(coordinates)}")
uniques = {(coordinate[0], coordinate[1], coordinate[2]): coordinate for coordinate in coordinates}
print(f"number of uniques: {len(uniques)}")

with open('sample-beaconset.txt') as sbs:
    beaconset_raw = sbs.readlines()

beaconset_strip = [i.strip() for i in beaconset_raw]
beaconset_split = [i.split(',') for i in beaconset_strip]
for item in beaconset_split:
    for i in range(len(item)):
        item[i] = int(item[i])
print(beaconset_split)
beaconset = {(beacon[0], beacon[1], beacon[2]): beacon for beacon in beaconset_split}

uniques_set = set(uniques.keys())
print(uniques_set)
print(len(uniques_set))
beaconset_set = set(beaconset.keys())
print(beaconset_set)
print(len(beaconset_set))
subset = beaconset_set.issubset(uniques_set)
print(subset)
