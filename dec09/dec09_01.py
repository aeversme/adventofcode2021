from input_handler import convert_input
from edge_corner_handler import check_corner

with open('test-heightmap.txt') as h:
    heightmap_raw = h.readlines()

heightmap = convert_input(heightmap_raw)
print(heightmap)

# conditions:
# if row is min or max, don't check -1 row or +1 row, respectively
# if column (index) is min or max, don't check -1 index or +1 index, respectively
# seems like 8 special cases: 4 corners and the remainder of the 4 edges

# row min index = 0, row max index = len(heightmap) - 1
# column min index = 0, column max index = len(heightmap[0]) -1


def find_low_spots():
    row_min = 0
    row_max = len(heightmap)
    print(f"row_max: {row_max}")
    col_min = 0
    col_max = len(heightmap[0])
    print(f"col_max: {col_max}")

    low_points = []

    for i in range(len(heightmap)):
        for j in range(len(heightmap[0])):
            if i == row_min or i == row_max or j == col_min or j == col_max:
                corner_value = check_corner(heightmap, i, j)
                if corner_value is not None:
                    low_points.append(corner_value)

    print(low_points)


find_low_spots()
