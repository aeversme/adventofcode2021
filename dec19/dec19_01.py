from input_handler import convert_input

with open('beacons.txt') as b:
    beacons_raw = b.readlines()

scanners = convert_input(beacons_raw)
print(f"There are {len(scanners)} scanners.")

scanners_copy = scanners.copy()
scanners[30].discover_scanner_relationships(scanners_copy)

print("\n")

for scanner in scanners:
    print(scanner)

# print("\n")
# abs_coords_1 = scanners[1].calc_scanner_absolute_coordinates()
# print(f"{scanners[1].name} absolute coordinates: {abs_coords_1}")
# abs_coords_4 = scanners[4].calc_scanner_absolute_coordinates()
# print(f"{scanners[4].name} absolute coordinates: {abs_coords_4}")
# abs_coords_3 = scanners[3].calc_scanner_absolute_coordinates()
# print(f"{scanners[3].name} absolute coordinates: {abs_coords_3}")
# abs_coords_2 = scanners[2].calc_scanner_absolute_coordinates()
# print(f"{scanners[2].name} absolute coordinates: {abs_coords_2}")

print("\n")

coordinates = scanners[30].transform_beacon_coordinates()
print(f"number of total coordinates: {len(coordinates)}")
uniques = {(coordinate[0], coordinate[1], coordinate[2]): coordinate for coordinate in coordinates}
print(f"There are {len(uniques)} beacons.")
