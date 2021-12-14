from input_handler import convert_input


def create_pair_count_dict(pairs):
    return {key: 0 for key in pairs.keys()}


def add_starting_pairs(polymer, counts):
    for i in range(len(polymer) - 1):
        pair = polymer[i:i + 2]
        counts[pair] += 1
    return counts


def insert_elements(pairs, counts):
    new_counts = create_pair_count_dict(pairs)
    for key in counts.keys():
        insertion_element = pairs[key]
        pair1 = key[0] + insertion_element
        pair2 = insertion_element + key[1]

        count = counts[key]

        new_counts[pair1] += count
        new_counts[pair2] += count
    return new_counts


def create_starting_dicts(polymer_data):
    starting_polymer, pair_dict = convert_input(polymer_data)
    pair_counts = create_pair_count_dict(pair_dict)
    pair_counts_with_start = add_starting_pairs(starting_polymer, pair_counts)
    return starting_polymer, pair_dict, pair_counts_with_start
