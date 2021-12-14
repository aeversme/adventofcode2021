from pairs_handler import create_starting_dicts, insert_elements

with open('polymer.txt') as p:
    polymer_raw = p.readlines()


def count_elements(polymer_data):
    starting_polymer, pair_dict, pair_counts = create_starting_dicts(polymer_data)

    new_pair_counts = pair_counts.copy()
    for _ in range(40):
        new_pair_counts = insert_elements(pair_dict, new_pair_counts)

    element_set = set(pair_dict.values())
    element_counts = {element: 0 for element in element_set}

    for element in element_set:
        for key in new_pair_counts.keys():
            if element == key[0]:
                element_counts[element] += new_pair_counts[key]

    element_counts[starting_polymer[-1]] += 1

    highest_count = max(element_counts.values())
    lowest_count = min(element_counts.values())

    return highest_count - lowest_count


final_count = count_elements(polymer_raw)
print(f"Most common minus least common after 40 steps: {final_count}")
