from operation_handler import add_numbers, split_number, explode_pair


def check_for_reduction(num):
    num_string = str(num)
    list_level = 0
    reduction_type = None
    reduction_operand = None
    operand_index = None
    for i in range(len(num_string)):
        if num_string[i] == '[' and list_level == 4:
            if num_string[i + 5] != ']':
                if num_string[i + 6] != ']':
                    reduction_operand = num_string[i:i + 8]
                else:
                    reduction_operand = num_string[i:i + 7]
            else:
                reduction_operand = num_string[i:i + 6]
            reduction_type = 'explode'
            operand_index = i
            break
        else:
            if num_string[i] == '[':
                list_level += 1
            elif num_string[i] == ']':
                list_level -= 1
    if reduction_type is None:
        for j in range(len(num_string)):
            if num_string[j].isnumeric() and num_string[j + 1].isnumeric():
                reduction_type = 'split'
                reduction_operand = num_string[j] + num_string[j + 1]
                operand_index = j
                break
    return reduction_type, reduction_operand, operand_index


def addition_with_checks(num1, num2):
    sum_nums = add_numbers(num1, num2)

    sum_copy = sum_nums.copy()
    needs_reduction = True
    while needs_reduction:
        reduction_type, reduction_operand, operand_index = check_for_reduction(sum_copy)
        if reduction_type == 'split':
            # print(f"called split:   {sum_copy} splitting value: {reduction_operand}")
            sum_copy = split_number(sum_copy, reduction_operand)
        elif reduction_type == 'explode':
            # print(f"called explode: {sum_copy} exploding pair: {reduction_operand}")
            sum_copy = explode_pair(sum_copy, reduction_operand, operand_index)
        else:
            # print("No further reductions needed.")
            needs_reduction = False

    return sum_copy
