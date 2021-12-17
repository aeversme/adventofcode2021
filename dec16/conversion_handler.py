hex_to_binary = {
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'A': '1010',
    'B': '1011',
    'C': '1100',
    'D': '1101',
    'E': '1110',
    'F': '1111'
}


def binary_to_decimal(binary_number):
    factor = len(binary_number) - 1
    decimal = 0
    for i in range(len(binary_number)):
        decimal += int(binary_number[i]) * (2 ** factor)
        factor -= 1
    return decimal
