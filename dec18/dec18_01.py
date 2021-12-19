from input_handler import convert_input
from operation_handler import explode_pair

with open('snailfish.txt') as s:
    snailfish_raw = s.readlines()

snailfish_homework = [convert_input(i) for i in snailfish_raw]

explode_pair([[6, [5, [4, [3, 2]]]], 1], [3, 2])

explode_pair([7, [6, [5, [4, [3, 2]]]]], [3, 2])

explode_pair([[[[[9, 8], 1], 2], 3], 4], [9, 8])
