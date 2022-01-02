from input_handler import convert_input

with open('test-trenchmap.txt') as t:
    trenchmap_raw = t.readlines()

image_algorithm, trenchmap = convert_input(trenchmap_raw)
print(image_algorithm)
print(f"The image enhancement algorithm is {len(image_algorithm)} characters long.")
print(trenchmap)
