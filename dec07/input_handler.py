def convert_input(data):
    data_list = data.split(',')
    for i in range(len(data_list)):
        data_list[i] = int(data_list[i])
    return data_list
