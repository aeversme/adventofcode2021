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


def check_line_type(coord_list):
    x1 = coord_list[0]
    x2 = coord_list[2]
    y1 = coord_list[1]
    y2 = coord_list[3]
    if x1 == x2:
        return "vertical"
    elif y1 == y2:
        return "horizontal"
    elif abs(x1 - x2) == abs(y1 - y2):
        if (x1 < x2 and y1 > y2) or (x1 > x2 and y1 < y2):
            return "negative_diag"
        else:
            return "positive_diag"
    else:
        return None


def plot_line(line_type, coord_list, plot):
    if line_type == "vertical":
        x_start = coord_list[0]
        y_start = min(coord_list[1], coord_list[3])
        for _ in range(abs(coord_list[1] - coord_list[3]) + 1):
            plot[y_start][x_start] += 1
            y_start += 1
    elif line_type == "horizontal":
        x_start = min(coord_list[0], coord_list[2])
        y_start = coord_list[1]
        for _ in range(abs(coord_list[0] - coord_list[2]) + 1):
            plot[y_start][x_start] += 1
            x_start += 1
    elif line_type == "positive_diag":
        x_start = min(coord_list[0], coord_list[2])
        y_start = min(coord_list[1], coord_list[3])
        for _ in range(abs(coord_list[0] - coord_list[2]) + 1):
            plot[y_start][x_start] += 1
            x_start += 1
            y_start += 1
    else:
        x_start = min(coord_list[0], coord_list[2])
        y_start = max(coord_list[1], coord_list[3])
        for _ in range(abs(coord_list[0] - coord_list[2]) + 1):
            plot[y_start][x_start] += 1
            x_start += 1
            y_start -= 1


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
    # print(vents_list)
    # print(max_value)
    plot = [[0] * (max_value + 1) for _ in range(max_value + 1)]
    for vent in vents_list:
        line_type = check_line_type(vent)
        if line_type is not None:
            plot_line(line_type, vent, plot)
    # print(plot)
    print(f"Number of vent overlaps: {count_overlaps(plot)}")
    return 0


analyze_vents()
