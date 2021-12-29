def increment_value(number, dictionary, key):
    if number not in dictionary[key].keys():
        dictionary[key][number] = 1
    else:
        dictionary[key][number] += 1


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

            increment_value(scanner1.beacons[i].x - scanner2.beacons[j].x, diff_dict, 'diff_xx')
            increment_value(scanner1.beacons[i].x - scanner2.beacons[j].y, diff_dict, 'diff_xy')

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


def get_scanner_coordinates(*dicts):
    x = 0
    y = 0
    z = 0
    for dictionary in dicts:
        for key, value in dictionary.items():
            key_split = key.split('_')
            if key_split[1][0] == 'x':
                x = list(value.keys())[0]
            elif key_split[1][0] == 'y':
                y = list(value.keys())[0]
            else:
                z = list(value.keys())[0]
    return x, y, z


def get_scanner_transform(*dicts):
    transform_matrix = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    for dictionary in dicts:
        for key, value in dictionary.items():
            key_split = key.split('_')
            scanner1_axis = key_split[1][0]
            scanner2_axis = key_split[1][1]
            operation = key_split[0][0]

            if scanner1_axis == 'x':
                if scanner2_axis == 'x' and operation == 'd':
                    transform_matrix[0][0] = 1
                elif scanner2_axis == 'x' and operation == 's':
                    transform_matrix[0][0] = -1
                elif scanner2_axis == 'y' and operation == 'd':
                    transform_matrix[0][1] = 1
                elif scanner2_axis == 'y' and operation == 's':
                    transform_matrix[0][1] = -1
                elif scanner2_axis == 'z' and operation == 'd':
                    transform_matrix[0][2] = 1
                elif scanner2_axis == 'z' and operation == 's':
                    transform_matrix[0][2] = -1
            elif scanner1_axis == 'y':
                if scanner2_axis == 'x' and operation == 'd':
                    transform_matrix[1][0] = 1
                elif scanner2_axis == 'x' and operation == 's':
                    transform_matrix[1][0] = -1
                elif scanner2_axis == 'y' and operation == 'd':
                    transform_matrix[1][1] = 1
                elif scanner2_axis == 'y' and operation == 's':
                    transform_matrix[1][1] = -1
                elif scanner2_axis == 'z' and operation == 'd':
                    transform_matrix[1][2] = 1
                elif scanner2_axis == 'z' and operation == 's':
                    transform_matrix[1][2] = -1
            else:
                if scanner2_axis == 'x' and operation == 'd':
                    transform_matrix[2][0] = 1
                elif scanner2_axis == 'x' and operation == 's':
                    transform_matrix[2][0] = -1
                elif scanner2_axis == 'y' and operation == 'd':
                    transform_matrix[2][1] = 1
                elif scanner2_axis == 'y' and operation == 's':
                    transform_matrix[2][1] = -1
                elif scanner2_axis == 'z' and operation == 'd':
                    transform_matrix[2][2] = 1
                elif scanner2_axis == 'z' and operation == 's':
                    transform_matrix[2][2] = -1
    return transform_matrix


def find_shared_beacons(scanner1, scanner2):
    print(f"Processing {scanner1}\nand {scanner2}...")

    diff_dict, sum_dict = find_diff_sum_nums(scanner1, scanner2)

    diff_subdict_filter = {k: filter_ge_12(v) for (k, v) in diff_dict.items()}
    sum_subdict_filter = {k: filter_ge_12(v) for (k, v) in sum_dict.items()}

    diff_dict_filter = {k: v for (k, v) in diff_subdict_filter.items() if len(v) > 0}
    sum_dict_filter = {k: v for (k, v) in sum_subdict_filter.items() if len(v) > 0}
    print(diff_dict_filter)
    print(sum_dict_filter)

    if diff_dict_filter or sum_dict_filter:
        scanner2.parent_scanner = scanner1
        x, y, z = get_scanner_coordinates(diff_dict_filter, sum_dict_filter)
        print(f"x: {x}, y: {y}, z: {z}")
        scanner2.rel_x = x
        scanner2.rel_y = y
        scanner2.rel_z = z
        transform_matrix = get_scanner_transform(diff_dict_filter, sum_dict_filter)
        print(transform_matrix)
        scanner2.transform_matrix = transform_matrix
        print(scanner2)

        transformed_coordinates = scanner2.transform_beacon_coordinates()
        print(f"{scanner2.name} transformed beacons: {transformed_coordinates}")
        for i, coordinate in enumerate(transformed_coordinates):
            print(f"{coordinate}")

    else:
        print("    No shared beacons.")

    return diff_dict_filter, sum_dict_filter
