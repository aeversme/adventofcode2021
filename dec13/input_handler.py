def convert_input(data):
    data_strip = [i.strip('\n') for i in data]
    data_folds = convert_folds(data_strip)
    number_folds = len(data_folds)
    data_coordinates = convert_coordinates(data_strip, number_folds)

    return data_folds, data_coordinates


def convert_folds(data):
    data_folds = [i for i in data if 'fold' in i]
    data_split = [i.split(' ') for i in data_folds]
    data_isolate = [i[2] for i in data_split]
    data_isolate_split = [i.split('=') for i in data_isolate]
    for fold in data_isolate_split:
        fold[1] = int(fold[1])

    return data_isolate_split


def convert_coordinates(data, folds):
    data_filter = list(filter(None, data[:-folds]))
    data_split = [i.split(',') for i in data_filter]
    for coordinates in data_split:
        for i in range(2):
            coordinates[i] = int(coordinates[i])

    return data_split
