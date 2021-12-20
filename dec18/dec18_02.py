from input_handler import convert_input
from procedure_handler import addition_with_checks
from operation_handler import calculate_magnitude

with open('snailfish.txt') as s:
    snailfish_raw = s.readlines()

snailfish_homework = [convert_input(i) for i in snailfish_raw]


def find_largest_pair_magnitude(data):
    data_length = len(data)
    largest_magnitude = 0
    sums_to_check = []
    for i in range(data_length):
        print(f"Calculating sums for index {i}/{data_length - 1}...")
        x = data[i]
        # print(f"i: {i}, x: {x}")
        for j in range(len(data)):
            if j != i:
                y = data[j]
                # print(f"   j: {j}, y: {y}")
                sum_x_y = addition_with_checks(x, y)
                sums_to_check.append(sum_x_y)
    print("Calculating magnitude of sums...")
    for num in sums_to_check:
        magnitude = calculate_magnitude(num)
        # print(f"   x + y: {magnitude}")
        if magnitude > largest_magnitude:
            # print(f"== Setting largest found magnitude to {magnitude}")
            largest_magnitude = magnitude
    return largest_magnitude


largest_mag = find_largest_pair_magnitude(snailfish_homework)
print(f"The largest magnitude is: {largest_mag}")
