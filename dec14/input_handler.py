def convert_input(data):
    data_strip = [i.strip('\n') for i in data]
    starting_polymer = data_strip.pop(0)
    pair_data = create_pair_dict(data_strip)

    return starting_polymer, pair_data


def create_pair_dict(data):
    data_split = [i.split(' -> ') for i in data if ' -> ' in i]
    data_dict = {i[0]: i[1] for i in data_split}

    return data_dict
