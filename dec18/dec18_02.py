from input_handler import convert_input
from procedure_handler import addition_with_checks, check_for_reduction
from operation_handler import calculate_magnitude

with open('snailfish.txt') as s:
    snailfish_raw = s.readlines()

snailfish_homework = [convert_input(i) for i in snailfish_raw]


def find_largest_pair_magnitude(data):
    largest_magnitude = 0
    first_number = None
    second_number = None
    for i in range(len(data) - 1):
        x = data[i]
        print(f"i: {i}, x: {x}")
        for j in range(len(data) - 1):
            if j != i:
                y = data[j]
                print(f"   j: {j}, y: {y}")
                sum_x_y = addition_with_checks(x, y)
                magnitude = calculate_magnitude(sum_x_y)
                print(f"   x + y: {magnitude}")
                if magnitude > largest_magnitude:
                    print(f"== Setting largest found magnitude to {magnitude}")
                    largest_magnitude = magnitude
                    first_number = x
                    second_number = y
    return largest_magnitude, first_number, second_number


largest_mag, first_num, second_num = find_largest_pair_magnitude(snailfish_homework)
print(f"The largest magnitude is: {largest_mag}\nfrom {first_num} + {second_num}")

# num1 = [[[[5, 2], 2], 5], 5]
# num2 = [38, 123]
#
# sum_nums = addition_with_checks(num1, num2)
# print(sum_nums)
#
# mag = calculate_magnitude(sum_nums)
# print(mag)

# explode on second '[5, 6]' at index 40
# num3 = [[[9, [5, 6]], [[8, 8], [0, 9]]], [[[9, [5, 6]], 15], [[8, 3], 8]]]
#
# print(check_for_reduction(num3))

# should be [[[9, [5, 6]], [[8, 8], [0, 9]]], [[[14, 0], 21], [[8, 3], 8]]]
