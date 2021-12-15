from input_handler import convert_input

with open('test-chiton.txt') as c:
    chiton_raw = c.readlines()


chiton_map = convert_input(chiton_raw)
print(chiton_map)
