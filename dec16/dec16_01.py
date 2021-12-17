from input_handler import convert_input
from conversion_handler import binary_to_decimal

with open('test-packet.txt') as p:
    packet_raw = p.read()

binary_packet = convert_input(packet_raw)
print(binary_packet)


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
    version = binary_to_decimal(packet[:3])
    print(f"Version: {version}")
    type_id = binary_to_decimal(packet[3:6])
    print(f"Type ID: {type_id}")
    packet_length = 0
    if type_id == 4:
        literal, bits = literal_value(packet[6:])
        print(f"Literal value: {literal}")
        decoded_length = 6 + bits
        trailing_zeros = 4 - (decoded_length % 4)
        literal_length = decoded_length + trailing_zeros
        if literal_length == len(packet):
            packet_length += literal_length
            return packet_length
        else:
            decode_packet(packet[packet_length:])
    else:
        print("This is an operator packet.")
        print(f"Length type ID: {packet[6]}")
        if packet[6] == 0:
            print("Next 15 bits are a number representing total length in bits of subpackets.")
            subpacket_bits = binary_to_decimal(packet[7:22])
            print(f"Subpacket bits: {subpacket_bits}")
        else:
            print("Next 11 bits are a number representing number of subpackets in this packet.")
            subpacket_number = binary_to_decimal(packet[7:18])
            print(f"Number of subpackets: {subpacket_number}")


length = decode_packet(binary_packet)
print(f"Packet length: {length}")
