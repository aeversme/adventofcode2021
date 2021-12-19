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
                reduction_type, reduction_operand, counter = check_for_reduction(pair_half, counter, reduction_type)
    counter -= 1
    return reduction_type, reduction_operand, counter


# TODO: have this take the entire 'number', change to string, manipulate, and perform literal_eval()
def split_number(num, operand):
    first_half = num // 2
    second_half = num - first_half
    return [first_half, second_half]


# TODO: make this work
def explode_pair(num, operand):
    # str(num)
    # str(operand)
    # find index of operand in num_string
    # split operand
    # add left value to next regular number (if any) to the left of the exploding pair
    # add right value to the next regular number (if any) to the right of the exploding pair
    # perform literal_eval() on new num_string
    pass
