from operation_handler import add_numbers, split_number, explode_pair


def check_for_reduction(number, count=0, reduction=None):
    counter = count
    reduction_type = reduction
    reduction_operand = None
    if count == 4:
        reduction_type = 'explode'
        reduction_operand = number
    else:
        for pair_half in number:
            if type(pair_half) == int and pair_half > 9:
                reduction_type = 'split'
                reduction_operand = pair_half
            elif type(pair_half) == list and reduction_type is None:
                counter += 1
                reduction_type, reduction_operand, counter = check_for_reduction(pair_half, counter, reduction_type)
    counter -= 1
    return reduction_type, reduction_operand, counter


def addition_with_checks(num1, num2):
    sum_nums = add_numbers(num1, num2)

    sum_copy = sum_nums.copy()
    needs_reduction = True
    while needs_reduction:
        print("Checking if reduction is needed...")
        reduction_type, reduction_operand, _ = check_for_reduction(sum_copy)
        if reduction_type == 'split':
            print(f"Splitting needed on {reduction_operand}...")
            sum_copy = split_number(sum_copy, reduction_operand)
            print(f"after split: {sum_copy}")
        elif reduction_type == 'explode':
            print(f"Explosion needed on {reduction_operand}...")
            sum_copy = explode_pair(sum_copy, reduction_operand)
            print(f"after explode: {sum_copy}")
        else:
            print("No further reductions needed.")
            needs_reduction = False

    return sum_copy
