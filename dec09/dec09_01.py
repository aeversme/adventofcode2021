from input_handler import convert_input
from edge_corner_handler import check_corner, check_edge

with open('heightmap.txt') as h:
    heightmap_raw = h.readlines()

heightmap = convert_input(heightmap_raw)
# print(heightmap)


def find_low_spots():
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
                    low_points.append(corner_value)
                edge_value = check_edge(heightmap, i, j)
                if edge_value is not None:
                    low_points.append(edge_value)
            else:
                rules = [heightmap[i][j] < heightmap[i - 1][j],
                         heightmap[i][j] < heightmap[i + 1][j],
                         heightmap[i][j] < heightmap[i][j - 1],
                         heightmap[i][j] < heightmap[i][j + 1]]
                if all(rules):
                    # print(f"inner at [{i}][{j}]: {heightmap[i][j]} is smaller than {heightmap[i - 1][j]},
                    # {heightmap[i + 1][j]}, " f"{heightmap[i][j - 1]}, and {heightmap[i][j + 1]}")
                    low_points.append(heightmap[i][j])
    return low_points


def calc_risk_level():
    """
    Adds one to each low point value to get the risk level, and returns the sum of all the risk levels for the
    heightmap.
    """

    low_points = find_low_spots()
    risk_level = 0
    for i in low_points:
        risk_level += int(i) + 1
    return risk_level


print(f"The low point risk level of this heightmap is: {calc_risk_level()}")
