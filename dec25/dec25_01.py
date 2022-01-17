from input_handler import convert_input

with open('test_slugs.txt') as s:
    slugs_raw = s.readlines()

slug_map = convert_input(slugs_raw)
print(slug_map)
