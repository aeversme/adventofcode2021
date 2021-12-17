from input_handler import convert_input
from conversion_handler import binary_to_decimal

with open('packet.txt') as p:
    packet_raw = p.read()

binary_packet = convert_input(packet_raw)
print(binary_packet)


version_sum = 0
trailing_zeros = 0


def literal_value(binary_string):
    found_last_group = False
    index = 0
    number_string = ''
    while not found_last_group:
        group = binary_string[index:index + 5]
        number_string += group[1:]
        index += 5
        if group[0] == '0':
            found_last_group = True
    literal = binary_to_decimal(number_string)
    return literal, index


def decode_packet(packet):
    global version_sum, trailing_zeros
    print(f"Processing packet string: {packet}")
    if set(packet) == {'0'}:
        print("These are trailing zeros; packet ending.")
        trailing_zeros = len(packet)
        return
    version = binary_to_decimal(packet[:3])
    print(f"Version: {version}")
    version_sum += version
    type_id = binary_to_decimal(packet[3:6])
    # print(f"Type ID: {type_id}")
    if type_id == 4:
        print("This is a literal value packet.")
        literal, bits = literal_value(packet[6:])
        # print(f"Literal value: {literal}")
        decoded_length = 6 + bits
        if decoded_length == len(packet):
            return
        else:
            decode_packet(packet[decoded_length:])
    else:
        print("This is an operator packet.")
        # print(f"Length type ID: {packet[6]}")
        if packet[6] == '0':
            # print("Next 15 bits are a number representing total length in bits of subpackets.")
            subpacket_bits = binary_to_decimal(packet[7:22])
            # print(f"Subpacket(s) bits: {subpacket_bits}")
            decode_packet(packet[22:])
        else:
            # print("Next 11 bits are a number representing number of subpackets in this packet.")
            subpacket_number = binary_to_decimal(packet[7:18])
            # print(f"Number of subpackets: {subpacket_number}")
            decode_packet(packet[18:])
    return


decode_packet(binary_packet)
print(f"\nVersion sum: {version_sum}")
print(f"Trailing zeros: {trailing_zeros}")
