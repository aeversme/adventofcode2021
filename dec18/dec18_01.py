from input_handler import convert_input

with open('snailfish.txt') as s:
    snailfish_raw = s.readlines()

snailfish_homework = [convert_input(i) for i in snailfish_raw]
