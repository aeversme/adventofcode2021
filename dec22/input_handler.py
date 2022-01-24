def convert_input(data):
    data = [i.strip('\n') for i in data]
    data = [i.split(' ') for i in data]

    for line in data:
        line[1] = line[1].split(',')
        line[1] = [i.strip('xyz=') for i in line[1]]
        line[1] = [i.split('..') for i in line[1]]
        for j in range(3):
            line[1][j] = [int(k) for k in line[1][j]]

    return data
