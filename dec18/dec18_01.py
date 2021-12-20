from input_handler import convert_input
from procedure_handler import addition_with_checks
from operation_handler import calculate_magnitude

with open('snailfish.txt') as s:
    snailfish_raw = s.readlines()

snailfish_homework = [convert_input(i) for i in snailfish_raw]


def complete_homework(data):
    number = data[0]
    for i in range(len(data) - 1):
        number = addition_with_checks(number, data[i + 1])
        print(f"=== Step {i + 1}: {number}")
    return number


def check_answer(homework):
    snailfish_number = complete_homework(homework)
    print(snailfish_number)
    magnitude = calculate_magnitude(snailfish_number)
    return magnitude


homework_magnitude = check_answer(snailfish_homework)
print(f"Homework final sum magnitude: {homework_magnitude}")
