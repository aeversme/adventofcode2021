def convert_input(data):
    data_strip_lines = [i.strip('\n') for i in data]
    data_split = [i.split(' | ') for i in data_strip_lines]
    return data_split
