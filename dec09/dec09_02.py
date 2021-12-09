from input_handler import convert_input
from low_point_handler import find_low_points

with open('heightmap.txt') as h:
    heightmap_raw = h.readlines()

heightmap = convert_input(heightmap_raw)
# print(heightmap)
