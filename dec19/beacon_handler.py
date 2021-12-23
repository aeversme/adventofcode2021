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


def find_diff_shared_beacons(num, s1_beacon_count, s2_beacon_count, scanner1, scanner2):
    diff_s1 = []
    diff_s2 = []
    for i in range(s1_beacon_count):
        for j in range(s2_beacon_count):
            if scanner1.beacons[i].x + scanner2.beacons[j].x == num:
                diff_s1.append(scanner1.beacons[i])
                diff_s2.append(scanner2.beacons[j])
    return diff_s1, diff_s2


def find_sum_shared_beacons(num, s1_beacon_count, s2_beacon_count, scanner1, scanner2):
    sum_s1 = []
    sum_s2 = []
    for i in range(s1_beacon_count):
        for j in range(s2_beacon_count):
            if abs(scanner1.beacons[i].x) + abs(scanner2.beacons[i].x) == num:
                sum_s1.append(scanner1.beacons[i])
                sum_s2.append(scanner2.beacons[i])
    return sum_s1, sum_s2


def set_scanner_y_z(shared_s1, shared_s2, scanner2):
    if shared_s1[0].y + shared_s2[0].y == shared_s1[1].y + shared_s2[1].y:
        y_num = shared_s1[0].y + shared_s2[0].y
        scanner2.y = y_num
    else:
        y_num = abs(shared_s1[0].y) + abs(shared_s2[0].y)
        if shared_s1[0].y < 0:
            y_num = -y_num
            scanner2.y = y_num
        else:
            scanner2.y = y_num
    if shared_s1[0].z + shared_s2[0].z == shared_s1[1].z + shared_s2[1].z:
        z_num = shared_s1[0].z + shared_s2[0].z
        scanner2.z = z_num
    else:
        z_num = abs(shared_s1[0].z) + abs(shared_s2[0].z)
        if shared_s1[0].z < 0:
            z_num = -z_num
            scanner2.z = z_num
        else:
            scanner2.z = z_num


def find_shared_beacons(scanner1, scanner2):
    s1_beacon_count = len(scanner1.beacons)
    s2_beacon_count = len(scanner2.beacons)

    diff_int, sum_int = find_diff_sum_nums(scanner1, scanner2, s2_beacon_count)

    shared_s1 = []
    shared_s2 = []

    for diff_num in diff_int:
        diff_s1, diff_s2 = find_diff_shared_beacons(diff_num, s1_beacon_count, s2_beacon_count, scanner1, scanner2)
        if len(diff_s1) >= 12:
            shared_s1 = diff_s1
            shared_s2 = diff_s2
            scanner2.x = diff_num
            break
        else:
            for sum_num in sum_int:
                sum_s1, sum_s2 = find_sum_shared_beacons(sum_num, s1_beacon_count, s2_beacon_count, scanner1, scanner2)
                if len(sum_s1) >= 12:
                    shared_s1 = sum_s1
                    shared_s2 = sum_s2
                    if shared_s1[0].x < 0:
                        scanner2.x = -sum_num
                    else:
                        scanner2.x = sum_num
                    break

    if not shared_s1:
        print(f"No shared beacons:\n     {scanner1}\n     {scanner2}")
    else:
        set_scanner_y_z(shared_s1, shared_s2, scanner2)
        for beacon in shared_s1:
            beacon.shared_with = scanner2
        for beacon in shared_s2:
            beacon.shared_with = scanner1

    return shared_s1, shared_s2


# TODO: calculate orientation of scanner2
# TODO: calculate absolute positions of scanner2 beacons
