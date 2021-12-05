# Advent of Code 2021
# December 05, part 1

with open('vent_lines.txt') as v:
    vents = v.readlines()


def convert_input(vent_data):
    vents_strip = [i.strip('\n') for i in vent_data]
    vents_replace = [i.replace(' -> ', ',') for i in vents_strip]
    vents_split = [i.split(',') for i in vents_replace]
    for i in vents_split:
        for j in range(4):
            i[j] = int(i[j])
    return vents_split


def find_max_value(vent_list):
    max_value = 0
    for row in vent_list:
        for element in row:
            if element > max_value:
                max_value = element
    return max_value


def is_line(coord_list):
    return coord_list[0] == coord_list[2] or coord_list[1] == coord_list[3]


def plot_line(coord_list, plot):
    if coord_list[0] == coord_list[2]:
        column = coord_list[0]
        y1 = coord_list[1]
        y2 = coord_list[3]
        mod = 1
        step = 1
        if y1 > y2:
            mod = -1
            step = -1
        for row in range(y1, y2 + mod, step):
            plot[row][column] += 1
    if coord_list[1] == coord_list[3]:
        row = coord_list[1]
        x1 = coord_list[0]
        x2 = coord_list[2]
        mod = 1
        step = 1
        if x1 > x2:
            mod = -1
            step = -1
        for column in range(x1, x2 + mod, step):
            plot[row][column] += 1
    return


def count_overlaps(plot):
    overlap_count = 0
    for row in plot:
        for element in row:
            if element >= 2:
                overlap_count += 1
    return overlap_count


def analyze_vents():
    vents_list = convert_input(vents)
    max_value = find_max_value(vents_list)
    print(vents_list)
    print(max_value)
    plot = [[0] * (max_value + 1) for _ in range(max_value + 1)]
    for vent in vents_list:
        if is_line(vent):
            plot_line(vent, plot)
    # print(plot)
    print(count_overlaps(plot))
    return 0


analyze_vents()
