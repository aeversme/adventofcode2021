from input_handler import convert_input
from operation_handler import check_for_reduction

with open('snailfish.txt') as s:
    snailfish_raw = s.readlines()

snailfish_homework = [convert_input(i) for i in snailfish_raw]

print(check_for_reduction([[1, 9], [18, [5, 5]]]))
