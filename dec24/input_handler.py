def convert_input(data):
    data_strip = [i.strip('\n') for i in data]
    data_split = [i.split(' ') for i in data_strip]

    conversion_dict = {
        'inp': 0,
        'add': 1,
        'mul': 2,
        'div': 3,
        'mod': 4,
        'eql': 5
    }

    for line in data_split:
        line[0] = conversion_dict[line[0]]
        if len(line) == 3 and not line[2].isalpha():
            line[2] = int(line[2])

    return data_split
