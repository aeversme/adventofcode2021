from input_handler import convert_input
from low_point_handler import find_low_points
from basin_handler import discover_basin

with open('heightmap.txt') as h:
    heightmap_raw = h.readlines()


def analyze_map(data_input):
    """
    Takes a set of input data. Generates a heightmap list, finds the low points in the map, discovers the basins
    around each low point, and calculates each basin size. Returns a list of the largest three basins on the map.
    """

    heightmap = convert_input(data_input)

    low_points = find_low_points(heightmap)

    basins = []
    for i in range(len(low_points)):
        basin_size = discover_basin(heightmap, low_points[i][1], low_points[i][2], is_low_point=True)
        basins.append(basin_size)
    biggest_three = sorted(basins)[-3:]
    return biggest_three


biggest_basins = analyze_map(heightmap_raw)
print(f"Product of largest three basins: {biggest_basins[0] * biggest_basins[1] * biggest_basins[2]}")
