from ast import literal_eval


def add_numbers(num1, num2):
    return [num1, num2]


def split_number(num, operand):
    num_string = str(num)
    first_half = operand // 2
    second_half = operand - first_half
    operand_split = str([first_half, second_half])
    num_string = num_string.replace(str(operand), operand_split)
    new_num = literal_eval(num_string)
    return new_num


def explode_pair(num, operand):
    num_string = str(num)
    # print(f"starting num_string: {num_string}")
    operand_string = str(operand)
    operand_first = operand[0]
    operand_second = operand[1]

    operand_index = num_string.index(operand_string)
    # print(f"operand_index: {operand_index}")

    new_num_string = num_string

    # add left value to next regular number (if any) to the left of the exploding pair
    left_string = ''
    left_num = None
    new_left_string = ''
    for i in range(operand_index - 1, 0, -1):
        left_string = new_num_string[i] + left_string
        if new_num_string[i].isnumeric():
            left_num = new_num_string[i]
            break
    # print(f"left_string: {left_string}")
    # print(f"left_num: {left_num}")
    if left_num:
        new_left_num = str(int(left_num) + operand_first)
        # print(f"new_l_n: {new_left_num}")
        new_left_string = left_string.replace(left_num, new_left_num)
        # print(f"new_l_s: {new_left_string}")
        new_num_string = new_num_string.replace(left_string + operand_string, new_left_string + operand_string)
        # print(f"left_mod num_string: {num_string}")

        # check for string length difference & modify operand_index
        if len(new_left_string) > len(left_string):
            operand_index += len(new_left_string) - len(left_string)

    # add right value to the next regular number (if any) to the right of the exploding pair
    right_string = ''
    right_num = None
    new_right_string = ''
    for i in range(operand_index + len(operand_string), len(new_num_string) - 1):
        right_string += new_num_string[i]
        if new_num_string[i].isnumeric():
            right_num = new_num_string[i]
            break
    # print(f"right_string: {right_string}")
    # print(f"right_num: {right_num}")
    if right_num:
        new_right_num = str(int(right_num) + operand_second)
        # print(f"new_r_n: {new_right_num}")
        new_right_string = right_string.replace(right_num, new_right_num)
        # print(f"new_r_s: {new_right_string}")
        new_num_string = new_num_string.replace(operand_string + right_string, operand_string + new_right_string)
        # print(f"right_mod num_string: {num_string}")

    # replace operand with regular number 0
    new_num_string = new_num_string.replace(new_left_string + operand_string + new_right_string,
                                            new_left_string + '0' + new_right_string)
    # print(f"final num_string: {num_string}")

    new_num = literal_eval(new_num_string)
    return new_num
