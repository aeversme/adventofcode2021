def convert_input(data):
    data_strip_lines = [i.strip('\n') for i in data]
    data_split = [i.split(' | ') for i in data_strip_lines]
    return data_split


def convert_for_part_two(data):
    """
    Takes a list of strings. Returns two lists of lists of strings.

    Note: the input should be sorted by length, but the output strings must remain in their original order but
    individually sorted alphabetically. A 'sort' value is passed to the split_and_sort() function: 1 = sort,
    0 = do not sort.
    """
    data_strip_lines = [i.strip('\n') for i in data]
    data_split = [i.split(' | ') for i in data_strip_lines]
    data_input = [i[0] for i in data_split]
    data_output = [i[1] for i in data_split]
    return split_and_sort(data_input, 1), split_and_sort(data_output, 0)


def split_and_sort(string_list, sort):
    """
    Takes a list of strings. For each string, splits the string and sorts the resulting strings alphabetically. Sorts
    each list of strings by length. Returns the split and sorted list of strings.
    """
    string_list_split = [i.split(' ') for i in string_list]
    for i in string_list_split:
        for j in range(len(i)):
            i[j] = sorted(i[j])
            i[j] = ''.join(i[j])
        if sort == 1:
            i.sort(key=len)
    return string_list_split
