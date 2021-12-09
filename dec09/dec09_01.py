from input_handler import convert_input
from low_point_handler import find_low_points

with open('heightmap.txt') as h:
    heightmap_raw = h.readlines()

heightmap = convert_input(heightmap_raw)
# print(heightmap)


def calc_risk_level():
    """
    Adds one to each low point value to get the risk level, and returns the sum of all the risk levels for the
    heightmap.
    """

    low_points = find_low_points(heightmap)
    risk_level = 0
    for i in low_points:
        risk_level += int(i[0]) + 1
    return risk_level


print(f"The low point risk level of this heightmap is: {calc_risk_level()}")
