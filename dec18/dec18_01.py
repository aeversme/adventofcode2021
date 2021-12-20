from input_handler import convert_input
from procedure_handler import addition_with_checks, check_for_reduction
from operation_handler import split_number, explode_pair

with open('test-snailfish.txt') as s:
    snailfish_raw = s.readlines()

snailfish_homework = [convert_input(i) for i in snailfish_raw]


def complete_homework(data):
    number = data[0]
    for i in range(len(data) - 1):
        number = addition_with_checks(number, data[i + 1])
        print(f"=== Step {i + 1}: {number}")
    return number


snailfish_number = complete_homework(snailfish_homework)
print(snailfish_number)

# num1 = [[[[12, 12], [6, 14]], [[15, 0], [17, [8, 1]]]], [2, 9]]
# print(check_for_reduction(num1))


# num1 = [[[0, [4, 5]], [0, 0]], [[[4, 5], [2, 6]], [9, 5]]]
# num2 = [7, [[[3, 7], [4, 3]], [[6, 3], [8, 8]]]]
#
# sum_nums = addition_with_checks(num1, num2)
# print(sum_nums)

# num1 = [[[0, [6, 6]], [0, [6, 7]]], [[[7, [6, 7]], [0, 6]], [[7, 8], [16, 0]]]]
#
# new_num = explode_pair(num1, '[8, 1]', 38)
# print(new_num)

# num1 = [[[[4, 0], [5, 4]], [[7, 7], [6, 0]]], [[8, 9], [[11, 9], [11, 0]]]]
#
# new_num = split_number(num1, '11')
# print(new_num)
