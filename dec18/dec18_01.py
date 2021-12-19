from input_handler import convert_input
from procedure_handler import addition_with_checks
from operation_handler import explode_pair

with open('test-snailfish.txt') as s:
    snailfish_raw = s.readlines()

snailfish_homework = [convert_input(i) for i in snailfish_raw]
