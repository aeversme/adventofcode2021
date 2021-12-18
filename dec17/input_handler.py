def convert_input(data):
    data_split = data.split(' ')
    target = []
    for i in range(2, 4):
        target_range = data_split[i].split('..')
        target_range[0] = int(target_range[0][2:])
        target_range[1] = int(target_range[1].strip(','))
        target.append(target_range)
    return target

