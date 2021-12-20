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

    new_num_string = num_string

    # add left value to next regular number (if any) to the left of the exploding pair
    left_string = ''
    left_num = None
    new_left_string = ''
    for i in range(operand_index - 1, 0, -1):
        left_string = new_num_string[i] + left_string
        if new_num_string[i].isnumeric():
            if new_num_string[i - 1].isnumeric():
                left_string = new_num_string[i - 1] + left_string
                left_num = new_num_string[i - 1] + new_num_string[i]
            else:
                left_num = new_num_string[i]
            break
    if left_num:
        new_left_num = str(int(left_num) + operand_first)
        new_left_string = left_string.replace(left_num, new_left_num)
        new_num_string = new_num_string.replace(left_string + operand, new_left_string + operand, 1)

        # check for string length difference & modify operand_index
        if len(new_left_string) > len(left_string):
            operand_index += len(new_left_string) - len(left_string)

    # add right value to the next regular number (if any) to the right of the exploding pair
    right_string = ''
    right_num = None
    new_right_string = ''
    for j in range(operand_index + len(operand), len(new_num_string) - 1):
        right_string += new_num_string[j]
        if new_num_string[j].isnumeric():
            if new_num_string[j + 1].isnumeric():
                right_string += new_num_string[j + 1]
                right_num = new_num_string[j] + new_num_string[j + 1]
            else:
                right_num = new_num_string[j]
            break
    if right_num:
        new_right_num = str(int(right_num) + operand_second)
        new_right_string = right_string.replace(right_num, new_right_num)
        new_num_string = new_num_string.replace(operand + right_string, operand + new_right_string, 1)

    # replace operand with regular number 0
    new_num_string = new_num_string.replace(new_left_string + operand + new_right_string,
                                            new_left_string + '0' + new_right_string)

    new_num = literal_eval(new_num_string)
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
