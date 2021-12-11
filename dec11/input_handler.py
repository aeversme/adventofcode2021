def convert_input(data):
    data_strip = [i.strip('\n') for i in data]
    data_split = [list(i) for i in data_strip]
    for i in data_split:
        for j in range(len(i)):
            i[j] = int(i[j])
    return data_split
