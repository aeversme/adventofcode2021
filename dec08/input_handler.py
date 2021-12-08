def convert_input(data):
    data_strip_lines = [i.strip('\n') for i in data]
    data_split = [i.split(' | ') for i in data_strip_lines]
    return data_split


def convert_for_part_two(data):
    data_strip_lines = [i.strip('\n') for i in data]
    data_split = [i.split(' | ') for i in data_strip_lines]
    data_input = [i[0] for i in data_split]
    data_input_sas = split_and_sort(data_input, 10)
    data_output = [i[1] for i in data_split]
    data_output_sas = split_and_sort(data_output, 4)
    return data_input_sas, data_output_sas


def split_and_sort(string_list, r):
    string_list_split = [i.split(' ') for i in string_list]
    for i in string_list_split:
        for j in range(r):
            i[j] = sorted(i[j])
            i[j] = "".join(i[j])
    return string_list_split
