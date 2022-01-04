def convert_input(data):
    data_strip = [i.strip('\n') for i in data]
    starting_positions = {}
    for position in data_strip:
        starting_positions[position[:8]] = int(position[-1])
    return starting_positions
