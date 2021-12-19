def add_numbers(num1, num2):
    return [num1, num2]


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
                reduction_type, reduction_operand = check_for_reduction(pair_half, counter, reduction_type)
    return reduction_type, reduction_operand
