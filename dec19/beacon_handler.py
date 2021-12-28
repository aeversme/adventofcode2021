def find_diff_sum_nums(scanner1, scanner2):
    s1_beacon_count = len(scanner1.beacons)
    s2_beacon_count = len(scanner2.beacons)
    diff_dict = {
        'diff_xx': {}, 'diff_xy': {}, 'diff_xz': {},
        'diff_yx': {}, 'diff_yy': {}, 'diff_yz': {},
        'diff_zx': {}, 'diff_zy': {}, 'diff_zz': {}
    }
    sum_dict = {
        'sum_xx': {}, 'sum_xy': {}, 'sum_xz': {},
        'sum_yx': {}, 'sum_yy': {}, 'sum_yz': {},
        'sum_zx': {}, 'sum_zy': {}, 'sum_zz': {}
    }

    for i in range(s1_beacon_count):
        for j in range(s2_beacon_count):
            diff_xx = scanner1.beacons[i].x - scanner2.beacons[j].x
            if diff_xx not in diff_dict['diff_xx'].keys():
                diff_dict['diff_xx'][diff_xx] = 1
            else:
                diff_dict['diff_xx'][diff_xx] += 1
            diff_xy = scanner1.beacons[i].x - scanner2.beacons[j].y
            if diff_xy not in diff_dict['diff_xy'].keys():
                diff_dict['diff_xy'][diff_xy] = 1
            else:
                diff_dict['diff_xy'][diff_xy] += 1
            diff_xz = scanner1.beacons[i].x - scanner2.beacons[j].z
            if diff_xz not in diff_dict['diff_xz'].keys():
                diff_dict['diff_xz'][diff_xz] = 1
            else:
                diff_dict['diff_xz'][diff_xz] += 1

            diff_yx = scanner1.beacons[i].y - scanner2.beacons[j].x
            if diff_yx not in diff_dict['diff_yx'].keys():
                diff_dict['diff_yx'][diff_yx] = 1
            else:
                diff_dict['diff_yx'][diff_yx] += 1
            diff_yy = scanner1.beacons[i].y - scanner2.beacons[j].y
            if diff_yy not in diff_dict['diff_yy'].keys():
                diff_dict['diff_yy'][diff_yy] = 1
            else:
                diff_dict['diff_yy'][diff_yy] += 1
            diff_yz = scanner1.beacons[i].y - scanner2.beacons[j].z
            if diff_yz not in diff_dict['diff_yz'].keys():
                diff_dict['diff_yz'][diff_yz] = 1
            else:
                diff_dict['diff_yz'][diff_yz] += 1

            diff_zx = scanner1.beacons[i].z - scanner2.beacons[j].x
            if diff_zx not in diff_dict['diff_zx'].keys():
                diff_dict['diff_zx'][diff_zx] = 1
            else:
                diff_dict['diff_zx'][diff_zx] += 1
            diff_zy = scanner1.beacons[i].z - scanner2.beacons[j].y
            if diff_zy not in diff_dict['diff_zy'].keys():
                diff_dict['diff_zy'][diff_zy] = 1
            else:
                diff_dict['diff_zy'][diff_zy] += 1
            diff_zz = scanner1.beacons[i].z - scanner2.beacons[j].z
            if diff_zz not in diff_dict['diff_zz'].keys():
                diff_dict['diff_zz'][diff_zz] = 1
            else:
                diff_dict['diff_zz'][diff_zz] += 1

            sum_xx = scanner1.beacons[i].x + scanner2.beacons[j].x
            if sum_xx not in sum_dict['sum_xx'].keys():
                sum_dict['sum_xx'][sum_xx] = 1
            else:
                sum_dict['sum_xx'][sum_xx] += 1
            sum_xy = scanner1.beacons[i].x + scanner2.beacons[j].y
            if sum_xy not in sum_dict['sum_xy'].keys():
                sum_dict['sum_xy'][sum_xy] = 1
            else:
                sum_dict['sum_xy'][sum_xy] += 1
            sum_xz = scanner1.beacons[i].x + scanner2.beacons[j].z
            if sum_xz not in sum_dict['sum_xz'].keys():
                sum_dict['sum_xz'][sum_xz] = 1
            else:
                sum_dict['sum_xz'][sum_xz] += 1

            sum_yx = scanner1.beacons[i].y + scanner2.beacons[j].x
            if sum_yx not in sum_dict['sum_yx'].keys():
                sum_dict['sum_yx'][sum_yx] = 1
            else:
                sum_dict['sum_yx'][sum_yx] += 1
            sum_yy = scanner1.beacons[i].y + scanner2.beacons[j].y
            if sum_yy not in sum_dict['sum_yy'].keys():
                sum_dict['sum_yy'][sum_yy] = 1
            else:
                sum_dict['sum_yy'][sum_yy] += 1
            sum_yz = scanner1.beacons[i].y + scanner2.beacons[j].z
            if sum_yz not in sum_dict['sum_yz'].keys():
                sum_dict['sum_yz'][sum_yz] = 1
            else:
                sum_dict['sum_yz'][sum_yz] += 1

            sum_zx = scanner1.beacons[i].z + scanner2.beacons[j].x
            if sum_zx not in sum_dict['sum_zx'].keys():
                sum_dict['sum_zx'][sum_zx] = 1
            else:
                sum_dict['sum_zx'][sum_zx] += 1
            sum_zy = scanner1.beacons[i].z + scanner2.beacons[j].y
            if sum_zy not in sum_dict['sum_zy'].keys():
                sum_dict['sum_zy'][sum_zy] = 1
            else:
                sum_dict['sum_zy'][sum_zy] += 1
            sum_zz = scanner1.beacons[i].z + scanner2.beacons[j].z
            if sum_zz not in sum_dict['sum_zz'].keys():
                sum_dict['sum_zz'][sum_zz] = 1
            else:
                sum_dict['sum_zz'][sum_zz] += 1
    return diff_dict, sum_dict


def filter_ge_12(dictionary):
    return {k: v for (k, v) in dictionary.items() if v >= 12}


def find_shared_beacons(scanner1, scanner2):

    diff_dict, sum_dict = find_diff_sum_nums(scanner1, scanner2)

    diff_subdict_filter = {k: filter_ge_12(v) for (k, v) in diff_dict.items()}
    sum_subdict_filter = {k: filter_ge_12(v) for (k, v) in sum_dict.items()}

    diff_dict_filter = {k: v for (k, v) in diff_subdict_filter.items() if len(v) > 0}
    sum_dict_filter = {k: v for (k, v) in sum_subdict_filter.items() if len(v) > 0}

    # if diff_dict_filter:
    #     print(f"=== diff_dict filtered: {diff_dict_filter}")
    # if sum_dict_filter:
    #     print(f"=== sum_dict filtered: {sum_dict_filter}")

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
