from input_handler import convert_input


def create_insertion_list(polymer, data_dict):
    insertion_list = []
    for i in range(len(polymer) - 1):
        pair = polymer[i:i + 2]
        insertion_list.append(data_dict[pair])

    return insertion_list


def merge_elements(polymer_string, insertion_list):
    new_polymer = []
    for i in range(len(insertion_list)):
        new_polymer.append(polymer_string[i])
        new_polymer.append(insertion_list[i])
    new_polymer.append(polymer_string[-1])

    return ''.join(new_polymer)


def create_polymer(polymer_data, steps):
    starting_polymer, pair_dict = convert_input(polymer_data)

    polymer = starting_polymer
    for i in range(steps):
        insertion_list = create_insertion_list(polymer, pair_dict)
        polymer = merge_elements(polymer, insertion_list)

    return polymer
