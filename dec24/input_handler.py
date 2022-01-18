def convert_input(data):
    data_strip = [i.strip('\n') for i in data]
    data_split = [i.split(' ') for i in data_strip]
    return data_split
