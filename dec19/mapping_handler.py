def find_diff_sum_nums(scanner1, scanner2, s2_beacon_count):
    diff_set_0 = set()
    sum_set_0 = set()

    for i in range(s2_beacon_count):
        diff_set_0.add(scanner1.beacons[0].x + scanner2.beacons[i].x)
        sum_set_0.add(abs(scanner1.beacons[0].x) + abs(scanner2.beacons[i].x))

    diff_set_1 = set()
    sum_set_1 = set()

    for j in range(s2_beacon_count):
        diff_set_1.add(scanner1.beacons[1].x + scanner2.beacons[j].x)
        sum_set_1.add(abs(scanner1.beacons[1].x) + abs(scanner2.beacons[j].x))

    diff_int = diff_set_0.intersection(diff_set_1)
    sum_int = sum_set_0.intersection(sum_set_1)

    return diff_int, sum_int


def determine_diff_shared_beacons(num, s1_beacon_count, s2_beacon_count, scanner1, scanner2):
    diff_s1 = []
    diff_s2 = []
    for i in range(s1_beacon_count):
        for j in range(s2_beacon_count):
            if scanner1.beacons[i].x + scanner2.beacons[j].x == num:
                diff_s1.append(scanner1.beacons[i])
                diff_s2.append(scanner2.beacons[j])
    return diff_s1, diff_s2


def determine_sum_shared_beacons(num, s1_beacon_count, s2_beacon_count, scanner1, scanner2):
    sum_s1 = []
    sum_s2 = []
    for i in range(s1_beacon_count):
        for j in range(s2_beacon_count):
            if abs(scanner1.beacons[i].x) + abs(scanner2.beacons[i].x) == num:
                sum_s1.append(scanner1.beacons[i])
                sum_s2.append(scanner2.beacons[i])
    return sum_s1, sum_s2


def find_shared_beacons(scanner1, scanner2):
    s1_beacon_count = len(scanner1.beacons)
    s2_beacon_count = len(scanner2.beacons)

    diff_int, sum_int = find_diff_sum_nums(scanner1, scanner2, s2_beacon_count)

    shared_s1 = []
    shared_s2 = []

    for num in diff_int:
        diff_s1, diff_s2 = determine_diff_shared_beacons(num, s1_beacon_count, s2_beacon_count, scanner1, scanner2)
        if len(diff_s1) >= 12:
            shared_s1 = diff_s1
            shared_s2 = diff_s2
            scanner2.x = num
            break

    if not shared_s1:
        for num in sum_int:
            sum_s1, sum_s2 = determine_sum_shared_beacons(num, s1_beacon_count, s2_beacon_count, scanner1, scanner2)
            if len(sum_s1) >= 12:
                shared_s1 = sum_s1
                shared_s2 = sum_s2
                break

    # scanner1.beacons[i].shared_with = scanner2
    # scanner2.beacons[j].shared_with = scanner1

    return shared_s1, shared_s2
