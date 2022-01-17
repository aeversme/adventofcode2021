from input_handler import convert_input
from movement_handler import movement_step

with open('test_slugs.txt') as s:
    slugs_raw = s.readlines()

slug_map = convert_input(slugs_raw)
print(slug_map)

line1 = ['...>>>>>...']
new_line = movement_step(line1)
print(new_line)
another_new_line = movement_step(new_line)
print(another_new_line)
