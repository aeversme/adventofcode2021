from input_handler import convert_input
from alu_handler import process_operation

with open('monad.txt') as m:
    m_raw = m.readlines()
monad = convert_input(m_raw)
print(monad)


def determine_variables(line, var_dict):
    variables = []
    for i in range(1, 3):
        if isinstance(line[i], str):
            variables.append(var_dict[line[i]])
        else:
            variables.append(line[i])

    return tuple(variables)


def validate_number(operations, model_number):
    number_index = 0
    var_dict = {
        'w': 0,
        'x': 0,
        'y': 0,
        'z': 0
    }

    for line in operations:
        if len(line) < 3:
            var_dict[line[1]] = int(model_number[number_index])
            # print(f"w set to {model_number[number_index]}")
            number_index += 1
        else:
            var1, var2 = determine_variables(line, var_dict)
            # print(f"var1: {var1} {type(var1)}, var2: {var2} {type(var2)}")
            var_dict[line[1]] = process_operation(line[0], var1, var2)
        # print(var_dict)

    return var_dict['z']


def get_new_test_number(number):
    new_number = str(int(number) - 1)
    zero_count = new_number.count('0')
    while zero_count > 0:
        new_number = str(int(new_number) - 1)
        zero_count = new_number.count('0')
    return new_number


def test_model_numbers():
    test_number = '55555555555555'
    z = 1

    # z = validate_number(monad, test_number)

    while z != 0:
        z = validate_number(monad, test_number)
        print(f"{test_number} is invalid.")
        test_number = get_new_test_number(test_number)

    print(f"{test_number} is the largest acceptable model number.")

    return z


test_model_numbers()
# test_result = test_model_numbers()
# print(test_result)
