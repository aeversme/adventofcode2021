from ast import literal_eval


def convert_input(data):
    data_list = literal_eval(data)
    return data_list
