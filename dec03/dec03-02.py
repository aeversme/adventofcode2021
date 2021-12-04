with open('diagnostic.txt') as d:
    diagnostic_codes = d.readlines()

diagnostic_codes = [i.strip('\n') for i in diagnostic_codes]
test_codes = ['00100', '11110', '10110', '10111', '10101', '01111', '00111', '11100', '10000', '11001', '00010',
              '01010']


def bit_value_count(codes, index):
    """
    Takes a list of binary codes and an index. Returns the number of zeros and ones at the given index across all codes.
    """
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
    return num_zeros, num_ones


def oxygen(codes):
    """
    Takes a list of binary codes. For each bit (index), keeps only the codes whose value at that index matches the
    'most common' bit for the remaining list of codes. In case of a tie, the 'most common' bit is '1'. Returns the
    last remaining code.
    """
    index = 0
    while len(codes) > 1:
        num_zeros, num_ones = bit_value_count(codes, index)
        if num_zeros > num_ones:
            most_common = '0'
        else:
            most_common = '1'
        codes = [code for i, code in enumerate(codes) if code[index] == most_common]
        index += 1
    return codes[0]


def co2(codes):
    """
    Takes a list of binary codes. For each bit (index), keeps only the codes whose value at that index matches the
    'least common' bit for the remaining list of codes. In case of a tie, the 'least common' bit is '1'. Returns the
    last remaining code.
    """
    index = 0
    while len(codes) > 1:
        num_zeros, num_ones = bit_value_count(codes, index)
        if num_zeros > num_ones:
            least_common = '1'
        else:
            least_common = '0'
        codes = [code for i, code in enumerate(codes) if code[index] == least_common]
        index += 1
    return codes[0]


def binary_to_decimal(binary_number):
    """
    Takes a binary string and returns the equivalent decimal integer.
    """
    factor = len(binary_number) - 1
    decimal = 0
    for i in range(len(binary_number)):
        decimal += int(binary_number[i]) * (2 ** factor)
        factor -= 1
    return decimal


def life_support(codes):
    """
    Takes a list of binary codes and returns the life support rating of the submarine.
    """
    oxygen_generator_rating = oxygen(codes)
    co2_scrubber_rating = co2(codes)
    return binary_to_decimal(oxygen_generator_rating) * binary_to_decimal(co2_scrubber_rating)


print(life_support(diagnostic_codes))
