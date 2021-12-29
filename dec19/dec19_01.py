from input_handler import convert_input

with open('test-beacons.txt') as b:
    beacons_raw = b.readlines()

scanners = convert_input(beacons_raw)
print(f"There are {len(scanners)} scanners.")

scanners_copy = scanners.copy()
scanners[0].discover_scanner_relationships(scanners_copy)

coordinates = scanners[0].transform_beacon_coordinates()
print(f"number of total coordinates: {len(coordinates)}")
uniques = {(coordinate[0], coordinate[1], coordinate[2]): coordinate for coordinate in coordinates}
print(f"number of uniques: {len(uniques)}")
