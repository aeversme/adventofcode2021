def find_diff_sum_nums(scanner1, scanner2):
    s1_beacon_count = len(scanner1.beacons)
    s2_beacon_count = len(scanner2.beacons)
    diff_dict = {}
    sum_dict = {}

    for i in range(s1_beacon_count):
        for j in range(s2_beacon_count):
            diff_xx = scanner1.beacons[i].x - scanner2.beacons[j].x
            diff_xy = scanner1.beacons[i].x - scanner2.beacons[j].y
            diff_xz = scanner1.beacons[i].x - scanner2.beacons[j].z
            diff_list = [diff_xx, diff_xy, diff_xz]

            for num in diff_list:
                if num not in diff_dict.keys():
                    diff_dict[num] = 1
                else:
                    diff_dict[num] += 1

            sum_xx = scanner1.beacons[i].x + scanner2.beacons[j].x
            sum_xy = scanner1.beacons[i].x + scanner2.beacons[j].y
            sum_xz = scanner1.beacons[i].x + scanner2.beacons[j].z
            sum_list = [sum_xx, sum_xy, sum_xz]

            for num in sum_list:
                if num not in sum_dict.keys():
                    sum_dict[num] = 1
                else:
                    sum_dict[num] += 1

    return diff_dict, sum_dict


def find_shared_beacons(scanner1, scanner2):

    diff_dict, sum_dict = find_diff_sum_nums(scanner1, scanner2)

    diff_dict_filter = {k: v for (k, v) in diff_dict.items() if v >= 12}
    sum_dict_filter = {k: v for (k, v) in sum_dict.items() if v >= 12}
    if diff_dict_filter:
        print(f"=== diff_dict filtered: {diff_dict_filter}")
    if sum_dict_filter:
        print(f"=== sum_dict filtered: {sum_dict_filter}")

    # shared_s1 = []
    # shared_s2 = []
    #
    # for diff_num in diff_int:
    #     diff_s1, diff_s2 = find_diff_shared_beacons(diff_num, s1_beacon_count, s2_beacon_count, scanner1, scanner2)
    #     if len(diff_s1) >= 12:
    #         shared_s1 = diff_s1
    #         shared_s2 = diff_s2
    #         scanner2.x = diff_num
    #         break
    #     else:
    #         for sum_num in sum_int:
    #             sum_s1, sum_s2 = find_sum_shared_beacons(sum_num, s1_beacon_count, s2_beacon_count, scanner1, scanner2)
    #             if len(sum_s1) >= 12:
    #                 shared_s1 = sum_s1
    #                 shared_s2 = sum_s2
    #                 if shared_s1[0].x < 0:
    #                     scanner2.x = -sum_num
    #                 else:
    #                     scanner2.x = sum_num
    #                 break
    #
    # if not shared_s1:
    #     print(f"No shared beacons:\n     {scanner1}\n     {scanner2}")
    # else:
    #     set_scanner_y_z(shared_s1, shared_s2, scanner2)
    #     for beacon in shared_s1:
    #         beacon.shared_with = scanner2
    #     for beacon in shared_s2:
    #         beacon.shared_with = scanner1
    #
    return diff_dict_filter, sum_dict_filter


# TODO: calculate orientation of scanner2
# TODO: calculate absolute positions of scanner2 beacons
