def find_grid_maximums(coord_list):
    x_list = []
    y_list = []
    for element in coord_list:
        x_list.append(element[0])
        y_list.append(element[1])
    max_x = max(x_list) + 1
    max_y = max(y_list) + 1

    return max_x, max_y


def add_dots(grid, coord_list):
    for element in coord_list:
        grid[element[1]][element[0]] = '#'
    return grid


def create_paper(coord_list):
    max_x, max_y = find_grid_maximums(coord_list)
    grid = [['.'] * max_x for _ in range(max_y)]
    grid_with_dots = add_dots(grid, coord_list)
    return grid_with_dots
