with open('diagnostic.txt') as d:
    diagnostic_codes = d.readlines()

diagnostic_codes = [i.strip('\n') for i in diagnostic_codes]
test_codes = ['00100', '11110', '10110', '10111', '10101', '01111', '00111', '11100', '10000', '11001', '00010',
              '01010']


def most_common_value(codes, index):
    num_zeros = 0
    num_ones = 0
    for i in range(len(codes)):
        if codes[i][index] == '0':
            num_zeros += 1
        elif codes[i][index] == '1':
            num_ones += 1
        else:
            print('Error: the diagnostic code contained a non-binary bit.')
            return
    if num_zeros > num_ones:
        most_common = '0'
    elif num_ones > num_zeros:
        most_common = '1'
    else:
        most_common = 'tie'
    return most_common


def least_common_value(codes, index):
    num_zeros = 0
    num_ones = 0
    for i in range(len(codes)):
        if codes[i][index] == '0':
            num_zeros += 1
        elif codes[i][index] == '1':
            num_ones += 1
        else:
            print('Error: the diagnostic code contained a non-binary bit.')
            return
    if num_zeros > num_ones:
        least_common = '1'
    elif num_ones > num_zeros:
        least_common = '0'
    else:
        least_common = 'tie'
    return least_common


def oxygen(codes):
    index = 0
    while len(codes) > 1:
        most_common = most_common_value(codes, index)
        if most_common == 'tie':
            most_common = '1'
        codes = [code for i, code in enumerate(codes) if code[index] == most_common]
        index += 1
    return codes[0]


def co2(codes):
    index = 0
    while len(codes) > 1:
        least_common = least_common_value(codes, index)
        if least_common == 'tie':
            least_common = '0'
        codes = [code for i, code in enumerate(codes) if code[index] == least_common]
        index += 1
    return codes[0]


def binary_to_decimal(binary_number):
    factor = len(binary_number) - 1
    decimal = 0
    for i in range(len(binary_number)):
        decimal += int(binary_number[i]) * (2 ** factor)
        factor -= 1
    return decimal


def life_support():
    oxygen_generator_rating = oxygen(diagnostic_codes)
    co2_scrubber_rating = co2(diagnostic_codes)
    return binary_to_decimal(oxygen_generator_rating) * binary_to_decimal(co2_scrubber_rating)


print(life_support())
