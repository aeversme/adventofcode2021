from polymer_handler import create_polymer

with open('polymer.txt') as p:
    polymer_raw = p.readlines()


def count_elements(polymer):
    polymer_set = set(polymer)

    element_counts = {element: polymer.count(element) for element in polymer_set}
    highest_count = max(element_counts.values())
    lowest_count = min(element_counts.values())

    return highest_count - lowest_count


final_polymer = create_polymer(polymer_raw, 10)
element_count = count_elements(final_polymer)
print(f"Most common minus least common: {element_count}")
