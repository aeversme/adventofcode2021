from conversion_handler import hex_to_binary


def convert_input(data):
    data = data.strip()
    binary_packet = ''
    for c in data:
        binary_packet += hex_to_binary[c]
    return binary_packet
