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
        highest_row_value = max(row)
        if highest_row_value > max_value:
            max_value = highest_row_value
    return max_value


# for diagonal lines, condition is:
# abs(coord_list[2] - coord_list[0]) == abs(coord_list[3] -coord_list[1])
def is_line(coord_list):
    return coord_list[0] == coord_list[2] or coord_list[1] == coord_list[3]


# define a way to plot diagonal lines
def plot_line(coord_list, plot):
    # vertical line
    if coord_list[0] == coord_list[2]:
        x_start = coord_list[0]
        y_start = min(coord_list[1], coord_list[3])
        for _ in range(abs(coord_list[1] - coord_list[3]) + 1):
            plot[y_start][x_start] += 1
            y_start += 1
    # horizontal line
    if coord_list[1] == coord_list[3]:
        x_start = min(coord_list[0], coord_list[2])
        y_start = coord_list[1]
        for _ in range(abs(coord_list[0] - coord_list[2]) + 1):
            plot[y_start][x_start] += 1
            x_start += 1


def count_overlaps(plot):
    overlap_count = 0
    for row in plot:
        for element in row:
            if element >= 2:
                overlap_count += 1
    return overlap_count


# include logic to plot diagonal lines
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
    print(f"Number of vent overlaps: {count_overlaps(plot)}")
    return 0


analyze_vents()
