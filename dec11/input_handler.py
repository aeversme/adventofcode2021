def convert_input(data):
    data_strip = [i.strip('\n') for i in data]
    data_split = [list(i) for i in data_strip]
    for i in data_split:
        i = [int(j) for j in i]
    return data_split
