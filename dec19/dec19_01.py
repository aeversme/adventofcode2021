from input_handler import convert_input

with open('beacons.txt') as b:
    beacons_raw = b.readlines()


def map_ocean(data):
    """
    Takes a list of scanner names and beacon coordinates. Returns a list of Scanner objects and a list of unique
    beacons.
    """
    scanner_list = convert_input(data)
    print(f"There are {len(scanner_list)} scanners.")

    scanners_copy = scanner_list.copy()
    print("\nDiscovering scanner relationships...")
    result = scanner_list[0].discover_scanner_relationships(scanners_copy)
    if result == 0:
        print("All scanner relationships processed.")

    print("\nPrinting scanners...")
    for scanner in scanner_list:
        print(scanner)

    print("\nCalculating scanner absolute coordinates...")
    for n in range(1, len(scanner_list)):
        scanner_list[n].calc_scanner_absolute_coordinates(scanner_list[n].rel_xyz())
        print(f"{scanner_list[n].name} absolute coordinates: {scanner_list[n].abs_xyz()}")

    print("\nCompiling list of unique beacons...")
    coordinates = scanner_list[0].transform_beacon_coordinates()
    uniques = {(coordinate[0], coordinate[1], coordinate[2]): coordinate for coordinate in coordinates}
    return scanner_list, uniques


scanners, unique_beacons = map_ocean(beacons_raw)
print(f"There are {len(unique_beacons)} beacons.")


def calc_biggest_distance(scanner_list):
    """
    Takes a list of scanners. Returns the biggest straight-line distance between any two scanners in the list.
    """
    print("\nCalculating largest distance between beacons...")
    biggest_distance = 0
    for i in range(len(scanner_list)):
        for j in range(len(scanner_list)):
            if i != j:
                s1_xyz = scanner_list[i].abs_xyz()
                s2_xyz = scanner_list[j].abs_xyz()
                distance = (s1_xyz[0] - s2_xyz[0]) + (s1_xyz[1] - s2_xyz[1]) + (s1_xyz[2] - s2_xyz[2])
                if distance > biggest_distance:
                    biggest_distance = distance
    return biggest_distance


print(f"The largest distance between scanners is {calc_biggest_distance(scanners)} units.")
