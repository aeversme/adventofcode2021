from input_handler import convert_input
from conversion_handler import binary_to_decimal
from operation_handler import perform_operation


def throwaway(unused):
    return


verbose = throwaway

with open('packet.txt') as p:
    packet_raw = p.read()

binary_packet = convert_input(packet_raw)
# print(binary_packet)

# version_sum = 0


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
    # global version_sum
    value = 0
    bitcount = 0

    verbose(f"Processing packet string: {packet}")
    # version = binary_to_decimal(packet[:3])
    bitcount += 3
    # print(f"Version: {version}")
    # version_sum += version
    type_id = binary_to_decimal(packet[3:6])
    bitcount += 3
    print(f"Type ID: {type_id}")
    if type_id == 4:
        print("This is a literal value packet.")
        literal, bits = literal_value(packet[6:])
        print(f"Literal value: {literal}")
        value = literal
        bitcount += bits
    else:
        print("This is an operator packet.")
        subpacket_returns = []
        bitcount += 1
        if packet[6] == '0':
            verbose("Next 15 bits are a number representing total length in bits of subpackets.")
            subpacket_bits = binary_to_decimal(packet[7:22])
            bitcount += 15
            verbose(f"Subpacket(s) bits: {subpacket_bits}")
            remaining_bits = subpacket_bits
            cursor = 22
            while remaining_bits > 0:
                subpacket_value, subpacket_bits = decode_packet(packet[cursor:])
                subpacket_returns.append(subpacket_value)
                cursor += subpacket_bits
                bitcount += subpacket_bits
                remaining_bits -= subpacket_bits
        else:
            verbose("Next 11 bits are a number representing number of subpackets in this packet.")
            subpacket_count = binary_to_decimal(packet[7:18])
            bitcount += 11
            verbose(f"Number of subpackets: {subpacket_count}")
            cursor = 18
            for i in range(subpacket_count):
                subpacket_value, subpacket_bits = decode_packet(packet[cursor:])
                subpacket_returns.append(subpacket_value)
                cursor += subpacket_bits
                bitcount += subpacket_bits
        value = perform_operation(type_id, subpacket_returns)
        print(f"Type: {type_id}, Subpacket returns: {subpacket_returns}")
    print(f"Value: {value}, bitcount: {bitcount}")
    return value, bitcount


packet_value, _ = decode_packet(binary_packet)
print(f"\nPacket value: {packet_value}")
