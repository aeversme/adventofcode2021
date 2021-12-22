def find_shared_beacons(scanner1, scanner2):
    # TODO: make this first part a sub-function
    diff_set_0 = set()
    diff_set_1 = set()
    sum_set_0 = set()
    sum_set_1 = set()

    s1_beacon_count = len(scanner1.beacons)
    s2_beacon_count = len(scanner2.beacons)

    for i in range(s2_beacon_count):
        diff_set_0.add(scanner1.beacons[0].x + scanner2.beacons[i].x)
        sum_set_0.add(abs(scanner1.beacons[0].x) + abs(scanner2.beacons[i].x))

    for j in range(s2_beacon_count):
        diff_set_1.add(scanner1.beacons[1].x + scanner2.beacons[j].x)
        sum_set_1.add(abs(scanner1.beacons[1].x) + abs(scanner2.beacons[j].x))

    diff_int = diff_set_0.intersection(diff_set_1)
    sum_int = sum_set_0.intersection(sum_set_1)

    # --- end sub-function ---

    shared_s1 = []
    shared_s2 = []

    # TODO: make some or all of this a sub-function
    for num in diff_int:
        diff_s1 = []
        diff_s2 = []
        for k in range(s1_beacon_count):
            for m in range(s2_beacon_count):
                if scanner1.beacons[k].x + scanner2.beacons[m].x == num:
                    diff_s1.append(scanner1.beacons[k])
                    scanner1.beacons[k].shared_with = scanner2
                    diff_s2.append(scanner2.beacons[m])
                    scanner2.beacons[m].shared_with = scanner1
        if len(diff_s1) >= 12:
            shared_s1 = diff_s1
            shared_s2 = diff_s2
            scanner2.x = num
            break

    # --- end sub-function ---

    print(f"shared from scanner 1: {shared_s1}")
    print(f"s1 shares {len(shared_s1)} beacons")
    print(f"shared from scanner 2: {shared_s2}")
    print(f"s2 shares {len(shared_s2)} beacons")
    print(f"updating scanner x coordinate: {scanner2}")
    print(f"{shared_s1[0]} from {scanner1} shared with {shared_s1[0].shared_with}")

    return diff_int, sum_int
