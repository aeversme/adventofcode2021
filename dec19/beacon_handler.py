def increment_value(number, dictionary, key):
    """
    Takes a number, a dictionary, and a key. If the number is not a key in the nested dictionary, adds the number as
    a key and 1 as the value. Otherwise, increments the value by 1.
    """
    if number not in dictionary[key].keys():
        dictionary[key][number] = 1
    else:
        dictionary[key][number] += 1


def find_diff_sum_nums(scanner1, scanner2):
    """
    Takes two Scanner objects. Compares the two scanners' beacon sets and compiles two dictionaries: one for the
    difference between every x, y, or z beacon coordinate from scanner 1 and every other x, y, AND z beacon coordinate
    from scanner 2, and one for the sum of the same comparisons. Returns a tuple containing the two dictionaries.
    """
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
            increment_value(scanner1.beacons[i].x - scanner2.beacons[j].z, diff_dict, 'diff_xz')

            increment_value(scanner1.beacons[i].y - scanner2.beacons[j].x, diff_dict, 'diff_yx')
            increment_value(scanner1.beacons[i].y - scanner2.beacons[j].y, diff_dict, 'diff_yy')
            increment_value(scanner1.beacons[i].y - scanner2.beacons[j].z, diff_dict, 'diff_yz')

            increment_value(scanner1.beacons[i].z - scanner2.beacons[j].x, diff_dict, 'diff_zx')
            increment_value(scanner1.beacons[i].z - scanner2.beacons[j].y, diff_dict, 'diff_zy')
            increment_value(scanner1.beacons[i].z - scanner2.beacons[j].z, diff_dict, 'diff_zz')

            increment_value(scanner1.beacons[i].x + scanner2.beacons[j].x, sum_dict, 'sum_xx')
            increment_value(scanner1.beacons[i].x + scanner2.beacons[j].y, sum_dict, 'sum_xy')
            increment_value(scanner1.beacons[i].x + scanner2.beacons[j].z, sum_dict, 'sum_xz')

            increment_value(scanner1.beacons[i].y + scanner2.beacons[j].x, sum_dict, 'sum_yx')
            increment_value(scanner1.beacons[i].y + scanner2.beacons[j].y, sum_dict, 'sum_yy')
            increment_value(scanner1.beacons[i].y + scanner2.beacons[j].z, sum_dict, 'sum_yz')

            increment_value(scanner1.beacons[i].z + scanner2.beacons[j].x, sum_dict, 'sum_zx')
            increment_value(scanner1.beacons[i].z + scanner2.beacons[j].y, sum_dict, 'sum_zy')
            increment_value(scanner1.beacons[i].z + scanner2.beacons[j].z, sum_dict, 'sum_zz')

    return diff_dict, sum_dict


def filter_ge_12(dictionary):
    """
    Takes a dictionary. Returns a dictionary with only the key-value pairs whose values are 12 or greater.
    """
    return {k: v for (k, v) in dictionary.items() if v >= 12}


def get_scanner_coordinates(*dicts):
    """
    Takes a number of dictionaries. For each dictionary, splits the key(s) and sets x, y, and z based on a character
    in the key. Returns a tuple containing x, y, and z.
    """
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
    """
    Takes a number of dictionaries. Returns a list of lists (a '3x2 matrix') based on the characters in each dictionary.
    """
    transform_matrix = [[0, 0], [0, 0], [0, 0]]
    for dictionary in dicts:
        for key, value in dictionary.items():
            key_split = key.split('_')
            scanner1_axis = key_split[1][0]
            scanner2_axis = key_split[1][1]
            operation = key_split[0]

            if scanner2_axis == 'x':
                matrix_index = 0
            elif scanner2_axis == 'y':
                matrix_index = 1
            else:
                matrix_index = 2

            if scanner1_axis == 'x':
                transform_matrix[matrix_index][0] = 0
            elif scanner1_axis == 'y':
                transform_matrix[matrix_index][0] = 1
            else:
                transform_matrix[matrix_index][0] = 2
            if operation == 'sum':
                transform_matrix[matrix_index][1] = -1
            else:
                transform_matrix[matrix_index][1] = 1

    return transform_matrix


def find_shared_beacons(scanner1, scanner2):
    """
    Takes two Scanner objects. Triggers functions to determine parent-child scanner relationships, calculate relative
    coordinates, and assemble transform matrices. Returns a tuple containing two filtered dictionaries,
    either or both of which might be empty.
    """
    # print(f"Processing {scanner1.name} and {scanner2.name}...")

    diff_dict, sum_dict = find_diff_sum_nums(scanner1, scanner2)

    diff_subdict_filter = {k: filter_ge_12(v) for (k, v) in diff_dict.items()}
    sum_subdict_filter = {k: filter_ge_12(v) for (k, v) in sum_dict.items()}

    diff_dict_filter = {k: v for (k, v) in diff_subdict_filter.items() if len(v) > 0}
    sum_dict_filter = {k: v for (k, v) in sum_subdict_filter.items() if len(v) > 0}
    # print(diff_dict_filter)
    # print(sum_dict_filter)

    if (diff_dict_filter or sum_dict_filter) and scanner2.parent_scanner is not None:
        # print(f"    {scanner2.name} already has a parent scanner, skipping relationship.")
        pass
    elif diff_dict_filter or sum_dict_filter:
        # print("    Shared beacons found.")
        scanner2.parent_scanner = scanner1
        x, y, z = get_scanner_coordinates(diff_dict_filter, sum_dict_filter)
        # print(f"x: {x}, y: {y}, z: {z}")
        scanner2.rel_x = x
        scanner2.rel_y = y
        scanner2.rel_z = z
        transform_matrix = get_scanner_transform(diff_dict_filter, sum_dict_filter)
        # print(transform_matrix)
        scanner2.transform_matrix = transform_matrix
        # print(scanner2)
    else:
        # print("    No shared beacons.")
        pass

    return diff_dict_filter, sum_dict_filter
