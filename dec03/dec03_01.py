with open('diagnostic.txt') as d:
    diagnostic_codes = d.readlines()

diagnostic_codes = [i.strip('\n') for i in diagnostic_codes]


def gamma(codes):
    gamma_binary = ''
    for i in range(12):
        num_zeros = 0
        num_ones = 0
        for j in range(len(codes)):
            if codes[j][i] == '0':
                num_zeros += 1
            elif codes[j][i] == '1':
                num_ones += 1
            else:
                print('The diagnostic code contained a non-binary bit.')
                return
        if num_zeros > num_ones:
            gamma_binary += '0'
        elif num_ones > num_zeros:
            gamma_binary += '1'
        else:
            print(f'The bit in position {i} has an equal number of zeros and ones.')
            return
    return gamma_binary


def epsilon(gamma_code):
    epsilon_binary = ''
    for i in range(12):
        if gamma_code[i] == '0':
            epsilon_binary += '1'
        else:
            epsilon_binary += '0'
    return epsilon_binary


def binary_to_decimal(binary_number):
    factor = len(binary_number) - 1
    decimal = 0
    for i in range(len(binary_number)):
        decimal += int(binary_number[i]) * (2 ** factor)
        factor -= 1
    return decimal


def power_consumption():
    gamma_binary = gamma(diagnostic_codes)
    print(f"gamma: {gamma_binary}")
    epsilon_binary = epsilon(gamma_binary)
    print(f"epsilon: {epsilon_binary}")
    gamma_rate = binary_to_decimal(gamma_binary)
    print(f"gamma rate: {gamma_rate}")
    epsilon_rate = binary_to_decimal(epsilon_binary)
    print(f"epsilon rate: {epsilon_rate}")
    return gamma_rate * epsilon_rate


print(f"power consumption: {power_consumption()}")
