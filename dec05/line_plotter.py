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
        range_value = abs(coord_list[1] - coord_list[3])
        x_increment = 0
        y_increment = 1
    elif line_type == "horizontal":
        x_start = min(coord_list[0], coord_list[2])
        y_start = coord_list[1]
        range_value = abs(coord_list[0] - coord_list[2])
        x_increment = 1
        y_increment = 0
    elif line_type == "negative_diag":
        x_start = min(coord_list[0], coord_list[2])
        y_start = max(coord_list[1], coord_list[3])
        range_value = abs(coord_list[0] - coord_list[2])
        x_increment = 1
        y_increment = -1
    else:
        x_start = min(coord_list[0], coord_list[2])
        y_start = min(coord_list[1], coord_list[3])
        range_value = abs(coord_list[0] - coord_list[2])
        x_increment = 1
        y_increment = 1

    for _ in range(range_value + 1):
        plot[y_start][x_start] += 1
        x_start += x_increment
        y_start += y_increment
