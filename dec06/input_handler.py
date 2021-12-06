def convert_input(data):
    data_list = data.split(',')
    for i in range(len(data_list)):
        data_list[i] = int(data_list[i])
    data_dict = {n: [] for n in range(9)}
    for i in range(9):
        tally = 0
        for j in range(len(data_list)):
            if data_list[j] == i:
                tally += 1
        data_dict[i].append(tally)
    return data_dict
