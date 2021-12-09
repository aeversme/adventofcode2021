from edge_corner_handler import check_corner, check_edge


def find_low_points(heightmap):
    """
    Finds low points in the heightmap. If the number at any [row][column] coordinate is lower than the four adjacent
    numbers (diagonals excluded), adds that number to the list of low points. Returns the list of low points.
    """

    row_max = len(heightmap) - 1
    col_max = len(heightmap[0]) - 1

    low_points = []

    for i in range(len(heightmap)):
        for j in range(len(heightmap[0])):
            if i == 0 or i == row_max or j == 0 or j == col_max:
                corner_value = check_corner(heightmap, i, j)
                if corner_value is not None:
                    low_points.append([corner_value, i, j])
                edge_value = check_edge(heightmap, i, j)
                if edge_value is not None:
                    low_points.append([edge_value, i, j])
            else:
                rules = [heightmap[i][j] < heightmap[i - 1][j],
                         heightmap[i][j] < heightmap[i + 1][j],
                         heightmap[i][j] < heightmap[i][j - 1],
                         heightmap[i][j] < heightmap[i][j + 1]]
                if all(rules):
                    # print(f"inner at [{i}][{j}]: {heightmap[i][j]} is smaller than {heightmap[i - 1][j]},
                    # {heightmap[i + 1][j]}, " f"{heightmap[i][j - 1]}, and {heightmap[i][j + 1]}")
                    low_points.append([heightmap[i][j], i, j])
    return low_points
