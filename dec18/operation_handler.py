from ast import literal_eval


def add_numbers(num1, num2):
    return [num1, num2]


def split_number(num, operand):
    num_string = str(num)
    first_half = int(operand) // 2
    second_half = int(operand) - first_half
    operand_split = str([first_half, second_half])
    num_string = num_string.replace(operand, operand_split, 1)
    new_num = literal_eval(num_string)
    return new_num


def explode_pair(num, operand, index):
    num_string = str(num)
    operand_literal = literal_eval(operand)
    operand_first = operand_literal[0]
    operand_second = operand_literal[1]

    operand_index = index

    num_string_copy = num_string

    # add left value to next regular number (if any) to the left of the exploding pair
    left_string = ''
    left_num = None
    new_left_string = ''
    for i in range(operand_index - 1, 0, -1):
        left_string = num_string_copy[i] + left_string
        if num_string_copy[i].isnumeric():
            if num_string_copy[i - 1].isnumeric():
                left_string = num_string_copy[i - 1] + left_string
                left_num = num_string_copy[i - 1] + num_string_copy[i]
            else:
                left_num = num_string_copy[i]
            break
    if left_num:
        new_left_num = str(int(left_num) + operand_first)
        new_left_string = left_string.replace(left_num, new_left_num)
        # TODO: conditional about num_string_copy.count(new_left_string + operand)
        # if num_string_copy.count(new_left_string + operand) > 1:
        num_string_copy = num_string_copy[:operand_index - len(left_string)] + new_left_string + \
                          num_string_copy[operand_index:]
        # else:
        #     num_string_copy = num_string_copy.replace(left_string + operand, new_left_string + operand, 1)

        # check for string length difference & modify operand_index
        if len(new_left_string) > len(left_string):
            operand_index += len(new_left_string) - len(left_string)

    # add right value to the next regular number (if any) to the right of the exploding pair
    right_string = ''
    right_num = None
    new_right_string = ''
    for j in range(operand_index + len(operand), len(num_string_copy) - 1):
        right_string += num_string_copy[j]
        if num_string_copy[j].isnumeric():
            if num_string_copy[j + 1].isnumeric():
                right_string += num_string_copy[j + 1]
                right_num = num_string_copy[j] + num_string_copy[j + 1]
            else:
                right_num = num_string_copy[j]
            break
    if right_num:
        new_right_num = str(int(right_num) + operand_second)
        new_right_string = right_string.replace(right_num, new_right_num)
        num_string_copy = num_string_copy.replace(operand + right_string, operand + new_right_string, 1)

    # replace operand with regular number 0
    num_string_copy = num_string_copy.replace(new_left_string + operand + new_right_string,
                                              new_left_string + '0' + new_right_string)

    new_num = literal_eval(num_string_copy)
    return new_num


def calculate_magnitude(num):
    first_half = 0
    second_half = 0
    for i in range(2):
        if type(num[i]) == list:
            num[i] = calculate_magnitude(num[i])
        if i == 0:
            first_half = num[i] * 3
        else:
            second_half = num[i] * 2
    return first_half + second_half
